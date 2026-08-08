---
date: 2025-09-16T17:44:30.000Z
---

## **Prerequisites**

| **Item** | **What you need to confirm** |
|----|----|
| **NFS Server** | The Synology (or other server) exports the folder with **Read/Write** permission for your Mac’s IP address and allows connections from **non-privileged ports** (*insecure* option enabled). |
| **Share path** | `/volume1/archive` (adjust if different). |
| **macOS user** | `gvenegas` (change the commands if the other Mac uses a different short username). |
| **Administrator rights** | You can run `sudo` on the Mac. |

---

## **Steps on the Mac**

> Run each command in **Terminal**. Replace the values in
> **UPPERCASE** where needed.

### **1 Remove the old mount point (if it exists)**

~~~bash
sudo rmdir ~/nfsarchive 2>/dev/null || true   # ignore “not found”
~~~

### **2 Edit the direct map file `/etc/auto_nfs`**

~~~bash
sudo nano /etc/auto_nfs
~~~

Add **one single** line (all on the same line):

~~~bash
/Users/USERNAME/nfsarchive   -fstype=nfs,nfc,resvport   NAS_IP:/volume1/archive
~~~

Save (`^O`, `Enter`) and exit (`^X`).

### **3 Tell autofs this is a direct map**

~~~bash
sudo nano /etc/auto_master
~~~

Add (or uncomment) exactly one line:

~~~bash
/-    auto_nfs   -nobrowse
~~~

Comment out any other line that points `auto_nfs` to a folder such as
`/Network` or `/nfs`; there should be **only one reference**.

The end of the file should look like this:

~~~bash
/home                   auto_home       -nobrowse,hidefromfinder
/Network/Servers        -fstab
/-                      auto_nfs        -nobrowse
~~~

### **4 Reload autofs**

~~~bash
sudo automount -vc
~~~

No errors should appear; ignore “no unmounts”.

### **5 Trigger the first mount and test**

~~~bash
cd ~/nfsarchive          # autofs creates and mounts on demand
ls                       # should list the files from Synology
~~~

Verify with `mount | grep nfsarchive` that the NFS mount is active.

---

## **What does this method do?**

- **Direct map (`/-`)** allows placing the share **wherever you want**
  without interfering with Apple’s reserved `/Network/Servers` hierarchy.
- **`nfc`** keeps filenames consistent in Finder;
  **`resvport`** satisfies Synology’s default security policy.
- **Autofs** mounts only when accessed and persists across reboots,
  without scripts or startup items, fully compatible with SIP.

---

## **Common issues and quick fixes**

| **Symptom** | **Solution** |
|----|----|
| `cd …: Permission denied` | 1) Run `sudo rmdir` to remove the leftover local folder and **then** try again. 2) In Synology, set **Squash** to “Map all users to admin” for testing, then adjust later. |
| `dir <name> must start with '/'` message in `automount -vc` | You are using a **direct** map, so the key **must be a full path** (Step 2). |
| Does not mount and shows no errors | Verify that in `/etc/auto_master` there is **only one** line pointing to `auto_nfs`. |
| Does not appear in Finder | Autofs hides mounts from the sidebar; add a favorite pointing to `~/nfsarchive`. |