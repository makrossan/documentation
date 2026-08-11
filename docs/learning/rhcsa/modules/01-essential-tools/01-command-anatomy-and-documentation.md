# Module 1, Lesson 1 — Command Anatomy and Local Documentation

Status: Learn + Guided Lab complete; Independent Task next  
Host: `lab-cli-rhel-46`  
Privilege: ordinary `student` account  
Additional infrastructure: none  
Snapshot: not required

## Learning goals

By the end of this lesson, you should be able to:

1. Distinguish a command name, options, option arguments, and operands.
2. Read a command synopsis without typing its notation literally.
3. Choose among `--help`, `man`, `info`, and `/usr/share/doc`.
4. Search local documentation efficiently and record a concise answer.
5. Verify whether a name resolves to a standard command, alias, function, or other shell construct.

## 1. Command anatomy

Consider the successful archive inspection from the diagnostic:

```bash
tar -tzvf archive/reports.tar.gz
```

- `tar` is the command name.
- `-tzvf` is a bundle of short options.
- The `f` option tells `tar` that the next argument names the archive file.
- `archive/reports.tar.gz` is therefore the argument consumed by `f`.

Whitespace separates shell words. In this failed form:

```bash
tar-tzvf archive/reports.tar.gz
```

the shell searches for a command literally named `tar-tzvf`. It never gets as far as interpreting tar options.

Short options can often be bundled, but only when that command documents the behavior. An option that consumes an argument needs special attention. Long options are clearer when recall is uncertain:

```text
--list
--gzip
--verbose
--file=ARCHIVE
```

Do not assume every command accepts the same option style or operand order. The command's synopsis is authoritative.

## 2. Reading a synopsis

Documentation commonly uses this notation:

- `[ITEM]` — optional; do not type the brackets
- `ITEM...` — may be repeated
- `A | B` — choose an alternative
- uppercase words such as `FILE` — placeholders to replace, not literal text
- text without brackets — required

For example:

```text
command [OPTION]... SOURCE DEST
```

means options are optional and repeatable, while source and destination operands are required.

## 3. Choosing documentation

Use the smallest source that answers the question:

| Source | Best use |
|---|---|
| `command --help` | Fast syntax and option reminder |
| `man command` | Normal command reference, examples, files, and related pages |
| `man SECTION name` | Select a particular page, such as a command or file format |
| `info command` | Longer or more structured GNU documentation |
| `/usr/share/doc` | Package-specific notes, examples, licenses, and release material |

Useful `man` navigation:

- `/word` searches forward.
- `n` repeats the search forward.
- `N` repeats it backward.
- `q` exits.

The manual section matters. Section 1 normally describes user commands; section 5 normally describes file formats and configuration files. A command and a file can have the same page name, so select the section when needed.

If a command is unfamiliar, first find what the shell will actually run:

```bash
type ls
type ssh
```

Personal aliases are not portable to a fresh exam system. Know the underlying standard command.

## 4. Record the answer, not the entire manual

For the diagnostic lookup, concise evidence would be:

```text
Command: ls
Option: -p, --indicator-style=slash
Meaning: append / to directory names
Source: man ls
```

Copying a complete manual page makes the relevant fact harder to verify. An administrator normally records the decision, the exact option, and where it was confirmed.

## 5. Common mistakes to watch

- Gluing the command name and option into one shell word
- Confusing mode changes (`chmod`) with ownership changes (`chown`)
- Typing synopsis punctuation literally
- Assuming an option from one command works on another
- Searching a manual for a nearby concept rather than the required behavior
- Capturing too much output instead of concise evidence
- Forgetting that `$?` reports only the most recently completed command's status

## Guided lab — Build a local command reference

Scenario: Operations wants a compact reference that another administrator can use on a fresh RHEL 10 system. All answers must come from local documentation.

Create this file:

```text
~/rhcsa-module1/lesson1/command-reference.txt
```

Use the following exact section headings in it:

```text
MKDIR
CP
LS
PASSWD-FORMAT
INFO
PACKAGE-DOCS
COMMAND-TYPES
```

Complete the sections as follows:

1. **MKDIR** — Using `mkdir --help`, record the option that creates missing parent directories, its meaning, and the source.
2. **CP** — Using `man cp`, record one option that preserves file attributes and state exactly which attributes it preserves. Do not assume “everything”; use the wording supported by the manual.
3. **LS** — Using `man ls`, record the option that displays numeric user and group IDs in a long listing.
4. **PASSWD-FORMAT** — Open the file-format manual page for `passwd`. Record the manual section and the seven colon-separated fields in order. Do not copy the whole page.
5. **INFO** — Open the Info documentation for either `ls` or GNU coreutils. Record the exact Info topic you successfully opened and one fact found there that was not needed in the previous sections. If Info content is unavailable, record the exact failure instead of installing anything.
6. **PACKAGE-DOCS** — Inspect the locally available coreutils-related location under `/usr/share/doc`. Record one documentation filename found there. If none exists, record the path checked and exact result.
7. **COMMAND-TYPES** — Record what the shell reports for `ls` and `ssh`: executable, alias, function, builtin, or another type.

Why these steps matter:

- The first three practice choosing the right source and extracting one exact option.
- The passwd task teaches manual sections and configuration-file documentation.
- Info and `/usr/share/doc` cover sources that are often forgotten during troubleshooting.
- Command-type inspection prevents dependence on aliases that will not exist on a fresh exam system.

## Verification and submission

Submit:

1. The commands used, in order.
2. The contents of `command-reference.txt`.
3. A brief note naming the hardest lookup and why.

Do not include full manual pages. This is guided practice, so questions are allowed; the later independent task will remove the headings and documentation hints.

## Guided lab review — 2026-08-10

Your interpretation of `PASSWD-FORMAT` was correct: the requirement was the manual section and the seven field names in order. Their detailed descriptions were not requested.

Accepted findings:

- `mkdir -p` / `--parents` and its documented meaning
- `cp -p` as `--preserve=mode,ownership,timestamps`
- `ls -n` / `--numeric-uid-gid`
- The seven `passwd(5)` fields in the correct order
- Exact evidence that `info` is not installed, with installation declined
- The coreutils documentation file `TODO`
- `ls` is an alias; `ssh` resolves to `/usr/bin/ssh`

The technical lookups were good. The remaining issue is the lesson's main administrative habit: record the answer, not pages of source material or copied shell prompts.

### Targeted correction

No new research is needed. Replace `command-reference.txt` with a concise reference using this content:

```text
MKDIR
Option: -p, --parents
Meaning: create missing parent directories as needed
Source: mkdir --help

CP
Option: -p
Meaning: same as --preserve=mode,ownership,timestamps
Source: man cp

LS
Option: -n, --numeric-uid-gid
Meaning: use a long listing with numeric user and group IDs
Source: man ls

PASSWD-FORMAT
Manual section: 5
Fields: name:password:UID:GID:GECOS:directory:shell
Source: man 5 passwd

INFO
Status: unavailable; `info` command not found
Action: installation declined as instructed

PACKAGE-DOCS
File: /usr/share/doc/coreutils-common/TODO

COMMAND-TYPES
ls: alias for `ls -p --color=auto`
ssh: executable `/usr/bin/ssh`
```

Display the corrected file and its line count. Once verified, the guided lab is complete and Lesson 1 moves to an independent task.

### Correction attempt 1 — 2026-08-10

The file was edited but not replaced: the long `passwd(5)` body and copied shell prompts remained. `README` is accepted as the selected package-documentation filename. The Sites skill link is unrelated and is not a valid replacement for the verified SSH command type (`/usr/bin/ssh`).

When using `vi`, remove all old lines before inserting the concise block. From normal mode, `:%d` deletes every line; then enter insert mode, paste only the prepared block above, save, and quit. Verify with both `cat` and `wc -l`.

## Guided lab completed — 2026-08-10

The final reference contained the seven required sections and exactly 30 lines. The guided lab is complete.

Account note: the final artifact was created as `xvin` under `/home/xvin` after an unintended SSH login. It remains accepted. Future labs use `student` and begin by verifying the active identity and hostname.

Instructor correction: the first lab prompt described a compact reference but did not provide a sufficiently explicit schema or example, then treated the unstated formatting expectation as a grading requirement. That was not a valid measure of RHCSA ability. Future guided labs will state exact formatting only when it matters and will grade only against criteria supplied before the attempt.
