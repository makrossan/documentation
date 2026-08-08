---
title: "Expansiones en la Shell"
date: 2026-03-02T15:13:58.000Z
slug: expansiones-en-la-shell
---

En este artículo explico de forma clara y práctica cómo funcionan las
expansiones más importantes de la shell.

## **Paso a paso**

Aquí presento cada tipo de expansión con una breve descripción y
ejemplos explicados.

### **1. Expansión con `*` (comodín general)**

El asterisco reemplaza cero o más caracteres.

### **2. Expansión con `?` (un carácter exacto)**

El signo `?` reemplaza exactamente un carácter.

### **3. Conjuntos de caracteres `[]`**

Permiten definir rangos o listas de caracteres válidos.

### **4. Expansión de llaves `{}`**

Sirve para generar múltiples cadenas o secuencias.

### **5. Expansión de tilde `~`**

Representa el directorio home del usuario.

### **6. Expansión de variables `$VAR`**

Permite utilizar variables dentro de comandos.

### **7. Sustitución de comandos `$( )`**

Inserta la salida de un comando dentro de otro.

### **8. Evitar expansiones**

Uso de barras invertidas y comillas para proteger caracteres.

------------------------------------------------------------------------

## **Bloque de comandos**

A continuación están los ejemplos completos utilizados en el artículo.

### **Usando `*`**

**Listar todos los archivos que terminan en `.txt`:**

``` bash
ls data/*.txt
```

**Output:**

``` bash
data/file1.txt  data/file_a.txt  data/report_2023.txt
```

**Listar archivos que contienen `file` en el nombre:**

``` bash
ls data/*file*
```

**Output:**

``` bash
data/file1.txt  data/file2.log  data/file_a.txt  data/file_b.log
```

------------------------------------------------------------------------

### **Usando `?`**

**Archivos con un carácter exacto antes de `.log`:**

``` bash
ls data/file?.log
```

**Output:**

``` bash
data/file2.log
```

------------------------------------------------------------------------

### **Usando `[]`**

**Reportes de 2023 y 2024:**

``` bash
ls data/report_[2][0][2][34].*
```

**Output:**

``` bash
data/report_2023.txt  data/report_2024.log
```

------------------------------------------------------------------------

### **Usando `{}`**

**Archivos `.txt` y `.log`:**

``` bash
ls data/file*.{txt,log}
```

**Output:**

``` bash
data/file1.txt  data/file2.log  data/file_a.txt  data/file_b.log
```

**Crear varios reportes:**

``` bash
touch data/report_{jan,feb,mar}.txt
```

**Crear secuencia numérica:**

``` bash
touch data/doc{1..3}.txt
```

**Crear secuencia de letras:**

``` bash
mkdir data/chapter{A..C}
```

------------------------------------------------------------------------

### **Tilde `~`**

``` bash
echo ~
echo ~root
echo ~/project/data
```

------------------------------------------------------------------------

### **Variables**

``` bash
MY_DIR=data
echo "Mi directorio es: $MY_DIR"
ls $MY_DIR
```

------------------------------------------------------------------------

### **Sustitución de comandos**

``` bash
touch data/log_$(date +%Y-%m-%d).txt
ls data/log_*.txt
echo "Hay $(ls data | wc -l) elementos en data."
```

------------------------------------------------------------------------

### **Proteger argumentos**

``` bash
echo "El valor de \$HOME es su directorio home."
echo 'La fecha actual es $(date +%Y-%m-%d).'
MY_DATE=$(date +%Y-%m-%d)
echo "Hoy es $MY_DATE."
```

------------------------------------------------------------------------

### **Eliminar el directorio `data`**

``` bash
rm -r data
```

## **Buenas prácticas**

- Use comillas simples cuando no quiera que nada se expanda.
- Use comillas dobles cuando necesite variables pero quiera controlar el
  resto de expansiones.
- Prefiera `$( )` sobre backticks para sustitución de comandos.
- Utilice brace expansion para automatizar la creación de múltiples
  archivos.
- Verifique siempre qué archivos afectará un comodín usando
  primero `ls`.
