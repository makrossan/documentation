---
title: Regular Expressions Cheat Sheet
description: An interactive regular-expression reference.
hide:
  - navigation
  - toc
---

<div class="cheatsheet-page cheatsheet-page--regex">
<main class="outer">
    <header class="hero">
      <div>
        <p class="eyebrow">Pattern language · quick reference</p>
        <h1>The Ultimate Regular Expressions Cheat Sheet</h1>
        <p>Find, validate, extract, and transform text with confidence. Choose a category below, then test your patterns against real examples.</p>
      </div>
      <div class="header-actions">
        <a class="practice-link dashboard-link" href="/#cheat-sheets">Back to the dashboard</a>
        <a class="practice-link" href="https://regex101.com/" target="_blank" rel="noopener noreferrer">Practice on regex101.com ↗</a>
      </div>
    </header>

    <div class="tabs-shell">
      <nav class="topnav" role="tablist" aria-label="Regular expression categories">
        <button class="tablinks active" id="tab-all" role="tab" aria-selected="true" aria-controls="AllTokens" onclick="openAppliance(event, 'AllTokens')">All Tokens</button>
        <button class="tablinks" id="tab-common" role="tab" aria-selected="false" aria-controls="CommonTokens" onclick="openAppliance(event, 'CommonTokens')">Common</button>
        <button class="tablinks" id="tab-general" role="tab" aria-selected="false" aria-controls="GeneralTokens" onclick="openAppliance(event, 'GeneralTokens')">General</button>
        <button class="tablinks" id="tab-anchors" role="tab" aria-selected="false" aria-controls="Anchors" onclick="openAppliance(event, 'Anchors')">Anchors</button>
        <button class="tablinks" id="tab-meta" role="tab" aria-selected="false" aria-controls="MetaSequences" onclick="openAppliance(event, 'MetaSequences')">Meta Sequences</button>
        <button class="tablinks" id="tab-quantifiers" role="tab" aria-selected="false" aria-controls="Quantifiers" onclick="openAppliance(event, 'Quantifiers')">Quantifiers</button>
        <button class="tablinks" id="tab-groups" role="tab" aria-selected="false" aria-controls="GroupConstructs" onclick="openAppliance(event, 'GroupConstructs')">Group Constructs</button>
        <button class="tablinks" id="tab-classes" role="tab" aria-selected="false" aria-controls="CharacterClasses" onclick="openAppliance(event, 'CharacterClasses')">Character Classes</button>
        <button class="tablinks" id="tab-flags" role="tab" aria-selected="false" aria-controls="FlagsModifiers" onclick="openAppliance(event, 'FlagsModifiers')">Flags / Modifiers</button>
        <button class="tablinks" id="tab-substitutions" role="tab" aria-selected="false" aria-controls="Substitutions" onclick="openAppliance(event, 'Substitutions')">Substitutions</button>
      </nav>
    </div>

    <section id="AllTokens" class="tabcontent active-panel" role="tabpanel" aria-labelledby="tab-all">
      <div class="section-header"><h2>All Tokens</h2><span class="tag">Master reference</span></div>
      <div class="section-body">
        <div class="note"><span class="note-icon">i</span><div><strong>Regex flavors differ.</strong> JavaScript, PCRE, Python, .NET, Java, POSIX tools, and Vim do not support every token in exactly the same way. Always select the matching flavor when testing.</div></div>
        <div class="table-wrap"><table>
          <thead><tr><th>Pattern</th><th>Meaning</th><th>Example</th><th>Matches</th></tr></thead>
          <tbody>
            <tr><td><code>.</code></td><td>Any character, usually except newline</td><td><code>c.t</code></td><td><code>cat</code>, <code>cot</code>, <code>c7t</code></td></tr>
            <tr><td><code>\</code></td><td>Escape a special character</td><td><code>\.</code></td><td>A literal period</td></tr>
            <tr><td><code>[abc]</code></td><td>One character from the set</td><td><code>[cm]at</code></td><td><code>cat</code>, <code>mat</code></td></tr>
            <tr><td><code>[^abc]</code></td><td>One character not in the set</td><td><code>[^c]at</code></td><td><code>bat</code>, not <code>cat</code></td></tr>
            <tr><td><code>[a-z]</code></td><td>One character in a range</td><td><code>[a-f]</code></td><td><code>a</code> through <code>f</code></td></tr>
            <tr><td><code>\d</code> / <code>\D</code></td><td>Digit / non-digit</td><td><code>\d+</code></td><td><code>7</code>, <code>2026</code></td></tr>
            <tr><td><code>\w</code> / <code>\W</code></td><td>Word / non-word character</td><td><code>\w+</code></td><td><code>user_42</code></td></tr>
            <tr><td><code>\s</code> / <code>\S</code></td><td>Whitespace / non-whitespace</td><td><code>a\sb</code></td><td><code>a b</code></td></tr>
            <tr><td><code>^</code> / <code>$</code></td><td>Start / end of string or line</td><td><code>^cat$</code></td><td>Only <code>cat</code></td></tr>
            <tr><td><code>\b</code> / <code>\B</code></td><td>Word boundary / non-boundary</td><td><code>\bcat\b</code></td><td><code>cat</code>, not <code>catalog</code></td></tr>
            <tr><td><code>*</code></td><td>Zero or more</td><td><code>ca*t</code></td><td><code>ct</code>, <code>cat</code>, <code>caaat</code></td></tr>
            <tr><td><code>+</code></td><td>One or more</td><td><code>a+</code></td><td><code>a</code>, <code>aa</code>, <code>aaa</code></td></tr>
            <tr><td><code>?</code></td><td>Zero or one</td><td><code>colou?r</code></td><td><code>color</code>, <code>colour</code></td></tr>
            <tr><td><code>{n}</code></td><td>Exactly n repetitions</td><td><code>a{2}</code></td><td><code>aa</code></td></tr>
            <tr><td><code>{n,m}</code></td><td>Between n and m repetitions</td><td><code>a{2,4}</code></td><td><code>aa</code>, <code>aaa</code>, <code>aaaa</code></td></tr>
            <tr><td><code>{n,}</code></td><td>At least n repetitions</td><td><code>a{2,}</code></td><td><code>aa</code>, <code>aaa...</code></td></tr>
            <tr><td><code>(ab)</code></td><td>Capturing group</td><td><code>(ab){2}</code></td><td><code>abab</code></td></tr>
            <tr><td><code>(?:ab)</code></td><td>Non-capturing group</td><td><code>(?:ha)+</code></td><td><code>ha</code>, <code>haha</code></td></tr>
            <tr><td><code>cat|dog</code></td><td>Alternation: either pattern</td><td><code>cat|dog</code></td><td><code>cat</code> or <code>dog</code></td></tr>
            <tr><td><code>(?=x)</code> / <code>(?!x)</code></td><td>Positive / negative lookahead</td><td><code>\d+(?=px)</code></td><td>Digits before <code>px</code></td></tr>
            <tr><td><code>(?&lt;=x)</code> / <code>(?&lt;!x)</code></td><td>Positive / negative lookbehind</td><td><code>(?&lt;=\$)\d+</code></td><td>Digits after <code>$</code></td></tr>
            <tr><td><code>\1</code></td><td>Backreference to capture group 1</td><td><code>(\w+)\s+\1</code></td><td><code>go go</code></td></tr>
          </tbody>
        </table></div>
      </div>
    </section>

    <section id="CommonTokens" class="tabcontent" role="tabpanel" aria-labelledby="tab-common">
      <div class="section-header"><h2>Common Tokens</h2><span class="tag">Everyday essentials</span></div>
      <div class="section-body">
        <div class="grid">
          <article class="box"><h3>Characters and sets</h3><ul><li><code>.</code> any character except usually a newline</li><li><code>\.</code> literal period</li><li><code>[abc]</code> one listed character</li><li><code>[^abc]</code> one character not listed</li><li><code>[a-z]</code> one character in the range</li></ul></article>
          <article class="box"><h3>Structure and repetition</h3><ul><li><code>^</code> start and <code>$</code> end</li><li><code>*</code> zero or more</li><li><code>+</code> one or more</li><li><code>?</code> zero or one</li><li><code>{2,4}</code> between two and four</li></ul></article>
          <article class="box"><h3>Shorthand classes</h3><ul><li><code>\d</code> digit</li><li><code>\w</code> word character</li><li><code>\s</code> whitespace</li><li>Uppercase forms—<code>\D</code>, <code>\W</code>, <code>\S</code>—mean “not.”</li></ul></article>
          <article class="box"><h3>Combining patterns</h3><ul><li><code>(...)</code> capture a group</li><li><code>(?:...)</code> group without capturing</li><li><code>a|b</code> match a or b</li><li><code>\b</code> word boundary</li><li><code>\1</code> repeat captured group 1</li></ul></article>
        </div>
      </div>
    </section>

    <section id="GeneralTokens" class="tabcontent" role="tabpanel" aria-labelledby="tab-general">
      <div class="section-header"><h2>General Tokens</h2><span class="tag">Literals and control characters</span></div>
      <div class="section-body"><div class="table-wrap"><table>
        <thead><tr><th>Token</th><th>Meaning</th><th>Example</th><th>Matches</th></tr></thead>
        <tbody>
          <tr><td><code>abc</code></td><td>Literal sequence</td><td><code>cat</code></td><td>The exact text <code>cat</code></td></tr>
          <tr><td><code>\n</code></td><td>Newline</td><td><code>one\ntwo</code></td><td>Text on consecutive lines</td></tr>
          <tr><td><code>\r</code></td><td>Carriage return</td><td><code>\r\n</code></td><td>Windows-style line ending</td></tr>
          <tr><td><code>\t</code></td><td>Tab</td><td><code>a\tb</code></td><td><code>a</code>, tab, <code>b</code></td></tr>
          <tr><td><code>\xHH</code></td><td>Character from hexadecimal byte</td><td><code>\x41</code></td><td><code>A</code></td></tr>
          <tr><td><code>\uHHHH</code></td><td>Unicode code unit in supported engines</td><td><code>\u0041</code></td><td><code>A</code></td></tr>
          <tr><td><code>\Q...\E</code></td><td>Treat content literally in supported engines</td><td><code>\Q$5.00\E</code></td><td><code>$5.00</code></td></tr>
          <tr><td><code>(?#...)</code></td><td>Inline comment in supported engines</td><td><code>\d+(?# number)</code></td><td>A number</td></tr>
        </tbody>
      </table></div></div>
    </section>

    <section id="Anchors" class="tabcontent" role="tabpanel" aria-labelledby="tab-anchors">
      <div class="section-header"><h2>Anchors</h2><span class="tag">Match positions, not characters</span></div>
      <div class="section-body"><div class="table-wrap"><table>
        <thead><tr><th>Anchor</th><th>Meaning</th><th>Example</th><th>Result</th></tr></thead>
        <tbody>
          <tr><td><code>^</code></td><td>Start of string, or line in multiline mode</td><td><code>^Error</code></td><td>Lines beginning with <code>Error</code></td></tr>
          <tr><td><code>$</code></td><td>End of string, or line in multiline mode</td><td><code>done$</code></td><td>Lines ending with <code>done</code></td></tr>
          <tr><td><code>\A</code></td><td>Absolute start of string in supported engines</td><td><code>\AHello</code></td><td><code>Hello</code> only at the beginning</td></tr>
          <tr><td><code>\Z</code></td><td>End of string, sometimes before final newline</td><td><code>world\Z</code></td><td><code>world</code> at the end</td></tr>
          <tr><td><code>\z</code></td><td>Absolute end of string in supported engines</td><td><code>world\z</code></td><td>Strict end position</td></tr>
          <tr><td><code>\b</code></td><td>Word boundary</td><td><code>\bcat\b</code></td><td><code>cat</code>, not <code>catalog</code></td></tr>
          <tr><td><code>\B</code></td><td>Not a word boundary</td><td><code>\Bcat</code></td><td><code>cat</code> inside another word</td></tr>
          <tr><td><code>\G</code></td><td>End of previous match or start position in supported engines</td><td><code>\G,?\w+</code></td><td>Contiguous tokens</td></tr>
        </tbody>
      </table></div></div>
    </section>

    <section id="MetaSequences" class="tabcontent" role="tabpanel" aria-labelledby="tab-meta">
      <div class="section-header"><h2>Meta Sequences</h2><span class="tag">Character shortcuts</span></div>
      <div class="section-body"><div class="table-wrap"><table>
        <thead><tr><th>Sequence</th><th>Meaning</th><th>Typical equivalent</th><th>Example</th></tr></thead>
        <tbody>
          <tr><td><code>\d</code></td><td>Digit</td><td><code>[0-9]</code> in ASCII mode</td><td><code>\d{4}</code> → <code>2026</code></td></tr>
          <tr><td><code>\D</code></td><td>Non-digit</td><td><code>[^0-9]</code></td><td><code>\D+</code> → <code>abc</code></td></tr>
          <tr><td><code>\w</code></td><td>Word character</td><td>Often <code>[A-Za-z0-9_]</code></td><td><code>user_1</code></td></tr>
          <tr><td><code>\W</code></td><td>Non-word character</td><td>Inverse of <code>\w</code></td><td><code>!@#</code></td></tr>
          <tr><td><code>\s</code></td><td>Whitespace</td><td>Space, tab, newline</td><td><code>a\sb</code></td></tr>
          <tr><td><code>\S</code></td><td>Non-whitespace</td><td>Inverse of <code>\s</code></td><td><code>hello</code></td></tr>
          <tr><td><code>\h</code> / <code>\H</code></td><td>Horizontal whitespace / inverse</td><td>Spaces and tabs</td><td>Flavor-dependent</td></tr>
          <tr><td><code>\v</code> / <code>\V</code></td><td>Vertical whitespace / inverse</td><td>Line-break characters</td><td>Flavor-dependent</td></tr>
          <tr><td><code>\R</code></td><td>Any Unicode line break</td><td><code>\n</code>, <code>\r\n</code>, etc.</td><td>Flavor-dependent</td></tr>
          <tr><td><code>\p{L}</code></td><td>Any Unicode letter</td><td>Unicode property escape</td><td><code>A</code>, <code>é</code>, <code>中</code></td></tr>
          <tr><td><code>\p{N}</code></td><td>Any Unicode number</td><td>Unicode property escape</td><td><code>4</code>, <code>٢</code></td></tr>
          <tr><td><code>\P{L}</code></td><td>Anything except a Unicode letter</td><td>Negated Unicode property</td><td><code>7</code>, <code>!</code></td></tr>
        </tbody>
      </table></div></div>
    </section>

    <section id="Quantifiers" class="tabcontent" role="tabpanel" aria-labelledby="tab-quantifiers">
      <div class="section-header"><h2>Quantifiers</h2><span class="tag">Control repetition</span></div>
      <div class="section-body">
        <div class="note"><span class="note-icon">Q</span><div><strong>Greedy, lazy, and possessive:</strong> greedy quantifiers take as much as possible; lazy quantifiers prefer as little as possible; possessive quantifiers prevent backtracking and are not available in every engine.</div></div>
        <div class="table-wrap"><table>
          <thead><tr><th>Quantifier</th><th>Meaning</th><th>Example</th><th>Matches</th></tr></thead>
          <tbody>
            <tr><td><code>*</code></td><td>Zero or more, greedy</td><td><code>go*</code></td><td><code>g</code>, <code>go</code>, <code>gooo</code></td></tr>
            <tr><td><code>+</code></td><td>One or more, greedy</td><td><code>go+</code></td><td><code>go</code>, <code>gooo</code></td></tr>
            <tr><td><code>?</code></td><td>Zero or one, greedy</td><td><code>go?</code></td><td><code>g</code>, <code>go</code></td></tr>
            <tr><td><code>{n}</code></td><td>Exactly n</td><td><code>\d{4}</code></td><td><code>2026</code></td></tr>
            <tr><td><code>{n,}</code></td><td>At least n</td><td><code>a{2,}</code></td><td><code>aa</code>, <code>aaa...</code></td></tr>
            <tr><td><code>{n,m}</code></td><td>From n through m</td><td><code>a{2,4}</code></td><td><code>aa</code> through <code>aaaa</code></td></tr>
            <tr><td><code>*?</code> / <code>+?</code></td><td>Lazy repetition</td><td><code>&lt;.*?&gt;</code></td><td>The shortest tag-like segment</td></tr>
            <tr><td><code>{n,m}?</code></td><td>Lazy bounded repetition</td><td><code>a{2,4}?</code></td><td>Prefers two <code>a</code>s</td></tr>
            <tr><td><code>*+</code> / <code>++</code></td><td>Possessive repetition in supported engines</td><td><code>a++a</code></td><td>Consumes without backtracking</td></tr>
          </tbody>
        </table></div>
      </div>
    </section>

    <section id="GroupConstructs" class="tabcontent" role="tabpanel" aria-labelledby="tab-groups">
      <div class="section-header"><h2>Group Constructs</h2><span class="tag">Capture, branch, and assert</span></div>
      <div class="section-body"><div class="table-wrap"><table>
        <thead><tr><th>Construct</th><th>Meaning</th><th>Example</th><th>Result</th></tr></thead>
        <tbody>
          <tr><td><code>(abc)</code></td><td>Numbered capturing group</td><td><code>(ha)+</code></td><td><code>ha</code>, <code>haha</code></td></tr>
          <tr><td><code>(?:abc)</code></td><td>Non-capturing group</td><td><code>(?:https?://)?</code></td><td>Optional protocol without a capture</td></tr>
          <tr><td><code>(?&lt;name&gt;abc)</code></td><td>Named capture in many engines</td><td><code>(?&lt;year&gt;\d{4})</code></td><td>Capture named <code>year</code></td></tr>
          <tr><td><code>(?P&lt;name&gt;abc)</code></td><td>Python-style named capture</td><td><code>(?P&lt;year&gt;\d{4})</code></td><td>Capture named <code>year</code></td></tr>
          <tr><td><code>a|b</code></td><td>Alternation</td><td><code>cat|dog</code></td><td><code>cat</code> or <code>dog</code></td></tr>
          <tr><td><code>\1</code></td><td>Numbered backreference</td><td><code>(\w+)\s+\1</code></td><td>A repeated word</td></tr>
          <tr><td><code>\k&lt;name&gt;</code></td><td>Named backreference in many engines</td><td><code>(?&lt;w&gt;\w+) \k&lt;w&gt;</code></td><td>A repeated named capture</td></tr>
          <tr><td><code>(?=abc)</code></td><td>Positive lookahead</td><td><code>\w+(?=:)</code></td><td>Word followed by a colon</td></tr>
          <tr><td><code>(?!abc)</code></td><td>Negative lookahead</td><td><code>foo(?!bar)</code></td><td><code>foo</code> not followed by <code>bar</code></td></tr>
          <tr><td><code>(?&lt;=abc)</code></td><td>Positive lookbehind</td><td><code>(?&lt;=\$)\d+</code></td><td>Digits after a dollar sign</td></tr>
          <tr><td><code>(?&lt;!abc)</code></td><td>Negative lookbehind</td><td><code>(?&lt;!-)\d+</code></td><td>Digits not preceded by a hyphen</td></tr>
          <tr><td><code>(?&gt;abc)</code></td><td>Atomic group in supported engines</td><td><code>(?&gt;a+)a</code></td><td>No backtracking inside the group</td></tr>
          <tr><td><code>(?i:abc)</code></td><td>Apply a modifier to one group</td><td><code>(?i:hello)</code></td><td><code>hello</code>, <code>HELLO</code></td></tr>
        </tbody>
      </table></div></div>
    </section>

    <section id="CharacterClasses" class="tabcontent" role="tabpanel" aria-labelledby="tab-classes">
      <div class="section-header"><h2>Character Classes</h2><span class="tag">Match one character from a set</span></div>
      <div class="section-body">
        <div class="table-wrap"><table>
          <thead><tr><th>Class</th><th>Meaning</th><th>Example</th><th>Matches</th></tr></thead>
          <tbody>
            <tr><td><code>[abc]</code></td><td>Any one listed character</td><td><code>[abc]</code></td><td><code>a</code>, <code>b</code>, or <code>c</code></td></tr>
            <tr><td><code>[^abc]</code></td><td>Any character except those listed</td><td><code>[^0-9]</code></td><td>One non-digit</td></tr>
            <tr><td><code>[a-z]</code></td><td>Lowercase ASCII range</td><td><code>[a-z]+</code></td><td><code>hello</code></td></tr>
            <tr><td><code>[A-Z]</code></td><td>Uppercase ASCII range</td><td><code>[A-Z]{2}</code></td><td><code>US</code></td></tr>
            <tr><td><code>[0-9]</code></td><td>ASCII digit range</td><td><code>[0-9]{2}</code></td><td><code>42</code></td></tr>
            <tr><td><code>[A-Za-z0-9_]</code></td><td>ASCII word-style character</td><td><code>[A-Za-z_]\w*</code></td><td>A simple identifier</td></tr>
            <tr><td><code>[a-fA-F0-9]</code></td><td>Hexadecimal digit</td><td><code>#[a-fA-F0-9]{6}</code></td><td><code>#00bcd4</code></td></tr>
            <tr><td><code>[._-]</code></td><td>Period, underscore, or hyphen</td><td><code>[._-]</code></td><td>One listed symbol</td></tr>
            <tr><td><code>[\[\]]</code></td><td>Opening or closing square bracket</td><td><code>[\[\]]</code></td><td><code>[</code> or <code>]</code></td></tr>
            <tr><td><code>[[:digit:]]</code></td><td>POSIX digit class</td><td><code>[[:digit:]]+</code></td><td>Digits in supporting engines</td></tr>
            <tr><td><code>[[:space:]]</code></td><td>POSIX whitespace class</td><td><code>[[:space:]]+</code></td><td>Whitespace in supporting engines</td></tr>
          </tbody>
        </table></div>
        <div class="note" style="margin-top:1rem;margin-bottom:0"><span class="note-icon">!</span><div><strong>Remember:</strong> <code>[cat]</code> matches one character—<code>c</code>, <code>a</code>, or <code>t</code>. Use <code>(cat)</code> to group the complete word. Place <code>-</code> first or last, or escape it, when you need a literal hyphen.</div></div>
      </div>
    </section>

    <section id="FlagsModifiers" class="tabcontent" role="tabpanel" aria-labelledby="tab-flags">
      <div class="section-header"><h2>Flags / Modifiers</h2><span class="tag">Change matching behavior</span></div>
      <div class="section-body"><div class="table-wrap"><table>
        <thead><tr><th>Flag</th><th>Name</th><th>Effect</th><th>Example</th></tr></thead>
        <tbody>
          <tr><td><code>i</code></td><td>Case-insensitive</td><td>Ignore letter case</td><td><code>/cat/i</code> matches <code>CAT</code></td></tr>
          <tr><td><code>g</code></td><td>Global</td><td>Find or replace all matches</td><td><code>/cat/g</code></td></tr>
          <tr><td><code>m</code></td><td>Multiline</td><td><code>^</code> and <code>$</code> match line boundaries</td><td><code>/^Error/gm</code></td></tr>
          <tr><td><code>s</code></td><td>Dotall / single-line</td><td><code>.</code> also matches newlines</td><td><code>/start.*end/s</code></td></tr>
          <tr><td><code>u</code></td><td>Unicode</td><td>Enable Unicode-aware behavior in engines such as JavaScript</td><td><code>/\p{L}+/u</code></td></tr>
          <tr><td><code>x</code></td><td>Extended / free-spacing</td><td>Allow layout whitespace and comments in supported engines</td><td><code>(?x) \d+ \s+ \w+</code></td></tr>
          <tr><td><code>y</code></td><td>Sticky</td><td>Match only at the current position in JavaScript</td><td><code>/\w+/y</code></td></tr>
          <tr><td><code>d</code></td><td>Indices</td><td>Return match indices in modern JavaScript</td><td><code>/cat/d</code></td></tr>
        </tbody>
      </table></div>
      <div class="grid" style="margin-top:1rem">
        <article class="box"><h3>Inline modifiers</h3><p><code>(?i)cat</code> enables case-insensitive matching where supported. <code>(?i:cat)</code> limits the modifier to one group.</p></article>
        <article class="box"><h3>Vim modifiers</h3><p>Use <code>\c</code> for case-insensitive and <code>\C</code> for case-sensitive matching, or configure <code>:set ignorecase</code>.</p></article>
      </div></div>
    </section>

    <section id="Substitutions" class="tabcontent" role="tabpanel" aria-labelledby="tab-substitutions">
      <div class="section-header"><h2>Substitutions</h2><span class="tag">Search and replace</span></div>
      <div class="section-body">
        <div class="note"><span class="note-icon">S</span><div><strong>Replacement syntax varies.</strong> JavaScript commonly uses <code>$1</code>, Python uses <code>\g&lt;1&gt;</code>, and Vim commonly uses <code>\1</code>. Confirm the syntax for your tool.</div></div>
        <div class="table-wrap"><table>
          <thead><tr><th>Goal</th><th>Search</th><th>Replacement</th><th>Result</th></tr></thead>
          <tbody>
            <tr><td>Swap first and last names</td><td><code>(\w+)\s+(\w+)</code></td><td><code>$2, $1</code></td><td><code>Ada Lovelace</code> → <code>Lovelace, Ada</code></td></tr>
            <tr><td>Reformat ISO date</td><td><code>(\d{4})-(\d{2})-(\d{2})</code></td><td><code>$3/$2/$1</code></td><td><code>2026-07-31</code> → <code>31/07/2026</code></td></tr>
            <tr><td>Collapse whitespace</td><td><code>\s+</code></td><td>One space</td><td><code>too&nbsp;&nbsp;&nbsp;many</code> → <code>too many</code></td></tr>
            <tr><td>Remove Markdown checkboxes</td><td><code>\[[ xX]\]</code></td><td>Empty text</td><td>Removes <code>[ ]</code>, <code>[x]</code>, and <code>[X]</code></td></tr>
            <tr><td>Wrap every number</td><td><code>(\d+)</code></td><td><code>[$1]</code></td><td><code>42</code> → <code>[42]</code></td></tr>
          </tbody>
        </table></div>
        <div class="grid" style="margin-top:1rem">
          <article class="box"><h3>Common replacement references</h3><ul><li><code>$&amp;</code> entire match in JavaScript</li><li><code>$1</code>, <code>$2</code> numbered groups in JavaScript</li><li><code>${name}</code> named group in JavaScript</li><li><code>\g&lt;name&gt;</code> named group in Python</li></ul></article>
          <article class="box"><h3>Vim substitution</h3><ul><li><code>:%s/old/new/g</code> replace all occurrences</li><li><code>:%s/\[x\]//g</code> delete every <code>[x]</code></li><li><code>:%s/\[[ xX]\]//gc</code> delete checkboxes with confirmation</li><li><code>&amp;</code> entire match; <code>\1</code> captured group 1</li></ul></article>
        </div>
      </div>
    </section>

    <footer class="footer">Build patterns one token at a time, test positive and negative cases, and practice interactively at <a href="https://regex101.com/" target="_blank" rel="noopener noreferrer">regex101.com</a>.</footer>
  </main>
</div>

<script>
function openAppliance(evt, panelName) {
      var i, tabcontent, tablinks;
      tabcontent = document.getElementsByClassName("tabcontent");
      for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
        tabcontent[i].classList.remove("active-panel");
      }
      tablinks = document.getElementsByClassName("tablinks");
      for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
        tablinks[i].setAttribute("aria-selected", "false");
      }
      document.getElementById(panelName).style.display = "block";
      document.getElementById(panelName).classList.add("active-panel");
      evt.currentTarget.className += " active";
      evt.currentTarget.setAttribute("aria-selected", "true");
      window.history.replaceState(null, "", "#" + panelName);
    }

    document.querySelector('.topnav').addEventListener('keydown', function (event) {
      var tabs = Array.from(document.querySelectorAll('.tablinks'));
      var current = tabs.indexOf(document.activeElement);
      if (current < 0 || (event.key !== 'ArrowRight' && event.key !== 'ArrowLeft')) return;
      event.preventDefault();
      var next = event.key === 'ArrowRight' ? (current + 1) % tabs.length : (current - 1 + tabs.length) % tabs.length;
      tabs[next].focus();
      tabs[next].click();
    });

    window.addEventListener('DOMContentLoaded', function () {
      var requested = window.location.hash.slice(1);
      var panel = requested && document.getElementById(requested);
      if (panel && panel.classList.contains('tabcontent')) {
        var button = document.querySelector('[aria-controls="' + requested + '"]');
        if (button) button.click();
      }
    });
</script>
