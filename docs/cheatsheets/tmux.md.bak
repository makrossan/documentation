---
title: The Ultimate tmux Guide and Cheat Sheet
description: Essential tmux commands organized into practical sections, using Ctrl+b as the default prefix.
---

# The Ultimate tmux Guide and Cheat Sheet

Essential tmux commands organized into practical sections. The default prefix is `Ctrl + b`.

[← Back to the dashboard](/#cheat-sheets)

## Prefix and basic concepts

*The minimum you need to get started.*

> **Default prefix:** `Ctrl + b`. You can change it with `set-option -g prefix C-a`. Every shortcut that mentions `Prefix` assumes `Ctrl + b`; adjust it if you have remapped the prefix.

## Starting tmux and managing sessions

*Create, list, attach to, and manage sessions.*

### Shell commands

- `tmux` — Start a new session.
- `tmux ls` — List all sessions.
- `tmux new -s name` — Create a named session.
- `tmux attach -t name` — Attach to a session.
- `tmux detach` — Detach from inside tmux.
- `tmux rename-session -t old_name new_name` — Rename a session.
- `tmux switch -t name` — Switch to a session.
- `tmux kill-session -t name` — Delete a session by name.
- `tmux kill-server` — Delete all sessions by stopping the tmux server.

### Prefix shortcuts inside tmux

- `Prefix + :` — Open the command prompt.
- `Prefix + d` — Detach from the session.
- `Prefix + s` — Open the session selector.
- `Prefix + $` — Rename the current session.
- `Prefix + ?` — List key bindings.
- `Prefix + ,` — Rename the current window.
- `Prefix + w` — Open the window selector.
- `Prefix + :`, then `kill-session` — Close the current session.

## Panes

*Split the terminal and move between panes.*

### Managing panes

- `Prefix + %` — Split the window vertically.
- `Prefix + "` — Split the window horizontally.
- `Prefix + o` — Move to the next pane.
- `Prefix + ;` — Switch between the two most recently used panes.
- `Prefix + {` / `Prefix + }` — Swap the current pane left or right.
- `Prefix + q` — Display pane numbers.
- `Prefix + z` — Toggle zoom for the current pane.
- `Prefix + x` — Close the current pane.
- `Prefix + !` — Promote the current pane to its own window.

### Movement and advanced options

- `Prefix + ↑/↓/←/→` — Move focus between panes.
- `Prefix + Alt + ↑/↓/←/→` — Resize the current pane.
- `join-pane -s 2.1 -t 1.0` — Join pane `2.1` to pane `1.0`.
- `break-pane` — Convert the current pane into a window.
- `swap-pane -[UDLR]` — Swap the pane in the specified direction.
- `select-pane -t :.+` — Select the next pane.
- `set-window-option synchronize-panes on` — Synchronize input across panes.
- `display-message '#P'` — Display the current pane index.

## Windows and tabs

*Organize your work across multiple views.*

### Window commands

- `rename-window new_name` — Rename the current window.
- `swap-window -t 2` — Swap the current window with window 2.
- `move-window -t 3` — Move the current window to index 3.
- `link-window -s src -t dst` — Link a window between sessions.
- `unlink-window` — Unlink the current window.
- `kill-window` — Close the current window.
- `display-message '#W'` — Display the current window name.

### Window shortcuts using the prefix

- `Prefix + c` — Create a new window.
- `Prefix + p` — Go to the previous window.
- `Prefix + n` — Go to the next window.
- `Prefix + <0-9>` — Select a window by number.
- `Prefix + &` — Delete the current window.
- `Prefix + .` — Move the current window.
- `Prefix + f` — Find a window by name.
- `Prefix + l` — Return to the most recently used window.

## Copy mode and scrolling

*Navigate history and select text.*

### Buffers and configuration

- `:show-buffer` — Display the primary paste buffer.
- `:list-buffers` — List all paste buffers.
- `:save-buffer file` — Save a paste buffer to a file.
- `:delete-buffer -b N` — Delete paste buffer *N*.
- `set -g mode-keys vi` — Use Vim keys in Copy mode.

### Copy mode shortcuts

- `Prefix + [` — Enter Copy mode.
- `q` — Leave Copy mode.
- `Space` — Start a selection.
- `Enter` — Copy the selection.
- `Page Up` / `Page Down` — Scroll up or down.
- `/` — Search forward.
- `?` — Search backward.
- `n` / `N` — Go to the next or previous search result.

## Resizing and layouts

*Built-in layouts and quick adjustments.*

### Layouts

- `select-layout even-horizontal` — Distribute panes evenly from left to right.
- `select-layout even-vertical` — Distribute panes evenly from top to bottom.
- `select-layout main-horizontal` — Place the main pane at the top and the others below it.
- `select-layout main-vertical` — Place the main pane on the left.
- `select-layout tiled` — Arrange all panes in a tiled grid.

### Layout shortcuts

- `Prefix + Alt + ↑/↓/←/→` — Resize the current pane.
- `Prefix + Space` — Cycle through pane layouts.
- `Prefix + q` — Display pane numbers.
- `Prefix + {` / `Prefix + }` — Swap panes left or right.
- `Prefix + z` — Toggle zoom for the active pane.

## Mouse support

*For times when you want to use the mouse.*

### Configuration

- `set -g mouse on` — Enable the mouse for resizing, selecting, and other actions.
- `set -g mouse off` — Disable mouse support.
- `setw -g mode-mouse on` — Enable the mouse in Copy mode for tmux versions earlier than 2.1.

### Practical use

- Drag a pane border to resize the pane.
- Click a pane or window to focus it.
- Use the mouse wheel to scroll through history.

## Automation and scripting

*Prepare complete sessions with a single command.*

### Useful scripting commands

- `tmux new-session -d -s MySession` — Create a detached session.
- `tmux send-keys -t MySession 'top' Enter` — Send a command to a pane.
- `tmux new-window -t MySession:1 -n 'htop'` — Create a window named `htop`.
- `tmux split-window -h -t MySession:1` — Split the window horizontally.
- `tmux select-pane -t MySession:1.0` — Select pane 0 in window 1.

### Example script

```bash
# Example script
tmux new-session -d -s dev
tmux new-window -t dev:1 -n code
tmux send-keys -t dev:1 'vim .' C-m
tmux split-window -h -t dev:1
tmux send-keys -t dev:1.1 'npm start' C-m
tmux attach -t dev
```

## Configuration file (`~/.tmux.conf`)

*Recommended shortcuts and options.*

```tmux
# Remap the prefix
set-option -g prefix C-a
unbind C-b
bind C-a send-prefix

# Mouse support
set -g mouse on

# Vim keys in Copy mode
setw -g mode-keys vi

# 256-color support
set -g default-terminal "screen-256color"

# Useful titles
set -g set-titles on
set -g set-titles-string "#S:#I.#P #W"

# Shortcuts for splitting panes
bind | split-window -h
bind - split-window -v

# Reload the configuration
bind r source-file ~/.tmux.conf \; display-message "Configuration reloaded!"
```

## Tips and troubleshooting

*Common problems and their solutions.*

- **tmux does not respond to key presses:** you may be inside a nested tmux session. The default prefix is `Ctrl + b`; try pressing `Ctrl + b` twice.
- **Copy and paste do not work:** use `set -g mouse on`, try holding `Shift` while using the mouse, or enable clipboard support with the `tmux-yank` plugin.
- **Terminal colors look incorrect:** verify that `set -g default-terminal "screen-256color"` is present in `~/.tmux.conf` and supported by your terminal emulator.
- **Share a tmux session:** run `tmux attach -t session` from multiple terminals under the same user account.

## Plugins and additional resources

*Extend tmux and keep learning.*

- [TPM — tmux Plugin Manager](https://github.com/tmux-plugins/tpm) — Easy plugin management.
- [tmux-sensible](https://github.com/tmux-plugins/tmux-sensible) — Better default settings.
- [tmux-resurrect](https://github.com/tmux-plugins/tmux-resurrect) — Restore tmux sessions.
- [tmux-continuum](https://github.com/tmux-plugins/tmux-continuum) — Continuously save tmux sessions.
- [tmux-yank](https://github.com/tmux-plugins/tmux-yank) — System clipboard integration.
- [Official tmux wiki](https://github.com/tmux/tmux/wiki)
- [The Tao of tmux](https://leanpub.com/the-tao-of-tmux/read) — Free online book.
- [tmuxcheatsheet.com](https://tmuxcheatsheet.com/)
