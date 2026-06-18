# Literature Review — 2026-06-18
**Query:** multi-agent LLM coordination failure emergent norms
**Papers reviewed:** 3

## 1. Emergent Language: A Survey and Taxonomy
- Authors: Jannik Peters, Constantin Waubert de Puiseau, Hasan Tercan | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - The field of emergent language is a novel area of research within artificial intelligence, particularly within multi-agent reinforcement learning.
  - Early approaches to studying language emergence were primarily concerned with explaining human language formation rather than its utility for artificial systems.
  - The abstract (as provided) does not contain specific empirical results or quantitative findings, so only methodological/contextual claims can be extracted.

## 2. MAEBE: Multi-Agent Emergent Behavior Framework
- Authors: Sinem Erisken, Timothy Gothard, Martin Leitgab | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - Using MAEBE with the Greatest Good Benchmark and a novel double-inversion question technique, the authors demonstrate emergent behaviors in LLM moral reasoning (claim truncated in abstract)

## 3. SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing
- Authors: Indraveni Chebolu, Arnab Mallick, Harmesh Rana | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - SPEAR models auditing as a coordinated mission carried out by specialized agents including a Planning Agent, Execution Agent, and Repair Agent.
  - The Planning Agent prioritizes contracts using risk-aware heuristics.
  - The Execution Agent allocates tasks via the Contract Net protocol.

## Synthesis
# Synthesis of Three Papers on Emergent Multi-Agent Systems

## 1. Points of Agreement

All three papers converge on the premise that multi-agent AI systems introduce qualitatively distinct dynamics that cannot be understood by studying individual agents in isolation. Paper 1 establishes this from a theoretical and taxonomic standpoint, arguing that emergent communication and coordination protocols in agent populations constitute a novel research domain requiring dedicated frameworks. Paper 2 extends this argument into the safety domain, asserting that traditional single-agent evaluation methodologies are categorically insufficient for multi-agent ensembles, which generate novel risk surfaces through their interactions. Paper 3 validates this concern from an applied engineering perspective, demonstrating that even when individual components are well-understood, their coordination in realistic workflows (smart contract auditing) produces emergent properties that demand systemic analysis. Together, the papers agree that the *interaction layer*—communication protocols, coordination patterns, and collective behavior—is where the most important research questions lie, and that existing tooling and theory are inadequate for this layer.

## 2. Points of Disagreement

The papers diverge significantly on their core concerns and what they consider the central challenge. Paper 1 treats emergent language primarily as a **scientific curiosity and capability**—an interesting phenomenon to study and taxonomize, with no explicit normative position on whether emergence is desirable or risky. Paper 2, conversely, frames emergent behavior as fundamentally a **safety hazard** requiring evaluation, monitoring, and likely mitigation. Paper 3 takes yet a third position, treating multi-agent coordination as a **design solution**—a structured engineering pattern (MAS) that solves real-world problems like security auditing, where emergence is controlled rather than observed. There is also an implicit tension around the locus of risk: Paper 2 locates danger in *unintended* emergent behaviors, while Paper 3 suggests that *deliberately engineered* coordination can be a risk-reduction strategy. Paper 1's neutral taxonomic stance sits uneasily alongside the other two's normative positions, raising the question of whether emergence is
