#!/usr/bin/env python3
"""Apply reviewed technical terminology corrections after translation."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1] / "docs" / "cheatsheets"

COMMON = {
    "The minimum to not get lost": "The essentials for getting started",
    "Mouse holder": "Mouse support",
    "Home and sessions": "Starting tmux and managing sessions",
    "Panels": "Panes",
    "panels": "panes",
    "Panel": "Pane",
    "panel": "pane",
    "Comandos de shell": "Shell commands",
    "Ejemplo de script": "Script example",
    "Movimiento por bloques y pantalla": "Movement by blocks and screens",
    "Guardar y salir": "Save and exit",
    "Atajos y opciones recomendadas": "Recommended shortcuts and options",
    "Extienda tmux y siga aprendiendo": "Extend tmux and keep learning",
}

AWK = {
    "02 · COINCIDENCES": "02 · MATCHING",
    "03 · ENTRANCE": "03 · INPUT",
    "06 · Features": "06 · FUNCTIONS",
    '"title":"Features"': '"title":"Functions"',
    "Text, numbers and proper functions": "Text, numbers, and user-defined functions",
    "Own function with premises": "User-defined function with local variables",
    "Entry dividers": "Input separators",
    "Cross two files by key": "Join two files by key",
    "Frequencies sorted by quantity": "Frequencies sorted by count",
    "09 · REPEAT": "09 · REPETITION",
    "10 · EXIT": "10 · OUTPUT",
    "TOOL BOX": "TOOLBOX",
    'title="Copiar"': 'title="Copy"',
    "AWK reads an entry record by record": "AWK reads input one record at a time",
    "if you skip the action": "if you omit the action",
    "AWK prints the log": "AWK prints the record",
    "Before entry / after all entry.": "Before input / after all input.",
    "module and power": "modulo and exponentiation",
    "s length; no argument uses $0.": "Length of s; without an argument, it uses $0.",
    "starts from scratch.": "starts from zero.",
    "when importing.": "when it matters.",
    "# Líneas vacías o solo con espacios": "# Empty or whitespace-only lines",
    "# IPv4 aproximada al inicio del registro": "# Approximate IPv4 address at the start of the record",
    "# Extraer todos los números de una línea": "# Extract every number from a line",
    "# usuarios.txt: id nombre": "# users.txt: id name",
    "# ventas.txt:  id importe": "# sales.txt:  id amount",
    "# Imprimir desde [section] hasta la próxima línea vacía": "# Print from [section] through the next blank line",
    "# Las dos fronteras se evalúan por separado.": "# The two boundaries are evaluated separately.",
    "# Un rango no puede activarse y desactivarse en el": "# In traditional awk, a range cannot start and stop on",
    "# mismo registro en awk tradicional.": "# the same record.",
    "# Use paréntesis cuando mezcle familias": "# Use parentheses when mixing operator families",
    "# La concatenación puede sorprender": "# Concatenation can be surprising",
    "# Asignación dentro de una condición": "# Assignment inside a condition",
    "# Ternario dentro de printf": "# Ternary expression inside printf",
    "# Los parámetros tras espacios son locales por convención": "# Parameters after extra spaces are local by convention",
    "# gawk: imprimir palabras más frecuentes primero": "# gawk: print the most frequent words first",
    "# Recorrer todos los campos": "# Iterate over every field",
    "# Recorrer en sentido inverso": "# Iterate in reverse",
    "# Contar y recorrer claves": "# Count and iterate over keys",
    "# Trazas a stderr (gawk y Unix habituales)": "# Trace output to stderr (gawk and typical Unix systems)",
    "# Mostrar campos delimitados inequívocamente": "# Display fields with unambiguous delimiters",
    "# Comprobar sintaxis y advertencias": "# Check syntax and warnings",
    "# Perfil de ejecución en gawk": "# Execution profile in gawk",
}

TMUX = {
    "Prefixed window shortcuts": "Window shortcuts using the prefix",
    "Buffers and configuration": "Copy buffers and configuration",
    "Shortcuts in copy mode": "Copy-mode shortcuts",
    "Layout Shortcuts": "Layout shortcuts",
    "Things that usually break": "Common troubleshooting issues",
    "<code>prefijo</code>": "<code>Prefix</code>",
    "<code>Espacio</code>": "<code>Space</code>",
    "<code>RePág</code>": "<code>Page Up</code>",
    "<code>AvPág</code>": "<code>Page Down</code>",
    "Desplazar arriba/abajo.": "Scroll up/down.",
    "panees": "panes",
    "<code>:save-buffer archivo</code>": "<code>:save-buffer file</code>",
    "# Soporte para ratón": "# Mouse support",
    "# Teclas Vim en modo copiar": "# Vim keys in copy mode",
    "# Soporte para 256 colores": "# 256-color support",
    "# Títulos útiles": "# Useful titles",
    "# Atajos para dividir panes": "# Shortcuts for splitting panes",
    "# Recargar configuración": "# Reload configuration",
    'display-message "¡Configuración recargada!"': 'display-message "Configuration reloaded!"',
    "Ejecute <code>tmux attach -t sesión</code> from several terminals": "Run <code>tmux attach -t session</code> from multiple terminals",
}

VIM = {
    "Command line (:)&": "Command line (:)&",
    "Command line (:)": "Command-line Mode (:)",
    "Quick setup options": "Useful configuration options",
    "<code>Ctrl + r {registro}</code>": "<code>Ctrl + r {register}</code>",
    "<code>:e archivo</code>": "<code>:e file</code>",
    "<code>/texto</code>": "<code>/text</code>",
    "<code>?texto</code>": "<code>?text</code>",
    '" Configuración básica recomendada': '" Recommended basic configuration',
    '" Atajos útiles': '" Useful shortcuts',
    '" Insertar texto al inicio de muchas líneas': '" Insert text at the start of many lines',
    '" modo visual en bloque': '" blockwise Visual mode',
    '" bajar para seleccionar varias líneas': '" move down to select multiple lines',
    '" insertar al inicio del bloque': '" insert at the start of the block',
    '" escriba el texto deseado': '" type the desired text',
    '" Vim repetirá el cambio en cada línea seleccionada': '" Vim repeats the change on every selected line',
    '" Dentro de modo visual, seleccione el rango': '" In Visual mode, select the range',
    '" Reemplaza solo dentro de la selección, con confirmación': '" Replace only within the selection, with confirmation',
}


def apply(name: str, replacements: dict[str, str], include_common: bool = True) -> None:
    path = ROOT / f"{name}.md"
    text = path.read_text(encoding="utf-8")
    combined = {**COMMON, **replacements} if include_common else replacements
    for old, new in combined.items():
        text = text.replace(old, new)
    path.write_text(text, encoding="utf-8")


apply("awk", AWK, include_common=False)
apply("tmux", TMUX)
apply("vim", VIM)
