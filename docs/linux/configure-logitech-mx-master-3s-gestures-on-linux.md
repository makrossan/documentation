---
title: "Configurar gestos del Logitech MX Master 3S en Linux"
date: 2026-04-11T17:00:00.000Z
slug: configurar-gestos-del-logitech-mx-master-3s-en-linux
---

## Resumen rápido

En esta guía dejo el paso a paso completo para deje mi **Logitech MX
Master 3S** funcionando con **LogiOps** tanto en **RHEL 10** como en
**Fedora 43**, incluyendo los problemas que encontré y cómo los resolví.
La configuración final que buscaba era:

- **Arriba** → `Ctrl + W`
- **Abajo** → mostrar aplicaciones
- **Izquierda** → `Ctrl + C`
- **Derecha** → `Ctrl + V`
- scroll vertical con sensación por pasos, pero más responsivo

En RHEL10 estos pasos funcionaron sin ningun problema con el mouse
conectado al Bolt. Pero con el nuevo kernel de Fedora 43, el Bolt
receiver se expone el mismo, pero con bluetooth si se puede ver el mouse
directamente. 

------------------------------------------------------------------------

## Paso a paso

### 1. Instalar dependencias

``` bash
sudo dnf install -y git
sudo dnf install -y cmake gcc-c++ make libevdev-devel systemd-devel libconfig-devel glib2-devel
```

En RHEL, si hace falta habilitar CRB:

``` bash
sudo subscription-manager repos --enable codeready-builder-for-rhel-10-$(arch)-rpms
```

------------------------------------------------------------------------

### 2. Clonar el proyecto

``` bash
mkdir -p ~/repositories/github
cd ~/repositories/github
git clone https://github.com/PixlOne/logiops.git
cd logiops
```

Este paso es importante. Si no lo hago, la compilación falla porque
falta `src/ipcgull`.

``` bash
git submodule update --init --recursive
```

------------------------------------------------------------------------

### 3. Compilar e instalar

``` bash
mkdir -p build
cd build
cmake -DCMAKE_BUILD_TYPE=Release ..
make -j$(nproc)
sudo make install
```

------------------------------------------------------------------------

### 4. Habilitar el servicio

``` bash
sudo systemctl enable --now logid
systemctl status logid
```

------------------------------------------------------------------------

## Diferencias entre RHEL y Fedora

Aquí fue donde encontré la mayor diferencia.

### En RHEL 10

El mouse funcionó directamente usando el **receptor Bolt**. Al ejecutar:

``` bash
sudo /usr/local/bin/logid -v
```

el sistema detectaba correctamente: **MX Master 3S**

------------------------------------------------------------------------

### En Fedora 43

Con Bolt, muchas veces el receptor era detectado, pero el servicio se
desactivaba pocos segundos después:

`logid.service: Deactivated Successfully`

Esto hacía que los gestos funcionaran solo por unos segundos.Además, con
Bolt el sistema a veces exponía solo el receptor y no el mouse. La unica
solución aqui fue **conectar el mouse por Bluetooth en lugar de Bolt**

Una vez conectado por Bluetooth, `logid` detectó correctamente:

`Device found: MX Master 3S`

Y desde ese momento los gestos comenzaron a funcionar de forma
consistente.

------------------------------------------------------------------------

## Crear el archivo de configuración

LogiOps no crea `/etc/logid.cfg` automáticamente, así que copie el
ejemplo:

``` bash
sudo cp ~/repositories/github/logiops/logid.example.cfg /etc/logid.cfg
```

## Mi configuración final

``` bash
devices: (
{
    name: "MX Master 3S";

    dpi: 1000;

    # Clean ratchet mode (no weird behavior)
    smartshift:
    {
        on: true;
    threshold: 40;
    };

    # Disable hi-res completely (most stable behavior)
    hiresscroll:
    {
        hires: true;
        target: false;
    };

    thumbwheel:
    {
        divert: false;
    };

    buttons: (
        {
            cid: 0xc3;

            action =
            {
                type: "Gestures";

                gestures: (
                    {
                        direction: "Up";
                        mode: "OnRelease";
                        action =
                        {
                            type: "Keypress";
                            keys: ["KEY_LEFTCTRL", "KEY_W"];
                        };
                    },
                    {
                        direction: "Down";
                        mode: "OnRelease";
                        action =
                        {
                            type: "Keypress";
                            keys: ["KEY_LEFTMETA", "KEY_A"];
                        };
                    },
                    {
                        direction: "Left";
                        mode: "OnRelease";
                        action =
                        {
                            type: "Keypress";
                            keys: ["KEY_LEFTCTRL", "KEY_C"];
                        };
                    },
                    {
                        direction: "Right";
                        mode: "OnRelease";
                        action =
                        {
                            type: "Keypress";
                            keys: ["KEY_LEFTCTRL", "KEY_V"];
                        };
                    },
                    {
                        direction: "None";
                        mode: "NoPress";
                    }
                );
            };
        }
    );
}
);
```

------------------------------------------------------------------------

## Ajuste opcional del scroll en GNOME

Este comando reduce la sensibilidad del scroll wheel en el sistema. Es
opcional pero para mi fue super importante. 

``` bash
gsettings set org.gnome.desktop.peripherals.mouse speed -0.3
```

------------------------------------------------------------------------

## Reiniciar el servicio

``` bash
sudo systemctl restart logid
```

En mi caso, a veces, despues de reiniciar el servicio en RHEL, tenia que
esperar unos segundo para que el cambio tome efecto no se porque, y
muchas veces no se sentia el cambio. Pero si desconecto el mouse y lo
vuelvo a conectar, todo parece fucionar nuevamente. 

------------------------------------------------------------------------

## Validaciones útiles

Ver estado del servicio:

    systemctl status logid

Ver logs:

    journalctl -u logid -e

Volver a correr en debug si necesito revisar nombre del dispositivo o
botones:

    sudo systemctl stop logid
    sudo /usr/local/bin/logid -v

Luego volver a iniciarlo:

    sudo systemctl start logid
