---
title: "Ubuntu - Como instalar OBS"
date: 2025-09-13T23:45:07.000Z
slug: ubuntu-como-instalar-obs
---

Para instalar OBS en Ubuntu, puedes seguir los siguientes pasos:

### 1. **Actualizar los Repositorios**

Antes de instalar OBS, es recomendable asegurarse de que tu sistema esté
actualizado. Abre una terminal y ejecuta:

``` bash
sudo apt update && sudo apt upgrade -y 
```

### 2. **Agregar el PPA de OBS**

OBS Studio se encuentra en un PPA (Personal Package Archive) que puedes
añadir a tu sistema. Para agregar el PPA, ejecuta:

``` bash
sudo add-apt-repository ppa:obsproject/obs-studio 
```

### 3. **Actualizar los Repositorios (Nuevamente)**

Después de añadir el PPA, necesitas actualizar los repositorios de nuevo
para incluir el nuevo software:

``` bash
sudo apt update 
```

### 4. **Instalar OBS Studio**

Ahora, puedes proceder con la instalación de OBS Studio:

``` bash
sudo apt install obs-studio -y 
```

### **Notas Adicionales:**

- **Dependencias**: Durante la instalación, OBS instalará
  automáticamente todas las dependencias necesarias.
- **GPU**: Si tienes una GPU dedicada, asegúrate de que los
  controladores estén correctamente instalados para obtener un mejor
  rendimiento con OBS.
