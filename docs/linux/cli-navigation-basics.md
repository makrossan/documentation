---
title: "Como navegar el CLI"
date: 2026-02-25T16:17:08.000Z
slug: como-navegar-el-cli
---

Perfecto para acelerar su flujo de trabajo y manejar comandos con más
agilidad.

------------------------------------------------------------------------

## Navegación del cursor

- **Ctrl+A** – Mover el cursor al inicio de la línea
- **Ctrl+E** – Mover el cursor al final de la línea
- **Ctrl+Left / Alt+B** – Saltar una palabra hacia atrás
- **Ctrl+Right / Alt+F** – Saltar una palabra hacia adelante

------------------------------------------------------------------------

## Edición rápida

- **Ctrl+U** – Borrar desde el cursor hasta el inicio de la línea
- **Ctrl+K** – Borrar desde el cursor hasta el final de la línea
- **Ctrl+W** – Borrar la palabra anterior
- **Alt+D** – Borrar la palabra siguiente
- **Ctrl+T** – Intercambiar los dos últimos caracteres (muy útil para
  corregir typos)
- **Ctrl+Y** – Pegar el último texto borrado

------------------------------------------------------------------------

## Historial y búsqueda

- **Ctrl+R** – Búsqueda inversa en el historial
- **Ctrl+S** – Búsqueda hacia adelante en el historial (puede estar
  deshabilitado en algunos sistemas)
- **Ctrl+P / Up Arrow** – Comando anterior
- **Ctrl+N / Down Arrow** – Comando siguiente

------------------------------------------------------------------------

## Ejecución desde el historial

- **!!** – Repetir el último comando ejecutado
- **!texto** – Ejecutar el último comando que empieza con `texto`

------------------------------------------------------------------------

## Control del terminal

- **Ctrl+L** – Limpiar la pantalla de la terminal
- **Ctrl+C** – Cancelar el comando actual
- **Ctrl+Z** – Suspender el proceso actual y enviarlo al fondo

------------------------------------------------------------------------

## Bloque de comandos

``` bash
# Repetir el último comando
!!

# Ejecutar el último comando que empezaba con "ssh"
!ssh
```

------------------------------------------------------------------------

## **Buenas prácticas**

- Use **Ctrl+R** como atajo principal para encontrar comandos largos que
  ya ejecutó antes.
- Combine **Ctrl+U, Ctrl+W y Alt+D** para editar solo partes de la línea
  sin borrarla completa.
- Evite reescribir comandos complejos: aproveche siempre el historial y
  los atajos de navegación.
