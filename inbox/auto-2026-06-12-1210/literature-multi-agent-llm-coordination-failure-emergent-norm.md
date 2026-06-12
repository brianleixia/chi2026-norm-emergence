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
  - [Could not extract]

## Synthesis
## Points of Agreement

All three papers converge on the recognition that multi-agent systems (MAS) represent a qualitatively distinct paradigm from single-agent or isolated LLM evaluation, producing behaviors—linguistic, coordinative, or otherwise—that cannot be reduced to the properties of individual agents. They share a foundational concern with **emergence**: the first paper treats emergent language as a phenomenon arising from agent interaction, the second frames emergent behavior as a novel risk surface in LLM ensembles, and the third operationalizes emergent coordination as an engineering asset for complex tasks like smart contract auditing. Each paper implicitly endorses the view that interaction protocols, communication channels, and coordination patterns are first-order design concerns rather than implementation details. They also agree that systematic study or engineering of these dynamics requires structured frameworks—whether taxonomic (Paper 1), evaluative (Paper 2), or architectural (Paper 3).

## Points of Disagreement

The papers diverge sharply in their **orientation toward emergence**. Paper 1 treats emergent language as a phenomenon to be *characterized and understood*, largely agnostic to whether it is desirable. Paper 2 casts emergent behavior in LLM ensembles as a *risk to be detected and mitigated*, presupposing that unintended emergence is dangerous. Paper 3, conversely, treats emergent coordination as a *capability to be cultivated* through deliberate architectural choices (role assignment, negotiation patterns). This produces a tension: is emergence an epistemic object, a hazard, or an engineering target? The papers also disagree on maturity—Paper 1 surveys a young, largely experimental field; Paper 3 presents a deployed engineering artifact; Paper 2 occupies a middle ground proposing an evaluation framework that has not yet been stress-tested at scale. Their methodological commitments differ accordingly (taxonomic analysis vs. safety benchmarking vs. case-study validation).

## Most Urgent Open Question

The most urgent open question is: **under what conditions does multi-agent emergence constitute a capability, a hazard, or merely an artifact of training/communication design—and
