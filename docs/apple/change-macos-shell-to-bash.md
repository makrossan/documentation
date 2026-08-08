---
date: 2025-09-26T13:27:49.000Z
---

# How to Change the macOS Shell to Bash

**Switch to Bash (system Bash):**

~~~bash
chsh -s /bin/bash
~~~

Close and reopen Terminal, or log out and sign back in.

**If you use Homebrew Bash, add it and switch to it:**

~~~bash
echo /opt/homebrew/bin/bash | sudo tee -a /etc/shells
chsh -s /opt/homebrew/bin/bash
~~~

**Check the current shell:**

~~~bash
echo $SHELL
~~~

**Switch back to zsh (macOS default):**

~~~bash
chsh -s /bin/zsh
~~~