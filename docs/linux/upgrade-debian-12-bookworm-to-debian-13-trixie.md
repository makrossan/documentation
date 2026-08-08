---
title: "Cómo actualicé de Debian 12 (Bookworm) a Debian 13 (Trixie)"
date: 2025-10-09T11:32:37.000Z
slug: como-actualice-de-debian-12-bookworm-a-debian-13-trixie
---

Quería dejar por escrito el procedimiento exacto que sigo para subir de
**Debian 12 → 13** sin sobresaltos. Está pensado para que usted lo
replique con confianza en su servidor o VM.

------------------------------------------------------------------------

## **En pocas palabras (si ya sabe lo que hace)**

1.  Verifico formato de APT, creo respaldo y cambio **bookworm →
    trixie**.
2.  Hago **upgrade mínimo** y luego **full-upgrade**.
3.  Reinicio y valido.

``` bash
# 0) Formato APT (rápido)
if find /etc/apt -maxdepth 2 -type f -name '*.sources' -print -quit | grep -q .; then
  echo "Formato deb822 (*.sources)"; 
else 
  echo "Formato clásico (sources.list / *.list)"; 
fi

# 1) (Clásico) Edito solo repos oficiales, con respaldo .bak
sudo bash -c '
set -e; shopt -s nullglob
FILES=(/etc/apt/sources.list /etc/apt/sources.list.d/*.list)
[ ${#FILES[@]} -gt 0 ] && sed -i.bak -E "/^[[:space:]]*#/! {/deb\.debian\.org\/debian|security\.debian\.org\/debian-security/ { s/\<bookworm-security\>/trixie-security/g; s/\<bookworm-updates\>/trixie-updates/g; s/\<bookworm\>/trixie/g; }}" "${FILES[@]}"
apt update
apt upgrade --without-new-pkgs -y
apt full-upgrade -y
reboot
'
```

> Si usa **deb822** (\*.sources), más abajo dejo el bloque exacto.

------------------------------------------------------------------------

## **Requisitos y buenas prácticas que sí me han ahorrado problemas**

- **Ventana de mantenimiento** y, si es VM, **snapshot** antes de
  empezar.
- Ejecuto en **tmux** o **screen** para no perder la sesión si la
  conexión cae:

``` bash
sudo apt install tmux -y && tmux
```

- **Espacio libre**: al menos 2–3 GB en /:

``` bash
df -h /
```

- Si tiene repos de terceros (Docker, Zabbix, Grafana, NodeSource,
  etc.), verifico si ya publicaron suite trixie. Si **no**, los dejo en
  bookworm o los comento temporalmente.

------------------------------------------------------------------------

## **Paso 1 — Detectar el formato de APT**

Debian hoy convive con dos formatos:

- **Clásico:** /etc/apt/sources.list y .list en sources.list.d/.
- **deb822:** uno o varios archivos \*.sources (p. ej. debian.sources).

Para detectarlo uso:

``` bash
if find /etc/apt -maxdepth 2 -type f -name '*.sources' -print -quit | grep -q .; then
  echo "Formato deb822 (*.sources)"
else
  echo "Formato clásico (sources.list / *.list)"
fi
```

------------------------------------------------------------------------

## **Paso 2A — Cambiar bookworm → trixie (formato clásico)**

Yo edito **solo los repos oficiales** y dejo respaldo .bak por si debo
revertir:

``` bash
sudo bash -c '
set -e
shopt -s nullglob
FILES=(/etc/apt/sources.list /etc/apt/sources.list.d/*.list)
[ ${#FILES[@]} -gt 0 ] && sed -i.bak -E "/^[[:space:]]*#/! {/deb\.debian\.org\/debian|security\.debian\.org\/debian-security/ { s/\<bookworm-security\>/trixie-security/g; s/\<bookworm-updates\>/trixie-updates/g; s/\<bookworm\>/trixie/g; }}" "${FILES[@]}"
```

> **Nota:** si tiene entradas de terceros, no las toco con el sed
> anterior. Prefiero revisarlas a mano.

------------------------------------------------------------------------

## **Paso 2B — Cambiar bookworm → trixie (formato deb822)**

Si su sistema usa \*.sources, el ajuste correcto es sobre el campo
**Suites**:

``` bash
sudo bash -c '
set -e
shopt -s nullglob
SRC=(/etc/apt/sources.list.d/*.sources /etc/apt/sources.list.d/debian.sources /etc/apt/sources.list.d/*debian*.sources /etc/apt/sources.list.d/*security*.sources)
[ ${#SRC[@]} -gt 0 ] && sed -i.bak -E "/^[[:space:]]*#/! { s/\bSuites:\s*bookworm-security\b/Suites: trixie-security/; s/\bSuites:\s*bookworm(\s+bookworm-updates)?/Suites: trixie trixie-updates/; }" "${SRC[@]}"
```

Si quiere “modernizar” primero desde formato clásico:

``` bash
sudo apt modernize-sources
```

------------------------------------------------------------------------

## **Paso 3 — Actualización en dos fases**

Primero **sin** meter paquetes nuevos; luego el **full-upgrade** que
resuelve cambios de dependencias:

``` bash
sudo apt update
sudo apt upgrade --without-new-pkgs
sudo apt full-upgrade
```

En esta etapa, si aparece una pantalla de conffile (Nginx, SSH, etc.),
yo reviso el diff y **conservo mi configuración** salvo que la nueva
traiga algo crítico que necesite.

------------------------------------------------------------------------

## **Paso 4 — Reinicio y validaciones**

``` bash
sudo reboot
```

Al volver:

``` bash
cat /etc/debian_version      # Debe decir 13.x
uname -r                     # Kernel nuevo (si aplicaba)
grep -R "deb .*debian" /etc/apt/sources.list{,.d/*.list} 2>/dev/null
```

<figure class="kg-card kg-image-card">
<img src="__GHOST_URL__/content/images/2025/10/image-1.png"
class="kg-image" loading="lazy"
srcset="__GHOST_URL__/content/images/size/w600/2025/10/image-1.png 600w, __GHOST_URL__/content/images/size/w1000/2025/10/image-1.png 1000w, __GHOST_URL__/content/images/size/w1600/2025/10/image-1.png 1600w, __GHOST_URL__/content/images/2025/10/image-1.png 2262w"
sizes="(min-width: 720px) 720px" width="2000" height="458" />
</figure>

Limpieza opcional:

``` bash
sudo apt --purge autoremove
sudo apt clean
```

------------------------------------------------------------------------

## **Problemas comunes que me he encontrado (y cómo los resuelvo)**

- **Repos de terceros no listos para Trixie**Si apt update arroja 404 o
  “Release file not found”, dejo esa entrada en **bookworm** o la
  comento hasta que el proveedor publique trixie. Ejemplo rápido:

``` bash
sudo sed -i 's/trixie/bookworm/g' /etc/apt/sources.list.d/docker.list
sudo apt update
```

- **Paquetes retenidos (held back)**

``` bash
apt-mark showhold
sudo apt install <paquete>
```

- o fuerzo resolver con:

``` bash
sudo apt -o Dpkg::Options::="--force-confold" full-upgrade
```

- **dpkg a medio camino** (corte de luz, SSH se cayó, etc.)

``` bash
sudo dpkg --configure -a
sudo apt -f install
```

- **Advertencias de “Directory not empty” o usr-is-merged**Son normales
  durante la transición; tras el reinicio suelen desaparecer. Si
  persisten como directorios vacíos, verifico que no rompan nada antes
  de eliminarlos.
- **Servicios críticos**Reviso que todo levante:

``` bash
systemctl --failed
journalctl -p 3 -xb
```

------------------------------------------------------------------------

## **¿Revertir? Lo prudente es **

## **restaurar el snapshot**

Hacer “downgrade del release” no es algo que yo recomiende. Si algo sale
mal, para mí la salida profesional es **volver al snapshot/backup**,
corregir, y reintentar el upgrade.

Para pequeños ajustes (solo APT), siempre quedan los \*.bak de las
fuentes:

``` bash
sudo mv /etc/apt/sources.list.bak /etc/apt/sources.list
sudo mv /etc/apt/sources.list.d/*.bak /etc/apt/sources.list.d/
sudo apt update
```

------------------------------------------------------------------------

## **Checklist rápido (lo que yo marco como “listo”)**

- Snapshot/backup verificado
- Repos oficiales apuntan a trixie
- Repos de terceros revisados (o comentados)
- apt upgrade --without-new-pkgs OK
- apt full-upgrade OK
- Reinicio, servicios arriba y systemctl --failed vacío
- Limpieza (autoremove, clean)
