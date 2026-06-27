# Literature Review — 2026-06-27
**Query:** multi-agent LLM coordination failure emergent norms
**Papers reviewed:** 3

## 1. Emergent Language: A Survey and Taxonomy
- Authors: Jannik Peters, Constantin Waubert de Puiseau, Hasan Tercan | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - Emergent language is a novel area of research within artificial intelligence, particularly within multi-agent reinforcement learning.
  - Early approaches to studying language emergence were primarily concerned with explaining human language formation with little consideration given to its potential utility for artificial systems.
  - The field of emergent language represents a distinct research domain situated at the intersection of multi-agent reinforcement learning and language emergence studies.

## 2. MAEBE: Multi-Agent Emergent Behavior Framework
- Authors: Sinem Erisken, Timothy Gothard, Martin Leitgab | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - Traditional AI safety evaluations on isolated LLMs are insufficient for assessing multi-agent AI ensembles, which introduce novel emergent risks.
  - The MAEBE framework, when applied with the Greatest Good Benchmark, demonstrates emergent behavior in LLM moral reasoning (the abstract is truncated but indicates empirical demonstration of such behaviors).
  - A novel double-inversion question technique was used as part of the MAEBE evaluation methodology to systematically assess multi-agent emergent risks.

## 3. SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing
- Authors: Indraveni Chebolu, Arnab Mallick, Harmesh Rana | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - SPEAR models auditing as a coordinated mission carried out by specialized agents: a Planning Agent prioritizes contracts using risk-aware heuristics, an Execution Agent allocates tasks via the Contract Net protocol, and a Repair Agent applies fixes based on audit findings

## Synthesis
**Paragraph 1 — Points of Agreement**

All three papers share a foundational conviction: as AI systems move from isolated models to interacting ensembles, multi-agent dynamics become the defining axis of analysis. Papers 1 and 2 both frame emergence as the central phenomenon—Paper 1 taxonomizes how communication protocols and conventions arise spontaneously in multi-agent reinforcement learning, while Paper 2 argues that emergent behaviors between agents constitute a qualitatively distinct safety surface that single-model evaluation cannot capture. Paper 3 implicitly endorses this premise by demonstrating that multi-agent coordination patterns produce measurable gains in a real engineering domain (smart contract auditing), reinforcing the claim that collective interaction is not a curiosity but a functional and methodological necessity. Together they treat emergence as both a research lens and an engineering resource.

**Paragraph 2 — Points of Divergence**

The papers diverge sharply in their stance toward emergence as a *desired* versus *risk-bearing* property. Paper 1 treats emergent language as a scientifically interesting artifact worthy of measurement and cataloguing, agnostic to whether it is beneficial. Paper 2 inverts the moral valence: emergence is reframed as a primary vector of safety risk, demanding adversarial evaluation frameworks (MAEBE) precisely because multi-agent interaction can produce hazards invisible at the individual-model level. Paper 3 occupies a more pragmatic middle ground—emergence is neither celebrated nor feared but *engineered*, with coordination protocols (SPEAR) deliberately imposed to channel agent capabilities toward a verifiable domain goal. A subtler disagreement concerns generalizability: Paper 1 abstracts away domain context to study emergence in the abstract, Paper 2 generalizes emergent risk across LLM populations, and Paper 3 insists that credible multi-agent claims must be grounded in concrete, domain-specific workflows. The field has not converged on whether emergence is fundamentally a scientific object, a safety hazard, or an engineering handle.

**Paragraph 3 — Most Urgent Open Question**

The most urgent open question is whether *emergence in multi-agent systems is inherently un
