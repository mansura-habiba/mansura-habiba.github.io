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

Talk slides, demos, and other public repositories live on [GitHub](https://github.com/mansura-habiba).

<div class="section-header" id="repos">
  <h2>Repositories</h2>
  <span class="post-meta">Selected</span>
</div>

<OpenSourceGrid>
  <OpenSourceCard
    title="autonomous-identity"
    href="https://github.com/mansura-habiba/autonomous-identity"
    :lines="[
      'Python library for identity at the moment of action — each tool call, state change, or delegation carries a portable identity envelope.',
      'Re-verifies that envelope at every material exercise against lifecycle state, active grants, and a signed delegation chain.',
      'Framework-free core with LangChain, LangGraph, A2A, Langflow, and tracing integrations — Apache-2.0.',
    ]"
    :tags="['python', 'library', 'identity', 'agents', 'langchain', 'langflow']"
  />
  <OpenSourceCard
    title="heunnet"
    href="https://github.com/mansura-habiba/heunnet"
    :lines="[
      'Research artifacts for HeunNet: extending ResNet using Heun\'s methods (Maleki, Habiba, Pearlmutter).',
      'Jupyter notebooks and a models directory for MNIST and time-series experiments.',
      'Includes comparisons against LSTM and phased-LSTM baselines.',
    ]"
    :tags="['python', 'neural network', 'jupyter', 'research', 'resnet']"
  />
  <OpenSourceCard
    title="meetup"
    href="https://github.com/mansura-habiba/meetup"
    :lines="[
      'Public talk slides and demo materials from community meetups.',
      'Includes PyLadies Dublin 2019 and Node.js meetup Dublin sessions.',
      'Lightweight repos meant for sharing code and examples from live talks.',
    ]"
    :tags="['talks', 'community', 'python', 'nodejs']"
  />
</OpenSourceGrid>

<div class="section-header" id="contributing">
  <h2>Contributing to</h2>
  <span class="post-meta">Upstream &amp; community</span>
</div>

<p class="post-meta">Broader codebases where work shows up as components, examples, or patches inside upstream communities.</p>

<OpenSourceGrid>
  <OpenSourceCard
    title="Langflow"
    href="https://github.com/langflow-ai/langflow"
    :lines="[
      'Open-source visual builder for LLM and agent flows.',
      'Collaboration focuses on custom components that bring exercise-time identity into Langflow graphs.',
      'Aligned with the autonomous-identity Langflow integration path.',
    ]"
    :tags="['langflow', 'agents', 'identity', 'visual builder', 'upstream']"
  />
  <OpenSourceCard
    title="mcp-composer"
    href="https://github.com/IBM/mcp-composer"
    :lines="[
      'IBM FastMCP orchestrator — registers multiple MCP servers and tools at runtime from structured JSON.',
      'Forwards invocations to the right upstream server and exposes a single MCP surface across OpenAPI, GraphQL, CLI, and SDKs.',
      'Apache-2.0 upstream collaboration.',
    ]"
    :tags="['mcp', 'python', 'ibm', 'orchestration', 'upstream']"
  />
</OpenSourceGrid>
