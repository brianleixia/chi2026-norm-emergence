# Literature Review — 2026-06-14
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
  - Traditional AI safety evaluations on isolated LLMs are insufficient for assessing multi-agent AI ensembles.
  - The MAEBE framework can systematically assess novel emergent risks introduced by multi-agent AI ensembles.
  - The Greatest Good Benchmark combined with a novel double-inversion question technique reveals that LLM moral [reasoning shows specific patterns in multi-agent settings].

## 3. SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing
- Authors: Indraveni Chebolu, Arnab Mallick, Harmesh Rana | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - SPEAR models auditing as a coordinated mission carried out by specialized agents, including a Planning Agent that prioritizes contracts using risk-aware heuristics.
  - An Execution Agent in SPEAR allocates tasks via the Contract Net protocol.
  - SPEAR applies established multi-agent systems (MAS) patterns in a realistic smart contract security analysis workflow.

## Synthesis
Based on the three paper excerpts provided, here is a synthesis:

**1. Points of Agreement:**
All three papers recognize that multi-agent systems (MAS) introduce fundamentally new dynamics that cannot be understood by studying individual agents in isolation. Each treats emergent phenomena—whether linguistic, behavioral, or coordinative—as a central object of study, and each frames such emergence as both a powerful capability and a source of complexity that demands systematic analysis. They also implicitly share an assumption that principled frameworks (taxonomies, evaluation benchmarks, or engineering patterns) are necessary to move multi-agent research from ad-hoc demonstration to rigorous discipline.

**2. Points of Disagreement:**
The papers differ sharply in normative posture toward emergent multi-agent behavior. The emergent language survey (Paper 1) treats emergence primarily as a phenomenon to be *characterized and understood*, documenting it neutrally as a research direction. The MAEBE framework (Paper 2) adopts an explicitly *adversarial, safety-oriented stance*, treating emergent behaviors as potential risks requiring evaluation and mitigation. SPEAR (Paper 3), by contrast, is *constructive and applied*, deliberately engineering multi-agent coordination for a specific productive workflow and treating emergence as a design feature rather than a hazard. This yields divergent research agendas: observation and taxonomy versus risk evaluation versus engineered deployment.

**3. Most Urgent Open Question:**
How can the field develop principled methods to *distinguish productive emergence from dangerous emergence* in multi-agent AI systems? Current work lacks a unified theoretical or empirical basis for determining when emergent multi-agent behavior (linguistic, behavioral, or coordinative) constitutes a beneficial capability to be cultivated, a novel risk to be contained, or a neutral artifact to be documented—leaving practitioners without guidance as MAS deployments scale.
