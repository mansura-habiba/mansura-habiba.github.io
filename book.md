---
layout: page
title: Books
description: Books authored by Mansura Habiba — Recent Trends in Modelling Continuous Time Series (Springer, 2026), Emergence of Agentic AI (Leanpub, 2025), and Hybrid Cloud Infrastructure and Operations Explained (Packt, 2022).
sidebar: false
aside: false
outline: false
---

<p class="page-eyebrow">Books</p>

# Books

Three published titles spanning continuous-time deep learning, agentic AI architecture, and hybrid cloud operations. Each book is written for the practitioner who has to make the architecture decision on Monday morning — not just understand it.

<!-- ============================================================= -->
<!-- 1. Recent Trends in Modelling the Continuous Time Series  ---- -->
<!-- ============================================================= -->

<article class="book-detail is-latest">
  <div class="book-detail-cover">
    <a href="https://link.springer.com/book/9783032180216" target="_blank" rel="noopener">
      <img src="https://media.springernature.com/w158/springer-static/cover/book/978-3-032-18021-6.jpg" alt="Recent Trends in Modelling the Continuous Time Series using Deep Learning — book cover" loading="lazy">
    </a>
    <a class="btn btn-primary book-detail-cta" href="https://link.springer.com/book/9783032180216" target="_blank" rel="noopener">Springer page →</a>
  </div>
  <div class="book-detail-body">

  <h2>Recent Trends in Modelling the Continuous Time Series using Deep Learning</h2>
  <p class="book-detail-publisher">Springer · 2026 · ISBN 978-3-032-18021-6</p>
  <p class="book-detail-tagline">A research monograph on neural ODEs and continuous-time models for messy, irregularly sampled time-series — including data with informative missingness.</p>

  ### About the book

  Most production time-series data isn't clean and regularly sampled. Sensors drop readings, patients miss appointments, financial markets close on weekends, and the missingness itself often carries signal. Classical deep-learning models — RNNs, transformers, even modern state-space models — assume an even tick of a clock that real-world data doesn't honour.

  This book traces the research that emerged from that mismatch: **neural ordinary differential equations**, **latent-ODE recurrent networks**, and the family of continuous-time models that treat time as a continuous variable rather than a discretised index. It is grounded in original research from my Ph.D. with Prof. Barak Pearlmutter at Maynooth University, and extended into the broader landscape of continuous-time deep learning that has matured since.

  ### Who it's for

  - **Researchers and grad students** working on time-series, healthcare data, or scientific machine learning who need a structured introduction to neural ODE-family models.
  - **ML engineers** dealing with irregular sampling, sensor data, EHRs, or other domains where missingness is informative rather than random.
  - **Architects and tech leads** evaluating whether continuous-time models are a fit for their problem before investing engineering effort.

  ### What the book covers

  - The mathematical foundations of neural ODEs and their adjoint sensitivity training.
  - Recurrent variants: **ODE-RNN**, **Latent ODE**, and continuous-time autoencoders.
  - Modelling **informative missingness** — when "no data" is itself a feature.
  - Numerical-solver trade-offs (fixed-step vs. adaptive) and what they mean for stability and cost.
  - Practical considerations: what to do when an ODE solver diverges in production.

  <div class="book-detail-meta">
    <a class="meta-pill" href="https://link.springer.com/book/9783032180216" target="_blank" rel="noopener">Springer</a>
    <a class="meta-pill" href="https://arxiv.org/abs/2409.09106" target="_blank" rel="noopener">Related papers</a>
  </div>

  </div>
</article>

<!-- ============================================================= -->
<!-- 2. Emergence of Agentic AI  --------------------------------- -->
<!-- ============================================================= -->

<article class="book-detail">
  <div class="book-detail-cover">
    <a href="https://leanpub.com/emergence-agentic-ai" target="_blank" rel="noopener">
      <img src="https://d2sofvawe08yqg.cloudfront.net/emergence-agentic-ai/s_hero?1746930297&amp;1746930297" alt="Emergence of Agentic AI — book cover" loading="lazy">
    </a>
    <a class="btn btn-primary book-detail-cta" href="https://leanpub.com/emergence-agentic-ai" target="_blank" rel="noopener">Get the book →</a>
  </div>
  <div class="book-detail-body">

  <h2>Emergence of Agentic AI</h2>
  <p class="book-detail-publisher">Leanpub · 2025 · Architecting the Next Generation of Intelligent Systems</p>
  <p class="book-detail-tagline">A practical framework for designing, securing, and operating agentic AI systems — the runtime layer most teams discover only after the demo ships.</p>

  ### About the book

  Agentic AI is being deployed faster than the architecture patterns to support it have stabilised. Most teams are shipping agents on stacks that were designed for stateless inference, with security models that assume a human is always in the loop. This book is the field guide I wish existed when I started building agentic platforms inside an enterprise: an architectural treatment of agents, runtimes, identity, and chain-of-custody, with the lessons that aviation, healthcare, and chain-of-custody-heavy industries can lend to AI.

  ### Who it's for

  - **Enterprise architects** moving from chatbots to action-taking agents and discovering the runtime gaps.
  - **Security engineers** trying to apply zero-trust thinking to systems that *act* rather than just *retrieve*.
  - **Engineering leaders** sizing the operational cost — and risk — of an agentic deployment.

  ### What the book covers

  - The reference anatomy of an agentic system: planner, executor, memory, tools, runtime.
  - **Identity and delegation** — when an agent acts "on behalf of" a user, what's actually being signed?
  - **Chain-of-custody** for AI actions, drawing patterns from clinical labs, aviation, and pharma.
  - Sandboxing and least-privilege execution environments for agents.
  - Failure modes specific to agentic systems — and how to design blameless post-mortems for them.
  - The operational economics of agentic platforms in production.

  <div class="book-detail-meta">
    <a class="meta-pill" href="https://leanpub.com/emergence-agentic-ai" target="_blank" rel="noopener">Leanpub</a>
    <a class="meta-pill" href="/blog/">Related writing</a>
  </div>

  </div>
</article>

<!-- ============================================================= -->
<!-- 3. Hybrid Cloud Infrastructure and Operations Explained ---- -->
<!-- ============================================================= -->

<article class="book-detail">
  <div class="book-detail-cover">
    <a href="https://packt.link/a/9781803248318" target="_blank" rel="noopener">
      <img src="https://m.media-amazon.com/images/I/81l1weci4RL._SL1500,204,203,200_.jpg" alt="Hybrid Cloud Infrastructure and Operations Explained — book cover" loading="lazy">
    </a>
    <a class="btn btn-primary book-detail-cta" href="https://packt.link/a/9781803248318" target="_blank" rel="noopener">Get the book →</a>
  </div>
  <div class="book-detail-body">

  <h2>Hybrid Cloud Infrastructure and Operations Explained</h2>
  <p class="book-detail-publisher">Packt Publishing · 2022 · ISBN 978-1-80324-831-8</p>
  <p class="book-detail-tagline">A practitioner's guide to modernising enterprise infrastructure with IBM Cloud and Red Hat — covering cloud architecture, migration patterns, and Day-2 operations.</p>

  ### About the book

  Most "cloud migration" books treat the cloud as the destination and skip lightly past the operational reality of running production workloads after the move. This one starts from the assumption that you'll be operating a hybrid estate — some workloads on-prem, some on IBM Cloud, some on a managed Kubernetes platform like OpenShift — and that the architecture has to make Day-2 operations possible, not just Day-1 cutover.

  ### Who it's for

  - **Cloud architects** designing reference architectures across IBM Cloud and Red Hat OpenShift.
  - **Platform engineers** running hybrid estates where workloads have to move between environments without rework.
  - **CIOs and tech leads** scoping a modernisation programme and trying to understand what operational maturity actually costs.

  ### What the book covers

  - Hybrid cloud reference architectures and the design trade-offs that go into each layer.
  - Workload migration patterns — rehost, replatform, refactor — and when each is the right call.
  - **IBM Cloud and Red Hat OpenShift** specifically: their place in the hybrid stack and how they interoperate with other clouds.
  - Day-2 operations: monitoring, capacity planning, incident response on hybrid platforms.
  - Security and compliance considerations that don't survive a naive lift-and-shift.

  <div class="book-detail-meta">
    <a class="meta-pill" href="https://packt.link/a/9781803248318" target="_blank" rel="noopener">Packt</a>
    <a class="meta-pill" href="https://partnerships.packt.com/edit-post-6/" target="_blank" rel="noopener">Author interview</a>
  </div>

  </div>
</article>

---

## Reviews and editorial roles

In addition to authoring, I serve as a peer reviewer and editorial board member for several IEEE journals and conferences, with a focus on AI security, cloud architecture, and continuous-time modelling. The current list is in the [full CV](/cv.html).

## Want updates on new books?

The fastest signal is on [LinkedIn](https://www.linkedin.com/in/mansura-h-a0174a19) — that's where I post when a new title goes into early access or release. For research papers, [Google Scholar](https://scholar.google.com/citations?user=oee3rpwAAAAJ) is the canonical list.
