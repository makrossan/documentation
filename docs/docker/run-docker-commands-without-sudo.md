---
title: "Ejecuta comandos Docker sin usar sudo"
date: 2025-09-13T17:43:59.000Z
slug: ejecuta-comandos-docker-sin-usar-sudo
---

Si quieres evitar usar el comando sudo siempre que corres el comando
docker, necesitas agregar el usuario al grupo docker.

``` bash
sudo usermod -aG docker ${USER}
```

Para aplicar la membresia al nuevo grupo.

su – \${USER}

Confirma que el grupo fue agregado

``` bash
groups
```

En caso de que este haciendo esto para un colega, o sea el usuario que
quieres agregar no es con el que entro al host, usa el siguiente
comando. (donde “dockerusername” es el nombre del usuario a quien le
haces el favor)

``` bash
sudo usermod -aG dockerusername
```
