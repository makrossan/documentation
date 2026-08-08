---
title: "Zabbix Appliance sin espacio en disco (AlmaLinux + Proxmox)"
date: 2025-10-06T02:39:09.000Z
slug: zabbix-appliance-sin-espacio-en-disco-almalinux-proxmox
---

> En mi caso, descargué y estoy usando Zabbix Appliance en mi homelab,
> ya que es una de las formas más fáciles de comenzar con Zabbix. Sin
> embargo, también me di cuenta de que este appliance fue pensado como
> una demostración, y no como algo que se pueda usar de forma estable en
> un laboratorio.

<figure class="kg-card kg-bookmark-card">
<a href="https://www.zabbix.com/download_appliance"
class="kg-bookmark-container"></a>
<div class="kg-bookmark-content">
<div class="kg-bookmark-title">
Download Zabbix appliance
</div>
<div class="kg-bookmark-description">
Download and install the pre-compiled Zabbix appliance.
</div>
<div class="kg-bookmark-metadata">
<img
src="__GHOST_URL__/content/images/icon/apple-touch-icon-180x180-precomposed.png"
class="kg-bookmark-icon" /><span
class="kg-bookmark-author">Zabbix</span>
</div>
</div>
<div class="kg-bookmark-thumbnail">
<img src="__GHOST_URL__/content/images/thumbnail/flag_en.svg"
onerror="this.style.display = &#39;none&#39;" />
</div>
</figure>

El enfoque de este artículo está en las particiones de dicho appliance.
Jamás lo usaría en un ambiente de producción, aunque me pareció una
opción genial para un homelab, porque funciona out of the box.

Sin embargo, me encontré con la limitante de que las particiones son muy
pequeñas. Y para empeorar las cosas, el disco ***/dev/sda*** está
dividido en múltiples particiones contiguas. Eso significa que la
partición raíz (/dev/sda2, de 4 GB) está seguida de otras (/dev/sda3,
/dev/sda5), lo que impide ampliarla porque otra partición bloquea el
espacio libre que esta al final de disco.

``` bash
/dev/sda
├─sda1  → /boot              (512 MB)
├─sda2  → /                  (4 GB)
├─sda3  → /tmp               (1 GB)
└─sda5  → /var/lib/mysql     (4.5 GB)
```

Una alternativa habría sido borrar o mover las particiones (/tmp,
/var/lib/mysql), lo cual implicaría riesgos, ya que se pueden perder
datos fácilmente. Así que decidí simplemente agregar un nuevo disco
desde Proxmox, formatearlo, montarlo en ***/var/lib/mysql*** y mover los
datos allí.

## **Antes de comenzar: Por qué mover /var/lib/mysql  a un nuevo disco?**

La base de datos MySQL, ubicada en /var/lib/mysql, es la que más espacio
ocupa.

Al moverla a otro disco, se libera espacio en el disco original
(/dev/sda), se reduce la carga de I/O sobre el mismo volumen donde se
encuentra el sistema operativo, se evita tocar particiones críticas y,
si en el futuro / se llena nuevamente, se podrá limpiar sin afectar los
datos de Zabbix.

Además, se gana la flexibilidad para aumentar el tamaño del disco de
MySQL en el futuro sin impactar el sistema.

Perfecto, Greivin. Aquí tienes una versión en español de las
instrucciones que seguiste para mover la base de datos de Zabbix
(/var/lib/mysql) a un nuevo disco en Proxmox. Puedes usar este texto
como entrada directa para tu blog en Ghost.

------------------------------------------------------------------------

## **Cómo mover /var/lib/mysql a un nuevo disco en Zabbix Appliance**

### **1. Agregar un nuevo disco en Proxmox**

Desde la interfaz de Proxmox:

1.  Abra la pestaña **Hardware** de la máquina virtual.
2.  Hagan clic en **Add → Hard Disk**.
3.  Seleccione:
    - **Bus:** VirtIO o SCSI (dependiendo de la configuración de su VM).
    - **Tamaño:** por ejemplo, 20G.
    - **Storage:** el datastore que prefieran.
4.  Hagan clic en **Add** para crear el nuevo disco.

------------------------------------------------------------------------

### **2. Formatear el nuevo disco y montarlo temporalmente**

Supongamos que el nuevo disco aparece como /dev/sdb:

``` bash
# Crear el sistema de archivos XFS
mkfs.xfs /dev/sdb

# Crear un punto de montaje temporal
mkdir /mnt/mysql-new

# Montar el disco temporalmente
mount /dev/sdb /mnt/mysql-new
```

------------------------------------------------------------------------

### **3. Detener los servicios y copiar los datos**

Detenga los servicios activos de Zabbix y MySQL:

``` bash
systemctl stop zabbix-server
systemctl stop mysqld
```

Copie los datos actuales al nuevo disco:

``` bash
rsync -avh /var/lib/mysql/ /mnt/mysql-new/
```

------------------------------------------------------------------------

### **4. Desmontar y reemplazar /var/lib/mysql**

Si /var/lib/mysql está montado como una partición independiente
(/dev/sda5), es necesario desmontarla primero:

``` bash
umount /var/lib/mysql
```

Luego, renómbrela como respaldo:

``` bash
mv /var/lib/mysql /var/lib/mysql.bak
```

Cree nuevamente el punto de montaje y monte el nuevo disco:

``` bash
mkdir /var/lib/mysql
umount /mnt/mysql-new   # Desmontar temporal
mount /dev/sdb /var/lib/mysql
```

Corrija los permisos de los archivos:

``` bash
chown -R mysql:mysql /var/lib/mysql
```

------------------------------------------------------------------------

### **5. Iniciar nuevamente los servicios**

``` bash
systemctl start mysqld
systemctl start zabbix-server
```

Verifique que ambos servicios se inicien correctamente y que los datos
sean accesibles.

------------------------------------------------------------------------

### **6. Hacer el cambio permanente con /etc/fstab**

Edíte el archivo /etc/fstab:

``` bash
nano /etc/fstab
```

Agregue la siguiente línea al final para que el disco se monte
automáticamente en cada inicio del sistema:

``` bash
/dev/sdb   /var/lib/mysql   xfs   defaults   0 0
```

Guarde los cambios y cierren el archivo.

------------------------------------------------------------------------

### **7. Verificar el resultado**

Compruebe que el nuevo disco esté montado correctamente:

``` bash
df -hT /var/lib/mysql
```

Debería ver un resultado similar a:

``` bash
Filesystem     Type  Size  Used Avail Use% Mounted on
/dev/sdb       xfs    20G  3.9G   17G  20% /var/lib/mysql
```

------------------------------------------------------------------------

### **8. Limpieza final**

Después de confirmar que el sistema funciona correctamente durante
algunos días, se puede eliminar el respaldo anterior:

``` bash
rm -rf /var/lib/mysql.bak
```

------------------------------------------------------------------------

## **Resultado final**

Con este procedimiento, habrá migrado exitosamente la base de datos
MySQL de Zabbix a un disco nuevo, liberando espacio en la partición
principal sin necesidad de modificar el particionado original del
sistema.

Además, al tener la base de datos en un disco separado, podrán ampliar
su capacidad o realizar respaldos de manera más flexible y segura.

Perfecto. A continuación encontrará la **sección adicional** lista para
incorporar a su artículo, siguiendo el mismo estilo, formato y tono
profesional con **ustedeo**, como si fuera usted quien explica a otros
administradores de sistemas cómo mantener limpia la partición raíz.

------------------------------------------------------------------------

## **Información adicional: cómo depurar y optimizar el espacio en /dev/sda2**

Después de haber movido la base de datos MySQL al nuevo disco
(/dev/sdb), la partición raíz (/dev/sda2) puede mantenerse liviana y
estable realizando una limpieza periódica.

Este proceso ayuda a liberar espacio ocupado por archivos temporales,
cachés del sistema y registros antiguos, sin comprometer la estabilidad
del servidor.

A continuación, comparto una guía práctica y segura para entornos de
prueba.

------------------------------------------------------------------------

### **1. Limpiar la caché del sistema y de paquetes**

``` bash
# Limpiar la caché de YUM
yum clean all
rm -rf /var/cache/yum

# Eliminar la caché de DNF (si existe)
rm -rf /var/cache/dnf

# Eliminar archivos temporales
rm -rf /tmp/*
```

------------------------------------------------------------------------

### **2. Revisar registros de gran tamaño**

``` bash
du -sh /var/log/*
```

Si algún directorio de registros (por ejemplo /var/log/journal o
/var/log/zabbix) ocupa demasiado espacio, se pueden truncar o rotar los
archivos:

``` bash
# Vaciar el contenido de los logs sin eliminarlos
find /var/log -type f -name "*.log" -exec truncate -s 0 {} \;

# Limpiar registros del journal de systemd
journalctl --vacuum-time=7d
```

⚠️ Es importante **no eliminar los directorios completos** dentro de
/var/log, únicamente limpiar o rotar sus contenidos.

------------------------------------------------------------------------

### **3. Eliminar paquetes huérfanos y kernels antiguos**

``` bash
dnf remove $(dnf repoquery --installonly --latest-limit=-1 -q)
dnf autoremove -y
```

Estos comandos eliminan versiones anteriores del kernel y dependencias
que ya no se utilizan.

------------------------------------------------------------------------

### **4. Identificar directorios grandes**

``` bash
du -hxd1 / | sort -h
```

Este comando muestra cuáles son los directorios que consumen más
espacio.

Algunos de los más comunes son:

- /var/cache
- /var/log
- /usr/share
- /root (si se descargaron archivos ISO o respaldos)

Si se encuentra algo innecesario, se recomienda moverlo a un disco con
más espacio, como /dev/sdb, creando un directorio adicional, por ejemplo
/data.

------------------------------------------------------------------------

### **5. Limpiar registros del sistema y volcados de fallos**

``` bash
rm -rf /var/crash/*
journalctl --vacuum-size=100M
```

Esto elimina archivos de registro excesivamente grandes y volcados de
memoria que el sistema conserva tras reinicios inesperados.

------------------------------------------------------------------------

### **6. (Opcional) Limpiar cachés de paquetes**

``` bash
rm -rf /root/.cache/*
rm -rf /var/tmp/*
```

Estas carpetas suelen acumular archivos temporales que no son críticos
para el funcionamiento del sistema.

------------------------------------------------------------------------

### **7. Verificar el espacio libre**

Finalmente, es recomendable comprobar el espacio disponible:

``` bash
df -h /
```

El resultado esperado debería mostrar una reducción significativa en el
uso de la partición raíz:

``` bash
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda2       4.0G  2.1G  1.9G  53% /
```

------------------------------------------------------------------------
