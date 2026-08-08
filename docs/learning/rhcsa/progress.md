# RHCSA RHEL 10 Objective Progress

Authoritative scale: `⬜ Not Started` · `🟨 Learning` · `🟦 Can Perform With Help` · `🟩 Can Perform Independently`

An objective reaches green only after an unaided, verified performance. For persistent configuration, evidence includes a reboot check when practical. The evidence column should point to a dated entry in `SESSION_LOG.md`.

## Understand and use essential tools

| Objective | Level | Last assessed | Evidence / next action |
|---|---:|---|---|
| Access a shell prompt and issue commands with correct syntax | ⬜ | — | Initial diagnostic |
| Use input-output redirection (`>`, `>>`, `|`, `2>`, etc.) | ⬜ | — | Initial diagnostic |
| Use grep and regular expressions to analyze text | ⬜ | — | Initial diagnostic |
| Access remote systems using SSH | ⬜ | — | Initial diagnostic |
| Log in and switch users in multi-user targets | ⬜ | — | Module 1/2 |
| Archive, compress, unpack, and uncompress files using tar, gzip, and bzip2 | ⬜ | — | Initial diagnostic |
| Create and edit text files | ⬜ | — | Initial diagnostic |
| Create, delete, copy, and move files and directories | ⬜ | — | Initial diagnostic |
| Create hard and soft links | ⬜ | — | Initial diagnostic |
| List, set, and change standard ugo/rwx permissions | ⬜ | — | Initial diagnostic |
| Locate, read, and use `man`, `info`, and `/usr/share/doc` | ⬜ | — | Initial diagnostic |

## Manage software

| Objective | Level | Last assessed | Evidence / next action |
|---|---:|---|---|
| Configure access to RPM repositories | ⬜ | — | Module 3 |
| Install and remove RPM software packages | ⬜ | — | Module 3 |
| Configure access to Flatpak repositories | ⬜ | — | Module 3 |
| Install and remove Flatpak software packages | ⬜ | — | Module 3 |

## Create simple shell scripts

| Objective | Level | Last assessed | Evidence / next action |
|---|---:|---|---|
| Conditionally execute code using `if`, `test`, `[]`, etc. | ⬜ | — | Module 10 |
| Use looping constructs such as `for` to process files and command-line input | ⬜ | — | Module 10 |
| Process script inputs using `$1`, `$2`, etc. | ⬜ | — | Module 10 |
| Process output of shell commands within a script | ⬜ | — | Module 10 |

## Operate running systems

| Objective | Level | Last assessed | Evidence / next action |
|---|---:|---|---|
| Boot, reboot, and shut down a system normally | ⬜ | — | Module 12 |
| Boot systems into different targets manually | ⬜ | — | Module 12 |
| Interrupt the boot process to gain access to a system | ⬜ | — | Module 12 |
| Identify CPU/memory-intensive processes and kill processes | ⬜ | — | Module 4 |
| Adjust process scheduling | ⬜ | — | Module 4 |
| Manage tuning profiles | ⬜ | — | Module 4 |
| Locate and interpret system log files and journals | ⬜ | — | Module 4 |
| Preserve system journals | ⬜ | — | Module 4 |
| Start, stop, and check the status of network services | ⬜ | — | Module 4/5 |
| Securely transfer files between systems | ⬜ | — | Initial diagnostic / Module 5 |

## Configure local storage

| Objective | Level | Last assessed | Evidence / next action |
|---|---:|---|---|
| List, create, and delete partitions on GPT disks | ⬜ | — | Module 6 |
| Create and remove physical volumes | ⬜ | — | Module 7 |
| Assign physical volumes to volume groups | ⬜ | — | Module 7 |
| Create and delete logical volumes | ⬜ | — | Module 7 |
| Configure systems to mount filesystems at boot by UUID or label | ⬜ | — | Module 6/7 |
| Add new partitions, logical volumes, and swap non-destructively | ⬜ | — | Module 6/7 |
| Create and configure filesystems | ⬜ | — | Module 6 |
| Create, mount, unmount, and use VFAT, ext4, and XFS filesystems | ⬜ | — | Module 6 |
| Mount and unmount network filesystems using NFS | ⬜ | — | Module 8 |
| Configure AutoFS | ⬜ | — | Module 8 |
| Extend existing logical volumes | ⬜ | — | Module 7 |
| Diagnose and correct file permission problems | ⬜ | — | Module 2 and cumulative labs |

## Deploy, configure, and maintain systems

| Objective | Level | Last assessed | Evidence / next action |
|---|---:|---|---|
| Schedule tasks using `at`, cron, and systemd timer units | ⬜ | — | Module 11 |
| Start and stop services and configure services to start automatically at boot | ⬜ | — | Module 4 |
| Configure systems to boot into a specific target automatically | ⬜ | — | Module 12 |
| Configure time service clients | ⬜ | — | Module 5 |
| Install and update packages from Red Hat CDN, remote repositories, or local files | ⬜ | — | Module 3 |
| Modify the system bootloader | ⬜ | — | Module 12 |

## Manage basic networking

| Objective | Level | Last assessed | Evidence / next action |
|---|---:|---|---|
| Configure IPv4 and IPv6 addresses | ⬜ | — | Module 5 |
| Configure hostname resolution | ⬜ | — | Module 5 |
| Configure network services to start automatically at boot | ⬜ | — | Module 5 |
| Restrict network access using firewalld and `firewall-cmd` | ⬜ | — | Module 5 and cumulative labs |

## Manage users and groups

| Objective | Level | Last assessed | Evidence / next action |
|---|---:|---|---|
| Create, delete, and modify local user accounts | ⬜ | — | Module 2 |
| Change passwords and adjust password aging for local accounts | ⬜ | — | Module 2 |
| Create, delete, and modify local groups and group memberships | ⬜ | — | Module 2 |
| Configure privileged access | ⬜ | — | Module 2 |

## Manage security

| Objective | Level | Last assessed | Evidence / next action |
|---|---:|---|---|
| Configure firewall settings using firewalld | ⬜ | — | Module 5 and cumulative labs |
| Manage default file permissions | ⬜ | — | Module 2 |
| Configure key-based authentication for SSH | ⬜ | — | Module 5 |
| Set enforcing and permissive modes for SELinux | ⬜ | — | Module 9 |
| List and identify SELinux file and process contexts | ⬜ | — | Module 9 |
| Restore default file contexts | ⬜ | — | Module 9 |
| Manage SELinux port labels | ⬜ | — | Module 9 |
| Use Boolean settings to modify system SELinux settings | ⬜ | — | Module 9 |

## Current summary

| Level | Count |
|---|---:|
| ⬜ Not Started | 63 |
| 🟨 Learning | 0 |
| 🟦 Can Perform With Help | 0 |
| 🟩 Can Perform Independently | 0 |

Weakest areas: not yet measured. First update follows the initial diagnostic.

