---
title: "The Ultimate Tmux Cheat Sheet & Guide"
date: 2025-09-14T00:05:30.000Z
slug: the-ultimate-tmux-cheat-sheet-guide
---

**Prefix default:** `Ctrl + b` (can be changed via
`set-option -g prefix C-a`). All commands assume **prefix** is
`Ctrl + b`. Replace as needed if you remap.

## Getting Started & Sessions

- `tmux` Start new session
- `tmux new -s name` New session with name
- `tmux ls` List all sessions
- `tmux attach -t name` Attach to named session
- `tmux detach` Detach (from inside tmux)
- `tmux kill-session -t name` Kill session by name
- `tmux kill-server` Kill all sessions (server)
- `tmux rename-session -t old new` Rename session
- `tmux switch -t name` Switch to session
- `prefix` d Detach from session
- `prefix` s Session chooser
- `prefix` \$ Rename current session
- `prefix` : Open command prompt
- `prefix` ? List key bindings
- `prefix` , Rename current window
- `prefix` w Window chooser

## Windows & Tabs

- `prefix` c Create new window
- `prefix` p Previous window
- `prefix` n Next window
- `prefix` \<0-9\> Select window by number
- `prefix` & Kill current window
- `prefix` . Move window
- `prefix` f Find window by name
- `prefix` l Last window
- `rename-window newname`
- `swap-window -t 2` Swap with window 2
- `move-window -t 3` Move to window 3
- `link-window -s src -t dst`
- `unlink-window`
- `kill-window`
- `display-message '#W'` Show window name

## Panes

- `prefix` % Split vertically
- `prefix` " Split horizontally
- `prefix` o Go to next pane
- `prefix` q Show pane numbers
- `prefix` ; Toggle between last two panes
- `prefix` x Kill current pane
- `prefix` { } Swap pane left/right
- `prefix` z Toggle zoom pane
- `prefix` \<arrow\> Move pane focus
- `prefix` Alt + \<arrow\> Resize pane
- `join-pane -s 2.1 -t 1.0` Join window 2.1 to 1.0
- `break-pane` Convert pane to window
- `swap-pane -[UDLR]` Swap pane direction
- `select-pane -t :.+` Select next
- `set-window-option synchronize-panes on` Sync panes
- `display-message '#P'` Show pane index

## Copy & Scroll Mode

- `prefix` \[ Enter copy mode
- `q` Quit copy mode
- `Space` Start selection
- `Enter` Copy selection
- `PgUp/PgDn` Scroll up/down
- `/` Search forward
- `?` Search backward
- `n/N` Next/Prev search result
- `:show-buffer` Show top buffer
- `:list-buffers` List all buffers
- `:save-buffer filename` Save buffer to file
- `:delete-buffer -b N` Delete buffer N
- `set -g mode-keys vi` Use Vim keys in copy mode

## Resizing & Layout

- `prefix` Alt + ↑/↓/←/→ Resize pane
- `prefix` Space Change pane layout
- `prefix` q Show pane numbers
- `prefix` { } Swap panes left/right
- `prefix` z Zoom/unzoom pane
- `select-layout even-horizontal`
- `select-layout even-vertical`
- `select-layout main-horizontal`
- `select-layout main-vertical`
- `select-layout tiled`

## Mouse Support

- `set -g mouse on` Enable mouse for resizing, selecting, etc
- `set -g mouse off` Disable mouse support
- `setw -g mode-mouse on` Enable mouse in copy mode (tmux \<2.1)
- Drag border to resize pane
- Click pane/window to focus
- Scroll mouse wheel to scroll history

## Scripting & Automation

- `tmux new-session -d -s mysession` Detached session
- `tmux send-keys -t mysession 'top' Enter` Send command to pane
- `tmux new-window -t mysession:1 -n 'htop'`
- `tmux split-window -h -t mysession:1`
- `tmux select-pane -t mysession:1.0`

\# Script Example  
tmux new-session -d -s dev  
tmux new-window -t dev:1 -n code  
tmux send-keys -t dev:1 'vim .' C-m  
tmux split-window -h -t dev:1  
tmux send-keys -t dev:1.1 'npm start' C-m  
tmux attach -t dev  

## Config File (~/.tmux.conf)

\# Prefix remap  
set-option -g prefix C-a  
unbind C-b  
bind C-a send-prefix  

# Mouse support

set -g mouse on

# Vim keys in copy mode

setw -g mode-keys vi

# Enable 256 color support

set -g default-terminal "screen-256color"

# Useful titles

set -g set-titles on  
  
set -g set-titles-string "#S:#I.#P \#W"

# Split pane shortcuts

bind \| split-window -h  
  
bind - split-window -v

# Reload config

bind r source-file ~/.tmux.conf ; display-message "Config reloaded!"  
  

## Troubleshooting & Tips

- tmux not responding to keys? Are you in a nested tmux session? Default
  prefix is `Ctrl+b`. Try `Ctrl+b` twice.
- Copy/paste not working? Use `set -g mouse on` and try Shift+Mouse or
  enable system clipboard with `tmux-yank` plugin.
- Terminal colors off? Check `set -g default-terminal "screen-256color"`
  in both `~/.tmux.conf` and your terminal emulator.
- Sharing tmux? Run `tmux attach -t session` from multiple terminals
  (same user).

## Plugins & Extensions

- [TPM (Tmux Plugin Manager)](https://github.com/tmux-plugins/tpm) Easy
  plugin management
- [tmux-sensible](https://github.com/tmux-plugins/tmux-sensible) Best
  default settings
- [tmux-resurrect](https://github.com/tmux-plugins/tmux-resurrect)
  Restore tmux sessions
- [tmux-continuum](https://github.com/tmux-plugins/tmux-continuum)
  Continuous saving
- [tmux-yank](https://github.com/tmux-plugins/tmux-yank) Clipboard
  integration

**Install TPM:**
`git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm` Then
add plugins in `~/.tmux.conf` and use prefix + I to install.

## More Resources

- [tmux Wiki (Official)](https://github.com/tmux/tmux/wiki)
- [The Tao of tmux (free
  ebook)](https://leanpub.com/the-tao-of-tmux/read)
- [tmuxcheatsheet.com](https://tmuxcheatsheet.com/)
