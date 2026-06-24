# Literature Review — 2026-06-24
**Query:** multi-agent LLM coordination failure emergent norms
**Papers reviewed:** 3

## 1. Emergent Language: A Survey and Taxonomy
- Authors: Jannik Peters, Constantin Waubert de Puiseau, Hasan Tercan | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - The field of emergent language represents a novel area of research within artificial intelligence, particularly in multi-agent reinforcement learning.
  - Early approaches to studying language emergence were primarily concerned with explaining human language formation with little consideration for its utility for artificial systems.
  - The concept of studying language emergence is not new and has been investigated prior to recent AI-focused research.

## 2. MAEBE: Multi-Agent Emergent Behavior Framework
- Authors: Sinem Erisken, Timothy Gothard, Martin Leitgab | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - Traditional AI safety evaluations on isolated LLMs are insufficient for assessing the novel emergent risks introduced by multi-agent AI ensembles.
  - The MAEBE framework, combined with the Greatest Good Benchmark and a novel double-inversion question technique, can systematically assess emergent risks in multi-agent AI systems.
  - LLMs exhibit specific moral reasoning behaviors when evaluated under the MAEBE framework, as demonstrated through the Greatest Good Benchmark methodology.

## 3. SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing
- Authors: Indraveni Chebolu, Arnab Mallick, Harmesh Rana | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - [Could not extract]

## Synthesis
# Synthesis of Three Papers on Multi-Agent Systems

## 1. Points of Agreement

All three papers converge on the recognition that multi-agent systems (MAS) introduce qualitatively distinct dynamics compared to single-agent or isolated LLM settings, and that these dynamics warrant dedicated study rather than being treated as simple extensions of single-agent analysis. Paper 1 frames emergent language as a core phenomenon arising from multi-agent reinforcement learning, emphasizing that communication protocols and coordination strategies are not pre-specified but emerge through interaction. Paper 2 makes a parallel claim about emergent behavior in LLM ensembles, arguing that traditional isolated safety evaluations are insufficient precisely because novel risks materialize only when agents interact. Paper 3 grounds this same premise in an applied engineering context, demonstrating that multi-agent coordination patterns produce more robust outcomes (in this case, smart contract auditing) than monolithic single-agent designs. Collectively, the papers agree that emergence—linguistic, behavioral, or coordinative—is the defining feature of MAS and that engineering or analyzing these systems requires frameworks specifically tailored to multi-agent dynamics.

## 2. Points of Disagreement

The papers diverge significantly in their disciplinary orientation and normative stance toward emergence. Paper 1 adopts a neutral, descriptive stance, treating emergent language as a phenomenon to be characterized and taxonomized, largely agnostic to whether the emergence is beneficial or harmful. Paper 2, by contrast, is explicitly normative and cautionary, framing emergent behavior in LLM ensembles as a source of novel safety risks requiring formal evaluation frameworks like MAEBE. Paper 3 occupies a third position—prescriptive and optimistic—where emergence is deliberately engineered and harnessed for productive ends (security analysis), drawing on established MAS coordination patterns rather than viewing them as unpredictable. In essence, Paper 1 asks *what is emergence?*, Paper 2 asks *how do we control its risks?*, and Paper 3 asks *how do we exploit its benefits?* This tension between emergence-as-subject, emergence-as-threat, and emergence-as-tool reflects
