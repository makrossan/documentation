---
title: "Cómo instalar controladores manualmente (Windows 10/11 y Windows Server)"
date: 2025-09-29T14:51:14.000Z
slug: como-instalar-controladores-manualmente-windows-10-11-y-windows-server
---

Guía práctica y **compacta**: comandos cortos que evitan el scroll
horizontal. Incluye instalación por INF, forzar controladores genéricos,
habilitar Wi‑Fi en Server 2019, bloqueo de reemplazos por Windows Update
y verificación.

------------------------------------------------------------------------

## **Antes de empezar**

- **Ejecute como Administrador.** Abra PowerShell/CMD con privilegios
  elevados.
- **Identifique el hardware.** devmgmt.msc → dispositivo → Propiedades →
  Detalles → *Identificadores de hardware*.
- **Descargue el driver correcto.** OEM (HP/Dell/Lenovo) o fabricante
  del chipset (AMD/Intel/NVIDIA/Realtek). Si el .exe no soporta su SO,
  **extraiga** y use el .inf.
- (Opcional) **Punto de restauración** antes de cambios.

### **Nota sobre continuación de línea en PowerShell**

Use el **acento grave** (backtick) \` al **final de la línea** para
partir comandos largos. No deje espacios después del backtick. También
puede usar **continuación implícita** dentro de (), \[\], {} o
**splatting** con hashtables; en esta guía hemos aplicado backticks para
mantener los comandos cortos y legibles.

------------------------------------------------------------------------

## **Método 1 — Instalación por INF (recomendado)**

### **Vía GUI**

1.  Administrador de dispositivos → clic derecho → **Actualizar
    controlador**.
2.  **Buscar software en el equipo** → **Elegir en una lista** → **Usar
    disco…**.
3.  Seleccione la carpeta con el .inf → Siguiente → reinicie si se
    solicita.

### **Vía CLI (PnPUtil)**

Use una variable corta para la ruta.

``` Powershell
$drv = 'C:\\Drivers\\MiDispositivo'
pnputil `
  /add-driver "$drv\\*.inf" `
  /subdirs `
  /install
# Si lo ejecuta directamente desde el directorio no necesita variable:
pnputil /add-driver *.inf /subdirs /install
```

> pnputil agrega el paquete al DriverStore e instala el que coincida con
> sus HW‑IDs.

------------------------------------------------------------------------

## **Método 2 — Forzar un controlador genérico de Microsoft**

**SATA/AHCI (SSD SATA):**

- Administrador de dispositivos → **Controladoras IDE ATA/ATAPI** → su
  controlador → **Actualizar** → **Elegir en una lista** → **Standard
  SATA AHCI Controller (Microsoft)**.

**NVMe (si aplica):**

- Administrador de dispositivos → **Controladoras de almacenamiento** →
  controlador NVMe → **Standard NVM Express Controller (Microsoft)**.

**Gráficos:**

- Evite **Microsoft Basic Display Adapter** instalando el driver del
  fabricante (ver Método 1).

------------------------------------------------------------------------

## **Wi‑Fi en Windows Server 2019**

Habilite la característica y el servicio, luego instale el INF.

``` Powershell
Install-WindowsFeature Wireless-Networking
Restart-Computer
Set-Service WlanSvc -StartupType Automatic
Start-Service WlanSvc
```

Instale el driver Wi‑Fi (paquete Win10 x64 del fabricante):

``` Powershell
$wifi = 'C:\\Drivers\\WiFi'
pnputil `
  /add-driver "$wifi\\*.inf" `
  /subdirs `
  /install
# Si lo ejecuta directamente desde el directorio no necesita variable:
pnputil /add-driver *.inf /subdirs /install
```

Conectar por perfil XML (si no usa GUI):

``` Powershell
$xml = 'C:\wifi\MiSSID.xml'
netsh wlan add profile filename="$xml" user=all
netsh wlan connect name="MiSSID" interface="Wi-Fi"
```

## **Verificación**

- **Administrador de dispositivos:** sin iconos amarillos; el nombre
  debe coincidir con el del fabricante o el genérico elegido.
- **PowerShell:**

``` Powershell
Get-PnpDevice -PresentOnly
| Where-Object { $_.Class -in @('Display','Net','SCSIAdapter','HDC','Media') }
| Format-Table -AutoSize FriendlyName, Class, Status
```

- **Gráficos:** dxdiag → pestaña *Pantalla* debe mostrar el driver del
  fabricante (no “Microsoft Basic Render Driver”).
- **Wi‑Fi:** netsh wlan show interfaces.

------------------------------------------------------------------------

## **Reversión / Desinstalación**

- **Revertir (GUI):** dispositivo → Propiedades → **Controlador** →
  **Revertir al controlador anterior**.
- **Quitar paquete (PnPUtil):**

``` Powershell
pnputil /enum-drivers | findstr /i ".inf"
# Identifique, p. ej. oem47.inf
pnputil /delete-driver oem47.inf /uninstall /force /reboot
```

------------------------------------------------------------------------

## **Problemas comunes**

- **El instalador dice “SO no soportado”.** Extraiga y use el .inf con
  pnputil.
- **BSOD tras driver de almacenamiento.** Use **Standard SATA
  AHCI**/**Standard NVM Express** y bloquee el HW‑ID problemático.
- **Wi‑Fi no aparece en Server 2019.** Aplique Wireless-Networking,
  reinicie e instale el INF.

------------------------------------------------------------------------

## **Buenas prácticas**

- Prefiera drivers del **OEM** o **chipset**.
- Mantenga una carpeta con **versiones probadas**.
- Actualice **BIOS/UEFI** y **firmware** cuando el fabricante lo
  recomiende.
- Documente qué versión funciona para **repetir** en reinstalaciones.

------------------------------------------------------------------------

## **Apéndice: comandos útiles**

``` Powershell
Get-NetAdapter | ft Status,Name,InterfaceDescription
pnputil /enum-drivers
pnputil /add-driver "C:\Drivers\**\*.inf" /subdirs /install
Install-WindowsFeature Wireless-Networking
netsh wlan connect name="MiSSID" interface="Wi-Fi"
```

> **Última revisión:** 29 de septiembre de 2025.
