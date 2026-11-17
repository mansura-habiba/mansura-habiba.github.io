---
title: What Software Engineering and Customer Support Had Figured Out Before AI Arrived
subtitle: Why agentic AI keeps showing gains in the same two places, and what the rest of the enterprise has not yet prepared.
date: 2026-11-17
categories: [agentic-ai, enterprise-ai, knowledge-architecture, accountable-knowledge]
---

# What Software Engineering and Customer Support Had Figured Out Before AI Arrived

<TldrCard title="TL;DR" read-time="~10 min">

- Software engineering and customer support keep appearing among the examples where AI is helping. I think part of the reason is what those environments had already prepared for the AI.
- Economics research on earlier technologies reached a similar conclusion: productivity gains depended on complementary changes to organisation, process and data, not on the technology alone.
- Acceptance criteria, definitions of done, UAT, maintained support articles and escalation rules make knowledge contextual, accountable, attributable, composable, on-demand, actionable and auditable.
- Elsewhere in an enterprise, those relationships still depend heavily on people's experience. An agent connected to all those sources is expected to make connections nobody has made explicit.
- Other industries need to spend real time and effort transforming their knowledge into accountable knowledge before they can enable accountable knowledge in action.
- Begin with one workflow: what the task requires, who owns its knowledge, what permits an action and what evidence demonstrates completion.
- Our book [*Accountable Knowledge Architecture for Enterprise AI*](https://leanpub.com/accountable-knowledge-architecture-for-ai) develops one architecture for making these responsibilities explicit.

</TldrCard>

Why is agentic AI transformation not bringing the productivity gains we hoped for across every industry? And why do software engineering and customer support keep appearing among the examples where AI is helping?

I keep coming back to this question.

We can connect a model to enterprise data, give it tools and ask it to complete a task. Then we discover how many things it still needs to understand before it can make a business decision.

Which information applies here? Which source should it trust? Is the policy still current? Who can approve the action? How will we know the job is actually done?

These questions sound familiar to me. They are questions we have spent years learning to answer in software engineering.

And I think that matters more than we sometimes acknowledge.

## The measurable benefits

There are measurable benefits to examine. Research covering 4,867 developers across three companies estimated a 26.08% increase in completed tasks with an AI coding assistant ([Cui et al.](https://doi.org/10.2139/ssrn.4945566), working paper). A peer-reviewed customer-support study in *The Quarterly Journal of Economics* found a 15% increase in issues resolved per hour, with larger benefits for less experienced workers ([Brynjolfsson, Li and Raymond, 2025](https://doi.org/10.1093/qje/qjae044)). An earlier controlled experiment found developers with GitHub Copilot completed a defined programming task 55.8% faster ([Peng et al., 2023](https://arxiv.org/abs/2302.06590)). These were studies of AI assistance in particular settings, but they give us useful examples of where it can help.

Other research shows that the gains depend on the task. In a peer-reviewed experiment published in *Science*, ChatGPT reduced the time for professional writing tasks by 40% and raised quality by 18% ([Noy and Zhang, 2023](https://www.science.org/doi/10.1126/science.adh2586)). A field experiment with 758 consultants at Boston Consulting Group found large gains on tasks inside what the authors call the "jagged technological frontier". On a task outside it, consultants using AI were 19 percentage points less likely to reach the correct answer ([Dell'Acqua et al., 2023](https://doi.org/10.2139/ssrn.4573321), working paper).

So the question is not only whether AI helps. It is where it helps, and why.

This is an old question in economics. Firm-level research on earlier information technology found that the productivity returns depended on complementary changes to workplace organisation, not on the technology alone ([Bresnahan, Brynjolfsson and Hitt, 2002](https://doi.org/10.1162/003355302753399526)). The "productivity J-curve" argument extends this to general-purpose technologies, including AI. Organisations must first make intangible investments in processes, skills and data, and those investments are poorly measured while they are being made ([Brynjolfsson, Rock and Syverson, 2021](https://doi.org/10.1257/mac.20180386)).

My question is what those environments had already prepared for the AI.

<PartDivider eyebrow="Part I" title="Software engineering had already prepared its knowledge" />

Take software engineering. Meet Maya, a software engineer. She is hypothetical, but you have probably worked with her, or been her! As we follow her day, watch for seven words in bold: **contextual**, **accountable**, **attributable**, **composable and interoperable**, **on-demand**, **actionable**, and **explainable and auditable**. I will come back to them!

**9:00.** Maya picks up a ticket: customers want to export their invoices as a CSV file. A requirement does not simply arrive and become source code. If only it were that easy! She checks which services touch invoices, what might break and whether exporting this data raises a privacy question. Now the knowledge is **contextual**. It means something for *this* change. The acceptance criteria say what the file must contain and what should happen for a month with no invoices. The definition of done reminds her that written code does not mean finished work.

**10:30.** One criterion is ambiguous. She does not guess. She asks the product owner, who owns the requirement. Later, a maintainer will challenge her design and an authorised reviewer will accept the work or send it back. That is **accountable** knowledge. Review does more than catch defects, by the way. It also spreads knowledge across the team ([Bacchelli and Bird, 2013](https://doi.org/10.1109/ICSE.2013.6606617)).

**13:00.** While coding, she needs the specification, the invoice service and its interfaces. Not the HR handbook. Not last year's architecture deck. She needs the right knowledge **on-demand**, for the decision in front of her.

<AnnotatedFigure
  :number="1"
  caption="Software already has a way to judge the work. The decision changes at each stage; earlier requirements remain part of the evidence."
  notice="Contextual and on-demand knowledge is selected and reassessed for the decision being made now. The other five characteristics hold across the whole lifecycle.">

<img src="/figures/software-lifecycle-knowledge.png" alt="Software lifecycle stages and the knowledge each needs. Understand: users and purpose, acceptance criteria, definition of done. Implement: relevant code, interfaces, dependencies. Validate: tests and reviews, UAT scenarios, observed behaviour. Release: approvals, security findings, rollback readiness. Observe: production results, incidents, corrective changes. Contextual and on-demand: select and reassess knowledge for the decision being made now. Across the lifecycle: accountable owners, attributable sources, composable and interoperable records, actionable evidence with separate authority checks, explainable and auditable outcomes." />

</AnnotatedFigure>

Models are no different. Their performance can drop when the important part is buried in the middle of a long input ([Liu et al., 2024](https://doi.org/10.1162/tacl_a_00638)). Giving an agent everything is not the same as giving it what the decision needs.

**15:00.** Her pull request links back to the ticket. The build attaches the test results. A short design note explains why she streamed the file instead of building it in memory. Anyone can now ask where an assumption came from and find something more useful than, "Well, the agent suggested it." **Attributable**. The ticket lives in an issue tracker, the code in a repository and the evidence in a build platform, and they still work together. **Composable and interoperable**.

**16:30.** One test fails on the empty month, and it sends her back. The next morning the tests pass, and UAT confirms that the finance team's workflow works. The release evidence supports a deployment, but the release approval still decides whether it goes. **Actionable**.

**Three weeks later,** someone reports a broken export at month-end. The on-call engineer follows the trail from the incident to the release, the change, the review and the original acceptance criteria. She can see what was expected and what actually happened. **Explainable and auditable**.

None of Maya's day came with AI. We built these habits over decades, mostly after learning the hard way why we needed them.

## The agent enters a prepared environment

Now give Maya a coding agent. It reads the ticket, finds the code, makes a change, runs the tests and gets feedback. Her workflow already knows how to judge its work and limit what it can do. That is a considerable head start!

Researchers lean on it too. SWE-bench builds its tasks from 2,294 real GitHub issues and counts a fix only when the repository's own tests pass ([Jimenez et al., 2024](https://arxiv.org/abs/2310.06770), ICLR).

It does not mean AI always makes us faster. In a randomised trial, experienced open-source developers took 19% longer with early-2025 tools, while believing AI had sped them up ([METR, 2025](https://arxiv.org/abs/2507.09089), preprint). The tools, the task and the review effort still matter.

But look how much of the work we can already explain to the agent: what it should achieve, which evidence matters and what counts as done.

<PartDivider eyebrow="Part II" title="Customer support had prepared its knowledge too" />

## A support centre is already a knowledge service

Think about what a support centre actually does all day. A question comes in. Someone finds the knowledge that applies to *this* customer, checks it against an approved policy, acts within their authority and records what happened. Then the next question comes in.

That is very close to what we ask an agent to do with retrieval-augmented generation (RAG): retrieve the right knowledge, reason over it and respond. So a large part of a support centre can be mimicked by an agent sitting on a RAG service, *if* the knowledge behind that service is accountable. Retrieval alone is not enough. The service needs all seven words.

It has to be **on-demand** first of all. A support conversation changes as it goes. Take a customer asking why they were charged twice. At first a billing explanation may be enough. Then we learn one charge is pending, or both have settled, and suddenly the agent needs transaction evidence, the refund policy and an approval limit.

<AnnotatedFigure
  :number="2"
  caption="A support conversation changes what the agent needs. Illustrative case: a customer asks why they were charged twice."
  notice="New facts can require new knowledge. A billing explanation may be enough at first; a refund needs transaction evidence and authority.">

<img src="/figures/support-conversation-knowledge.png" alt="Support case stages and the knowledge each needs. Identify the case: correct customer, correct purchase, account context. Investigate: transaction status, pending or settled, applicable policy. Choose a remedy: evidence for a refund, approval limit, escalation conditions. Verify resolution: refund result, customer follow-up, retained case record. Approved sources, named owners and case histories make the response reviewable." />

</AnnotatedFigure>

The other six matter just as much:

- **Contextual:** the right customer, the right purchase, the right account, not a general billing article.
- **Attributable:** the answer cites an approved, versioned policy, and a transaction record stays distinct from a previous agent's note about it.
- **Accountable:** someone maintains each support article, corrects outdated guidance and approves exceptions. Every case has an owner.
- **Composable and interoperable:** billing, order and account records line up on the same customer and purchase.
- **Actionable:** the evidence supports a remedy, and the authority to issue it is checked separately.
- **Explainable and auditable:** the case history, policy reference, approval and result show whether the customer was actually helped. Closing the ticket does not prove they got their money back!

Mature support centres built most of this long before generative AI: maintained knowledge bases, approved policies, escalation rules, case ownership and case histories. So when an agent arrives, the knowledge service it needs is largely already there. I think that is a big reason this industry shows some of the clearest gains from AI.

The support study fits this picture. The assistant appears to have spread the habits of the best agents to newer ones ([Brynjolfsson, Li and Raymond, 2025](https://doi.org/10.1093/qje/qjae044)). It learned from a record of resolved conversations that someone had to build and keep first.

It is not magic, though. In τ-bench, agents following written retail and airline policies completed fewer than half the tasks, and were much less consistent on repeated attempts ([Yao et al., 2024](https://arxiv.org/abs/2406.12045), preprint). A well-kept knowledge base is necessary. Applying it reliably is something we still have to check.

<PartDivider eyebrow="Part III" title="The common advantage" />

## Accountable knowledge in action

So, what is the common advantage?

I think an important part of the secret sauce is accountable knowledge in action.

### What accountable knowledge means

Enterprise data gives us records, transactions, documents and events. Enterprise knowledge adds business meaning and relationships, so we can interpret that data. **Accountable knowledge** adds verifiable evidence, explicit governance and conditions for use to that understanding. Whether it is fit for a decision depends on the context, its validity and whether the evidence is adequate.

**Knowledge in action** is how that knowledge is used: by people or agents reasoning, deciding and acting, within delegated authority, and leaving records that let someone verify the outcome.

The seven words from Parts I and II are its defining characteristics. They describe what has to be preserved as the knowledge is assembled and used.

1. **Accountable.** Knowledge has an identified owner, explicit validity and governance conditions, and a managed lifecycle. Responsibility for accepting, correcting and retiring it is clear.
2. **Contextual.** Knowledge keeps the business meaning, relationships, dependencies and qualifications needed for a particular task or decision.
3. **On-demand.** Knowledge is discoverable and composable at the point of need. What is selected, and how it is checked, changes as the task, evidence and conditions change.
4. **Actionable.** Knowledge supports the assessment of possible actions through evidence, uncertainty and business constraints. Execution remains subject to policy, delegated authority and approval.
5. **Attributable.** Claims keep their origins and supporting evidence. Enterprise records, external evidence, model-generated inferences, user input and tool observations stay distinguishable, so their authority can be assessed.
6. **Composable and interoperable.** Knowledge can be interpreted and combined across systems, domains and organisations while keeping its meaning, provenance, qualifications and permitted use.
7. **Explainable and auditable.** Selection, decisions and actions leave enough evidence for independent review: what was known, which rules applied, what was authorised and what happened.

<AnnotatedFigure
  :number="3"
  caption="What makes knowledge usable for an agent? Each characteristic answers one question about the task."
  notice="The right knowledge changes with the task.">

<img src="/figures/akai-seven-characteristics.jpg" alt="What makes knowledge usable for an agent. 1 Contextual: what does it mean for this task? Preserve identity, relationships and business scope. 2 On-demand: what is needed at this point? Discover, assemble and reassess as conditions change. 3 Attributable: where did it come from? Distinguish source observations from interpretation. 4 Accountable: who maintains it? Assign ownership and govern correction and retirement. 5 Composable and interoperable: can different domains use it together? Preserve meaning and permitted use across boundaries. 6 Actionable: which next step does it support? Assess options; check execution authority separately. 7 Explainable and auditable: can we review the decision and result? Retain the context, reasoning basis and observed outcome." />

</AnnotatedFigure>

Neither software engineering nor customer support uses this vocabulary. But look back at Maya's day and the support centre. Every one of these questions already had an answer.

These fields had already started adopting its practices, even if they never called them that. Acceptance criteria, definitions of done, UAT, maintained support articles and escalation rules all help answer the same practical question.

<PullQuote>

What must we know, and what must we check, before this work can move forward?

</PullQuote>

The productivity studies do not prove that these practices caused the gains. This is my interpretation of the architectural advantage. It is consistent with the complementary-investment research above, and with benchmarks that take their tasks and checks from these same workflows. Mature software and support teams had already made parts of their knowledge usable within a controlled process. AI could participate in something that was established.

## Elsewhere, the connections live in people

Elsewhere in an enterprise, those relationships may still depend heavily on people's experience.

The policy exists, but someone knows it has an exception. The record exists, but someone knows the status means something different in another system. An approval was given, but the conditions are buried in an email. A specialist knows which evidence is missing because they have handled the same situation for years.

Knowledge-management research has a name for this. Polanyi described tacit knowledge as knowing more than we can tell ([Polanyi, 1966](https://press.uchicago.edu/ucp/books/book/chicago/T/bo6035368.html)). Nonaka and Takeuchi described how organisations turn tacit knowledge into explicit, shared knowledge, and why that conversion takes deliberate effort ([Nonaka and Takeuchi, 1995](https://global.oup.com/academic/product/the-knowledge-creating-company-9780195092691)).

We connect an LLM to all those sources and expect it to make the connections correctly.

But have we made those connections explicit enough for anyone to follow?

This is where I think we need to put more effort. An agent needs the right knowledge at the right time to make the right decision for the given task. It also needs to recognise when that knowledge is insufficient.

Otherwise, its nondeterministic reasoning may take a different turn. Yes, it might reach a solution, but not the solution the business required.

A payment may be technically possible while still lacking approval. A support answer may be reasonable while applying the wrong policy. A software change may pass its tests while missing the user's acceptance criteria.

So here is the uncomfortable part. Most industries cannot simply plug in an agent and expect the support-centre result. They first have to do the work software and support did over years: turn the knowledge they already have into accountable knowledge. That means giving each policy and record an owner, recording where each claim came from and when it stops being valid, making the meaning survive between systems, and writing down what permits an action and what proves it worked.

That takes real time and effort. It is not a side task for the AI team. But it is what makes accountable knowledge in action possible, and I do not see a shortcut around it.

## Why "in action" matters

This is why I keep emphasising *in action*.

The characteristics need to exist in the architecture and the way the organisation works. Someone owns the knowledge. Something assesses whether it is adequate for the task. A separate control checks permission to execute. Changes trigger reassessment, and the outcome leaves evidence.

Standards and regulation are moving in the same direction. The NIST AI Risk Management Framework places accountability, roles and documentation under its Govern function ([NIST, 2023](https://doi.org/10.6028/NIST.AI.100-1)). The EU AI Act requires high-risk AI systems to support automatic record-keeping and effective human oversight (Articles 12 and 14, [Regulation (EU) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)). The W3C PROV model gives a standard vocabulary for recording which entity, activity and agent produced a piece of information ([W3C, 2013](https://www.w3.org/TR/prov-dm/)).

Consider an agent processing an invoice. It matches the purchase order and goods receipt, but a required compliance assessment is missing.

The architecture must make that gap visible. When the assessment arrives, the task can be reassessed. Payment still needs the required authority and approval. After dispatch, the system must establish whether the payment happened. A missing response cannot simply become a reason to pay again.

<AsideNote title="One architectural approach">

In our book, [*Accountable Knowledge Architecture for Enterprise AI*](https://leanpub.com/accountable-knowledge-architecture-for-ai), we develop this through Accountable Knowledge Units (AKU) that preserve governed claims, Knowledge Context Packages (KCP) that assemble and assess them for a task, and a proposed Knowledge Context Exchange Protocol (KCEP) that lets services request and refresh that context. Execution remains under a separate action gateway.

That is one architectural approach to making these responsibilities explicit.

</AsideNote>

<AnnotatedFigure
  :number="4"
  caption="From the book: AKU, KCP and KCEP each carry one level of accountability."
  notice="Claim level, task level and interaction level. A positive knowledge assessment never replaces the separate check on authority, policy and approvals at the Governed Action Gateway.">

<img src="/figures/akai-aku-kcp-kcep.png" alt="Claims, context and governed action. The Accountable Knowledge Core governs Accountable Knowledge Units (claim level: is this statement supported, owned and still valid?). Knowledge Composition Services assemble a Knowledge Context Package (task level: is the assembled evidence adequate for this purpose?). An enterprise agent requests, inspects, verifies and refreshes context through the KCEP interface (interaction level). Proposed actions pass through a Governed Action Gateway that verifies context and checks authority before the enterprise workflow runs." />

</AnnotatedFigure>

## Where to begin

We can begin with one workflow. Establish what the task requires, who owns its knowledge, what permits an action and what evidence demonstrates completion. Then test what happens when information is missing or conditions change.

Software engineering and customer support give us something useful to learn from. Their more mature practices had already done part of this preparation before AI arrived.

I believe that preparation deserves much more attention in our transformation plans. Budget for it, staff it and measure it, the same way we budget for the model and the platform. Transforming enterprise knowledge into accountable knowledge is the investment that lets agents take part in the work.

<PullQuote>

If we want agents to take responsibility for more work, we first need to make the knowledge behind that work usable, governed and connected to its outcome.

</PullQuote>

That is the problem we explore in [*Accountable Knowledge Architecture for Enterprise AI*](https://leanpub.com/accountable-knowledge-architecture-for-ai).

<aside class="feature-card is-top" aria-label="Featured book">
  <a href="https://leanpub.com/accountable-knowledge-architecture-for-ai" target="_blank" rel="noopener">
    <img src="/books/accountable-knowledge-architecture-cover.png" alt="Accountable Knowledge Architecture for Enterprise AI — book cover" loading="lazy" />
  </a>
  <div>
    <p class="feature-eyebrow">The book</p>
    <h3>Accountable Knowledge Architecture for Enterprise AI</h3>
    <p class="feature-meta">Designing Distributed Knowledge Systems for Humans, Models, and Autonomous Agents<br />Mansura Habiba, Rafflesia Khan and Nafiul Islam Khan · Leanpub</p>
    <p>
      How to make the knowledge behind enterprise work usable, governed and connected to its outcome,
      so agents can take responsibility for more of that work.
    </p>
    <ul>
      <li><strong>Accountable Knowledge Units (AKU)</strong> preserve governed claims: who owns them, where they came from and whether they still hold.</li>
      <li><strong>Knowledge Context Packages (KCP)</strong> assemble those claims for a task and assess whether they are adequate for the decision.</li>
      <li>The proposed <strong>Knowledge Context Exchange Protocol (KCEP)</strong> lets services request and refresh that context as conditions change.</li>
      <li>Execution stays under a separate <strong>Governed Action Gateway</strong>, so knowing what should happen and being permitted to do it remain separate checks.</li>
    </ul>
    <a class="btn btn-primary" href="https://leanpub.com/accountable-knowledge-architecture-for-ai" target="_blank" rel="noopener">Get it on Leanpub →</a>
  </div>
</aside>

<AnnotatedFigure
  :number="5"
  caption="From the book: seven principles guide every layer of the architecture."
  notice="The seven characteristics in this post become the architecture's pillars. These principles guide decisions across them.">

<img src="/figures/akai-seven-principles.png" alt="Seven design principles from Accountable Knowledge Architecture for Enterprise AI: keep knowledge connected to its evidence; separate knowledge formation from decision use; assess adequacy for the intended purpose; enforce authority at the point of action; design for changing knowledge; preserve meaning and restrictions across boundaries; record decisions and recover uncertain outcomes." />

</AnnotatedFigure>

## References

### Peer-reviewed

- Erik Brynjolfsson, Danielle Li and Lindsey Raymond, [Generative AI at Work](https://doi.org/10.1093/qje/qjae044), *The Quarterly Journal of Economics* 140(2), 2025.
- Shakked Noy and Whitney Zhang, [Experimental evidence on the productivity effects of generative artificial intelligence](https://www.science.org/doi/10.1126/science.adh2586), *Science* 381(6654), 2023.
- Timothy F. Bresnahan, Erik Brynjolfsson and Lorin M. Hitt, [Information Technology, Workplace Organization, and the Demand for Skilled Labor: Firm-Level Evidence](https://doi.org/10.1162/003355302753399526), *The Quarterly Journal of Economics* 117(1), 2002.
- Erik Brynjolfsson, Daniel Rock and Chad Syverson, [The Productivity J-Curve: How Intangibles Complement General Purpose Technologies](https://doi.org/10.1257/mac.20180386), *American Economic Journal: Macroeconomics* 13(1), 2021.
- Carlos E. Jimenez et al., [SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](https://arxiv.org/abs/2310.06770), ICLR 2024.
- Nelson F. Liu et al., [Lost in the Middle: How Language Models Use Long Contexts](https://doi.org/10.1162/tacl_a_00638), *Transactions of the Association for Computational Linguistics* 12, 2024.
- Alberto Bacchelli and Christian Bird, [Expectations, Outcomes, and Challenges of Modern Code Review](https://doi.org/10.1109/ICSE.2013.6606617), ICSE 2013.

### Working papers and preprints

- Kevin Zheyuan Cui, Mert Demirer, Sonia Jaffe, Leon Musolff, Sida Peng and Tobias Salz, [The Effects of Generative AI on High-Skilled Work: Evidence from Three Field Experiments with Software Developers](https://doi.org/10.2139/ssrn.4945566), SSRN.
- Fabrizio Dell'Acqua et al., [Navigating the Jagged Technological Frontier](https://doi.org/10.2139/ssrn.4573321), Harvard Business School Working Paper 24-013, 2023.
- Sida Peng, Eirini Kalliamvakou, Peter Cihon and Mert Demirer, [The Impact of AI on Developer Productivity: Evidence from GitHub Copilot](https://arxiv.org/abs/2302.06590), arXiv, 2023.
- Joel Becker, Nate Rush, Elizabeth Barnes and David Rein (METR), [Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](https://arxiv.org/abs/2507.09089), arXiv, 2025.
- Shunyu Yao, Noah Shinn, Pedram Razavi and Karthik Narasimhan, [τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](https://arxiv.org/abs/2406.12045), arXiv, 2024.

### Books, standards and regulation

- Michael Polanyi, [The Tacit Dimension](https://press.uchicago.edu/ucp/books/book/chicago/T/bo6035368.html), 1966.
- Ikujiro Nonaka and Hirotaka Takeuchi, [The Knowledge-Creating Company](https://global.oup.com/academic/product/the-knowledge-creating-company-9780195092691), Oxford University Press, 1995.
- NIST, [Artificial Intelligence Risk Management Framework (AI RMF 1.0)](https://doi.org/10.6028/NIST.AI.100-1), NIST AI 100-1, 2023.
- European Union, [Regulation (EU) 2024/1689 (Artificial Intelligence Act)](https://eur-lex.europa.eu/eli/reg/2024/1689/oj), 2024.
- W3C, [PROV-DM: The PROV Data Model](https://www.w3.org/TR/prov-dm/), W3C Recommendation, 2013.
