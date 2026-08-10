---
title: AWK Cheat Sheet
description: A complete interactive AWK quick reference.
hide:
  - navigation
  - toc
---

<div class="cheatsheet-page cheatsheet-page--awk">
<main class="outer">
    <header class="page-header">
      <div class="page-title">
        <span class="overline">AWK · FIELD NOTES</span>
        <h1>Hoja de trucos AWK</h1>
        <p>Del primer filtro a programas completos, organizado para consulta rápida y uso diario.</p>
      </div>
      <div class="header-right">
        <a href="/#cheat-sheets" class="back-button">Volver al Dashboard anterior</a>
        <div class="mode-pill-row" aria-label="Compatibilidad">
          <div class="mode-pill"><span class="key">awk</span><span>POSIX</span></div>
          <div class="mode-pill"><span class="key">gawk</span><span>GNU</span></div>
          <div class="mode-pill"><span class="key">mawk</span><span>Rápido</span></div>
        </div>
      </div>
    </header>

    <nav class="tab-shell" aria-label="Categorías de la hoja de trucos">
      <div class="tab-intro">
        <span>ÍNDICE</span>
        <small>← → para navegar</small>
      </div>
      <div class="tabs" id="tabs" role="tablist" aria-label="Temas de AWK"></div>
    </nav>

    <section class="section tabcontent" id="topic-panel" role="tabpanel" tabindex="0">
      <div class="section-header" id="section-header"></div>
      <div class="section-body">
        <div class="note" id="topic-note"></div>
        <div class="grid" id="topic-grid"></div>
      </div>
    </section>

    <footer class="page-footer">
      <div>
        <span class="footer-mark" aria-hidden="true">AWK</span>
        <p><strong>¿Necesita profundizar?</strong> Consulte el manual completo de GNU AWK para detalles, casos límite y extensiones.</p>
      </div>
      <a href="https://www-zeuthen.desy.de/dv/documentation/unixguide/infohtml/gawk/gawk.html" target="_blank" rel="noreferrer">
        Abrir la documentación <span aria-hidden="true">↗</span>
      </a>
    </footer>
  </main>
</div>

<script>
"use strict";

    const topics = [{"id":"getting-started","label":"Getting started","eyebrow":"01 · FUNDAMENTOS","title":"Primeros pasos con AWK","tag":"De cero a un programa útil","icon":"A","note":"AWK lee una entrada registro por registro, prueba cada patrón y ejecuta su acción. Si omite el patrón, la acción siempre se ejecuta; si omite la acción, AWK imprime el registro.","cards":[{"title":"Formas de invocación","entries":[{"code":"awk 'programa' archivo","description":"Ejecutar un programa corto sobre un archivo."},{"code":"awk 'programa' archivo1 archivo2","description":"Procesar varios archivos como una sola secuencia."},{"code":"awk -F: '{ print $1 }' /etc/passwd","description":"Definir el separador de campos con -F."},{"code":"awk -v limite=10 '$3 > limite' datos","description":"Pasar una variable antes de ejecutar BEGIN."},{"code":"awk -f programa.awk datos","description":"Cargar el programa desde un archivo."},{"code":"comando | awk '{ print $1 }'","description":"Leer desde la salida estándar de otro comando."}]},{"title":"Modelo de ejecución","entries":[{"code":"BEGIN { ... }","description":"Ejecutar una vez antes de leer la entrada."},{"code":"patrón { acción }","description":"Evaluar una vez por cada registro de entrada."},{"code":"END { ... }","description":"Ejecutar una vez al terminar o al llamar exit."},{"code":"patrón","description":"Acción implícita: { print $0 }."},{"code":"{ acción }","description":"Patrón implícito: verdadero para cada registro."},{"code":"# comentario","description":"Comentario desde # hasta el final de la línea."}]},{"title":"Registros y campos esenciales","entries":[{"code":"$0","description":"Registro completo actual."},{"code":"$1 … $NF","description":"Primer campo hasta el último campo."},{"code":"NF","description":"Número de campos del registro actual."},{"code":"NR","description":"Número acumulado del registro entre todos los archivos."},{"code":"FNR","description":"Número de registro dentro del archivo actual."},{"code":"FS / OFS","description":"Separador de campos de entrada / salida."},{"code":"RS / ORS","description":"Separador de registros de entrada / salida."}]},{"title":"Opciones que conviene memorizar","entries":[{"code":"-F 'regex'","description":"Configurar FS desde la línea de comandos."},{"code":"-v nombre=valor","description":"Asignar una variable antes de BEGIN."},{"code":"-f archivo.awk","description":"Leer el programa desde un archivo."},{"code":"-f uno.awk -f dos.awk","description":"Combinar varios archivos de programa."},{"code":"gawk --lint","description":"Avisar sobre construcciones dudosas o no portables."},{"code":"gawk --posix","description":"Restringir extensiones y priorizar POSIX."}]},{"title":"Script completo mínimo","code":"#!/usr/bin/awk -f\n\nBEGIN {\n    FS = \",\"\n    OFS = \"\t\"\n}\n\nNR > 1 && $3 >= 70 {\n    total += $3\n    aprobados++\n    print $1, $3\n}\n\nEND {\n    if (aprobados)\n        printf \"Promedio: %.2f\n\", total / aprobados\n}","caption":"Guárdelo como reporte.awk, aplique chmod +x y ejecútelo con ./reporte.awk datos.csv.","wide":true}]},{"id":"regex","label":"Regex","eyebrow":"02 · COINCIDENCIAS","title":"Expresiones regulares","tag":"ERE de POSIX y patrones dinámicos","icon":"/","note":"AWK usa expresiones regulares extendidas (ERE). Un literal /regex/ prueba $0; los operadores ~ y !~ permiten probar cualquier cadena o campo.","cards":[{"title":"Uso básico","entries":[{"code":"/error/","description":"Registros cuyo $0 contiene error."},{"code":"$2 ~ /^[A-Z]/","description":"El segundo campo comienza con mayúscula."},{"code":"$3 !~ /^(ok|ready)$/","description":"El tercer campo no es exactamente ok ni ready."},{"code":"pat = \"warn|fail\"; $0 ~ pat","description":"Expresión regular dinámica almacenada en una variable."},{"code":"tolower($0) ~ /error/","description":"Búsqueda insensible a mayúsculas portable."},{"code":"gawk 'BEGIN { IGNORECASE=1 } /error/'","description":"Coincidencia global sin distinguir mayúsculas en gawk."}]},{"title":"Metacaracteres ERE","entries":[{"code":".","description":"Cualquier carácter individual."},{"code":"^ / $","description":"Inicio / fin de la cadena."},{"code":"* / + / ?","description":"Cero o más / uno o más / cero o uno."},{"code":"{m,n}","description":"Entre m y n repeticiones (POSIX moderno)."},{"code":"[abc] / [^abc]","description":"Clase positiva / clase negada."},{"code":"(uno|dos)","description":"Agrupación y alternancia."},{"code":"\\.","description":"Punto literal; escape el metacarácter."}]},{"title":"Clases POSIX portables","entries":[{"code":"[[:alpha:]]","description":"Letra según la configuración regional."},{"code":"[[:digit:]]","description":"Dígito decimal."},{"code":"[[:alnum:]]","description":"Letra o dígito."},{"code":"[[:space:]]","description":"Espacio, tabulación o salto de línea."},{"code":"[[:blank:]]","description":"Espacio horizontal o tabulación."},{"code":"[[:lower:]] / [[:upper:]]","description":"Minúscula / mayúscula."},{"code":"[[:xdigit:]]","description":"Dígito hexadecimal."}]},{"title":"match, RSTART y RLENGTH","entries":[{"code":"match(s, /re/)","description":"Posición de la primera coincidencia o 0."},{"code":"RSTART","description":"Índice inicial de la última coincidencia."},{"code":"RLENGTH","description":"Longitud de la última coincidencia; -1 si no hubo."},{"code":"substr(s, RSTART, RLENGTH)","description":"Extraer exactamente el texto encontrado."},{"code":"match(s, /([0-9]+)/, m)","description":"gawk: guardar coincidencia y grupos capturados en m."}]},{"title":"Recetas con regex","code":"# Líneas vacías o solo con espacios\n/^[[:space:]]*$/\n\n# IPv4 aproximada al inicio del registro\nmatch($0, /^([0-9]{1,3}.){3}[0-9]{1,3}/)\n\n# Extraer todos los números de una línea\n{\n    s = $0\n    while (match(s, /[0-9]+([.][0-9]+)?/)) {\n        print substr(s, RSTART, RLENGTH)\n        s = substr(s, RSTART + RLENGTH)\n    }\n}","wide":true}]},{"id":"reading-files","label":"Reading Files","eyebrow":"03 · ENTRADA","title":"Lectura de archivos y flujos","tag":"Campos, registros y getline","icon":"R","note":"FS divide registros en campos y RS divide la entrada en registros. Cambiarlos en BEGIN suele ser la opción más clara; getline se reserva para entradas adicionales o control explícito.","cards":[{"title":"Varios archivos","entries":[{"code":"FILENAME","description":"Nombre del archivo de entrada actual."},{"code":"NR == FNR","description":"Verdadero mientras se procesa el primer archivo."},{"code":"FNR == 1","description":"Primera línea de cada archivo."},{"code":"ARGC / ARGV","description":"Cantidad y vector de argumentos de la invocación."},{"code":"ARGIND","description":"gawk: índice de ARGV del archivo actual."},{"code":"next","description":"Saltar el resto de reglas para este registro."},{"code":"nextfile","description":"Dejar de leer el archivo actual y abrir el siguiente."}]},{"title":"Separadores de entrada","entries":[{"code":"FS = \",\"","description":"Separar campos por una coma literal."},{"code":"FS = \"[[:space:]]+\"","description":"Separar por uno o más espacios POSIX."},{"code":"FS = \"\"","description":"gawk/mawk: separar cada carácter; no es POSIX."},{"code":"RS = \"\"","description":"Modo párrafo: registros separados por líneas vacías."},{"code":"RS = \"END|STOP\"","description":"gawk: RS puede ser una expresión regular."},{"code":"RT","description":"gawk: texto que coincidió con RS."}]},{"title":"Campos especiales de gawk","entries":[{"code":"FIELDWIDTHS = \"5 10 8\"","description":"Dividir por anchos fijos en lugar de FS."},{"code":"FPAT = \"([^,]+)|(\\\"[^\\\"]+\\\")\"","description":"Definir qué constituye un campo, útil para CSV simple."},{"code":"patsplit(s, a, fpat, seps)","description":"Separar por contenido de campo y guardar separadores."},{"code":"split(s, a, fs, seps)","description":"gawk: dividir y capturar separadores coincidentes."}]},{"title":"Variantes de getline","entries":[{"code":"getline","description":"Leer el siguiente registro en $0 y recalcular NF."},{"code":"getline variable","description":"Leer en variable sin modificar $0 ni NF."},{"code":"getline variable \u003c archivo","description":"Leer de otro archivo; pruebe el valor de retorno."},{"code":"comando | getline variable","description":"Leer una línea de la salida de un comando."},{"code":"resultado = getline variable","description":"Guardar el estado: 1 leído, 0 fin de archivo, -1 error."},{"code":"close(archivo_o_comando)","description":"Cerrar un recurso para evitar descriptores agotados."}]},{"title":"Cruzar dos archivos por clave","code":"# usuarios.txt: id nombre\n# ventas.txt:  id importe\nawk '\n    NR == FNR { nombre[$1] = $2; next }\n    $1 in nombre { total[nombre[$1]] += $2 }\n    END {\n        for (persona in total)\n            print persona, total[persona]\n    }\n' usuarios.txt ventas.txt","caption":"NR == FNR carga el primer archivo; next evita que ese registro pase a las reglas de ventas.","wide":true}]},{"id":"patterns-actions-variables","label":"Patterns, Actions, and Variables","eyebrow":"04 · ESTRUCTURA","title":"Patrones, acciones y variables","tag":"El corazón del lenguaje","icon":"P","note":"Cada regla tiene la forma patrón { acción }. Las reglas se prueban en orden para el mismo registro, salvo que next, nextfile o exit cambien el flujo.","cards":[{"title":"Clases de patrón","entries":[{"code":"BEGIN / END","description":"Antes de la entrada / después de toda la entrada."},{"code":"BEGINFILE / ENDFILE","description":"gawk: antes y después de cada archivo."},{"code":"/regex/","description":"Coincidencia contra $0."},{"code":"$3 > 100","description":"Expresión booleana."},{"code":"/inicio/, /fin/","description":"Rango inclusivo con estado entre dos patrones."},{"code":"pat1 && pat2","description":"Componer condiciones con lógica booleana."}]},{"title":"Variables integradas de campos","entries":[{"code":"FS / OFS","description":"Separador de campos de entrada / salida."},{"code":"RS / ORS","description":"Separador de registros de entrada / salida."},{"code":"NF / NR / FNR","description":"Campos actuales / registro total / registro del archivo."},{"code":"FILENAME","description":"Nombre del archivo en curso."},{"code":"SUBSEP","description":"Separador interno para índices multidimensionales simulados."},{"code":"CONVFMT / OFMT","description":"Formato de conversión numérica / salida numérica de print."}]},{"title":"Variables desde la shell","entries":[{"code":"awk -v x=valor 'BEGIN{print x}'","description":"Asignación disponible antes de BEGIN."},{"code":"awk '{...}' x=valor archivo","description":"Asignación procesada en su posición dentro de ARGV."},{"code":"ENVIRON[\"HOME\"]","description":"Leer una variable de entorno dentro de AWK."},{"code":"export MODO=prod","description":"Exporte en la shell antes de usar ENVIRON[\"MODO\"]."},{"code":"ARGV[1] = \"\"","description":"Eliminar un argumento para que no se trate como archivo."}]},{"title":"Cambiar campos y reconstruir $0","entries":[{"code":"$2 = toupper($2)","description":"Modificar un campo reconstruye $0 usando OFS."},{"code":"$1 = $1","description":"Forzar la reconstrucción del registro con el OFS actual."},{"code":"NF--","description":"Reducir NF elimina el último campo en gawk/mawk."},{"code":"$0 = nueva_linea","description":"Asignar $0 vuelve a dividir campos usando FS."}]},{"title":"Rango de patrones","code":"# Imprimir desde [section] hasta la próxima línea vacía\n/^[section]$/, /^[[:space:]]*$/ {\n    print\n}\n\n# Las dos fronteras se evalúan por separado.\n# Un rango no puede activarse y desactivarse en el\n# mismo registro en awk tradicional.","wide":true}]},{"id":"operators","label":"Operators","eyebrow":"05 · EXPRESIONES","title":"Operadores","tag":"Cálculo, comparación y control","icon":"+","note":"AWK convierte entre números y cadenas según el contexto. Sea explícito con +0 o concatenando \"\" cuando datos como 001, fechas o identificadores no deban compararse de forma ambigua.","cards":[{"title":"Aritmética y asignación","entries":[{"code":"+  -  *  /  %  ^","description":"Suma, resta, multiplicación, división, módulo y potencia."},{"code":"++x / x++","description":"Incremento previo / posterior."},{"code":"--x / x--","description":"Decremento previo / posterior."},{"code":"= += -= *= /= %= ^=","description":"Asignación simple y compuesta."},{"code":"-x / +x","description":"Negación / conversión numérica unaria."}]},{"title":"Comparación y lógica","entries":[{"code":"== != \u003c \u003c= > >=","description":"Comparaciones numéricas o de cadenas según operandos."},{"code":"&& / || / !","description":"Y, O y negación lógica; && y || cortocircuitan."},{"code":"cadena ~ /re/","description":"La cadena coincide con la expresión regular."},{"code":"cadena !~ /re/","description":"La cadena no coincide con la expresión regular."},{"code":"índice in array","description":"Probar existencia sin crear el elemento."}]},{"title":"Operadores propios de AWK","entries":[{"code":"a b","description":"Concatenación sin operador visible."},{"code":"cond ? sí : no","description":"Expresión condicional ternaria."},{"code":"$expresión","description":"Referencia indirecta a un campo; $(i + 1)."},{"code":"expr1, expr2","description":"Coma en listas de argumentos o patrón de rango."},{"code":"(i, j) in a","description":"Probar un índice compuesto con SUBSEP."}]},{"title":"Precedencia práctica","code":"# Use paréntesis cuando mezcle familias\npromedio = (suma + extra) / (n + 1)\n\n# La concatenación puede sorprender\nclave = (prefijo i) \"-\" sufijo\n\n# Asignación dentro de una condición\nif ((linea = getline) > 0) print $0\n\n# Ternario dentro de printf\nprintf \"%s\n\", (n ? total / n : \"N/A\")","caption":"Los paréntesis convierten la intención en documentación y evitan depender de una tabla de precedencia.","wide":true}]},{"id":"functions","label":"Functions","eyebrow":"06 · REUTILIZACIÓN","title":"Funciones","tag":"Texto, números y funciones propias","icon":"ƒ","note":"Los argumentos escalares se pasan por valor y los arrays por referencia. AWK no tiene variables locales declaradas: por convención se agregan como parámetros extra después de varios espacios.","cards":[{"title":"Funciones de cadenas","entries":[{"code":"length(s)","description":"Longitud de s; sin argumento usa $0."},{"code":"substr(s, inicio, largo)","description":"Subcadena; los índices empiezan en 1."},{"code":"index(s, busca)","description":"Posición de busca en s o 0."},{"code":"tolower(s) / toupper(s)","description":"Convertir a minúsculas / mayúsculas."},{"code":"sub(re, repl, objetivo)","description":"Reemplazar la primera coincidencia; objetivo por defecto $0."},{"code":"gsub(re, repl, objetivo)","description":"Reemplazar todas las coincidencias."},{"code":"gensub(re, repl, cómo, objetivo)","description":"gawk: reemplazo con referencias \\1, sin alterar el objetivo."}]},{"title":"Dividir y encontrar","entries":[{"code":"split(s, a, sep)","description":"Dividir s en a[1]…a[n] y devolver n."},{"code":"patsplit(s, a, re)","description":"gawk: construir campos con lo que coincide."},{"code":"match(s, re)","description":"Encontrar re y configurar RSTART / RLENGTH."},{"code":"sprintf(formato, args)","description":"Formatear y devolver una cadena sin imprimir."}]},{"title":"Funciones numéricas","entries":[{"code":"int(x)","description":"Truncar hacia cero."},{"code":"sqrt(x) / exp(x) / log(x)","description":"Raíz cuadrada, exponencial y logaritmo natural."},{"code":"sin(x) / cos(x) / atan2(y,x)","description":"Trigonometría en radianes."},{"code":"rand()","description":"Pseudoaleatorio en [0, 1)."},{"code":"srand(semilla)","description":"Cambiar la semilla y devolver la anterior."}]},{"title":"Sistema, tiempo y bits","entries":[{"code":"system(comando)","description":"Ejecutar un comando y devolver su estado."},{"code":"systime()","description":"gawk: segundos Unix del momento actual."},{"code":"strftime(formato, tiempo)","description":"gawk: formatear fecha y hora."},{"code":"mktime(fecha)","description":"gawk: convertir YYYY MM DD HH MM SS a tiempo Unix."},{"code":"and(), or(), xor(), compl()","description":"gawk: operaciones de bits."},{"code":"lshift() / rshift()","description":"gawk: desplazamiento de bits."}]},{"title":"Función propia con locales","code":"function trim(s) {\n    sub(/^[[:space:]]+/, \"\", s)\n    sub(/[[:space:]]+$/, \"\", s)\n    return s\n}\n\n# Los parámetros tras espacios son locales por convención\nfunction media(a, n,    i, suma) {\n    for (i = 1; i \u003c= n; i++) suma += a[i]\n    return n ? suma / n : 0\n}","wide":true}]},{"id":"arrays","label":"Arrays","eyebrow":"07 · DATOS","title":"Arrays asociativos","tag":"Conteos, índices y agrupación","icon":"[ ]","note":"Todos los arrays de AWK son asociativos: sus índices se convierten en cadenas. No asuma un orden al recorrer for (k in a); ordénelo explícitamente cuando el resultado lo requiera.","cards":[{"title":"Operaciones esenciales","entries":[{"code":"a[clave] = valor","description":"Crear o actualizar un elemento."},{"code":"a[clave]++","description":"Contador por clave; parte de cero."},{"code":"clave in a","description":"Comprobar existencia sin crear un elemento."},{"code":"delete a[clave]","description":"Eliminar un elemento."},{"code":"delete a","description":"gawk/mawk y POSIX 2012+: vaciar el array completo."},{"code":"for (clave in a)","description":"Recorrer claves en orden no especificado."}]},{"title":"Índices multidimensionales","entries":[{"code":"a[i, j]","description":"Índice compuesto equivalente a i SUBSEP j."},{"code":"(i, j) in a","description":"Probar un índice compuesto."},{"code":"split(clave, partes, SUBSEP)","description":"Descomponer una clave compuesta."},{"code":"a[i][j]","description":"gawk: arrays de arrays verdaderos."},{"code":"isarray(x)","description":"gawk: comprobar si x es un array."},{"code":"length(a)","description":"gawk/mawk: número de elementos; no es POSIX clásico."}]},{"title":"Ordenar en gawk","entries":[{"code":"asort(origen, destino)","description":"Ordenar valores en destino[1…n]."},{"code":"asorti(origen, destino)","description":"Ordenar índices en destino[1…n]."},{"code":"PROCINFO[\"sorted_in\"]","description":"Controlar el orden posterior de for (k in a)."},{"code":"@ind_str_asc","description":"Índices como cadenas en orden ascendente."},{"code":"@val_num_desc","description":"Valores numéricos en orden descendente."}]},{"title":"Frecuencias ordenadas por cantidad","code":"# gawk: imprimir palabras más frecuentes primero\n{\n    for (i = 1; i \u003c= NF; i++)\n        frecuencia[tolower($i)]++\n}\nEND {\n    PROCINFO[\"sorted_in\"] = \"@val_num_desc\"\n    for (palabra in frecuencia)\n        printf \"%7d  %s\n\", frecuencia[palabra], palabra\n}","wide":true}]},{"id":"conditions","label":"Conditions","eyebrow":"08 · DECISIONES","title":"Condiciones","tag":"Filtrar y ramificar","icon":"?","note":"En contexto booleano, cero y la cadena vacía son falsos; todo lo demás es verdadero. Una cadena numérica como \"0\" puede conservar atributos de cadena y número, así que valide entradas cuando importe.","cards":[{"title":"if, else if y else","code":"if ($3 >= 90) {\n    nivel = \"excelente\"\n} else if ($3 >= 70) {\n    nivel = \"aprobado\"\n} else {\n    nivel = \"revisar\"\n}\n\nprint $1, nivel"},{"title":"Patrones como guardas","entries":[{"code":"NF == 0 { next }","description":"Ignorar registros sin campos."},{"code":"$1 ~ /^#/ { next }","description":"Ignorar comentarios."},{"code":"$3 + 0 > 100","description":"Forzar comparación numérica."},{"code":"($2 \"\") == \"001\"","description":"Forzar comparación como cadena."},{"code":"clave in visto","description":"Rama basada en existencia de clave."},{"code":"!visto[$1]++","description":"Verdadero solo en la primera aparición de $1."}]},{"title":"Validación robusta","entries":[{"code":"$2 ~ /^-?[0-9]+([.][0-9]+)?$/","description":"Validar un decimal sencillo antes de convertir."},{"code":"NF != esperado","description":"Detectar filas con cantidad incorrecta de campos."},{"code":"(getline) > 0","description":"Lectura correcta."},{"code":"(getline) == 0","description":"Fin de archivo."},{"code":"(getline) \u003c 0","description":"Error de lectura; ERRNO aporta detalle en gawk."},{"code":"ERRNO","description":"gawk: mensaje asociado al último error de E/S."}]},{"title":"Salir con un estado útil","code":"BEGIN { errores = 0 }\n\nNF != 4 {\n    printf \"Fila %d inválida: %s\n\", FNR, $0 > \"/dev/stderr\"\n    errores++\n}\n\nEND {\n    if (errores)\n        exit 2\n}","caption":"El estado de exit permite que scripts de shell, CI o cron sepan si la validación falló.","wide":true}]},{"id":"loops","label":"Loops","eyebrow":"09 · REPETICIÓN","title":"Bucles y control de flujo","tag":"Recorrer campos, arrays y entradas","icon":"↻","note":"Use for numérico cuando el orden importa y for (clave in array) cuando solo necesita visitar cada elemento. El orden de un array asociativo no está definido por POSIX.","cards":[{"title":"for numérico","code":"# Recorrer todos los campos\nfor (i = 1; i \u003c= NF; i++) {\n    if ($i ~ /^[0-9]+$/)\n        suma += $i\n}\n\n# Recorrer en sentido inverso\nfor (i = NF; i >= 1; i--)\n    printf \"%s%s\", $i, (i > 1 ? OFS : ORS)"},{"title":"for asociativo","code":"# Contar y recorrer claves\n{ cuenta[$1]++ }\n\nEND {\n    for (clave in cuenta) {\n        if (cuenta[clave] \u003c 2)\n            continue\n        print clave, cuenta[clave]\n    }\n}"},{"title":"while y do…while","entries":[{"code":"while (condición) { ... }","description":"Probar antes de cada iteración."},{"code":"do { ... } while (condición)","description":"Ejecutar al menos una vez."},{"code":"while ((getline linea \u003c f) > 0)","description":"Leer un archivo auxiliar línea por línea."},{"code":"while (match(s, re))","description":"Consumir coincidencias repetidas dentro de una cadena."}]},{"title":"Control de flujo","entries":[{"code":"break","description":"Salir del bucle más cercano."},{"code":"continue","description":"Saltar a la siguiente iteración del bucle."},{"code":"next","description":"Saltar el registro y reiniciar las reglas."},{"code":"nextfile","description":"Saltar el resto del archivo actual."},{"code":"exit / exit código","description":"Finalizar entrada, ejecutar END y devolver un estado."},{"code":"return valor","description":"Salir de una función con un valor."}]},{"title":"Consumir todas las coincidencias","code":"{\n    resto = $0\n    while (match(resto, /[[:alpha:]]+@[[:alnum:].-]+/)) {\n        correo = substr(resto, RSTART, RLENGTH)\n        print correo\n        resto = substr(resto, RSTART + RLENGTH)\n    }\n}","wide":true}]},{"id":"formatted-printing","label":"Formatted Printing","eyebrow":"10 · SALIDA","title":"Impresión con formato","tag":"print, printf y redirección","icon":"%","note":"print agrega ORS y separa argumentos con OFS. printf usa un formato explícito y no agrega salto de línea: inclúyalo con \\n cuando lo necesite.","cards":[{"title":"print frente a printf","entries":[{"code":"print $1, $2","description":"Separar argumentos con OFS y terminar con ORS."},{"code":"print $1 $2","description":"Concatenar sin OFS."},{"code":"printf \"%s %d\\n\", $1, $2","description":"Control preciso de tipos, ancho y terminación."},{"code":"texto = sprintf(\"%.2f\", n)","description":"Construir una cadena formateada."},{"code":"OFMT = \"%.6g\"","description":"Formato numérico usado por print."},{"code":"CONVFMT = \"%.6g\"","description":"Formato al convertir números a cadenas."}]},{"title":"Conversiones de printf","entries":[{"code":"%s","description":"Cadena."},{"code":"%d / %i","description":"Entero decimal."},{"code":"%f","description":"Punto flotante decimal."},{"code":"%e / %E","description":"Notación científica."},{"code":"%g / %G","description":"Formato compacto automático."},{"code":"%o / %x / %X","description":"Octal / hexadecimal."},{"code":"%c / %%","description":"Carácter / signo de porcentaje literal."}]},{"title":"Ancho, precisión y alineación","entries":[{"code":"%10s","description":"Cadena alineada a la derecha en 10 columnas."},{"code":"%-10s","description":"Cadena alineada a la izquierda."},{"code":"%08d","description":"Entero de 8 posiciones rellenado con ceros."},{"code":"%10.2f","description":"Ancho 10 y dos decimales."},{"code":"%*.*f","description":"Tomar ancho y precisión desde argumentos."},{"code":"%+.2f","description":"Mostrar siempre el signo."}]},{"title":"Redirección y tuberías","entries":[{"code":"print > \"salida.txt\"","description":"Redirigir; AWK mantiene el archivo abierto."},{"code":"print >> \"salida.txt\"","description":"Agregar al final."},{"code":"print | \"sort\"","description":"Enviar salida a un comando."},{"code":"print |& comando","description":"gawk: comunicación bidireccional con coproceso."},{"code":"close(destino)","description":"Cerrar archivo o tubería cuando ya no se use."},{"code":"fflush(destino)","description":"gawk/POSIX reciente: vaciar el búfer de salida."}]},{"title":"Tabla alineada","code":"BEGIN {\n    printf \"%-20s %8s %12s\n\", \"Producto\", \"Cant.\", \"Total\"\n    printf \"%-20s %8s %12s\n\", \"--------------------\", \"--------\", \"------------\"\n}\n{\n    total = $2 * $3\n    printf \"%-20.20s %8d %12.2f\n\", $1, $2, total\n    gran_total += total\n}\nEND {\n    printf \"%41s\n\", \"------------\"\n    printf \"%-29s %12.2f\n\", \"TOTAL\", gran_total\n}","wide":true}]},{"id":"miscellaneous","label":"Miscellaneous","eyebrow":"11 · CAJA DE HERRAMIENTAS","title":"Miscelánea y recetas","tag":"One-liners, portabilidad y depuración","icon":"…","note":"Para automatización durable, prefiera programas en archivos, comillas simples en la shell, variables con -v y características POSIX salvo que haya decidido depender de gawk.","cards":[{"title":"One-liners imprescindibles","entries":[{"code":"awk 'NF' archivo","description":"Eliminar líneas vacías."},{"code":"awk '!visto[$0]++' archivo","description":"Eliminar líneas duplicadas conservando orden."},{"code":"awk '{ suma += $1 } END { print suma }'","description":"Sumar la primera columna."},{"code":"awk 'END { print NR }' archivo","description":"Contar registros."},{"code":"awk '{ print NF, $0 }' archivo","description":"Prefijar cada línea con su número de campos."},{"code":"awk 'length > max { max=length; linea=$0 } END{print linea}'","description":"Encontrar la línea más larga."}]},{"title":"Reformatear y seleccionar","entries":[{"code":"awk -F, -v OFS=';' '{$1=$1; print}'","description":"Cambiar el separador de campos."},{"code":"awk '{ print $NF }'","description":"Imprimir el último campo."},{"code":"awk 'NR >= 10 && NR \u003c= 20'","description":"Imprimir un intervalo de líneas."},{"code":"awk '$1 == max { print }' max=42","description":"Asignar una variable en la invocación."},{"code":"awk '{ for(i=NF;i;i--) printf \"%s%s\",$i,(i>1?OFS:ORS) }'","description":"Invertir el orden de campos."}]},{"title":"Shell y seguridad","entries":[{"code":"awk -v valor=\"$variable\" '...'","description":"Pasar datos de shell sin inyectarlos en el programa."},{"code":"'programa AWK'","description":"Use comillas simples para proteger $, \\ y espacios de la shell."},{"code":"system(\"cmd \" dato)","description":"Riesgoso con entrada externa; evite construir comandos sin escapar."},{"code":"--","description":"Algunas implementaciones marcan fin de opciones; revise portabilidad."},{"code":"/dev/stderr","description":"Común, pero no POSIX; en gawk use print ... > \"/dev/stderr\"."}]},{"title":"Portabilidad y rendimiento","entries":[{"code":"LC_ALL=C","description":"Resultados de clases, orden y números más predecibles y rápidos."},{"code":"gawk --lint --posix -f script.awk","description":"Detectar extensiones al probar portabilidad."},{"code":"next","description":"Evitar trabajo innecesario en reglas posteriores."},{"code":"close()","description":"Evitar agotar archivos y procesos abiertos."},{"code":"sub() antes que gsub()","description":"Si solo necesita reemplazar la primera coincidencia."},{"code":"regex literal","description":"Preferible a reconstruir la misma regex dinámica por registro."}]},{"title":"Depuración y diagnóstico","code":"# Trazas a stderr (gawk y Unix habituales)\nprint \"DEBUG NR=\" NR \", NF=\" NF > \"/dev/stderr\"\n\n# Mostrar campos delimitados inequívocamente\nfor (i = 1; i \u003c= NF; i++)\n    printf \"[$%d]=\u003c%s>\n\", i, $i > \"/dev/stderr\"\n\n# Comprobar sintaxis y advertencias\ngawk --lint -f programa.awk \u003c/dev/null\n\n# Perfil de ejecución en gawk\ngawk --profile -f programa.awk datos","wide":true}]}];
    let activeId = topics[0].id;
    let copySequence = 0;
    const copyValues = new Map();

    const tabsElement = document.getElementById("tabs");
    const panelElement = document.getElementById("topic-panel");
    const headerElement = document.getElementById("section-header");
    const noteElement = document.getElementById("topic-note");
    const gridElement = document.getElementById("topic-grid");

    function escapeHtml(value) {
      return String(value)
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;")
        .replaceAll("'", "&#039;");
    }

    function registerCopy(value) {
      const id = "copy-" + (++copySequence);
      copyValues.set(id, value);
      return id;
    }

    function copyButton(value, compact) {
      const id = registerCopy(value);
      return '<button class="copy-button' + (compact ? ' compact' : '') +
        '" type="button" data-copy-id="' + id +
        '" aria-label="Copiar código" title="Copiar"><span aria-hidden="true">⧉</span>' +
        (compact ? "" : "<span>Copiar</span>") + "</button>";
    }

    function renderTabs() {
      tabsElement.innerHTML = topics.map(function (topic, index) {
        const active = topic.id === activeId;
        return '<button class="tablinks' + (active ? ' active' : '') +
          '" type="button" role="tab" id="tab-' + escapeHtml(topic.id) +
          '" data-topic-id="' + escapeHtml(topic.id) +
          '" aria-selected="' + active +
          '" aria-controls="topic-panel" tabindex="' + (active ? "0" : "-1") + '">' +
          '<span class="tab-number">' + String(index + 1).padStart(2, "0") + '</span>' +
          '<span>' + escapeHtml(topic.label) + '</span></button>';
      }).join("");
    }

    function renderCard(card) {
      const entries = card.entries
        ? '<ul class="cmd-list">' + card.entries.map(function (entry) {
            return '<li><span class="command-wrap"><code>' + escapeHtml(entry.code) + '</code>' +
              copyButton(entry.code, true) + '</span><span class="desc">' +
              escapeHtml(entry.description) + '</span></li>';
          }).join("") + '</ul>'
        : "";

      const code = card.code
        ? '<div class="code-wrap">' + copyButton(card.code, false) +
          '<pre><code>' + escapeHtml(card.code) + '</code></pre></div>'
        : "";

      const caption = card.caption
        ? '<p class="caption">' + escapeHtml(card.caption) + '</p>'
        : "";

      return '<article class="box' + (card.wide ? ' box-wide' : '') + '">' +
        '<div class="box-title"><span class="dot" aria-hidden="true"></span><span>' +
        escapeHtml(card.title) + '</span></div>' + entries + code + caption + '</article>';
    }

    function renderPanel() {
      const topic = topics.find(function (item) { return item.id === activeId; }) || topics[0];
      copySequence = 0;
      copyValues.clear();

      panelElement.setAttribute("aria-labelledby", "tab-" + topic.id);
      panelElement.dataset.topic = topic.id;
      headerElement.innerHTML =
        '<div><span class="eyebrow">' + escapeHtml(topic.eyebrow) + '</span><h2>' +
        escapeHtml(topic.title) + '</h2></div><span class="tag">' +
        escapeHtml(topic.tag) + '</span>';
      noteElement.innerHTML =
        '<div class="note-icon" aria-hidden="true">' + escapeHtml(topic.icon) +
        '</div><div><strong>Idea clave.</strong> ' + escapeHtml(topic.note) + '</div>';
      gridElement.innerHTML = topic.cards.map(renderCard).join("");

      panelElement.style.animation = "none";
      void panelElement.offsetWidth;
      panelElement.style.animation = "";
    }

    function openTopic(id, options) {
      const settings = options || {};
      if (!topics.some(function (topic) { return topic.id === id; })) return;
      activeId = id;
      renderTabs();
      renderPanel();

      if (settings.updateHash !== false) {
        history.replaceState(null, "", "#" + id);
      }
      if (settings.scroll) {
        window.scrollTo({ top: 0, behavior: "smooth" });
      }
      if (settings.focus) {
        const tab = tabsElement.querySelector('[data-topic-id="' + CSS.escape(id) + '"]');
        if (tab) tab.focus();
      }
    }

    async function copyText(value) {
      if (navigator.clipboard && window.isSecureContext) {
        await navigator.clipboard.writeText(value);
        return;
      }
      const area = document.createElement("textarea");
      area.value = value;
      area.setAttribute("readonly", "");
      area.style.position = "fixed";
      area.style.opacity = "0";
      document.body.appendChild(area);
      area.select();
      document.execCommand("copy");
      area.remove();
    }

    tabsElement.addEventListener("click", function (event) {
      const tab = event.target.closest("[data-topic-id]");
      if (tab) openTopic(tab.dataset.topicId, { updateHash: true, scroll: true });
    });

    tabsElement.addEventListener("keydown", function (event) {
      const tab = event.target.closest("[data-topic-id]");
      if (!tab) return;
      const index = topics.findIndex(function (topic) { return topic.id === tab.dataset.topicId; });
      let nextIndex = index;

      if (event.key === "ArrowRight" || event.key === "ArrowDown") nextIndex = (index + 1) % topics.length;
      else if (event.key === "ArrowLeft" || event.key === "ArrowUp") nextIndex = (index - 1 + topics.length) % topics.length;
      else if (event.key === "Home") nextIndex = 0;
      else if (event.key === "End") nextIndex = topics.length - 1;
      else return;

      event.preventDefault();
      openTopic(topics[nextIndex].id, { updateHash: true, focus: true });
    });

    gridElement.addEventListener("click", async function (event) {
      const button = event.target.closest("[data-copy-id]");
      if (!button) return;
      const value = copyValues.get(button.dataset.copyId);
      if (typeof value !== "string") return;

      try {
        await copyText(value);
        const original = button.innerHTML;
        button.innerHTML = button.classList.contains("compact")
          ? '<span aria-hidden="true">✓</span>'
          : '<span aria-hidden="true">✓</span><span>Copiado</span>';
        button.title = "Copiado";
        window.setTimeout(function () {
          button.innerHTML = original;
          button.title = "Copiar";
        }, 1400);
      } catch (error) {
        button.title = "No se pudo copiar";
      }
    });

    window.addEventListener("hashchange", function () {
      const id = location.hash.slice(1);
      if (id) openTopic(id, { updateHash: false });
    });

    const initialId = location.hash.slice(1);
    openTopic(
      topics.some(function (topic) { return topic.id === initialId; }) ? initialId : topics[0].id,
      { updateHash: false }
    );
</script>
