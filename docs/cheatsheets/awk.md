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
        <h1>AWK Cheat Sheet</h1>
        <p>From the first filter to complete programs, organized for quick reference and daily use.</p>
      </div>
      <div class="header-right">
        <a href="/#cheat-sheets" class="back-button">Back to the dashboard</a>
        <div class="mode-pill-row" aria-label="Compatibility">
          <div class="mode-pill"><span class="key">awk</span><span>POSIX</span></div>
          <div class="mode-pill"><span class="key">gawk</span><span>GNU</span></div>
          <div class="mode-pill"><span class="key">mawk</span><span>Fast</span></div>
        </div>
      </div>
    </header>

    <nav class="tab-shell" aria-label="Cheat Sheet Categories">
      <div class="tab-intro">
        <span>INDEX</span>
        <small>← → to navigate</small>
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
        <p><strong>Do you need to go deeper?</strong> See the full GNU AWK manual for details, edge cases, and extensions.</p>
      </div>
      <a href="https://www-zeuthen.desy.de/dv/documentation/unixguide/infohtml/gawk/gawk.html" target="_blank" rel="noreferrer">
        Open documentation <span aria-hidden="true">↗</span>
      </a>
    </footer>
  </main>
</div>

<script>
"use strict";

    const topics = [{"id":"getting-started","label":"Getting started","eyebrow":"01 · FUNDAMENTALS","title":"Getting started with AWK","tag":"From zero to a useful program","icon":"A","note":"AWK reads input one record at a time, tests each pattern, and executes its action. If you omit the pattern, the action is always executed; if you omit the action, AWK prints the record.","cards":[{"title":"Invocation Forms","entries":[{"code":"awk 'programa' archivo","description":"Run a short program on a file."},{"code":"awk 'programa' archivo1 archivo2","description":"Process multiple files as a single stream."},{"code":"awk -F: '{ print $1 }' /etc/passwd","description":"Define the field separator with -F."},{"code":"awk -v limite=10 '$3 > limite' datos","description":"Pass a variable before executing BEGIN."},{"code":"awk -f programa.awk datos","description":"Load the program from a file."},{"code":"comando | awk '{ print $1 }'","description":"Read from the standard output of another command."}]},{"title":"Execution model","entries":[{"code":"BEGIN { ... }","description":"Run once before reading the input."},{"code":"patrón { acción }","description":"Evaluate once for each check-in."},{"code":"END { ... }","description":"Execute once upon completion or upon calling exit."},{"code":"patrón","description":"Implicit action: { print $0 }."},{"code":"{ acción }","description":"Implicit pattern: true for each record."},{"code":"# comentario","description":"Comment from # to the end of the line."}]},{"title":"Records and essential fields","entries":[{"code":"$0","description":"Current complete record."},{"code":"$1 … $NF","description":"First field to last field."},{"code":"NF","description":"Number of fields in the current record."},{"code":"NR","description":"Cumulative record number across all files."},{"code":"FNR","description":"Record number within the current file."},{"code":"FS / OFS","description":"Input/output field separator."},{"code":"RS / ORS","description":"In/out record separator."}]},{"title":"Options that should be memorized","entries":[{"code":"-F 'regex'","description":"Configure FS from the command line."},{"code":"-v nombre=valor","description":"Assign a variable before BEGIN."},{"code":"-f archivo.awk","description":"Read the program from a file."},{"code":"-f uno.awk -f dos.awk","description":"Combine multiple program files."},{"code":"gawk --lint","description":"Warn about dubious or non-portable constructions."},{"code":"gawk --posix","description":"Restrict extensions and prioritize POSIX."}]},{"title":"Minimal full script","code":"#!/usr/bin/awk -f\n\nBEGIN {\n    FS = \",\"\n    OFS = \"\t\"\n}\n\nNR > 1 && $3 >= 70 {\n    total += $3\n    aprobados++\n    print $1, $3\n}\n\nEND {\n    if (aprobados)\n        printf \"Promedio: %.2f\n\", total / aprobados\n}","caption":"Save it as report.awk, chmod +x and run it with ./reporte.awk data.csv.","wide":true}]},{"id":"regex","label":"Regex","eyebrow":"02 · MATCHING","title":"Regular Expressions","tag":"POSIX ERE and dynamic patterns","icon":"/","note":"AWK uses extended regular expressions (ERE). A /regex/ literal tests $0; The ~ and !~ operators allow you to test any string or field.","cards":[{"title":"Basic use","entries":[{"code":"/error/","description":"Records whose $0 contains an error."},{"code":"$2 ~ /^[A-Z]/","description":"The second field begins with a capital letter."},{"code":"$3 !~ /^(ok|ready)$/","description":"The third field is not exactly ok or ready."},{"code":"pat = \"warn|fail\"; $0 ~ pat","description":"Dynamic regular expression stored in a variable."},{"code":"tolower($0) ~ /error/","description":"Portable case-insensitive search."},{"code":"gawk 'BEGIN { IGNORECASE=1 } /error/'","description":"Case-insensitive global matching in gawk."}]},{"title":"ERE metacharacters","entries":[{"code":".","description":"Any individual character."},{"code":"^ / $","description":"Start/end of string."},{"code":"* / + / ?","description":"Zero or more / one or more / zero or one."},{"code":"{m,n}","description":"Between m and n repetitions (modern POSIX)."},{"code":"[abc] / [^abc]","description":"Positive class / negated class."},{"code":"(uno|dos)","description":"Grouping and alternation."},{"code":"\\.","description":"Literal point; escape the metacharacter."}]},{"title":"Portable POSIX classes","entries":[{"code":"[[:alpha:]]","description":"Font depending on locale."},{"code":"[[:digit:]]","description":"Decimal digit."},{"code":"[[:alnum:]]","description":"Letter or digit."},{"code":"[[:space:]]","description":"Space, tab or line break."},{"code":"[[:blank:]]","description":"Horizontal space or tab."},{"code":"[[:lower:]] / [[:upper:]]","description":"Lowercase/uppercase."},{"code":"[[:xdigit:]]","description":"Hexadecimal digit."}]},{"title":"match, RSTART and RLENGTH","entries":[{"code":"match(s, /re/)","description":"Position of the first match or 0."},{"code":"RSTART","description":"Initial index of the last match."},{"code":"RLENGTH","description":"Length of last match; -1 if there were none."},{"code":"substr(s, RSTART, RLENGTH)","description":"Extract exactly the text found."},{"code":"match(s, /([0-9]+)/, m)","description":"gawk: save match and captured groups in m."}]},{"title":"Recipes with regex","code":"# Empty or whitespace-only lines\n/^[[:space:]]*$/\n\n# Approximate IPv4 address at the start of the record\nmatch($0, /^([0-9]{1,3}.){3}[0-9]{1,3}/)\n\n# Extract every number from a line\n{\n    s = $0\n    while (match(s, /[0-9]+([.][0-9]+)?/)) {\n        print substr(s, RSTART, RLENGTH)\n        s = substr(s, RSTART + RLENGTH)\n    }\n}","wide":true}]},{"id":"reading-files","label":"Reading Files","eyebrow":"03 · INPUT","title":"Reading files and streams","tag":"Fields, records and getline","icon":"R","note":"FS splits records into fields and RS splits the input into records. Changing them in BEGIN is usually the clearest option; getline is reserved for additional input or explicit control.","cards":[{"title":"Multiple files","entries":[{"code":"FILENAME","description":"Name of the current input file."},{"code":"NR == FNR","description":"True while the first file is being processed."},{"code":"FNR == 1","description":"First line of each file."},{"code":"ARGC / ARGV","description":"Quantity and vector of arguments of the invocation."},{"code":"ARGIND","description":"gawk: ARGV index of the current file."},{"code":"next","description":"Skip the rest of the rules for this record."},{"code":"nextfile","description":"Stop reading the current file and open the next one."}]},{"title":"Input separators","entries":[{"code":"FS = \",\"","description":"Separate fields by a literal comma."},{"code":"FS = \"[[:space:]]+\"","description":"Separate by one or more POSIX spaces."},{"code":"FS = \"\"","description":"gawk/mawk: separate each character; It is not POSIX."},{"code":"RS = \"\"","description":"Paragraph mode: records separated by empty lines."},{"code":"RS = \"END|STOP\"","description":"gawk: RS can be a regular expression."},{"code":"RT","description":"gawk: text that matched RS."}]},{"title":"Gawk Special Fields","entries":[{"code":"FIELDWIDTHS = \"5 10 8\"","description":"Split by fixed widths instead of FS."},{"code":"FPAT = \"([^,]+)|(\\\"[^\\\"]+\\\")\"","description":"Define what constitutes a field, useful for simple CSV."},{"code":"patsplit(s, a, fpat, seps)","description":"Separate by field content and save separators."},{"code":"split(s, a, fs, seps)","description":"gawk: split and capture matching separators."}]},{"title":"getline variants","entries":[{"code":"getline","description":"Read the following record at $0 and recalculate NF."},{"code":"getline variable","description":"Read into variable without modifying $0 or NF."},{"code":"getline variable < archivo","description":"Read from another file; try the return value."},{"code":"comando | getline variable","description":"Read a line of command output."},{"code":"resultado = getline variable","description":"Save status: 1 read, 0 end of file, -1 error."},{"code":"close(archivo_o_comando)","description":"Close a resource to avoid exhausted descriptors."}]},{"title":"Join two files by key","code":"# users.txt: id name\n# sales.txt:  id amount\nawk '\n    NR == FNR { nombre[$1] = $2; next }\n    $1 in nombre { total[nombre[$1]] += $2 }\n    END {\n        for (persona in total)\n            print persona, total[persona]\n    }\n' usuarios.txt ventas.txt","caption":"NR == FNR load the first file; next prevents that record from being passed to the sales rules.","wide":true}]},{"id":"patterns-actions-variables","label":"Patterns, Actions, and Variables","eyebrow":"04 · STRUCTURE","title":"Patterns, actions and variables","tag":"The heart of language","icon":"P","note":"Each rule has the form pattern { action }. The rules are tested in order for the same record, unless next, nextfile, or exit change the flow.","cards":[{"title":"Pattern classes","entries":[{"code":"BEGIN / END","description":"Before input / after all input."},{"code":"BEGINFILE / ENDFILE","description":"gawk: before and after each file."},{"code":"/regex/","description":"Match against $0."},{"code":"$3 > 100","description":"Boolean expression."},{"code":"/inicio/, /fin/","description":"Inclusive range with state between two patterns."},{"code":"pat1 && pat2","description":"Compose conditions with Boolean logic."}]},{"title":"Built-in field variables","entries":[{"code":"FS / OFS","description":"Input/output field separator."},{"code":"RS / ORS","description":"In/out record separator."},{"code":"NF / NR / FNR","description":"Current fields / total record / file record."},{"code":"FILENAME","description":"Name of the current file."},{"code":"SUBSEP","description":"Internal separator for simulated multidimensional indexes."},{"code":"CONVFMT / OFMT","description":"Numeric conversion format/print numeric output."}]},{"title":"Variables from the shell","entries":[{"code":"awk -v x=valor 'BEGIN{print x}'","description":"Allocation available before BEGIN."},{"code":"awk '{...}' x=valor archivo","description":"Assignment processed in its position within ARGV."},{"code":"ENVIRON[\"HOME\"]","description":"Read an environment variable within AWK."},{"code":"export MODO=prod","description":"Export in the shell before using ENVIRON[\"MODE\"]."},{"code":"ARGV[1] = \"\"","description":"Remove an argument so that it is not treated as a file."}]},{"title":"Change fields and rebuild $0","entries":[{"code":"$2 = toupper($2)","description":"Modifying a field rebuilds $0 using OFS."},{"code":"$1 = $1","description":"Force rebuild the registry with the current OFS."},{"code":"NF--","description":"Reduce NF removes the last field in gawk/mawk."},{"code":"$0 = nueva_linea","description":"Assigning $0 splits fields again using FS."}]},{"title":"Pattern Range","code":"# Print from [section] through the next blank line\n/^[section]$/, /^[[:space:]]*$/ {\n    print\n}\n\n# The two boundaries are evaluated separately.\n# In traditional awk, a range cannot start and stop on\n# the same record.","wide":true}]},{"id":"operators","label":"Operators","eyebrow":"05 · EXPRESSIONS","title":"Operators","tag":"Calculation, comparison and control","icon":"+","note":"AWK converts between numbers and strings based on context. Be explicit with +0 or concatenating \"\" when data such as 001, dates, or identifiers should not be compared ambiguously.","cards":[{"title":"Arithmetic and assignment","entries":[{"code":"+  -  *  /  %  ^","description":"Addition, subtraction, multiplication, division, modulo and exponentiation."},{"code":"++x / x++","description":"Pre/post increment."},{"code":"--x / x--","description":"Pre/post decrement."},{"code":"= += -= *= /= %= ^=","description":"Simple and compound assignment."},{"code":"-x / +x","description":"Unary numerical negation/conversion."}]},{"title":"Comparison and logic","entries":[{"code":"== != < <= > >=","description":"Numerical or string comparisons according to operands."},{"code":"&& / || / !","description":"AND, OR and logical negation; && and || they short circuit."},{"code":"cadena ~ /re/","description":"The string matches the regular expression."},{"code":"cadena !~ /re/","description":"The string does not match the regular expression."},{"code":"índice in array","description":"Test existence without creating the element."}]},{"title":"AWK's own operators","entries":[{"code":"a b","description":"Concatenation without visible operator."},{"code":"cond ? sí : no","description":"Ternary conditional expression."},{"code":"$expresión","description":"Indirect reference to a field; $(i + 1)."},{"code":"expr1, expr2","description":"Comma in argument lists or range pattern."},{"code":"(i, j) in a","description":"Test a composite index with SUBSEP."}]},{"title":"Practical precedence","code":"# Use parentheses when mixing operator families\npromedio = (suma + extra) / (n + 1)\n\n# Concatenation can be surprising\nclave = (prefijo i) \"-\" sufijo\n\n# Assignment inside a condition\nif ((linea = getline) > 0) print $0\n\n# Ternary expression inside printf\nprintf \"%s\n\", (n ? total / n : \"N/A\")","caption":"Parentheses turn intent into documentation and avoid relying on a precedence table.","wide":true}]},{"id":"functions","label":"functions","eyebrow":"06 · REUSE","title":"Functions","tag":"Text, numbers, and user-defined functions","icon":"ƒ","note":"Scalar arguments are passed by value and arrays by reference. AWK has no declared local variables: by convention they are added as extra parameters after several spaces.","cards":[{"title":"String functions","entries":[{"code":"length(s)","description":"Length of s; without an argument, it uses $0."},{"code":"substr(s, inicio, largo)","description":"Substring; indexes start at 1."},{"code":"index(s, busca)","description":"Search position in s or 0."},{"code":"tolower(s) / toupper(s)","description":"Convert to lowercase/uppercase."},{"code":"sub(re, repl, objetivo)","description":"Replace the first match; default target $0."},{"code":"gsub(re, repl, objetivo)","description":"Replace all matches."},{"code":"gensub(re, repl, cómo, objetivo)","description":"gawk: replace with \\1 references, without altering the target."}]},{"title":"Split and find","entries":[{"code":"split(s, a, sep)","description":"Split s into a[1]…a[n] and return n."},{"code":"patsplit(s, a, re)","description":"gawk: build fields with what matches."},{"code":"match(s, re)","description":"Find re and set RSTART/RLENGTH."},{"code":"sprintf(formato, args)","description":"Format and return a string without printing."}]},{"title":"Numerical functions","entries":[{"code":"int(x)","description":"Truncate towards zero."},{"code":"sqrt(x) / exp(x) / log(x)","description":"Square root, exponential and natural logarithm."},{"code":"sin(x) / cos(x) / atan2(y,x)","description":"Trigonometry in radians."},{"code":"rand()","description":"Pseudorandom in [0, 1)."},{"code":"srand(semilla)","description":"Change the seed and return the previous one."}]},{"title":"System, time and bits","entries":[{"code":"system(comando)","description":"Execute a command and return its status."},{"code":"systime()","description":"gawk: Unix seconds of the current moment."},{"code":"strftime(formato, tiempo)","description":"gawk: format date and time."},{"code":"mktime(fecha)","description":"gawk: convert YYYY MM DD HH MM SS to Unix time."},{"code":"and(), or(), xor(), compl()","description":"gawk: bit operations."},{"code":"lshift() / rshift()","description":"gawk: bit shift."}]},{"title":"User-defined function with local variables","code":"function trim(s) {\n    sub(/^[[:space:]]+/, \"\", s)\n    sub(/[[:space:]]+$/, \"\", s)\n    return s\n}\n\n# Parameters after extra spaces are local by convention\nfunction media(a, n,    i, suma) {\n    for (i = 1; i <= n; i++) suma += a[i]\n    return n ? suma / n : 0\n}","wide":true}]},{"id":"arrays","label":"Arrays","eyebrow":"07 · DATA","title":"Associative arrays","tag":"Counts, indexes and grouping","icon":"[ ]","note":"All AWK arrays are associative: their indexes are converted to strings. Don't assume an order when looping through for (k in a); order it explicitly when the result requires it.","cards":[{"title":"Essential operations","entries":[{"code":"a[clave] = valor","description":"Create or update an item."},{"code":"a[clave]++","description":"Counter by key; starts from zero."},{"code":"clave in a","description":"Check existence without creating an element."},{"code":"delete a[clave]","description":"Delete an element."},{"code":"delete a","description":"gawk/mawk and POSIX 2012+: empty the entire array."},{"code":"for (clave in a)","description":"Loop through keys in unspecified order."}]},{"title":"Multidimensional indices","entries":[{"code":"a[i, j]","description":"Composite index equivalent to i SUBSEP j."},{"code":"(i, j) in a","description":"Try a composite index."},{"code":"split(clave, partes, SUBSEP)","description":"Decompose a compound key."},{"code":"a[i][j]","description":"gawk: arrays of true arrays."},{"code":"isarray(x)","description":"gawk: check if x is an array."},{"code":"length(a)","description":"gawk/mawk: number of elements; it is not classic POSIX."}]},{"title":"Sort in gawk","entries":[{"code":"asort(origen, destino)","description":"Sort values ​​in destination[1…n]."},{"code":"asorti(origen, destino)","description":"Sort indexes on destination[1…n]."},{"code":"PROCINFO[\"sorted_in\"]","description":"Control the subsequent order of for (k in a)."},{"code":"@ind_str_asc","description":"Indexes as strings in ascending order."},{"code":"@val_num_desc","description":"Numeric values ​​in descending order."}]},{"title":"Frequencies sorted by count","code":"# gawk: print the most frequent words first\n{\n    for (i = 1; i <= NF; i++)\n        frecuencia[tolower($i)]++\n}\nEND {\n    PROCINFO[\"sorted_in\"] = \"@val_num_desc\"\n    for (palabra in frecuencia)\n        printf \"%7d  %s\n\", frecuencia[palabra], palabra\n}","wide":true}]},{"id":"conditions","label":"Conditions","eyebrow":"08 · DECISIONS","title":"Conditions","tag":"Filter and branch","icon":"?","note":"In boolean context, zero and the empty string are false; everything else is true. A numeric string such as \"0\" can retain string and number attributes, so validate inputs when it matters.","cards":[{"title":"if, else if and else","code":"if ($3 >= 90) {\n    nivel = \"excelente\"\n} else if ($3 >= 70) {\n    nivel = \"aprobado\"\n} else {\n    nivel = \"revisar\"\n}\n\nprint $1, nivel"},{"title":"Patterns as guards","entries":[{"code":"NF == 0 { next }","description":"Ignore records without fields."},{"code":"$1 ~ /^#/ { next }","description":"Ignore comments."},{"code":"$3 + 0 > 100","description":"Force numerical comparison."},{"code":"($2 \"\") == \"001\"","description":"Force comparison as string."},{"code":"clave in visto","description":"Branch based on key existence."},{"code":"!visto[$1]++","description":"True only on the first occurrence of $1."}]},{"title":"Robust validation","entries":[{"code":"$2 ~ /^-?[0-9]+([.][0-9]+)?$/","description":"Validate a single decimal before converting."},{"code":"NF != esperado","description":"Detect rows with incorrect number of fields."},{"code":"(getline) > 0","description":"Correct reading."},{"code":"(getline) == 0","description":"End of file."},{"code":"(getline) < 0","description":"Read error; ERRNO provides detail in gawk."},{"code":"ERRNO","description":"gawk: message associated with the last I/O error."}]},{"title":"Exit with a useful state","code":"BEGIN { errores = 0 }\n\nNF != 4 {\n    printf \"Fila %d inválida: %s\n\", FNR, $0 > \"/dev/stderr\"\n    errores++\n}\n\nEND {\n    if (errores)\n        exit 2\n}","caption":"The exit status allows shell, CI, or cron scripts to know if validation failed.","wide":true}]},{"id":"loops","label":"Loops","eyebrow":"09 · REPETITION","title":"Loops and flow control","tag":"Loop through fields, arrays, and entries","icon":"↻","note":"Use numeric for when order matters and for (key in array) when you only need to visit each element. The order of an associative array is not defined by POSIX.","cards":[{"title":"for numeric","code":"# Iterate over every field\nfor (i = 1; i <= NF; i++) {\n    if ($i ~ /^[0-9]+$/)\n        suma += $i\n}\n\n# Iterate in reverse\nfor (i = NF; i >= 1; i--)\n    printf \"%s%s\", $i, (i > 1 ? OFS : ORS)"},{"title":"for associative","code":"# Count and iterate over keys\n{ cuenta[$1]++ }\n\nEND {\n    for (clave in cuenta) {\n        if (cuenta[clave] < 2)\n            continue\n        print clave, cuenta[clave]\n    }\n}"},{"title":"while and do…while","entries":[{"code":"while (condición) { ... }","description":"Test before each iteration."},{"code":"do { ... } while (condición)","description":"Run at least once."},{"code":"while ((getline linea < f) > 0)","description":"Read an auxiliary file line by line."},{"code":"while (match(s, re))","description":"Consume repeated matches within a string."}]},{"title":"Flow control","entries":[{"code":"break","description":"Exit the nearest loop."},{"code":"continue","description":"Jump to the next iteration of the loop."},{"code":"next","description":"Skip registration and reset rules."},{"code":"nextfile","description":"Skip the rest of the current file."},{"code":"exit / exit código","description":"End input, execute END and return a status."},{"code":"return valor","description":"Exit a function with a value."}]},{"title":"Consume all matches","code":"{\n    resto = $0\n    while (match(resto, /[[:alpha:]]+@[[:alnum:].-]+/)) {\n        correo = substr(resto, RSTART, RLENGTH)\n        print correo\n        resto = substr(resto, RSTART + RLENGTH)\n    }\n}","wide":true}]},{"id":"formatted-printing","label":"Formatted Printing","eyebrow":"10 · OUTPUT","title":"Formatted printing","tag":"print, printf and redirection","icon":"%","note":"print adds ORS and separates arguments with OFS. printf uses explicit formatting and does not add line breaks: include it with \\n when needed.","cards":[{"title":"print vs printf","entries":[{"code":"print $1, $2","description":"Separate arguments with OFS and end with ORS."},{"code":"print $1 $2","description":"Concatenate without OFS."},{"code":"printf \"%s %d\\n\", $1, $2","description":"Precise control of types, width and termination."},{"code":"texto = sprintf(\"%.2f\", n)","description":"Build a formatted string."},{"code":"OFMT = \"%.6g\"","description":"Numeric format used by print."},{"code":"CONVFMT = \"%.6g\"","description":"Format when converting numbers to strings."}]},{"title":"printf conversions","entries":[{"code":"%s","description":"Chain."},{"code":"%d / %i","description":"Decimal integer."},{"code":"%f","description":"Decimal floating point."},{"code":"%e / %E","description":"Scientific notation."},{"code":"%g / %G","description":"Automatic compact format."},{"code":"%o / %x / %X","description":"Octal/hexadecimal."},{"code":"%c / %%","description":"Literal percentage character/sign."}]},{"title":"Width, precision and alignment","entries":[{"code":"%10s","description":"Right aligned string in 10 columns."},{"code":"%-10s","description":"String aligned left."},{"code":"%08d","description":"8-position integer padded with zeros."},{"code":"%10.2f","description":"Width 10 and two decimal places."},{"code":"%*.*f","description":"Take width and precision from arguments."},{"code":"%+.2f","description":"Always show the sign."}]},{"title":"Redirection and piping","entries":[{"code":"print > \"salida.txt\"","description":"Redirect; AWK keeps the file open."},{"code":"print >> \"salida.txt\"","description":"Add to the end."},{"code":"print | \"sort\"","description":"Send output to a command."},{"code":"print |& comando","description":"gawk: two-way communication with coprocessing."},{"code":"close(destino)","description":"Close file or pipe when no longer used."},{"code":"fflush(destino)","description":"recent gawk/POSIX: Flush output buffer."}]},{"title":"Aligned table","code":"BEGIN {\n    printf \"%-20s %8s %12s\n\", \"Producto\", \"Cant.\", \"Total\"\n    printf \"%-20s %8s %12s\n\", \"--------------------\", \"--------\", \"------------\"\n}\n{\n    total = $2 * $3\n    printf \"%-20.20s %8d %12.2f\n\", $1, $2, total\n    gran_total += total\n}\nEND {\n    printf \"%41s\n\", \"------------\"\n    printf \"%-29s %12.2f\n\", \"TOTAL\", gran_total\n}","wide":true}]},{"id":"miscellaneous","label":"Miscellaneous","eyebrow":"11 · TOOLBOX","title":"Miscellaneous and recipes","tag":"One-liners, portability and debugging","icon":"…","note":"For durable automation, prefer programs in files, single quotes in the shell, variables with -v and POSIX features unless you have decided to depend on gawk.","cards":[{"title":"Essential one-liners","entries":[{"code":"awk 'NF' archivo","description":"Delete empty lines."},{"code":"awk '!visto[$0]++' archivo","description":"Eliminate duplicate lines while preserving order."},{"code":"awk '{ suma += $1 } END { print suma }'","description":"Add the first column."},{"code":"awk 'END { print NR }' archivo","description":"Count records."},{"code":"awk '{ print NF, $0 }' archivo","description":"Prefix each line with its number of fields."},{"code":"awk 'length > max { max=length; linea=$0 } END{print linea}'","description":"Find the longest line."}]},{"title":"Reformat and select","entries":[{"code":"awk -F, -v OFS=';' '{$1=$1; print}'","description":"Change the field separator."},{"code":"awk '{ print $NF }'","description":"Print the last field."},{"code":"awk 'NR >= 10 && NR <= 20'","description":"Print a range of lines."},{"code":"awk '$1 == max { print }' max=42","description":"Assign a variable in the invocation."},{"code":"awk '{ for(i=NF;i;i--) printf \"%s%s\",$i,(i>1?OFS:ORS) }'","description":"Reverse the order of fields."}]},{"title":"Shell and security","entries":[{"code":"awk -v valor=\"$variable\" '...'","description":"Pass shell data without injecting it into the program."},{"code":"'programa AWK'","description":"Use single quotes to protect $, \\, and spaces from the shell."},{"code":"system(\"cmd \" dato)","description":"Risky with external entry; avoid building unescaped commands."},{"code":"--","description":"Some implementations mark the end of options; check portability."},{"code":"/dev/stderr","description":"Common, but not POSIX; in gawk use print ... > \"/dev/stderr\"."}]},{"title":"Portability and performance","entries":[{"code":"LC_ALL=C","description":"More predictable and faster class, order and number results."},{"code":"gawk --lint --posix -f script.awk","description":"Detect extensions when testing portability."},{"code":"next","description":"Avoid unnecessary work on later rules."},{"code":"close()","description":"Avoid exhausting open files and processes."},{"code":"sub() antes que gsub()","description":"If you only need to replace the first match."},{"code":"regex literal","description":"Preferable to rebuilding the same dynamic regex per record."}]},{"title":"Debugging and diagnosis","code":"# Trace output to stderr (gawk and typical Unix systems)\nprint \"DEBUG NR=\" NR \", NF=\" NF > \"/dev/stderr\"\n\n# Display fields with unambiguous delimiters\nfor (i = 1; i <= NF; i++)\n    printf \"[$%d]=<%s>\n\", i, $i > \"/dev/stderr\"\n\n# Check syntax and warnings\ngawk --lint -f programa.awk </dev/null\n\n# Execution profile in gawk\ngawk --profile -f programa.awk datos","wide":true}]}];
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
        '" aria-label="Copy code" title="Copy"><span aria-hidden="true">⧉</span>' +
        (compact ? "" : "<span>Copy</span>") + "</button>";
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
        '</div><div><strong>Key idea.</strong> ' + escapeHtml(topic.note) + '</div>';
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
          : '<span aria-hidden="true">✓</span><span>Copied</span>';
        button.title = "Copied";
        window.setTimeout(function () {
          button.innerHTML = original;
          button.title = "Copy";
        }, 1400);
      } catch (error) {
        button.title = "Could not copy";
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
