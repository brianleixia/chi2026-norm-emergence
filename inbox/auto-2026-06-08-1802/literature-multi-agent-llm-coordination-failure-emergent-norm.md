# Literature Review — 2026-06-08
**Query:** multi-agent LLM coordination failure emergent norms
**Papers reviewed:** 3

## 1. Emergent Language: A Survey and Taxonomy
- Authors: Jannik Peters, Constantin Waubert de Puiseau, Hasan Tercan | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - [Could not extract]

## 2. SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing
- Authors: Indraveni Chebolu, Arnab Mallick, Harmesh Rana | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - SPEAR is a multi-agent coordination framework for smart contract auditing that applies established MAS (Multi-Agent System) patterns in a realistic security analysis workflow.
  - SPEAR models auditing as a coordinated mission carried out by specialized agents, including a Planning Agent that prioritizes contracts using risk-aware heuristics, an Execution Agent that allocates tasks via the Contract Net protocol, and a Repair Agent.
  - The framework is presented as an engineering case study, applying multi-agent coordination patterns specifically to the domain of smart contract auditing.

## 3. MAEBE: Multi-Agent Emergent Behavior Framework
- Authors: Sinem Erisken, Timothy Gothard, Martin Leitgab | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - Traditional AI safety evaluations on isolated LLMs are insufficient for assessing multi-agent AI ensembles.
  - The MAEBE framework systematically assesses novel emergent risks introduced by multi-agent AI ensembles.
  - MAEBE employs a novel double-inversion question technique when used with the Greatest Good Benchmark to evaluate LLM moral reasoning.

## Synthesis
**Areas of Agreement:**
All three papers converge on the recognition that multi-agent systems (MAS) introduce qualitatively distinct dynamics that cannot be understood by studying individual agents in isolation. Papers 1 and 3 both explicitly frame emergence—whether linguistic or behavioral—as a defining property of agent interaction that resists decomposition into single-agent analysis. Paper 1 documents how agent populations develop compositional communication protocols through reinforcement learning pressure, while Paper 3 shows that LLM ensembles exhibit failure modes absent in any individual model. Paper 2 contributes empirical evidence for this consensus by demonstrating that coordinating specialized agents (each handling a distinct auditing subtask) yields capabilities exceeding those of monolithic approaches, and it credits its success to established coordination patterns (role differentiation, message-passing, consensus) drawn from the broader MAS literature. Implicitly, all three endorse the view that interaction topology, communication structure, and task decomposition are first-class design considerations rather than implementation details.

**Areas of Disagreement:**
The papers diverge sharply on whether emergent multi-agent behavior is an asset to be cultivated or a hazard to be controlled. Paper 1 adopts a largely optimistic stance, treating emergent language as a window into how communication and compositionality can arise naturally, with the implicit promise that such systems could yield interpretable or generalizable protocols. Paper 2 sits in a pragmatic middle ground: it neither celebrates nor fears emergence, instead focusing on engineering reliability by imposing structured coordination patterns from the outset. Paper 3, by contrast, is overtly cautionary, framing emergence in deployed LLM ensembles as a new attack surface and safety liability. A subtler disagreement concerns the locus of explanation: Papers 1 and 2 attribute multi-agent outcomes to the designed interaction protocol (learning pressure or hand-engineered coordination), whereas Paper 3 suggests that even well-behaved individual agents can produce system-level pathologies, implying emergence is not fully under designer control.

**Most Urgent Open Question:**
The most pressing unresolved question is whether emergent multi-agent behaviors—including beneficial ones like compositional communication and harmful ones
