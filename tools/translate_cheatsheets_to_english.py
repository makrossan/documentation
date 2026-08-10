#!/usr/bin/env python3
"""Translate cheat-sheet prose without modifying code or HTML structure."""

from __future__ import annotations

import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

from lxml import html


ROOT = Path(__file__).resolve().parents[1]
CHEATSHEETS = ROOT / "docs" / "cheatsheets"
SPANISH = re.compile(
    r"(?i)(?:[áéíóúñ¿¡]|\b(?:el|la|los|las|una|para|con|sin|que|cómo|"
    r"archivo|comando|modo|línea|copiar|borrar|salida|entrada|siguiente|"
    r"anterior|todos|usuario|directorio|servicio|sesión|panel|ventana|"
    r"patrón|acción|campo|registro|inicio|fin|buscar|reemplazar|hoja|trucos|"
    r"crear|listar|gestionar|organizar|atajos|opciones|extienda|siga|"
    r"aprendiendo|paneles|fundamentos|coincidencias|expresiones|regulares|"
    r"registros|campos|funciones|operadores|condiciones|bucles)\b)"
)

EXACT = {
    "Hoja de trucos AWK": "AWK Cheat Sheet",
    "Hoja de Trucos tmux": "tmux Cheat Sheet",
    "La guía definitiva y hoja de trucos de tmux": "The Ultimate tmux Guide and Cheat Sheet",
    "Hoja de trucos Vim por modos": "Vim Cheat Sheet by Mode",
    "Volver al Dashboard anterior": "Back to the dashboard",
    "Compatibilidad": "Compatibility",
    "Rápido": "Fast",
    "ÍNDICE": "INDEX",
    "Índice": "Index",
    "para navegar": "to navigate",
    "Idea clave.": "Key idea.",
    "Modo Normal": "Normal Mode",
    "Modo Insertar": "Insert Mode",
    "Línea de comandos": "Command-line Mode",
    "Modo Visual": "Visual Mode",
}

REPAIRS = {
    "Stunt Sheet": "Cheat Sheet",
    "Trick Sheet": "Cheat Sheet",
    "trick sheet": "cheat sheet",
    "Dialcode": "Prefix",
    "dialcode": "prefix",
    "restart the service": "restart the service",
    "archive": "file",
    "Archives": "Files",
    "archive name": "file name",
}

CACHE_PATH = Path("/tmp/mkdocs-cheatsheet-google-cache.json")
if CACHE_PATH.exists():
    CACHE = json.loads(CACHE_PATH.read_text(encoding="utf-8"))
else:
    CACHE = {}


def google_translate(text: str) -> str:
    if text in CACHE:
        return CACHE[text]
    query = urllib.parse.urlencode(
        {"client": "gtx", "sl": "es", "tl": "en", "dt": "t", "q": text}
    )
    request = urllib.request.Request(
        "https://translate.googleapis.com/translate_a/single?" + query,
        headers={"User-Agent": "Mozilla/5.0"},
    )
    for attempt in range(5):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                payload = json.load(response)
            result = "".join(part[0] for part in payload[0] if part[0])
            CACHE[text] = result
            CACHE_PATH.write_text(
                json.dumps(CACHE, ensure_ascii=False, indent=2), encoding="utf-8"
            )
            time.sleep(0.08)
            return result
        except Exception:
            if attempt == 4:
                raise
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError("Translation retry loop exited unexpectedly")


def english(text: str, force: bool = False) -> str:
    leading = text[: len(text) - len(text.lstrip())]
    trailing = text[len(text.rstrip()) :]
    core = text.strip()
    if not core:
        return text
    if core in EXACT:
        result = EXACT[core]
    elif not force and not SPANISH.search(core):
        return text
    else:
        result = google_translate(core)
    for wrong, right in REPAIRS.items():
        result = result.replace(wrong, right)
    return leading + result + trailing


def translate_fragment(markdown: str) -> str:
    front, separator, fragment = markdown.partition("---\n\n")
    if not separator:
        raise ValueError("Expected YAML front matter")
    wrapper = html.fragment_fromstring(fragment, create_parent="div")
    blocked = {"code", "pre", "script", "style"}
    for element in wrapper.iter():
        if element.tag not in blocked and element.text:
            element.text = english(element.text)
        if element.tail:
            element.tail = english(element.tail)
        for attribute in ("aria-label", "title"):
            if attribute in element.attrib:
                element.attrib[attribute] = english(element.attrib[attribute])
    rendered = "".join(
        html.tostring(child, encoding="unicode", method="html") for child in wrapper
    )
    return front + separator + rendered.rstrip() + "\n"


def translate_awk_script(markdown: str) -> str:
    match = re.search(r"(const topics = )(\[.*?\]);\n", markdown, flags=re.S)
    if not match:
        raise ValueError("AWK topics JSON was not found")
    topics = json.loads(match.group(2))
    prose_keys = {"label", "eyebrow", "title", "tag", "note", "description", "caption"}

    def visit(value, key=""):
        if isinstance(value, dict):
            return {k: visit(v, k) for k, v in value.items()}
        if isinstance(value, list):
            return [visit(item, key) for item in value]
        if isinstance(value, str) and key in prose_keys:
            return english(value, force=True)
        return value

    encoded = json.dumps(visit(topics), ensure_ascii=False, separators=(",", ":"))
    markdown = markdown[: match.start(2)] + encoded + markdown[match.end(2) :]
    replacements = {
        "Copiar código": "Copy code",
        ">Copiar<": ">Copy<",
        ">Copiado<": ">Copied<",
        'button.title = "Copiado"': 'button.title = "Copied"',
        'button.title = "Copiar"': 'button.title = "Copy"',
        'button.title = "No se pudo copiar"': 'button.title = "Could not copy"',
        "Idea clave.": "Key idea.",
    }
    for old, new in replacements.items():
        markdown = markdown.replace(old, new)
    return markdown


def main() -> None:
    for path in sorted(CHEATSHEETS.glob("*.md")):
        original = path.read_text(encoding="utf-8")
        translated = translate_fragment(original)
        if path.name == "awk.md":
            translated = translate_awk_script(translated)
        path.write_text(translated, encoding="utf-8")
        print(f"Translated {path.name}", flush=True)


if __name__ == "__main__":
    main()
