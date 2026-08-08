---
title: "Docker en Raspberry Pi4"
date: 2025-09-13T17:43:21.000Z
slug: docker-en-raspberry-pi4
---

Primero actualiza tu sistema

``` bash
sudo apt update
sudo apt upgrade -y
```

Instala docker

``` bash
curl -fsSL https://get.docker.com -o get-docker.sh
```

``` bash
sudo bash get-docker.sh
```

Actualiza los permisos de usuario para que no tengas que usar “sudo”
siempre que ejecutas docker.

``` bash
sudo usermod -aG docker ${USER}
```

``` bash
su - ${USER}
```

Asegurate que docker funciona correctamente probando al version.

``` bash
docker --version
```

Seguidamente instala docker-compose

``` bash
sudo apt install -y python3-pip libffi-dev
sudo pip3 install docker-compose
```

y reinicia el host para complementar.

``` bash
sudo reboot
```
