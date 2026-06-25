# Literature Review — 2026-06-25
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
  - Traditional AI safety evaluations on isolated LLMs are insufficient for assessing multi-agent AI ensembles.
  - The Multi-Agent Emergent Behavior Evaluation (MAEBE) framework is introduced to systematically assess emergent risks in multi-agent AI systems.
  - MAEBE uses the Greatest Good Benchmark and a novel double-inversion question technique for evaluation.

## 3. SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing
- Authors: Indraveni Chebolu, Arnab Mallick, Harmesh Rana | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - SPEAR is a multi-agent coordination framework for smart contract auditing that applies established MAS patterns in a realistic security analysis workflow.
  - SPEAR models auditing as a coordinated mission carried out by specialized agents: a Planning Agent prioritizes contracts using risk-aware heuristics, an Execution Agent allocates tasks via the Contract Net protocol, and a Repair Agent addresses identified issues.
  - The Planning Agent uses risk-aware heuristics to prioritize contracts during the auditing process.

## Synthesis
**1. Points of Agreement**

All three papers converge on the central premise that multi-agent systems (MAS) introduce qualitatively distinct dynamics that cannot be understood by studying individual agents in isolation. Papers 1 and 2 explicitly frame emergence—both linguistic and behavioral—as a property arising from agent interaction rather than from any single agent's capabilities. Paper 3 reinforces this empirically by demonstrating that coordinating specialized agents in a realistic workflow (smart contract auditing) yields capabilities exceeding those of any individual agent. There is also shared concern about evaluation rigor: Paper 1 emphasizes the lack of standardized benchmarks and metrics in emergent language research, Paper 2 introduces a dedicated framework precisely because existing LLM safety evaluations "are insufficient" for multi-agent settings, and Paper 3 implicitly acknowledges this gap by proposing an "engineering case study" rather than claiming a general solution. Collectively, they suggest the field lacks mature tooling for measuring and validating emergent multi-agent phenomena.

**2. Points of Disagreement**

The papers diverge significantly in their treatment of emergence itself. Paper 1 treats emergent language primarily as a *phenomenon to be understood and characterized*, focusing on taxonomy, categorization of approaches, and open scientific questions. Paper 2 treats emergent behavior as a *risk to be mitigated*, positioning multi-agent interaction as a source of safety failures rather than a source of capability or insight. Paper 3 takes an explicitly *constructive* stance, treating multi-agent coordination as an engineering tool for solving domain problems, with emergence being a mostly incidental byproduct. A second tension lies in optimism: Paper 1 is largely agnostic, Paper 3 is constructive and applied, and Paper 2 is the most cautionary—suggesting emergent risks may require fundamentally new evaluation paradigms rather than extensions of existing ones.

**3. Most Urgent Open Question**

The most pressing unresolved question is: **How can we rigorously measure and predict when multi-agent interaction produces beneficial emergence versus harmful emergence?** Paper 1 highlights the absence of unified metrics for emergent communication; Paper
