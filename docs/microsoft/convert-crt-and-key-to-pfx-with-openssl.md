---
title: "Convertir crt y key a pfx usando openssl"
date: 2025-09-13T23:37:59.000Z
slug: convertir-crt-y-key-a-pfx-usando-openssl
---

- Instale [openssl](https://slproweb.com/products/Win32OpenSSL.html) en
  la máquina cliente de Windows.
- En mi caso, para simplificar, copie el crt y la key en la siguiente
  ruta.

``` cmd
C:\Program Files\OpenSSL-Win64
```

- Luego, ejecute el siguiente comando.

``` cmd
openssl pkcs12 -export -out certificate.pfx -inkey certificate.key -in certificate.crt
```
