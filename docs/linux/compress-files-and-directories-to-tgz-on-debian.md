---
title: "Debian - comprimir directorios o archivos en tgz"
date: 2025-09-13T23:57:58.000Z
slug: debian-comprimir-directorios-o-archivos-en-tgz
---

Comprimir un directorio.

``` bash
tar czvf nombre_del_archivo.tgz /nombre/del/directorio/
```

 Comprimir un archivo.

``` bash
tar czvf nombre_del_archivo.tgz nombre_archivo_a_compactar
```

Descompactar un tgz. 

``` bash
tar xzvf nombre_del_archivo.tgz
```

- `c`: Crea un nuevo archivo.
- `z`: Comprime el archivo usando gzip.
- `v`: Modo verboso (muestra el proceso).
- `f`: Especifica el nombre del archivo (siguiente argumento).
- `x`: Extrae el contenido del archivo.

Otros argumentos disponibles. 

1.  **Operaciones principales**: 
    - `t`: Listar el contenido de un archivo tarball.
    - `r`: Añadir archivos a un archivo tarball existente (rara vez se
      usa porque el archivo debe ser no comprimido).
    - `u`: Actualizar archivos en un archivo tarball existente si el
      archivo en el disco es más reciente (nuevamente, rara vez se usa
      por la misma razón).
    - `d`: Comparar el contenido del archivo tarball con el sistema de
      archivos.
2.  **Opciones de manipulación del archivo**: 
    - `j`: Comprimir usando `bzip2` o descomprimir un archivo bzip2.
    - `J`: Comprimir usando `xz` o descomprimir un archivo xz.
3.  **Opciones de selección de archivo**:
    - `A`: Concatenar archivos tar.
    - `--exclude`: Excluir archivos que coincidan con el patrón
      especificado.
    - `--no-recursion`: No archivar subdirectorios.
    - `--recursion`: Archivar subdirectorios (esto es el comportamiento
      predeterminado).  
4.  **Opciones relacionadas con el manejo de permisos y propietarios**:
    - `--no-same-owner`: Al extraer, no intentar conservar el mismo
      propietario que en el archivo original.
    - `--no-same-permissions`: Al extraer, no intentar conservar los
      mismos permisos que en el archivo original.
    - `p`: Conservar permisos (usado al extraer).
    - `--numeric-owner`: No resolver nombres de usuario/grupo al crear o
      mostrar.
5.  **Otras opciones**:
    - `W`: Verificar la creación del archivo tarball.
    - `k`: No sobrescribir.
    - `m`: No restaurar la fecha de modificación.
    - `--totals`: Muestra el total de bytes después de procesar el
      archivo.
    - `--checkpoint`: Muestra puntos de control mientras procesa el
      archivo.
