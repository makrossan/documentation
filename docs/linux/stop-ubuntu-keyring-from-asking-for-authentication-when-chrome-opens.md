---
title: "Evitar que Ubuntu keyring pida autenticación cada vez que Chrome abre"
date: 2025-09-13T23:45:38.000Z
slug: evitar-que-ubuntu-keyring-pida-autenticacion-cada-vez-que-chrome-abre
---

El problema se debe a que el keyring de GNOME pide la contraseña para
desbloquear y proporcionar las credenciales almacenadas (como las de
Chrome). Si ya tienes un gestor de contraseñas propio, esto puede ser
muy molesto. 

Para evitar que aparezca este mensaje cada vez que abres Chrome en
Ubuntu, te ofrezco 3 opciones:

#### Opción 1

Desactivar la Solicitud de Contraseña del Keyring para Chrome.

``` `bash
sudo nano /usr/share/applications/google-chrome.desktop
```

#### Opción 2 

Estableca una Contraseña en Blanco para el Keyring.

1.  Busque "Contraseñas y Claves" en el menú de aplicaciones.
    - En el panel izquierdo, click derecho en el keyring "Login" y
      seleccione "Cambiar contraseña".  
    - Ingrese tu contraseña actual.
    - Para la nueva contraseña, déjale en blanco (simplemente presione
      \`Enter\` dos veces).
    - Confirme esta acción cuando se lo pida.  
        
2.  Reinicie la computadora para asegurarse de que los cambios tengan
    efecto.

#### Opción 3

Desbloquear Automáticamente el Keyring al Iniciar Sesión

1.  Instale \`seahorse\` (si no está instalado):  
    `sudo apt install seahorse`  
2.  Busque "Contraseñas y Claves" (o simplemente ejecute \`seahorse\`
    desde la terminal)
    - Encuentra el keyring "Login", click derecho en él y seleccione
      "Establecer como predeterminado" (si no lo está).  
3.  Vincule la contraseña del keyring con su contraseña de inicio de
    sesión:  
    - Abra la terminal y ejecuta los siguientes comandos:  
      `cp ~/.Xauthority /etc/gdm3/ sudo nano /etc/pam.d/gdm-password`  
    - Añada esta línea al final del archivo:  
      `auth optional pam_gnome_keyring.so`  
    - Guarde y cierre el archivo.
