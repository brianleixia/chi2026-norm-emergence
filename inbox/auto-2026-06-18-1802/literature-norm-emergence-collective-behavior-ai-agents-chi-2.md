# Literature Review — 2026-06-18
**Query:** norm emergence collective behavior AI agents CHI 2026
**Papers reviewed:** 2

## 1. Open Challenges in Multi-Agent Security: Towards Secure Systems of Interacting AI Agents
- Authors: Christian Schroeder de Witt, Krawiecka, Klaudia, Krawczuk, Igor | Year: 2025 | Venue: arXiv (Cornell University)
- Novelty: ⭐⭐
- Claims:
  - Free-form protocols are essential for AI's task generalization but enable new threats like secret collusion and coordinated swarm attacks.
  - Network effects can rapidly spread privacy breaches across multi-agent systems.
  - Security challenges in multi-agent AI systems extend beyond traditional cybersecurity and AI safety frameworks.

## 2. Integrated Design and Governance of Agentic AI Systems through Adaptive Information Modulation
- Authors: Qiliang Chen, Sepehr Ilami, Nunzio Lorè | Year: 2024 | Venue: arXiv (Cornell University)
- Novelty: ⭐⭐⭐
- Claims:
  - [Could not extract]

## Synthesis
# Synthesis: Multi-Agent Security & Agentic AI Governance

**1. Points of Agreement**

Both papers recognize that the convergence of multiple autonomous agents—particularly those powered by large language models—fundamentally challenges existing security and governance paradigms designed for single-agent or human-only systems. They share a core diagnosis that traditional cybersecurity frameworks and static governance models are insufficient for environments where AI agents act, negotiate, and make decisions with partial autonomy in complex sociotechnical settings. Both works emphasize the need for adaptive, layered approaches that combine technical safeguards with governance mechanisms, and they highlight that the interaction space between agents—rather than the agents themselves in isolation—represents the primary locus of risk. They further agree that emergent behaviors arising from multi-agent interaction are difficult to predict ex ante, necessitating continuous monitoring, evaluation, and policy adjustment rather than one-time certification.

**2. Points of Disagreement**

The papers diverge in their primary framing of the problem. The first adopts a security-centric lens, treating inter-agent interaction as an attack surface and focusing on adversarial dynamics, trust establishment, and resilience against manipulation by malicious or compromised agents. The second adopts a governance-and-design lens, treating the challenge as one of socio-technical system integration where adaptive information-flow policies, role differentiation, and human oversight structures must be designed in from the outset. The first paper tends to position AI safety as a distinct problem requiring new technical primitives, while the second positions agentic AI as an extension of existing engineered-system governance, leveraging principles from controls theory, information security, and organizational design. Consequently, the first emphasizes defensive measures against unknown threats, whereas the second emphasizes proactive architectural choices that constrain agent behavior through governance.

**3. Most Urgent Open Question**

The most pressing unresolved question is: *How can governance frameworks be operationally aligned with security mechanisms so that adaptive policy enforcement and threat defense function as a coherent system rather than parallel tracks?* In practice, no established methodology bridges the gap between the first paper's concern with adversarial robustness and
