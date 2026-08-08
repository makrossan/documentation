---
title: "Proxmox: reactivar root@pam desde la terminal y recuperar el acceso al WebUI"
date: 2025-10-15T12:55:32.000Z
slug: proxmox-reactivar-root-pam-desde-la-terminal-y-recuperar-el-acceso-al-webui
---

> Hoy les cuento una situación real que me ocurrió: al editar el
> usuario **root** en el WebUI de Proxmox, dejé la
> casilla **Enable** desmarcada y, al guardar, me quedé sin acceso. Por
> suerte tenía una sesión **SSH** abierta. Aquí le muestro, paso a paso,
> cómo lo solucioné.

------------------------------------------------------------------------

## Resumen rápido

Si ya tiene una sesión SSH abierta en el nodo, estos comandos le
devuelven el acceso en segundos:

``` bash
sudo -i && \
pveum user modify root@pam --enable 1 && \
pveum account unlock root@pam || true && \
systemctl restart pveproxy && \
echo "Listo: intente entrar como root@pam (Realm: Linux PAM)"
```

Luego entre al WebUI con **Usuario:** `root@pam` y **Realm:** *Linux
PAM*.

------------------------------------------------------------------------

## Retrocediendo y explicando el paso a paso

### 1) Verificar acceso a la terminal

Asegúrese de estar dentro por SSH en el nodo afectado. Si no es `root`,
eleve privilegios:

``` bash
sudo -i
```

### 2) Confirmar el estado del usuario `root@pam`

Compruebe si aparece como deshabilitado o bloqueado:

``` bash
pveum user list | grep 'root@pam'
```

Debería ver una fila con `enabled` y, si corresponde, campos de bloqueo.

### 3) Volver a **habilitar** el usuario

``` bash
pveum user modify root@pam --enable 1
```

Esto reestablece el flag de cuenta activa.

### 4) Desbloquear la cuenta (si hubo varios intentos fallidos)

``` bash
pveum account unlock root@pam
```

### 5) (Opcional) Corregir nombre, apellido y correo

Si el problema empezó al editar estos campos, puede dejarlos bien desde
CLI:

``` bash
pveum user modify root@pam \
  --firstname "Usuario" \
  --lastname  "Master" \
  --email     "correo@nuestrodominio.com"
```

> Ajuste los valores a su preferencia.

### 6) Refrescar el servicio del WebUI

Aunque no siempre es necesario, reiniciar el proxy del UI ayuda a
aplicar cambios visualmente:

``` bash
systemctl restart pveproxy
```

### 7) Probar el inicio de sesión

Abra el WebUI y verifique:

- **Usuario:** `root@pam`
- **Realm:** **Linux PAM**
- Contraseña habitual de *root* del sistema

Si el UI seguía abierto en otra pestaña, actualice la página por
completo (Ctrl/Cmd + Shift + R).

------------------------------------------------------------------------

Buenas prácticas para que no vuelva a pasar

1.  **Mantener un usuario administrativo alterno** (no-root) con
    permisos adecuados y **2FA**.
2.  **No deshabilitar `root@pam`** mientras se edita el perfil; si
    quiere restringir su uso, documente un plan de rollback.
3.  **Respaldar la configuración del clúster** con regularidad (por
    ejemplo, copia de `/etc/pve/`).
4.  **Registro de cambios**: al tocar permisos/usuarios, anote fecha,
    nodo y acciones.

------------------------------------------------------------------------

## Solución de problemas (FAQ breve)

- **"No encuentro `pveum`"**: asegúrese de estar en Proxmox (no en un
  contenedor) y de tener privilegios de root.
- **"Cambios no se reflejan"**: borre caché del navegador o pruebe en
  ventana privada.

**"Sigue sin entrar"**: revise que el *Realm* sea **Linux PAM** y que no
haya *Caps Lock*. Intente reiniciar también `pvedaemon` si lo ve
inestable:

``` bash
systemctl restart pvedaemon
```
