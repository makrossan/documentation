---
title: "Eliminar archivos excepto un documento"
date: 2025-10-20T13:45:02.000Z
slug: eliminar-archivos-excepto-un-documento
---

A veces, un directorio se llena de archivos temporales, pruebas o restos
de comandos mal ejecutados. Si lo que usted desea es **eliminar todo
excepto un archivo específico**, como por ejemplo documento-ejemplo,
Bash ofrece una forma rápida y segura de hacerlo.

------------------------------------------------------------------------

**Paso a paso**

- Abra la terminal y ubíquese en el directorio donde está el archivo que
  quiere conservar.

``` bash
cd /ruta/al/directorio
```

- Ejecute el siguiente script, que recorre todos los archivos y carpetas
  del directorio actual y elimina todo lo que **no sea**
  documento-ejemplo.

``` bash
for item in *; do
  if [[ "$item" != "documento-ejemplo" ]]; then
    rm -rf -- "$item"
  fi
done
```

- Si prefiere verificar primero qué se eliminará sin borrar nada, puede
  hacer una prueba con:

``` bash
for item in *; do
  [[ "$item" != "documento-ejemplo" ]] && echo "Se eliminaría: $item"
done
```

------------------------------------------------------------------------

**Bloque de comandos**

``` bash
#!/usr/bin/env bash
# Script para eliminar todo excepto 'documento-ejemplo'

for item in *; do
  if [[ "$item" != "documento-ejemplo" ]]; then
    rm -rf -- "$item"
  fi
done
```

------------------------------------------------------------------------

**Buenas prácticas**

Siempre pruebe con ***echo*** antes de ejecutar ***rm -rf***, para
evitar borrar algo importante.

- Use comillas alrededor de las variables (”\$item”) para evitar errores
  con nombres que contengan espacios o caracteres especiales.
- Si desea conservar varios archivos, puede modificar la condición, por
  ejemplo:

``` bash
if [[ "$item" != "documento-ejemplo" && "$item" != "informe.txt" ]]; then
```

- No ejecute este tipo de comandos como superusuario (sudo) a menos que
  sea estrictamente necesario.

------------------------------------------------------------------------

**FAQ**

**¿Puedo usar este script en subdirectorios?**

No directamente. El script actúa solo en el directorio actual. Para
aplicar recursivamente, puede combinarlo con find o un bucle que explore
subdirectorios.

**¿Qué pasa si el archivo se llama distinto?**

Solo debe cambiar el nombre dentro de la condición !=
"documento-ejemplo".

**¿Y si quiero conservar un tipo de archivo, como todos los .txt?**

Reemplace la condición con algo como:

``` bash
[[ $item != *.txt ]]
```
