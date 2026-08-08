---
title: "ESXi - Synology ABB - VMware - CBT is not enabled on VM"
date: 2025-09-13T23:40:01.000Z
slug: synology-abb-vmware-cbt-is-not-enabled-on-vm
---

<figure class="kg-card kg-image-card">
<img src="__GHOST_URL__/content/images/2025/09/image.png"
class="kg-image" loading="lazy"
srcset="__GHOST_URL__/content/images/size/w600/2025/09/image.png 600w, __GHOST_URL__/content/images/2025/09/image.png 934w"
sizes="(min-width: 720px) 720px" width="934" height="138" />
</figure>

El mensaje indica que el seguimiento de bloques cambiados (CBT) no está
habilitado en la máquina virtual debido a un problema de licencia. La
máquina virtual llamada "vSDA" no soporta CBT por este problema. Se te
aconseja habilitar manualmente la función de CBT en el hipervisor.

Para resolver este problema, deberás revisar las configuraciones del
hipervisor para asegurarte de que la licencia permita el uso de CBT. Si
la licencia no es suficiente, puede que necesites actualizarla. Una vez
resuelto el problema de licencia, puedes habilitar CBT para la máquina
virtual, ya sea a través de la interfaz de administración del hipervisor
o utilizando comandos o herramientas específicas proporcionadas por la
plataforma del hipervisor (como ESXi, por ejemplo).

1\. **Acceda a la Interfaz Web de ESXi**

2\. **Apague la Máquina Virtual**

3\. **Edite la Configuración de la Máquina Virtual**:

• Una vez que la máquina virtual esté apagada, haga clic en la pestaña
**Editar** (Edit) o en **Ajustes de la VM** (VM Options) dentro de la
vista de la máquina virtual.

• Seleccione **Opciones VM** (VM Options) en el menú de la izquierda.

• Desplácese hacia abajo hasta encontrar **Opciones avanzadas**
(Advanced Options) y haga clic en **Editar parámetros de configuración**
(Edit Configuration Parameters).

4\. **Agregue Parámetros de CBT**:

• En la ventana de **Parámetros de Configuración**, haga clic en
**Agregar fila** (Add Row).

• Añada los siguientes parámetros y valores:

• ctkEnabled = TRUE

• scsi0:0.ctkEnabled = TRUE

• Si la máquina tiene más de un disco, agregue una línea similar para
cada uno, reemplazando scsi0:0 con el identificador correspondiente del
disco (por ejemplo, scsi0:1).

5\. **Guarde los Cambios**:

• Una vez que haya ingresado todos los parámetros, haga clic en
**Aceptar** (OK) para guardar los cambios.

6\. **Encienda la Máquina Virtual**:

• Después de guardar los cambios, encienda la máquina virtual desde la
interfaz web.

7\. **Verifique la Configuración**:

• Para asegurarse de que CBT está habilitado, puede revisar si se han
creado archivos .ctk en el datastore de la máquina virtual. Esto se
puede hacer navegando al datastore correspondiente y buscando los
archivos .ctk en el directorio de la VM.
