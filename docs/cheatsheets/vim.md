---
title: Vim Cheat Sheet
description: A visual Vim reference organized by mode.
hide:
  - navigation
  - toc
---

<div class="cheatsheet-page cheatsheet-page--vim">
<main class="outer">
    <div class="page-header">
      <div class="page-title">
        <h1>Vim Cheat Sheet by Mode</h1>
        <p>Organized in the same order of daily use, Normal, Insert, Command Line, Visual.</p>
      </div>
      <div class="header-right">
        <a href="/#cheat-sheets" class="back-button">Back to the dashboard</a>
        <div class="mode-pill-row">
          <div class="mode-pill"><span class="key">Esc</span><span>Normal Mode</span></div>
          <div class="mode-pill"><span class="key">i</span><span>Insert Mode</span></div>
          <div class="mode-pill"><span class="key">:</span><span>Command-line Mode</span></div>
          <div class="mode-pill"><span class="key">v</span><span>Visual Mode</span></div>
        </div>
      </div>
    </div>

    <!-- NORMAL MODE -->
    <section class="section" id="normal">
      <div class="section-header">
        <h2>Normal Mode (Esc)</h2>
        <span class="tag">Main mode for browsing and editing</span>
      </div>
      <div class="section-body">
        <div class="note">
          <div class="note-icon">N</div>
          <div>
            <strong>Key idea.</strong>
            In normal mode you navigate, delete, copy and combine movements with actions.
            You can always return to this mode with <code>Esc</code>.
          </div>
        </div>

        <div class="grid">
          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Basic movement in the file</div>
            <ul class="cmd-list">
              <li><code>h j k l</code><span class="desc">Move the cursor, left, down, up, right.</span></li>
              <li><code>0</code> <span class="desc">Go to the beginning of the line.</span></li>
              <li><code>^</code> <span class="desc">Go to the first non-space character.</span></li>
              <li><code>$</code> <span class="desc">Go to the end of the line.</span></li>
              <li><code>w</code> <span class="desc">Next word start.</span></li>
              <li><code>b</code> <span class="desc">Beginning of previous word.</span></li>
              <li><code>e</code> <span class="desc">End of the current word.</span></li>
              <li><code>gg</code> <span class="desc">Go to the beginning of the file.</span></li>
              <li><code>G</code> <span class="desc">Go to the end of the file.</span></li>
              <li><code>nG</code> <span class="desc">go to line <span class="highlight">n</span>.</span></li>
            </ul>
          </div>

          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Movement by blocks and screens</div>
            <ul class="cmd-list">
              <li><code>{</code> / <code>}</code><span class="desc">Previous or next paragraph.</span></li>
              <li><code>%</code><span class="desc">Jump to the pair of parentheses or brackets.</span></li>
              <li><code>Ctrl + u</code><span class="desc">Media pantalla arriba.</span></li>
              <li><code>Ctrl + d</code><span class="desc">Media pantalla abajo.</span></li>
              <li><code>Ctrl + b</code> / <code>Ctrl + f</code><span class="desc">Full page up or down.</span></li>
              <li><code>H</code> <span class="desc">Position the cursor at the top of the screen.</span></li>
              <li><code>M</code> <span class="desc">Position cursor in the center of the screen.</span></li>
              <li><code>L</code> <span class="desc">Position the cursor at the bottom of the screen.</span></li>
            </ul>
          </div>

          <!-- COMPLETE QUICK EDITING -->
          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Quick edit from normal mode</div>
            <ul class="cmd-list">
              <li><span class="highlight">Basic operators</span><span class="desc"><code>d</code> delete, <code>c</code> cambiar, <code>y</code> copy, always combined with a movement.</span></li>
              <li><code>d{mov}</code> <span class="desc">Delete using a movement, for example <code>dw</code>, <code>d$</code>, <code>d0</code>, <code>d3w</code>.</span></li>
              <li><code>c{mov}</code> <span class="desc">Change the text covered by the move and enter insert, for example <code>cw</code>, <code>c$</code>.</span></li>
              <li><code>y{mov}</code> <span class="desc">Copy using a motion, for example <code>yw</code>, <code>y$</code>, <code>yap</code> full paragraph.</span></li>
              <li><code>dd</code> <span class="desc">Delete entire line.</span></li>
              <li><code>yy</code> <span class="desc">Copy entire line.</span></li>
              <li><code>cc</code> <span class="desc">Change entire line and enter insert.</span></li>
              <li><code>D</code> / <code>C</code> <span class="desc">Delete or change from the cursor to the end of the line, equivalent to <code>d$</code> y <code>c$</code>.</span></li>
              <li><code>dj</code> / <code>dk</code> <span class="desc">Delete current line and the next or the previous one.</span></li>
              <li><code>dG</code> <span class="desc">Delete from the current line to the end of the file.</span></li>
              <li><code>dgg</code> <span class="desc">Delete from the current line to the beginning of the file.</span></li>
              <li><code>n dd</code> <span class="desc">Delete <span class="highlight">n</span> lines, for example <code>5dd</code>.</span></li>
              <li><code>xp</code> <span class="desc">Swap two characters, quickly cut and paste.</span></li>
              <li><code>s</code> <span class="desc">Delete character under the cursor and enter insert.</span></li>
              <li><code>S</code> <span class="desc">Delete entire line and enter insert, similar to <code>cc</code>.</span></li>
              <li><code>r</code> <span class="desc">Replace a single character without entering insert.</span></li>
              <li><code>~</code> <span class="desc">Reverse upper or lower case of the character under the cursor.</span></li>
              <li><code>gU{mov}</code> / <code>gu{mov}</code> <span class="desc">Convert to upper or lower case using a move, for example <code>gUw</code>.</span></li>
              <li><code>u</code> <span class="desc">Undo last action.</span></li>
              <li><code>Ctrl + r</code> <span class="desc">Redo the undone action.</span></li>
              <li><code>.</code> <span class="desc">Repeat the last complete action, key to fast editing.</span></li>
            </ul>
          </div>

          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Copy, paste and indent</div>
            <ul class="cmd-list">
              <li><code>yy</code> <span class="desc">Copy the entire line.</span></li>
              <li><code>p</code> <span class="desc">Paste after the cursor or line.</span></li>
              <li><code>P</code> <span class="desc">Paste before the cursor or line.</span></li>
              <li><code>gp</code> <span class="desc">Paste and leave the cursor at the end of the pasted text.</span></li>
              <li><code>J</code> <span class="desc">Join the current line with the next one.</span></li>
              <li><code>&gt;&gt;</code> <span class="desc">Increase line indentation.</span></li>
              <li><code>&lt;&lt;</code> <span class="desc">Decrease line indentation.</span></li>
              <li><code>&gt;{mov}</code> / <code>&lt;{mov}</code> <span class="desc">Increase or decrease indentation in the indicated range, e.g. <code>&gt;ap</code>.</span></li>
              <li><code>=</code> o <code>={mov}</code> <span class="desc">Auto indentation of the line or range, for example <code>=ap</code>.</span></li>
            </ul>
          </div>

          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Search from normal mode</div>
            <ul class="cmd-list">
              <li><code>/text</code> <span class="desc">Search down.</span></li>
              <li><code>?text</code> <span class="desc">Search up.</span></li>
              <li><code>n</code> / <code>N</code> <span class="desc">Next or previous match.</span></li>
              <li><code>*</code> <span class="desc">Search the word under the down cursor.</span></li>
              <li><code>#</code> <span class="desc">Search the word under the cursor up.</span></li>
            </ul>
          </div>

          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Windows, tabs and buffers</div>
            <ul class="cmd-list">
              <li><code>Ctrl + w s</code> <span class="desc">Split window horizontally.</span></li>
              <li><code>Ctrl + w v</code> <span class="desc">Split window vertically.</span></li>
              <li><code>Ctrl + w w</code> <span class="desc">Switch to the next window.</span></li>
              <li><code>Ctrl + w h/j/k/l</code> <span class="desc">Moverse entre ventanas.</span></li>
              <li><code>:tabnew</code> <span class="desc">New tab with an empty buffer.</span></li>
              <li><code>gt</code> / <code>gT</code> <span class="desc">Next or previous tab.</span></li>
              <li><code>:ls</code> <span class="desc">List open buffers.</span></li>
              <li><code>:b n</code> <span class="desc">Go to buffer number <span class="highlight">n</span>.</span></li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- INSERT MODE -->
    <section class="section" id="insert">
      <div class="section-header">
        <h2>Insert Mode (i)</h2>
        <span class="tag">To enter text and make direct changes</span>
      </div>
      <div class="section-body">
        <div class="note">
          <div class="note-icon">I</div>
          <div>
            <strong>Key idea.</strong>
            Use insert mode only to type text, then return to normal mode with <code>Esc</code> to move and edit without touching the mouse.
          </div>
        </div>

        <div class="grid">
          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Enter insert mode</div>
            <ul class="cmd-list">
              <li><code>i</code> <span class="desc">Insertar antes del cursor.</span></li>
              <li><code>a</code> <span class="desc">Insert after the cursor.</span></li>
              <li><code>I</code> <span class="desc">Insert at the beginning of the line.</span></li>
              <li><code>A</code> <span class="desc">Insert at the end of the line.</span></li>
              <li><code>o</code> <span class="desc">Create new line below and insert.</span></li>
              <li><code>O</code> <span class="desc">Create new line above and insert.</span></li>
              <li><code>cc</code> <span class="desc">Change entire line and enter insert.</span></li>
              <li><code>cw</code> <span class="desc">Cambiar palabra y entrar en insertar.</span></li>
            </ul>
          </div>

          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Exit insert and useful shortcuts</div>
            <ul class="cmd-list">
              <li><code>Esc</code> <span class="desc">Return to normal mode.</span></li>
              <li><code>Ctrl + h</code> <span class="desc">Delete previous character.</span></li>
              <li><code>Ctrl + w</code> <span class="desc">Delete previous word.</span></li>
              <li><code>Ctrl + u</code> <span class="desc">Delete until start of line.</span></li>
              <li><code>Ctrl + r {register}</code> <span class="desc">Paste content from a record.</span></li>
              <li><code>Ctrl + n</code> / <code>Ctrl + p</code> <span class="desc">Autocompletar palabras siguientes o anteriores.</span></li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- COMMAND LINE -->
    <section class="section" id="command-line">
      <div class="section-header">
        <h2>Command-line Mode (:)</h2>
        <span class="tag">To save, exit, search, configure.</span>
      </div>
      <div class="section-body">
        <div class="note">
          <div class="note-icon">:</div>
          <div>
            <strong>Key idea.</strong>
            From normal mode, press <code>:</code> to open the command line, there you can use any full Vim command, e.g. <code>:w</code>, <code>:q</code>, <code>:help</code>.
          </div>
        </div>

        <div class="grid">
          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Save and exit</div>
            <ul class="cmd-list">
              <li><code>:w</code> <span class="desc">Save file.</span></li>
              <li><code>:w nuevo_nombre</code> <span class="desc">Save as a new file.</span></li>
              <li><code>:q</code> <span class="desc">Salir si no hay cambios pendientes.</span></li>
              <li><code>:q!</code> <span class="desc">Salir descartando cambios.</span></li>
              <li><code>:wq</code> o <code>:x</code> <span class="desc">Save and exit.</span></li>
              <li><code>ZZ</code> <span class="desc">Save and exit, shortcut from normal mode.</span></li>
              <li><code>ZQ</code> <span class="desc">Exit without saving, shortcut from normal mode.</span></li>
            </ul>
          </div>

          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Global Search and Replace</div>
            <ul class="cmd-list">
              <li><code>:%s/viejo/nuevo/g</code> <span class="desc">Replace throughout the file.</span></li>
              <li><code>:%s/viejo/nuevo/gc</code> <span class="desc">Replace in entire file with commit.</span></li>
              <li><code>:s/viejo/nuevo/</code> <span class="desc">Replace only on the current line.</span></li>
              <li><code>:'&lt;,'&gt;s/viejo/nuevo/g</code> <span class="desc">Replace within a visual selection.</span></li>
              <li><code>:noh</code> <span class="desc">Remove search highlighting.</span></li>
            </ul>
          </div>

          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Work with files, buffers and tabs</div>
            <ul class="cmd-list">
              <li><code>:e file</code> <span class="desc">Edit or open a file.</span></li>
              <li><code>:bnext</code> / <code>:bprev</code> <span class="desc">Next or previous buffer.</span></li>
              <li><code>:bd</code> <span class="desc">Close the current buffer.</span></li>
              <li><code>:tabnew</code> <span class="desc">Create new tab.</span></li>
              <li><code>:tabclose</code> <span class="desc">Close current tab.</span></li>
              <li><code>:split</code> / <code>:vsplit</code> <span class="desc">Split window horizontally or vertically.</span></li>
            </ul>
          </div>

          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Useful configuration options</div>
            <ul class="cmd-list">
              <li><code>:set number</code> <span class="desc">Show line numbers.</span></li>
              <li><code>:set relativenumber</code> <span class="desc">Relative line numbers.</span></li>
              <li><code>:set hlsearch</code> <span class="desc">Highlight search results.</span></li>
              <li><code>:set expandtab</code> <span class="desc">Convertir tab en espacios.</span></li>
              <li><code>:set tabstop=4</code> <span class="desc">Visible tab size.</span></li>
              <li><code>:set shiftwidth=4</code> <span class="desc">Espacios usados al sangrar.</span></li>
              <li><code>:help tema</code> <span class="desc">Open help for a topic, for example <code>:help motion.txt</code>.</span></li>
            </ul>
          </div>

          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Ejemplo compacto de .vimrc</div>
            <pre>
" Recommended basic configuration
set number
set relativenumber
set tabstop=4
set shiftwidth=4
set expandtab
set smartindent
set hlsearch
set incsearch
set clipboard=unnamedplus
set mouse=a

" Useful shortcuts
nnoremap &lt;Space&gt; :nohlsearch&lt;CR&gt;
nnoremap &lt;leader&gt;w :w&lt;CR&gt;
            </pre>
          </div>

          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Command line tips</div>
            <ul class="cmd-list">
              <li><span class="highlight">History</span><span class="desc">Use the up and down arrows to step through previous commands.</span></li>
              <li><span class="highlight">Ranges</span><span class="desc">You can use ranges, for example <code>:10,20s/old/new/g</code>.</span></li>
              <li><span class="highlight">Completion</span><span class="desc">Use <code>Tab</code> to complete command and file names.</span></li>
              <li><span class="highlight">Save as administrator</span><span class="desc">If you forgot to open the file with <code>sudo</code> and don't have permission to save it, use <code>:w !sudo tee %</code> to save changes without leaving Vim.</span></li>
              <li><span class="highlight">Delete lines containing KSWM</span><span class="desc">Delete every line in the file containing KSWM, kswm, etc.: <code>:g/KSWM\c/d</code></span></li>
           </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- VISUAL MODE -->
    <section class="section" id="visual">
      <div class="section-header">
        <h2>Visual Mode (v)</h2>
        <span class="tag">Select text to copy, delete or modify</span>
      </div>
      <div class="section-body">
        <div class="note">
          <div class="note-icon">V</div>
          <div>
            <strong>Key idea.</strong>
            In visual mode select text, then apply a command, e.g. <code>d</code> to delete, <code>y</code> to copy, <code>&gt;</code> to bleed.
          </div>
        </div>

        <div class="grid">
          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Selection types</div>
            <ul class="cmd-list">
              <li><code>v</code><span class="desc">Select by character.</span></li>
              <li><code>V</code><span class="desc">Select entire lines.</span></li>
              <li><code>Ctrl + v</code><span class="desc">Select a rectangular block of columns.</span></li>
              <li><code>Esc</code><span class="desc">Exit Visual mode.</span></li>
              <li><code>o</code><span class="desc">Switch the active end of the selection.</span></li>
          </ul>
          </div>

          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Actions on selection</div>
            <ul class="cmd-list">
              <li><code>y</code> <span class="desc">Copy the selection.</span></li>
              <li><code>d</code> <span class="desc">Clear the selection.</span></li>
              <li><code>c</code> <span class="desc">Change the selection and go to insert.</span></li>
              <li><code>&gt;</code> / <code>&lt;</code> <span class="desc">Increase or decrease indentation.</span></li>
              <li><code>=</code> <span class="desc">Auto indentation of the selection.</span></li>
              <li><code>gU</code> / <code>gu</code> <span class="desc">Convert to upper or lower case.</span></li>
            </ul>
          </div>

          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Block visual, bulk editing</div>
            <pre>
" Insert text at the start of many lines
Ctrl+v      " blockwise Visual mode
j j j       " move down to select multiple lines
I           " insert at the start of the block
#           " type the desired text
Esc         " Vim repeats the change on every selected line
            </pre>
          </div>

          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Guided replacement with selection</div>
            <pre>
" In Visual mode, select the range
:'&lt;,'&gt;s/viejo/nuevo/gc
" Replace only within the selection, with confirmation
            </pre>
          </div>
        </div>
      </div>
    </section>
  </main>
</div>
