# Literature Review — 2026-06-14
**Query:** multi-agent LLM coordination failure emergent norms
**Papers reviewed:** 3

## 1. Emergent Language: A Survey and Taxonomy
- Authors: Jannik Peters, Constantin Waubert de Puiseau, Hasan Tercan | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - Early approaches to studying language emergence were primarily concerned with explaining human language formation, with little consideration given to its potential utility for artificial systems.

## 2. MAEBE: Multi-Agent Emergent Behavior Framework
- Authors: Sinem Erisken, Timothy Gothard, Martin Leitgab | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - Traditional AI safety evaluations on isolated LLMs are insufficient for assessing multi-agent AI ensembles
  - The MAEBE framework was developed to systematically assess emergent risks in multi-agent AI systems
  - The framework was tested using the Greatest Good Benchmark combined with a novel double-inversion question technique

## 3. SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing
- Authors: Indraveni Chebolu, Arnab Mallick, Harmesh Rana | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - [Could not extract]

## Synthesis
# Research Synthesis

## Points of Agreement

All three papers converge on the recognition that **multi-agent systems (MAS) introduce qualitatively distinct dynamics that cannot be understood by studying individual agents in isolation**. The emergent language survey establishes that interaction protocols between agents produce communication structures and behaviors not reducible to single-agent capabilities. MAEBE extends this logic to the safety domain, arguing that emergent risks in LLM ensembles are categorically different from those in monolithic models. SPEAR operationalizes this principle in a concrete engineering context, demonstrating that a coordinated multi-agent architecture can address smart contract auditing problems more effectively than single-agent approaches. Together, the papers share an underlying thesis: the *interaction topology* between agents—whether communicative, behavioral, or task-oriented—generates system-level properties that warrant dedicated study, formalization, and engineering discipline.

## Points of Disagreement

The papers diverge most sharply on **whether emergent multi-agent phenomena are primarily an opportunity or a threat**. The emergent language survey adopts a largely neutral, analytical posture—cataloging phenomena as objects of scientific curiosity without taking a strong normative stance. MAEBE takes a distinctly cautionary position, framing emergent behavior as a safety liability requiring proactive evaluation and containment. SPEAR, by contrast, takes a pragmatic-optimistic stance, treating multi-agent coordination as an engineering tool whose risks are manageable through established MAS design patterns and workflow discipline. A subtler disagreement concerns methodology: the survey privileges taxonomy-building and analysis of natural emergence, MAEBE pushes for benchmark-based adversarial evaluation, and SPEAR advocates for applied case studies in real-world deployment contexts—reflecting three different epistemic cultures (observational, adversarial, and constructive) addressing the same phenomenon.

## Most Urgent Open Question

**Under what conditions do the beneficial coordination patterns that SPEAR relies on (e.g., role specialization, task decomposition) become indistinguishable from the harmful emergent behaviors that MAEBE warns about?** The field currently lacks a principled framework that distinguishes *productive* emergence—where agent interactions produce capabilities
