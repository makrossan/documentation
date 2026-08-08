---
date: 2025-11-16T17:28:00.000Z
---

In this guide, I am sharing a step-by-step walkthrough to get macOS 15 Sequoia running inside a VM on Proxmox VE using OpenCore as the bootloader.

The idea is simple: download the Sequoia ISO and the OpenCore ISO, create a VM, adjust the hardware so macOS boots properly, and edit the VM configuration file.

The approach is practical: few steps, minimal theory, and everything I personally need to remember whenever I need to repeat the process.

---

## Step by step

### 1. Prerequisites

- Make sure your Proxmox node has a CPU with AVX2 support  
  (required for macOS Sequoia).
- Verify that you are running an updated version of Proxmox VE 8.x.
- <a href="__GHOST_URL__/descargar-iso-de-macos/" rel="noreferrer">Prepare a macOS 15 Sequoia ISO</a> (or download it from a trusted repository).
- Download the ISO for
  <a href="https://github.com/thenickdude/KVM-Opencore/releases"
  rel="noreferrer">KVM OpenCore</a> from GitHub.
- From the Proxmox web interface, upload both ISOs to the storage where you normally keep your images (for example, `local` or `local-lvm`).

---

### 2. Create the base VM in Proxmox

1. Sign in to the Proxmox web interface.
2. In the tree on the left, right-click the node and select **Create VM**.
3. Give it an easy-to-identify name, for example `macOS-Sequoia`, and use an ID you will remember (in this example I use `109`).
4. In the **OS** tab:
   - In **Type**, select **Other**.
   - In **ISO image**, select the KVM OpenCore ISO  
     (not the Sequoia ISO yet).
   - Continue with **Next**.

---

### 3. Adjust the system (firmware, graphics, and EFI)

- In the **System** tab:
  - **Graphic card**: VMware compatible
  - **BIOS**: OVMF (UEFI)
  - Uncheck **Pre-Enroll Keys**
  - Check **Add EFI Disk** and leave the default storage
  - **Machine**: `q35`
  - **SCSI Controller**: `VirtIO SCSI`

---

### 4. Disk, CPU, memory, and network

#### 4.1. Disk

- **Bus/Device**: `VirtIO Block`  
  (or SCSI if you prefer, but I usually use VirtIO)
- **Disk size**: minimum 64 GB, personally I use 128 GB if I have space
- **Cache**: **Write back (unsafe)** for better performance  
  (keep the power-loss risk in mind)

#### 4.2. CPU

- Assign at least 4 cores  
  (more if you have the resources)
- **Type**: `host`

#### 4.3. Memory

- Configure 8192 MB minimum  
- If possible, assign 12 GB or more

#### 4.4. Network

- **Network Model**: `VMware vmxnet3`  
  (usually works better with macOS)
- Review the summary and click **Finish** to create the VM

---

### 5. Add the macOS Sequoia ISO to the VM

1. In the tree on the left, select the new VM  
   (for example, `109 macOS-Sequoia`)
2. Go to **Hardware**
3. Click **Add → CD/DVD Drive**
4. Select the storage and the macOS Sequoia ISO, then confirm with **Add**

---

### 6. Select the boot drive

Next, click your macOS VM to select it. Then go to **Options -> Boot Order**.

We need to make sure that **OpenCore.iso** is configured as the first boot option.

---

### 7. Edit the VM configuration file on the node

Open a console on the Proxmox node (SSH or shell from the web interface) and edit the VM configuration file  
(replace `109` with your actual VM ID):

~~~terminal
nano /etc/pve/qemu-server/109.conf
~~~

~~~bash
args: -device isa-applesmc,osk="ourhardworkbythesewordsguardedpleasedontsteal(c)AppleComputerInc" -smbios type=2 -device qemu-xhci -device usb-kbd -device usb-tablet -global nec-usb-xhci.msi=off -global ICH9-LPC.acpi-pci-hotplug-with-bridge-support=off -cpu host,vendor=GenuineIntel,+invtsc,+hypervisor,kvm=on,vmware-cpuid-freq=on
~~~

If your Proxmox node is running on an Intel CPU, add the following line at the end of the `.conf` file.

~~~bash
args: -device isa-applesmc,osk="ourhardworkbythesewordsguardedpleasedontsteal(c)AppleComputerInc" -smbios type=2 -device qemu-xhci -device usb-kbd -device usb-tablet -global nec-usb-xhci.msi=off -global ICH9-LPC.acpi-pci-hotplug-with-bridge-support=off -cpu Haswell-noTSX,vendor=GenuineIntel,+invtsc,+hypervisor,kvm=on,vmware-cpuid-freq=on
~~~

If your Proxmox node is running on an AMD CPU, add the following line at the end of the `.conf` file.

1. Find the lines for both CD/DVD drives  
   (OpenCore and Sequoia)
   - Use `Ctrl+W` and search for `media=cdrom`
   - On each line where you see `,media=cdrom`, replace it with `,media=disk` and add `,cache=unsafe`
2. Save and exit with `Ctrl+O`, `Enter`, and then `Ctrl+X`

---

### 8. Start the VM and launch the macOS installer

1. Go back to the Proxmox web interface
2. Select the VM `macOS-Sequoia`, right-click it, and choose **Start**
3. Open **Console**
4. In the OpenCore menu, first try the macOS install option

If the Sequoia installer does not appear, enter the UEFI Shell and run:

~~~bash
fs0: System\Library\CoreServices\boot.efi
~~~

(The disk number `fs0:` may vary, try `fs1:` or `fs2:` if needed.)

---

### 9. Format the disk and install inside the VM

1. Once the macOS wizard loads, select your language
2. Open **Disk Utility**
3. Select the **VirtIO Block Media** disk you created when configuring the VM
4. Click **Erase** and configure:
   - **Name**: `macOS`
   - **Format**: **APFS**
5. Confirm the erase, close **Disk Utility**
6. Select **Install macOS Sequoia** and follow the wizard:
   accept the terms, select the `macOS` disk, and continue
7. The VM will reboot several times, let it finish until the initial setup screen appears

---

### 10. Initial macOS setup

1. Complete the basic wizard steps:
   - Region, language, and keyboard
   - Accessibility options  
     (I usually choose “Later”)
   - Skip migrations and Apple ID at first if you only want to test
   - Accept the terms, create a local user, and set a password
   - Adjust the time zone and disable analytics if you prefer
2. At the end, you will see the macOS Sequoia desktop inside the VM

---

### 11. (Optional) Copy OpenCore to the disk EFI partition

This part allows the VM to boot without leaving the OpenCore ISO mounted.

1. From macOS inside the VM:
   - Download the <a
     href="https://github.com/thenickdude/KVM-Opencore/releases/download/v21/OpenCoreEFIFolder-v21.zip"
     rel="noreferrer"><strong>EFI</strong></a> folder from KVM OpenCore
   - Download <a href="https://github.com/corpnewt/MountEFI"
     rel="noreferrer"><strong>MountEFI</strong></a> from GitHub
2. Select the disk number where macOS is installed
3. The EFI partition will be mounted in Finder
4. If an `EFI` folder already exists, rename it to `EFI.orig`
5. Copy the OpenCore `EFI` folder into the mounted partition
6. Shut down the VM from macOS

Open **Terminal** in macOS and run:

~~~terminal
cd ~/Downloads/MountEFI-update
chmod +x MountEFI.command
./MountEFI.command
~~~

---

### 12. Remove the ISOs and test direct boot

1. With the VM powered off, go back to **Hardware** in Proxmox
2. Select the OpenCore CD/DVD drive and click **Detach**
3. Do the same for the Sequoia ISO
4. Start the VM again and verify it still boots macOS without the ISOs mounted

---

## Command block

~~~bash
# (on the Proxmox node)
# 1. Edit the VM configuration
nano /etc/pve/qemu-server/1500.conf

# 2. Add the correct args line for your CPU

# 3. Adjust ISO lines
# remove ,media=cdrom
# add ,cache=unsafe

# 4. Save changes and return to the GUI

# 5. Start the VM from the GUI

# (inside UEFI shell if installer does not boot)
fs0:
System\Library\CoreServices\boot.efi

# (inside macOS, optional)
cd ~/Downloads/MountEFI-update
chmod +x MountEFI.command
./MountEFI.command
~~~

---

## Best practices

- Only run macOS in environments where you clearly understand the legal and licensing implications  
  I personally treat this as a lab environment for testing
- Take VM snapshots in Proxmox before editing the `1500.conf` file and before major changes
- Use fast storage (SSD/NVMe) for the VM disk  
  macOS feels much smoother
- Avoid over-allocating memory  
  ideally leave enough RAM for the host and other VMs
- Keep Proxmox and hardware firmware updated to minimize compatibility issues with AVX2 and virtualization

---

## FAQ

### Does the VM stay on a black screen at boot?

This is usually an issue with the `args` line or firmware settings  
(BIOS not OVMF or machine not `q35`).

Review the `qemu-server/ID.conf` file and compare it with a known working configuration.

### The macOS installer does not see the disk

Make sure the disk is configured as `VirtIO Block` (or SCSI) and initialized as APFS in **Disk Utility**.

### The installation keeps rebooting in a loop

This is often because the VM is booting again from the Sequoia or OpenCore ISO.

Verify boot order and, once installed, use the internal EFI and remove the ISOs.

### Do I need the exact same CPU and args values from other tutorials?

Not necessarily.

The important thing is to respect the overall structure of the `args` line and use a CPU-compatible configuration for Intel or AMD.

---

## Closing

I keep this guide as a quick reminder of what works for me when bringing up macOS 15 Sequoia inside Proxmox without losing hours testing different combinations.

If this helps you as well, the idea is that you can follow the steps above, adapt the details to your environment, and get the VM ready for testing, demos, or whatever you need without turning it into an endless weekend project.

---

**Sources and references:**

- Max Kulik:  
  https://klabsdev.com/definitive-guide-to-running-macos-in-proxmox/
- i12bretro:  
  https://i12bretro.github.io/tutorials/0944.html