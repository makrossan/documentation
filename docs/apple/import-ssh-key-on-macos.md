---
date: 2025-09-13T17:30:59.000Z
---

### **1. Place the private key in the correct directory**

By default, SSH looks for keys in `~/.ssh/`

1. Open Terminal and run:

~~~bash
mkdir -p ~/.ssh
chmod 700 ~/.ssh
~~~

2. Move your `id_rsa` and `id_rsa.pub` files into the `~/.ssh/` directory. For example:

~~~bash
mv /path/to/id_rsa ~/.ssh/
mv /path/to/id_rsa.pub ~/.ssh/
~~~

3. Set the correct permissions:

~~~bash
chmod 600 ~/.ssh/id_rsa
chmod 644 ~/.ssh/id_rsa.pub
~~~

---

### **2. Add the key to the SSH agent**

macOS uses `ssh-agent` to manage SSH keys.

If you want the key to be remembered even after restarting, you can use the macOS Keychain:

~~~bash
/usr/bin/ssh-add --apple-use-keychain ~/.ssh/id_rsa
~~~

Start the agent and add the key:

~~~bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
~~~

---

### **3. (Optional) Add host configuration in `~/.ssh/config`**

To simplify connections to specific servers using your key, you can create or edit the `~/.ssh/config` file:

~~~bash
nano ~/.ssh/config
~~~

Example entry:

~~~bash
Host service.ourdomain.com
    HostName service.lan.ourdomain.com
    User $USER
    Port 22
    IdentityFile ~/.ssh/id_rsa
    UseKeychain yes
    AddKeysToAgent yes
~~~