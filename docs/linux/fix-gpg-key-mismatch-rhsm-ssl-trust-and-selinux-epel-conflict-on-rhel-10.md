---
title: "GPG key mismatch, RHSM SSL trust y conflicto SELinux/EPEL en RHEL 10"
date: 2026-03-26T00:12:41.000Z
slug: gpg-key-mismatch-rhsm-ssl-trust-y-conflicto-selinux-epel-en-rhel-10
---

Me encontré con un problema que al parecer es bastante común en
instalaciones nuevas de RHEL 10 Developer Subscription o en VMs
importadas, por ejemplo desde Proxmox.

El sistema sí tenía llaves GPG instaladas, pero no eran las correctas
para los paquetes actuales del repositorio. Por eso apareció este error:
`The GPG keys listed ... are already installed but they are not correct for this package`

Luego también salió un problema de SSL con RHSM:
`SSL certificate problem: self-signed certificate in certificate chain`

Y después, al avanzar, apareció otro error relacionado con dependencias
protegidas de SELinux:
`Problem: The operation would result in removing the following protected packages: selinux-policy-targeted`

Al final, no era un solo fallo, sino una cadena de tres problemas:
llaves GPG incorrectas, un problema de confianza SSL con
subscription-manager, y EPEL habilitado sin CRB, que en RHEL 10.1 hace
falta para resolver bien varias dependencias.

------------------------------------------------------------------------

## Pasos tomados para resolverlo

### 1. Ver qué llaves GPG había instaladas

``` bash
rpm -qa gpg-pubkey*
```

### **2. Eliminar las llaves antiguas**

Fue necesario eliminarlas individualmente, por ejemplo:

``` bash
sudo rpm -e gpg-pubkey-fd431d51-4ae0493b
sudo rpm -e gpg-pubkey-05707a62-68e6a1f3
...
```

### **3. Reimportar la llave oficial de Red Hat**

``` bash
sudo rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release
```

### **4. Limpiar DNF**

``` bash
sudo dnf clean all
sudo rm -rf /var/cache/dnf
```

### **5. Inspeccionar el problema más a fondo**

Intentar descargar e inspeccionar un paquete manualmente:

``` bash
sudo dnf download kernel
rpm -Kv kernel-*.rpm
```

Cuando esto falla por metadata, queda claro que el problema ya no era
solo GPG.

### **6. Probar SSL manualmente**

``` bash
curl -v https://cdn.redhat.com
openssl s_client -connect cdn.redhat.com:443 -showcerts
openssl s_client -connect cdn.redhat.com:443 -CAfile /etc/rhsm/ca/redhat-uep.pem </dev/null
curl -v https://subscription.rhsm.redhat.com/subscription/ --cacert /etc/rhsm/ca/redhat-uep.pem
```

Estas pruebas mostraron que:

- la validación genérica falla
- pero RHSM sí validaba correctamente con redhat-uep.pem

### **7. Regenerar repositorios RHSM**

Pero primero, hay que hacer un respaldo del respositorio, por eso la
primera linea.

``` bash
sudo cp -a /etc/yum.repos.d/redhat.repo /etc/yum.repos.d/redhat.repo.bak
sudo subscription-manager refresh
sudo subscription-manager repos \
  --disable='*' \
  --enable='rhel-10-for-x86_64-baseos-rpms' \
  --enable='rhel-10-for-x86_64-appstream-rpms'
```

### **8. Reconstruir caché**

``` bash
sudo dnf makecache
```

En este punto, el problema SSL quedó resuelto. Pero como tambien estoy
usando el repositorio EPEL, fue necesario el siguiente paso.

### **9. Resolver el conflicto final con EPEL y SELinux**

Como EPEL seguía habilitado, apareció este error:

``` bash
Problem: The operation would result in removing the following protected packages: selinux-policy-targeted
```

La solución fue habilitar CRB y sincronizar paquetes:

``` bash
sudo subscription-manager repos --enable=codeready-builder-for-rhel-10-x86_64-rpms
sudo dnf clean all
sudo rm -rf /var/cache/dnf
sudo dnf makecache
sudo dnf distro-sync
```

Con eso quedó resuelto el problema por completo.

## **Bloque final de comandos**

``` bash
rpm -qa gpg-pubkey*
sudo rpm -e gpg-pubkey-fd431d51-4ae0493b
sudo rpm -e gpg-pubkey-05707a62-68e6a1f3
sudo rpm -e gpg-pubkey-e37ed158-65785fa9
sudo rpm -e gpg-pubkey-f21541eb-49a40330
sudo rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release
sudo dnf clean all
sudo rm -rf /var/cache/dnf
curl -v https://cdn.redhat.com
openssl s_client -connect cdn.redhat.com:443 -showcerts
openssl s_client -connect cdn.redhat.com:443 -CAfile /etc/rhsm/ca/redhat-uep.pem </dev/null
curl -v https://subscription.rhsm.redhat.com/subscription/ --cacert /etc/rhsm/ca/redhat-uep.pem
sudo cp -a /etc/yum.repos.d/redhat.repo /etc/yum.repos.d/redhat.repo.bak
sudo subscription-manager refresh
sudo subscription-manager repos \
  --disable='*' \
  --enable='rhel-10-for-x86_64-baseos-rpms' \
  --enable='rhel-10-for-x86_64-appstream-rpms'
sudo subscription-manager repos --enable=codeready-builder-for-rhel-10-x86_64-rpms
sudo dnf clean all
sudo rm -rf /var/cache/dnf
sudo dnf makecache
sudo dnf distro-sync
```

Basado en bloque final de comando, tambien anexo este playbook.

<div class="kg-card kg-file-card">

<a
href="__GHOST_URL__/content/files/2026/03/rhel-dnf-update-ssl_rhsm-gpg_key-fix.yaml"
class="kg-file-card-container" download="" title="Download"></a>

<div class="kg-file-card-contents">

<div class="kg-file-card-title">

rhel-dnf-update-ssl_rhsm-gpg_key-fix

</div>

<div class="kg-file-card-caption">

</div>

<div class="kg-file-card-metadata">

<div class="kg-file-card-filename">

rhel-dnf-update-ssl_rhsm-gpg_key-fix.yaml

</div>

<div class="kg-file-card-filesize">

5 KB

</div>

</div>

</div>

<div class="kg-file-card-icon">

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiPjxkZWZzPjxzdHlsZT4uYXtmaWxsOm5vbmU7c3Ryb2tlOmN1cnJlbnRDb2xvcjtzdHJva2UtbGluZWNhcDpyb3VuZDtzdHJva2UtbGluZWpvaW46cm91bmQ7c3Ryb2tlLXdpZHRoOjEuNXB4O308L3N0eWxlPjwvZGVmcz48dGl0bGU+ZG93bmxvYWQtY2lyY2xlPC90aXRsZT48cG9seWxpbmUgY2xhc3M9ImEiIHBvaW50cz0iOC4yNSAxNC4yNSAxMiAxOCAxNS43NSAxNC4yNSI+PC9wb2x5bGluZT48bGluZSBjbGFzcz0iYSIgeDE9IjEyIiB5MT0iNi43NSIgeDI9IjEyIiB5Mj0iMTgiPjwvbGluZT48Y2lyY2xlIGNsYXNzPSJhIiBjeD0iMTIiIGN5PSIxMiIgcj0iMTEuMjUiPjwvY2lyY2xlPjwvc3ZnPg==)

</div>

</div>

## **Rollback**

``` bash
cp -a /etc/yum.repos.d/redhat.repo.bak /etc/yum.repos.d/redhat.repo
subscription-manager repos --disable='*'
subscription-manager repos --enable='rhel-10-for-x86_64-baseos-rpms'
subscription-manager repos --enable='rhel-10-for-x86_64-appstream-rpms'
dnf clean all
rm -rf /var/cache/dnf
```
