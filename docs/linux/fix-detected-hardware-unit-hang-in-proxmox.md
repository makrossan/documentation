---
title: "Cómo diagnostiqué y resolví el problema “Detected Hardware Unit Hang” en Proxmox"
date: 2025-12-11T15:57:22.000Z
slug: como-diagnostique-y-resolvi-el-problema-detected-hardware-unit-hang-en-proxmox
---

## **1. Descripción del problema**

En las últimas semanas noté que mi servidor Proxmox perdía la conexión
de red de forma intermitente. Nunca le tomé importancia porque
fácilmente se resolvía desconectando el cable Ethernet del patch panel y
reconectándolo inmediatamente. Pero conforme más intensa era la
utilización de la red, más frecuente se presentaba este problema.

Lo extraño es que la IP nunca cambiaba y la ruta tampoco se perdía. El
servidor **no parecía “caerse”**, pero sí dejaba de pasar tráfico. Esto
indicaba un problema **a nivel de NIC o driver**, no de configuración.

El verdadero problema apareció al revisar los logs del kernel:

Proxmox estaba registrando una falla constante del driver Intel
**e1000e**, acompañada del mensaje:

``` bash
e1000e 0000:00:1f.6 enp0s31f6: Detected Hardware Unit Hang
```

Este mensaje confirma que la tarjeta de red Intel integrada **se queda
colgada a nivel de hardware**, causando microcortes que afectan toda la
comunicación.

------------------------------------------------------------------------

## **2. Cómo encontré la causa**

### **2.1 Verifiqué si el servidor realmente perdía su IP o su default gateway**

Ejecuté:

``` bash
ip -4 addr show
ip route show
```

La IP seguía siendo la misma y el default gateway estaba correcto. Esto
descartaba DHCP, fallas en el bridge o en la configuración de red.

------------------------------------------------------------------------

### **2.2 Revisé si la interfaz estaba cayéndose físicamente**

Busqué eventos de cambios de link:

``` bash
dmesg -T | grep -iE "link is down|reset|timeout|e1000e"
```

Y ahí apareció la verdadera causa:

``` bash
Detected Hardware Unit Hang
```

Este mensaje es **un bug reconocido en los NIC Intel I219-V/I219-LM**,
muy común en mini PC y placas base modernas.

El kernel repetía el error cada 2 segundos, confirmando que el
controlador estaba entrando en un ciclo de recuperación interminable.

------------------------------------------------------------------------

### **2.3 Validé que el tráfico pasaba por el NIC problemático**

La interfaz afectada era:

``` bash
enp0s31f6
```

Y el proxmox bridge vmbr0 dependía totalmente de ella:

``` bash
iface vmbr0 inet static
    bridge-ports enp0s31f6
```

Esto explicaba por qué toda la red se congelaba aunque las virtuales y
contenedores siguieran vivos.

------------------------------------------------------------------------

## **3. La solución definitiva**

El problema es causado por dos funciones de ahorro de energía en los NIC
Intel:

1.  **EEE (Energy Efficient Ethernet)**
2.  **ASPM (Active State Power Management)**

Ambas hacen que el chip se “duerma” y el driver e1000e registre el
famoso **hardware unit hang**.

### **3.1 Desactivar EEE (obligatorio)**

Primero apliqué el cambio temporal:

``` bash
ethtool --set-eee enp0s31f6 eee off
```

Luego lo hice permanente:

``` bash
echo 'ETHTOOL_OPTS="--set-eee enp0s31f6 eee off"' > /etc/default/ethtool
```

Y agregué un servicio systemd:

``` bash
cat <<EOF > /etc/systemd/system/disable-eee.service
[Unit]
Description=Disable EEE on Intel NIC
After=network-online.target

[Service]
Type=oneshot
ExecStart=/usr/sbin/ethtool --set-eee enp0s31f6 eee off

[Install]
WantedBy=multi-user.target
EOF

systemctl enable disable-eee.service
```

------------------------------------------------------------------------

### **3.2 Desactivar ASPM (obligatorio)**

Edite /etc/default/grub:

``` bash
nano /etc/default/grub
```

Y modifiqué esta línea:

``` bash
GRUB_CMDLINE_LINUX_DEFAULT="quiet pcie_aspm=off"
```

Luego regeneré el grub:

``` bash
update-grub
```

Y reinicié el servidor:

``` bash
reboot
```

------------------------------------------------------------------------

## **4. Cómo validar que la solución funcionó**

Después del reinicio verifiqué:

### **EEE desactivado**

``` bash
ethtool --show-eee enp0s31f6
```

Debe mostrar:

``` bash
EEE status: disabled
```

### **Sin nuevos errores en el kernel**

``` bash
dmesg | grep e1000e
```

No deben aparecer más mensajes de:

``` bash
Detected Hardware Unit Hang
```

------------------------------------------------------------------------

## **5. Diagnostico encontrado**

Este es un problema común en hardware reciente que usa NIC Intel
integrados, especialmente en mini PC, placas base económicas y
servidores compactos. La buena noticia es que la solución es definitiva
y completamente estable.
