---
title: "Proxmox dejó de responder al ping, y la única forma de recuperarlo fue desconectar el cable Ethernet y volver a conectarlo."
date: 2025-09-13T23:42:15.000Z
slug: proxmox-dejo-de-responder-al-ping-y-la-unica-forma-de-recuperarlo-fue-desconectar-el-cable-ethernet-y-volver-a-conectarlo
---

Si Proxmox dejó de responder al ping y solo se recuperó después de
desconectar y volver a conectar físicamente el cable Ethernet,
probablemente se trate de un problema relacionado con la red (por
ejemplo, un fallo en el controlador de la NIC, un problema con la
concesión de DHCP, un fallo en la negociación del enlace, etc.).

### Revise los registros del sistema alrededor del momento de la interrupción.

Commando:

``` bash
journalctl --since "20:15" --until "20:25"
```

o mas ampliamente:

``` bash
journalctl -xe
```

Busque entradas relacionadas con:

- networkd, systemd-networkd, NetworkManager o ifupdown
- e1000e, igb, r8169 u otros controladores de tarjetas de red (NIC)
- mensajes como *link is down*, *carrier lost*, *eth0*, *enpXsY*, etc.
- dhclient, pérdida de concesión de IPv4, *timeout*

en mi caso:

``` bash
Jun 05 08:32:23 desklab rrdcached[1104]: handle_request_update: Could not read RRD file.
Jun 05 08:32:23 desklab pmxcfs[1117]: [status] notice: RRDC update error 
/var/lib/rrdcached/db/pve2-node/desklab: -1
Jun 05 08:32:23 desklab pmxcfs[1117]: [status] notice: RRD update error 
/var/lib/rrdcached/db/pve2-node/desklab: mmaping file 
'/var/lib/rrdcached/db/pve2-node/desklab': Invalid argument
Jun 05 08:32:24 desklab kernel: e1000e 0000:00:1f.6 enp0s31f6: Detected Hardware Unit Hang:
                                  TDH                  <b1>
                                  TDT                  <5f>
                                  next_to_use          <5f>
                                  next_to_clean        <b0>
                                buffer_info[next_to_clean]:
                                  time_stamp           <14ce53dcb>
                                  next_to_watch        <b1>
                                  jiffies              <14ce65201>
                                  next_to_watch.status <0>
                                MAC Status             <40080083>
                                PHY Status             <796d>
                                PHY 1000BASE-T Status  <3800>
                                PHY Extended Status    <3000>
                                PCI Status             <10>
.......................
Jun 05 08:33:03 desklab kernel: e1000e 0000:00:1f.6 enp0s31f6: NIC Link is Down
Jun 05 08:33:03 desklab kernel: vmbr0: port 1(enp0s31f6) entered disabled state
Jun 05 08:33:03 desklab rrdcached[1104]: handle_request_update: Could not read RRD file.
Jun 05 08:33:03 desklab pmxcfs[1117]: [status] notice: RRDC update error 
/var/lib/rrdcached/db/pve2-node/desklab: -1
Jun 05 08:33:03 desklab pmxcfs[1117]: [status] notice: RRD update error
/var/lib/rrdcached/db/pve2-node/desklab: 
mmaping file '/var/lib/rrdcached/db/pve2-node/desklab': Invalid argument
```

### **Que muestran los registros?** 

| **Hora** | **Evento** |
|----|----|
| 08 : 32 : 23 | Comienza el *spam* de “e1000e … Detected Hardware Unit Hang” ⇒ la tarjeta Intel I219-V se congela y no puede transmitir/recibir. |
| 08 : 32 : 23 | <span class="s1">rrdcached</span>/<span class="s1">pmxcfs</span> empiezan a fallar al hacer *mmap* de los archivos RRD – Proxmox no puede escribir los gráficos de rendimiento porque la NIC ya está detenida. |
| 08 : 33 : 03 | El controlador finalmente se rinde → Enlace de red (NIC) caído → el puerto <span class="s1">vmbr0</span> se deshabilita. A partir de este punto, Proxmox queda fuera de la red hasta que se desconectó y volvió a conectar el cable (o hasta que el controlador reinició la tarjeta). |

El volcado de registros repetitivo (TDH/TDT/jiffies/PHY Status) es la
clásica firma del *unit-hang* de e1000e, documentada en el bug \#118721
del kernel de Linux y en múltiples reportes de errores de distintas
distribuciones.

Por lo tanto, el problema no está relacionado con el cable o el switch;
se trata del conocido error de firmware de e1000e/I219-V que reaparece
en ciertos núcleos (kernels) y configuraciones de ahorro de energía.

------------------------------------------------------------------------

### **Por que pasa esto con las NIC I219-V?**

- Las rutas de ahorro de energía (EEE y PCIe ASPM) a veces dejan el
  transmit ring en un estado no válido.
- La descarga de paquetes grandes (TSO/GSO/GRO) también puede activarlo
  bajo carga.
- Una vez que se presenta el fallo, solo un reinicio completo del enlace
  o volver a conectar el cable soluciona la condición.

------------------------------------------------------------------------

### **Soluciones que funcionan en la práctica**

| **Impacto** | **Acción** | **Cómo hacerlo** |
|----|----|----|
| **Mínimo (pruebe primero)** | Desactivar los dos ahorros de energía que más suelen causar el cuelgue | \`\`\`bash\n# un solo comando\nprintf ‘options e1000e EEE=0 AspmSupport=0\n’ |
| Bajo | Desactivar los offloads pesados | bash\nethtool -K enp0s31f6 tso off gso off gro off\n<span class="s1"> (añádalo en </span>/etc/network/interfaces<span class="s1"> con </span>post-up<span class="s1"> si soluciona el problema).</span> |
| Medio | Instalar el último driver externo de Intel (3.8.7) o cambiar al kernel más nuevo de Proxmox | Pasos detallados en el mensaje anterior; cualquiera reemplaza la versión con errores dentro del kernel. |
| Radical | Evitar por completo la I219-V | Instalar una tarjeta PCIe basada en Intel i350 / 82576, muy estable y totalmente soportada. |

> **Buena práctica: después de aplicar una solución, deje una terminal
> root monitoreando el driver durante un día:  
> `journalctl -k -f | grep -E "e1000e|NIC Link"`  
> Si pasan 24 h sin Hardware Unit Hang, el problema está resuelto.**

------------------------------------------------------------------------

### **(Opt.) Red de seguridad automática**

Mientras verifica la solución, cree un pequeño watchdog que reinicie la
interfaz cuando los pings a su puerta de enlace fallen. Así evita caídas
totales y genera un registro que luego puede revisar.

A continuación verá **dos archivos** que necesita crear y cómo
activarlos para que su servidor compruebe la conectividad y, si se
pierde, reinicie la interfaz de red automáticamente.

#### **1. Script que hace el chequeo**

Guárdelo como **/usr/local/sbin/net-watch** y déle permisos de
ejecución.

``` bash
#!/usr/bin/env bash
IF="enp0s31f6"           # nombre de la interfaz
GATEWAY="192.168.1.1"    # puerta de enlace a la que hará ping
Envía 2 pings; si fallan, baja y sube la interfaz
```

``` bash
chmod +x /usr/local/sbin/net-watch
```

#### **2. Servicio systemd**

Cree **/etc/systemd/system/net-watch.service** con este contenido:

``` bash
[Unit]
Description=Comprueba la puerta de enlace y reinicia la NIC si no responde
```

#### **3. Temporizador systemd**

Para que el chequeo se ejecute cada minuto (puede cambiar el intervalo),
cree

**/etc/systemd/system/net-watch.timer**:

``` bash
[Unit]
Description=Ejecuta net-watch cada minuto
[Timer]
OnCalendar=--* ::00
AccuracySec=30s
Persistent=true
```

#### **4. Activar todo**

``` bash
# Recargar los archivos de systemd
systemctl daemon-reload
Habilitar y arrancar el temporizador ahora mismo
```

- **`systemctl status net-watch.timer`** le mostrará si el temporizador
  está activo y cuándo correrá de nuevo.
- **`journalctl -u net-watch.service -f`** permitirá ver en tiempo real
  los reinicios de la NIC (si ocurren).

Con esto, Proxmox comprobará la conectividad cada minuto y recuperará la
interfaz automáticamente si el NIC vuelve a colgarse.

------------------------------------------------------------------------

## **Visión a largo plazo**

La I219-V es una tarjeta de red económica; si el host es de misión
crítica, la solución definitiva es instalar una tarjeta PCIe basada en
Intel i350-T2/T4 o un 82576. Esa familia no comparte la base de código
e1000e y es extremadamente estable bajo cargas elevadas.
