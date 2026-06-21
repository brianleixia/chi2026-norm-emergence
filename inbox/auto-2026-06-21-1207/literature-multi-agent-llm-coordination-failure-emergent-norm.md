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
  - Traditional AI safety evaluations on isolated LLMs are insufficient for assessing risks in multi-agent AI ensembles.
  - The paper introduces the Multi-Agent Emergent Behavior Evaluation (MAEBE) framework for systematically assessing emergent risks in multi-agent AI systems.
  - The framework employs the Greatest Good Benchmark along with a novel double-inversion question technique for evaluation.
  - LLM moral [reasoning/judgment can be influenced by multi-agent emergent behavior, as demonstrated through MAEBE evaluation]

## 3. SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing
- Authors: Indraveni Chebolu, Arnab Mallick, Harmesh Rana | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - [Could not extract]

## Synthesis
**1. Areas of Agreement**

All three papers converge on the premise that emergent multi-agent dynamics are both a defining feature and a critical research concern of modern AI systems. They share a recognition that traditional single-agent evaluations fail to capture the novel behaviors, communication patterns, and failure modes that arise when multiple agents interact. Whether framed as emergent communication protocols (Paper 1), emergent behavioral risks in LLM ensembles (Paper 2), or emergent coordination workflows in applied auditing (Paper 3), each work treats inter-agent interaction as a first-class object of study rather than an implementation detail. They also implicitly agree that analyzing or engineering such emergence requires moving beyond purely theoretical or purely empirical approaches—calling instead for systematic taxonomies, frameworks, or structured engineering practices to make the phenomenon tractable.

**2. Areas of Disagreement**

The papers diverge sharply in their orientation toward emergence. Paper 1 treats emergent language primarily as an object of scientific curiosity and taxonomic analysis, seeking to describe and categorize phenomena observed in controlled multi-agent reinforcement learning settings. Paper 2, by contrast, frames emergent behavior as a safety hazard, treating it as something to be measured, bounded, and mitigated in deployed LLM systems. Paper 3 takes yet a third stance, treating emergent coordination not as a risk or curiosity but as an engineered feature to be deliberately induced through careful application of established MAS patterns. Implicitly, they disagree on whether emergence is desirable (Paper 3), neutral (Paper 1), or dangerous (Paper 2)—and on whether the field needs better descriptive vocabularies, defensive evaluation methods, or constructive design principles.

**3. Most Urgent Open Question**

The most urgent open question is: **Under what conditions does emergent multi-agent behavior shift from being a productive or benign phenomenon into a safety-critical risk, and how can we detect that transition before deployment?** Papers 1 and 3 suggest emergence can be understood and even harnessed, while Paper 2 warns it can also produce novel hazards
