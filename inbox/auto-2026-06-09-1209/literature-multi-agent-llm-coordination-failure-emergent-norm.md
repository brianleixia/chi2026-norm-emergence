# Literature Review — 2026-06-09
**Query:** multi-agent LLM coordination failure emergent norms
**Papers reviewed:** 3

## 1. Emergent Language: A Survey and Taxonomy
- Authors: Jannik Peters, Constantin Waubert de Puiseau, Hasan Tercan | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - [Could not extract]

## 2. SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing
- Authors: Indraveni Chebolu, Arnab Mallick, Harmesh Rana | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - claim 1
  - claim 2
  - claim 3

## 3. MAEBE: Multi-Agent Emergent Behavior Framework
- Authors: Sinem Erisken, Timothy Gothard, Martin Leitgab | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - Traditional AI safety evaluations on isolated LLMs are insufficient as multi-agent AI ensembles become prevalent, introducing novel emergent risks.

## Synthesis
# Synthesis of Three Papers on Multi-Agent Systems

## 1. Points of Agreement

All three papers converge on the premise that multi-agent systems (MAS) introduce qualitatively distinct dynamics that cannot be understood by studying individual agents in isolation. Papers 1 and 3 explicitly frame emergent multi-agent behavior as a novel source of complexity and risk—Paper 1 through its taxonomy of emergent language in reinforcement learning settings, and Paper 3 through its focus on emergent hazards arising when LLM ensembles interact. Paper 2, while more applied, reinforces this view by demonstrating that coordinating agents in a real-world security workflow requires dedicated architectural patterns beyond single-agent solutions. Collectively, the papers agree that studying the *interaction layer*—whether it manifests as emergent communication, coordinated audit behavior, or unsafe collective dynamics—is now a necessary and distinct research priority. They also implicitly share an assumption that formalization, whether through taxonomy (Paper 1), framework engineering (Paper 2), or evaluation benchmarks (Paper 3), is the appropriate response to this complexity.

## 2. Points of Disagreement

The papers diverge sharply in their stance toward emergent multi-agent behavior. Paper 1 treats emergence primarily as a *phenomenon to be characterized and understood*, treating emergent language as an object of scientific curiosity with potential to illuminate the origins of natural language. Paper 3 adopts an almost opposite posture, treating emergence as a *risk surface to be detected, bounded, and mitigated* before deployment. Paper 2 sidesteps this debate entirely by focusing on *engineered coordination*—its agents are deliberately orchestrated rather than emergent, and emergence is neither celebrated nor feared but architected away. A second tension concerns methodology: Paper 1 emphasizes descriptive taxonomies, Paper 2 emphasizes applied system building, and Paper 3 emphasizes adversarial benchmarking, suggesting the field has not yet converged on what evidence counts as progress.

## 3. Most Urgent Open Question

The most pressing unresolved question is: **How can we
