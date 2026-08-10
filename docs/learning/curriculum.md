# Curriculum

The sequence is cumulative. Later work deliberately reuses earlier users, groups, directories, services, storage, and security controls.

## Stage 0 — Baseline diagnostic

Assess basic shell use, file manipulation, redirection, text filtering, links, permissions, archives, documentation, SSH, and verification. The result determines whether Module 1 is taught normally or accelerated.

Gate: submit commands used and final-state evidence from the diagnostic. No green ratings are assigned without unaided evidence.

## Module 1 — Essential command-line tools

- Correct command syntax and shell navigation
- Create, edit, copy, move, and remove files and directories
- Standard input, output, error redirection, and pipelines
- `grep` and regular expressions
- Hard and symbolic links
- Archives and gzip/bzip2 compression
- Standard `ugo/rwx` permissions
- `man`, `info`, `--help`, and `/usr/share/doc`
- Local logins, user switching, SSH, and secure file transfer fundamentals

Enterprise result: a controlled working area containing reports, links, and backups that can be inspected and transferred between servers.

## Module 2 — Users, groups, permissions, and privilege

- Local account lifecycle and password aging
- Groups and supplementary membership
- Default permissions and `umask`
- SGID collaboration directories, sticky bit, and ACLs
- Diagnosing permission failures
- Privileged access with RHEL 10-supported sudo configuration

Enterprise result: `admins`, `developers`, and `operations` teams collaborate safely under `/srv/projects` and `/srv/backups`.

## Module 3 — Software and repositories

- Inspect and configure RPM repositories
- Install, update, query, verify, and remove RPM packages
- Use Red Hat CDN and local/remote package sources
- Configure Flatpak remotes and manage Flatpak applications
- Diagnose repository and package problems

Enterprise result: documented software sources and a small approved package baseline.

## Module 4 — Processes, services, logs, and performance

- Find CPU- and memory-intensive processes and stop them safely
- Adjust process scheduling
- Manage and enable systemd services
- Locate and interpret logs and the journal
- Configure persistent system journals
- Select and verify TuneD profiles

Enterprise result: a managed service with persistent logs and an appropriate performance profile.

## Module 5 — Networking and remote administration

- Configure persistent IPv4 and IPv6 networking with NetworkManager
- Configure hostname resolution
- Ensure network services start at boot
- SSH and key-based authentication
- SCP/SFTP and remote administration
- Restrict access with firewalld
- Diagnose connectivity, listeners, routes, name resolution, and firewall failures

Enterprise result: reliable administration between the two lab servers using names and SSH keys with deliberately limited network exposure.

## Module 6 — GPT partitions, filesystems, mounts, and swap

- Safely identify disposable disks
- Create and remove GPT partitions
- Create and use VFAT, ext4, and XFS filesystems
- Mount by UUID or label and validate `/etc/fstab`
- Add partitions, filesystems, and swap non-destructively
- Diagnose mount and permission failures

Enterprise result: persistent data, interchange, archive, and swap resources on disposable storage.

Snapshot gate: obtain a fresh Proxmox snapshot before the first destructive storage lab. Never select the OS disk.

## Module 7 — LVM lifecycle

- Create and remove physical volumes
- Create and extend volume groups
- Create, delete, and extend logical volumes
- Grow supported filesystems correctly
- Verify LVM and persistent mounts before and after reboot
- Diagnose LVM/storage problems

Enterprise result: `vgdata` supplies expandable storage for applications, projects, and backups.

Snapshot gate: obtain a fresh Proxmox snapshot before destructive or fault-injection work.

## Module 8 — NFS and AutoFS

- Prepare an NFS service on the secondary server
- Apply permissions, SELinux, service, and firewall requirements
- Mount NFS manually and persistently
- Configure and diagnose AutoFS

Enterprise result: the secondary server publishes team data; the primary consumes fixed and on-demand mounts.

## Module 9 — SELinux

- Enforcing and permissive modes
- File and process contexts
- Restore default contexts
- Persistent custom file context rules
- Port labels
- Boolean settings
- Use logs and analysis tools to diagnose denials

Enterprise result: services operate under enforcing SELinux without broad or temporary workarounds.

## Module 10 — Shell scripting

- Positional input
- Command substitution and processing command output
- Conditions with `if`, `test`, and `[]`
- `for` loops over files and arguments
- Exit status, safe quoting, executable permissions, and verification

Enterprise result: small scripts audit users, storage, services, and backups created in earlier modules.

## Module 11 — Task scheduling

- One-time work with `at`
- Repeating work with cron
- Native scheduling with systemd timer units
- Service identities, paths, logging, missed runs, enablement, and verification

Enterprise result: reports and backup checks run predictably and leave inspectable evidence.

## Module 12 — Boot, targets, recovery, and bootloader

- Normal boot, reboot, and shutdown
- Temporary and default systemd targets
- Interrupt boot to regain administrative access
- Modify and validate the RHEL 10 bootloader configuration
- Recover from broken boot-related configuration

Enterprise result: systems boot into the required target and can be recovered under exam conditions.

Snapshot gate: obtain a fresh Proxmox snapshot before boot interruption, bootloader modification, or deliberate boot failure.

## Module 13 — Integrated reviews and mock exams

- Mini exams follow major sections.
- Full mock exams mix requirements without commands or unsolicited hints.
- Every mock includes verification and persistence; later mocks include fault diagnosis.
- Grading separates correct, partial, incorrect, dangerous, and nonpersistent results.
- Weak objectives generate remediation labs and spaced-repetition retests.

Suggested checkpoints:

1. Mini exam A after Module 3
2. Mini exam B after Module 5
3. Mini exam C after Module 9
4. Mini exam D after Module 12
5. Full mock exams until all objectives are independently reproducible

