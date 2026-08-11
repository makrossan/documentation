---
title: AWK Cheat Sheet
description: A practical AWK reference—from the first filter to complete programs.
---

# AWK Cheat Sheet

From your first filter to complete programs, organized for quick reference and daily use.

[Back to the dashboard](/#cheat-sheets){ .md-button }
[Open the GNU AWK manual](https://www.gnu.org/software/gawk/manual/gawk.html){ .md-button .md-button--primary }

??? tip "Material for MkDocs configuration"

    This page uses admonitions, annotations, content tabs, card grids, code-block titles, footnotes, and abbreviation tooltips. Add these extensions to `mkdocs.yml`:

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

## Choose an implementation

=== "awk (POSIX)"

    Prefer this when portability matters. The entries marked **gawk** are GNU extensions and should be avoided in strictly POSIX scripts.

=== "gawk (GNU)"

    GNU `gawk` adds features such as `BEGINFILE`, `ENDFILE`, `FPAT`, `patsplit()`, arrays of arrays, sorting helpers, time functions, and profiling.[^gawk]

=== "mawk"

    `mawk` is a compact, fast implementation. Check its documentation before relying on behavior that is not defined by POSIX.

## Getting started

*From zero to a useful AWK program.*

!!! info "Key idea"

    AWK reads input one record at a time, tests every pattern, and runs its action. If the pattern is omitted, the action always runs. If the action is omitted, AWK prints the record.

### Ways to invoke AWK

- `awk 'program' file` — Run a short program against one file.
- `awk 'program' file1 file2` — Process multiple files as one input sequence.
- `awk -F: '{ print $1 }' /etc/passwd` — Set the field separator with `-F`.
- `awk -v limit=10 '$3 > limit' data` — Pass a variable before `BEGIN` runs.
- `awk -f program.awk data` — Load the program from a file.
- `command | awk '{ print $1 }'` — Read the standard output of another command.

### Execution model

- `BEGIN { ... }` — Run once before reading input.
- `pattern { action }` — Evaluate once for every input record.
- `END { ... }` — Run once after input ends or `exit` is called.
- `pattern` — Use the implicit action `{ print $0 }`.
- `{ action }` — Use an implicit pattern that is true for every record.
- `# comment` — Comment from `#` to the end of the line.

### Essential records and fields

- `$0` — The complete current record.
- `$1 … $NF` — The first field through the last field.
- `NF` — Number of fields in the current record.
- `NR` — Cumulative record number across all input files.
- `FNR` — Record number within the current file.
- `FS` / `OFS` — Input and output field separators.
- `RS` / `ORS` — Input and output record separators.

### Options worth memorizing

- `-F 'regex'` — Set `FS` from the command line.
- `-v name=value` — Assign a variable before `BEGIN`.
- `-f program.awk` — Read the program from a file.
- `-f one.awk -f two.awk` — Combine multiple program files.
- `gawk --lint` — Warn about questionable or nonportable constructs.
- `gawk --posix` — Restrict extensions and prioritize POSIX behavior.

### Minimal complete script

```awk title="report.awk" linenums="1"
#!/usr/bin/awk -f

BEGIN {
    FS = ","       # (1)!
    OFS = "\t"     # (2)!
}

NR > 1 && $3 >= 70 {
    total += $3
    passed++
    print $1, $3
}

END {
    if (passed)
        printf "Average: %.2f\n", total / passed  # (3)!
}
```

1. Split each input record on commas.
2. Separate output fields with a tab.
3. Guard the division so an empty result set never causes division by zero.

Save the file as `report.awk`, run `chmod +x report.awk`, and execute it with `./report.awk data.csv`.

## Regular expressions

*POSIX ERE syntax and dynamic patterns.*

!!! info "Key idea"

    AWK uses extended regular expressions (EREs). A `/regex/` literal tests `$0`; the `~` and `!~` operators can test any string or field.

### Basic use

- `/error/` — Match records whose `$0` contains `error`.
- `$2 ~ /^[A-Z]/` — Match when the second field begins with an uppercase letter.
- `$3 !~ /^(ok|ready)$/` — Match when the third field is neither exactly `ok` nor `ready`.
- `pat = "warn|fail"; $0 ~ pat` — Store a dynamic regular expression in a variable.
- `tolower($0) ~ /error/` — Perform a portable case-insensitive search.
- `gawk 'BEGIN { IGNORECASE=1 } /error/'` — Enable global case-insensitive matching in `gawk`.

### ERE metacharacters

- `.` — Any single character.
- `^` / `$` — Beginning or end of the string.
- `*` / `+` / `?` — Zero or more, one or more, or zero or one.
- `{m,n}` — Between *m* and *n* repetitions in modern POSIX AWK.
- `[abc]` / `[^abc]` — Positive or negated character class.
- `(one|two)` — Grouping and alternation.
- `\.` — A literal period; escape the metacharacter.

### Portable POSIX character classes

- `[[:alpha:]]` — A letter according to the current locale.
- `[[:digit:]]` — A decimal digit.
- `[[:alnum:]]` — A letter or digit.
- `[[:space:]]` — A space, tab, or newline.
- `[[:blank:]]` — A horizontal space or tab.
- `[[:lower:]]` / `[[:upper:]]` — A lowercase or uppercase letter.
- `[[:xdigit:]]` — A hexadecimal digit.

### `match()`, `RSTART`, and `RLENGTH`

- `match(s, /re/)` — Return the position of the first match, or `0`.
- `RSTART` — Starting index of the most recent match.
- `RLENGTH` — Length of the most recent match, or `-1` when no match was found.
- `substr(s, RSTART, RLENGTH)` — Extract exactly the text that matched.
- `match(s, /([0-9]+)/, m)` — **gawk:** save the match and captured groups in `m`.

### Regular-expression recipes

```awk title="regex-recipes.awk"
# Blank lines or lines containing only whitespace
/^[[:space:]]*$/

# Approximate IPv4 address at the beginning of a record
match($0, /^([0-9]{1,3}[.]){3}[0-9]{1,3}/)

# Extract every number from a line
{
    s = $0
    while (match(s, /[0-9]+([.][0-9]+)?/)) {
        print substr(s, RSTART, RLENGTH)
        s = substr(s, RSTART + RLENGTH)
    }
}
```

## Reading files and streams

*Fields, records, and `getline`.*

!!! info "Key idea"

    `FS` splits records into fields, while `RS` splits input into records. Setting them in `BEGIN` is usually clearest. Reserve `getline` for additional input sources or explicit input control.

### Multiple files

- `FILENAME` — Name of the current input file.
- `NR == FNR` — True while AWK is processing the first file.
- `FNR == 1` — First line of each file.
- `ARGC` / `ARGV` — Argument count and argument vector for the invocation.
- `ARGIND` — **gawk:** index in `ARGV` of the current file.
- `next` — Skip the remaining rules for the current record.
- `nextfile` — Stop reading the current file and open the next one.

### Input separators

- `FS = ","` — Split fields on a literal comma.
- `FS = "[[:space:]]+"` — Split on one or more POSIX whitespace characters.
- `FS = ""` — **gawk/mawk:** split into individual characters; not POSIX.
- `RS = ""` — Paragraph mode: records are separated by blank lines.
- `RS = "END|STOP"` — **gawk:** use a regular expression as `RS`.
- `RT` — **gawk:** text matched by `RS`.

### Special `gawk` field features

- `FIELDWIDTHS = "5 10 8"` — Split on fixed widths instead of `FS`.
- `FPAT = "([^,]+)|(\"[^\"]+\")"` — Define what constitutes a field; useful for simple CSV.
- `patsplit(s, a, fpat, seps)` — Split by field content and save separators.
- `split(s, a, fs, seps)` — Split and capture matching separators.

### `getline` variants

- `getline` — Read the next record into `$0` and recalculate `NF`.
- `getline variable` — Read into a variable without changing `$0` or `NF`.
- `getline variable < file` — Read from another file; always test the return value.
- `command | getline variable` — Read one line from a command's output.
- `result = getline variable` — Save the status: `1` read, `0` end of file, `-1` error.
- `close(file_or_command)` — Close a resource to avoid exhausting file descriptors.

### Join two files by key

```awk title="join-by-key.awk"
# users.txt: id name
# sales.txt: id amount
awk '
    NR == FNR { name[$1] = $2; next }
    $1 in name { total[name[$1]] += $2 }
    END {
        for (person in total)
            print person, total[person]
    }
' users.txt sales.txt
```

`NR == FNR` loads the first file, and `next` prevents those records from reaching the sales rules.

## Patterns, actions, and variables

*The heart of the language.*

!!! info "Key idea"

    Every rule has the form `pattern { action }`. Rules are tested in order for the same record unless `next`, `nextfile`, or `exit` changes the flow.

### Pattern types

- `BEGIN` / `END` — Before input or after all input.
- `BEGINFILE` / `ENDFILE` — **gawk:** before and after each file.
- `/regex/` — Match against `$0`.
- `$3 > 100` — Boolean expression.
- `/start/, /end/` — Inclusive stateful range between two patterns.
- `pat1 && pat2` — Combine conditions with Boolean logic.

### Built-in field variables

- `FS` / `OFS` — Input and output field separators.
- `RS` / `ORS` — Input and output record separators.
- `NF` / `NR` / `FNR` — Current field count, total record number, and per-file record number.
- `FILENAME` — Name of the file currently being processed.
- `SUBSEP` — Internal separator for simulated multidimensional indexes.
- `CONVFMT` / `OFMT` — Numeric conversion format and `print` numeric output format.

### Variables from the shell

- `awk -v x=value 'BEGIN{print x}'` — Make an assignment available before `BEGIN`.
- `awk '{...}' x=value file` — Process an assignment at its position in `ARGV`.
- `ENVIRON["HOME"]` — Read an environment variable inside AWK.
- `export MODE=prod` — Export a shell variable before reading `ENVIRON["MODE"]`.
- `ARGV[1] = ""` — Remove an argument so AWK does not treat it as a file.

### Changing fields and rebuilding `$0`

- `$2 = toupper($2)` — Modify a field and rebuild `$0` using `OFS`.
- `$1 = $1` — Force the record to be rebuilt with the current `OFS`.
- `NF--` — Reduce `NF`, removing the last field in `gawk` and `mawk`.
- `$0 = new_line` — Assign to `$0` and split the fields again using `FS`.

### Range patterns

```awk title="range-pattern.awk"
# Print from [section] through the next blank line
/^\[section\]$/, /^[[:space:]]*$/ {
    print
}

# The two boundaries are evaluated separately.
# In traditional awk, a range cannot turn on and off
# on the same record.
```

## Operators

*Arithmetic, comparison, and control.*

!!! warning "Be explicit about types"

    AWK converts between numbers and strings according to context. Use `+ 0` to force numeric comparison or concatenate `""` to force string comparison when values such as `001`, dates, or identifiers must not be compared ambiguously.

### Arithmetic and assignment

- `+ - * / % ^` — Addition, subtraction, multiplication, division, remainder, and exponentiation.
- `++x` / `x++` — Prefix or postfix increment.
- `--x` / `x--` — Prefix or postfix decrement.
- `= += -= *= /= %= ^=` — Simple and compound assignment.
- `-x` / `+x` — Unary negation or numeric conversion.

### Comparison and logic

- `== != < <= > >=` — Numeric or string comparisons, depending on the operands.
- `&&` / `||` / `!` — Logical AND, OR, and NOT; `&&` and `||` short-circuit.
- `string ~ /re/` — Test whether a string matches a regular expression.
- `string !~ /re/` — Test whether a string does not match a regular expression.
- `index in array` — Test for existence without creating the element.

### AWK-specific operators

- `a b` — Concatenation without a visible operator.
- `condition ? yes : no` — Ternary conditional expression.
- `$expression` — Indirect field reference; for example, `$(i + 1)`.
- `expr1, expr2` — Comma in argument lists or a range pattern.
- `(i, j) in a` — Test a compound index built with `SUBSEP`.

### Practical precedence

```awk title="precedence.awk"
# Use parentheses when mixing operator families
average = (sum + extra) / (n + 1)

# Concatenation can be surprising
key = (prefix i) "-" suffix

# Assignment inside a condition
if ((line = getline) > 0)
    print $0

# A ternary expression inside printf
printf "%s\n", (n ? total / n : "N/A")
```

Parentheses turn intent into documentation and remove the need to rely on a precedence table.

## Functions

*Text, numbers, system integration, and reusable code.*

!!! info "Key idea"

    Scalar arguments are passed by value, while arrays are passed by reference. AWK has no explicit local-variable declaration. By convention, local variables are added as extra parameters after several spaces in the function signature.

### String functions

- `length(s)` — Length of `s`; without an argument, use `$0`.
- `substr(s, start, length)` — Extract a substring; indexes start at 1.
- `index(s, search)` — Return the position of `search` in `s`, or `0`.
- `tolower(s)` / `toupper(s)` — Convert to lowercase or uppercase.
- `sub(re, replacement, target)` — Replace the first match; `target` defaults to `$0`.
- `gsub(re, replacement, target)` — Replace every match.
- `gensub(re, replacement, how, target)` — **gawk:** replace with backreferences such as `\1` without changing the target.

### Splitting and finding

- `split(s, a, separator)` — Split `s` into `a[1]…a[n]` and return `n`.
- `patsplit(s, a, re)` — **gawk:** build fields from the text that matches.
- `match(s, re)` — Find `re` and set `RSTART` and `RLENGTH`.
- `sprintf(format, args)` — Format and return a string without printing it.

### Numeric functions

- `int(x)` — Truncate toward zero.
- `sqrt(x)` / `exp(x)` / `log(x)` — Square root, exponential, and natural logarithm.
- `sin(x)` / `cos(x)` / `atan2(y,x)` — Trigonometric functions using radians.
- `rand()` — Return a pseudorandom number in `[0, 1)`.
- `srand(seed)` — Change the random seed and return the previous seed.

### System, time, and bitwise functions

- `system(command)` — Run a command and return its exit status.
- `systime()` — **gawk:** current Unix timestamp in seconds.
- `strftime(format, time)` — **gawk:** format a date and time.
- `mktime(date)` — **gawk:** convert `YYYY MM DD HH MM SS` to Unix time.
- `and()` / `or()` / `xor()` / `compl()` — **gawk:** bitwise operations.
- `lshift()` / `rshift()` — **gawk:** bit shifts.

### User-defined functions and local variables

```awk title="functions.awk"
function trim(s) {
    sub(/^[[:space:]]+/, "", s)
    sub(/[[:space:]]+$/, "", s)
    return s
}

# Parameters after the extra spaces are local by convention
function mean(a, n,    i, sum) {
    for (i = 1; i <= n; i++)
        sum += a[i]
    return n ? sum / n : 0
}
```

## Associative arrays

*Counting, indexing, and grouping.*

!!! info "Key idea"

    Every AWK array is associative: indexes are converted to strings. Do not assume an order when iterating with `for (key in array)`; sort explicitly when output order matters.

### Essential operations

- `a[key] = value` — Create or update an element.
- `a[key]++` — Count by key, starting from zero.
- `key in a` — Check for existence without creating an element.
- `delete a[key]` — Delete one element.
- `delete a` — Empty the entire array in `gawk`, `mawk`, and POSIX 2012 or later.
- `for (key in a)` — Visit keys in an unspecified order.

### Multidimensional indexes

- `a[i, j]` — Compound index equivalent to `i SUBSEP j`.
- `(i, j) in a` — Test a compound index.
- `split(key, parts, SUBSEP)` — Decompose a compound key.
- `a[i][j]` — **gawk:** true arrays of arrays.
- `isarray(x)` — **gawk:** test whether `x` is an array.
- `length(a)` — **gawk/mawk:** number of elements; not classic POSIX.

### Sorting in `gawk`

- `asort(source, destination)` — Sort values into `destination[1…n]`.
- `asorti(source, destination)` — Sort indexes into `destination[1…n]`.
- `PROCINFO["sorted_in"]` — Control the order of later `for (key in array)` loops.
- `@ind_str_asc` — Sort indexes as strings in ascending order.
- `@val_num_desc` — Sort values numerically in descending order.

### Frequencies sorted by count

```awk title="word-frequency.awk"
# gawk: print the most frequent words first
{
    for (i = 1; i <= NF; i++)
        frequency[tolower($i)]++
}
END {
    PROCINFO["sorted_in"] = "@val_num_desc"
    for (word in frequency)
        printf "%7d  %s\n", frequency[word], word
}
```

## Conditions

*Filtering, branching, and validation.*

!!! warning "Truth and input types"

    In a Boolean context, zero and the empty string are false; everything else is true. A numeric string such as `"0"` can retain both string and numeric attributes, so validate input when the distinction matters.

### `if`, `else if`, and `else`

```awk title="classification.awk"
if ($3 >= 90) {
    level = "excellent"
} else if ($3 >= 70) {
    level = "passed"
} else {
    level = "review"
}

print $1, level
```

### Patterns as guards

- `NF == 0 { next }` — Ignore records with no fields.
- `$1 ~ /^#/ { next }` — Ignore comments.
- `$3 + 0 > 100` — Force a numeric comparison.
- `($2 "") == "001"` — Force a string comparison.
- `key in seen` — Branch based on key existence.
- `!seen[$1]++` — True only for the first occurrence of `$1`.

### Robust validation

- `$2 ~ /^-?[0-9]+([.][0-9]+)?$/` — Validate a simple decimal before conversion.
- `NF != expected` — Detect rows with the wrong number of fields.
- `(getline) > 0` — Successful read.
- `(getline) == 0` — End of file.
- `(getline) < 0` — Read error; `ERRNO` provides details in `gawk`.
- `ERRNO` — **gawk:** message associated with the most recent I/O error.

### Exit with a useful status

```awk title="validate.awk"
BEGIN { errors = 0 }

NF != 4 {
    printf "Invalid row %d: %s\n", FNR, $0 > "/dev/stderr"
    errors++
}

END {
    if (errors)
        exit 2
}
```

The exit status lets shell scripts, CI jobs, and cron tasks detect a failed validation.

## Loops and flow control

*Iterating over fields, arrays, and input.*

!!! info "Key idea"

    Use a numeric `for` loop when order matters and `for (key in array)` when you only need to visit every element. POSIX does not define the iteration order of an associative array.

### Numeric `for`

```awk title="numeric-for.awk"
# Visit every field
for (i = 1; i <= NF; i++) {
    if ($i ~ /^[0-9]+$/)
        sum += $i
}

# Visit fields in reverse order
for (i = NF; i >= 1; i--)
    printf "%s%s", $i, (i > 1 ? OFS : ORS)
```

### Associative `for`

```awk title="associative-for.awk"
# Count and visit keys
{ count[$1]++ }

END {
    for (key in count) {
        if (count[key] < 2)
            continue
        print key, count[key]
    }
}
```

### `while` and `do…while`

- `while (condition) { ... }` — Test before every iteration.
- `do { ... } while (condition)` — Run at least once.
- `while ((getline line < file) > 0)` — Read an auxiliary file one line at a time.
- `while (match(s, re))` — Consume repeated matches within a string.

### Flow control

- `break` — Leave the nearest loop.
- `continue` — Skip to the next loop iteration.
- `next` — Skip the current record and restart the rules.
- `nextfile` — Skip the rest of the current file.
- `exit` / `exit code` — Stop input, run `END`, and return a status.
- `return value` — Leave a function and return a value.

### Consume every match

```awk title="extract-emails.awk"
{
    rest = $0
    while (match(rest, /[[:alpha:]]+@[[:alnum:].-]+/)) {
        email = substr(rest, RSTART, RLENGTH)
        print email
        rest = substr(rest, RSTART + RLENGTH)
    }
}
```

## Formatted output

*`print`, `printf`, redirection, and pipes.*

!!! info "Key idea"

    `print` adds `ORS` and separates arguments with `OFS`. `printf` uses an explicit format and does not add a newline—include `\n` when you need one.

### `print` versus `printf`

- `print $1, $2` — Separate arguments with `OFS` and finish with `ORS`.
- `print $1 $2` — Concatenate without `OFS`.
- `printf "%s %d\n", $1, $2` — Control types, width, and line termination precisely.
- `text = sprintf("%.2f", n)` — Build a formatted string.
- `OFMT = "%.6g"` — Set the numeric format used by `print`.
- `CONVFMT = "%.6g"` — Set the format used when converting numbers to strings.

### `printf` conversions

- `%s` — String.
- `%d` / `%i` — Decimal integer.
- `%f` — Decimal floating-point value.
- `%e` / `%E` — Scientific notation.
- `%g` / `%G` — Automatic compact format.
- `%o` / `%x` / `%X` — Octal or hexadecimal.
- `%c` / `%%` — Character or literal percent sign.

### Width, precision, and alignment

- `%10s` — Right-align a string in 10 columns.
- `%-10s` — Left-align a string.
- `%08d` — Pad an 8-position integer with zeros.
- `%10.2f` — Use width 10 with two decimal places.
- `%*.*f` — Take width and precision from arguments.
- `%+.2f` — Always display the sign.

### Redirection and pipes

- `print > "output.txt"` — Redirect output; AWK keeps the file open.
- `print >> "output.txt"` — Append output.
- `print | "sort"` — Pipe output to a command.
- `print |& command` — **gawk:** communicate bidirectionally with a coprocess.
- `close(destination)` — Close a file or pipe when it is no longer needed.
- `fflush(destination)` — **gawk/recent POSIX:** flush an output buffer.

### Aligned table

```awk title="aligned-report.awk"
BEGIN {
    printf "%-20s %8s %12s\n", "Product", "Qty.", "Total"
    printf "%-20s %8s %12s\n", "--------------------", "--------", "------------"
}
{
    total = $2 * $3
    printf "%-20.20s %8d %12.2f\n", $1, $2, total
    grand_total += total
}
END {
    printf "%41s\n", "------------"
    printf "%-29s %12.2f\n", "TOTAL", grand_total
}
```

## Miscellaneous recipes

*One-liners, portability, security, and debugging.*

!!! tip "Write durable automation"

    For maintainable automation, prefer programs stored in files, single quotes in the shell, variables passed with `-v`, and POSIX features unless you have deliberately chosen to depend on `gawk`.

### Essential one-liners

- `awk 'NF' file` — Remove blank lines.
- `awk '!seen[$0]++' file` — Remove duplicate lines while preserving order.
- `awk '{ sum += $1 } END { print sum }'` — Sum the first column.
- `awk 'END { print NR }' file` — Count records.
- `awk '{ print NF, $0 }' file` — Prefix every line with its field count.
- `awk 'length > max { max=length; line=$0 } END{print line}'` — Find the longest line.

### Reformatting and selecting

- `awk -F, -v OFS=';' '{$1=$1; print}'` — Change the field separator.
- `awk '{ print $NF }'` — Print the last field.
- `awk 'NR >= 10 && NR <= 20'` — Print a range of lines.
- `awk '$1 == max { print }' max=42` — Assign a variable in the invocation.
- `awk '{ for(i=NF;i;i--) printf "%s%s",$i,(i>1?OFS:ORS) }'` — Reverse the field order.

### Shell interaction and security

- `awk -v value="$variable" '...'` — Pass shell data without injecting it into the AWK program.
- `'AWK program'` — Use single quotes to protect `$`, `\`, and spaces from the shell.
- `system("cmd " data)` — Risky with external input; avoid building commands without escaping.
- `--` — Some implementations use this to mark the end of options; check portability.
- `/dev/stderr` — Common but not POSIX; in `gawk`, use `print ... > "/dev/stderr"`.

### Portability and performance

- `LC_ALL=C` — Produce faster, more predictable character-class, sorting, and numeric behavior.
- `gawk --lint --posix -f script.awk` — Detect extensions while testing portability.
- `next` — Avoid unnecessary work in later rules.
- `close()` — Avoid exhausting open files and processes.
- `sub()` before `gsub()` — Prefer `sub()` when only the first match needs replacement.
- `literal regex` — Prefer a literal when the same dynamic regular expression would otherwise be rebuilt for every record.

### Debugging and diagnostics

```awk title="debugging-recipes.awk"
# Trace to stderr on gawk and typical Unix systems
print "DEBUG NR=" NR ", NF=" NF > "/dev/stderr"

# Display fields with unambiguous delimiters
for (i = 1; i <= NF; i++)
    printf "[$%d]=<%s>\n", i, $i > "/dev/stderr"

# Check syntax and warnings
gawk --lint -f program.awk </dev/null

# Create an execution profile with gawk
gawk --profile -f program.awk data
```

## Further reading

[Read the GNU AWK manual](https://www.gnu.org/software/gawk/manual/gawk.html){ .md-button .md-button--primary }
[Return to the dashboard](https://greivinvenegas.com/){ .md-button }

[^gawk]: See the [GNU AWK User's Guide](https://www.gnu.org/software/gawk/manual/gawk.html) for extension details, edge cases, and implementation-specific behavior.

*[AWK]: A pattern-scanning and text-processing language
*[ERE]: Extended Regular Expression
*[GNU]: GNU's Not Unix
*[I/O]: Input/output
*[POSIX]: Portable Operating System Interface
