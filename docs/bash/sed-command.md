---
title: "Comando sed"
date: 2025-09-14T00:06:45.000Z
slug: comando-sed
---

`sed` es un editor de flujo utilizado para editar texto a medida que se
procesa. Aquí están sus usos principales:

- **Print** (Imprimir): Muestra la salida basada en un patrón.
- **Delete** (Eliminar): Borra el texto que coincide con un patrón.
- **Substitute** (Sustituir): Reemplaza un patrón con otro.

Puede manejar expresiones regulares básicas y extendidas, lo que lo
convierte en una herramienta poderosa para la manipulación de texto en
Linux.

Considere el archivo anexo. 

A estos numero de telefonos, podemos agregarles codigo de pais,
parentesis y guion para reformarlo apropiadamente. 

Si `telefonos.txt` tiene una línea como: `1123456789` después de
ejecutar el comando, se transformaría en: `+55(11)2345-6789`

``` bash
sed -E 's/([0-9]{2})([0-9]{4})([0-9]{4})/+55(\1)\2-\3/' telefonos.txt
```

Vamos a desglosarlo:

1.  **`sed -E`**:
    - La opción `-E` habilita expresiones regulares extendidas, lo que
      permite patrones de coincidencia más potentes sin la necesidad de
      escapar caracteres como `+` o `?`.
2.  **`s/([0-9]{2})([0-9]{4})([0-9]{4})/`**:Cada `([0-9]{...})` captura
    el grupo de números correspondiente (1, 2 y 3) para usarlos en la
    parte de reemplazo. (esto es secuencial y por lo que vi no se puede
    reemplazar)
    - La estructura `s/.../.../` es la sintaxis para sustitución en
      `sed`, donde el patrón a la izquierda es reemplazado por el
      formato especificado a la derecha.
    - **`([0-9]{2})`**: Coincide con los dos primeros dígitos, que
      representan el código de área del estado.
    - **`([0-9]{4})`**: Coincide con los siguientes cuatro dígitos, que
      representan el prefijo.
    - **`([0-9]{4})`**: Coincide con los últimos cuatro dígitos, que
      representan el número final.
3.  **Patrón de reemplazo `+55(\1)\2-\3/`**:
    - **`+55`**: Agrega el prefijo de código de país al inicio.
    - **`(\1)`**: Coloca el primer grupo (el código de área) entre
      paréntesis.
    - **`\2`**: Inserta el segundo grupo (el prefijo) tal como está.
    - **`-`**: Coloca un guion entre el segundo y el tercer grupo.
    - **`\3`**: Inserta el tercer grupo (el número final).
4.  **`telefonos.txt`**:
    - Es el archivo de entrada que contiene los números de teléfono.
      `sed` aplica el formato especificado a cada línea del archivo.
