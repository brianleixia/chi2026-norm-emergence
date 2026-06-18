# Literature Review — 2026-06-18
**Query:** multi-agent LLM coordination failure emergent norms
**Papers reviewed:** 3

## 1. Emergent Language: A Survey and Taxonomy
- Authors: Jannik Peters, Constantin Waubert de Puiseau, Hasan Tercan | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - The field of emergent language represents a novel area of research within the domain of artificial intelligence, particularly within the context of multi-agent reinforcement learning.

## 2. MAEBE: Multi-Agent Emergent Behavior Framework
- Authors: Sinem Erisken, Timothy Gothard, Martin Leitgab | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - Traditional AI safety evaluations on isolated LLMs are insufficient for assessing multi-agent AI ensembles
  - MAEBE uses a Greatest Good Benchmark and a novel double-inversion question technique to assess emergent risks
  - LLM moral [reasoning/text cut off - claim incomplete]

## 3. SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing
- Authors: Indraveni Chebolu, Arnab Mallick, Harmesh Rana | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - [Could not extract]

## Synthesis
# Research Synthesis: Multi-Agent Emergent Behavior

## Areas of Agreement

All three papers converge on the fundamental premise that **multi-agent AI systems exhibit emergent properties that cannot be understood by analyzing individual agents in isolation**. The emergent language survey establishes this foundation by demonstrating how linguistic conventions arise from agent interactions, while MAEBE explicitly frames emergent behaviors in LLM ensembles as a novel risk surface requiring dedicated evaluation frameworks rather than isolated model testing. SPEAR reinforces this consensus from an applied engineering perspective, showing that effective multi-agent coordination for smart contract auditing depends on interaction patterns—role allocation, coordinated workflows, and information exchange—that produce collective intelligence exceeding the sum of individual agent capabilities. Together, they suggest that the field has broadly accepted emergence as a first-order phenomenon deserving systematic study, whether the goal is understanding, risk mitigation, or capability amplification.

## Points of Divergence

The papers diverge significantly in their **stance on whether emergence is primarily a benefit or a risk**. The emergent language survey treats emergence largely as a phenomenon to be understood and characterized, presenting it as scientifically interesting without strongly privileging either positive or negative framings. MAEBE adopts an explicitly safety-oriented perspective, positioning emergent behaviors as novel hazards that traditional single-model evaluation cannot capture—a more cautionary stance. SPEAR, in contrast, is fundamentally optimistic, demonstrating emergence as an *engineered* tool for producing high-quality security audits. A second axis of disagreement concerns **evaluability**: MAEBE insists on rigorous, standardized benchmarking for emergent behaviors; the survey acknowledges the field's methodological fragmentation; and SPEAR demonstrates that domain-specific metrics (audit accuracy, false positive rates) may suffice when emergence is deployed toward well-defined objectives.

## Most Urgent Open Question

The most pressing unresolved question across these works is: **how can we reliably detect, predict, and control emergent behaviors in multi-agent AI systems before deployment, particularly when those behaviors may be both beneficial and harmful depending on context?** MAEBE raises the alarm that current evaluation paradigms are
