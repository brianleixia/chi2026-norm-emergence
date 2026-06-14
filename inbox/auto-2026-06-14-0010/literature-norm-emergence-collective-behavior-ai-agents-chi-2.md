# Literature Review — 2026-06-14
**Query:** norm emergence collective behavior AI agents CHI 2026
**Papers reviewed:** 2

## 1. Open Challenges in Multi-Agent Security: Towards Secure Systems of Interacting AI Agents
- Authors: Christian Schroeder de Witt, Krawiecka, Klaudia, Krawczuk, Igor | Year: 2025 | Venue: arXiv (Cornell University)
- Novelty: ⭐⭐
- Claims:
  - AI agents are beginning to interact with each other directly and across internet platforms and physical environments
  - Free-form protocols are essential for AI's task generalization but enable new threats like secret collusion and coordinated swarm attacks
  - Network effects can rapidly spread privacy breaches

## 2. Integrated Design and Governance of Agentic AI Systems through Adaptive Information Modulation
- Authors: Qiliang Chen, Sepehr Ilami, Nunzio Lorè | Year: 2024 | Venue: arXiv (Cornell University)
- Novelty: ⭐⭐⭐
- Claims:
  - Modern engineered systems increasingly involve complex sociotechnical environments where multiple agents must navigate social dilemmas that pit individual interests against collective welfare.
  - Engineered systems are evolving toward multi-agent architectures with autonomous LLM-based agents.
  - Traditional governance approaches are insufficient for these emerging agentic AI systems.

## Synthesis
**Paragraph 1 — Points of Agreement**

Both papers converge on the core premise that contemporary AI systems no longer operate in isolation but as nodes within complex sociotechnical networks involving humans, other AI agents, and heterogeneous institutional actors. They agree that this shift fundamentally breaks single-agent security and governance paradigms, demanding frameworks explicitly designed for multi-agent interaction. Both recognize that traditional risk taxonomies—focused on either AI alignment, cybersecurity, or institutional compliance—are insufficient when systems must reason about *other agents* whose goals, capabilities, and trustworthiness are partially opaque. They also share a methodological commitment to integrating technical design with governance mechanisms from the outset, rather than treating governance as an external audit layer. Finally, both implicitly endorse a defense-in-depth posture: layered technical safeguards (authentication, sandboxing, audit trails) combined with procedural and institutional controls (human oversight, regulatory frameworks).

**Paragraph 2 — Points of Disagreement**

The papers diverge substantially in scope and primary concern. The multi-agent security paper treats the threat landscape as the dominant object of analysis, foregrounding adversarial dynamics—prompt injection across agent boundaries, emergent collusion, identity spoofing, and cascading trust failures—where the central question is *how to make systems of interacting AI agents robust against attack*. The adaptive information governance paper instead centers normative and epistemic coordination, framing the problem as *how heterogeneous agents (human and artificial) can share information, make decisions, and allocate authority under conditions of uncertainty and contested values*. This yields different design philosophies: the security paper privileges containment, verification, and adversarial robustness as first-class objectives, while the governance paper privileges deliberative processes, adaptive norms, and legitimate authority. The security paper is largely agnostic about whether participating agents share aligned goals; the governance paper presupposes that alignment is precisely what must be continuously negotiated.

**Paragraph 3 — Most Urgent Open Question**

The most urgent open question bridging both papers is: **how can we design multi-agent AI systems whose technical security guarantees and governance legitimacy co-evolve
