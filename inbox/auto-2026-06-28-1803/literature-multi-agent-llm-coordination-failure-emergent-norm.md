# Literature Review — 2026-06-28
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
  - LLM moral [claim is incomplete in the provided abstract text]

## 3. SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing
- Authors: Indraveni Chebolu, Arnab Mallick, Harmesh Rana | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - [Could not extract]

## Synthesis
## Where They Agree

All three papers converge on the premise that **multi-agent systems introduce qualitatively different dynamics than single-agent setups**, warranting dedicated frameworks of study. Paper 1 establishes emergent communication as a legitimate subfield, arguing that the compositional and information-theoretic properties of agent-generated protocols deserve systematic taxonomy. Papers 2 and 3 both implicitly endorse this framing by treating multi-agent interaction as the object of analysis rather than a means to an end—Paper 2 through the lens of emergent risks in LLM ensembles, and Paper 3 through coordinated MAS patterns applied to a concrete engineering domain (smart contract auditing). They also share a methodological commitment to **empirical evaluation over purely theoretical claims**: Paper 1 inventories benchmarks, Paper 2 proposes an evaluation framework, and Paper 3 reports a case study deployment. There is mutual recognition that emergence is not guaranteed and must be measured, whether through language compositionality, behavioral divergence, or task performance.

## Where They Disagree

The papers diverge sharply on **whether emergence is a feature to cultivate or a hazard to contain**. Paper 1 and parts of Paper 3 treat emergent properties (language, coordination patterns) as desirable research outcomes worth characterizing and engineering toward. Paper 2, by contrast, frames emergent behavior in LLM ensembles primarily as a *safety liability*—novel failure modes that single-agent testing cannot catch. A second axis of disagreement concerns **realism versus abstraction**: Paper 1 remains largely in controlled reference games and signaling environments, Paper 3 grounds itself in a domain-specific deployment with real artifacts (smart contracts, audit workflows), while Paper 2 occupies a middle ground with synthetic but realistic-sounding multi-agent scenarios. Finally, the papers disagree on **the locus of value**—Paper 1 centers communication protocols, Paper 2 centers behavioral risk profiles, and Paper 3 centers task outcomes—suggesting no shared consensus on what "success" in multi-agent research even means.

## Most Urgent Open Question

**How
