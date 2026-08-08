---
title: "Instala Docker en macOS"
date: 2025-09-13T17:42:19.000Z
slug: instala-docker-en-macos
---

Al igual que en Windows, para instalar Docker en macOS, tambien podemos
utilizar Docker Desktop.  
Aquí te dejo los pasos para instalar Docker Desktop en macOS:

### Requisitos

- Se recomienda tener al menos una de las ultimas 2 versiones de macOS.
  Mas información
  [aqui](https://docs.docker.com/desktop/install/mac-install/).
- La virtualización debe estar habilitada, lo cual es estándar en la
  mayoría de las Macs modernas.

### Pasos para la instalación

1.  Descarga Docker Desktop para macOS desde el sitio oficial de
    Docker:  
    <https://www.docker.com/products/docker-desktop>. 
2.  **Instalar Docker Desktop**:
    - Abre el archivo `.dmg` que descargaste y arrastra el ícono de
      Docker a la carpeta de Aplicaciones.
    - Abre Docker desde tu carpeta de Aplicaciones. La primera vez que
      lo abras, macOS te pedirá confirmación para abrir la aplicación
      descargada de Internet.
3.  **Proporcionar permisos**:
    - Docker te pedirá permisos para instalar una nueva herramienta de
      ayuda y necesitarás tu contraseña para continuar. Es posible que
      también necesites permisos de administrador.
    - Si tu sistema tiene habilitado el chip de seguridad, te pedirá
      permiso para acceder a él. Acepta para permitir que Docker
      funcione correctamente.
4.  **Verifica la instalación**:
    - Una vez completada la instalación y otorgados los permisos
      necesarios, verás el ícono de Docker en la barra de menú superior,
      indicando que Docker se está ejecutando.
    - Puedes hacer clic en el ícono para ver el estado de Docker y
      acceder a las preferencias.

### Post-instalación

Después de instalar Docker Desktop, es una buena práctica verificar que
todo funcione correctamente ejecutando un contenedor de prueba. Puedes
hacerlo abriendo una terminal y ejecutando: `docker run hello-world`

Este comando descargará una imagen de prueba y ejecutará un contenedor
basado en ella. Si la instalación fue exitosa, verás un mensaje en la
terminal indicando que Docker está funcionando correctamente.

Para obtener la documentación más detallada y actualizada, visita la
guía oficial de instalación de Docker Desktop para macOS en
<https://docs.docker.com/desktop/mac/install/>.

Si quieres aprender a instalar tu primera aplicacion, te recomiendo un
video de la siguiente [lista en
YouTube](https://libreria.greivinvenegas.com/Docker%20https:/www.youtube.com/playlist?list=PLM3kkICu9CaiVy8fN03nYkJBWrTSWd4Xt). 
