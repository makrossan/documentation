---
date: 2025-11-18T02:26:15.000Z
---

**Step 1:** On a Mac, start by downloading
<a href="https://github.com/corpnewt/gibMacOS"
rel="noreferrer"><strong>gibMacOS</strong></a> from **GitHub**.
Extract the contents of the downloaded **.zip** file and enter the
folder.

<figure class="kg-card kg-image-card">
<img src="__GHOST_URL__/content/images/2025/11/image.png"
class="kg-image" loading="lazy"
srcset="__GHOST_URL__/content/images/size/w600/2025/11/image.png 600w, __GHOST_URL__/content/images/size/w1000/2025/11/image.png 1000w, __GHOST_URL__/content/images/2025/11/image.png 1295w"
sizes="(min-width: 720px) 720px" width="1295" height="636" />
</figure>

**Step 2:** Enter the extracted directory and double-click the
`gibMacOS.command` file

<figure class="kg-card kg-image-card">
<img src="__GHOST_URL__/content/images/2025/11/image-1.png"
class="kg-image" loading="lazy"
srcset="__GHOST_URL__/content/images/size/w600/2025/11/image-1.png 600w, __GHOST_URL__/content/images/2025/11/image-1.png 783w"
sizes="(min-width: 720px) 720px" width="783" height="284" />
</figure>

<div class="kg-card kg-callout-card kg-callout-card-yellow">

<div class="kg-callout-emoji">

⚠️

</div>

<div class="kg-callout-text">

Since we are running a script, the file may not open right away.
Open the security settings window and allow the file to run after
opening it for the first time.

</div>

</div>

<figure class="kg-card kg-image-card">
<img src="__GHOST_URL__/content/images/2025/11/image-4.png"
class="kg-image" loading="lazy" width="264" height="266" />
</figure>

<figure class="kg-card kg-image-card">
<img src="__GHOST_URL__/content/images/2025/11/image-2.png"
class="kg-image" loading="lazy"
srcset="__GHOST_URL__/content/images/size/w600/2025/11/image-2.png 600w, __GHOST_URL__/content/images/2025/11/image-2.png 719w"
width="719" height="717" />
</figure>

<div class="kg-card kg-callout-card kg-callout-card-blue">

<div class="kg-callout-emoji">

💡

</div>

<div class="kg-callout-text">

When the file opens, if prompted, choose **yes (Y)** to install
**Python**.

</div>

</div>

**Step 3:** Once the script finishes installing Python, you will see a
screen in the terminal asking which version of macOS you want to
download. In this example, **macOS Sequoia 15.7.1** is used, so
option **7** will be selected.

<div class="kg-card kg-callout-card kg-callout-card-blue">

<div class="kg-callout-emoji">

💡

</div>

<div class="kg-callout-text">

Write down the size of the file you are going to download.
Later, we will create an image based on this file, and it must be
larger than the downloaded file.

</div>

</div>

<figure class="kg-card kg-image-card">
<img src="__GHOST_URL__/content/images/2025/11/image-6.png"
class="kg-image" loading="lazy" width="397" height="533" />
</figure>

<figure class="kg-card kg-image-card">
<img src="__GHOST_URL__/content/images/2025/11/image-8.png"
class="kg-image" loading="lazy" width="509" height="179" />
</figure>

**Step 4:** Once the download is complete, go to the created folder.
If you ran the file from the Downloads folder, the path will look like
this:
`~/Downloads/gibMacOS-master/macOS Downloads/publicrelease/093-52107-15.7.1 macOS Sequoia (24G231)/`
Your version numbers may be different.
Inside this folder, double-click **`InstallAssistant.pkg`** and follow
the instructions. This will install the application needed to build the
ISO image compatible with Proxmox.

<figure class="kg-card kg-image-card">
<img src="__GHOST_URL__/content/images/2025/11/image-9.png"
class="kg-image" loading="lazy"
srcset="__GHOST_URL__/content/images/size/w600/2025/11/image-9.png 600w, __GHOST_URL__/content/images/2025/11/image-9.png 806w"
sizes="(min-width: 720px) 720px" width="806" height="586" />
</figure>

**Step 5:** Now we will build the ISO image for Proxmox.
In a new terminal window, create a temporary disk image.
Make sure it is larger than the downloaded image.
For macOS Sequoia 15.7.1, a 20GB image worked.

~~~console
hdiutil create -o /tmp/macOS -size 20000m -volname macOS -layout SPUD -fs HFS+J
~~~

**Step 6:** Mount the temporary image you just created.

~~~console
hdiutil attach /tmp/macOS.dmg -noverify -mountpoint /Volumes/macOSISO
~~~

**Step 7:** Use the program installed earlier to create the ISO image
compatible with Proxmox.
This will take a few minutes.

~~~console
sudo /Applications/Install\ macOS\ Sequoia.app/Contents/Resources/createinstallmedia --volume /Volumes/macOSISO --nointeraction
~~~

<figure class="kg-card kg-image-card">
<img src="__GHOST_URL__/content/images/2025/11/image-10.png"
class="kg-image" loading="lazy"
srcset="__GHOST_URL__/content/images/size/w600/2025/11/image-10.png 600w, __GHOST_URL__/content/images/2025/11/image-10.png 949w"
sizes="(min-width: 720px) 720px" width="949" height="307" />
</figure>

<div class="kg-card kg-callout-card kg-callout-card-yellow">

<div class="kg-callout-emoji">

⚠️

</div>

<div class="kg-callout-text">

Make sure the path matches the exact version you installed.
In this case, the file is called `Install macOS Sequoia.app`, so the
path is `/Applications/Install\ macOS\ Sequoia.app/`
If you installed a beta, for example, it might be:
`/Applications/Install\ macOS\ Ventura\ beta.app/`

</div>

</div>

**Step 8:** Unmount the image using the following command:

~~~console
hdiutil detach -force /Volumes/Install\ macOS\ Sequoia
~~~

<div class="kg-card kg-callout-card kg-callout-card-yellow">

<div class="kg-callout-emoji">

⚠️

</div>

<div class="kg-callout-text">

If you follow this guide exactly, you can copy and paste the command.
If you use a different version, verify the correct path from Finder.

</div>

</div>

**Step 9:** Convert the unmounted image into an **ISO** file to upload
to Proxmox.

~~~console
hdiutil convert /tmp/macOS.dmg -format UDTO -o ~/Desktop/macOS-Sequoia.cdr
~~~

**Step 10:** Change the extension from `.cdr` to `.iso`.

~~~console
mv ~/Desktop/macOS-Sequoia.cdr ~/Desktop/macOS-Sequoia.iso
~~~

**Step 11:** Finally, remove the temporary image.

~~~console
rm /tmp/macOS.dmg
~~~
