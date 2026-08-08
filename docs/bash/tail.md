---
title: "Tail"
date: 2025-09-14T00:03:40.000Z
slug: tail
---

En esta guía, aprenderás cómo usar el comando tail. Usar tail es una
manera sencilla de mostrar los finales de archivos, por ejemplo, al
analizar registros y otros archivos de texto que cambian con el tiempo.
También puede combinarse con otras herramientas para un monitoreo
selectivo y en tiempo real. Al realizar tareas administrativas en tu
Linode, tail es una de las herramientas más útiles disponibles.

- Ingresa el comando tail, seguido por el archivo que te gustaría ver:

`tail /var/quest/kace/user/KAgent.log `

Esto imprimirá las últimas diez líneas del archivo /var/log/auth.log en
la salida de tu terminal.

- Para cambiar el número de líneas mostradas, usa la opción -n:

`tail -n 50 /var/quest/kace/user/KAgent.log `

En este ejemplo, se mostrarán las últimas 50 líneas, pero puedes
modificar este número para mostrar tantas o tan pocas líneas como
necesites.

- Para mostrar una salida en tiempo real, de un archivo que está
  cambiando, usa las opciones -f o --follow:

`tail -f /var/quest/kace/user/KAgent.log `

Esto imprimirá el final del archivo en tu pantalla y lo actualizará a
medida que el archivo cambie. Por ejemplo, puedes usar esta opción con
/var/log/auth.log (en sistemas Debian y Ubuntu) para mostrar tu registro
de acceso en tiempo real. Esto se ejecutará como un proceso en primer
plano, así que para cancelarlo, presiona CTRL+C.

- Tail incluso puede combinarse con otras herramientas como grep para
  filtrar los resultados:

`tail /var/quest/kace/user/KAgent.log  | grep 127.0.0.1`

Este comando buscaría las últimas diez líneas de tu registro de acceso y
solo mostraría aquellas que contienen la dirección IP 198.51.100.1.
También puedes aplicar opciones a tail para mostrar más o menos líneas,
ver los resultados filtrados en tiempo real y más.
