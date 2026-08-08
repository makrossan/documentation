---
title: "Cómo crear un repositorio Git desde una carpeta existente (solo SSH, Gitea en puerto 3022)"
date: 2025-10-13T02:11:39.000Z
slug: como-crear-un-repositorio-git-desde-una-carpeta-existente-solo-ssh-gitea-en-puerto-3022
---

**Contexto de mi laboratorio**

- Servidor Git (Gitea): repo.lan.nuestrodominio.com
- Puerto SSH de Gitea: **3022**
- Propietario en Gitea: admin
- Llave SSH: ~/.ssh/id_ed25519 (la pública se agregará en el Paso 0)
- Carpeta que deseo versionar: ~/ansible en mi servidor srv-01-dev
  (Debian)

El objetivo es tomar una carpeta existente y convertirla en un
repositorio en Gitea usando **SSH**.

------------------------------------------------------------------------

## **Paso 0 — Agregar y verificar la llave SSH en Gitea**

1.  Entre a: https://repo.lan.nuestrodominio.com/user/settings/keys →
    sección **Manage SSH keys** → **Add key**.
2.  Pegue el **contenido** de su llave pública id_ed25519.pub, asigne un
    nombre descriptivo y haga clic en **Add key**.
    1.  Si aún no tiene una llave **ed25519**, puede crearla siguiendo
        esta guía oficial:<a
        href="https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent"
        rel="noreferrer">https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent</a>*(aplica
        igual para Gitea)*.
3.  **Verifique la llave** desde el **equipo que posee la llave
    privada** (~/.ssh/id_ed25519):

<figure class="kg-card kg-image-card">
<img src="__GHOST_URL__/content/images/2025/10/image-4.png"
class="kg-image" loading="lazy"
srcset="__GHOST_URL__/content/images/size/w600/2025/10/image-4.png 600w, __GHOST_URL__/content/images/2025/10/image-4.png 788w"
sizes="(min-width: 720px) 720px" width="788" height="513" />
</figure>

``` bash
ssh -T -p 3022 git@repo.lan.nuestrodominio.com
# Debería responder: “Hi admin! You've successfully authenticated, but Gitea does not provide shell access.”
```

> Si pide contraseña, más abajo le indico cómo corregir puerto/llave.

------------------------------------------------------------------------

## **Paso 1 — Configurar SSH en el host que empuja (**srv-01-dev**)**

En srv-01-dev, o ajusto ~/.ssh/config para que Git use el puerto
**3022** y la llave correcta:

``` bash
# ~/.ssh/config  (en srv-01-dev, sin sudo)
Host repo.lan.nuestrodominio.com
  HostName repo.lan.nuestrodominio.com
  User git
  Port 3022
  IdentityFile ~/.ssh/id_ed25519
  IdentitiesOnly yes
```

Endurezco permisos:

``` bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/config ~/.ssh/id_ed25519
chmod 644 ~/.ssh/id_ed25519.pub
chown -R "$USER":"$USER" ~/.ssh
```

Pruebo la autenticación:

``` bash
ssh -T git@repo.lan.nuestrodominio.com
# o, explícito con puerto:
ssh -T -p 3022 git@repo.lan.nuestrodominio.com
```

------------------------------------------------------------------------

## **Paso 2 — Crear el repositorio vacío en Gitea (una sola vez, vía UI)**

En mi servidor **push-to-create está deshabilitado**, por eso primero
creo el repo en la interfaz web:

1.  Abrir repo.lan.nuestrodominio.com y autenticarse.
2.  **New Repository** → **Owner**: admin → **Repository Name**:
    ansible.
3.  Elegir visibilidad (uso *Private*).
4.  **No** inicializar con README/.gitignore/License (para evitar
    conflictos en el primer push).
5.  Crear.

<figure class="kg-card kg-image-card">
<img src="__GHOST_URL__/content/images/2025/10/image-7.png"
class="kg-image" loading="lazy"
srcset="__GHOST_URL__/content/images/size/w600/2025/10/image-7.png 600w, __GHOST_URL__/content/images/2025/10/image-7.png 802w"
sizes="(min-width: 720px) 720px" width="802" height="1259" />
</figure>

> Si en su entorno *sí* está habilitado el push-to-create, podría
> saltarse este paso y pasar directo al push. En el mío no.

------------------------------------------------------------------------

## **Paso 3 — Inicializar la carpeta local y hacer el primer push (en** srv-01-dev**)**

Dentro de srv-01-dev:~/ansible:

``` bash
cd ~/ansible
git init -b main
git add .
git commit -m "Initial import"

# Opción A — confiar en ~/.ssh/config (usa puerto 3022 automáticamente)
git remote add origin git@repo.lan.nuestrodominio.com:admin/ansible.git

# Empujar la rama principal
git push -u origin main
```

> Alternativa si desea forzar el puerto en la URL (ignora
> ~/.ssh/config):

> git remote set-url origin
> ssh://git@repo.lan.nuestrodominio.com:3022/admin/ansible.git

Compruebo el remoto:

``` bash
git remote -v
```

------------------------------------------------------------------------

## **Paso 4 — (Opcional) Añadir un .gitignore típico para Ansible**

``` bash
cat > .gitignore <<'EOF'
*.retry
*.swp
*.swo
.cache/
.idea/
.vscode/
**/.DS_Store
EOF

git add .gitignore
git commit -m "Add .gitignore"
git push
```

------------------------------------------------------------------------

## **Paso 5 — (Opcional) Configurar identidad global de Git**

``` bash
git config --global user.name  "Admin 0"
git config --global user.email "admin@srv-01-dev.nuestrodominio.lan"
```

------------------------------------------------------------------------

## **Solución de problemas (lo que me pasó y cómo lo resolví)**

- **Pide contraseña para git@…**Casi siempre es porque se está
  intentando por **puerto 22**.**Solución:** asegúrese de tener Port
  3022 en ~/.ssh/config del host que empuja (srv-01-dev), o use la URL
  con puerto:

``` bash
git remote set-url origin ssh://git@repo.lan.nuestrodominio.com:3022/admin/ansible.git
```

- Verifique qué parámetros usará SSH:

``` bash
ssh -G repo.lan.nuestrodominio.com | grep -Ei 'user|port|identityfile'
```

- **Permission denied (publickey)**Gitea no aceptó la llave
  ofrecida.**Solución:** confirmar que la pública cargada en Gitea es
  exactamente ~/.ssh/id_ed25519.pub del host que empuja.

``` bash
ssh -Tvv -p 3022 git@repo.lan.nuestrodominio.com
# Busque “Offering public key: ~/.ssh/id_ed25519” y luego “Authentication succeeded”
```

- **Push to create is not enabled for users.**En mi servidor, el
  push-to-create está deshabilitado.**Solución:** crear el repositorio
  en la **UI** y repetir git push -u origin main.
- **El repositorio remoto tiene un README (auto-init) y rechaza mi
  primer pushA (segura):**

``` bash
git pull --rebase origin main
git push -u origin main
```

- **B (para repos nuevos, aceptando sobrescribir):**

``` bash
git push -u origin main --force-with-lease
```

- **El proceso de push quedó en segundo plano (Stopped)Solución:** use
  fg para traerlo al frente, o realice un push nuevo tras corregir la
  configuración.

------------------------------------------------------------------------

## **Repetir la receta para otras carpetas**

Mismo patrón. Por ejemplo, para ~/dockerbackups:

``` bash
cd ~/dockerbackups
git init -b main
git add .
git commit -m "Initial import"
git remote add origin git@repo.lan.nuestrodominio.com:admin/dockerbackups.git
git push -u origin main
```

------------------------------------------------------------------------

### **Resumen**

- Agregué y verifiqué la **llave SSH** en Gitea (Paso 0).
- Ajusté SSH en srv-01-dev para usar **id_ed25519** por el puerto
  **3022** (Paso 1).
- Como mi Gitea no permite **push-to-create**, **primero** creé el repo
  admin/ansible en la UI (Paso 2).
- Inicialicé ~/ansible, añadí el remoto y empujé main (Paso 3).
- Añadí un .gitignore práctico, y dejé comandos de
  verificación/diagnóstico.

Así, su carpeta existente queda versionada y respaldada en su Gitea,
usando únicamente **SSH**.
