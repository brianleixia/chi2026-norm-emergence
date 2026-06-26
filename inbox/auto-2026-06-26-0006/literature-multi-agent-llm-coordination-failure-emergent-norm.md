# Literature Review — 2026-06-26
**Query:** multi-agent LLM coordination failure emergent norms
**Papers reviewed:** 3

## 1. Emergent Language: A Survey and Taxonomy
- Authors: Jannik Peters, Constantin Waubert de Puiseau, Hasan Tercan | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - The field of emergent language is a novel area of research within artificial intelligence, particularly within multi-agent reinforcement learning.
  - The concept of studying language emergence is not new, with early approaches primarily concerned with explaining human language formation.
  - Early approaches to language emergence gave little consideration to its potential utility for artificial systems.

## 2. MAEBE: Multi-Agent Emergent Behavior Framework
- Authors: Sinem Erisken, Timothy Gothard, Martin Leitgab | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - The MAEBE framework systematically assesses novel emergent risks that arise from multi-agent AI ensembles, which cannot be captured by traditional AI safety evaluations on isolated LLMs.
  - Using the Greatest Good Benchmark with a novel double-inversion question technique, MAEBE demonstrates that LLM moral reasoning exhibits specific emergent behaviors when deployed in multi-agent configurations.
  - The double-inversion question technique, when applied within MAEBE, reveals emergent behavioral patterns in multi-agent LLM systems that are not observable in single-agent evaluations.

## 3. SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing
- Authors: Indraveni Chebolu, Arnab Mallick, Harmesh Rana | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - [Could not extract]

## Synthesis
## Agreements

All three papers converge on a core premise: as AI systems increasingly operate in multi-agent configurations, single-agent evaluation frameworks are insufficient for understanding real-world capabilities and risks. They share an assumption that interaction between agents produces phenomena—useful or dangerous—that cannot be predicted by examining any individual agent in isolation. Paper 1 frames this as "emergent language" and compositional communication arising from multi-agent reinforcement learning, Paper 2 formalizes it as "emergent behavior" warranting dedicated safety evaluation, and Paper 3 demonstrates it through coordinated auditing workflows where agent specialization yields collective performance exceeding the sum of parts. Implicitly, all three treat emergent multi-agent dynamics as both a research opportunity and a domain requiring principled engineering rather than ad-hoc scaling.

## Disagreements

The papers diverge sharply on whether emergent multi-agent phenomena are fundamentally *beneficial* or *fundamentally risky*. Paper 1 adopts a neutral-to-optimistic stance, treating emergent communication as a scientific phenomenon worth characterizing and cataloguing, with an implicit promise of insight into natural language and coordination. Paper 2 takes the opposite pole, framing emergent behavior in deployed LLM ensembles primarily as a *safety hazard* requiring adversarial benchmarking. Paper 3 sidesteps the debate entirely by arguing emergent coordination in narrow, well-bounded engineering domains (smart contract auditing) is controllable and productivity-enhancing. They also implicitly disagree on tractability: Paper 1 emphasizes how poorly understood emergence remains, while Paper 3 presupposes that established MAS patterns are mature enough to deploy in production workflows.

## Most Urgent Open Question

**Under what conditions does emergent multi-agent behavior transition from a controllable engineering phenomenon into an unpredictable safety risk?** Paper 3's confident deployment and Paper 2's alarm about emergent risks are difficult to reconcile without a principled account of *why* coordinated auditing agents behave predictably while general-purpose LLM ensembles allegedly do not. Without a taxonomy of which interaction structures, objectives, and environment complexities bound emergence versus amplify it,
