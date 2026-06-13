# Literature Review — 2026-06-13
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
  - The paper introduces the Multi-Agent Emergent Behavior Evaluation (MAEBE) framework to systematically assess emergent risks in multi-agent AI systems.
  - The framework was evaluated using the Greatest Good Benchmark along with a novel double-inversion question technique.

## 3. SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing
- Authors: Indraveni Chebolu, Arnab Mallick, Harmesh Rana | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - SPEAR is a multi-agent coordination framework for smart contract auditing that applies established MAS patterns in a realistic security analysis workflow.
  - SPEAR models auditing as a coordinated mission carried out by specialized agents including a Planning Agent, an Execution Agent, and a Repair Agent.
  - The Planning Agent prioritizes contracts using risk-aware heuristics while the Execution Agent allocates tasks via the Contract Net protocol.

## Synthesis
Based on the three paper abstracts provided, here is a synthesis:

**1. Points of Agreement**
All three papers converge on the recognition that multi-agent systems represent a critical and rapidly evolving frontier in AI research, moving beyond the limitations of evaluating isolated single-agent models. They share a common framing that emergent behaviors—whether arising from multi-agent reinforcement learning communication protocols (Paper 1), from ensembles of LLM-based agents (Paper 2), or from coordinated agent architectures applied to real-world tasks like smart contract auditing (Paper 3)—produce capabilities and risks that cannot be predicted by examining individual agents in isolation. Each paper treats multi-agent interaction as a distinct phenomenon worthy of its own study, taxonomy, or evaluation framework, suggesting a field-wide consensus that agent coordination fundamentally changes the safety, performance, and behavioral profile of AI systems.

**2. Points of Disagreement**
The papers diverge significantly in their orientation toward the risks and opportunities of multi-agent systems. Paper 1 takes a relatively neutral, descriptive stance—cataloging emergent language phenomena as a research domain to be understood and characterized. Paper 2, by contrast, adopts an explicitly cautionary posture, framing multi-agent emergent behavior as a source of "novel emergent risks" that current AI safety evaluations fail to capture. Paper 3 occupies a more optimistic, applied position, treating multi-agent coordination as a constructive engineering tool for solving concrete problems (smart contract security) rather than a phenomenon to be wary of. This creates an underlying tension: whether multi-agent emergence should be primarily studied as a scientific curiosity, guarded against as a safety hazard, or harnessed as an engineering solution.

**3. Most Urgent Open Question**
The most pressing unresolved question is: **How can we reliably detect, measure, and predict emergent behaviors in multi-agent systems before deployment, given that such behaviors arise from interactions that no single-agent evaluation can anticipate?** This question cuts across all three papers but remains unanswered by any of them—Paper 1 acknowledges emergence without offering predictive tools,
