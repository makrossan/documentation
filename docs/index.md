---
title: Home
description: Practical IT, Cloud, Linux, and command-line notes from the field.
hide:
  - navigation
  - toc
---

<!--
  Ready for Material for MkDocs.

  Expected cheat-sheet locations:
    docs/cheatsheets/awk.md
    docs/cheatsheets/regex.md
    docs/cheatsheets/tmux.md
    docs/cheatsheets/vim.md

  If your files use different names, update the four href values below.
-->

<style>
  /* Make only this page full-width, while keeping the Material header/footer. */
  .md-main__inner {
    margin-top: 0;
    max-width: none;
  }

  .md-content {
    max-width: none;
  }

  .md-content__inner {
    margin: 0;
    padding: 0;
  }

  .md-content__inner::before {
    display: none;
  }

  .home-page {
    --home-content-width: 61rem;
    --home-radius: 0.8rem;
    --home-border: color-mix(
      in srgb,
      var(--md-default-fg-color) 14%,
      transparent
    );
    --home-muted: var(--md-default-fg-color--light);
    color: var(--md-default-fg-color);
    overflow: hidden;
  }

  .home-page * {
    box-sizing: border-box;
  }

  .home-section {
    padding: clamp(1.75rem, 4vw, 3.5rem) 1rem;
    width: 100%;
  }

  .home-section--soft {
    background:
      radial-gradient(
        circle at 100% 0%,
        color-mix(in srgb, var(--md-primary-fg-color) 11%, transparent),
        transparent 28rem
      ),
      color-mix(in srgb, var(--md-default-bg-color) 94%, var(--md-code-bg-color));
  }

  .home-section__inner {
    margin: 0 auto;
    max-width: var(--home-content-width);
  }

  .home-eyebrow {
    color: var(--md-primary-fg-color);
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.12em;
    margin: 0 0 0.8rem;
    text-transform: uppercase;
  }

  .home-heading {
    color: var(--md-default-fg-color);
    font-size: clamp(2rem, 5vw, 3.4rem);
    font-weight: 750;
    letter-spacing: -0.035em;
    line-height: 1.08;
    margin: 0 0 1.2rem;
  }

  .home-lead {
    color: var(--home-muted);
    font-size: clamp(1rem, 2.1vw, 1.2rem);
    line-height: 1.75;
    margin: 0;
    max-width: 38rem;
  }

  /* Hero */
  .home-hero {
    align-items: center;
    background:
      radial-gradient(circle at 85% 18%, rgba(79, 70, 229, 0.35), transparent 28rem),
      radial-gradient(circle at 8% 90%, rgba(14, 165, 233, 0.25), transparent 30rem),
      linear-gradient(145deg, #111827 0%, #172554 48%, #0f172a 100%);
    color: #fff;
    display: flex;
    min-height: calc(100svh - 2.4rem);
    padding: clamp(4.5rem, 10vw, 8rem) 1rem;
    position: relative;
  }

  .home-hero::before {
    background-image:
      linear-gradient(rgba(255,255,255,0.035) 1px, transparent 1px),
      linear-gradient(90deg, rgba(255,255,255,0.035) 1px, transparent 1px);
    background-size: 2rem 2rem;
    content: "";
    inset: 0;
    mask-image: linear-gradient(to bottom, black, transparent 88%);
    pointer-events: none;
    position: absolute;
  }

  .home-hero__inner {
    align-items: center;
    display: grid;
    gap: clamp(2.5rem, 7vw, 6rem);
    grid-template-columns: minmax(0, 1.25fr) minmax(16rem, 0.75fr);
    margin: 0 auto;
    max-width: var(--home-content-width);
    position: relative;
    width: 100%;
    z-index: 1;
  }

  .home-hero .home-eyebrow {
    color: #7dd3fc;
  }

  .home-hero__title {
    color: #fff;
    font-size: clamp(2.8rem, 8vw, 5.8rem);
    font-weight: 800;
    letter-spacing: -0.055em;
    line-height: 0.98;
    margin: 0 0 1.4rem;
    max-width: 14ch;
  }

  .home-hero__title span {
    background: linear-gradient(90deg, #7dd3fc, #c4b5fd 55%, #f0abfc);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
  }

  .home-hero__text {
    color: rgba(255, 255, 255, 0.78);
    font-size: clamp(1rem, 2.2vw, 1.22rem);
    line-height: 1.7;
    margin: 0;
    max-width: 37rem;
  }

  .home-actions {
    display: flex;
    flex-wrap: wrap;
    gap: 0.75rem;
    margin-top: 1.8rem;
  }

  .home-page .home-button {
    align-items: center;
    border: 0.08rem solid rgba(255, 255, 255, 0.72);
    border-radius: 0.35rem;
    color: #fff;
    display: inline-flex;
    font-weight: 700;
    gap: 0.45rem;
    padding: 0.72rem 1rem;
    transition: background-color 160ms ease, border-color 160ms ease,
      color 160ms ease, transform 160ms ease;
  }

  .home-page .home-button:hover,
  .home-page .home-button:focus-visible {
    background: rgba(255, 255, 255, 0.1);
    border-color: #fff;
    color: #fff;
    transform: translateY(-0.1rem);
  }

  .home-page .home-button--primary {
    background: #fff;
    border-color: #fff;
    color: #172554;
  }

  .home-page .home-button--primary:hover,
  .home-page .home-button--primary:focus-visible {
    background: #e0f2fe;
    border-color: #e0f2fe;
    color: #172554;
  }

  .home-terminal {
    background: rgba(3, 7, 18, 0.76);
    border: 1px solid rgba(255, 255, 255, 0.16);
    border-radius: var(--home-radius);
    box-shadow: 0 2rem 5rem rgba(0, 0, 0, 0.35);
    min-width: 0;
    overflow: hidden;
    transform: rotate(1.5deg);
  }

  .home-terminal__bar {
    align-items: center;
    background: rgba(255, 255, 255, 0.06);
    display: flex;
    gap: 0.4rem;
    padding: 0.65rem 0.8rem;
  }

  .home-terminal__dot {
    background: #64748b;
    border-radius: 50%;
    height: 0.55rem;
    width: 0.55rem;
  }

  .home-terminal__dot:nth-child(1) { background: #fb7185; }
  .home-terminal__dot:nth-child(2) { background: #fbbf24; }
  .home-terminal__dot:nth-child(3) { background: #4ade80; }

  .home-terminal pre {
    background: transparent;
    color: #cbd5e1;
    font-size: 0.72rem;
    line-height: 1.8;
    margin: 0;
    overflow-x: auto;
    padding: 1.2rem;
  }

  .home-terminal .prompt { color: #7dd3fc; }
  .home-terminal .answer { color: #c4b5fd; }

  .home-scroll-hint {
    animation: home-bounce 1.8s ease-in-out infinite;
    bottom: 1.2rem;
    color: rgba(255, 255, 255, 0.55);
    font-size: 1.2rem;
    left: 50%;
    position: absolute;
    transform: translateX(-50%);
  }

  @keyframes home-bounce {
    0%, 100% { transform: translate(-50%, 0); }
    50% { transform: translate(-50%, -0.45rem); }
  }

  /* About */
  .home-about {
    align-items: start;
    display: grid;
    gap: clamp(2rem, 7vw, 5rem);
    grid-template-columns: minmax(12rem, 0.7fr) minmax(0, 1.3fr);
  }

  .home-about__aside {
    border-left: 0.2rem solid var(--md-primary-fg-color);
    color: var(--home-muted);
    font-size: 0.92rem;
    line-height: 1.65;
    margin: 0;
    padding-left: 1rem;
  }

  .home-about__copy p {
    font-size: clamp(0.92rem, 1.8vw, 1.05rem);
    line-height: 1.85;
    margin: 0 0 1.15rem;
  }

  .home-about__copy p:last-child {
    margin-bottom: 0;
  }

  /* Cheat-sheet cards */
  .home-cards {
    display: grid;
    gap: 1rem;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    margin-top: 2.4rem;
  }

  .home-card {
    background: var(--md-default-bg-color);
    border: 1px solid var(--home-border);
    border-radius: var(--home-radius);
    box-shadow: 0 0.5rem 1.6rem rgba(0, 0, 0, 0.06);
    color: var(--md-default-fg-color);
    display: flex;
    flex-direction: column;
    min-height: 11rem;
    padding: 1.3rem;
    position: relative;
    transition: border-color 180ms ease, box-shadow 180ms ease,
      transform 180ms ease;
  }

  .home-card:hover,
  .home-card:focus-visible {
    border-color: color-mix(in srgb, var(--md-primary-fg-color) 70%, transparent);
    box-shadow: 0 0.9rem 2.2rem rgba(0, 0, 0, 0.11);
    color: var(--md-default-fg-color);
    transform: translateY(-0.22rem);
  }

  .home-card__top {
    align-items: center;
    display: flex;
    justify-content: space-between;
    margin-bottom: 1rem;
  }

  .home-card__command {
    background: var(--md-code-bg-color);
    border-radius: 0.3rem;
    color: var(--md-code-fg-color);
    font-family: var(--md-code-font-family);
    font-size: 0.82rem;
    padding: 0.35rem 0.55rem;
  }

  .home-card__arrow {
    color: var(--md-primary-fg-color);
    font-size: 1.15rem;
    transition: transform 180ms ease;
  }

  .home-card:hover .home-card__arrow,
  .home-card:focus-visible .home-card__arrow {
    transform: translateX(0.22rem);
  }

  .home-card h3 {
    color: inherit;
    font-size: 1.2rem;
    font-weight: 700;
    margin: 0 0 0.45rem;
  }

  .home-card p {
    color: var(--home-muted);
    line-height: 1.6;
    margin: 0;
  }

  /* Topic strip */
  .home-topics {
    display: grid;
    gap: 1rem;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    margin-top: 2.4rem;
  }

  .home-topic {
    border-top: 1px solid var(--home-border);
    padding-top: 1.1rem;
  }

  .home-topic__number {
    color: var(--md-primary-fg-color);
    display: block;
    font-family: var(--md-code-font-family);
    font-size: 0.7rem;
    margin-bottom: 0.65rem;
  }

  .home-topic h3 {
    font-size: 1rem;
    margin: 0 0 0.4rem;
  }

  .home-topic p {
    color: var(--home-muted);
    line-height: 1.6;
    margin: 0;
  }

  /* Photography */
  .home-photo {
    background:
      linear-gradient(110deg, rgba(2, 6, 23, 0.95), rgba(30, 41, 59, 0.86)),
      radial-gradient(circle at 80% 50%, #0369a1, #0f172a 55%);
    color: #fff;
  }

  .home-photo__inner {
    align-items: center;
    display: grid;
    gap: clamp(2rem, 6vw, 5rem);
    grid-template-columns: minmax(0, 1.25fr) minmax(12rem, 0.75fr);
  }

  .home-photo .home-eyebrow { color: #7dd3fc; }
  .home-photo .home-heading { color: #fff; }
  .home-photo .home-lead { color: rgba(255, 255, 255, 0.74); }

  .home-photo__frame {
    aspect-ratio: 4 / 3;
    background:
      linear-gradient(140deg, transparent 48%, rgba(125, 211, 252, 0.18) 48%),
      radial-gradient(circle at 62% 34%, #fde68a 0 3%, transparent 3.2%),
      linear-gradient(155deg, #0c4a6e, #1e293b 58%, #020617);
    border: 0.35rem solid rgba(255, 255, 255, 0.86);
    border-radius: 0.25rem;
    box-shadow: 0 1.5rem 3rem rgba(0, 0, 0, 0.35);
    position: relative;
    transform: rotate(2deg);
  }

  .home-photo__frame::after {
    bottom: -1.75rem;
    color: rgba(255, 255, 255, 0.6);
    content: "Photography keeps me curious.";
    font-size: 0.68rem;
    left: 0;
    position: absolute;
  }

  /* Closing callout */
  .home-closing {
    text-align: center;
  }

  .home-closing .home-lead {
    margin-left: auto;
    margin-right: auto;
  }

  .home-closing .home-actions {
    justify-content: center;
  }

  .home-closing .home-button {
    border-color: var(--md-primary-fg-color);
    color: var(--md-primary-fg-color);
  }

  .home-closing .home-button:hover,
  .home-closing .home-button:focus-visible {
    background: var(--md-primary-fg-color);
    border-color: var(--md-primary-fg-color);
    color: var(--md-primary-bg-color);
  }

  /* Readable, understated accents when the Material slate palette is active. */
  [data-md-color-scheme="slate"] .home-section:not(.home-photo) .home-eyebrow,
  [data-md-color-scheme="slate"] .home-topic__number {
    color: #8fa3bc;
  }

  [data-md-color-scheme="slate"] .home-closing .home-button {
    border-color: #53657a;
    color: #9eb1c8;
  }

  [data-md-color-scheme="slate"] .home-closing .home-button:hover,
  [data-md-color-scheme="slate"] .home-closing .home-button:focus-visible {
    background: #263446;
    border-color: #71859e;
    color: #e0e7ef;
  }

  /* Reveal-on-scroll: content remains visible when JavaScript is unavailable. */
  .home-page.reveal-ready [data-reveal] {
    opacity: 0;
    transform: translateY(1.5rem);
    transition: opacity 700ms cubic-bezier(0.2, 0.7, 0.2, 1),
      transform 700ms cubic-bezier(0.2, 0.7, 0.2, 1);
  }

  .home-page.reveal-ready [data-reveal="left"] {
    transform: translateX(-1.5rem);
  }

  .home-page.reveal-ready [data-reveal="right"] {
    transform: translateX(1.5rem);
  }

  .home-page.reveal-ready [data-reveal].is-visible {
    opacity: 1;
    transform: translate(0, 0);
  }

  .home-page.reveal-ready .home-card:nth-child(2),
  .home-page.reveal-ready .home-topic:nth-child(2) {
    transition-delay: 90ms;
  }

  .home-page.reveal-ready .home-card:nth-child(3),
  .home-page.reveal-ready .home-topic:nth-child(3) {
    transition-delay: 180ms;
  }

  .home-page.reveal-ready .home-card:nth-child(4) {
    transition-delay: 270ms;
  }

  @media screen and (max-width: 52rem) {
    .home-hero__inner,
    .home-about,
    .home-photo__inner {
      grid-template-columns: 1fr;
    }

    .home-hero {
      min-height: auto;
      padding-bottom: 6rem;
    }

    .home-terminal {
      max-width: 30rem;
      transform: none;
    }

    .home-photo__frame {
      max-width: 24rem;
      width: 85%;
    }
  }

  @media screen and (max-width: 38rem) {
    .home-cards,
    .home-topics {
      grid-template-columns: 1fr;
    }

    .home-card {
      min-height: 0;
    }

    .home-actions {
      align-items: stretch;
      flex-direction: column;
    }

    .home-button {
      justify-content: center;
    }
  }

  @media (prefers-reduced-motion: reduce) {
    .home-scroll-hint {
      animation: none;
    }

    .home-page.reveal-ready [data-reveal],
    .home-page.reveal-ready [data-reveal].is-visible {
      opacity: 1;
      transform: none;
      transition: none;
    }

    .home-card,
    .home-button {
      transition: none;
    }
  }
</style>

<div class="home-page">
  <section class="home-hero" aria-labelledby="home-title">
    <div class="home-hero__inner">
      <div data-reveal="left">
        <p class="home-eyebrow">Welcome to my personal Knowledgebase</p>
        <h1 class="home-hero__title" id="home-title">
          Practical notes for <span>real-world problems.</span>
        </h1>
        <p class="home-hero__text">
          A personal collection of concise instructions, tested solutions, and
          command-line cheat sheets gathered throughout my work in IT and Cloud.
        </p>
        <div class="home-actions">
          <a class="home-button home-button--primary" href="#cheat-sheets">
            Browse cheat sheets <span aria-hidden="true">→</span>
          </a>
          <a class="home-button" href="https://greivinvenegas.com/">Main Website Dashboard</a>
        </div>
      </div>

      <div class="home-terminal" data-reveal="right" aria-label="A short terminal-style introduction">
        <div class="home-terminal__bar" aria-hidden="true">
          <span class="home-terminal__dot"></span>
          <span class="home-terminal__dot"></span>
          <span class="home-terminal__dot"></span>
        </div>
        <pre><span class="prompt">$</span> whoami
<span class="answer">IT &amp; Cloud technician</span>

<span class="prompt">$</span> focus
<span class="answer">Linux · Cloud · Automation</span>

<span class="prompt">$</span> approach
<span class="answer">Keep it simple. Make it useful.</span></pre>
      </div>
    </div>
    <a class="home-scroll-hint" href="#topics-title" aria-label="Scroll to Topics">↓</a>
  </section>
<!--
  <section class="home-section" id="about-me" aria-labelledby="about-title">
    <div class="home-section__inner home-about">
      <div data-reveal="left">
        <p class="home-eyebrow">About me</p>
        <h2 class="home-heading" id="about-title">There is more behind the label.</h2>
        <p class="home-about__aside">
          Technology is my work. Photography is one of the ways I slow down,
          observe, and stay curious.
        </p>
      </div>

      <div class="home-about__copy" data-reveal="right">
        <p>
          I am passionate about photography. I am a simple IT and Cloud technician,
          but there is much more behind that label. Throughout my career, I have had
          the opportunity to face a wide range of technological challenges. Along the
          way, I have collected instructions and specific solutions that I adapted to
          the needs of each situation.
        </p>
        <p>
          Over time, I realized that these small pieces of technical knowledge were
          useful not only to me, but could also help others facing similar situations.
          I decided to use this space to share those instructions—not only as a
          personal record, but also as a way to contribute to the IT community.
        </p>
        <p>
          Publishing and sharing here is also a great way for me to spend my time.
          That is precisely why I avoid formalities. Do not expect long articles or
          unnecessarily complicated technical language. I prefer to keep things
          simple and get straight to the point, writing as directly and clearly as I
          can.
        </p>
        <p>
          If you have found your way here, I hope something I have shared proves
          useful—or at least inspires you to keep learning and exploring. Thank you
          for visiting, and welcome to my digital corner!
        </p>
      </div>
    </div>
  </section>
-->
  <section class="home-section home-section--soft" id="cheat-sheets" aria-labelledby="cheats-title">
    <div class="home-section__inner">
      <h2 class="home-heading" id="cheats-title" data-reveal>Cheat Sheets</h2>
      <p class="home-lead" data-reveal>
        Short, practical references for the tools I reach for often. Open one,
        find the command you need, and get back to work.
      </p>

      <div class="home-cards">

  <a class="home-card" href="cheatsheets/vim/" data-reveal>
    <div class="home-card__top">
      <code class="home-card__command">vim</code>
      <span class="home-card__arrow" aria-hidden="true">→</span>
    </div>
    <p>Modes, movement, editing, search, substitution, registers, and useful commands.</p>
  </a>

  <a class="home-card" href="cheatsheets/tmux/" data-reveal>
    <div class="home-card__top">
      <code class="home-card__command">tmux</code>
      <span class="home-card__arrow" aria-hidden="true">→</span>
    </div>
    <p>Sessions, windows, panes, navigation, resizing, and everyday shortcuts.</p>
  </a>

  <a class="home-card" href="cheatsheets/regex/#CommonTokens" data-reveal>
    <div class="home-card__top">
      <code class="home-card__command">regex .*</code>
      <span class="home-card__arrow" aria-hidden="true">→</span>
    </div>
    <p>Common tokens, anchors, groups, lookarounds, and examples worth keeping nearby.</p>
  </a>

  <a class="home-card" href="cheatsheets/awk/" data-reveal>
    <div class="home-card__top">
      <code class="home-card__command">awk</code>
      <span class="home-card__arrow" aria-hidden="true">→</span>
    </div>
    <p>Patterns, fields, filtering, formatting, and compact text-processing recipes.</p>
  </a>

      </div>
    </div>
  </section>

  <section class="home-section" aria-labelledby="topics-title">
    <div class="home-section__inner">
      <p class="home-eyebrow" data-reveal>What you will find here</p>
      <h2 class="home-heading" id="topics-title" data-reveal>
        Notes shaped by hands-on work.
      </h2>
      <p class="home-lead" data-reveal>
        The site grows as I solve problems, revisit old commands, and turn useful
        discoveries into documentation I can find again.
      </p>

      <div class="home-topics">
        <div class="home-topic" data-reveal>
          <span class="home-topic__number">01</span>
          <h3>Linux &amp; RHCSA</h3>
          <p>Administration notes, troubleshooting steps, and certification study material.</p>
        </div>
        <div class="home-topic" data-reveal>
          <span class="home-topic__number">02</span>
          <h3>Cloud &amp; Automation</h3>
          <p>Repeatable workflows, useful commands, and lessons from building and operating systems.</p>
        </div>
        <div class="home-topic" data-reveal>
          <span class="home-topic__number">03</span>
          <h3>Homelab &amp; Projects</h3>
          <p>Experiments, personal infrastructure, and practical ideas tested outside production.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="home-section home-photo" aria-labelledby="photo-title">
    <div class="home-section__inner home-photo__inner">
      <div data-reveal="left">
        <p class="home-eyebrow">Beyond the terminal</p>
        <h2 class="home-heading" id="photo-title">Photography keeps me looking closer.</h2>
        <p class="home-lead">
          Good technical work and good photography have something in common:
          both reward patience, attention to detail, and a willingness to see a
          familiar problem from a different angle.
        </p>
      </div>
      <div class="home-photo__frame" data-reveal="right" aria-hidden="true"></div>
    </div>
  </section>

  <section class="home-section home-closing" aria-labelledby="closing-title">
    <div class="home-section__inner" data-reveal>
      <p class="home-eyebrow">Start exploring</p>
      <h2 class="home-heading" id="closing-title">Simple notes. Useful answers.</h2>
      <p class="home-lead">
        I hope these references save you a little time—or give you a useful idea
        for the next problem you solve.
      </p>
      <div class="home-actions">
        <a class="home-button" href="#cheat-sheets">
          View the cheat sheets <span aria-hidden="true">↑</span>
        </a>
      </div>
    </div>
  </section>
</div>

<script>
  (() => {
    const setupHomeReveal = () => {
      const root = document.querySelector(".home-page");

      if (!root || root.dataset.revealBound === "true") return;
      root.dataset.revealBound = "true";

      const items = Array.from(root.querySelectorAll("[data-reveal]"));
      const reduceMotion = window.matchMedia(
        "(prefers-reduced-motion: reduce)"
      ).matches;

      if (!("IntersectionObserver" in window) || reduceMotion) {
        items.forEach((item) => item.classList.add("is-visible"));
        return;
      }

      root.classList.add("reveal-ready");

      const observer = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (!entry.isIntersecting) return;
            entry.target.classList.add("is-visible");
            observer.unobserve(entry.target);
          });
        },
        {
          threshold: 0.14,
          rootMargin: "0px 0px -8% 0px",
        }
      );

      items.forEach((item) => observer.observe(item));
    };

    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", setupHomeReveal, { once: true });
    } else {
      setupHomeReveal();
    }

    /* Re-run after Material's instant-navigation page swaps, when enabled. */
    if (typeof document$ !== "undefined") {
      document$.subscribe(setupHomeReveal);
    }
  })();
</script>
