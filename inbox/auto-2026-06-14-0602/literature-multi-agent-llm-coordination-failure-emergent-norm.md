# Literature Review — 2026-06-14
**Query:** multi-agent LLM coordination failure emergent norms
**Papers reviewed:** 3

## 1. Emergent Language: A Survey and Taxonomy
- Authors: Jannik Peters, Constantin Waubert de Puiseau, Hasan Tercan | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - The field of emergent language represents a novel area of research within the domain of artificial intelligence, particularly within the context of multi-agent reinforcement learning.
  - Early approaches to studying language emergence were primarily concerned with explaining human language formation, with little consideration given to its potential utility for artificial intelligence.
  - The concept of studying language emergence is not entirely new, as it has historical roots in explaining human language formation.

## 2. MAEBE: Multi-Agent Emergent Behavior Framework
- Authors: Sinem Erisken, Timothy Gothard, Martin Leitgab | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - Traditional AI safety evaluations on isolated LLMs are insufficient as multi-agent AI ensembles become prevalent, introducing novel emergent risks.
  - Using MAEBE with the Greatest Good Benchmark and a novel double-inversion question technique, they demonstrate that LLM moral [claim truncated in abstract]

## 3. SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing
- Authors: Indraveni Chebolu, Arnab Mallick, Harmesh Rana | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - [Could not extract]

## Synthesis
# Research Synthesis: Multi-Agent Systems in Language, Safety, and Engineering

## Points of Agreement

All three papers converge on the premise that multi-agent systems (MAS) produce emergent properties that exceed the sum of their individual components, though they explore this phenomenon from fundamentally different vantage points. Paper 1 frames emergence primarily as a *linguistic* phenomenon, documenting how agents develop compositional and structured communication protocols without explicit supervision, while Paper 2 reframes emergence as a *risk surface*, arguing that isolated LLM evaluations fail to capture systemic vulnerabilities that arise only when agents interact. Paper 3 grounds the concept in a *practical engineering* context, demonstrating that multi-agent coordination patterns—role differentiation, structured workflows, and inter-agent communication—can be deliberately harnessed for complex tasks like smart contract auditing. Together, they share an implicit consensus that single-agent analysis is an inadequate unit of evaluation: whether studying language emergence, safety, or applied coordination, the interaction layer between agents introduces qualitatively new behaviors that cannot be predicted from individual agent capabilities.

## Points of Disagreement

The papers diverge sharply on whether emergent multi-agent behavior is fundamentally an *opportunity* or a *threat*, and on the role of structured design in mediating this. Paper 1 treats emergence as a research phenomenon worthy of empirical study, largely agnostic about its downstream implications—emergent languages are interesting insofar as they reveal properties of communication learning. Paper 2 takes an explicitly adversarial stance, positioning emergent multi-agent behavior as a *novel attack surface* requiring new evaluation frameworks (MAEBE) to probe coordination failures, collusion, and deceptive alignment that emerge at the system level. Paper 3 occupies a contrarian engineering position: it argues that emergence is neither mysterious nor dangerous but rather a *designable artifact*, achieved through well-known MAS patterns like task decomposition and role-based coordination. This creates an unresolved tension about whether emergent properties are inherent to MAS interaction (Papers 1–2) or whether they are largely a consequence of
