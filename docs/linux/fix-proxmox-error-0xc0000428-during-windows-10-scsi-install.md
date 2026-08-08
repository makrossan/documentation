---
title: "Proxmox - Error 0xc0000428 - Instalacion Windows 10 SCSI"
date: 2025-09-13T23:41:33.000Z
slug: proxmox-error-0xc0000428-instalacion-windows-10-scsi
---

En mi caso tuve el error despues de instalar Windows 10 en Proxmox
usando un Boot Environment atraves de PXE. 

> Código de error: 0xc0000428  
> “No se pudo cargar el sistema operativo porque no se pudo verificar la
> firma digital de un archivo o una de sus dependencias.”  
> Archivo: \Windows\System32\drivers\vioscsi.sys

Esto me ocurrio porque estoy usando SCSI arrancar y usando controladores
que no están firmados o no son de confianza por Secure Boot.

------------------------------------------------------------------------

### Resolución

#### Opción 1

**Desactive Secure Boot** en las configuraciones OVMF (UEFI):

- Inicie la VM y entre en el menú UEFI (normalmente con Esc o F2).
- Vaya a **Device Manager \> Secure Boot Configuration**.
- Establezca **Secure Boot** como **Disabled**.
- Guarde y salga.

> Esto permite que Windows cargue controladores no firmados como VirtIO
> sin bloquearlos.

#### Opción 2 

Use un disco IDE temporalmenteSi desea evitar usar VirtIO durante la
instalación:

- Cambie el tipo de disco de scsi a ide o sata en la configuración de la
  VM.
- Instale Windows 10.
- Después de instalar, agregue los controladores VirtIO y luego cambie
  de nuevo a scsi para mejor rendimiento.
