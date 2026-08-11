---
title: The Ultimate Regular Expressions Cheat Sheet
description: Find, validate, extract, and transform text with practical regular-expression patterns.
---

# The Ultimate Regular Expressions Cheat Sheet

Find, validate, extract, and transform text with confidence. Start with common tokens, choose the correct regex flavor, and test patterns against both positive and negative examples.

[Practice on regex101.com](https://regex101.com/){ .md-button .md-button--primary }
[Back to the dashboard](/#cheat-sheets){ .md-button }

??? tip "Material for MkDocs configuration"

    This page uses admonitions, content tabs, card grids, data tables, buttons, footnotes, and abbreviation tooltips. Add these extensions to `mkdocs.yml`:

    ```yaml
    markdown_extensions:
      - abbr
      - admonition
      - attr_list
      - footnotes
      - md_in_html
      - tables
      - pymdownx.details
      - pymdownx.highlight:
          anchor_linenums: true
      - pymdownx.inlinehilite
      - pymdownx.superfences
      - pymdownx.tabbed:
          alternate_style: true
    ```

## Choose the correct regex flavor

!!! warning "Regex flavors differ"

    JavaScript, PCRE, Python, .NET, Java, POSIX tools, and Vim do not support every token in exactly the same way. Always select the matching flavor when testing a pattern.[^flavors]

=== "JavaScript"

    Commonly uses `/pattern/flags`, `$1` for numbered replacements, `${name}` for named replacements, and flags such as `g`, `i`, `m`, `s`, `u`, `y`, and `d`.

=== "Python"

    Uses the `re` module, supports Python-style named groups such as `(?P<name>...)`, and commonly uses `\g<1>` or `\g<name>` in replacements.

=== "PCRE, .NET, and Java"

    These engines support many advanced constructs, but named groups, backreferences, atomic groups, Unicode handling, and replacement syntax still vary by engine.

=== "POSIX tools and Vim"

    POSIX BRE/ERE syntax is smaller than PCRE-style syntax. Vim has its own modifiers and escaping rules, including `\c` and `\C` for case behavior.

## Quick navigation

<div class="grid cards" markdown>

- **01 · All tokens**

  A compact master table of the most important regex tokens.

  [Open section](#all-tokens)

- **02 · Common tokens**

  The everyday core: characters, sets, repetition, classes, groups, and boundaries.

  [Open section](#common-tokens)

- **03 · General tokens**

  Literals, line breaks, tabs, Unicode escapes, quoting, and inline comments.

  [Open section](#general-tokens)

- **04 · Anchors**

  Match string, line, word, and previous-match positions.

  [Open section](#anchors)

- **05 · Meta sequences**

  Shorthand character classes, whitespace, line breaks, and Unicode properties.

  [Open section](#meta-sequences)

- **06 · Quantifiers**

  Greedy, lazy, possessive, exact, minimum, and bounded repetition.

  [Open section](#quantifiers)

- **07 · Group constructs**

  Captures, alternation, backreferences, lookarounds, atomic groups, and modifiers.

  [Open section](#group-constructs)

- **08 · Character classes**

  Positive and negative sets, ranges, symbols, and POSIX classes.

  [Open section](#character-classes)

- **09 · Flags and modifiers**

  Case, global matching, multiline, dotall, Unicode, free-spacing, and Vim options.

  [Open section](#flags-and-modifiers)

- **10 · Substitutions**

  Captured replacements, date reformatting, whitespace cleanup, and Vim commands.

  [Open section](#substitutions)

</div>

## All tokens

*Master reference.*

| Pattern | Meaning | Example | Matches |
| --- | --- | --- | --- |
| `.` | Any character, usually except a newline | `c.t` | `cat`, `cot`, `c7t` |
| `\` | Escape a special character | `\.` | A literal period |
| `[abc]` | One character from the set | `[cm]at` | `cat`, `mat` |
| `[^abc]` | One character not in the set | `[^c]at` | `bat`, not `cat` |
| `[a-z]` | One character in a range | `[a-f]` | `a` through `f` |
| `\d` / `\D` | Digit / non-digit | `\d+` | `7`, `2026` |
| `\w` / `\W` | Word / non-word character | `\w+` | `user_42` |
| `\s` / `\S` | Whitespace / non-whitespace | `a\sb` | `a b` |
| `^` / `$` | Start / end of string or line | `^cat$` | Only `cat` |
| `\b` / `\B` | Word boundary / non-boundary | `\bcat\b` | `cat`, not `catalog` |
| `*` | Zero or more | `ca*t` | `ct`, `cat`, `caaat` |
| `+` | One or more | `a+` | `a`, `aa`, `aaa` |
| `?` | Zero or one | `colou?r` | `color`, `colour` |
| `{n}` | Exactly *n* repetitions | `a{2}` | `aa` |
| `{n,m}` | Between *n* and *m* repetitions | `a{2,4}` | `aa`, `aaa`, `aaaa` |
| `{n,}` | At least *n* repetitions | `a{2,}` | `aa`, `aaa...` |
| `(ab)` | Capturing group | `(ab){2}` | `abab` |
| `(?:ab)` | Non-capturing group | `(?:ha)+` | `ha`, `haha` |
| <code>cat&#124;dog</code> | Alternation: either pattern | <code>cat&#124;dog</code> | `cat` or `dog` |
| `(?=x)` / `(?!x)` | Positive / negative lookahead | `\d+(?=px)` | Digits before `px` |
| `(?<=x)` / `(?<!x)` | Positive / negative lookbehind | `(?<=\$)\d+` | Digits after `$` |
| `\1` | Backreference to capture group 1 | `(\w+)\s+\1` | `go go` |

## Common tokens

*Everyday essentials.*

### Characters and sets

- `.` — Any character except, usually, a newline.
- `\.` — A literal period.
- `[abc]` — One listed character.
- `[^abc]` — One character not listed.
- `[a-z]` — One character in the range.

### Structure and repetition

- `^` / `$` — Start or end.
- `*` — Zero or more.
- `+` — One or more.
- `?` — Zero or one.
- `{2,4}` — Between two and four repetitions.

### Shorthand classes

- `\d` — Digit.
- `\w` — Word character.
- `\s` — Whitespace.
- `\D` / `\W` / `\S` — The uppercase forms mean “not.”

### Combining patterns

- `(...)` — Capture a group.
- `(?:...)` — Group without capturing.
- `a|b` — Match `a` or `b`.
- `\b` — Word boundary.
- `\1` — Repeat the text captured by group 1.

## General tokens

*Literals and control characters.*

| Token | Meaning | Example | Matches |
| --- | --- | --- | --- |
| `abc` | Literal sequence | `cat` | The exact text `cat` |
| `\n` | Newline | `one\ntwo` | Text on consecutive lines |
| `\r` | Carriage return | `\r\n` | Windows-style line ending |
| `\t` | Tab | `a\tb` | `a`, tab, `b` |
| `\xHH` | Character from a hexadecimal byte | `\x41` | `A` |
| `\uHHHH` | Unicode code unit in supported engines | `\u0041` | `A` |
| `\Q...\E` | Treat content literally in supported engines | `\Q$5.00\E` | `$5.00` |
| `(?#...)` | Inline comment in supported engines | `\d+(?# number)` | A number |

## Anchors

*Match positions, not characters.*

| Anchor | Meaning | Example | Result |
| --- | --- | --- | --- |
| `^` | Start of string, or line in multiline mode | `^Error` | Lines beginning with `Error` |
| `$` | End of string, or line in multiline mode | `done$` | Lines ending with `done` |
| `\A` | Absolute start of string in supported engines | `\AHello` | `Hello` only at the beginning |
| `\Z` | End of string, sometimes before a final newline | `world\Z` | `world` at the end |
| `\z` | Absolute end of string in supported engines | `world\z` | Strict end position |
| `\b` | Word boundary | `\bcat\b` | `cat`, not `catalog` |
| `\B` | Not a word boundary | `\Bcat` | `cat` inside another word |
| `\G` | End of the previous match or start position in supported engines | `\G,?\w+` | Contiguous tokens |

## Meta sequences

*Character shortcuts.*

| Sequence | Meaning | Typical equivalent | Example |
| --- | --- | --- | --- |
| `\d` | Digit | `[0-9]` in ASCII mode | `\d{4}` → `2026` |
| `\D` | Non-digit | `[^0-9]` | `\D+` → `abc` |
| `\w` | Word character | Often `[A-Za-z0-9_]` | `user_1` |
| `\W` | Non-word character | Inverse of `\w` | `!@#` |
| `\s` | Whitespace | Space, tab, newline | `a\sb` |
| `\S` | Non-whitespace | Inverse of `\s` | `hello` |
| `\h` / `\H` | Horizontal whitespace / inverse | Spaces and tabs | Flavor-dependent |
| `\v` / `\V` | Vertical whitespace / inverse | Line-break characters | Flavor-dependent |
| `\R` | Any Unicode line break | `\n`, `\r\n`, etc. | Flavor-dependent |
| `\p{L}` | Any Unicode letter | Unicode property escape | `A`, `é`, `中` |
| `\p{N}` | Any Unicode number | Unicode property escape | `4`, `٢` |
| `\P{L}` | Anything except a Unicode letter | Negated Unicode property | `7`, `!` |

## Quantifiers

*Control repetition.*

!!! info "Greedy, lazy, and possessive"

    Greedy quantifiers take as much as possible. Lazy quantifiers prefer as little as possible. Possessive quantifiers prevent backtracking and are not available in every engine.

| Quantifier | Meaning | Example | Matches |
| --- | --- | --- | --- |
| `*` | Zero or more, greedy | `go*` | `g`, `go`, `gooo` |
| `+` | One or more, greedy | `go+` | `go`, `gooo` |
| `?` | Zero or one, greedy | `go?` | `g`, `go` |
| `{n}` | Exactly *n* | `\d{4}` | `2026` |
| `{n,}` | At least *n* | `a{2,}` | `aa`, `aaa...` |
| `{n,m}` | From *n* through *m* | `a{2,4}` | `aa` through `aaaa` |
| `*?` / `+?` | Lazy repetition | `<.*?>` | The shortest tag-like segment |
| `{n,m}?` | Lazy bounded repetition | `a{2,4}?` | Prefers two `a` characters |
| `*+` / `++` | Possessive repetition in supported engines | `a++a` | Consumes without backtracking |

### Greedy versus lazy

=== "Greedy"

    ```regex title="Greedy repetition"
    <.*>
    ```

    Against `<b>one</b><i>two</i>`, this typically consumes from the first `<` through the final `>`.

=== "Lazy"

    ```regex title="Lazy repetition"
    <.*?>
    ```

    Against the same input, this prefers the shortest tag-like segments.

=== "Possessive"

    ```regex title="Possessive repetition"
    a++a
    ```

    In supporting engines, `a++` will not give characters back to satisfy the final `a`.

## Group constructs

*Capture, branch, and assert.*

| Construct | Meaning | Example | Result |
| --- | --- | --- | --- |
| `(abc)` | Numbered capturing group | `(ha)+` | `ha`, `haha` |
| `(?:abc)` | Non-capturing group | `(?:https?://)?` | Optional protocol without a capture |
| `(?<name>abc)` | Named capture in many engines | `(?<year>\d{4})` | Capture named `year` |
| `(?P<name>abc)` | Python-style named capture | `(?P<year>\d{4})` | Capture named `year` |
| <code>a&#124;b</code> | Alternation | <code>cat&#124;dog</code> | `cat` or `dog` |
| `\1` | Numbered backreference | `(\w+)\s+\1` | A repeated word |
| `\k<name>` | Named backreference in many engines | `(?<w>\w+) \k<w>` | A repeated named capture |
| `(?=abc)` | Positive lookahead | `\w+(?=:)` | A word followed by a colon |
| `(?!abc)` | Negative lookahead | `foo(?!bar)` | `foo` not followed by `bar` |
| `(?<=abc)` | Positive lookbehind | `(?<=\$)\d+` | Digits after a dollar sign |
| `(?<!abc)` | Negative lookbehind | `(?<!-)\d+` | Digits not preceded by a hyphen |
| `(?>abc)` | Atomic group in supported engines | `(?>a+)a` | No backtracking inside the group |
| `(?i:abc)` | Apply a modifier to one group | `(?i:hello)` | `hello`, `HELLO` |

!!! tip "Capture only what you need"

    Prefer a non-capturing group such as `(?:...)` when grouping is required only for precedence or repetition. This keeps numbered captures stable and easier to maintain.

## Character classes

*Match one character from a set.*

| Class | Meaning | Example | Matches |
| --- | --- | --- | --- |
| `[abc]` | Any one listed character | `[abc]` | `a`, `b`, or `c` |
| `[^abc]` | Any character except those listed | `[^0-9]` | One non-digit |
| `[a-z]` | Lowercase ASCII range | `[a-z]+` | `hello` |
| `[A-Z]` | Uppercase ASCII range | `[A-Z]{2}` | `US` |
| `[0-9]` | ASCII digit range | `[0-9]{2}` | `42` |
| `[A-Za-z0-9_]` | ASCII word-style character | `[A-Za-z_]\w*` | A simple identifier |
| `[a-fA-F0-9]` | Hexadecimal digit | `#[a-fA-F0-9]{6}` | `#00bcd4` |
| `[._-]` | Period, underscore, or hyphen | `[._-]` | One listed symbol |
| `[\[\]]` | Opening or closing square bracket | `[\[\]]` | `[` or `]` |
| `[[:digit:]]` | POSIX digit class | `[[:digit:]]+` | Digits in supporting engines |
| `[[:space:]]` | POSIX whitespace class | `[[:space:]]+` | Whitespace in supporting engines |

!!! warning "A class is not a word"

    `[cat]` matches exactly one character: `c`, `a`, or `t`. Use `(cat)` to group the complete word. Place `-` first or last—or escape it—when you need a literal hyphen.

## Flags and modifiers

*Change matching behavior.*

| Flag | Name | Effect | Example |
| --- | --- | --- | --- |
| `i` | Case-insensitive | Ignore letter case | `/cat/i` matches `CAT` |
| `g` | Global | Find or replace every match | `/cat/g` |
| `m` | Multiline | Make `^` and `$` match line boundaries | `/^Error/gm` |
| `s` | Dotall / single-line | Make `.` also match newlines | `/start.*end/s` |
| `u` | Unicode | Enable Unicode-aware behavior in engines such as JavaScript | `/\p{L}+/u` |
| `x` | Extended / free-spacing | Allow layout whitespace and comments in supported engines | `(?x) \d+ \s+ \w+` |
| `y` | Sticky | Match only at the current position in JavaScript | `/\w+/y` |
| `d` | Indices | Return match indices in modern JavaScript | `/cat/d` |

=== "Inline modifiers"

    `(?i)cat` enables case-insensitive matching where supported. `(?i:cat)` limits the modifier to one group.

=== "Vim modifiers"

    Use `\c` for case-insensitive matching and `\C` for case-sensitive matching, or configure `:set ignorecase`.

## Substitutions

*Search and replace.*

!!! warning "Replacement syntax varies"

    JavaScript commonly uses `$1`, Python uses `\g<1>`, and Vim commonly uses `\1`. Confirm the replacement syntax for your tool before running a bulk edit.

| Goal | Search | Replacement | Result |
| --- | --- | --- | --- |
| Swap first and last names | `(\w+)\s+(\w+)` | `$2, $1` | `Ada Lovelace` → `Lovelace, Ada` |
| Reformat an ISO date | `(\d{4})-(\d{2})-(\d{2})` | `$3/$2/$1` | `2026-07-31` → `31/07/2026` |
| Collapse whitespace | `\s+` | One space | <code>too&nbsp;&nbsp;&nbsp;many</code> → `too many` |
| Remove Markdown checkboxes | `\[[ xX]\]` | Empty text | Removes `[ ]`, `[x]`, and `[X]` |
| Wrap every number | `(\d+)` | `[$1]` | `42` → `[42]` |

### Common replacement references

- `$&` — Entire match in JavaScript.
- `$1` / `$2` — Numbered groups in JavaScript.
- `${name}` — Named group in JavaScript.
- `\g<name>` — Named group in Python.

### Vim substitution

- `:%s/old/new/g` — Replace all occurrences.
- `:%s/\[x\]//g` — Delete every `[x]`.
- `:%s/\[[ xX]\]//gc` — Delete checkboxes with confirmation.
- `&` / `\1` — Entire match or captured group 1.

## A practical workflow

1. State what the pattern should match in plain language.
2. Start with literals and add one token at a time.
3. Test valid examples and near misses.
4. Select the exact flavor used by the target application.
5. Prefer readable patterns over clever ones.
6. Benchmark patterns that will run against large or untrusted inputs.

[Practice on regex101.com](https://regex101.com/){ .md-button .md-button--primary }
[Back to the dashboard](https://greivinvenegas.com/){ .md-button }

[^flavors]: The syntax and behavior of anchors, Unicode properties, lookbehind, atomic groups, possessive quantifiers, inline modifiers, and replacements vary significantly between engines.

*[ASCII]: American Standard Code for Information Interchange
*[BRE]: Basic Regular Expression
*[ERE]: Extended Regular Expression
*[PCRE]: Perl-Compatible Regular Expressions
*[POSIX]: Portable Operating System Interface
