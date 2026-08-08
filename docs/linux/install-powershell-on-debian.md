---
title: "Debian - Como installar PowerShell"
date: 2025-09-13T23:58:37.000Z
slug: como-installar-powershell
---

**Inicia PowerShell:**  

``` bash
pwsh
```

**Instala PowerShell:**  

``` bash
sudo apt-get install -y powershell
```

**Actualiza la lista de paquetes:**  

``` bash
sudo apt-get update
```

**Importa las claves GPG del repositorio de Microsoft:**  

``` bash
wget -q https://packages.microsoft.com/config/debian/12/packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb
```

Reemplaza `debian/12` en la URL con la versión apropiada de tu
distribución de Debian (por ejemplo, `debian/9`, `debian/10`,
`debian/11`, etc.).

Una vez instalado, puedes iniciar PowerShell escribiendo `pwsh` en tu
terminal.
