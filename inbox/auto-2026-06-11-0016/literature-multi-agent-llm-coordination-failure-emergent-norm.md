# Literature Review — 2026-06-11
**Query:** multi-agent LLM coordination failure emergent norms
**Papers reviewed:** 3

## 1. Emergent Language: A Survey and Taxonomy
- Authors: Jannik Peters, Constantin Waubert de Puiseau, Hasan Tercan | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - The field of emergent language represents a novel area of research within artificial intelligence, particularly within multi-agent reinforcement learning.
  - Early approaches to studying language emergence were primarily concerned with explaining human language formation.
  - Early approaches gave little consideration to the potential utility of emergent language for artificial intelligence applications.

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
**1. Areas of Agreement**

All three papers converge on the premise that multi-agent systems introduce qualitatively distinct dynamics that cannot be inferred from studying single-agent or isolated LLM behavior. Paper 1 frames emergent language as a novel research domain rooted in multi-agent reinforcement learning, where novel communicative protocols arise from agent interactions; Paper 2 explicitly critiques isolated LLM safety evaluations as insufficient, arguing that multi-agent ensembles create "emergent risks" absent in single-model contexts; and Paper 3, while more applied, similarly treats multi-agent coordination as a distinct engineering paradigm requiring its own architectural patterns (audit roles, dispute mediation, consensus mechanisms) rather than simply parallelized single-agent workflows. They also share an implicit methodological commitment: emergent multi-agent behavior must be studied *systemically*, whether through taxonomic analysis (Paper 1), empirical evaluation frameworks (Paper 2), or applied coordination protocols (Paper 3).

**2. Areas of Disagreement**

The papers diverge significantly in scope, abstraction level, and implicit assumptions about controllability. Paper 1 treats emergent communication as a phenomenon to be characterized and categorized — relatively neutral in its framing of emergence as a research opportunity. Paper 2 takes a notably adversarial stance, positioning emergent behavior primarily as a *risk vector* requiring detection and mitigation. Paper 3 stands apart as the most sanguine, treating multi-agent emergence as an engineering resource to be harnessed for productive ends (smart contract auditing), assuming coordination patterns can be deliberately designed. A second tension concerns the locus of emergence: Paper 1 and Paper 2 both emphasize bottom-up, unanticipated behavior arising from agent interactions, while Paper 3 emphasizes top-down coordination architectures where emergence is bounded by engineered protocols — suggesting fundamentally different theories of how much structure must be imposed for multi-agent systems to be useful or safe.

**3. Most Urgent Open Question**

How can we develop unified theoretical and empirical frameworks that simultaneously *harness productive emergence* (Paper 3's vision) while *detecting and
