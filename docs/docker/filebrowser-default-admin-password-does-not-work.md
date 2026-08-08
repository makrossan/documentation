---
title: "La contraseña admin/admin por defecto en Filebrowser no funciona."
date: 2025-09-13T19:39:32.000Z
slug: la-contrasena-admin-admin-por-defecto-en-filebrowser-no-funciona
---

En la imagen oficial de filebrowser/filebrowser, el **único usuario
incorporado es admin, pero la contraseña se genera aleatoriamente la
primera vez que se inicia el contenedor** y solo se muestra una vez en
los registros del contenedor. Si vuelve a crear el contenedor sin
mantener la base de datos SQLite, FileBrowser entra nuevamente en “modo
primera ejecución”, genera una nueva contraseña y no podrá iniciar
sesión con la anterior. Para evitar esto, monte la base de datos (y
opcionalmente el settings.json) en una ruta persistente en el host o en
un volumen nombrado. Si prefiere usar una contraseña fija, puede
establecer FB_USER y FB_PASSWORD (o usar el CLI) la primera vez.

------------------------------------------------------------------------

## **1. ¿Cuál es el usuario y contraseña por defecto?**

| **Imagen / versión** | **Usuario** | **Contraseña en el primer inicio** |
|----|----|----|
| Imagen oficial Alpine / S6 (v2.x) | admin | **Cadena aleatoria mostrada una sola vez en logs** |
| Algunas guías antiguas o no oficiales | admin | admin |

**¿Dónde encontrar la contraseña aleatoria?**

``` bash
docker logs <nombre_del_contenedor> | grep -i "generated password"
```

Si ya no aparece, puede restablecer la contraseña desde dentro del
contenedor:

``` bash
docker exec -it <nombre_del_contenedor> filebrowser users update admin --password NUEVAPASS
```

------------------------------------------------------------------------

## **2. ¿Por qué se reinicia la contraseña cada vez que actualizo?**

1.  **FileBrowser guarda los usuarios y configuraciones en un solo
    archivo SQLite** (/database/filebrowser.db o /database.db, según la
    imagen).
2.  Si actualiza la imagen o recrea el contenedor y **no ha montado ese
    archivo en un volumen persistente**, Docker crea una capa nueva de
    archivos vacía. FileBrowser no encuentra la base de datos y vuelve a
    generarla desde cero con nueva contraseña aleatoria.

------------------------------------------------------------------------

## **3. ¿Cómo mantener el acceso después de actualizar?**

Ejemplo docker-compose.yml:

``` bash
services:
  filebrowser:
    image: filebrowser/filebrowser:latest   # o especifique una versión fija
    container_name: filebrowser
    ports:
      - "8080:80"
    environment:
      - PUID=1000
      - PGID=1000
      # Opcional: defina credenciales fijas al crear por primera vez la DB
      - FB_USER=admin
      - FB_PASSWORD=SuperSecreta123
    volumes:
      - /srv/files:/srv
      - /opt/filebrowser/filebrowser.db:/database/filebrowser.db
      - /opt/filebrowser/settings.json:/config/settings.json  # Opcional
    restart: unless-stopped
```

- Montar /database/... y /config/... asegura que **los usuarios,
  contraseñas y la configuración de interfaz** se mantengan incluso al
  actualizar el contenedor.
- Fijar el tag de imagen (v2.36.3, por ejemplo) evita cambios
  inesperados.
- Si usa herramientas como Watchtower, use etiquetas para controlar
  cuándo actualizar.

------------------------------------------------------------------------

## **4. Cambiar o restablecer la contraseña del admin**

| **Método** | **Comando** |
|----|----|
| Desde el host | docker exec -it filebrowser filebrowser users update admin --password NUEVAPASS |
| Con variables de entorno (una vez) | -e FB_USER=admin -e FB_PASSWORD=NUEVAPASS |
| Desde la interfaz web | *Usuarios → Editar* |

------------------------------------------------------------------------

## **5. Consejos adicionales**

- Haga una **copia de seguridad** de filebrowser.db; es pequeña y
  contiene todo.
- Asegúrese de que los permisos en el host sean correctos (chown
  1000:1000) para que el contenedor pueda escribir en el archivo.
- Use variables PUID y PGID para que el contenedor se ejecute como su
  usuario del host (mejor seguridad).
- Puede poner FileBrowser detrás de Traefik (que usted ya usa), para
  añadir HTTPS y protección adicional con middlewares.

------------------------------------------------------------------------

### **Resumen**

*El usuario siempre es admin; la contraseña es aleatoria (imagen
oficial) o admin (guías antiguas). El motivo por el que “pierde” el
acceso es porque la base de datos desaparece cuando el contenedor se
reinicia sin una capa persistente. Monte ese archivo o defina sus
propias credenciales una vez, y no volverá a tener este problema.*
