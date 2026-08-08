---
title: "Instala Docker en Windows"
date: 2025-09-13T17:41:49.000Z
slug: instala-docker-en-windows
---

Para este ejemplo estaremos usando [Docker
Desktop](https://www.docker.com/products/docker-desktop/).
Alternativamente, si los requisitos para Docker Desktop no son
alcanzado, se puede instalar [Docker
Toolbox](https://docs.docker.com/toolbox/toolbox_install_windows/). 

Requisitos: 

\- Docker Desktop para Windows utiliza Hyper-V en Windows 10  
- Pro/Enterprise/Education usa Hyper-V (para habilitarlo has esto)  
- Home usa WSL 2 (Build 19018 o posterior) (has esto para habilitarlo y
convertirlo en el motor predeterminado)  
- Virtualización habilitada en la BIOS. (asi fue como yo lo hice cd
/volume1/homes/gvenegas/videos/youtube/ && mkdir '15004 - asi es como
activo la virtualizacion en la BIOS de mi computadora’)  
- Al menos 4GB de RAM.

##### Docker Toolbox (Para versiones antiguas de Windows)

Si tienes una versión más antigua de Windows que no soporta Docker
Desktop o WSL 2, como Windows 7 o Windows 8, puedes utilizar Docker
Toolbox.  
    1. Descarga Docker Toolbox desde el repositorio de
[GitHub](https://docs.docker.com/toolbox/toolbox_install_windows/) o
desde la página de
[Docker](https://docs.docker.com/toolbox/toolbox_install_windows/).  
    2. Ejecuta el instalador y segue las instrucciones, que incluyen
aceptar la licencia y seleccionar los componentes a instalar, como
VirtualBox y Git for Windows.  
    3. Ejecuta Docker QuickStart Terminal después de la instalación para
lanzar un entorno pre-configurado.

##### Docker desktop

    1. buscar el instalador en google o directamente
[https://www.docker.com/products/docker-desktop/ ](https://www.docker.com/products/docker-desktop/)  
    2. si pide activar la virtualizacion en la BIOS, seguir estas
instrucciones comunes:
[Dell](https://www.dell.com/support/kbdoc/es-pr/000195978/c%C3%B3mo-habilitar-o-deshabilitar-la-virtualizaci%C3%B3n-de-hardware-en-sistemas-dell),
[HP](https://support.hp.com/ve-es/document/ish_5637144-5698274-16),
[Lenovo](https://support.lenovo.com/bo/es/solutions/ht500006-how-to-enable-virtualization-technology-on-lenovo-computers)...  
    3. al instalarlo, se recomienda iniciar session con una cuenta,
aunque no es completamente necessario. Pero a veces es necesario
reininiciar la computadora.   
    4. una vez instalado. Esto iniciará el daemon de Docker. Si ves un
mensaje de "Docker is running", significa que la instalación fue
exitosa.  

Si quieres aprender a instalar tu primera aplicacion, te recomiendo un
video de la siguiente [lista en
YouTube](https://libreria.greivinvenegas.com/Docker%20https:/www.youtube.com/playlist?list=PLM3kkICu9CaiVy8fN03nYkJBWrTSWd4Xt). 
