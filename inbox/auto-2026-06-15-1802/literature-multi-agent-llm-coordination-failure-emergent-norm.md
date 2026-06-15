# Literature Review — 2026-06-15
**Query:** multi-agent LLM coordination failure emergent norms
**Papers reviewed:** 3

## 1. Emergent Language: A Survey and Taxonomy
- Authors: Jannik Peters, Constantin Waubert de Puiseau, Hasan Tercan | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - Emergent language is a research area within artificial intelligence, particularly in multi-agent reinforcement learning
  - Early approaches to studying language emergence were primarily concerned with explaining human language formation
  - Early approaches gave little consideration to language's potential utility for artificial systems

## 2. MAEBE: Multi-Agent Emergent Behavior Framework
- Authors: Sinem Erisken, Timothy Gothard, Martin Leitgab | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - Traditional AI safety evaluations on isolated LLMs are insufficient for multi-agent AI ensembles due to novel emergent risks.
  - The MAEBE framework systematically assesses emergent risks in multi-agent AI systems.
  - MAEBE employs the Greatest Good Benchmark along with a novel double-inversion question technique to evaluate LLM moral reasoning.

## 3. SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing
- Authors: Indraveni Chebolu, Arnab Mallick, Harmesh Rana | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - SPEAR models auditing as a coordinated mission carried out by specialized agents, including a Planning Agent, an Execution Agent, and a Repair Agent.
  - The Planning Agent prioritizes contracts using risk-aware heuristics.
  - The Execution Agent allocates tasks via the Contract Net protocol.

## Synthesis
# Research Synthesis

**Points of Agreement:** All three papers converge on the premise that multi-agent systems represent a fundamentally different paradigm from single-agent AI, warranting dedicated study frameworks rather than extrapolating findings from isolated model evaluations. They share a commitment to structured analysis—whether through taxonomies (Paper 1), formal behavior frameworks (Paper 2), or coordination architectures (Paper 3)—as essential tools for understanding collective intelligence. Each work implicitly acknowledges that inter-agent dynamics, whether linguistic or task-oriented, produce properties that cannot be predicted from individual agent capabilities alone, reflecting the field's broader acceptance of emergence as a substantive phenomenon rather than a metaphorical one.

**Points of Disagreement:** The papers differ markedly in their normative orientation and scope of concern. Paper 1 treats emergent language as a neutral scientific phenomenon worth characterizing for its own sake, focusing on descriptive taxonomy rather than risk. Paper 2 explicitly frames multi-agent dynamics as a safety concern, positioning emergent behaviors as novel risks requiring adversarial evaluation methods. Paper 3 takes a constructive engineering perspective, treating multi-agent coordination as a solution to domain problems (smart contract auditing) rather than a source of risk. There is also tension in their assumptions about stability: Paper 1's taxonomy implies emergent communication can be productively analyzed and compared across contexts, while Paper 2 suggests such behaviors may resist systematic characterization due to their inherently unpredictable nature.

**Most Urgent Open Question:** How can the field develop evaluation methodologies that distinguish between *beneficial* and *harmful* emergence in multi-agent systems? Papers 1 and 3 implicitly treat emergence as analyzable and potentially steerable toward useful outcomes, while Paper 2 treats it as a vector for novel failures—but no framework yet bridges these views. The critical gap is a unified theory of emergence that supports both constructive engineering (deliberately cultivating desirable collective behaviors) and safety evaluation (detecting undesirable ones before deployment), particularly as multi-agent LLM ensembles move from research curiosities to production systems.
