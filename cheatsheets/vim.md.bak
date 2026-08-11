---
title: Vim Cheat Sheet by Mode
description: A quick Vim reference organized by Normal, Insert, Command-line, and Visual modes.
---

# Vim Cheat Sheet by Mode

Organized in the order the modes are commonly used: **Normal**, **Insert**, **Command-line**, and **Visual**.

[← Back to the dashboard](/#cheat-sheets)

## Vim Modes

- `Esc` — Normal mode
- `i` — Insert mode
- `:` — Command-line mode
- `v` — Visual mode

## Normal Mode (`Esc`)

*The main mode for navigating and editing.*

> **Key idea:** Normal mode is used to navigate, delete, copy, and combine motions with actions. You can always return to this mode by pressing `Esc`.

### Basic movement within a file

- `h j k l` — Move the cursor left, down, up, and right.
- `0` — Go to the beginning of the line.
- `^` — Go to the first non-blank character on the line.
- `$` — Go to the end of the line.
- `w` — Go to the beginning of the next word.
- `b` — Go to the beginning of the previous word.
- `e` — Go to the end of the current word.
- `gg` — Go to the beginning of the file.
- `G` — Go to the end of the file.
- `nG` — Go to line *n*.

### Moving by blocks and screens

- `{` / `}` — Go to the previous or next paragraph.
- `%` — Jump to the matching parenthesis or bracket.
- `Ctrl + u` — Move up half a screen.
- `Ctrl + d` — Move down half a screen.
- `Ctrl + b` / `Ctrl + f` — Move up or down a full screen.
- `H` — Position the cursor at the top of the screen.
- `M` — Position the cursor in the middle of the screen.
- `L` — Position the cursor at the bottom of the screen.

### Quick editing from Normal mode

- **Basic operators:** `d` deletes, `c` changes, and `y` copies. Each operator can be combined with a motion.
- `d{motion}` — Delete using a motion; for example, `dw`, `d$`, `d0`, or `d3w`.
- `c{motion}` — Change the text covered by a motion and enter Insert mode; for example, `cw` or `c$`.
- `y{motion}` — Copy using a motion; for example, `yw`, `y$`, or `yap` for a complete paragraph.
- `dd` — Delete the entire line.
- `yy` — Copy the entire line.
- `cc` — Change the entire line and enter Insert mode.
- `D` / `C` — Delete or change from the cursor to the end of the line; equivalent to `d$` and `c$`.
- `dj` / `dk` — Delete the current line and the next or previous line.
- `dG` — Delete from the current line to the end of the file.
- `dgg` — Delete from the current line to the beginning of the file.
- `ndd` — Delete *n* lines; for example, `5dd`.
- `xp` — Swap two characters by quickly cutting and pasting.
- `s` — Delete the character under the cursor and enter Insert mode.
- `S` — Delete the entire line and enter Insert mode, similar to `cc`.
- `r` — Replace a single character without entering Insert mode.
- `~` — Toggle the case of the character under the cursor.
- `gU{motion}` / `gu{motion}` — Convert text to uppercase or lowercase using a motion; for example, `gUw`.
- `u` — Undo the last action.
- `Ctrl + r` — Redo the action that was undone.
- `.` — Repeat the last complete action; this is essential for fast editing.

### Copying, pasting, and indentation

- `yy` — Copy the entire line.
- `p` — Paste after the cursor or line.
- `P` — Paste before the cursor or line.
- `gp` — Paste and leave the cursor at the end of the inserted text.
- `J` — Join the current line with the next line.
- `>>` — Increase the indentation of the current line.
- `<<` — Decrease the indentation of the current line.
- `>{motion}` / `<{motion}` — Increase or decrease indentation over the specified range; for example, `>ap`.
- `=` or `={motion}` — Automatically indent the current line or range; for example, `=ap`.

### Searching from Normal mode

- `/text` — Search forward.
- `?text` — Search backward.
- `n` / `N` — Go to the next or previous match.
- `*` — Search forward for the word under the cursor.
- `#` — Search backward for the word under the cursor.

### Windows, tabs, and buffers

- `Ctrl + w s` — Split the window horizontally.
- `Ctrl + w v` — Split the window vertically.
- `Ctrl + w w` — Switch to the next window.
- `Ctrl + w h/j/k/l` — Move between windows.
- `:tabnew` — Create a new tab with an empty buffer.
- `gt` / `gT` — Go to the next or previous tab.
- `:ls` — List open buffers.
- `:b n` — Go to buffer number *n*.

## Insert Mode (`i`)

*For typing text and making direct changes.*

> **Key idea:** Use Insert mode only to type text. Then return to Normal mode with `Esc` so you can navigate and edit without using the mouse.

### Entering Insert mode

- `i` — Insert before the cursor.
- `a` — Insert after the cursor.
- `I` — Insert at the beginning of the line.
- `A` — Insert at the end of the line.
- `o` — Create a new line below and enter Insert mode.
- `O` — Create a new line above and enter Insert mode.
- `cc` — Change the entire line and enter Insert mode.
- `cw` — Change the word and enter Insert mode.

### Leaving Insert mode and useful shortcuts

- `Esc` — Return to Normal mode.
- `Ctrl + h` — Delete the previous character.
- `Ctrl + w` — Delete the previous word.
- `Ctrl + u` — Delete back to the beginning of the line.
- `Ctrl + r {register}` — Paste the contents of a register.
- `Ctrl + n` / `Ctrl + p` — Complete using the next or previous matching word.

## Command-line Mode (`:`)

*For saving, quitting, searching, and configuring Vim.*

> **Key idea:** From Normal mode, press `:` to open the command line. You can then use complete Vim commands such as `:w`, `:q`, and `:help`.

### Saving and quitting

- `:w` — Save the file.
- `:w new_name` — Save as a new file.
- `:q` — Quit if there are no unsaved changes.
- `:q!` — Quit and discard changes.
- `:wq` or `:x` — Save and quit.
- `ZZ` — Save and quit from Normal mode.
- `ZQ` — Quit without saving from Normal mode.

### Search and replace

- `:%s/old/new/g` — Replace all occurrences in the file.
- `:%s/old/new/gc` — Replace all occurrences in the file with confirmation.
- `:s/old/new/` — Replace only on the current line.
- `:'<,'>s/old/new/g` — Replace within a Visual selection.
- `:noh` — Clear search highlighting.

### Working with files, buffers, and tabs

- `:e file` — Edit or open a file.
- `:bnext` / `:bprev` — Go to the next or previous buffer.
- `:bd` — Close the current buffer.
- `:tabnew` — Create a new tab.
- `:tabclose` — Close the current tab.
- `:split` / `:vsplit` — Split the window horizontally or vertically.

### Quick configuration options

- `:set number` — Display line numbers.
- `:set relativenumber` — Display relative line numbers.
- `:set hlsearch` — Highlight search results.
- `:set expandtab` — Convert tabs to spaces.
- `:set tabstop=4` — Set the displayed width of a tab.
- `:set shiftwidth=4` — Set the number of spaces used for indentation.
- `:help topic` — Open help for a topic; for example, `:help motion.txt`.

### Compact `.vimrc` example

```vim
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
nnoremap <Space> :nohlsearch<CR>
nnoremap <leader>w :w<CR>
```

### Command-line tips

- **History:** use the Up and Down arrow keys to cycle through previous commands.
- **Ranges:** commands can use ranges; for example, `:10,20s/old/new/g`.
- **Completion:** press `Tab` to complete command and file names.
- **Save as administrator:** if you forgot to open the file with `sudo` and do not have permission to save it, use `:w !sudo tee %` to save your changes without leaving Vim.
- **Delete lines containing `KSWM`:** to delete every line containing `KSWM`, ignoring case, use `:g/KSWM\c/d`.

## Visual Mode (`v`)

*For selecting text and then copying, deleting, or modifying it.*

> **Key idea:** In Visual mode, select some text and then apply a command—for example, `d` to delete, `y` to copy, or `>` to indent.

### Selection types

- `v` — Select by character.
- `V` — Select entire lines.
- `Ctrl + v` — Select a rectangular block of columns.
- `Esc` — Leave Visual mode.
- `o` — Switch the active end of the selection.

### Actions on a selection

- `y` — Copy the selection.
- `d` — Delete the selection.
- `c` — Change the selection and enter Insert mode.
- `>` / `<` — Increase or decrease indentation.
- `=` — Automatically indent the selection.
- `gU` / `gu` — Convert the selection to uppercase or lowercase.

### Bulk editing with Visual Block mode

```vim
" Insert text at the beginning of multiple lines
Ctrl+v      " Enter Visual Block mode
j j j       " Move down to select multiple lines
I           " Insert at the beginning of the block
#           " Type the desired text
Esc         " Vim will repeat the change on each selected line
```

### Guided replacement within a selection

```vim
" Select the desired range in Visual mode
:'<,'>s/old/new/gc

" Replaces text only within the selection, with confirmation
```
