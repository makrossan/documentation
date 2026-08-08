---
title: "Como ocultar la hora y la fecha en la bandeja de Windows con PowerShell"
date: 2025-09-13T23:36:22.000Z
slug: como-ocultar-la-hora-y-la-fecha-en-la-bandeja-de-windows-con-powershell
---

Para ocultar la hora y la fecha en la bandeja del sistema en Windows
usando PowerShell, puedes usar el siguiente comando:

``` powershell
Set-ItemProperty `
  -Path "HKLM:\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" `
  -Name "HideClock" `
  -Value 1

Stop-Process `
  -Name "explorer" `
  -Force
```

Este comando establece el valor del registro \`HideClock\` en 1, lo que
oculta el reloj en la bandeja del sistema, y luego reinicia el proceso
Explorer para aplicar los cambios.

Si deseas mostrar la hora y la fecha nuevamente, puedes usar el
siguiente comando para revertir los cambios:

``` powershell
Remove-ItemProperty `
  -Path "HKLM:\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" `
  -Name "HideClock"

Stop-Process `
  -Name "explorer" `
  -Force
```

Este comando elimina el valor del registro \`HideClock\`, lo que
restaura la visualización del reloj en la bandeja del sistema.
