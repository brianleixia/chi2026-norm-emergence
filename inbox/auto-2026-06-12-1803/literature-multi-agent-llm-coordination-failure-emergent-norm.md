# Literature Review — 2026-06-12
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
  - Traditional AI safety evaluations on isolated LLMs are insufficient as multi-agent AI ensembles become prevalent, introducing novel emergent risks.
  - The MAEBE framework uses a novel double-inversion question technique to systematically assess emergent risks in multi-agent AI ensembles.
  - MAEBE was applied using the Greatest Good Benchmark to evaluate LLM moral reasoning.

## 3. SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing
- Authors: Indraveni Chebolu, Arnab Mallick, Harmesh Rana | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - [Could not extract]

## Synthesis
# Synthesis of Three Papers on Multi-Agent Systems

## 1. Points of Agreement

All three papers converge on the premise that multi-agent systems (MAS) represent a distinct and increasingly important research paradigm that cannot be adequately understood by studying isolated agents alone. Paper 1 frames emergent language as a phenomenon arising specifically from multi-agent reinforcement learning interactions, where communicative protocols develop that are not reducible to individual agent capabilities. Paper 2 extends this reasoning to safety, arguing that traditional single-LLM evaluations miss "novel emergent risks" that only manifest when agents interact within ensembles. Paper 3 grounds the same principle in applied engineering, demonstrating that established MAS coordination patterns (used in its SPEAR framework for smart contract auditing) yield capabilities and failure modes distinct from monolithic approaches. Together, they agree that interaction-level dynamics—communication, coordination, and emergent behavior—are the defining object of study, and that multi-agent settings demand dedicated theoretical and methodological tools rather than extrapolation from single-agent findings.

## 2. Points of Disagreement

The papers diverge most sharply in their orientation toward emergent phenomena. Paper 1 treats emergence as a *desirable* feature to be cultivated and taxonomized, focusing on the conditions under which agents develop useful communicative structure. Paper 2 treats emergence as a *hazard* to be detected and mitigated, emphasizing that the same properties which make multi-agent systems powerful also produce unpredictable and potentially unsafe behaviors absent in isolated models. Paper 3 implicitly challenges both positions by demonstrating that, in practice, multi-agent coordination need not rely on emergent protocols at all—instead applying "established MAS patterns" in a top-down engineering manner for smart contract auditing. This raises a fundamental tension: should the field pursue emergence as a research target (Paper 1), guard against it as a risk (Paper 2), or sidestep it through principled design (Paper 3)?

## 3. Most Urgent Open Question

The most pressing unresolved question is: **Under what conditions does emergence in multi-agent
