---
title: "Hard Links y Soft Links explicado"
date: 2026-02-27T13:45:48.000Z
slug: hard-links-y-soft-links-explicado
---

A veces en Linux uno se encuentra con archivos que parecen ser “el
mismo”, o enlaces que no se entiende bien qué hacen. La verdad, no es
complicado. Solo es cuestión de verlos como diferentes maneras de
apuntar a datos dentro del sistema de archivos. Vamos paso por paso,
para que ustedes lo entiendan sin enredos.

------------------------------------------------------------------------

## **Qué es un Hard Link**

Un **hard link** es simplemente otro nombre para el mismo archivo.

No es una copia. No es un acceso directo. Es el mismo archivo con dos
nombres distintos.

Imagínense que el archivo real no es el nombre, sino el **inode**, que
es donde se guarda la información y los metadatos.

Cuando crean un hard link, lo único que hacen es agregar otro nombre que
apunta al mismo inode.

Ejemplo:

- original.txt → inode 77777
- copia_real.txt → inode 77777

Ambos son exactamente el mismo archivo. Si editan uno, editan el otro.
Si borran uno, el otro sigue funcionando porque los datos siguen
existiendo mientras haya al menos un hard link apuntando al inode.

### **Cómo ver cuántos hard links tiene un archivo**

``` Bash
$ ls -l archivo_original.txt
-rw-r--r--@ 2 root  0 Feb 25 18:26 archivo_original.txt
```

El segundo número que aparece despues del @ es la cantidad de hard links

### **Cómo confirmar si dos archivos son hard links**

``` Bash
$ ls -i archivo_original.txt archivo_hardlink.txt
90616348 archivo_hardlink.txt  90616348 archivo_original.txt
```

Si comparten el mismo número de inode → son el mismo archivo.

------------------------------------------------------------------------

## **Qué es un Soft Link**

Un **soft link** (también llamado symlink) es más parecido a un atajo.

Este no apunta al inode, sino al **nombre del archivo** original.

Si el archivo original desaparece, el enlace queda roto.

Ejemplo:

- mi_enlace.txt → apunta a → /home/usuario/original.txt

Si borran original.txt, el soft link ya no sirve.

### **Cómo crear un soft link**

``` Bash
$ ln -s archivo_original.txt enlace.txt
```

### **Cómo identificar un soft link**

Al hacer:

``` Bash
$ ls -l enlace
lrwxr-xr-x@ 1 root  20 Feb 25 18:30 enlace.txt -> archivo_original.txt
```

Verán una flecha indicando hacia dónde apunta.

------------------------------------------------------------------------

## **Diferencias rápidas entre ambos**

| **Tema** | **Hard Link** | **Soft Link** |
|----|----|----|
| Apunta al inode | Sí | No |
| Apunta al nombre | No | Sí |
| Mismo contenido | Sí | No |
| Sobrevive si se borra el original | Sí | No |
| Funciona entre sistemas de archivos distintos | No | Sí |
| Puede apuntar a directorios | No | Sí |
| Si el original desaparece | No pasa nada | El link se rompe |

------------------------------------------------------------------------

## **Comandos esenciales**

### **Crear un hard link**

``` Bash
ln archivo_original archivo_nuevo
```

### **Crear un soft link**

``` Bash
ln -s archivo_original enlace
```

### **Ver inode**

``` Bash
ls -i archivo
```

### **Ver cuántos hard links existen**

``` Bash
ls -l archivo
```

------------------------------------------------------------------------

## **Cómo encontrar un archivo aunque esté en otro directorio**

Si un archivo tiene hard links repartidos en diferentes carpetas, todos
comparten el mismo inode.

Entonces lo más fácil es:

### **1. Obtener el inode del archivo**

``` Bash
ls -i archivo
```

Supongamos que les da:

**1234567**

### **2. Buscar todos los archivos con ese inode (en todo el sistema)**

``` Bash
find / -inum 1234567 2>/dev/null
```

Esto muestra todas las rutas que apuntan a ese mismo inode, sin importar
dónde estén.

### **Buscar solo en el directorio actual**

``` Bash
find . -inum 1234567
```

### **Buscar por nombre si no recuerdan el inode**

``` Bash
find / -name archivo.txt 2>/dev/null
```

### **Mostrar cada archivo con su inode**

``` Bash
find / -type f -printf "%i %p\n" 2>/dev/null
```
