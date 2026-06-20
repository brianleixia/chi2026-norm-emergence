# Literature Review — 2026-06-20
**Query:** norm emergence collective behavior AI agents CHI 2026
**Papers reviewed:** 2

## 1. Open Challenges in Multi-Agent Security: Towards Secure Systems of Interacting AI Agents
- Authors: Christian Schroeder de Witt, Krawiecka, Klaudia, Krawczuk, Igor | Year: 2025 | Venue: arXiv (Cornell University)
- Novelty: ⭐⭐
- Claims:
  - AI agents are beginning to interact with each other directly and across internet platforms and physical environments.
  - Free-form protocols are essential for AI's task generalization but enable new threats like secret collusion and coordinated swarm attacks.
  - Network effects can rapidly spread privacy breaches across multi-agent systems.

## 2. Integrated Design and Governance of Agentic AI Systems through Adaptive Information Modulation
- Authors: Qiliang Chen, Sepehr Ilami, Nunzio Lorè | Year: 2024 | Venue: arXiv (Cornell University)
- Novelty: ⭐⭐⭐
- Claims:
  - Modern engineered systems increasingly involve complex sociotechnical environments where multiple agents, including humans and LLM-based agentic AI, must navigate social dilemmas pitting individual interests against collective welfare.
  - Traditional governance approaches are insufficient for emerging multi-agent architectures with autonomous LLM-based agents.
  - An integrated design and governance framework using adaptive information modulation can address the social dilemmas arising in agentic AI systems.

## Synthesis
# Synthesis of Two Papers on Multi-Agent AI Security and Governance

## 1. Points of Agreement

Both papers converge on the recognition that traditional cybersecurity and AI safety paradigms are insufficient for the emerging landscape of multi-agent AI systems. They agree that as AI agents increasingly interact with one another—across digital platforms, physical environments, and sociotechnical contexts—new vulnerabilities emerge that cannot be addressed through siloed approaches focused on individual models or isolated systems. Both works emphasize the need for governance frameworks that account for the dynamic, adaptive nature of agentic systems, and they share a concern about emergent risks arising from inter-agent communication, delegation, and coordination. Additionally, both papers recognize the importance of designing security and governance mechanisms proactively, rather than retrofitting them after deployment, and they highlight the sociotechnical dimension of these challenges—where human actors, AI agents, and institutional structures must be considered together rather than in isolation.

## 2. Points of Disagreement

The papers differ in their primary focus and proposed solutions. The first paper (*Open Challenges in Multi-Agent Security*) is oriented toward a threat-centric taxonomy, cataloging specific attack surfaces such as adversarial inter-agent communication, compromised tool use, and cross-platform identity spoofing, with an emphasis on technical mitigations like authentication protocols and sandboxing. The second paper (*Integrated Design and Governance of Agentic AI Systems*) takes a more holistic, systems-engineering approach, arguing that security must be embedded into the design process from the outset and governed through adaptive information architectures that span human and machine actors. Where the first paper treats governance as a downstream concern layered atop technical security, the second treats governance as a co-equal design principle. They also differ on the role of formal methods: the second paper leans toward structured governance and verification frameworks, while the first prioritizes empirical threat modeling and red-teaming in deployed, open environments.

## 3. Most Urgent Open Question

The most pressing unresolved question is: **How can we design governance and security mechanisms
