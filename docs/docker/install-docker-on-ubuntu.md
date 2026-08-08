---
title: "Instala Docker en Ubuntu"
date: 2025-09-13T17:42:56.000Z
slug: instala-docker-en-ubuntu
---

Para la nueva version de Docker hay varios cambios que impactan bastante
la forma tradicional de instalacion.

Algunas distro de Linux pueden tener paquetes no oficiales de Docker en
sus repositorios. Segun la [documentacion
oficial](https://docs.docker.com/engine/install/ubuntu/), hay que
remover paquetes relacionados y desinstalar versiones antiguas o
conflictivas con Docker Engine.

Los paquetes que podrían necesitar ser desinstalados incluyen:

- `docker.io`
- `docker-compose`
- `docker-doc`
- `podman-docker`

Para desinstalar los paquetes conflictivos, puedes ejecutar el siguiente
comando en la terminal:

``` bash
for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do sudo apt-get remove $pkg; done
```

### Ubuntu

1.  **Actualiza tu sistema**:*`sudo apt update && sudo apt upgrade -y`*
2.  **Instala certificados y herramienta de transferencia de
    datos**:*`sudo apt-get install ca-certificates curl`*
3.  **Crea un directorio seguro para llaves de repositorios
    APT:***`sudo install -m 0755 -d /etc/apt/keyrings`*
4.  **Descarga y guarda la clave GPG de Docker en el
    sistema:***`sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc`*
5.  **Otorgar permisos de lectura a todos los usuarios para la clave GPG
    de Docker**:*`sudo chmod a+r /etc/apt/keyrings/docker.asc`*
6.  **Agregar el repositorio de Docker a las fuentes de Apt y actualizar
    la lista de
    paquetes**:*`echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null sudo apt-get update`*
7.  **Instalar Docker Engine, CLI, Containerd, Buildx y Compose
    plugins**:*`sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin`*

### Post-instalación (para cualquier distribución)

**Iniciar el servicio Docker:** *`sudo service docker start`*

Para evitar tener que usar `sudo` cada vez que ejecutes el comando
`docker`, puedes agregar tu usuario al grupo `docker` con el siguiente
comando:

1.  **Crear un grupo llamado 'docker'**:*`sudo groupadd docker`*
2.  **Agregar el usuario actual al grupo
    'docker'**:*`sudo usermod -aG docker $USER`*
