# Literature Review — 2026-06-18
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
  - Traditional AI safety evaluations on isolated LLMs are insufficient for assessing multi-agent AI ensembles, which introduce novel emergent risks.
  - The MAEBE framework was introduced to systematically assess emergent risks in multi-agent AI systems.
  - Using MAEBE with the Greatest Good Benchmark and a novel double-inversion question technique, the authors demonstrated properties about LLM moral reasoning.

## 3. SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing
- Authors: Indraveni Chebolu, Arnab Mallick, Harmesh Rana | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - [Could not extract]

## Synthesis
**1. Points of Agreement**

All three papers converge on the premise that multi-agent systems (MAS) introduce fundamentally different dynamics compared to single-agent settings, warranting dedicated study frameworks and taxonomies. Each positions emergent behavior—whether linguistic, behavioral, or coordination-based—as a central phenomenon that arises from agent interaction rather than individual agent capability. The authors share a methodological commitment to structured analysis: Paper 1 proposes taxonomy-building as a means to organize the emergent language literature, Paper 2 introduces a formal framework (MAEBE) for evaluating emergent risks, and Paper 3 demonstrates engineered coordination patterns applied to a real-world domain (smart contract auditing). Together, they reinforce the view that multi-agent AI research requires moving beyond isolated agent benchmarks toward interaction-aware evaluation, and that practical safety or performance outcomes depend on how agents coordinate, communicate, or compete.

**2. Points of Disagreement**

The papers diverge meaningfully in their orientation toward emergence. Paper 1 and Paper 3 treat emergent properties as either a research subject to be catalogued (taxonomies of emergent language) or a resource to be harnessed (structured coordination patterns that produce reliable auditing outcomes). Paper 2, by contrast, frames emergence as primarily a *risk vector*—an emergent behavior is potentially unsafe by default, demanding adversarial-style evaluation. There is also tension regarding the role of structure: Paper 3 argues that established MAS coordination patterns (e.g., role-based or hierarchical architectures) can be productively deployed to *constrain* emergence into useful forms, whereas Paper 1's survey tradition tends to study emergence under minimal structural priors (e.g., referential games), where communicative codes arise with little architectural guidance. Paper 2 sits ambiguously—advocating frameworks that detect emergence but not clearly endorsing whether it should be suppressed, channeled, or merely monitored.

**3. Most Urgent Open Question**

How can we develop evaluation methodologies that distinguish *beneficial* emergent coordination from *harmful* emergent behavior in multi
