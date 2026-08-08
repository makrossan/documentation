---
title: "Debian - Waiting for cache lock: Could not get lock /var/lib/dpkg/lock-frontend. It is held by process 13347 (unattended-upgr)"
date: 2025-09-13T23:59:41.000Z
slug: debian-waiting-for-cache-lock-could-not-get-lock-var-lib-dpkg-lock-frontend-it-is-held-by-process-13347-unattended-upgr
---

Este mensaje de error indica que otro proceso, en este caso
\`unattended-upgr\`, está utilizando el sistema de gestión de paquetes
\`dpkg\` y ha bloqueado el acceso para evitar conflictos.
\`unattended-upgr\` es un proceso que se encarga de las actualizaciones
automáticas de seguridad en sistemas basados en Debian y Ubuntu.

Para resolver este problema, puedes esperar a que el proceso
\`unattended-upgr\` termine su trabajo y libere el bloqueo. Esto puede
tardar varios minutos, especialmente si está descargando e instalando
actualizaciones.

Si necesitas interrumpir \`unattended-upgr\` y proceder con tus propias
operaciones de gestión de paquetes, puedes hacer lo siguiente:

1\. **Verificar si \`unattended-upgr\` todavía se está ejecutando:**  

``` bash
ps -p 13347
```

   Si el proceso ya no está en ejecución, el bloqueo debería haberse
liberado.

2\. **Matar el proceso \`unattended-upgr\`** (solo si es necesario y
comprendes las posibles consecuencias):  

``` bash
sudo kill 13347
```

   O, si quieres forzar el cierre del proceso:  

``` bash
sudo kill -9 13347
```

3\. **Esperar unos momentos** y luego intentar nuevamente tu operación
de gestión de paquetes.

4\. **Eliminar manualmente el archivo de bloqueo** (último recurso y no
recomendado a menos que estés seguro de que ningún proceso de \`dpkg\` o
\`apt\` se esté ejecutando):  

``` bash
sudo rm /var/lib/dpkg/lock-frontend
```

Después de resolver el problema del bloqueo, es una buena práctica
ejecutar \`sudo dpkg --configure -a\` para asegurarte de que todos los
paquetes estén correctamente configurados y \`sudo apt update\` para
actualizar la lista de paquetes disponibles.
