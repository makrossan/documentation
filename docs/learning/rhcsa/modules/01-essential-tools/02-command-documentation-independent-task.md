# Module 1, Lesson 1 — Independent Task

Status: Independent assessment  
Host: `lab-cli-rhel-46`  
Required account: `student`  
Privilege: ordinary user only  
Additional infrastructure: none  
Snapshot: not required  
Suggested timebox: 25 minutes

## Scenario

Operations needs a compact local reference for several commands and system files. Create it using only documentation already available on the RHEL 10 system.

This is an independent task. Commands and answers are intentionally not supplied. You may use locally installed documentation; asking for a hint is allowed but changes the assessment from independent to assisted.

## Identity gate

Before creating or editing anything, verify the active identity, host, and home directory.

Required values:

```text
User: student
Host: lab-cli-rhel-46
Home: /home/student
```

If any value differs, stop, leave that session, and reconnect correctly. Do not copy the earlier `xvin` artifact into this task.

## Required final state

Create this new file:

```text
/home/student/rhcsa-module1/lesson1-independent/reference.txt
```

The file must use the exact headings and labels below. Replace every `<value>` placeholder; no angle-bracket placeholders may remain.

```text
IDENTITY
User: <value>
Host: <value>
Home: <value>

DATE
Option: <value>
Meaning: <one sentence>
Sample: <one observed output line>
Source: <local documentation source>

GREP
Option: <value>
Meaning: <one sentence>
Source: <local documentation source>

GROUP-FORMAT
Manual page: <page name and section>
Fields: <field names in colon-separated order>
Source: <local documentation source>

PACKAGE-DOC
Path: <absolute path>
Purpose: <one sentence>

COMMAND-TYPES
cd: <type>
cat: <type and resolved path when applicable>

COMMAND-ANATOMY
Invocation: cp -p alpha.txt beta.txt
Command: <token>
Option: <token>
Source operand: <token>
Destination operand: <token>
```

## Facts to research

Use local documentation to determine:

1. **DATE** — the `date` option that prints an RFC 3339 timestamp with seconds precision. Run it once and record one output line.
2. **GREP** — the `grep` option that prefixes each selected line with its input line number.
3. **GROUP-FORMAT** — the manual page section for the local group-account file and its field names in order.
4. **PACKAGE-DOC** — use `/usr/share/doc/coreutils-common/ABOUT-NLS`. Record that exact path and summarize the file's purpose in one sentence based on its contents.
5. **COMMAND-TYPES** — determine how the current shell resolves `cd` and `cat`. Record the type for both and the resolved path for `cat` if it is an executable.
6. **COMMAND-ANATOMY** — classify the four non-whitespace tokens in the supplied invocation. Do not run it; the named files do not need to exist.

## Formatting rules

Exact requirements:

- Preserve the headings, their order, and the labels shown in the schema.
- Use one line per label.
- Keep the file at or below 35 lines.
- Record answers only—no shell prompts, command transcript, copied manual paragraphs, or error dialogs in the file.
- `PACKAGE-DOC` must use the specified absolute path.

Allowed variation:

- Capitalization in explanatory sentences
- Equivalent short or long option spelling when local documentation proves it
- Normal variation in the observed timestamp
- Concise wording of meanings and purpose

## Safety and prohibited actions

- Do not use root or sudo.
- Do not install `info` or any other package.
- Do not alter system-wide files or configuration.
- Do not reuse or copy the previous guided-lab reference.
- Internet and AI assistance are not allowed; installed local documentation is allowed.

## Acceptance criteria

The task passes when all of the following are true:

1. Identity values match the required account, host, and home.
2. The file exists at the exact required path.
3. All seven sections appear once and in order.
4. Every placeholder is replaced and every researched answer is correct.
5. The timestamp is actual observed output, not placeholder text.
6. The file is 35 lines or fewer and contains no prompts or copied documentation bodies.
7. No privileged or system-changing action was taken.
8. The submitted evidence includes everything listed below.

## What to submit

Submit:

1. Commands used, in order, including the initial identity gate.
2. Final contents of `reference.txt`.
3. Its line count.
4. A short note identifying your hardest lookup or stating `No uncertainty`.

Do not submit whole manual pages.

## Attempt 1 review — 2026-08-11

Result: 7 of 8 acceptance criteria passed.

Accepted:

- Correct identity, host, and home
- Exact required file path
- All seven sections in order
- Correct date option and observed timestamp
- Correct grep option
- Correct group fields
- Accurate ABOUT-NLS purpose
- Correct command types and command anatomy
- Exactly 35 lines with no prompts or documentation dumps
- Complete evidence and no privileged changes

Two lines require correction:

1. **DATE Source** — the source must name documentation actually shown in the submitted command history. The transcript shows `date --help`, not a `man date` lookup. Either record the source actually used or supply the omitted lookup evidence.
2. **GROUP-FORMAT Manual page** — `Section 5` supplies only half of the requested value. Record both the page name and its section, based on the manual page you opened.

Do not change any other answer. Resubmit the DATE section, GROUP-FORMAT section, and final line count.

## Final result — 2026-08-11

Passed after targeted feedback.

- DATE source corrected to `date --help`.
- GROUP-FORMAT corrected to identify `group(5)`.
- The repeated label in `Manual page: Manual page: group(5)` is a minor presentation typo and does not invalidate the technically correct value.
- The artifact retains the previously verified 35-line structure.

The associated objectives remain `🟦 Can Perform With Help`. A later unaided retest is required for green, and practical `info` use remains pending because the command is not installed.
