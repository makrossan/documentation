---
title: "Comando for"
date: 2025-09-14T00:40:57.000Z
slug: comando-for
---

Estaba bajando muchos archivos .wav con su licensia .pdf. Y estos los
estaba guardando en una carpeta. 

Resulta que estos archivos viene con un nombre que usa esta expresion "

Eso es muy incomodo e innecesariamente repetitivo, asi que usando el
fomando `for` pude renombrar cientos de archivos para que solo contentan
la descripcion y borrar el resto. 

``` bash
for file in *.wav *.pdf; do
    if [[ "$file" =~ ^[0-9]{8}__ ]]; then
        mv "$file" "${file:10}"
    fi
done
```

### Explicación

- `for file in *.wav *.pdf; do`: Itera sobre todos los archivos `.wav` y
  `.pdf` en el directorio actual.
- `if [[ "$file" =~ ^[0-9]{8}__ ]]; then`: Comprueba si el nombre del
  archivo comienza con 8 dígitos seguidos de `__`.
- `mv "$file" "${file:10}"`: Usa `mv` para renombrar el archivo,
  quitando los primeros 10 caracteres (`${file:10}`).
