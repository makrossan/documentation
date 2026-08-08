---
title: "$ docker-compose up -d -bash: docker-compose: command not found"
date: 2025-09-13T19:35:01.000Z
slug: docker-compose-up-d-bash-docker-compose-command-not-found
---

El mensaje "docker-compose: comando no encontrado" indica que Docker
Compose no está instalado en su sistema. Deberá instalarlo para
continuar. Así es como puede instalar Docker Compose en un sistema
Linux:

### Instalar Docker Compose en Linux

**Verificar la instalación**: Comprueba si Docker Compose se instaló
correctamente verificando su versión:bash

``` bash
docker-compose --version
```

**Establecer los permisos**: Después de descargarlo, necesitas
establecer permisos de ejecución en el binario:bash

``` bash
sudo chmod +x /usr/local/bin/docker-compose
```

**Descargar el binario de Docker Compose**: Usa el siguiente comando
para descargar la versión más reciente de Docker Compose. Reemplaza
`1.29.2` por la versión más actual si es necesario:bash

``` bash
sudo curl -L "https://github.com/docker/compose/releases/download/v2.23.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

Esto debería mostrar la versión de Docker Compose, confirmando que está
instalado correctamente.
