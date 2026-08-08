---
title: "SSH"
date: 2025-12-04T00:26:29.000Z
slug: ssh
---

En este artículo documento cómo generé mi **personal SSH key** en macOS,
dónde quedó almacenada, cómo la cargué en el `ssh-agent`, cómo la
integré con el **Keychain de macOS** y cómo copio esa clave a servidores
Linux, como mis nodos Ansible. Todo el flujo queda listo para
reutilizarlo en cualquier entorno.

------------------------------------------------------------------------

## Paso a paso

### 1. Generación de la clave SSH

Seguí las instrucciones oficiales de GitHub para generar una nueva clave
SSH con algoritmo **ED25519**. Ejecuté el siguiente comando:

``` bash
ssh-keygen -t ed25519 -C "adm@dominio.com"
```

Durante el proceso:

- Definí la ruta manualmente:

``` bash
/volumes/ext/user/.ssh/id_ed25519
```

- No asigné **passphrase** a la clave.

Resultado final:

- Clave privada:

``` bash
/volumes/ext/user/.ssh/id_ed25519
```

- Clave pública:

``` bash
/volumes/ext/user/.ssh/id_ed25519.pub
```

- Fingerprint generado:

``` bash
SHA256:ujH64Myk6G5EJEMLPOq6U5jx5PeS5Ij81vPhHc4 adm@dominio.com
```

Este paso es únicamente para tener claro **desde qué equipo y desde qué
ruta se origina la clave**.

------------------------------------------------------------------------

### 2. Inicialización del ssh-agent

Como estoy en macOS, inicialicé el agente con:

``` bash
eval "$(ssh-agent -s)"
```

Salida esperada:

``` bash
Agent pid 42900
```

Esto habilita la carga de claves en memoria.

------------------------------------------------------------------------

### 3. Configuración automática en ~/.ssh/config

Para que macOS cargue automáticamente la clave en cada conexión y la
integre con el Keychain, edité el archivo:

``` bash
open ~/.ssh/config
```

Mi configuración quedó así:

``` bash
Host git.domino.com
    HostName git.domino.com
    User xvin
    Port 2222
    AddKeysToAgent yes
    IdentityFile /volumes/ext/user/.ssh/id_ed25519
```

Esto permite:

- Carga automática de la clave.
- Asociación con el host correcto.
- Uso de puertos personalizados.

------------------------------------------------------------------------

### 4. Carga de la clave en el Keychain de macOS

Ejecuté:

``` bash
ssh-add --apple-use-keychain /volumes/ext/user/.ssh/id_ed25519
```

Esto permite que la clave quede almacenada en el **Keychain** y se
cargue automáticamente sin solicitar credenciales repetidamente.

------------------------------------------------------------------------

### 5. Copia de la clave al servidor remoto

Desde mi **servidor Ansible** utilizo este comando para copiar la clave
al host remoto:

``` bash
ssh-copy-id -i ~/.ssh/ansible.pub user@10.0.0.10
```

Si el servidor usa un puerto distinto, por ejemplo **3022**:

``` bash
ssh-copy-id -i ~/.ssh/ansible.pub -p 2222 user@10.0.0.10
```

Solo debo reemplazar:

- `user` por el usuario real del servidor
- `10.0.0.10` por la IP del host destino

------------------------------------------------------------------------

### 6. Verificación de acceso sin contraseña

Después de copiar la clave verifico el acceso con:

``` bash
ssh user@10.0.0.10
```

Si la conexión entra directamente sin solicitar password, la clave quedó
correctamente instalada.

------------------------------------------------------------------------

## Bloque de comandos

``` bash
# Generar clave
ssh-keygen -t ed25519 -C "adm@dominio.com"

# Iniciar agente
eval "$(ssh-agent -s)"

# Editar configuración SSH
open ~/.ssh/config

# Cargar clave en el Keychain
ssh-add --apple-use-keychain /volumes/ext/user/.ssh/id_ed25519

# Copiar clave al servidor
ssh-copy-id -i ~/.ssh/ansible.pub user@10.0.0.10

# Verificar acceso
ssh user@10.0.0.10
```

------------------------------------------------------------------------

## Buenas prácticas

- Usar siempre **ED25519** por seguridad y rendimiento.
- Mantener las claves fuera del disco principal si el equipo lo permite.
- Definir correctamente los `Host` en `~/.ssh/config` para evitar
  errores.
- No reutilizar claves personales en entornos compartidos.
- En servidores críticos, considerar usar **passphrase**.

------------------------------------------------------------------------

## FAQ

**¿Es obligatorio usar passphrase?**  
No es obligatorio, pero es altamente recomendado en entornos
corporativos.

**¿Puedo usar la misma clave para GitHub y mis servidores?**  
Se puede, pero para mayor segmentación de seguridad es mejor separar
claves.

**¿Qué pasa si borro el Keychain?**  
La clave seguirá existiendo en disco, pero deberá volver a cargarse
manualmente.
