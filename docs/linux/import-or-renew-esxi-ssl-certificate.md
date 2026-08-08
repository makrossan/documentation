---
title: "ESXi — Importar o renovar el certificado SSL (paso a paso)"
date: 2025-09-26T01:00:00.000Z
slug: esxi-importar-o-renovar-el-certificado-ssl-paso-a-paso
---

Esta guía le muestra dos caminos para actualizar el certificado de su
host ESXi: (A) firmar el CSR generado por ESXi directamente en pfSense,
y (B) reemplazar manualmente los archivos `rui.crt` y `rui.key`. Incluye
respaldo, verificación y solución de errores.

## Antes de comenzar

### Requisitos

- Acceso por SSH al host ESXi o acceso por consola directa.
- Para el método B, disponer de un certificado (`.crt` o `.pem`) y su
  clave privada (`.key`).
- Los archivos deben llamarse exactamente `rui.crt` y `rui.key`.

### Respaldo (recomendado)

Antes de realizar cambios, haga copia de los certificados actuales:

``` bash
cp /etc/vmware/ssl/rui.crt /etc/vmware/ssl/rui.crt.bak
cp /etc/vmware/ssl/rui.key /etc/vmware/ssl/rui.key.bak
```

Nota: no es necesario crear un archivo PEM combinado si va a usar el CSR
generado por ESXi; puede firmarlo en pfSense y luego importarlo.

### Ruta rápida en la UI

Para agregar o administrar certificados desde la interfaz web del host,
visite:

`/ui/#/host/manage/security/certificates`

Después de importar, es posible que su navegador (por ejemplo, Chrome)
no recargue correctamente la página. Reiniciar el navegador puede no ser
suficiente; si persiste, reinicie el equipo.

## Método A — Firmar el CSR de ESXi en pfSense (recomendado)

1.  **Genere el CSR en ESXi.** Desde la UI del host, cree la solicitud
    de firma (CSR) y descárguela.
2.  **Firme el CSR en pfSense.** Use el gestor de certificados de
    pfSense (CA propia o intermedia) para emitir el certificado.
3.  **Importe el certificado firmado en ESXi.** Vuelva
    a `/ui/#/host/manage/security/certificates` y cargue el certificado
    (y cadena si aplica).
4.  **Reinicie los agentes de gestión.**

``` bash
/etc/init.d/hostd restart
/etc/init.d/vpxa restart
```

Ventaja: la clave privada no sale del host ESXi, disminuyendo el riesgo
de desajustes.

## Método B — Reemplazo manual de `rui.crt` y `rui.key`

### 1) Cargue los archivos al host

Transfiera `rui.crt` y `rui.key` (por ejemplo, a `/tmp`):

``` bash
scp rui.crt root@ESXI_HOST_IP:/tmp
scp rui.key root@ESXI_HOST_IP:/tmp
```

### 2) Muévalos al directorio correcto

``` bash
mv /tmp/rui.crt /etc/vmware/ssl/rui.crt
mv /tmp/rui.key /etc/vmware/ssl/rui.key
```

### 3) Ajuste permisos mínimos

``` bash
chmod 400 /etc/vmware/ssl/rui.*
```

### 4) Reinicie servicios

``` bash
/etc/init.d/hostd restart
/etc/init.d/vpxa restart
```

## Verificación del certificado y del par

### Ver qué certificado presenta ESXi (puerto 443)

``` bash
echo | openssl s_client -connect ESXI_HOST_IP:443 | openssl x509 -noout -text
```

Reemplace `ESXI_HOST_IP` por la IP o el FQDN de su host.

### Comprobar que el certificado y la clave coinciden

Los hashes (MD5 del módulo) de ambos comandos deben ser iguales:

``` bash
openssl x509 -noout -modulus -in /etc/vmware/ssl/rui.crt  | md5sum
openssl rsa  -noout -modulus -in /etc/vmware/ssl/rui.key  | md5sum
```

## Problemas frecuentes y soluciones

### La UI no carga después de importar

- Borre caché del navegador y vuelva a intentar.
- Si no basta, reinicie el equipo para actualizar el almacén de
  certificados del sistema.

### No puede iniciar sesión en la web después del cambio

- Verifique que `hostd` y `vpxa` estén activos y sin errores.
- Compruebe la hora/fecha del host (rango de validez del certificado).
- Si usó reemplazo manual y necesita revertir, restaure los
  respaldos `.bak` y reinicie servicios.
- Si no puede acceder porque estuvo haciendo pruebas de conexión, es muy
  posible que su cuenta esté bloqueada. Utilice el siguiente comando
  para verificar los registros y confirmar si está bloqueada.

``` bash
tail -n 200 /var/log/hostd.log | grep -Ei "auth|fail|lock"
tail -n 200 /var/log/auth.log   | grep -Ei "auth|fail|lock"
```

- Si está bloqueada, y no ha perdido conexion con su SSH, puede limpiar
  el bloqueo inmediatamente, de lo contrario debera hacerlo directamente
  en la consola.

``` bash
pam_tally2 --user root
pam_tally2 --user root --reset
```

## Notas y recordatorios

Los certificados expiran; lleve control de fechas y renueve con
antelación.

- Si usa CA propia (pfSense), conserve la cadena completa (raíz +
  intermedias).
- El Método A suele ser más seguro y menos propenso a errores de
  coincidencia de clave.

Para verificar el estado desde un navegador, acceda al host ESXi por
HTTPS y confirme que el certificado presentado es el nuevo.
