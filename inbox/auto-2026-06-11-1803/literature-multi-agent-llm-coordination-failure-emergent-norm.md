# Literature Review — 2026-06-11
**Query:** multi-agent LLM coordination failure emergent norms
**Papers reviewed:** 3

## 1. Emergent Language: A Survey and Taxonomy
- Authors: Jannik Peters, Constantin Waubert de Puiseau, Hasan Tercan | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - [Could not extract]

## 2. MAEBE: Multi-Agent Emergent Behavior Framework
- Authors: Sinem Erisken, Timothy Gothard, Martin Leitgab | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - Traditional AI safety evaluations on isolated LLMs are insufficient for multi-agent AI ensembles
  - The MAEBE framework can systematically assess emergent risks in multi-agent AI systems
  - LLM moral reasoning can be evaluated using the Greatest Good Benchmark combined with a double-inversion question technique

## 3. SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing
- Authors: Indraveni Chebolu, Arnab Mallick, Harmesh Rana | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - SPEAR models auditing as a coordinated mission carried out by specialized agents including a Planning Agent, Execution Agent, and Repair Agent
  - The Planning Agent prioritizes contracts using risk-aware heuristics
  - The Execution Agent allocates tasks via the Contract Net protocol

## Synthesis
Based on the paper excerpts provided, here's my synthesis:

**1. Areas of Agreement**

All three papers converge on the recognition that multi-agent systems represent a distinct and increasingly important research frontier, with emergent properties—arising from agent interactions rather than individual capabilities—being central to understanding their behavior. Paper 1 frames emergent language as a phenomenon specific to multi-agent reinforcement learning contexts, while Paper 2 explicitly argues that multi-agent AI ensembles introduce "novel emergent risks" that cannot be captured by evaluating isolated LLMs. Paper 3 reinforces this by demonstrating that established multi-agent system (MAS) patterns can be productively applied to complex real-world coordination problems (smart contract auditing). Together, they establish that the *interactional dynamics* between agents—rather than the capabilities of any single agent—are the locus of both opportunity and risk in this research domain.

**2. Areas of Disagreement**

The papers diverge meaningfully in their *posture toward emergence itself*. Paper 1 treats emergent language as a phenomenon to be *understood and taxonomized*—essentially a neutral object of scientific study worth cataloging. Paper 2 adopts a *cautious, safety-oriented stance*, treating emergent behaviors in deployed multi-agent LLM systems as risks requiring systematic evaluation and mitigation. Paper 3 takes a decidedly *pragmatic-engineering stance*, treating multi-agent coordination not as an emergent phenomenon to study but as an established set of design patterns to be *applied deliberately* toward a practical goal. This represents a spectrum from curiosity-driven observation (Paper 1), to risk-focused evaluation (Paper 2), to pattern-driven construction (Paper 3).

**3. Most Urgent Open Question**

The most pressing unresolved question is: **How can we reliably distinguish *desirable* emergent coordination from *undesirable* emergent risk in deployed multi-agent AI systems?** Paper 3 shows we can deliberately engineer coordination for beneficial ends; Paper 2 warns that the same interactional dynamics can produce unforeseen harmful behaviors; and
