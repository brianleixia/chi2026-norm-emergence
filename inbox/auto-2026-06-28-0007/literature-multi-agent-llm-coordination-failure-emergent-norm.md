# Literature Review — 2026-06-28
**Query:** multi-agent LLM coordination failure emergent norms
**Papers reviewed:** 3

## 1. Emergent Language: A Survey and Taxonomy
- Authors: Jannik Peters, Constantin Waubert de Puiseau, Hasan Tercan | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - The field of emergent language is a novel area of research within artificial intelligence, particularly within multi-agent reinforcement learning.
  - The concept of studying language emergence is not new.
  - Early approaches to language emergence were primarily concerned with explaining human language formation, with little consideration given to its potential utility for artificial systems.

## 2. MAEBE: Multi-Agent Emergent Behavior Framework
- Authors: Sinem Erisken, Timothy Gothard, Martin Leitgab | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - LLM moral reasoning (truncated - insufficient information to extract additional specific claims)

## 3. SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing
- Authors: Indraveni Chebolu, Arnab Mallick, Harmesh Rana | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - SPEAR models smart contract auditing as a coordinated mission carried out by specialized agents
  - The framework includes a Planning Agent that prioritizes contracts using risk-aware heuristics
  - An Execution Agent allocates tasks via the Contract Net protocol

## Synthesis
# Research Synthesis: Three Papers on Emergent Language and Multi-Agent Systems

**1. Points of Agreement**

All three papers converge on the recognition that multi-agent systems (MAS) exhibit properties that cannot be understood by examining individual agents in isolation. The *Emergent Language* survey frames communication protocols that arise between agents as a distinct research frontier requiring its own theoretical vocabulary, while *MAEBE* argues that traditional single-agent safety evaluations are fundamentally insufficient for ensembles where "novel emergent risks" arise from interaction. *SPEAR* implicitly endorses this view by deliberately modeling smart contract auditing as a coordination problem rather than as a monolithic task. Together, they treat emergence—whether linguistic, behavioral, or procedural—as the central object of study, and they all implicitly accept that engineering or evaluating such systems requires multi-agent-aware frameworks rather than reductive single-agent analysis.

**2. Points of Disagreement**

The papers diverge sharply on the *role of emergence itself*. The *Emergent Language* survey treats emergent communication as a phenomenon to be *understood and characterized*, building a taxonomy of observed behaviors across reinforcement learning settings. *MAEBE*, by contrast, treats emergent behavior as a *hazard to be detected and constrained*—its contribution is a benchmarking framework for identifying dangerous multi-agent dynamics before deployment. *SPEAR* takes a third position: emergence is not the focus at all, and the paper instead applies "established MAS patterns" to a practical engineering problem, treating multi-agent coordination as a solved design vocabulary rather than an open scientific question. This reflects a deeper disagreement about whether multi-agent AI research should prioritize descriptive science, safety diagnostics, or applied engineering—priorities that are largely orthogonal across the three works.

**3. Most Urgent Open Question**

The most pressing open question bridging these works is: **Can we reliably distinguish productive emergence (like SPEAR's coordinated auditing routines or useful emergent communication protocols) from hazardous emergence (like the unsafe behaviors MAEBE seeks to detect) before
