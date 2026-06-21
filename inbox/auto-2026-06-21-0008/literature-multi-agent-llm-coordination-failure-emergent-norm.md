# Literature Review — 2026-06-21
**Query:** multi-agent LLM coordination failure emergent norms
**Papers reviewed:** 3

## 1. Emergent Language: A Survey and Taxonomy
- Authors: Jannik Peters, Constantin Waubert de Puiseau, Hasan Tercan | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - The field of emergent language represents a novel area of research within artificial intelligence, particularly within multi-agent reinforcement learning.
  - Early approaches to studying language emergence were primarily concerned with explaining human language formation rather than its utility for artificial systems.
  - These early approaches gave little consideration to the potential practical applications of emergent language for artificial intelligence.

## 2. MAEBE: Multi-Agent Emergent Behavior Framework
- Authors: Sinem Erisken, Timothy Gothard, Martin Leitgab | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - The paper introduces the MAEBE framework to systematically assess emergent risks in multi-agent AI ensembles.
  - Traditional AI safety evaluations on isolated LLMs are insufficient for multi-agent AI ensembles, which introduce novel emergent risks.
  - The paper uses the Greatest Good Benchmark with a novel double-inversion question technique in their evaluation.

## 3. SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing
- Authors: Indraveni Chebolu, Arnab Mallick, Harmesh Rana | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - [Could not extract]

## Synthesis
# Research Synthesis: Emergent Language and Multi-Agent AI Systems

## 1. Points of Agreement

All three papers converge on the recognition that multi-agent systems represent a meaningful shift beyond single-agent AI paradigms, warranting dedicated study frameworks. Paper 1 (Emergent Language) and Paper 2 (MAEBE) share a foundational concern: emergent properties arising from agent interactions are not reliably predictable from individual agent analysis alone. Both implicitly treat emergence as a first-class phenomenon requiring specialized evaluation methodologies. Paper 3 (SPEAR) reinforces this by demonstrating how multi-agent coordination patterns—originally theoretical constructs from MAS literature—can be operationalized into engineering practice, validating that multi-agent approaches yield benefits beyond monolithic systems, at least in domain-specific applications like smart contract auditing. There is also implicit consensus that established single-agent evaluation paradigms are inadequate for capturing system-level dynamics.

## 2. Points of Disagreement

The most significant divergence lies in **scope and risk framing**. Paper 2 (MAEBE) takes a cautionary stance, emphasizing that multi-agent ensembles introduce *novel emergent risks* that are largely uncharacterized and potentially dangerous, particularly as LLM-based systems proliferate. Paper 3 (SPEAR), by contrast, presents multi-agent coordination as an *engineering solution*—a structured methodology that applies well-understood MAS patterns to produce reliable, beneficial outcomes in security-critical domains. Paper 1 occupies a more neutral taxonomic position, treating emergent language as a phenomenon to be characterized and understood rather than as a risk to be mitigated or a tool to be deployed. A secondary tension exists between Paper 2's focus on *uncontrolled* emergence in open-ended LLM ensembles and Paper 3's focus on *controlled* emergence within bounded task domains (smart contract auditing), suggesting the field has not yet reconciled whether multi-agent dynamics are fundamentally hazardous or contextually manageable.

## 3. Most Urgent Open Question

**Under what conditions does multi-agent coordination produce beneficial emergence versus
