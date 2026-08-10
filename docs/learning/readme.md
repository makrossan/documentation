# RHCSA RHEL 10 / EX200 Training Project

This workspace is the persistent record for a practical RHCSA course built around two RHEL 10 virtual machines.

## Current position

- Stage: Module 1 — Essential command-line tools
- Diagnostic status: closed; [final result](assessments/00-initial-diagnostic-result.md)
- Active lesson: [Command anatomy and local documentation](modules/01-essential-tools/01-command-anatomy-and-documentation.md)
- Next action: complete the Lesson 1 guided lab on `lab-cli-rhel-46`.
- Module 1 uses the normal pace, with faster treatment of independently demonstrated strengths.

## Project files

- [curriculum.md](curriculum.md) — learning sequence and module gates
- [progress.md](progress.md) — authoritative objective checklist and demonstrated proficiency
- [lab_state.md](lab_state.md) — infrastructure, fictional enterprise design, and configuration ledger
- [session_log.md](session_log.md) — dated assessments, weak areas, and next actions
- [assessments/00-initial-diagnostic.md](assessments/00-initial-diagnostic.md) — first no-solution challenge
- [assessments/00-initial-diagnostic-result.md](assessments/00-initial-diagnostic-result.md) — grading and targeted correction round
- [modules/01-essential-tools/01-command-anatomy-and-documentation.md](modules/01-essential-tools/01-command-anatomy-and-documentation.md) — active Module 1 lesson

## Operating rules

1. Training follows Learn → Guided Lab → Independent Exam Task → Troubleshooting.
2. Independent tasks contain requirements, not commands. Hints escalate from concept to full solution only as needed.
3. A command that exits successfully is not proof of completion; final-state evidence is required.
4. Persistent configuration is verified after reboot whenever appropriate.
5. `🟩` is awarded only after an unaided performance. Old green objectives are retested through spaced repetition.
6. RHEL 10 methods take priority over obsolete RHEL 7–9 workflows.
7. No service or configuration is assumed to exist unless it is recorded in `lab_state.md` or newly verified.
8. Before risky boot, storage, filesystem, or networking work, pause for a Proxmox snapshot.
9. In troubleshooting exercises, the fault and repair remain undisclosed until the learner has investigated.
10. Disposable virtual disks are used for storage work; the operating-system disk is kept out of destructive exercises.

## Assessment scale

| Level | Meaning |
|---|---|
| ⬜ Not Started | No usable evidence yet |
| 🟨 Learning | Concept or workflow is being learned |
| 🟦 Can Perform With Help | Completed with hints, references to supplied syntax, or correction |
| 🟩 Can Perform Independently | Completed unaided and verified, including persistence where applicable |

