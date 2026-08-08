---
title: "Solución Rápida para el Problema de Actualización de tu Repositorio Debian"
date: 2025-09-13T23:49:08.000Z
slug: solucion-rapida-para-el-problema-de-actualizacion-de-tu-repositorio-debian
---

Cuando se executa el comando "apt update" el siguiente error aparece. 

``` bash
The repositor 'cdrom://[Debian GNU/Linux 12.4.0 _Bookworm_ - Official amd64 
DVD Binary-1 with firmware 20231210-17:57] bookworm release’ does not have a Release file.
N: Updating from such a repository can't be done securely, and is therefore disabled by default.
N: See apt-secure(8) manpage for repository creation and user configuration details.
```

Para resolver este problema, edite el archivo "/etc/apt/sources.list"
usando nano. 

``` bash
sudo nano /etc/apt/sources.list
```

Seguidamente busque la línea que se parece al error de repositorio de
CD-ROM. Comenzará con deb cdrom:*\[Debian GNU/Linux....* Ponga un \# al
inicio de esta línea. Esto lo comenta y le dice a su sistema: "Oye, no
usemos esto".

Si su lista de fuentes parece un poco vacía, agregue los repositorios en
línea oficiales de Debian. Aquí hay una línea de ejemplo que puede
agregar para Debian Bookworm:

``` bash
deb http://deb.debian.org/debian/ bookworm main contrib non-free
```

Presione "Ctrl + O", luego Enter para guardar los cambios. "Ctrl + X" te
saca del editor nano e intenta "apt udpate" nuevamente.
