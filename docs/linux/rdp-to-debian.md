---
title: "RDP a Debian"
date: 2025-09-13T23:58:18.000Z
slug: rdp-a-debian
---

En el siguiente ejemplo se demuestra como hacer una conexion rdp a un
dispositivo con distro basada en debian.

1.  por si estan usando KDE   
      
2.  ahora puedes hacer conexiones rdp a una maquina linux.

si usas el firewall del os, asegurate de que el puerto 3389 es
accesible.  

``` bash
sudo ufw allow 3389/tcp
```

  

habilita XRDP para iniciar cuando el sistema operativo arranca.   

``` bash
sudo systemctl enable xrdp
```

  

instala XRDP.  

``` bash
sudo apt-get install xrdp -y
```

  

si no tienes desktop instalado.   

``` bash
sudo apt-get install ubuntu-desktop
```

  

actualiza la libreria  

``` bash
sudo apt-get update
```

  
