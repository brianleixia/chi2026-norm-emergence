# Literature Review — 2026-06-21
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
**Points of Agreement**

All three papers converge on the foundational premise that multi-agent systems (MAS) introduce qualitatively distinct phenomena that cannot be predicted from the behavior of individual agents in isolation. Paper 1 frames emergent language as a novel research area requiring its own taxonomy precisely because the conventions, protocols, and compositional structures arising between agents constitute a new object of study. Paper 2 operationalizes this concern from an AI safety perspective, arguing that single-agent evaluations are insufficient and that emergent behaviors across agent ensembles create novel risk surfaces. Paper 3, while more applied, embodies the same assumption by treating smart contract auditing as fundamentally a coordination problem rather than a collection of independent reasoning tasks. Together, they share an implicit commitment to the view that interaction topology, communication protocols, and coordination dynamics are first-order research concerns rather than implementation details.

**Points of Divergence**

The papers diverge sharply in their methodological posture and target outcomes. Paper 1 is descriptive and taxonomic, aiming to characterize and categorize what emergent communication looks like without prescribing how it should be engineered, treating emergence as an object of curiosity and analysis. Paper 2 is adversarial and diagnostic, treating emergent behavior primarily as a hazard to be detected, measured, and mitigated, with its MAEBE framework geared toward safety benchmarking. Paper 3, by contrast, is prescriptive and constructive, treating multi-agent coordination as an engineering resource to be deliberately composed for a specific domain task. There is also a divergence in epistemic stance toward emergence itself: Paper 1 treats it as a phenomenon to be understood; Paper 2 treats it as a risk to be bounded; Paper 3 treats it as a capability to be harnessed. This tri-partite split—understanding, guarding, and exploiting emergence—reveals that the field lacks a unified theory linking these orientations.

**Most Urgent Open Question**

The most pressing unresolved question is whether emergence in multi-agent systems can be reliably characterized and controlled well enough to simultaneously enable the constructive coordination Paper 3 demonstrates while remaining detectable
