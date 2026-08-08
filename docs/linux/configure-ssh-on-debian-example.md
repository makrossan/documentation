---
title: "Configura SSH (ejemplo con debian)"
date: 2025-09-14T00:00:27.000Z
slug: configura-ssh-ejemplo-con-debian
---

Para configurar SSH, use los siguientes pasos.

Usando la termina, instale openssh.

``` bash
sudo apt-get install openssh-server -y
```

Configure el servicio para iniciar automaticamente

``` bash
sudo systemctl enable ssh
```

Por defecto podra usarlo con autenticacion por contraseña, pero
alternativamente, se puede mejorar la seguridad al configurar
autenticacion por key.

Para crear un SSH key, user el siguiente comando y siga el asistente.

``` bash
ssh-keygen -t rsa
```

Ese public key puede ser copiado al servidor remoto usando el siguiente
comando de ejemplo.

``` bash
ssh-copy-id username@remote_host
```

Ya que tenemos el public key, podemos desabilitar la autenticacion en el
archivo de SSH.  
Abra el archivo /etc/ssh/sshd_config y configure las siguientes
opciones.

``` bash
ChallengeResponseAuthentication no
PasswordAuthentication no
UsePAM no
```

Guarde los cambio y reincie el servicio de SSH.

``` bash
sudo service ssh restart
```
