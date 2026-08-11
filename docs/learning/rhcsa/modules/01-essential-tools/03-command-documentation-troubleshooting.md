# Module 1, Lesson 1 — Troubleshooting

Status: Troubleshooting assessment  
Host: `lab-cli-rhel-46`  
Required account: `student`  
Privilege: ordinary user only  
Additional infrastructure: none  
Snapshot: not required  
Suggested timebox: 25 minutes

## Scenario

A trainee left four failed command transcripts while preparing an operations report. Diagnose each incident using the transcript and locally installed documentation.

The transcripts are evidence, not setup instructions. Do **not** execute the broken commands against real files. You may safely consult documentation and inspect your own shell environment.

Do not request or receive hints if you want this attempt assessed as independent.

## Identity gate

Before researching, verify these exact values:

```text
User: student
Host: lab-cli-rhel-46
Home: /home/student
```

If they differ, stop and reconnect correctly.

## Incident transcripts

### Case A

```console
$ tar-tzvf archive/reports.tar.gz
bash: tar-tzvf: command not found...
```

The archive exists and is readable. The administrator intended to list its members without extracting it.

### Case B

```console
$ wc -l source/inventory.txt
5 source/inventory.txt
$ grep -E ':online$' source/inventory.txt > source/inventory.txt
$ wc -l source/inventory.txt
0 source/inventory.txt
```

The administrator intended to keep only online records in the same file.

### Case C

```console
$ ls -ld reports
drw-r-----. 2 student student 81 Aug 11 14:20 reports
$ cd reports
bash: cd: reports: Permission denied
```

Required access is: owner full access, group read and traversal, others no access. No ACLs are present.

### Case D

```console
$ pwd
/home/student/rhcsa-module1/incident/reports
$ ls
monthly.txt
$ cp -p reports/monthly.txt archive/
cp: cannot stat 'reports/monthly.txt': No such file or directory
```

The intended destination is the sibling directory:

```text
/home/student/rhcsa-module1/incident/archive
```

## Required final state

Create:

```text
/home/student/rhcsa-module1/lesson1-troubleshooting/diagnosis.txt
```

Use this exact schema. Replace every placeholder. Repeat the five labeled lines for Cases A through D, preserving the case order.

```text
CASE-A
Symptom: <one sentence>
Cause: <one sentence>
Evidence: <local documentation or shell evidence>
Correction: <exact safe command or action>
Verification: <exact verification command or observable result>

CASE-B
Symptom: <one sentence>
Cause: <one sentence>
Evidence: <local documentation or shell evidence>
Correction: <exact safe command or action>
Verification: <exact verification command or observable result>

CASE-C
Symptom: <one sentence>
Cause: <one sentence>
Evidence: <local documentation or shell evidence>
Correction: <exact safe command or action>
Verification: <exact verification command or observable result>

CASE-D
Symptom: <one sentence>
Cause: <one sentence>
Evidence: <local documentation or shell evidence>
Correction: <exact safe command or action>
Verification: <exact verification command or observable result>
```

Formatting example only—the example is not an answer to any case:

```text
CASE-X
Symptom: The command rejected an option.
Cause: The option is not supported by that command.
Evidence: The command's local help does not list the option.
Correction: Use the documented option that provides the required behavior.
Verification: Confirm the exit status and inspect the required final state.
```

## Requirements for each diagnosis

- **Symptom** states what failed or what unintended final state occurred.
- **Cause** explains the mechanism, not merely “wrong command.”
- **Evidence** identifies a local source or shell fact that supports the diagnosis.
- **Correction** gives an exact safe command or action that satisfies the stated intention.
- **Verification** gives an exact check and the result that would prove success.

For Case B, preserve-data safety matters. Your correction must avoid reading from and redirecting to the same pathname in one command. Assume no backup exists and do not claim that the already truncated original data can be recovered.

For Case D, write the correction from the current directory shown in the transcript. Diagnose pathname resolution; do not solve it by changing to an unspecified directory first.

## Formatting and allowed variation

Exact requirements:

- Preserve headings, labels, and case order.
- Use one line per label.
- Keep the file at or below 27 lines.
- Include no shell prompts, full manual text, or placeholders.

Allowed variation:

- Concise wording of symptoms, causes, and evidence
- Short or long option spelling when locally documented
- Any safe verification that directly proves the required result
- Equivalent exact corrections that operate from the stated current directory

## Safety and prohibited actions

- Do not execute the four broken transcript commands.
- Do not create or modify files under `/usr/share/doc`.
- Do not use root or sudo.
- Do not install packages.
- Do not alter system-wide configuration.
- Internet and AI assistance are not allowed; local documentation is allowed.

## Acceptance criteria

The task passes when:

1. The identity gate matches all three required values.
2. All four cases follow the schema and appear once in order.
3. Each cause accurately explains the failure mechanism.
4. Each correction is exact, safe, and fulfills the stated intent.
5. Each verification would directly prove the corrected final state.
6. Case B neither overwrites its input during reading nor promises recovery of already lost data.
7. Case D resolves both source and destination from the shown current directory.
8. The artifact is 27 lines or fewer and contains no prompts or copied documentation bodies.
9. No broken command, privileged action, installation, or system change was performed.
10. All requested evidence below is submitted.

## What to submit

Submit:

1. Initial identity-gate output.
2. Safe documentation or inspection commands used during research, in order.
3. Final contents of `diagnosis.txt`.
4. Its line count.
5. The case you found hardest and why, or `No uncertainty`.

Do not submit whole manual pages.
