---
title: "Debian - Linux Map SMB network"
date: 2025-09-14T00:00:51.000Z
slug: debian-linux-map-smb-network
---

Primero instala CIFS-UTILS

``` bash
Debian
sudo apt install -y cifs-utils
```

en /mnt crea la carpeta a ser relacionada.

``` bash
sudo mkdir /mnt/PATH
```

usa el comando para montarla

``` bash
sudo mount.cifs //FQDN o IP/ /mnt/folder/ -o user=user pass=p@ssw0rd
```

## Para montar la carpeta permanentemente

Siguiendo el ejemplo anterio, instala CIFS-UTILS, y crea la carpeta a
ser relacionada.

Seguidamente, modifica el archivo fstab

``` bash
sudo vi /etc/fstab
```

usando VI copia la siguiente linea de ejemplo al final del texto.

``` bash
//FQDN O IP/folder /mnt/folder/ -o user=user,password=p@ssw0rd,iocharset=utf8,file_mode=0777,dir_mode=0777
```
