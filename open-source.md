---
layout: page
title: Open Source Projects
description: Open source by Mansura Habiba — autonomous-identity (agent identity envelopes), meetup talks, and more on GitHub.
sidebar: false
aside: false
outline: false
---

<p class="page-eyebrow">Code &amp; community</p>

# Open Source Projects

Talk slides, demos, and other public repositories live on [GitHub](https://github.com/mansura-habiba). Highlights from this site's publications page:

<div class="section-header" id="repos">
  <h2>Repositories</h2>
  <span class="post-meta">Selected</span>
</div>

<ul class="pub-list">
  <li>
    <p><strong><a href="https://github.com/mansura-habiba/autonomous-identity" target="_blank" rel="noopener">autonomous-identity</a></strong> — Python library for <strong>identity at the moment of action</strong>: each tool call, state change, or delegation carries a portable <strong>identity envelope</strong> that describes who is acting, under what scopes, and with what provenance.</p>
    <p>At every <strong>material exercise</strong>, the library re-verifies that envelope against the current lifecycle state, active grants, and a <strong>signed delegation chain</strong> anchored to a human, team, or organization.</p>
    <p>The design targets eight governability properties together — persistence, addressability, cryptographic verifiability at exercise time, attenuating delegation, instance specificity, provenance binding, lifecycle control, and audit linkage — with pluggable <strong>IdentityAdapter</strong> implementations (for example SPIFFE-shaped envelopes and Merkle-chain histories) where each construction favors different trade-offs.</p>
    <p>Framework-free core types pair with storage backends (file, SQLite, Postgres) and append-only audit trails so verification and revocation stay visible across processes.</p>
    <p>Integrations and examples cover <strong>LangChain</strong>, <strong>LangGraph</strong>, <strong>A2A</strong>, Langflow, tracing (console and Langfuse), plus a small CLI — licensed under Apache-2.0.</p>
  </li>
  <li>
    <strong><a href="https://github.com/mansura-habiba/meetup" target="_blank" rel="noopener">meetup</a></strong>
    — Talk materials (e.g. PyLadies Dublin 2019, Node.js meetup Dublin).
  </li>
</ul>
