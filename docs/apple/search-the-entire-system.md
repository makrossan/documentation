---
date: 2025-09-15T16:40:02.000Z
---

To search for anything whose name contains `example_name` in macOS.

1. **Do you need to search the entire system?**

~~~bash
sudo find / -iname '*example_name*' 2>/dev/null
~~~

Using `sudo` allows `find` to enter protected directories, and `2>/dev/null`
hides permission denied messages.

2. **If you are looking specifically for directories or files, use a filter:**
   - Files only: `... -type f`
   - Folders only: `... -type d`

3. **To view the result in Finder:**

~~~bash
open "$(mdfind -name 'example_name' | head -1)"
~~~

This will open the first result directly in Finder.