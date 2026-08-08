---
title: "Instalar autokey en Ubuntu 24.04 LTS"
date: 2025-09-13T23:44:23.000Z
slug: instalar-autokey-en-ubuntu-24-04-lts
---

Segund el github the autokey, al correr el comando de APT para su
instalacion, el mismo ya instala las dependencias, pero a mi eso no me
funciono. Por lo que procederemos a instalar la dependencias manualmente
una por una segun [este
documento. ](https://github.com/autokey/autokey/blob/master/apt-requirements.txt)

``` bash
sudo apt-get update && sudo apt-get install -y \
  dbus \
  python3-dbus \
  libdbus-1-dev \
  libpython3-dev \
  libdbus-glib-1-dev \
  libgirepository1.0-dev \
  wmctrl \
  gir1.2-gtk-3.0 \
  gir1.2-gtksource-3.0 \
  gir1.2-appindicator3-0.1 \
  gir1.2-glib-2.0 \
  gir1.2-notify-0.7 \
  python3-gi \
  zenity \
  kdialog \
  pyqt5-dev-tools \
  x11-xserver-utils
```

Antes de continuar con la instalacion, es importante asegurarnos que
ubuntu este ejecutando `xorg`, en lugar de `wayland`,  de lo contrario
autokey no funcionara correctamente. 

Para determinar si tu sistema Ubuntu está ejecutando Xorg o Wayland, use
el siguiente comando:

`echo $XDG_SESSION_TYPE`

Este comando mostrará \`x11\` si estás usando Xorg, o \`wayland\` si
estás usando Wayland.

Despues de confirmar que cumplimos con los requisitos, para instalar
autokey, use el siguiente comando: 

`sudo apt update`  
`sudo apt install autokey-gtk`  

- Personalmente, prefiero gtk, pero qt tambien puede ser instalado con
  este comando:

`sudo apt install autokey-qt`  
