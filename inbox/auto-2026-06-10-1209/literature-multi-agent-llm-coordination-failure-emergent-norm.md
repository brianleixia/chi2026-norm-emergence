# Literature Review — 2026-06-10
**Query:** multi-agent LLM coordination failure emergent norms
**Papers reviewed:** 3

## 1. Emergent Language: A Survey and Taxonomy
- Authors: Jannik Peters, Constantin Waubert de Puiseau, Hasan Tercan | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - The field of emergent language represents a novel area of research within the domain of artificial intelligence.
  - Early approaches to studying language emergence were primarily concerned with explaining human language formation.
  - These early approaches gave little consideration to the potential utility of language emergence for artificial intelligence applications.

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
## Where They Agree

All three papers converge on the premise that **multi-agent systems (MAS) introduce qualitatively new dynamics that cannot be understood by studying individual agents in isolation.** Whether the focus is emergent communication protocols, emergent safety risks, or coordinated domain-specific behavior, the authors treat the interactions between agents as the primary unit of analysis. They share a vocabulary of "emergence" as something that arises from agent interaction rather than being explicitly programmed, and they all implicitly accept that scaling, environment structure, and inter-agent dependencies are the key variables shaping what emerges. Each paper, in its own way, also argues for *better tooling* to study or manage these dynamics—be it taxonomies, evaluation frameworks, or engineering patterns.

## Where They Disagree

The most pointed disagreement concerns the **stance toward emergence itself and the role of formalization.** The Survey and Taxonomy (Paper 1) treats emergent language as a *phenomenon to be catalogued and understood scientifically*, remaining largely descriptive and agnostic about its utility. MAEBE (Paper 2), by contrast, frames emergence as a *risk surface requiring adversarial evaluation and safety guarantees*, pushing toward formal benchmarks. SPEAR (Paper 3) takes an almost opposite engineering posture: emergence is something to be *tamed through deliberate architectural patterns*, showing that in sufficiently structured domains, coordinated MAS behavior can be made reliable and predictable. Underlying these is a deeper tension about whether multi-agent systems should be studied as open-ended scientific objects, adversarial testbeds, or engineered products.

## Most Urgent Open Question

**How do we know when emergent multi-agent behavior is a feature, a bug, or a hazard?** The three papers together expose that the field lacks a unifying criterion for distinguishing benign emergence (useful coordination, learned protocols) from malign emergence (deception, collusion, unsafe cascades). The survey provides no predictive theory for *when* emergence becomes problematic; MAEBE can detect risks but cannot guarantee their absence; SPEAR shows
