# Initial Practical Diagnostic

Purpose: measure current basic Linux ability before Module 1. This is an assessment, not a lesson.

Suggested timebox: 30–45 minutes. Accuracy and verification matter more than speed.

## Rules

- Work on `lab-cli-rhel-46` as a non-root user unless a task genuinely requires otherwise.
- You may use documentation installed on the RHEL system.
- Do not use web search, AI assistance, or a copied solution.
- Do not install packages or change system-wide configuration.
- If a required utility is not installed, capture the exact result and continue; do not install it for this assessment.
- Do not delete or overwrite unrelated files.
- This diagnostic needs no Proxmox snapshot and no additional infrastructure.
- If access to `lab-cli-rhel-47` is unavailable, record that fact and complete the rest; do not reconfigure SSH or the firewall yet.

## Scenario

Operations has asked you to build and transfer a small status bundle. Meet the requirements below without being given commands.

### Part A — Workspace and files

1. Connect to `lab-cli-rhel-46` remotely with SSH.
2. Under your home directory, create `rhcsa-diagnostic` with these subdirectories:
   - `source`
   - `reports`
   - `archive`
3. In `source`, create and edit `systems.txt` so it contains exactly these five lines:

   ```text
   server1:production:online
   server2:development:offline
   server3:production:offline
   client1:testing:online
   client2:production:online
   ```

4. Make a copy of this file in `archive` named `systems.original`.
5. Move the original `source/systems.txt` to `source/inventory.txt`.
6. Create an empty file named `source/ready.flag` without opening an editor.

### Part B — Redirection and text analysis

7. From `source/inventory.txt`, create `reports/production.txt` containing only records whose environment field is exactly `production`.
8. Create `reports/offline.txt` containing only records whose final field is exactly `offline`.
9. Create `reports/count.txt` containing only the number of records whose final field is `online`.
10. Run one deliberately invalid pathname listing. Save its error message in `reports/error.txt` without placing that error on the terminal and without mixing it into another report.
11. Add a line containing your current login name to the end of `reports/count.txt`; do not replace the existing count.

### Part C — Links and permissions

12. In `rhcsa-diagnostic`, create:
    - a symbolic link named `latest-report` that resolves to `reports/production.txt`
    - a hard link named `inventory.hard` to `source/inventory.txt`
13. Set permissions so that:
    - `source/inventory.txt` is readable and writable by its owner, readable by its group, and inaccessible to others
    - `reports` is fully accessible by its owner, traversable and readable by its group, and inaccessible to others

### Part D — Archives and documentation

14. Create `archive/reports.tar.gz` containing the `reports` directory and its contents.
15. Create a bzip2-compressed tar archive named `archive/source.tar.bz2` containing the `source` directory and its contents.
16. Validate both archives by listing their contents without extracting over your working files.
17. Use only locally installed documentation to determine which option makes a human-readable long listing display an indicator after directory names. Record:
    - the command whose documentation you consulted
    - the option you found
    - which local documentation source you used
    in `reports/documentation.txt`.

### Part E — Remote transfer

18. Transfer `archive/reports.tar.gz` to your home directory on `lab-cli-rhel-47` using a secure transfer method.
19. Log in to `lab-cli-rhel-47` and verify that the transferred archive exists, is recognized as gzip-compressed data, and can have its contents listed.

Do not configure a service, open a firewall port, or create an SSH key merely to finish this part. If normal SSH access is unavailable, report the exact symptom as evidence.

## What to submit here

Reply with:

1. The commands you used, in order. Shell history is acceptable after removing unrelated or sensitive entries.
2. Final verification output showing:
   - the directory structure
   - permissions and both link targets/types
   - the contents of all report text files
   - the member listing of both archives
   - the remote archive verification, or the exact SSH failure
3. A short note identifying any step where you used local documentation or were uncertain.

Do not include passwords, private keys, subscription data, or tokens.

## Grading policy

The result will be graded for correctness, safety, command choice, verification quality, and independent execution. Mistakes receive hints before a full solution. Ratings and the Module 1 pace should be recorded in `PROGRESS.md` and `SESSION_LOG.md`.
