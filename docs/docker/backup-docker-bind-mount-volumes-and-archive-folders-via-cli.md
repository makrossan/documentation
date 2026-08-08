---
title: "Backup de volumen Docker (bind mount) y archivado de carpetas vía CLI"
date: 2025-10-02T11:01:53.000Z
slug: backup-de-volumen-docker-bind-mount-y-archivado-de-carpetas-via-cli
---

En este artículo aprenderá a realizar un respaldo comprimido (`.tar.gz`)
de un volumen de Docker *montado por
bind* en `$HOME/docker/volume` (ejemplo: stack **ghost**), verificar su
contenido y copiarlo a un NAS por `scp`.  
**También aplica** para comprimir/archivar cualquier carpeta desde
CLI.  
**Probado en:** 10.11.11.12

### Requisitos

- Acceso por shell (SSH o consola) al servidor.
- Docker y Docker Compose instalados; permisos `sudo`.
- Espacio libre suficiente para generar el `.tar.gz` (igual o mayor al
  tamaño de los datos).
- Nombre del contenedor de base de datos y credenciales si
  hará *dump* en caliente.
- (Opcional) Destino remoto (NAS) accesible por `scp`.

### Respaldo (opcional/recomendado)

Antes de proceder, haga un respaldo rápido de sus archivos de
orquestación:

``` bash
cd ~/docker/volume/ghost
cp docker-compose.yml docker-compose.yml.bak
cp .env .env.bak  # si existe
```

## Pasos principales

### Paso 1 — (Recomendado) Detener servicios para consistencia

Detener la aplicación y la base de datos garantiza que el backup de
archivos quede consistente. Puede hacerlo con Docker Compose o desde
Portainer.

``` bash
cd ~/docker/volume/ghost
sudo docker compose down
# Alternativa:
# sudo docker stop <ghost_container> <db_container>
```

### Paso 2 — Crear el archivo comprimido del proyecto

Genere el `.tar.gz` desde la carpeta padre y use un nombre fresco con la
fecha. Ejecute el `tar` como root para no perder permisos/propietarios.

``` bash
cd ~/docker/volume
sudo tar -czf "$HOME/docker/volume/ghost-$(date +%F).tar.gz" \
  -C "$HOME/docker/volume" ghost

# Entregar el archivo a su usuario (ajuste user1:user1 a su usuario/grupo)
sudo chown user1:user1 "$HOME/docker/volume/ghost-$(date +%F).tar.gz"
```

### Paso 3 — (Opcional) Levantar nuevamente los servicios

``` bash
cd ~/docker/volume/ghost
sudo docker compose up -d
# o use Portainer
```

### Paso 4 — (Sin downtime) Respaldo en caliente

Si no puede detener servicios, respalde **archivos de
aplicación** pero *excluya* los datos crudos de la base de datos y haga
un *dump* lógico. Ajuste la ruta de exclusión a su estructura real.

``` bash
# Archivos de app (excluyendo datos de MySQL)
cd ~/docker/volume
sudo tar --exclude='ghost/docs/mysql-data/**' -czf \
  "$HOME/docker/volume/ghost-nodb-$(date +%F).tar.gz" \
  -C "$HOME/docker/volume" ghost
sudo chown user1:user1 "$HOME/docker/volume/ghost-nodb-$(date +%F).tar.gz"

# Dump de base de datos desde el contenedor en ejecución
docker exec -t <db_container> mysqldump \
  -u root -p'<password>' --single-transaction ghost \
  > "$HOME/docker/volume/ghost-db-$(date +%F).sql"
```

### Paso 5 — (Opcional) Enviar el backup a su NAS por SCP

Si nombró el archivo con la fecha de hoy:

``` bash
scp -p ~/docker/volume/ghost-$(date +%F).tar.gz \
  user1@nas1:/archive/backups/containers/ghost/
```

Si no recuerda el nombre exacto, envíe el más reciente:

``` bash
latest=$(ls -t ~/docker/volume/ghost-*.tar.gz | head -n1)
scp -p "$latest" user1@nas1:/volume1/archive/backups/containers/ghost/
```

### Paso 6 — (Adicional) Solo archivar una carpeta (sin Docker)

Para comprimir cualquier carpeta local por CLI:

``` bash
# Crear archivo .tar.gz de una carpeta
tar -czf carpeta-$(date +%F).tar.gz -C /ruta/ a/la/carpeta

# Listar el contenido sin extraer
tar -tf carpeta-$(date +%F).tar.gz | head
```

## Verificación

Compruebe el contenido del archivo y su tamaño. Opcionalmente valide
checksum.

``` bash
# Ver los primeros elementos del tar
tar -tf "$HOME/docker/volume/ghost-$(date +%F).tar.gz" | head

# Ver tamaño del archivo
du -h "$HOME/docker/volume/ghost-$(date +%F).tar.gz"

# (Opcional) Generar checksum
sha256sum "$HOME/docker/volume/ghost-$(date +%F).tar.gz"
```

Prueba de restauración rápida en una carpeta temporal (no sobreescribe
su stack):

``` bash
mkdir -p ~/restore-test
tar -xzf "$HOME/docker/volume/ghost-$(date +%F).tar.gz" -C ~/restore-test
ls -la ~/restore-test/ghost | head
```

## Problemas frecuentes y soluciones

### 1) `scp: stat remote: No such file or directory`

El directorio de destino no existe en el NAS. Créelo antes de copiar.

``` bash
ssh user1@nas1 "mkdir -p /volume1/archive/backups/containers/ghost
scp -p "$HOME/docker/volume/ghost-$(date +%F).tar.gz" \
  user1@nas1:/volume1/archive/backups/containers/ghost/
```

### 2) `tar: file changed as we read it`

Ocurre si los archivos cambian durante el empaquetado. Detenga el
servicio (recomendado) o use la estrategia “sin downtime”
con *dump* lógico de la base de datos.

### 3) Permisos/propietarios incorrectos tras extraer

Asegúrese de crear el tar con `sudo` y, si lo necesita, ajuste
propietarios luego de restaurar:

``` bash
sudo chown -R <usuario>:<grupo> ~/docker/volume/ghost
```

### 4) Espacio insuficiente

Verifique espacio libre antes de crear o transferir el archivo:

``` bash
df -h
du -sh ~/docker/volume/ghost
```

### 5) La ruta de exclusión de MySQL no coincide

Ajuste `--exclude='ghost/docs/mysql-data/**'` a la ruta real de su
estructura. Si sus datos están en otra subcarpeta, cambie el patrón en
consecuencia.

## Notas y recordatorios

- Reemplace `user1:user1`, `<db_container>` y `<password>` según su
  entorno.
- Considere rotación/retención (por ejemplo, conservar 7 a 14 días).
  Puede automatizar con `cron`.
- Para respaldos más rápidos, evalúe `pigz` o `zstd` en lugar de gzip.
- Antes de confiar en el procedimiento, haga una **prueba de
  restauración** en un entorno aislado.
- Alternativa de transferencia: `rsync -avh --progress` para copias
  incrementales.

Última revisión: 2025-10-02
