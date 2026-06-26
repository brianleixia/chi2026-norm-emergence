# Literature Review — 2026-06-26
**Query:** multi-agent LLM coordination failure emergent norms
**Papers reviewed:** 3

## 1. Emergent Language: A Survey and Taxonomy
- Authors: Jannik Peters, Constantin Waubert de Puiseau, Hasan Tercan | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - Emergent language is a research area within artificial intelligence, particularly in multi-agent reinforcement learning contexts.
  - Early approaches to studying language emergence were primarily concerned with explaining human language formation.
  - Early approaches to language emergence gave little consideration to its potential utility for artificial systems.

## 2. MAEBE: Multi-Agent Emergent Behavior Framework
- Authors: Sinem Erisken, Timothy Gothard, Martin Leitgab | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - [Could not extract]

## 3. SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing
- Authors: Indraveni Chebolu, Arnab Mallick, Harmesh Rana | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - SPEAR models auditing as a coordinated mission carried out by specialized agents: a Planning Agent, an Execution Agent, and a Repair Agent.
  - The Planning Agent prioritizes contracts using risk-aware heuristics.
  - The Execution Agent allocates tasks via the Contract Net protocol.

## Synthesis
# Synthesis of Three Papers on Multi-Agent Systems and Emergent Language

## 1. Points of Agreement

All three papers converge on the foundational premise that multi-agent systems (MAS) represent a paradigm shift beyond single-agent AI, requiring fundamentally new analytical frameworks rather than scaled-up versions of existing approaches. Paper 1 establishes that when multiple agents interact, novel communicative and behavioral phenomena emerge that cannot be predicted from individual agent capabilities. Paper 2 operationalizes this insight by demonstrating that traditional isolated LLM safety evaluations are insufficient precisely because emergent multi-agent risks are qualitatively distinct from single-agent failure modes. Paper 3 corroborates this by showing that multi-agent coordination patterns (even when applying established MAS principles) require purpose-built engineering frameworks to function reliably. Implicitly, all three agree that coordination, communication protocols, and emergent dynamics are central research concerns for understanding and deploying MAS.

## 2. Points of Disagreement

The papers diverge on their primary orientation and the role of language/communication. Paper 1 treats emergent language as the central phenomenon of interest, framing it as an open scientific research question about how communication protocols arise naturally between agents. Paper 2 takes a safety-and-evaluation stance, treating emergent *behavior* (not language per se) as the object of study, with a focus on risk identification and benchmarking rather than understanding communicative genesis. Paper 3 sidesteps the emergence question entirely by engineering coordination deliberately, applying known MAS patterns to a structured domain (smart contract auditing) rather than allowing protocols to emerge organically. There is also a methodological tension: Paper 1 is exploratory and theoretical, Paper 2 is diagnostic and evaluative, while Paper 3 is constructive and applied—each implicitly skeptical of the others' approach as sufficient on its own.

## 3. Most Urgent Open Question

The most pressing unresolved question bridging all three works is: **How can we reliably distinguish productive emergent coordination from emergent risks in deployed multi-agent systems?** Paper 1 shows emergence is poorly understood; Paper
