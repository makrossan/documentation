---
title: "Actualiza Portainer manualmente"
date: 2025-09-13T19:37:27.000Z
slug: actualiza-portainer-manualmente
---

- Pare el contenedor

``` bash
docker stop portainer
```

- Remueva el contenedor

``` bash
docker rm portainer
```

- Actualice la nueva imagen

``` bash
docker pull portainer/portainer-ee
```

- Recree el contenedor de Portainer usando el ejemplo del comando abajo

``` bash
PORTAINER-CE
sudo docker run -d \
  -p 8000:8000 \
  -p 9000:9000 \
  -p 9443:9443 \
  --name=portainer \
  --restart=always \
  --pull=always \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v /home/user/docker/portainer_data:/data \
  portainer/portainer-ce:latest
```

Si instala Portainer-EE. Cierre sesión en Portainer (si ya está
conectado) y luego vuelva a iniciar sesión. Cuando inicie sesión por
primera vez, se le pedirá que ingrese su clave de licencia.

## Actualiza Portainer desde Portainer

A partir de la versión 2.19, los usuarios de Business Edition pueden
actualizar su instalación de Portainer directamente desde Portainer.
Para hacerlo, haga clic en el enlace Actualizar ahora en la notificación
de actualización en la parte inferior izquierda de la interfaz de
usuario de Portainer.
