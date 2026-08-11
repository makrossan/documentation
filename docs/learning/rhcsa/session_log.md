# Session and Assessment Log

## 2026-08-08 — Project initialized

- Recorded the two-server RHEL 10/Proxmox infrastructure.
- Established the cumulative curriculum and all objective ratings at `⬜ Not Started`.
- Created the fictional enterprise design without assuming that any planned object already exists.
- Selected the initial practical diagnostic as the next action.
- No VM configuration was changed.

Next action: learner completes `assessments/00-initial-diagnostic.md` on the primary system and submits commands plus verification evidence. Grade the evidence, update `progress.md`, then choose the normal or accelerated Module 1 path.

## 2026-08-09 — Initial diagnostic graded

- Received a timed command transcript through Part D plus the attempted Part E transfer.
- Fully met 9 task requirements, partially met 4, left 4 incomplete or unverified, and encountered an infrastructure block on 2 remote-transfer requirements.
- Awarded independent ratings for redirection, text creation, file/directory operations, and hard/symbolic links.
- Marked shell syntax, grep/regular expressions, archives/compression, permissions, and documentation use as learning areas.
- Did not penalize the secondary transfer: SSH was reachable, but `student` does not exist on `lab-cli-rhel-47`.
- Selected the normal Module 1 pace. Demonstrated strengths can be accelerated, while identified gaps receive deliberate practice.

Next action: complete the focused correction round in `assessments/00-initial-diagnostic-result.md`. Do not redo Part E yet. After grading those corrections, begin Module 1.

## 2026-08-09 — Initial diagnostic correction, submission 1

- Demonstrated a successful remote login from the client machine to `10.11.11.46` as `student`; SSH advanced to independent.
- Removed the unrequested SGID bit and set `reports` to `0750`, which satisfies the stated owner/group/other mode requirement.
- Correctly created `archive/reports.tar.gz` with gzip and `archive/source.tar.bz2` with bzip2 through `tar`.
- Learner identified uncertainty about directory traversal; retain permissions at learning until the semantics are understood and retested.
- Archive rating remains learning because non-extracting member listings and unpack/uncompress behavior are not yet demonstrated.

Next action: finish exact report regeneration, line-based counting, both archive member listings, and `reports/documentation.txt`; submit concise verification. Part E remains deferred.

## 2026-08-09 — Initial diagnostic correction, submission 2

- Replaced the malformed count report with an exact final-field selection and a line count; numeric result is correct.
- Correctly listed both gzip and bzip2 tar archives without extracting them.
- Advanced archive/compression and permissions to `🟦 Can Perform With Help`; each needs a later unaided retest, and archives still need extraction practice.
- Documentation lookup selected `-h`, which controls human-readable sizes rather than appending a directory indicator; task remains incomplete.
- Production and offline outputs are correct, but their correction commands did not demonstrate exact field/end matching.
- Replacing `count.txt` removed the originally required login-name line; it must be restored after the count.

Next action: submit exact-field regeneration commands for production/offline, a final two-line count report containing the count and actual login name, and the corrected documentation record. Then close the diagnostic and begin Module 1.

## 2026-08-09 — Initial diagnostic correction, submission 3

- Restored `count.txt` to the required two-line final state: numeric count followed by `student`.
- Located `ls -p` / `--indicator-style=slash`, which is a valid directory-specific indicator option.
- The documentation file still needs to name `man ls` as the source.
- Production was rebuilt with plain substring matching and append redirection; exact second-field matching and replace semantics remain unproven.
- No corrected creation command was supplied for the offline report.

Next action: use the supplied full regex syntax to rebuild production/offline safely, add the documentation source, and show the three final files. These items will be rated as completed with help rather than independent.

## 2026-08-09 — Initial diagnostic closed

- Verified correct final contents for the production and offline reports after full regex syntax was supplied.
- Accepted `ls -p` / `--indicator-style=slash` as the directory-indicator answer and the included `ls(1)` manual content as evidence of the local source.
- The documentation file was much larger than required; concise evidence extraction becomes the first Module 1 practice topic.
- Final diagnostic ratings: 5 independent, 5 with help, 53 not yet started.
- Began Module 1, Lesson 1: command anatomy and local documentation.

Next action: learner completes the Lesson 1 guided lab in `modules/01-essential-tools/01-command-anatomy-and-documentation.md` on the primary server.

## 2026-08-10 — Module 1, Lesson 1 guided lab reviewed

- Correctly found the required `mkdir`, `cp`, and `ls` options using local help and man pages.
- Correctly opened `passwd(5)` and found the seven fields in order. Only the field names and manual section were required; the detailed descriptions were not.
- Confirmed that `info` is absent and declined the installation prompt as instructed.
- Found `/usr/share/doc/coreutils-common/TODO` and correctly identified `ls` as an alias and `ssh` as `/usr/bin/ssh`.
- The reference copied long documentation bodies and shell prompts rather than recording concise answers, despite the stated constraint. Documentation-use remains `🟦`.

Next action: replace `command-reference.txt` with the concise version in the guided-lab review, display it, and report its line count. No additional research is required.

## 2026-08-10 — Module 1, Lesson 1 correction attempt 1

- The submitted reference still contained the previously copied `passwd(5)` body and shell prompts, so it did not satisfy the concise-reference requirement.
- `README` is a valid coreutils documentation filename and is accepted in place of `TODO`.
- The SSH command-type line was replaced by an unrelated Sites skill reference; the already verified answer remains executable `/usr/bin/ssh`.
- The requested line count was not supplied.

Next action: delete the entire contents of `command-reference.txt`, paste only the concise reference block from the lesson review, then submit `cat` and `wc -l` output.

## 2026-08-10 — Module 1, Lesson 1 guided lab completed

- Verified the corrected 30-line `command-reference.txt`; all seven sections now contain the required concise findings.
- Accepted the guided lab as complete. Documentation use remains `🟦` because the final format was completed from a supplied template.
- Learner correctly identified that the original prompt required overly specific presentation without providing a template or example.
- Updated the permanent teaching rules: guided artifacts receive an explicit schema/example when format matters, and grading cannot introduce unstated criteria after submission.

Next action: present the Lesson 1 independent task with command-free but explicit requirements, deliverable schema, allowed variation, and acceptance criteria.

## 2026-08-10 — Training account clarified

- Learner confirmed that Module 1 Lesson 1 was accidentally performed after SSH login as `xvin`, explaining why `~` resolved to `/home/xvin`.
- The work remains valid because it used an ordinary account and required no account-specific configuration.
- Future exercises standardize on `student`; each lab will begin with identity and hostname verification to prevent work in the wrong home directory.

## 2026-08-10 — Module 1, Lesson 1 independent task issued

- Issued a command-free independent assessment covering identity verification, command anatomy, `--help`, man-page sections, `/usr/share/doc`, command types, concise evidence, and final verification.
- Added an exact deliverable schema, allowed variation, omissions, and acceptance criteria before the attempt.
- No snapshot, root access, package installation, or additional infrastructure is required.

Next action: learner completes `modules/01-essential-tools/02-command-documentation-independent-task.md` as `student` and submits the commands, final artifact, line count, and uncertainty note.

## 2026-08-11 — Module 1, Lesson 1 independent attempt 1

- Passed the identity gate as `student` on `lab-cli-rhel-46` with `/home/student`.
- Produced the required artifact at the correct path with all seven sections, exactly 35 lines, concise content, and complete submission evidence.
- Correctly researched the RFC 3339 seconds option, grep line-number option, group fields, ABOUT-NLS purpose, command types, and command-token anatomy.
- DATE recorded `man date` as its source, but the submitted command history shows `date --help` and no `man date` lookup.
- GROUP-FORMAT recorded only `Section 5`, while the published schema explicitly required the page name and section.
- Several relative-path mistakes and an accidental shell escape from `vi` were self-corrected without privileged changes.

Result: 7 of 8 acceptance criteria pass. Ratings remain `🟦` pending the two-line correction and a later `info` exercise.

Next action: correct only the DATE source and GROUP-FORMAT manual-page line, then submit the two sections and final line count.

## 2026-08-11 — Module 1, Lesson 1 independent task completed

- DATE now records the documentation source actually shown in the command history: `date --help`.
- GROUP-FORMAT now identifies the page and section as `group(5)`.
- The value was submitted as `Manual page: Manual page: group(5)`; the duplicated label is treated as a minor presentation typo, not another failed attempt.
- The previously verified 35-line structure is unchanged.

Result: independent task passed after targeted feedback. Command syntax and documentation objectives remain `🟦` because corrections were required; both are scheduled for a later unaided retest, and `info` still needs hands-on use after it becomes available.

Next action: begin the Lesson 1 troubleshooting phase.

## 2026-08-11 — Module 1, Lesson 1 troubleshooting issued

- Issued four safe incident cases covering shell tokenization, destructive redirection order, directory traversal permissions, and relative-path resolution.
- The learner analyzes static transcripts and must not execute the broken commands against real files.
- Added an exact diagnosis schema, a non-answer formatting example, allowed variation, safety limits, and acceptance criteria.
- No snapshot, root access, package installation, or additional infrastructure is required.

Next action: learner completes `modules/01-essential-tools/03-command-documentation-troubleshooting.md` and submits research commands, `diagnosis.txt`, its line count, and an uncertainty note.
