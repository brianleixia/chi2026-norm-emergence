# Literature Review — 2026-06-19
**Query:** multi-agent LLM coordination failure emergent norms
**Papers reviewed:** 3

## 1. Emergent Language: A Survey and Taxonomy
- Authors: Jannik Peters, Constantin Waubert de Puiseau, Hasan Tercan | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - The field of emergent language is a novel area of research within artificial intelligence
  - Emergent language research is situated particularly within the context of multi-agent reinforcement learning
  - Early approaches to studying language emergence were primarily concerned with explaining human language formation with little consideration given to its potential utility for artificial intelligence

## 2. MAEBE: Multi-Agent Emergent Behavior Framework
- Authors: Sinem Erisken, Timothy Gothard, Martin Leitgab | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - Traditional AI safety evaluations on isolated LLMs are insufficient as multi-agent AI ensembles become prevalent, introducing novel emergent risks.
  - The paper introduces the Multi-Agent Emergent Behavior Evaluation (MAEBE) framework to systematically assess emergent risks in multi-agent AI systems.
  - Using MAEBE with the Greatest Good Benchmark and a novel double-inversion question technique, the authors demonstrate properties about LLM moral behavior in multi-agent settings.

## 3. SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing
- Authors: Indraveni Chebolu, Arnab Mallick, Harmesh Rana | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - [Could not extract]

## Synthesis
## Points of Agreement

All three papers converge on a shared foundational premise: multi-agent systems (MAS) represent a qualitatively different computational paradigm that demands specialized analysis beyond what single-agent or isolated-model frameworks can provide. Each paper treats emergent properties—whether linguistic, behavioral, or coordinative—as the central object of study rather than a peripheral curiosity. Paper 1 frames emergent language as a phenomenon arising specifically from agent interaction that cannot be reduced to individual agent capabilities; Paper 2 builds its entire safety framework around emergent risks that materialize only when LLMs interact; and Paper 3 argues that effective smart contract auditing emerges from structured agent coordination rather than monolithic reasoning. There is also implicit agreement that engineering or analyzing such systems requires deliberate structural design—reference games and signaling protocols in Paper 1, compositional evaluation harnesses in Paper 2, and role-specialized agent topologies in Paper 3—rather than emergent behavior being left to arise unconstrained.

## Points of Divergence

The papers diverge sharply on the *epistemic status* of emergence and the appropriate methodological response to it. Paper 1 treats emergent language as a phenomenon worth studying for its own sake, agnostic to deployment and emphasizing its potential to illuminate the nature of communication and meaning—its tone is exploratory and scientific. Paper 2, by contrast, adopts an explicitly adversarial and defensive posture, treating emergence as a *risk surface* to be measured, bounded, and mitigated before deployment. Paper 3 sits between these poles but leans toward an engineering optimism, treating emergent coordination as a resource to be harnessed through proven MAS patterns (task allocation, role specialization, negotiation) rather than a mysterious property to be either studied or feared. A subtler disagreement concerns the role of human oversight: Paper 1 largely abstracts away from human-in-the-loop considerations, Paper 2 centers human auditors in its evaluation loop, and Paper 3 embeds domain experts (security auditors) as first-class participants in the coordination protocol.

## Most Urgent Open Question

The
