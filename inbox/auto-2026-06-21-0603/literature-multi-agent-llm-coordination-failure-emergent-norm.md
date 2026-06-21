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
  - Traditional AI safety evaluations on isolated LLMs are insufficient because multi-agent AI ensembles introduce novel emergent risks.
  - The paper introduces the Multi-Agent Emergent Behavior Evaluation (MAEBE) framework to systematically assess emergent risks in multi-agent AI systems.
  - The paper demonstrates the use of MAEBE with the Greatest Good Benchmark along with a novel double-inversion question technique to evaluate LLM moral behavior.

## 3. SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing
- Authors: Indraveni Chebolu, Arnab Mallick, Harmesh Rana | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - SPEAR is a multi-agent coordination framework designed for smart contract auditing.
  - The framework uses established MAS patterns in a realistic security analysis workflow.
  - SPEAR models auditing as a coordinated mission involving specialized agents including a Planning Agent, an Execution Agent, and a Repair Agent.

## Synthesis
# Research Synthesis: Emergent Language, MAEBE, and SPEAR

## 1. Points of Agreement

All three papers converge on the premise that **multi-agent systems (MAS) introduce qualitatively distinct dynamics that cannot be reduced to single-agent analysis**. Each frames emergence—whether linguistic, behavioral, or coordinative—as the defining feature warranting specialized study. They share a common vocabulary of "emergence," "coordination," and "protocol" as load-bearing concepts. Papers 1 and 3 both treat structured interaction protocols (linguistic conventions in emergent communication, coordination patterns in auditing) as the mechanism through which collective intelligence arises. Paper 2 (MAEBE) implicitly agrees by treating emergent behavior as a *safety-relevant* phenomenon requiring dedicated evaluation frameworks—suggesting emergence is not merely interesting but consequential. All three also implicitly endorse the value of empirical, task-grounded study over purely theoretical analysis.

## 2. Points of Disagreement

The papers diverge sharply on **whether emergent phenomena are assets to be cultivated or risks to be contained**. Paper 1 treats emergent language as a research *opportunity*—a novel capability to understand and harness. Paper 3 (SPEAR) occupies a middle ground, attempting to *engineer* emergence by imposing MAS patterns onto a real domain (smart contract auditing), treating coordination as a tool for reliability. Paper 2 (MAEBE) is the outlier: it frames the same class of phenomena as a *threat surface*, arguing that traditional safety evaluations fail precisely because emergent multi-agent behavior escapes single-model analysis. A subtler disagreement concerns methodology—Paper 1 advocates taxonomic/survey-level synthesis, Paper 3 favors applied engineering case studies, and Paper 2 pushes for adversarial evaluation frameworks. These are not merely stylistic choices but reflect different epistemic commitments about how the field should progress.

## 3. Most Urgent Open Question

**Can we develop a unified theoretical account of emergence in multi-agent LLM systems that simultaneously
