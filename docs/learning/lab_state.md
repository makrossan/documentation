# Lab Environment and State Ledger

This file distinguishes verified state from planned state. A service is not treated as configured merely because it appears in the design.

## Available infrastructure

| Role | Current hostname | Address | OS | Intended use |
|---|---|---:|---|---|
| Primary | `lab-cli-rhel-46` | `10.11.11.46` | RHEL 10 | Most RHCSA administration and all local storage labs |
| Secondary | `lab-cli-rhel-47` | `10.11.11.47` | RHEL 10 | SSH, transfer, NFS, AutoFS peer, and client/server exercises |

Verified from infrastructure description:

- Both VMs are registered with Red Hat and can access RHEL repositories.
- Both run on Proxmox and may be rebooted freely.
- CPU, RAM, NICs, and virtual disks can be added when a lab requires them.

Still to discover rather than assume:

- Prefix length, gateway, DNS servers, active NetworkManager connection names, and NIC names
- Administrative login account names and the secondary server's available ordinary accounts
- Current service, firewall, SELinux, repository, disk, and filesystem state
- Whether the two systems already resolve one another by name

Observed during the 2026-08-09 diagnostic:

- Ordinary account `student` exists and was used on `lab-cli-rhel-46`.
- SSH on `10.11.11.47` is reachable and presents a host key and authentication prompt.
- The operator confirmed that `student` does not exist on `lab-cli-rhel-47`; password authentication therefore failed and SCP could not complete.
- No SSH, firewall, or account configuration was changed to work around the missing secondary account.

## Fictional enterprise design

Organization: Example Operations Lab  
DNS namespace used in exercises: `lab.example.com`

Planned host aliases, added only during the appropriate networking exercise:

| Alias | Address | Purpose |
|---|---:|---|
| `server1.lab.example.com` | `10.11.11.46` | Primary administration node |
| `server2.lab.example.com` | `10.11.11.47` | Remote services node |

The current Proxmox hostnames remain the infrastructure identifiers unless a later hostname exercise explicitly changes them.

Planned reusable identities:

- Groups: `admins`, `developers`, `operations`
- Individual users: selected and created during Module 2
- Privilege policy: developed during Module 2; no sudo policy is currently assumed

Planned reusable paths:

- `/srv/projects` — developer collaboration
- `/srv/backups` — operations-owned backup data
- `/srv/appdata` — application logical volume
- `/mnt/data` — persistent local data mount
- `/mnt/shared` — fixed NFS client mount
- `/rhome` — AutoFS-managed remote content

Nothing in the planned lists is recorded as present until a lab creates it and verification is logged below.

## Resource plan

No additional infrastructure is needed for the initial diagnostic or Modules 1–5.

Before Module 6 begins, add these disposable virtual disks to `lab-cli-rhel-46`:

1. One 12 GiB disk for GPT, VFAT, ext4, XFS, mount, and swap exercises.
2. One 16 GiB disk for the initial LVM physical volume and `vgdata`.
3. One 8 GiB disk for volume-group extension and destructive recovery practice.

Disk device names such as `/dev/sdb` are never assumed. Each disk must be identified from its observed size and device metadata after attachment. The OS disk must be explicitly identified and excluded before any write.

No extra disk is initially required on `lab-cli-rhel-47`; its NFS export can use a deliberately created, modest directory on its existing filesystem. If free-space verification shows that is inappropriate, a separate 8 GiB disposable disk will be requested before the NFS lab.

No additional NIC, CPU, or RAM is currently required. Network changes will use the existing NICs unless a fault-injection lab explicitly calls for another one.

## Snapshot and recovery policy

A fresh Proxmox snapshot is required immediately before:

- First partitioning/filesystem lab and later destructive storage fault injection
- Risky `/etc/fstab` exercises
- Network configuration changes that may remove remote access
- Bootloader edits, boot interruption, or deliberate boot failures
- Any exercise whose rollback would otherwise require rebuilding a VM

The learner confirms the snapshot exists before the exercise begins. Snapshots supplement verification; they do not replace diagnosis or persistent configuration.

## Configuration ledger

| Date | Host | Change | Verification | Persistence checked |
|---|---|---|---|---|
| 2026-08-09 | `lab-cli-rhel-46` | Created `~/rhcsa-diagnostic` as `student`; no system-wide configuration | Submitted directory, content, link, and permission evidence | Not applicable |

