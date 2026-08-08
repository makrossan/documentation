---
date: 2025-09-13T03:56:58.000Z
---

When trying to free up space on a MacBook, we often run into surprises. Recently, I found myself in a similar situation: after running diagnostics, deleting files, uninstalling applications, and using tools like CleanMyMac, the disk space was still not being recovered. What was concerning was that the **System Data** section had grown to an unusually large size, and I could not figure out why.

After investigating, I discovered that the culprit was the stored **snapshots** (local backup snapshots) on the system. When I ran the command `tmutil listlocalsnapshots /`, I was met with a long list of backup files, including several from **Synology Active Backup**, software I had been using to protect my data:

~~~bash
gvenegas@Greivin-Mac ~ % tmutil listlocalsnapshots /

Snapshots for disk /:
com.apple.TimeMachine.2023-12-12-074503.local
com.synology.activebackup.69YCpj37
com.synology.activebackup.7OImXMVy
com.synology.activebackup.g7rZGhdD
com.synology.activebackup.lH-caUKG
com.synology.activebackup.n6lu7Paf
com.synology.activebackup.wbWvj1M2
~~~

Despite the usefulness of **Synology Active Backup**, I ran into an issue: while I could delete the Time Machine snapshots with the command:

~~~bash
tmutil deletelocalsnapshots 2023-12-12-074503
~~~

there was no obvious way to do the same with the **Synology Active Backup** snapshots.

The solution turned out to be quite simple. I only needed to access **Synology DSM**, locate the active backup task, and delete it.

Immediately after that, the command:

~~~bash
tmutil listlocalsnapshots /
~~~

no longer showed any files, which freed up a significant amount of space in the **System Data** section.

To keep my data safe, I had to create a new backup task in Synology, knowing that I may need to repeat this process every six months to avoid these files piling up again.

While this is not a major inconvenience, it would be ideal if Synology offered a more efficient solution for this issue.

For now, I will continue investigating whether this problem affects only macOS or if it also impacts other systems such as Windows, Linux, and server or virtual environments.

Managing disk space on computers is always a challenge, but with the right approach and tools, we can keep our systems running smoothly.