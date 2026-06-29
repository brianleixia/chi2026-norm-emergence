# Literature Review — 2026-06-29
**Query:** multi-agent LLM coordination failure emergent norms
**Papers reviewed:** 3

## 1. Emergent Language: A Survey and Taxonomy
- Authors: Jannik Peters, Constantin Waubert de Puiseau, Hasan Tercan | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - The field of emergent language is a novel area of research within artificial intelligence, particularly within multi-agent reinforcement learning.
  - Early approaches to studying language emergence were primarily concerned with explaining human language formation.
  - Early approaches gave little consideration to the potential utility of language for artificial systems.

## 2. MAEBE: Multi-Agent Emergent Behavior Framework
- Authors: Sinem Erisken, Timothy Gothard, Martin Leitgab | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - LLM moral [claim is incomplete - cut off]
  - Multi-agent AI ensembles introduce novel emergent risks
  - Traditional AI safety evaluations on isolated LLMs are insufficient for assessing multi-agent risks

## 3. SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing
- Authors: Indraveni Chebolu, Arnab Mallick, Harmesh Rana | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - SPEAR models smart contract auditing as a coordinated mission involving a Planning Agent, an Execution Agent, and a Repair Agent.
  - The Planning Agent prioritizes contracts using risk-aware heuristics.
  - The Execution Agent allocates tasks via the Contract Net protocol.

## Synthesis
**Points of Agreement:** All three papers converge on the premise that multi-agent AI systems exhibit qualitatively different behaviors than isolated single-agent models, making them a distinct and important area of study. They share an understanding that interactions between autonomous agents—whether in simulated communication games, LLM ensembles, or structured task workflows—give rise to emergent properties (linguistic, behavioral, or coordinative) that cannot be fully predicted by examining individual components. Each work also implicitly accepts that engineering or evaluating such systems requires dedicated frameworks tailored to the multi-agent setting rather than borrowed directly from single-agent paradigms.

**Points of Disagreement:** The papers diverge sharply on whether emergent multi-agent behavior is primarily an opportunity to be cultivated or a risk to be controlled. The emergent language survey treats emergent phenomena as a phenomenon to be understood and characterized scientifically, largely agnostic to downstream value. MAEBE frames emergence as inherently suspect—a source of novel safety risks requiring red-teaming and adversarial evaluation. SPEAR takes a yet different stance, treating emergent coordination as an engineering resource to be deliberately harnessed through structured MAS patterns for productive outcomes like security auditing. There is also tension in scope: the survey and MAEBE address open-ended, less constrained agent populations, while SPEAR argues for tightly structured workflows with bounded agency.

**Most Urgent Open Question:** How can we develop principled methods to distinguish *beneficial* emergent coordination from *harmful* emergent behavior in multi-agent AI systems? As LLM ensembles and autonomous agent networks proliferate in high-stakes domains, the field lacks unified theory or benchmarks to determine when emergence should be encouraged (à la SPEAR), constrained (à la MAEBE), or simply observed (à la the survey)—making this classification problem the critical bottleneck for both safe deployment and effective system design.
