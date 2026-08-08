---
date: 2025-09-13T04:24:50.000Z
---

1. Open Terminal
2. After making your changes, press CTRL+O to save the file, then CTRL+X to exit nano.

To make sure your changes take effect immediately, you can clear your system's DNS cache with the following command:

~~~bash
sudo killall -HUP mDNSResponder
~~~

This restarts the DNS service on your Mac.

In the nano editor, you will see a list of IP addresses followed by one or more hostnames. To block a website, you can add a new line with `127.0.0.1` followed by the domain name. For example:

~~~bash
127.0.0.1 example.com
~~~

This redirects requests for `example.com` to your local machine, effectively blocking it.

Use the following command to open the hosts file in the nano editor, which comes built into macOS:

~~~bash
sudo nano /etc/hosts
~~~

You will be prompted to enter your password. This is your user account password.

Now, any changes you made should be active. If you are using the hosts file for development and need to configure more advanced options, you may want to consider additional tools or directly edit your environment configuration.