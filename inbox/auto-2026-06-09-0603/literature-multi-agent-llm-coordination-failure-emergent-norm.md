# Literature Review — 2026-06-09
**Query:** multi-agent LLM coordination failure emergent norms
**Papers reviewed:** 3

## 1. Emergent Language: A Survey and Taxonomy
- Authors: Jannik Peters, Constantin Waubert de Puiseau, Hasan Tercan | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - The abstract does not contain extractable empirical claims; it is a truncated survey paper introduction describing the field of emergent language in multi-agent reinforcement learning.

## 2. SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing
- Authors: Indraveni Chebolu, Arnab Mallick, Harmesh Rana | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - SPEAR is a multi-agent coordination framework that applies established MAS patterns for smart contract auditing.
  - SPEAR models auditing as a coordinated mission carried out by three specialized agents: a Planning Agent, an Execution Agent, and a Repair Agent.
  - The Planning Agent prioritizes contracts using risk-aware heuristics, while the Execution Agent allocates tasks via the Contract Net protocol.

## 3. MAEBE: Multi-Agent Emergent Behavior Framework
- Authors: Sinem Erisken, Timothy Gothard, Martin Leitgab | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - Traditional AI safety evaluations on isolated LLMs are insufficient for assessing multi-agent AI ensembles.
  - Multi-agent AI ensembles introduce novel emergent risks not present in isolated LLMs.
  - MAEBE uses the Greatest Good Benchmark along with a novel double-inversion question technique to systematically assess emergent risks in multi-agent LLM systems.

## Synthesis
## What do they agree on?

All three papers recognize multi-agent systems (MAS) as a rapidly expanding research frontier that introduces qualitatively new dynamics absent in single-agent settings. They share a conviction that interactions between autonomous agents—whether linguistic, task-oriented, or safety-critical—generate emergent phenomena that cannot be reliably predicted from the behavior of individual components. Each paper also implicitly endorses the need for more structured methodologies: Paper 1 calls for taxonomies to organize the nascent study of emergent communication, Paper 2 demonstrates that established MAS engineering patterns (role assignment, coordination protocols, message passing) can be productively applied to complex real-world domains like smart contract auditing, and Paper 3 argues that conventional AI safety evaluation must be extended with frameworks specifically designed to detect emergent risks in agent ensembles. Together, they treat multi-agent dynamics as both an opportunity (new capabilities, richer coordination) and a challenge (new forms of opacity, risk, and complexity).

## Where do they disagree?

The papers occupy notably different positions on whether emergent multi-agent behavior is primarily a *benefit* to be cultivated or a *risk* to be controlled. Paper 1 takes a largely neutral, descriptive stance—treating emergent language as a phenomenon worth cataloging and understanding in its own right, with open curiosity about its implications. Paper 2 is overtly optimistic and prescriptive, framing multi-agent coordination as an engineering solution whose value is demonstrated through successful application to a concrete security problem. Paper 3, by contrast, adopts a precautionary, even alarmist posture, positioning emergent behavior in LLM ensembles as a novel *threat surface* requiring dedicated defensive evaluation frameworks. A subtler disagreement concerns the locus of intelligence: Paper 1 privileges emergent communication protocols as the object of study, Paper 2 emphasizes structured role-based orchestration as the source of effectiveness, and Paper 3 treats emergent behavior as an unintended byproduct that must be measured and bounded.

## Most urgent open question?

**How can we reliably distinguish *beneficial* emergent coordination from *
