# Literature Review — 2026-06-27
**Query:** multi-agent LLM coordination failure emergent norms
**Papers reviewed:** 3

## 1. Emergent Language: A Survey and Taxonomy
- Authors: Jannik Peters, Constantin Waubert de Puiseau, Hasan Tercan | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:

## 2. MAEBE: Multi-Agent Emergent Behavior Framework
- Authors: Sinem Erisken, Timothy Gothard, Martin Leitgab | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - Traditional AI safety evaluations on isolated LLMs are insufficient as multi-agent AI ensembles become prevalent, introducing novel emergent risks
  - The MAEBE framework uses the Greatest Good Benchmark along with a novel double-inversion question technique to assess multi-agent emergent risks
  - LLM moral [claim truncated - not fully extractable from provided text]

## 3. SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing
- Authors: Indraveni Chebolu, Arnab Mallick, Harmesh Rana | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - SPEAR models auditing as a coordinated mission carried out by specialized agents including a Planning Agent, Execution Agent, and Repair Agent
  - The Planning Agent prioritizes contracts using risk-aware heuristics
  - The Execution Agent allocates tasks via the Contract Net protocol

## Synthesis
# Research Synthesis: Emergent Language, Multi-Agent Safety, and MAS Engineering

**1. Points of Agreement**

All three papers converge on the recognition that multi-agent systems (MAS) exhibit dynamics—particularly *emergent behaviors*—that cannot be predicted from the properties of individual agents in isolation. Paper 1 frames emergent language as a phenomenon where compositional, sometimes human-interpretable protocols arise from grounded signaling games and reinforcement learning pressures, without being explicitly programmed. Paper 2 builds directly on this premise by arguing that such emergence extends beyond communicative protocols into the broader behavioral space, where ensembles of LLM-based agents can produce coordinated actions, planning failures, or steganographic evasion that no single model would generate alone. Paper 3 grounds the abstract concept in an engineering reality: when multiple specialized auditors (each with a distinct role) coordinate on a shared task like smart contract analysis, the *interaction structure itself*—role assignment, message routing, consensus mechanisms—becomes the determining factor of system performance and reliability. Together, they agree that inter-agent coordination introduces qualitatively new system-level properties requiring dedicated study.

**2. Points of Disagreement**

The papers diverge sharply on the *evaluative valence* of emergence and the appropriate response from the research community. Paper 1 treats emergent language as a largely *productive* and scientifically interesting phenomenon—evidence that artificial agents can discover compositional communication, with potential downstream value for interpretability and protocol design. Paper 2 inverts this framing, treating emergence as a primary *risk surface*: emergent behaviors are novel attack vectors, sources of misalignment, and obstacles to verification, necessitating adversarial benchmarks like MAEBE. Paper 3 sidesteps the debate entirely by adopting a pragmatic engineering posture—emergence is neither celebrated nor feared, but *managed* through deliberate architectural choices (explicit coordination frameworks, role separation, deterministic communication contracts). Implicitly, Paper 1 and Paper 2 disagree on whether the field's central challenge is *cultivating* emergence
