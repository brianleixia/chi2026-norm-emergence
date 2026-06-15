# Literature Review — 2026-06-15
**Query:** norm emergence collective behavior AI agents CHI 2026
**Papers reviewed:** 2

## 1. Open Challenges in Multi-Agent Security: Towards Secure Systems of Interacting AI Agents
- Authors: Christian Schroeder de Witt, Krawiecka, Klaudia, Krawczuk, Igor | Year: 2025 | Venue: arXiv (Cornell University)
- Novelty: ⭐⭐
- Claims:
  - AI agents are beginning to interact with each other directly and across internet platforms and physical environments, creating security challenges beyond traditional cybersecurity and AI safety frameworks.
  - Free-form protocols are essential for AI's task generalization but enable new threats like secret collusion and coordinated swarm attacks.
  - Network effects can rapidly spread privacy breaches across multi-agent systems.

## 2. Integrated Design and Governance of Agentic AI Systems through Adaptive Information Modulation
- Authors: Qiliang Chen, Sepehr Ilami, Nunzio Lorè | Year: 2024 | Venue: arXiv (Cornell University)
- Novelty: ⭐⭐⭐
- Claims:
  - [Could not extract]

## Synthesis
Based on the two paper titles and abstracts provided, I'll synthesize what I can reasonably infer while being transparent about the limits of my analysis given only titles and truncated descriptions.

**1. Points of Agreement**

Both papers appear to converge on the recognition that multi-agent systems—whether AI-AI or human-AI—exceed the analytical capacity of traditional security and governance frameworks. They share a foundational premise: as agents become more autonomous and begin interacting in open environments (digital platforms, physical spaces, or sociotechnical workflows), the resulting system behavior emerges from interactions rather than from any single component. Both seem to advocate for moving beyond siloed approaches (pure cybersecurity in one case, pure technical design in the other) toward integrated frameworks that treat governance, security, and adaptive information flow as coupled design concerns rather than afterthoughts.

**2. Points of Disagreement or Divergent Emphasis**

The papers likely diverge in their primary locus of concern. The first frames the problem as fundamentally one of *security under adversarial conditions*—threats, vulnerabilities, and the integrity of interacting agent populations in open environments. The second appears to frame it as a *design and governance problem*—how to structure adaptive information sharing so that legitimate coordination is enabled while misalignment is controlled. One is essentially asking "how do we keep these systems from being exploited or attacking each other?", while the other asks "how do we design them so they cooperate well in the first place?" These are complementary but distinct framings, and they likely imply different methodologies (threat modeling versus mechanism design) and different evaluation criteria.

**3. Most Urgent Open Question**

The most pressing unresolved question is: *How should security guarantees be specified and verified for open multi-agent systems where agent identities, capabilities, and goals cannot be fully known in advance?* Neither traditional perimeter security (which assumes a trusted inside) nor static governance frameworks (which assume knowable agent types) appear adequate when AI agents can be dynamically created, composed, or compromised. Without a rigorous
