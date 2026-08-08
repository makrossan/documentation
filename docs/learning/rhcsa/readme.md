# RHCSA RHEL 10 / EX200 Training Project

This workspace is the persistent record for a practical RHCSA course built around two RHEL 10 virtual machines.

## Current position

- Stage: baseline assessment
- Active assessment: [Initial practical diagnostic](assessments/00-initial-diagnostic.md)
- Module teaching has not started.
- All objectives begin at `⬜ Not Started`; the diagnostic evidence will establish the first ratings.

## Project files

- [CURRICULUM.md](CURRICULUM.md) — learning sequence and module gates
- [PROGRESS.md](PROGRESS.md) — authoritative objective checklist and demonstrated proficiency
- [LAB_STATE.md](LAB_STATE.md) — infrastructure, fictional enterprise design, and configuration ledger
- [SESSION_LOG.md](SESSION_LOG.md) — dated assessments, weak areas, and next actions
- [assessments/00-initial-diagnostic.md](assessments/00-initial-diagnostic.md) — first no-solution challenge

## Operating rules

1. Training follows Learn → Guided Lab → Independent Exam Task → Troubleshooting.
2. Independent tasks contain requirements, not commands. Hints escalate from concept to full solution only as needed.
3. A command that exits successfully is not proof of completion; final-state evidence is required.
4. Persistent configuration is verified after reboot whenever appropriate.
5. `🟩` is awarded only after an unaided performance. Old green objectives are retested through spaced repetition.
6. RHEL 10 methods take priority over obsolete RHEL 7–9 workflows.
7. No service or configuration is assumed to exist unless it is recorded in `LAB_STATE.md` or newly verified.
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

