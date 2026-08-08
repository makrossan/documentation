---
title: "Error de permisos en subida de archivos en WordPress dentro de un contenedor Docker"
date: 2025-09-13T19:38:48.000Z
slug: error-de-permisos-en-subida-de-archivos-en-wordpress-dentro-de-un-contenedor-docker
---

Si el contenedor Docker de WordPress esta mapeado a un volumen
personalizado, es posible que el problema esté relacionado con los
permisos en la carpeta mapeada en su sistema host, es decir, en
`/home/${USER}/volumendocker/wordpress/`.

Muchas recomendaciones en linea indicar que los permisos deberia ser
configurados a 755, pero a mi solo me funciono despues de configurarlos
a 777. 

### Pasos para Resolver:

**Verifique los Permisos en el Sistema Host**:

- Asegúrese de que el usuario bajo el cual se ejecuta el contenedor
  Docker tiene los permisos necesarios para escribir en la carpeta
  mapeada. Puede hacerlo cambiando los permisos con el siguiente comando
  en su host:  
  `bash chmod -R 777 /home/${USER}/volumendocker/wordpress/wp-content/uploads`
- Si es necesario, también asegúrese de que el propietario del
  directorio es el usuario correcto. Por ejemplo, si Docker se ejecuta
  bajo un usuario específico, puede cambiar la propiedad con:  
  `bash chown -R <docker_user>:<docker_user> /home/${USER}/volumendocker/wordpress/wp-content/uploads`

**Verifique la Configuración de Volúmenes en Docker**:

- Asegúrese de que el volumen está correctamente montado y que los
  cambios en el sistema host se reflejan dentro del contenedor. Puede
  verificarlo entrando en el contenedor y revisando los permisos en la
  carpeta `/var/www/html/wp-content/uploads`:  
  `bash docker exec -it <nombre_del_contenedor> /bin/bash`  
  `ls -l /var/www/html/wp-content/uploads`  
- Esto le permitirá ver si los permisos y la propiedad en el contenedor
  son correctos. En caso contrario, ejecute el comando aqui usando el
  camino por defecto del
  contenedor. `chmod -R 755 /var/www/html/wp-content/uploads`  

**Reinicie el Contenedor**:

- Si ha realizado cambios en los permisos o la configuración, puede ser
  útil reiniciar el contenedor Docker para asegurarse de que los cambios
  se aplican correctamente:  
  `bash docker restart <nombre_del_contenedor>`

Si después de realizar estos pasos sigue teniendo problemas, puede ser
útil revisar los logs del contenedor Docker para ver si hay algún otro
error adicional que pueda estar afectando las subidas.
