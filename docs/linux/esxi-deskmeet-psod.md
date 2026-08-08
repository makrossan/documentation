---
title: "ESXi en Deskmeet PSOD"
date: 2025-09-13T23:40:36.000Z
slug: esxi-en-deskmeet-psod
---

Si al instalar ESXi obtiene un PSOD (Purple Screen of Death), es
importante saber que esto puede deberse a una incompatibilidad con el
CPU.

Para resolverlo, se debe deshabilitar la verificación del CPU.

El procedimiento implica modificar el archivo boot.cfg para agregar el
parámetro `cpuUniformityHardCheckPanic=FALSE`. Este cambio debe
realizarse en las rutas `/bootbank/boot.cfg` y `/altbootbank/boot.cfg`
de su medio de arranque (que puede ser un disco SATA local, USB u otro
medio).

Para hacer este ajuste, agregue el parámetro en la sección “kernelopt”
del archivo mencionado. Como referencia, puede usar un editor como VI a
través de SSH, que fue el método que utilicé en mi caso.

Este ajuste desactiva la verificación que provoca el error de
incompatibilidad de CPU, lo que debería permitirle completar la
instalación sin problemas.

<figure class="kg-card kg-image-card">
<img src="__GHOST_URL__/content/images/2025/09/image-1.png"
class="kg-image" loading="lazy"
srcset="__GHOST_URL__/content/images/size/w600/2025/09/image-1.png 600w, __GHOST_URL__/content/images/2025/09/image-1.png 627w"
width="627" height="455" />
</figure>
