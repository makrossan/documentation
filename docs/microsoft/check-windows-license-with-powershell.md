---
title: "Comando powershell para ver la licensia usada en Windows"
date: 2025-09-13T23:37:27.000Z
slug: comando-powershell-para-ver-la-licensia-usada-en-windows
---

``` powershell
(Get-WmiObject -Query 'select * from SoftwareLicensingService').OA3xOriginalProductKey
```

Este comando mostrará la clave del producto de Windows asociada con tu
sistema.
