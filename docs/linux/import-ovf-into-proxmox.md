---
title: "Importar OVF en Proxmox"
date: 2025-09-27T13:30:23.000Z
slug: importar-ovf-en-proxmox
---

## Resumen del escenario

- **VMID:** 800
- **Almacenamiento:** datastore2
- **Nodo Proxmox (IP):** 10.11.11.15
- **Ruta temporal para importación en el
  nodo:** `/var/lib/vz/imports/kace`
- **Archivos de origen en su
  equipo:** `VK1000_14_1_101_1T.ovf`, `VK1000_14_1_101_1T-disk-0.vmdk`, `VK1000_14_1_101_1T.mf`

## Requisitos

- Acceso SSH al nodo Proxmox (`root@10.11.11.15`).
- Paquete OVF/VMDK/MF del SMA disponible en su Mac/Linux.
- Puente de red en Proxmox (por ejemplo, `vmbr0`); si usa VLAN, conocer
  el *tag* correspondiente.
- Espacio libre suficiente en el almacenamiento de destino
  (**datastore2**). La build de ejemplo es de ~1 TB.
- Conectividad de red para que el appliance obtenga IP por DHCP (o plan
  para configurarla manualmente).

### 0) (Opcional) Verificar espacio en el almacenamiento

En el nodo Proxmox, asegúrese de que datastore2 tenga ~1 TB libre.

``` bash
pvesm status
```

## Pasos detallados

### 1) Subir los archivos al nodo

En el nodo (crear carpeta de importación)

``` bash
ssh root@10.11.11.15
mkdir -p /var/lib/vz/imports/kace
```

Desde su Mac/Linux (en la carpeta donde están OVF/VMDK/MF)

<figure class="kg-card kg-code-card">
<div class="sourceCode" id="cb1"><pre
class="sourceCode bash"><code class="sourceCode bash"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">scp</span> VK1000_14_1_101_1T<span class="pp">*</span> root@10.11.11.15:/var/lib/vz/imports/kace/</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a><span class="fu">rsync</span> <span class="at">-av</span> <span class="at">--progress</span> VK1000_14_1<span class="pp">*</span> root@10.11.11.15:/var/lib/vz/imports/kace/</span></code></pre></div>
<figcaption><p><span style="white-space: pre-wrap;">Si el tamaño del
archivo es muy grande, es preferible que use
RSYNC</span></p></figcaption>
</figure>

Verificar en el nodo, debería ver los tres archivos allí.

``` bash
ssh root@10.11.11.15
ls -lh /var/lib/vz/imports/kace
```

### 2) Importar el OVF en Proxmox (crea la VM y convierte el disco)

Sintaxis: qm importovf \<ruta .ovf\>

``` bash
qm importovf 800 /var/lib/vz/imports/kace/VK1000_14_1_101_1T.ovf datastore2
```

Esto crea la VM 800 y coloca el disco convertido en datastore2.

### 3) Configurar hardware (NIC, SCSI, arranque, CPU/RAM, nombre)

NIC en su bridge principal (ajuste vmbr/VLAN; agregue ,tag= si usa VLAN)

<figure class="kg-card kg-code-card">
<div class="sourceCode" id="cb1"><pre
class="sourceCode bash"><code class="sourceCode bash"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="ex">qm</span> set 800 <span class="at">--net0</span> e1000,bridge=vmbr0</span></code></pre></div>
<figcaption><p><span style="white-space: pre-wrap;">ejemplo con NIC
e1000</span></p></figcaption>
</figure>

<figure class="kg-card kg-code-card">
<div class="sourceCode" id="cb1"><pre
class="sourceCode bash"><code class="sourceCode bash"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="ex">qm</span> set 800 <span class="at">--net0</span> vmxnet3,bridge=vmbr0,mac=52:52:00:AB:CD:EF</span></code></pre></div>
<figcaption><p><span style="white-space: pre-wrap;">ejemplo con NIC
vmxnet3 y MAC asignado manualmente</span></p></figcaption>
</figure>

Controladora SCSI + orden de arranque (SMA/FreeBSD funciona muy bien con
VirtIO-SCSI)

``` bash
qm set 800 --scsihw virtio-scsi-pci --boot order=scsi0
```

Firmware: SeaBIOS es un valor seguro para BSD

``` bash
qm set 800 --bios seabios
```

Rendimiento (ajuste según su entorno)

``` bash
qm set 800 --cpu host --sockets 1 --cores 2 --memory 16384
```

Nombre descriptivo

``` bash
qm set 800 --name SMA
```

¿Usa VLAN? Ejemplo con VirtIO y tag 10

``` bash
qm set 800 --net0 virtio,bridge=vmbr0,tag=10
```

### 4) Iniciar y obtener IP/URL

``` bash
qm start 800
```

Abra la Consola de la VM 800 en Proxmox.

En el primer arranque, el appliance mostrará la IP/URL (por defecto usa
DHCP).

Ingrese a esa URL para ejecutar el Asistente de configuración inicial
(EULA, contraseñas, red, etc.).

### Verificación

- En Proxmox, confirme que la tarea de *importovf* terminó sin errores
  (panel de Tareas).
- Compruebe el estado de la VM: `qm status 800`.
- Desde otra máquina, haga `ping` a la IP que muestra la consola del
  SMA.
- Abra la URL del SMA en el navegador y complete el asistente inicial.
- Dentro del SMA, verifique que la hora, red y DNS sean correctos
  (evitar problemas de activación/descargas).

``` bash
# Ejemplos
qm status 800
ping <IP-asignada-al-SMA>
# Desde un equipo con curl:
curl -I http://<IP-o-FQDN-del-SMA>
```

## Problemas frecuentes y soluciones

### Sin DHCP / sin IP

Si no obtiene IP por DHCP, asegurese de usar e1000 o e1000e y manualment
configure la red. Por el momento VirtIO no es soportado.

### Integridad (hash) no coincide

Si el `sha1sum` del VMDK no coincide con el manifiesto `.mf`, vuelva a
descargar/copiar los archivos antes de importar.

``` bash
# En el nodo
cd /var/lib/vz/imports/kace
echo "== Manifest =="
cat VK1000_14_1_101_1T.mf
echo "== SHA1 del VMDK =="
sha1sum VK1000_14_1_101_1T-disk-0.vmdk
# Confirme que el hash que figura en el .mf coincide con el del VMDK.
```

### Permiso denegado al copiar por SCP

Verifique credenciales y conectividad. Asegúrese de que la
carpeta `/var/lib/vz/imports/kace` exista y tenga permisos adecuados.

### Compatibilidad de plataforma

Quest no declara Proxmox como plataforma oficialmente soportada. Para
laboratorio funciona muy bien, pero el soporte del fabricante podría
solicitar reproducir el problema en un hipervisor soportado
(ESXi/Hyper‑V/Azure/Nutanix).
