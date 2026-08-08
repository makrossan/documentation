---
title: "Comando grep"
date: 2025-09-14T00:06:04.000Z
slug: comando-grep
---

  
El comando `grep` es una herramienta muy utilizada en sistemas Linux
para buscar cadenas de texto o patrones específicos dentro de archivos o
salidas de otros comandos. Su función principal es filtrar líneas que
coinciden con el patrón de búsqueda proporcionado.

### Comando ejemplo:

`grep tcp /etc/services | awk '{print $1}' | sort | less`

### Desglose:

1.  **`grep tcp /etc/services`**:
    - **`grep`** busca líneas que contienen el texto **`tcp`** en el
      archivo **`/etc/services`**.
    - El archivo `/etc/services` es una lista de servicios de red y sus
      puertos asociados, incluyendo si usan **TCP** o **UDP**.
    - Esto filtra todas las líneas donde aparece "tcp", que corresponde
      a servicios que usan el protocolo TCP.
2.  **`awk '{print $1}'`**:
    - **`awk`** es una herramienta para procesar texto. En este caso,
      toma la salida de `grep` y extrae la **primera columna** (campo),
      que en el archivo `/etc/services` es el **nombre del servicio**.
    - Por ejemplo, si una línea contiene `http 80/tcp`, el
      `awk '{print $1}'` extraerá solo `http`.
3.  **`sort`**:
    - **`sort`** ordena alfabéticamente los nombres de los servicios
      extraídos por `awk`. Esto organiza los resultados para que se
      muestren en orden.
4.  **`less`**:
    - **`less`** es un paginador que permite visualizar la salida de
      manera interactiva. Como la lista de servicios puede ser larga,
      `less` facilita la navegación por la salida paginada (arriba/abajo
      con las teclas de flecha o espacio).
