---
title: "Redireccionar el resultado de un comando a un archivo."
date: 2025-09-14T00:05:10.000Z
slug: redireccionar-el-resultado-de-un-comando-a-un-archivo
---

En Linux, la **redirección de archivos** es una forma de controlar hacia
dónde van los datos de entrada y salida al ejecutar comandos. Puedes
redirigir la entrada estándar (stdin), la salida estándar (stdout) y los
errores estándar (stderr) hacia o desde archivos u otros comandos. Esto
permite manejar flujos de datos de manera eficiente, como guardar la
salida en un archivo o leer la entrada desde un archivo.

### Tipos de redirección:

1.  **Salida estándar (stdout)** (`>` y `>>`)
2.  **Entrada estándar (stdin)** (`<`)
3.  **Error estándar (stderr)** (`2>`, `2>>`, y `2>&1`)

#### 1. **Redirección de la salida estándar (stdout)**

Por defecto, la salida de un comando se muestra en la terminal. Puedes
redirigir esta salida a un archivo.

- **Sobrescribir archivo (`>`)**: Redirige la salida estándar a un
  archivo, sobrescribiendo el contenido del archivo si ya
  existe.`comando > archivo.txt`  
    
  Ejemplo:`echo "Hola, mundo" > salida.txt`  
    
  Esto escribe "Hola, mundo" en el archivo `salida.txt`, reemplazando su
  contenido si ya existe.
- **Agregar al archivo (`>>`)**: Redirige la salida estándar a un
  archivo, pero en lugar de sobrescribir, **agrega** el contenido al
  final del archivo si ya existe.`comando >> archivo.txt`  
    
  Ejemplo:`echo "Texto adicional" >> salida.txt`  
    
  Esto agrega "Texto adicional" al final del archivo `salida.txt` sin
  sobrescribir su contenido.

#### 2. **Redirección de la entrada estándar (stdin)**

Por defecto, muchos comandos toman entrada desde el teclado. Puedes
redirigir la entrada para que venga de un archivo en lugar del teclado.

- **Redirigir la entrada desde un archivo (`<`)**: Redirige la entrada
  estándar desde un
  archivo.`comando < archivo.txt`Ejemplo:`cat < archivo.txt`Esto usa el
  contenido de `archivo.txt` como entrada para el comando `cat`.

#### 3. **Redirección de errores estándar (stderr)**

Los errores producidos por los comandos suelen mostrarse en la terminal.
Puedes redirigir estos mensajes de error a un archivo.

- **Redirigir los errores (`2>`)**: Redirige la salida de errores a un
  archivo, sobrescribiendo el archivo si ya
  existe.`comando 2> errores.txt`  
    
  Ejemplo:`ls archivo_inexistente 2> errores.txt`  
    
  Este comando enviará el mensaje de error (porque el archivo no existe)
  a `errores.txt`.
- **Agregar los errores (`2>>`)**: Redirige los errores estándar a un
  archivo y agrega el contenido en lugar de
  sobrescribirlo.`comando 2>> errores.txt`  
    
- **Redirigir stdout y stderr al mismo archivo (`&>` o `2>&1`)**:
  Redirige tanto la salida estándar como los errores estándar al mismo
  archivo.`comando > archivo.txt 2>&1`  
  Ejemplo:`ls archivo_existente archivo_inexistente > salida.txt 2>&1`Esto
  enviará tanto la salida (listado del archivo existente) como el
  mensaje de error al archivo `salida.txt`.

#### 4. **Pipes (`|`)**

Puedes usar un **pipe (`|`)** para enviar la salida de un comando como
entrada a otro comando. Es una forma de redirección útil para encadenar
comandos.

`comando1 | comando2`

  
Ejemplo:

`ls | grep "archivo"`

Esto toma la salida de `ls` (listar archivos) y la pasa como entrada al
comando `grep` para filtrar y mostrar solo archivos que coinciden con
"archivo".

### Ejemplos comunes de redirección de archivos

- **Redirigir salida a un archivo**:`echo "Hola, mundo" > hola.txt`  
    
- **Agregar salida a un archivo**:`echo "Texto adicional" >> hola.txt`  
    
- **Redirigir stdout y stderr al mismo
  archivo**:`comando > salida.txt 2>&1`  
    
- **Redirigir stderr a un archivo**:`comando 2> errores.txt`  
    
- **Usar un archivo como entrada para un comando**:`cat < entrada.txt`  
    

### Resumen de símbolos:

- **`>`**: Redirigir stdout a un archivo (sobrescribe).
- **`>>`**: Redirigir stdout a un archivo (agregar).
- **`<`**: Redirigir stdin desde un archivo.
- **`2>`**: Redirigir stderr a un archivo (sobrescribe).
- **`2>>`**: Redirigir stderr a un archivo (agregar).
- **`2>&1`**: Redirigir stderr al mismo lugar que stdout.
- **`|`**: Encadenar la salida de un comando como entrada a otro.

La redirección de archivos en Linux es una herramienta muy poderosa para
gestionar la entrada y salida de datos, especialmente en la
automatización de scripts o manejo de grandes volúmenes de información.
