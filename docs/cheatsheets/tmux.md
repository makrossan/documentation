---
title: tmux Cheat Sheet
description: A visual tmux command reference.
hide:
  - navigation
  - toc
---

<div class="cheatsheet-page cheatsheet-page--tmux">
<main class="outer">
    <div class="page-header">
      <div class="page-title">
        <h1>The Ultimate tmux Guide and Cheat Sheet</h1>
        <p>Essential tmux commands organized by practical sections. Default prefix Ctrl + b.</p>
      </div>
      <a href="/#cheat-sheets" class="back-button">Back to the dashboard</a>
    </div>

    <!-- Prefix/intro -->
    <section class="section">
      <div class="section-header">
        <h2>Prefix and basic concepts</h2>
        <span class="tag">The essentials for getting started</span>
      </div>
      <div class="section-body">
        <div class="note">
          <div class="note-icon">P</div>
          <div>
            <strong>Default prefix:</strong>
            <code>Ctrl + b</code> (can be changed with <code>set-option -g prefix C-a</code>).
            All the shortcuts that say <code>Prefix</code> assume <code>Ctrl + b</code> has been remapped.
          </div>
        </div>
      </div>
    </section>

    <!-- Starting tmux and managing sessions -->
    <section class="section">
      <div class="section-header">
        <h2>Starting tmux and managing sessions</h2>
        <span class="tag">Create, list and manage sessions</span>
      </div>
      <div class="section-body">
        <div class="grid">
          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Shell commands
            </div>
            <ul class="cmd-list">
              <li><code>tmux</code> <span class="desc">Start new session.</span></li>
              <li><code>tmux ls</code> <span class="desc">List all sessions.</span></li>
              <li><code>tmux new -s <span class="highlight">nombre</span></code> <span class="desc">New session with name.</span></li>
              <li><code>tmux attach -t <span class="highlight">nombre</span></code> <span class="desc">Join session.</span></li>
              <li><code>tmux detach</code> <span class="desc">Desacoplar (desde dentro de tmux).</span></li>
              <li><code>tmux rename-session -t <span class="highlight">nombre1</span> <span class="highlight">nombre2</span></code> <span class="desc">Rename session.</span></li>
              <li><code>tmux switch -t <span class="highlight">nombre</span></code> <span class="desc">Switch to session.</span></li>
              <li><code>tmux kill-session -t <span class="highlight">nombre</span></code> <span class="desc">Delete session by name.</span></li>
              <li><code>tmux kill-server</code> <span class="desc">Delete all sessions (server).</span></li>
            </ul>
          </div>
          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Prefix shortcuts within tmux
            </div>
            <ul class="cmd-list">
              <li><code>Prefix</code><span class="hotkey">:</span><span class="desc"> Open command prompt.</span></li>
              <li><code>Prefix</code><span class="hotkey">d</span><span class="desc"> Undock from the session.</span></li>
              <li><code>Prefix</code><span class="hotkey">s</span><span class="desc"> Session selector.</span></li>
              <li><code>Prefix</code><span class="hotkey">$</span><span class="desc"> Rename current session.</span></li>
              <li><code>Prefix</code><span class="hotkey">?</span><span class="desc"> List key combinations.</span></li>
              <li><code>Prefix</code><span class="hotkey">,</span><span class="desc"> Rename current window.</span></li>
              <li><code>Prefix</code><span class="hotkey">w</span><span class="desc"> Windows selector.</span></li>
              <li><span class="desc">To close the current session, use:</span> <code>Prefix</code><span class="hotkey">:</span> <code> kill-session</code></li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- Panes -->
    <section class="section">
      <div class="section-header">
        <h2>Panes</h2>
        <span class="tag">Split the terminal and move between panes</span>
      </div>
      <div class="section-body">
        <div class="grid">
          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Pane management
            </div>
            <ul class="cmd-list">
              <li><code>Prefix</code><span class="hotkey">%</span><span class="desc"> Split vertically.</span></li>
              <li><code>Prefix</code><span class="hotkey">"</span><span class="desc"> Split horitzontally.</span></li>
              <li><code>Prefix</code><span class="hotkey">o</span><span class="desc"> Go to the next pane.</span></li>
              <li><code>Prefix</code><span class="hotkey">;</span><span class="desc"> Toggle between the last two panes.</span></li>
              <li><code>Prefix</code><span class="hotkey">{ }</span><span class="desc"> Swap left/right pane.</span></li>
              <li><code>Prefix</code><span class="hotkey">q</span><span class="desc"> Show pane numbers.</span></li>
              <li><code>Prefix</code><span class="hotkey">z</span><span class="desc"> Zoom in pane.</span></li>
              <li><code>Prefix</code><span class="hotkey">x</span><span class="desc"> Close current pane.</span></li>
              <li><code>Prefix</code><span class="hotkey">!</span><span class="desc"> Promotes current pane to window.</span></li>
            </ul>
          </div>
          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Movement and advanced options
            </div>
            <ul class="cmd-list">
              <li><code>Prefix</code><span class="hotkey">↑/↓/←/→</span><span class="desc"> Move pane focus.</span></li>
              <li><code>Prefix</code><span class="hotkey">Alt + ↑/↓/←/→</span><span class="desc"> Resize pane.</span></li>
              <li><code>join-pane -s 2.1 -t 1.0</code> <span class="desc">Join pane 2.1 to 1.0.</span></li>
              <li><code>break-pane</code> <span class="desc">Convert pane to window.</span></li>
              <li><code>swap-pane -[UDLR]</code> <span class="desc">Exchange pane address.</span></li>
              <li><code>select-pane -t :.+</code> <span class="desc">Select next pane.</span></li>
              <li><code>set-window-option synchronize-panes on</code> <span class="desc">Synchronize panes.</span></li>
              <li><code>display-message '#P'</code> <span class="desc">Show pane index.</span></li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- Windows and tabs -->
    <section class="section">
      <div class="section-header">
        <h2>Windows and tabs</h2>
        <span class="tag">Organize work in multiple views</span>
      </div>
      <div class="section-body">
        <div class="grid">
          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Window commands
            </div>
            <ul class="cmd-list">
              <li><code>rename-window <span class="highlight">new-name</span></code><span class="desc">Rename current window.</span></li>
              <li><code>swap-window -t 2</code> <span class="desc">Swap with window 2.</span></li>
              <li><code>move-window -t 3</code> <span class="desc">Move to window 3.</span></li>
              <li><code>link-window -s src -t dst</code> <span class="desc">Link window between sessions.</span></li>
              <li><code>unlink-window</code> <span class="desc">Unlink window.</span></li>
              <li><code>kill-window</code> <span class="desc">Close window.</span></li>
              <li><code>display-message '#W'</code> <span class="desc">Show window name.</span></li>
            </ul>
          </div>
          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Window shortcuts using the prefix
            </div>
            <ul class="cmd-list">
              <li><code>Prefix</code><span class="hotkey">c</span><span class="desc"> Create new window.</span></li>
              <li><code>Prefix</code><span class="hotkey">p</span><span class="desc"> Previous window.</span></li>
              <li><code>Prefix</code><span class="hotkey">n</span><span class="desc"> Next window.</span></li>
              <li><code>Prefix</code><span class="hotkey">&lt;0-9&gt;</span><span class="desc"> Select window by number.</span></li>
              <li><code>Prefix</code><span class="hotkey">&amp;</span><span class="desc"> Delete current window.</span></li>
              <li><code>Prefix</code><span class="hotkey">.</span><span class="desc"> Move window.</span></li>
              <li><code>Prefix</code><span class="hotkey">f</span><span class="desc"> Search window by name.</span></li>
              <li><code>Prefix</code><span class="hotkey">l</span><span class="desc"> Last window used.</span></li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- Copy and move -->
    <section class="section">
      <div class="section-header">
        <h2>Copy and scroll mode</h2>
        <span class="tag">History and text selection</span>
      </div>
      <div class="section-body">
        <div class="grid">
          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Copy buffers and configuration
            </div>
            <ul class="cmd-list">
              <li><code>:show-buffer</code> <span class="desc">Mostrar buffer principal.</span></li>
              <li><code>:list-buffers</code> <span class="desc">List all buffers.</span></li>
              <li><code>:save-buffer file</code> <span class="desc">Save buffer to file.</span></li>
              <li><code>:delete-buffer -b N</code> <span class="desc">Delete buffer N.</span></li>
              <li><code>set -g mode-keys vi</code> <span class="desc">Use Vim keys in copy mode.</span></li>
            </ul>
          </div>
          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Copy-mode shortcuts
            </div>
            <ul class="cmd-list">
              <li><code>Prefix</code><span class="hotkey">[</span><span class="desc"> Enter copy mode.</span></li>
              <li><code>q</code> <span class="desc">Exit copy mode.</span></li>
              <li><code>Space</code> <span class="desc">Start selection.</span></li>
              <li><code>Enter</code> <span class="desc">Copy selection.</span></li>
              <li><code>Page Up</code> / <code>Page Down</code> <span class="desc">Scroll up/down.</span></li>
              <li><code>/</code> <span class="desc">Search ahead.</span></li>
              <li><code>?</code> <span class="desc">Search back.</span></li>
              <li><code>n</code> / <code>N</code> <span class="desc">Next/previous search result.</span></li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- Resize and layout -->
    <section class="section">
      <div class="section-header">
        <h2>Resize and layout</h2>
        <span class="tag">Predefined layouts and quick settings</span>
      </div>
      <div class="section-body">
        <div class="grid">
          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Layouts
            </div>
            <ul class="cmd-list">
              <li><code>select-layout even-horizontal</code> <span class="desc">Horizontally distributed panes.</span></li>
              <li><code>select-layout even-vertical</code> <span class="desc">Vertically distributed panes.</span></li>
              <li><code>select-layout main-horizontal</code> <span class="desc">Main pane above, others below.</span></li>
              <li><code>select-layout main-vertical</code> <span class="desc">Main pane on the left.</span></li>
              <li><code>select-layout tiled</code> <span class="desc">All mosaic panes.</span></li>
            </ul>
          </div>
          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Layout shortcuts
            </div>
            <ul class="cmd-list">
              <li><code>Prefix</code><span class="hotkey">Alt + ↑/↓/←/→</span><span class="desc"> Resize pane.</span></li>
              <li><code>Prefix</code><span class="hotkey">space</span><span class="desc"> Change pane layout.</span></li>
              <li><code>Prefix</code><span class="hotkey">q</span><span class="desc"> Show pane numbers.</span></li>
              <li><code>Prefix</code><span class="hotkey">{ }</span><span class="desc"> Swap left/right panes.</span></li>
              <li><code>Prefix</code><span class="hotkey">z</span><span class="desc"> Active pane zoom/unzoom.</span></li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- Mouse -->
    <section class="section">
      <div class="section-header">
        <h2>Mouse support</h2>
        <span class="tag">When you want to use the mouse</span>
      </div>
      <div class="section-body">
        <div class="grid">
          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Configuration
            </div>
            <ul class="cmd-list">
              <li><code>set -g mouse on</code> <span class="desc">Enable mouse to resize, select, etc.</span></li>
              <li><code>set -g mouse off</code> <span class="desc">Disable mouse support.</span></li>
              <li><code>setw -g mode-mouse on</code> <span class="desc">Enable mouse in copy mode (tmux &lt;2.1).</span></li>
            </ul>
          </div>
          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Practical use
            </div>
            <ul class="cmd-list">
              <li>Drag the border to resize the pane.</li>
              <li>Click on the pane/window to focus.</li>
              <li>Scroll the mouse wheel to view the history.</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- Automation and scripting -->
    <section class="section">
      <div class="section-header">
        <h2>Automation and scripting</h2>
        <span class="tag">Sessions prepared with a single command</span>
      </div>
      <div class="section-body">
        <div class="grid">
          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Useful commands for scripts
            </div>
            <ul class="cmd-list">
              <li><code>tmux new-session -d -s MiSesion</code> <span class="desc">Decoupled session.</span></li>
              <li><code>tmux send-keys -t MiSesion 'top' Enter</code> <span class="desc">Send command to pane.</span></li>
              <li><code>tmux new-window -t MiSesion:1 -n 'htop'</code> <span class="desc">Create window called htop.</span></li>
              <li><code>tmux split-window -h -t MiSesion:1</code> <span class="desc">Split window horizontally.</span></li>
              <li><code>tmux select-pane -t MiSesion:1.0</code> <span class="desc">Select pane 0 in window 1.</span></li>
            </ul>
          </div>
          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Script example
            </div>
            <pre>
# Script example
tmux new-session -d -s dev
tmux new-window -t dev:1 -n code
tmux send-keys -t dev:1 'vim .' C-m
tmux split-window -h -t dev:1
tmux send-keys -t dev:1.1 'npm start' C-m
tmux attach -t dev
            </pre>
          </div>
        </div>
      </div>
    </section>

    <!-- Configuration -->
    <section class="section">
      <div class="section-header">
        <h2>Configuration file (~/.tmux.conf)</h2>
        <span class="tag">Shortcuts and recommended options</span>
      </div>
      <div class="section-body">
        <pre>
# Remapping prefix
set-option -g prefix C-a
unbind C-b
bind C-a send-prefix

# Mouse support
set -g mouse on

# Vim keys in copy mode
setw -g mode-keys vi

# 256-color support
set -g default-terminal "screen-256color"

# Useful titles
set -g set-titles on
set -g set-titles-string "#S:#I.#P #W"

# Shortcuts for splitting panes
bind | split-window -h
bind - split-window -v

# Reload configuration
bind r source-file ~/.tmux.conf \; display-message "Configuration reloaded!"
        </pre>
      </div>
    </section>

    <!-- Tips and troubleshooting -->
    <section class="section">
      <div class="section-header">
        <h2>Tips and troubleshooting</h2>
        <span class="tag">Common troubleshooting issues</span>
      </div>
      <div class="section-body">
        <ul class="cmd-list">
          <li><span class="highlight">tmux not responding to keystrokes?</span><span class="desc">It can be in a nested tmux session. The default prefix is <code>Ctrl+b</code> try <code>Ctrl+b</code> twice.</span></li>
          <li><span class="highlight">Copy/paste not working?</span><span class="desc">Use <code>set -g mouse on</code> and try Shift + Mouse or enable clipboard with plugin <code>tmux-yank</code>.</span></li>
          <li><span class="highlight">Wrong terminal colors?</span><span class="desc">Check <code>set -g default-terminal "screen-256color"</code> in <code>~/.tmux.conf</code> and in your terminal emulator.</span></li>
          <li><span class="highlight">Share tmux?</span><span class="desc">Run <code>tmux attach -t session</code> from multiple terminals (same user).</span></li>
        </ul>
      </div>
    </section>

    <!-- Plugins y recursos -->
    <section class="section">
      <div class="section-header">
        <h2>Plugins and more resources</h2>
        <span class="tag">Extend tmux and keep learning</span>
      </div>
      <div class="section-body">
        <ul class="cmd-list">
          <li><a class="inline-link" href="https://github.com/tmux-plugins/tpm">TPM (tmux plugin manager)</a> <span class="desc">Easy plugin management.</span></li>
          <li><a class="inline-link" href="https://github.com/tmux-plugins/tmux-sensible">tmux-sensible</a> <span class="desc">Better default settings.</span></li>
          <li><a class="inline-link" href="https://github.com/tmux-plugins/tmux-resurrect">tmux-resurrect</a> <span class="desc">Restore tmux sessions.</span></li>
          <li><a class="inline-link" href="https://github.com/tmux-plugins/tmux-continuum">tmux-continuum</a> <span class="desc">Continuous saving.</span></li>
          <li><a class="inline-link" href="https://github.com/tmux-plugins/tmux-yank">tmux-yank</a> <span class="desc">Clipboard integration.</span></li>
          <li><a class="inline-link" href="https://github.com/tmux/tmux/wiki">Official tmux Wiki</a></li>
          <li><a class="inline-link" href="https://leanpub.com/the-tao-of-tmux/read">The Tao of tmux (free book)</a></li>
          <li><a class="inline-link" href="https://tmuxcheatsheet.com/">tmuxcheatsheet.com</a></li>
       </ul>
      </div>
    </section>
  </main>
</div>
