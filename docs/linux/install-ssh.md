---
title: "Instalar SSH"
date: 2025-09-14T00:04:18.000Z
slug: instalar-ssh
---

Para instalar el servidor SSH en Ubuntu, puedes usar el siguiente
comando en la terminal:

`sudo apt updatesudo apt install openssh-server`

Esto instalará el servidor SSH y lo iniciará automáticamente. Puedes
verificar si el servicio está funcionando correctamente con el siguiente
comando:

`sudo systemctl status ssh`

Si necesitas habilitar o deshabilitar el servicio de SSH para que se
inicie automáticamente al arrancar el sistema, puedes usar los
siguientes comandos:

- Para habilitar:`sudo systemctl enable ssh`
- Para deshabilitar:`sudo systemctl disable ssh`

Una vez instalado, puedes conectarte a tu máquina desde otro equipo
mediante un cliente SSH, usando el comando `ssh usuario@dirección_ip`
desde la terminal del otro equipo.

 

 

*`sudo apt update && sudo apt upgrade`*
