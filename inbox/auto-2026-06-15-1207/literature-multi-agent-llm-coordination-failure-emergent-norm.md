# Literature Review — 2026-06-15
**Query:** multi-agent LLM coordination failure emergent norms
**Papers reviewed:** 3

## 1. Emergent Language: A Survey and Taxonomy
- Authors: Jannik Peters, Constantin Waubert de Puiseau, Hasan Tercan | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - Emergent language is a novel area of research within multi-agent reinforcement learning, though the concept of studying language emergence is not new.

## 2. MAEBE: Multi-Agent Emergent Behavior Framework
- Authors: Sinem Erisken, Timothy Gothard, Martin Leitgab | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - Traditional AI safety evaluations on isolated LLMs are insufficient as multi-agent AI ensembles become prevalent, introducing novel emergent risks.
  - The MAEBE framework was introduced to systematically assess emergent risks in multi-agent AI ensembles.
  - Using MAEBE with the Greatest Good Benchmark and a novel double-inversion question technique, the authors demonstrated that LLM moral reasoning can produce specific emergent behaviors when LLMs operate in multi-agent settings (additional details truncated in the provided abstract).

## 3. SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing
- Authors: Indraveni Chebolu, Arnab Mallick, Harmesh Rana | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - [Could not extract]

## Synthesis
# Synthesis of Three Papers on Multi-Agent Systems and Emergent Behavior

## Points of Agreement

All three papers converge on the observation that multi-agent systems (MAS) introduce fundamentally novel dynamics that cannot be understood by studying individual agents in isolation. Paper 1 frames this as "emergent language"—the phenomena where communication protocols, conventions, and coordination strategies arise spontaneously among agents during training, beyond what any single agent is explicitly programmed to produce. Paper 2 echoes this by arguing that multi-agent AI ensembles generate "novel emergent risks" that elude traditional safety evaluations designed for isolated LLMs. Paper 3 reinforces the practical relevance by demonstrating that successful multi-agent coordination in real-world domains (smart contract auditing) requires explicit architectural patterns to manage inter-agent dependencies, role assignment, and information flow. Together, the papers agree that emergence—whether in communication, behavior, or coordination—defines the core phenomenon and challenge of multi-agent AI.

## Points of Disagreement

The papers diverge notably in their stance on whether emergence is an asset or a liability, and on how it should be engineered. Paper 1 adopts a largely descriptive and taxonomical perspective, treating emergent language as a phenomenon to be observed, classified, and understood—implicitly treating it as scientifically interesting rather than inherently problematic. Paper 2 takes a cautionary posture, framing emergent multi-agent behavior primarily as a *risk surface* requiring new evaluation frameworks. Paper 3 takes a constructive, engineering-oriented view: rather than letting emergence happen and studying it (Paper 1) or guarding against it (Paper 2), it argues for *deliberately designing* coordination patterns so that desirable system-level properties are engineered into the multi-agent topology from the start. This represents a spectrum from "observe" to "defend" to "design."

## Most Urgent Open Question

The most pressing unresolved question is: **How can we reliably distinguish *beneficial* emergence (useful communication, effective coordination, novel problem-solving strategies) from *harmful
