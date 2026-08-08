---
title: "Debian - Install AppImageLaucher"
date: 2025-09-13T23:56:57.000Z
slug: debian-install-appimagelaucher
---

Open your terminal.

``` bash
sudo apt install software-properties-common
```

For debian download the official .deb package for AppImageLauncher:

``` bash
wget https://github.com/TheAssassin/AppImageLauncher/releases/download/continuous/appimagelauncher_2.2.0-gha111.d9d4c73+bionic_amd64.deb
```

Now, try installing the downloaded package again using dpkg:

``` bash
sudo dpkg -i appimagelauncher_2.2.0-gha111.d9d4c73+bionic_amd64.deb
```

If you encounter any missing dependency errors during the installation,
you can try running:

``` bash
sudo apt-get -f install
```

Once the installation is successful, you can update the desktop
database:

``` bash
update-desktop-database
```

This should install AppImageLauncher on your Debian system.   
