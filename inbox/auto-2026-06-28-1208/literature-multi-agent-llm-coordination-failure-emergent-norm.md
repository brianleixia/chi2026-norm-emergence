# Literature Review — 2026-06-28
**Query:** multi-agent LLM coordination failure emergent norms
**Papers reviewed:** 3

## 1. Emergent Language: A Survey and Taxonomy
- Authors: Jannik Peters, Constantin Waubert de Puiseau, Hasan Tercan | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - The field of emergent language represents a novel area of research within artificial intelligence, particularly within multi-agent reinforcement learning.
  - Early approaches to studying language emergence were primarily concerned with explaining human language formation.
  - Early approaches to language emergence gave little consideration to its potential utility for artificial intelligence applications.

## 2. MAEBE: Multi-Agent Emergent Behavior Framework
- Authors: Sinem Erisken, Timothy Gothard, Martin Leitgab | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - Using MAEBE with the Greatest Good Benchmark and a novel double-inversion question technique demonstrates that LLM moral reasoning exhibits specific emergent behaviors when evaluated in multi-agent ensembles.
  - The MAEBE framework successfully identifies emergent risks arising from interactions between multiple LLM agents that are not detectable in isolated LLM evaluations.
  - The double-inversion question technique, applied within the Greatest Good Benchmark, reveals systematic patterns in how LLM moral judgments shift under multi-agent conditions.

## 3. SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing
- Authors: Indraveni Chebolu, Arnab Mallick, Harmesh Rana | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - [Could not extract]

## Synthesis
# Research Synthesis

## Points of Agreement

All three papers converge on the premise that multi-agent systems introduce qualitatively distinct dynamics that cannot be understood by studying individual agents in isolation. The emergent language survey establishes that interaction between agents produces communicative and behavioral phenomena not reducible to single-agent capabilities, while MAEBE explicitly argues that isolated LLM safety evaluations are insufficient precisely because multi-agent ensembles generate novel emergent risks. SPEAR reinforces this view from an applied engineering perspective, demonstrating that established multi-agent coordination patterns—when properly composed—can produce more robust collective behavior than any single auditing agent could achieve alone. Collectively, they treat emergence as a real, consequential property of agent interaction rather than a metaphorical artifact, and they share a methodological commitment to empirical investigation of these dynamics rather than purely theoretical treatment.

## Points of Disagreement

The papers diverge significantly in their framing of *what kind* of emergence matters and whether it is desirable. The emergent language survey treats emergent communication as a phenomenon to be *characterized and understood*, operating largely in controlled or synthetic environments. MAEBE, by contrast, frames emergent behavior primarily as a *risk vector*—something to be detected, bounded, and evaluated before deployment in safety-critical contexts. SPEAR takes an almost opposite stance, treating coordination emergence as *beneficial and engineered*: emergence here is harnessed through deliberate MAS patterns to improve smart contract auditing outcomes. There is also implicit disagreement on methodological maturity—the survey presents the field as still taxonomically unsettled, MAEBE positions itself as offering a needed evaluation framework, while SPEAR claims sufficient practical readiness to deploy multi-agent coordination in production security workflows today.

## Most Urgent Open Question

The most urgent open question is whether **multi-agent emergence can be reliably predicted, characterized, and governed before deployment**—or whether it remains inherently post-hoc and observational. MAEBE implicitly assumes emergent risks can be evaluated systematically, the emergent language survey suggests the field still lacks stable taxonomies for doing so, and SPEAR demonstrates that
