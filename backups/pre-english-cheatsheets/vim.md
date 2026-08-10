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
        <h1>Hoja de trucos Vim por modos</h1>
        <p>Organizado en el mismo orden de uso diario, Normal, Insertar, Línea de comandos, Visual.</p>
      </div>
      <div class="header-right">
        <a href="/#cheat-sheets" class="back-button">Volver al Dashboard anterior</a>
        <div class="mode-pill-row">
          <div class="mode-pill"><span class="key">Esc</span><span>Modo Normal</span></div>
          <div class="mode-pill"><span class="key">i</span><span>Modo Insertar</span></div>
          <div class="mode-pill"><span class="key">:</span><span>Línea de comandos</span></div>
          <div class="mode-pill"><span class="key">v</span><span>Modo Visual</span></div>
        </div>
      </div>
    </div>

    <!-- MODO NORMAL -->
    <section class="section" id="normal">
      <div class="section-header">
        <h2>Modo Normal (Esc)</h2>
        <span class="tag">Modo principal para navegar y editar</span>
      </div>
      <div class="section-body">
        <div class="note">
          <div class="note-icon">N</div>
          <div>
            <strong>Idea clave.</strong>
            En modo normal se navega, se borra, se copia y se combinan movimientos con acciones.
            Siempre puede regresar a este modo con <code>Esc</code>.
          </div>
        </div>

        <div class="grid">
          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Movimiento básico en el archivo</div>
            <ul class="cmd-list">
              <li><code>h j k l</code><span class="desc">Mover el cursor, izquierda, abajo, arriba, derecha.</span></li>
              <li><code>0</code> <span class="desc">Ir al inicio de la línea.</span></li>
              <li><code>^</code> <span class="desc">Ir al primer carácter que no es espacio.</span></li>
              <li><code>$</code> <span class="desc">Ir al final de la línea.</span></li>
              <li><code>w</code> <span class="desc">Siguiente inicio de palabra.</span></li>
              <li><code>b</code> <span class="desc">Inicio de palabra anterior.</span></li>
              <li><code>e</code> <span class="desc">Final de la palabra actual.</span></li>
              <li><code>gg</code> <span class="desc">Ir al inicio del archivo.</span></li>
              <li><code>G</code> <span class="desc">Ir al final del archivo.</span></li>
              <li><code>nG</code> <span class="desc">Ir a la línea <span class="highlight">n</span>.</span></li>
            </ul>
          </div>

          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Movimiento por bloques y pantalla</div>
            <ul class="cmd-list">
              <li><code>{</code> / <code>}</code><span class="desc">Párrafo anterior o siguiente.</span></li>
              <li><code>%</code><span class="desc">Saltar al par de paréntesis o corchete.</span></li>
              <li><code>Ctrl + u</code><span class="desc">Media pantalla arriba.</span></li>
              <li><code>Ctrl + d</code><span class="desc">Media pantalla abajo.</span></li>
              <li><code>Ctrl + b</code> / <code>Ctrl + f</code><span class="desc">Página completa arriba o abajo.</span></li>
              <li><code>H</code> <span class="desc">Posicionar cursor en la parte alta de la pantalla.</span></li>
              <li><code>M</code> <span class="desc">Posicionar cursor en el centro de la pantalla.</span></li>
              <li><code>L</code> <span class="desc">Posicionar cursor en la parte baja de la pantalla.</span></li>
            </ul>
          </div>

          <!-- EDICIÓN RÁPIDA COMPLETA -->
          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Edición rápida desde modo normal</div>
            <ul class="cmd-list">
              <li><span class="highlight">Operadores básicos</span><span class="desc"><code>d</code> borrar, <code>c</code> cambiar, <code>y</code> copiar, siempre combinados con un movimiento.</span></li>
              <li><code>d{mov}</code> <span class="desc">Borrar usando un movimiento, por ejemplo <code>dw</code>, <code>d$</code>, <code>d0</code>, <code>d3w</code>.</span></li>
              <li><code>c{mov}</code> <span class="desc">Cambiar el texto cubierto por el movimiento y entrar en insertar, por ejemplo <code>cw</code>, <code>c$</code>.</span></li>
              <li><code>y{mov}</code> <span class="desc">Copiar usando un movimiento, por ejemplo <code>yw</code>, <code>y$</code>, <code>yap</code> párrafo completo.</span></li>
              <li><code>dd</code> <span class="desc">Borrar línea completa.</span></li>
              <li><code>yy</code> <span class="desc">Copiar línea completa.</span></li>
              <li><code>cc</code> <span class="desc">Cambiar línea completa y entrar en insertar.</span></li>
              <li><code>D</code> / <code>C</code> <span class="desc">Borrar o cambiar desde el cursor hasta el final de la línea, equivalente a <code>d$</code> y <code>c$</code>.</span></li>
              <li><code>dj</code> / <code>dk</code> <span class="desc">Borrar línea actual y la siguiente o la anterior.</span></li>
              <li><code>dG</code> <span class="desc">Borrar desde la línea actual hasta el final del archivo.</span></li>
              <li><code>dgg</code> <span class="desc">Borrar desde la línea actual hasta el inicio del archivo.</span></li>
              <li><code>n dd</code> <span class="desc">Borrar <span class="highlight">n</span> líneas, por ejemplo <code>5dd</code>.</span></li>
              <li><code>xp</code> <span class="desc">Intercambiar dos caracteres, cortar y pegar rápidamente.</span></li>
              <li><code>s</code> <span class="desc">Borrar carácter bajo el cursor y entrar en insertar.</span></li>
              <li><code>S</code> <span class="desc">Borrar línea completa y entrar en insertar, similar a <code>cc</code>.</span></li>
              <li><code>r</code> <span class="desc">Reemplazar un solo carácter sin entrar en insertar.</span></li>
              <li><code>~</code> <span class="desc">Invertir mayúscula o minúscula del carácter bajo el cursor.</span></li>
              <li><code>gU{mov}</code> / <code>gu{mov}</code> <span class="desc">Convertir a mayúsculas o minúsculas usando un movimiento, por ejemplo <code>gUw</code>.</span></li>
              <li><code>u</code> <span class="desc">Deshacer última acción.</span></li>
              <li><code>Ctrl + r</code> <span class="desc">Rehacer la acción deshecha.</span></li>
              <li><code>.</code> <span class="desc">Repetir la última acción completa, clave para editar rápido.</span></li>
            </ul>
          </div>

          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Copiar, pegar y sangría</div>
            <ul class="cmd-list">
              <li><code>yy</code> <span class="desc">Copiar la línea completa.</span></li>
              <li><code>p</code> <span class="desc">Pegar después del cursor o de la línea.</span></li>
              <li><code>P</code> <span class="desc">Pegar antes del cursor o de la línea.</span></li>
              <li><code>gp</code> <span class="desc">Pegar y dejar el cursor al final del texto pegado.</span></li>
              <li><code>J</code> <span class="desc">Unir la línea actual con la siguiente.</span></li>
              <li><code>&gt;&gt;</code> <span class="desc">Aumentar sangría de la línea.</span></li>
              <li><code>&lt;&lt;</code> <span class="desc">Disminuir sangría de la línea.</span></li>
              <li><code>&gt;{mov}</code> / <code>&lt;{mov}</code> <span class="desc">Aumentar o disminuir sangría en el rango indicado, por ejemplo <code>&gt;ap</code>.</span></li>
              <li><code>=</code> o <code>={mov}</code> <span class="desc">Auto sangría de la línea o del rango, por ejemplo <code>=ap</code>.</span></li>
            </ul>
          </div>

          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Búsqueda desde modo normal</div>
            <ul class="cmd-list">
              <li><code>/texto</code> <span class="desc">Buscar hacia abajo.</span></li>
              <li><code>?texto</code> <span class="desc">Buscar hacia arriba.</span></li>
              <li><code>n</code> / <code>N</code> <span class="desc">Siguiente o anterior coincidencia.</span></li>
              <li><code>*</code> <span class="desc">Buscar la palabra bajo el cursor hacia abajo.</span></li>
              <li><code>#</code> <span class="desc">Buscar la palabra bajo el cursor hacia arriba.</span></li>
            </ul>
          </div>

          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Ventanas, pestañas y buffers</div>
            <ul class="cmd-list">
              <li><code>Ctrl + w s</code> <span class="desc">Dividir ventana en horizontal.</span></li>
              <li><code>Ctrl + w v</code> <span class="desc">Dividir ventana en vertical.</span></li>
              <li><code>Ctrl + w w</code> <span class="desc">Cambiar a la siguiente ventana.</span></li>
              <li><code>Ctrl + w h/j/k/l</code> <span class="desc">Moverse entre ventanas.</span></li>
              <li><code>:tabnew</code> <span class="desc">Nueva pestaña con un buffer vacío.</span></li>
              <li><code>gt</code> / <code>gT</code> <span class="desc">Pestaña siguiente o anterior.</span></li>
              <li><code>:ls</code> <span class="desc">Listar buffers abiertos.</span></li>
              <li><code>:b n</code> <span class="desc">Ir al buffer número <span class="highlight">n</span>.</span></li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- MODO INSERTAR -->
    <section class="section" id="insert">
      <div class="section-header">
        <h2>Modo Insertar (i)</h2>
        <span class="tag">Para escribir texto y hacer cambios directos</span>
      </div>
      <div class="section-body">
        <div class="note">
          <div class="note-icon">I</div>
          <div>
            <strong>Idea clave.</strong>
            Use modo insertar solo para escribir texto, luego regrese a modo normal con <code>Esc</code> para moverse y editar sin tocar el ratón.
          </div>
        </div>

        <div class="grid">
          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Entrar en modo insertar</div>
            <ul class="cmd-list">
              <li><code>i</code> <span class="desc">Insertar antes del cursor.</span></li>
              <li><code>a</code> <span class="desc">Insertar después del cursor.</span></li>
              <li><code>I</code> <span class="desc">Insertar al inicio de la línea.</span></li>
              <li><code>A</code> <span class="desc">Insertar al final de la línea.</span></li>
              <li><code>o</code> <span class="desc">Crear nueva línea debajo e insertar.</span></li>
              <li><code>O</code> <span class="desc">Crear nueva línea encima e insertar.</span></li>
              <li><code>cc</code> <span class="desc">Cambiar línea completa y entrar en insertar.</span></li>
              <li><code>cw</code> <span class="desc">Cambiar palabra y entrar en insertar.</span></li>
            </ul>
          </div>

          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Salir de insertar y atajos útiles</div>
            <ul class="cmd-list">
              <li><code>Esc</code> <span class="desc">Volver a modo normal.</span></li>
              <li><code>Ctrl + h</code> <span class="desc">Borrar carácter anterior.</span></li>
              <li><code>Ctrl + w</code> <span class="desc">Borrar palabra anterior.</span></li>
              <li><code>Ctrl + u</code> <span class="desc">Borrar hasta inicio de línea.</span></li>
              <li><code>Ctrl + r {registro}</code> <span class="desc">Pegar contenido de un registro.</span></li>
              <li><code>Ctrl + n</code> / <code>Ctrl + p</code> <span class="desc">Autocompletar palabras siguientes o anteriores.</span></li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- LÍNEA DE COMANDOS -->
    <section class="section" id="command-line">
      <div class="section-header">
        <h2>Línea de comandos (:)</h2>
        <span class="tag">Para guardar, salir, buscar, configurar.</span>
      </div>
      <div class="section-body">
        <div class="note">
          <div class="note-icon">:</div>
          <div>
            <strong>Idea clave.</strong>
            Desde modo normal, presione <code>:</code> para abrir la línea de comandos, allí puede usar cualquier comando completo de Vim, por ejemplo <code>:w</code>, <code>:q</code>, <code>:help</code>.
          </div>
        </div>

        <div class="grid">
          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Guardar y salir</div>
            <ul class="cmd-list">
              <li><code>:w</code> <span class="desc">Guardar archivo.</span></li>
              <li><code>:w nuevo_nombre</code> <span class="desc">Guardar como un archivo nuevo.</span></li>
              <li><code>:q</code> <span class="desc">Salir si no hay cambios pendientes.</span></li>
              <li><code>:q!</code> <span class="desc">Salir descartando cambios.</span></li>
              <li><code>:wq</code> o <code>:x</code> <span class="desc">Guardar y salir.</span></li>
              <li><code>ZZ</code> <span class="desc">Guardar y salir, atajo desde modo normal.</span></li>
              <li><code>ZQ</code> <span class="desc">Salir sin guardar, atajo desde modo normal.</span></li>
            </ul>
          </div>

          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Búsqueda y reemplazo global</div>
            <ul class="cmd-list">
              <li><code>:%s/viejo/nuevo/g</code> <span class="desc">Reemplazar en todo el archivo.</span></li>
              <li><code>:%s/viejo/nuevo/gc</code> <span class="desc">Reemplazar en todo el archivo con confirmación.</span></li>
              <li><code>:s/viejo/nuevo/</code> <span class="desc">Reemplazar solo en la línea actual.</span></li>
              <li><code>:'&lt;,'&gt;s/viejo/nuevo/g</code> <span class="desc">Reemplazar dentro de una selección visual.</span></li>
              <li><code>:noh</code> <span class="desc">Quitar el resaltado de búsqueda.</span></li>
            </ul>
          </div>

          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Trabajar con archivos, buffers y pestañas</div>
            <ul class="cmd-list">
              <li><code>:e archivo</code> <span class="desc">Editar o abrir un archivo.</span></li>
              <li><code>:bnext</code> / <code>:bprev</code> <span class="desc">Buffer siguiente o anterior.</span></li>
              <li><code>:bd</code> <span class="desc">Cerrar el buffer actual.</span></li>
              <li><code>:tabnew</code> <span class="desc">Crear nueva pestaña.</span></li>
              <li><code>:tabclose</code> <span class="desc">Cerrar pestaña actual.</span></li>
              <li><code>:split</code> / <code>:vsplit</code> <span class="desc">Dividir ventana en horizontal o vertical.</span></li>
            </ul>
          </div>

          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Opciones rápidas de configuración</div>
            <ul class="cmd-list">
              <li><code>:set number</code> <span class="desc">Mostrar números de línea.</span></li>
              <li><code>:set relativenumber</code> <span class="desc">Números de línea relativos.</span></li>
              <li><code>:set hlsearch</code> <span class="desc">Resaltar resultados de búsqueda.</span></li>
              <li><code>:set expandtab</code> <span class="desc">Convertir tab en espacios.</span></li>
              <li><code>:set tabstop=4</code> <span class="desc">Tamaño de tabulación visible.</span></li>
              <li><code>:set shiftwidth=4</code> <span class="desc">Espacios usados al sangrar.</span></li>
              <li><code>:help tema</code> <span class="desc">Abrir la ayuda para un tema, por ejemplo <code>:help motion.txt</code>.</span></li>
            </ul>
          </div>

          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Ejemplo compacto de .vimrc</div>
            <pre>
" Configuración básica recomendada
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

" Atajos útiles
nnoremap &lt;Space&gt; :nohlsearch&lt;CR&gt;
nnoremap &lt;leader&gt;w :w&lt;CR&gt;
            </pre>
          </div>

          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Consejos de línea de comandos</div>
            <ul class="cmd-list">
              <li><span class="highlight">Historial</span><span class="desc">Use las flechas arriba y abajo para recorrer comandos anteriores.</span></li>
              <li><span class="highlight">Rangos</span><span class="desc">Puede usar rangos, por ejemplo <code>:10,20s/viejo/nuevo/g</code>.</span></li>
              <li><span class="highlight">Completar</span><span class="desc">Use <code>Tab</code> para completar nombres de comandos y archivos.</span></li>
              <li><span class="highlight">Guardar como administrador</span><span class="desc">Si olvidó abrir el archivo con <code>sudo</code> y no tiene permisos para guardarlo, use <code>:w !sudo tee %</code> para guardar los cambios sin salir de Vim.</span></li> 
              <li><span class="highlight">Borrar lineas que contienen KSWM</span><span class="desc">Por cada linea en el archivo que contiene KSWM, kswm... borrela: <code>:g/KSWM\c/d</code></span></li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- MODO VISUAL -->
    <section class="section" id="visual">
      <div class="section-header">
        <h2>Modo Visual (v)</h2>
        <span class="tag">Seleccionar texto para copiar, borrar o modificar</span>
      </div>
      <div class="section-body">
        <div class="note">
          <div class="note-icon">V</div>
          <div>
            <strong>Idea clave.</strong>
            En modo visual selecciona texto, luego aplica un comando, por ejemplo <code>d</code> para borrar, <code>y</code> para copiar, <code>&gt;</code> para sangrar.
          </div>
        </div>

        <div class="grid">
          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Tipos de selección</div>
            <ul class="cmd-list">
              <li><code>v</code> <span class="desc">Seleccionar por caracteres.</span></li>
              <li><code>V</code> <span class="desc">Seleccionar líneas completas.</span></li>
              <li><code>Ctrl + v</code> <span class="desc">Seleccionar un bloque rectangular de columnas.</span></li>
              <li><code>Esc</code> <span class="desc">Salir de modo visual.</span></li>
              <li><code>o</code> <span class="desc">Cambiar el extremo activo de la selección.</span></li>
            </ul>
          </div>

          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Acciones sobre la selección</div>
            <ul class="cmd-list">
              <li><code>y</code> <span class="desc">Copiar la selección.</span></li>
              <li><code>d</code> <span class="desc">Borrar la selección.</span></li>
              <li><code>c</code> <span class="desc">Cambiar la selección e ir a insertar.</span></li>
              <li><code>&gt;</code> / <code>&lt;</code> <span class="desc">Aumentar o disminuir sangría.</span></li>
              <li><code>=</code> <span class="desc">Auto sangría de la selección.</span></li>
              <li><code>gU</code> / <code>gu</code> <span class="desc">Convertir a mayúsculas o minúsculas.</span></li>
            </ul>
          </div>

          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Visual en bloque, edición masiva</div>
            <pre>
" Insertar texto al inicio de muchas líneas
Ctrl+v      " modo visual en bloque
j j j       " bajar para seleccionar varias líneas
I           " insertar al inicio del bloque
#           " escriba el texto deseado
Esc         " Vim repetirá el cambio en cada línea seleccionada
            </pre>
          </div>

          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Reemplazo guiado con selección</div>
            <pre>
" Dentro de modo visual, seleccione el rango
:'&lt;,'&gt;s/viejo/nuevo/gc
" Reemplaza solo dentro de la selección, con confirmación
            </pre>
          </div>
        </div>
      </div>
    </section>
  </main>
</div>
