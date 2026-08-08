---
title: "Ejecuta un archivo YAML de Docker Compose"
date: 2025-09-13T19:35:00.000Z
slug: ejecuta-un-archivo-yaml-de-docker-compose
---

Para ejecutar un archivo YAML de Docker Compose, normalmente usas el
comando `docker-compose up`, el cual construye, (re)crea, inicia y
adjunta contenedores para un servicio. Aquí tienes una guía básica sobre
cómo usarlo:

**Navega al directorio**: Asegúrate de estar en el directorio que
contiene tu archivo Docker Compose (`docker-compose.yml`). Puedes usar
el comando `cd` en tu terminal para cambiar de directorio.

**Ejecutar Docker Compose**:

- Para iniciar los servicios definidos en tu archivo Docker Compose, usa
  el siguiente comando:`docker-compose up`
- Si quieres ejecutarlo en modo desacoplado (en segundo plano), utiliza
  la opción `-d`:`docker-compose up -d`

**Verificar el estado de los contenedores**: Para verificar el estado de
los contenedores que son gestionados por Docker Compose, puedes
usar: `docker-compose ps`

**Detener los servicios**: Cuando quieras detener los servicios, puedes
usar: `docker-compose down`

Este comando detiene y elimina los contenedores, redes, volúmenes e
imágenes creados por `up`.

Estos comandos asumen que tienes Docker Compose instalado. Si estás
usando Docker Desktop para Windows o macOS, Docker Compose está
incluido. Para Linux, podrías necesitar instalarlo por separado. [Más
información
aquí](https://libreria.greivinvenegas.com/books/docker-compose/page/docker-compose-up-d-bash-docker-compose-command-not-found)

A partir de la versión 1.27.0 de Docker Compose, también puedes usar
directamente la CLI de Docker para gestionar archivos compose usando
comandos como `docker compose up` sin el guión. Esto está convirtiéndose
en la manera estándar de usar Compose con la integración de la CLI de
Docker.
