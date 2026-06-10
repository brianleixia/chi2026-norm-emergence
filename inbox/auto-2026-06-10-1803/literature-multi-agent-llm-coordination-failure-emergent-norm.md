# Literature Review — 2026-06-10
**Query:** multi-agent LLM coordination failure emergent norms
**Papers reviewed:** 3

## 1. Emergent Language: A Survey and Taxonomy
- Authors: Jannik Peters, Constantin Waubert de Puiseau, Hasan Tercan | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - Emergent language is a research area within artificial intelligence, particularly within multi-agent reinforcement learning.
  - Early approaches to studying language emergence were primarily concerned with explaining human language formation with little consideration given to its potential utility for artificial systems.
  - The paper presents a survey and taxonomy of the emergent language field.

## 2. MAEBE: Multi-Agent Emergent Behavior Framework
- Authors: Sinem Erisken, Timothy Gothard, Martin Leitgab | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - Traditional AI safety evaluations on isolated LLMs are insufficient for assessing risks in multi-agent AI ensembles.
  - The MAEBE framework can systematically assess novel emergent risks introduced by multi-agent AI ensembles.
  - Using MAEBE with the Greatest Good Benchmark and a novel double-inversion question technique reveals that LLM moral reasoning exhibits specific emergent behaviors (claim truncated in abstract).

## 3. SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing
- Authors: Indraveni Chebolu, Arnab Mallick, Harmesh Rana | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - SPEAR models auditing as a coordinated mission carried out by specialized agents including a Planning Agent, Execution Agent, and Repair Agent.
  - The Planning Agent prioritizes contracts using risk-aware heuristics.
  - The Execution Agent allocates tasks via the Contract Net protocol.

## Synthesis
**1. What do they agree on?**

All three papers converge on the premise that multi-agent systems (MAS) are a rapidly expanding and consequential area of AI research that demands dedicated frameworks, taxonomies, and evaluation methodologies. Each treats emergent behavior—whether in the form of emergent communication protocols, emergent safety risks, or emergent coordination patterns in applied workflows—as a defining phenomenon that distinguishes MAS from single-agent or isolated-model paradigms. They share an underlying concern with *how interactions between agents give rise to properties not present in any individual agent*, and each implicitly or explicitly argues that tools borrowed from single-agent AI research are insufficient for capturing these dynamics. Furthermore, all three recognize multi-agent interaction as a domain where structure, role differentiation, and coordination mechanisms matter substantially for outcomes.

**2. Where do they disagree?**

The papers diverge sharply in scope, risk framing, and practical orientation. Paper 1 (*Emergent Language: A Survey and Taxonomy*) treats emergent language as a primarily *beneficial* phenomenon to be understood and cultivated, focusing on how communication protocols can arise from multi-agent reinforcement learning in controlled, often game-theoretic settings. Paper 2 (*MAEBE*) inverts this posture, treating emergent behavior in LLM ensembles primarily as a *risk surface*—an attack vector or failure mode requiring defensive evaluation rather than capability elicitation. Paper 3 (*SPEAR*) sidesteps the emergence debate almost entirely, treating multi-agent coordination as an *engineering tool* whose value lies in decomposing a complex real-world task (smart contract auditing) into well-defined agent roles, without claiming that the resulting behavior is emergent in the theoretical sense at all. In short, Paper 1 asks *how does emergence arise and what forms does it take?*, Paper 2 asks *how can emergent interaction cause harm?*, and Paper 3 asks *how can MAS coordination be productively applied?*.

**3. Most urgent open question?**

The most urgent open question is whether there exists a **
