---
title: "Bookstack - Como cree la pagina de descargo de responsabilidad."
date: 2025-09-13T17:38:37.000Z
slug: como-cree-la-pagina-de-descargo-de-responsabilidad
---

Para esto basicamente lo unico que hice fue cambiar el mensaje de error
que viene por defecto al 404, y le coloque mi propio mensaje. Lo malo de
esto es que cualquier cosa 404 va a ver visto como un disclaimer, pero
eso no me importa.

1- Con esto entramos al container de Bookstack

``` bash
docker exec -it 55caab4e32971ffb85a6cd3e173e96a4f35358fe2547e09301f7428bf9d81290 /bin/bash
```

2- Con este comando buscamos dentro de la carpeta `/app` y sus
subcarpetas todos los archivos que contentan la frase "page not found”

- La opción **`r`** le indica a **`grep`** que busque de manera
  recursiva en el directorio.
- La opción **`i`** le indica a **`grep`** que busque sin hacer caso a
  mayusculas o minusculas.
- La opción **`l`** le indica a **`grep`** que solo muestre los nombres
  de los archivos que contienen

``` bash
grep -rli "page not found" /app
```

3- Seguidamente use `nano` para cambiar las siguientes lineas.

``` bash
nano /app/www/lang/en/errors.php
```

``` bash
nano /app/www/lang/es/errors.php
```

``` php
    // Error pages
    '404_page_not_found' => 'Descargo de responsabilidad:',
    'sorry_page_not_found' => 'Todo el contenido proporcionado en este sitio se ofrece "tal cual" y está destinado únicamente a fines informativos. Siempre se recomienda probar cualquier configuración o cambio en un entorno de laboratorio antes de implementarlo en un entorno de producción. El uso de este contenido es bajo su propio riesgo.',
    'sorry_page_not_found_permission_warning' => 'Tenga en cuenta que algunas páginas en estos libros han sido parcialmente asistidas por inteligencia artificial (AI). Un autor ha revisado y modificado el contenido según fuera necesario para garantizar su precisión y relevancia. Sin embargo, no se puede garantizar la exactitud completa del contenido asistido por AI. 
Al acceder y utilizar este sitio, usted acepta este descargo de responsabilidad y reconoce que es el único responsable de cualquier resultado derivado del uso de la información proporcionada aquí.',
```

``` php
    // Error pages
    '404_page_not_found' => 'Disclaimer',
    'sorry_page_not_found' => 'All content provided on this site is offered "as is" and is intended for informational purposes only. It is always recommended to test any configurations or changes in a laboratory environment before implementing them in a production environment. The use of this content is at your own risk.',
    'sorry_page_not_found_permission_warning' => 'Please note that some pages in these books have been partially assisted by artificial intelligence (AI). An author has reviewed and modified the content as necessary to ensure its accuracy and relevance. However, complete accuracy of the AI-assisted content cannot be guaranteed.
By accessing and using this site, you agree to this disclaimer and acknowledge that you are solely responsible for any outcomes resulting from the use of the information provided here.',
```

Al finalizar, reinicie el contenedor. 
