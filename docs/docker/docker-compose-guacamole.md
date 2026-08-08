---
title: "docker-compose - Guacamole"
date: 2025-09-13T19:37:04.000Z
slug: docker-compose-guacamole
---

A continuación un ejemplo de archivo \`docker-compose.yml\` que ejecuta
Guacamole junto con el proxy \`guacd\` y una base de datos MySQL.

Recuerde personalizar las contrasenhas del ejemplo. 

``` bash
services:
guacamole-mysql:
image: mysql:latest
container_name: guacamole-mysql
environment:
MYSQL_ROOT_PASSWORD: password_root
MYSQL_DATABASE: guacamole_db
MYSQL_USER: guacamole_user
MYSQL_PASSWORD: password_db
volumes:
- mysql_data:/var/lib/mysql
networks:
- guacamole-network
guacd:
image: guacamole/guacd
container_name: guacd
networks:
- guacamole-network
guacamole:
image: guacamole/guacamole
container_name: guacamole
environment:
MYSQL_DATABASE: guacamole_db
MYSQL_USER: guacamole_user
MYSQL_PASSWORD: password_db
MYSQL_HOSTNAME: guacamole-mysql
GUACD_HOSTNAME: guacd   # Añadido para especificar el contenedor guacd
ports:
- "8080:8080"
depends_on:
- guacd
- guacamole-mysql
networks:
- guacamole-network
networks:
guacamole-network:
driver: bridge
```

##### Pasos para ejecutar con Docker Compose

1\. Cree un archivo \`docker-compose.yml\` en el servidor.  
2. Copie el contenido anterior en el archivo.  
3. Ejecute el siguiente comando en el mismo directorio donde está el
archivo \`docker-compose.yml\`:

`docker-compose up -d`

##### Acceder a Guacamole 

Una vez que los contenedores estén en funcionamiento, puede acceder a
Guacamole desde un navegador en
\`http://\<ip-del-servidor\>:8080/guacamole\`.

Las credenciales por defecto son:  
- **Usuario**: \`guacadmin\`  
- **Contraseña**: \`guacadmin\`
