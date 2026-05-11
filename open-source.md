---
layout: page
title: Open Source Projects
description: Open source by Mansura Habiba — own repositories, upstream work (Langflow, IBM MCP Composer), HeunNet, meetup materials, and more on GitHub.
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
    <p>Integrations and examples cover <strong>LangChain</strong>, <strong>LangGraph</strong>, <strong>A2A</strong>, <a href="https://github.com/langflow-ai/langflow" target="_blank" rel="noopener">Langflow</a>, tracing (console and Langfuse), plus a small CLI — licensed under Apache-2.0.</p>
  </li>
  <li>
    <p><strong><a href="https://github.com/mansura-habiba/heunnet" target="_blank" rel="noopener">heunnet</a></strong> — Research artifacts for <em>HeunNet: Extending ResNet using Heun's Methods</em> (Maleki, Habiba, Pearlmutter): Jupyter notebooks and a <code>models</code> directory exploring Heun-type steps with ResNet-style training on MNIST and time-series data, including notebooks that compare against LSTM and phased-LSTM baselines.</p>
  </li>
  <li>
    <strong><a href="https://github.com/mansura-habiba/meetup" target="_blank" rel="noopener">meetup</a></strong>
    — Talk materials (e.g. PyLadies Dublin 2019, Node.js meetup Dublin).
  </li>
</ul>

<div class="section-header" id="contributing">
  <h2>Contributing to</h2>
  <span class="post-meta">Upstream &amp; community</span>
</div>

<p class="post-meta">Broader codebases where work shows up as components, examples, or patches inside upstream communities.</p>

<ul class="pub-list">
  <li>
    <p><strong><a href="https://github.com/langflow-ai/langflow" target="_blank" rel="noopener">Langflow</a></strong> — Open-source visual builder for LLM and agent flows. Collaboration here focuses on custom components and wiring that bring exercise-time identity and delegation into Langflow graphs, aligned with the <a href="https://github.com/mansura-habiba/autonomous-identity" target="_blank" rel="noopener">autonomous-identity</a> Langflow integration path.</p>
  </li>
  <li>
    <p><strong><a href="https://github.com/IBM/mcp-composer" target="_blank" rel="noopener">mcp-composer</a></strong> (<a href="https://github.com/IBM" target="_blank" rel="noopener">IBM</a>) — FastMCP-based orchestrator that registers multiple MCP servers and tools at runtime from structured JSON, forwards invocations to the right upstream MCP server or interface, and exposes a single MCP surface across OpenAPI, GraphQL, CLI tools, client SDKs, and nested MCP servers — Apache-2.0.</p>
  </li>
</ul>
