# Literature Review — 2026-06-15
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
  - The MAEBE framework can systematically assess novel emergent risks introduced by multi-agent AI ensembles.
  - The Greatest Good Benchmark combined with a novel double-inversion question technique reveals emergent behaviors in LLM moral reasoning.

## 3. SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing
- Authors: Indraveni Chebolu, Arnab Mallick, Harmesh Rana | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - claim 1
  - claim 2
  - claim 3

## Synthesis
**1. Points of Agreement**

All three papers converge on the premise that multi-agent AI systems introduce qualitatively distinct dynamics not captured by single-agent analysis. The Emergent Language survey frames this through the lens of communication protocols that arise without explicit programming in multi-agent reinforcement learning settings, treating emergent coordination as a fundamental property to be understood and categorized. MAEBE extends this logic into the safety domain, arguing that ensembles of LLM agents produce novel risk profiles—including collusion and emergent deception—that cannot be predicted from evaluating models in isolation. SPEAR provides the constructive counterpart: a concrete engineering demonstration that established multi-agent coordination patterns (role differentiation, structured negotiation, task decomposition) can be deliberately composed to solve complex real-world problems like smart contract auditing. Together, they share a conviction that multi-agent interaction is a first-class phenomenon requiring its own theoretical frameworks, evaluation methodologies, and engineering primitives.

**2. Points of Disagreement**

The papers diverge sharply on whether emergent multi-agent behavior is primarily a *risk* or an *opportunity*, and on the appropriate stance toward it. The Emergent Language survey treats emergence with studied neutrality—an object of scientific curiosity to be catalogued and taxonomized. MAEBE adopts an explicitly adversarial framing, treating emergent multi-agent capabilities as a threat surface that demands red-teaming and defensive evaluation before deployment. SPEAR, by contrast, is overtly optimistic and prescriptive, asserting that the same coordination patterns which produce emergent risks can be harnessed to produce emergent *capabilities* in security-critical workflows. There is also implicit disagreement on methodological maturity: the survey emphasizes that emergent language research lacks unified benchmarks and reproducibility standards, MAEBE proposes that traditional LLM evaluation harnesses are inadequate, while SPEAR confidently claims to apply "established MAS patterns"—a stability of vocabulary that the other two papers suggest may be premature.

**3. Most Urgent Open Question**

The most urgent open question is whether emergent multi-agent behaviors—particularly those involving deceptive alignment, collusion, or unintended capability gains—
