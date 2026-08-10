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
        <h1>La guía y hoja de trucos definitiva de tmux</h1>
        <p>Comandos esenciales de tmux organizados por secciones prácticas. Prefijo por defecto Ctrl + b.</p>
      </div>
      <a href="/#cheat-sheets" class="back-button">Volver al Dashboard anterior</a>
    </div>

    <!-- Prefijo / introducción -->
    <section class="section">
      <div class="section-header">
        <h2>Prefijo y conceptos básicos</h2>
        <span class="tag">Lo mínimo para no perderse</span>
      </div>
      <div class="section-body">
        <div class="note">
          <div class="note-icon">P</div>
          <div>
            <strong>Prefijo por defecto.</strong>
            <code>Ctrl + b</code> (puede cambiarse con <code>set-option -g prefix C-a</code>).
            Todos los atajos que dicen <code>prefijo</code> asumen <code>Ctrl + b</code>, cambie si lo ha remapeado.
          </div>
        </div>
      </div>
    </section>

    <!-- Inicio y sesiones -->
    <section class="section">
      <div class="section-header">
        <h2>Inicio y sesiones</h2>
        <span class="tag">Crear, listar y gestionar sesiones</span>
      </div>
      <div class="section-body">
        <div class="grid">
          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Comandos de shell
            </div>
            <ul class="cmd-list">
              <li><code>tmux</code> <span class="desc">Iniciar nueva sesión.</span></li>
              <li><code>tmux ls</code> <span class="desc">Listar todas las sesiones.</span></li>
              <li><code>tmux new -s <span class="highlight">nombre</span></code> <span class="desc">Nueva sesión con nombre.</span></li>
              <li><code>tmux attach -t <span class="highlight">nombre</span></code> <span class="desc">Adjuntarse a sesión.</span></li>
              <li><code>tmux detach</code> <span class="desc">Desacoplar (desde dentro de tmux).</span></li>
              <li><code>tmux rename-session -t <span class="highlight">nombre1</span> <span class="highlight">nombre2</span></code> <span class="desc">Renombrar sesión.</span></li>
              <li><code>tmux switch -t <span class="highlight">nombre</span></code> <span class="desc">Cambiar a sesión.</span></li>
              <li><code>tmux kill-session -t <span class="highlight">nombre</span></code> <span class="desc">Eliminar sesión por nombre.</span></li>
              <li><code>tmux kill-server</code> <span class="desc">Eliminar todas las sesiones (servidor).</span></li>
            </ul>
          </div>
          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Atajos con prefijo dentro de tmux
            </div>
            <ul class="cmd-list">
              <li><code>prefijo</code><span class="hotkey">:</span><span class="desc"> Abrir prompt de comando.</span></li>
              <li><code>prefijo</code><span class="hotkey">d</span><span class="desc"> Desacoplar de la sesión.</span></li>
              <li><code>prefijo</code><span class="hotkey">s</span><span class="desc"> Selector de sesiones.</span></li>
              <li><code>prefijo</code><span class="hotkey">$</span><span class="desc"> Renombrar sesión actual.</span></li>
              <li><code>prefijo</code><span class="hotkey">?</span><span class="desc"> Listar combinaciones de teclas.</span></li>
              <li><code>prefijo</code><span class="hotkey">,</span><span class="desc"> Renombrar ventana actual.</span></li>
              <li><code>prefijo</code><span class="hotkey">w</span><span class="desc"> Selector de ventanas.</span></li>
              <li><span class="desc">Para cerrar la sesión actual, use:</span> <code>prefijo</code><span class="hotkey">:</span> <code> kill-session</code></li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- Paneles -->
    <section class="section">
      <div class="section-header">
        <h2>Paneles</h2>
        <span class="tag">Dividir la terminal y moverse entre paneles</span>
      </div>
      <div class="section-body">
        <div class="grid">
          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Gestión de paneles
            </div>
            <ul class="cmd-list">
              <li><code>prefijo</code><span class="hotkey">%</span><span class="desc"> Dividir verticalmente.</span></li>
              <li><code>prefijo</code><span class="hotkey">"</span><span class="desc"> Dividir horizontalmente.</span></li>
              <li><code>prefijo</code><span class="hotkey">o</span><span class="desc"> Ir al siguiente panel.</span></li>
              <li><code>prefijo</code><span class="hotkey">;</span><span class="desc"> Alternar entre los dos últimos paneles.</span></li>
              <li><code>prefijo</code><span class="hotkey">{ }</span><span class="desc"> Intercambiar panel izquierda/derecha.</span></li>
              <li><code>prefijo</code><span class="hotkey">q</span><span class="desc"> Mostrar números de panel.</span></li>
              <li><code>prefijo</code><span class="hotkey">z</span><span class="desc"> Zoom en panel.</span></li>
              <li><code>prefijo</code><span class="hotkey">x</span><span class="desc"> Cerrar panel actual.</span></li>
              <li><code>prefijo</code><span class="hotkey">!</span><span class="desc"> Promuebe panel actual a ventana.</span></li>
            </ul>
          </div>
          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Movimiento y opciones avanzadas
            </div>
            <ul class="cmd-list">
              <li><code>prefijo</code><span class="hotkey">↑/↓/←/→</span><span class="desc"> Mover foco de panel.</span></li>
              <li><code>prefijo</code><span class="hotkey">Alt + ↑/↓/←/→</span><span class="desc"> Redimensionar panel.</span></li>
              <li><code>join-pane -s 2.1 -t 1.0</code> <span class="desc">Unir panel 2.1 a 1.0.</span></li>
              <li><code>break-pane</code> <span class="desc">Convertir panel en ventana.</span></li>
              <li><code>swap-pane -[UDLR]</code> <span class="desc">Intercambiar dirección del panel.</span></li>
              <li><code>select-pane -t :.+</code> <span class="desc">Seleccionar siguiente panel.</span></li>
              <li><code>set-window-option synchronize-panes on</code> <span class="desc">Sincronizar paneles.</span></li>
              <li><code>display-message '#P'</code> <span class="desc">Mostrar índice de panel.</span></li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- Ventanas y pestañas -->
    <section class="section">
      <div class="section-header">
        <h2>Ventanas y pestañas</h2>
        <span class="tag">Organizar trabajo en varias vistas</span>
      </div>
      <div class="section-body">
        <div class="grid">
          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Comandos de ventana
            </div>
            <ul class="cmd-list">
              <li><code>rename-window <span class="highlight">nombrenuevo</span></code><span class="desc">Renombrar ventana actual.</span></li>
              <li><code>swap-window -t 2</code> <span class="desc">Intercambiar con ventana 2.</span></li>
              <li><code>move-window -t 3</code> <span class="desc">Mover a ventana 3.</span></li>
              <li><code>link-window -s src -t dst</code> <span class="desc">Enlazar ventana entre sesiones.</span></li>
              <li><code>unlink-window</code> <span class="desc">Desenlazar ventana.</span></li>
              <li><code>kill-window</code> <span class="desc">Cerrar ventana.</span></li>
              <li><code>display-message '#W'</code> <span class="desc">Mostrar nombre de ventana.</span></li>
            </ul>
          </div>
          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Atajos de ventana con prefijo
            </div>
            <ul class="cmd-list">
              <li><code>prefijo</code><span class="hotkey">c</span><span class="desc"> Crear nueva ventana.</span></li>
              <li><code>prefijo</code><span class="hotkey">p</span><span class="desc"> Ventana anterior.</span></li>
              <li><code>prefijo</code><span class="hotkey">n</span><span class="desc"> Ventana siguiente.</span></li>
              <li><code>prefijo</code><span class="hotkey">&lt;0-9&gt;</span><span class="desc"> Seleccionar ventana por número.</span></li>
              <li><code>prefijo</code><span class="hotkey">&amp;</span><span class="desc"> Eliminar ventana actual.</span></li>
              <li><code>prefijo</code><span class="hotkey">.</span><span class="desc"> Mover ventana.</span></li>
              <li><code>prefijo</code><span class="hotkey">f</span><span class="desc"> Buscar ventana por nombre.</span></li>
              <li><code>prefijo</code><span class="hotkey">l</span><span class="desc"> Última ventana usada.</span></li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- Copiar y desplazarse -->
    <section class="section">
      <div class="section-header">
        <h2>Modo copiar y desplazarse</h2>
        <span class="tag">Historial y selección de texto</span>
      </div>
      <div class="section-body">
        <div class="grid">
          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Buffers y configuración
            </div>
            <ul class="cmd-list">
              <li><code>:show-buffer</code> <span class="desc">Mostrar buffer principal.</span></li>
              <li><code>:list-buffers</code> <span class="desc">Listar todos los buffers.</span></li>
              <li><code>:save-buffer archivo</code> <span class="desc">Guardar buffer en archivo.</span></li>
              <li><code>:delete-buffer -b N</code> <span class="desc">Eliminar buffer N.</span></li>
              <li><code>set -g mode-keys vi</code> <span class="desc">Usar teclas Vim en modo copiar.</span></li>
            </ul>
          </div>
          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Atajos en modo copiar
            </div>
            <ul class="cmd-list">
              <li><code>prefijo</code><span class="hotkey">[</span><span class="desc"> Entrar en modo copiar.</span></li>
              <li><code>q</code> <span class="desc">Salir de modo copiar.</span></li>
              <li><code>Espacio</code> <span class="desc">Iniciar selección.</span></li>
              <li><code>Enter</code> <span class="desc">Copiar selección.</span></li>
              <li><code>RePág</code> / <code>AvPág</code> <span class="desc">Desplazar arriba/abajo.</span></li>
              <li><code>/</code> <span class="desc">Buscar adelante.</span></li>
              <li><code>?</code> <span class="desc">Buscar atrás.</span></li>
              <li><code>n</code> / <code>N</code> <span class="desc">Siguiente / anterior resultado de búsqueda.</span></li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- Redimensionar y disposición -->
    <section class="section">
      <div class="section-header">
        <h2>Redimensionar y disposición</h2>
        <span class="tag">Layouts predefinidos y ajustes rápidos</span>
      </div>
      <div class="section-body">
        <div class="grid">
          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Layouts
            </div>
            <ul class="cmd-list">
              <li><code>select-layout even-horizontal</code> <span class="desc">Paneles distribuidos horizontalmente.</span></li>
              <li><code>select-layout even-vertical</code> <span class="desc">Paneles distribuidos verticalmente.</span></li>
              <li><code>select-layout main-horizontal</code> <span class="desc">Panel principal arriba, otros abajo.</span></li>
              <li><code>select-layout main-vertical</code> <span class="desc">Panel principal a la izquierda.</span></li>
              <li><code>select-layout tiled</code> <span class="desc">Todos los paneles en mosaico.</span></li>
            </ul>
          </div>
          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Atajos para disposición
            </div>
            <ul class="cmd-list">
              <li><code>prefijo</code><span class="hotkey">Alt + ↑/↓/←/→</span><span class="desc"> Redimensionar panel.</span></li>
              <li><code>prefijo</code><span class="hotkey">Espacio</span><span class="desc"> Cambiar diseño de paneles.</span></li>
              <li><code>prefijo</code><span class="hotkey">q</span><span class="desc"> Mostrar números de panel.</span></li>
              <li><code>prefijo</code><span class="hotkey">{ }</span><span class="desc"> Intercambiar paneles izquierda/derecha.</span></li>
              <li><code>prefijo</code><span class="hotkey">z</span><span class="desc"> Zoom/deszoom de panel activo.</span></li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- Ratón -->
    <section class="section">
      <div class="section-header">
        <h2>Soporte para ratón</h2>
        <span class="tag">Cuando quiere usar el mouse</span>
      </div>
      <div class="section-body">
        <div class="grid">
          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Configuración
            </div>
            <ul class="cmd-list">
              <li><code>set -g mouse on</code> <span class="desc">Habilitar ratón para redimensionar, seleccionar, etc.</span></li>
              <li><code>set -g mouse off</code> <span class="desc">Deshabilitar soporte de ratón.</span></li>
              <li><code>setw -g mode-mouse on</code> <span class="desc">Habilitar ratón en modo copiar (tmux &lt;2.1).</span></li>
            </ul>
          </div>
          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Uso práctico
            </div>
            <ul class="cmd-list">
              <li>Arrastre el borde para redimensionar el panel.</li>
              <li>Haga clic en el panel/ventana para enfocar.</li>
              <li>Desplace la rueda del ratón para ver el historial.</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- Automatización y scripting -->
    <section class="section">
      <div class="section-header">
        <h2>Automatización y scripting</h2>
        <span class="tag">Sesiones preparadas con un solo comando</span>
      </div>
      <div class="section-body">
        <div class="grid">
          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Comandos útiles para scripts
            </div>
            <ul class="cmd-list">
              <li><code>tmux new-session -d -s MiSesion</code> <span class="desc">Sesión desacoplada.</span></li>
              <li><code>tmux send-keys -t MiSesion 'top' Enter</code> <span class="desc">Enviar comando al panel.</span></li>
              <li><code>tmux new-window -t MiSesion:1 -n 'htop'</code> <span class="desc">Crear ventana llamada htop.</span></li>
              <li><code>tmux split-window -h -t MiSesion:1</code> <span class="desc">Dividir ventana en horizontal.</span></li>
              <li><code>tmux select-pane -t MiSesion:1.0</code> <span class="desc">Seleccionar panel 0 en ventana 1.</span></li>
            </ul>
          </div>
          <div class="box">
            <div class="box-title">
              <span class="dot"></span>Ejemplo de script
            </div>
            <pre>
# Ejemplo de script
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

    <!-- Configuración -->
    <section class="section">
      <div class="section-header">
        <h2>Archivo de configuración (~/.tmux.conf)</h2>
        <span class="tag">Atajos y opciones recomendadas</span>
      </div>
      <div class="section-body">
        <pre>
# Remapeo de prefijo
set-option -g prefix C-a
unbind C-b
bind C-a send-prefix

# Soporte para ratón
set -g mouse on

# Teclas Vim en modo copiar
setw -g mode-keys vi

# Soporte para 256 colores
set -g default-terminal "screen-256color"

# Títulos útiles
set -g set-titles on
set -g set-titles-string "#S:#I.#P #W"

# Atajos para dividir paneles
bind | split-window -h
bind - split-window -v

# Recargar configuración
bind r source-file ~/.tmux.conf \; display-message "¡Configuración recargada!"
        </pre>
      </div>
    </section>

    <!-- Consejos y resolución de problemas -->
    <section class="section">
      <div class="section-header">
        <h2>Consejos y resolución de problemas</h2>
        <span class="tag">Cosas que suelen romperse</span>
      </div>
      <div class="section-body">
        <ul class="cmd-list">
          <li><span class="highlight">¿tmux no responde a las teclas?</span><span class="desc">Puede estar en una sesión tmux anidada. El prefijo por defecto es <code>Ctrl+b</code>. Pruebe <code>Ctrl+b</code> dos veces.</span></li>
          <li><span class="highlight">¿Copiar/pegar no funciona?</span><span class="desc">Use <code>set -g mouse on</code> y pruebe Shift + ratón o habilite el portapapeles con el plugin <code>tmux-yank</code>.</span></li>
          <li><span class="highlight">¿Colores de terminal incorrectos?</span><span class="desc">Verifique <code>set -g default-terminal "screen-256color"</code> en <code>~/.tmux.conf</code> y en su emulador de terminal.</span></li>
          <li><span class="highlight">¿Compartir tmux?</span><span class="desc">Ejecute <code>tmux attach -t sesión</code> desde varias terminales (mismo usuario).</span></li>
        </ul>
      </div>
    </section>

    <!-- Plugins y recursos -->
    <section class="section">
      <div class="section-header">
        <h2>Plugins y más recursos</h2>
        <span class="tag">Extienda tmux y siga aprendiendo</span>
      </div>
      <div class="section-body">
        <ul class="cmd-list">
          <li><a class="inline-link" href="https://github.com/tmux-plugins/tpm">TPM (Gestor de Plugins de tmux)</a> <span class="desc">Fácil gestión de plugins.</span></li>
          <li><a class="inline-link" href="https://github.com/tmux-plugins/tmux-sensible">tmux-sensible</a> <span class="desc">Mejores configuraciones por defecto.</span></li>
          <li><a class="inline-link" href="https://github.com/tmux-plugins/tmux-resurrect">tmux-resurrect</a> <span class="desc">Restaurar sesiones de tmux.</span></li>
          <li><a class="inline-link" href="https://github.com/tmux-plugins/tmux-continuum">tmux-continuum</a> <span class="desc">Guardado continuo.</span></li>
          <li><a class="inline-link" href="https://github.com/tmux-plugins/tmux-yank">tmux-yank</a> <span class="desc">Integración con portapapeles.</span></li>
          <li><a class="inline-link" href="https://github.com/tmux/tmux/wiki">Wiki oficial de tmux</a></li>
          <li><a class="inline-link" href="https://leanpub.com/the-tao-of-tmux/read">The Tao of tmux (libro gratuito)</a></li>
          <li><a class="inline-link" href="https://tmuxcheatsheet.com/">tmuxcheatsheet.com</a></li>
        </ul>
      </div>
    </section>
  </main>
</div>
