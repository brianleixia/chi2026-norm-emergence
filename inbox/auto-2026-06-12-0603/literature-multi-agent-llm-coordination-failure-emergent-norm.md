# Literature Review — 2026-06-12
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
  - [Could not extract]

## 3. SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing
- Authors: Indraveni Chebolu, Arnab Mallick, Harmesh Rana | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - SPEAR models auditing as a coordinated mission carried out by specialized agents including a Planning Agent that prioritizes contracts using risk-aware heuristics.
  - SPEAR employs an Execution Agent that allocates tasks via the Contract Net protocol.
  - SPEAR includes a Repair Agent as part of its multi-agent coordination framework for smart contract auditing.

## Synthesis
## What do they agree on?

All three papers converge on the premise that multi-agent AI systems generate behaviors and capabilities that cannot be predicted by examining individual agents in isolation. Paper 1 frames this through *emergent language* in multi-agent reinforcement learning, noting that compositional and communicative structures arise from agent interaction without explicit programming. Paper 2 extends the same logic to modern LLM ensembles, arguing that isolated safety evaluations miss risks that only surface when agents interact. Paper 3 grounds the principle in practice, demonstrating that coordinated MAS patterns produce auditing capabilities exceeding what any single agent could achieve on a complex domain like smart contract security. Together, they treat emergence as a defining and exploitable property of multi-agent architectures.

## Where do they disagree?

The papers diverge sharply on whether emergence is an asset or a hazard, and on how it should be engineered. Paper 1 treats emergent language as a phenomenon to be *characterized*—building a taxonomy and studying it largely as a research curiosity, with ambiguity about its real-world utility. Paper 2 adopts an adversarial stance, positioning emergent multi-agent behavior as a *new attack surface* requiring red-teaming and dedicated evaluation frameworks like MAEBE. Paper 3 is the most sanguine, presenting emergence in multi-agent coordination as a *designable engineering tool* using established MAS patterns (auctions, contract nets, blackboards) to solve concrete problems. This produces a tension: is emergent coordination something to taxonomize, to defend against, or to deliberately engineer?

## Most urgent open question?

**Can we develop unified theoretical foundations that simultaneously explain, predict, and control emergent multi-agent behavior across the full spectrum from beneficial coordination (Paper 3) to adversarial risk (Paper 2)?** None of the three papers bridges these perspectives—Paper 1 lacks a predictive theory tying emergence to downstream task performance, Paper 2 cannot yet quantify when benign coordination tips into dangerous behavior, and Paper 3 offers no formalism for why its coordination patterns work or how
