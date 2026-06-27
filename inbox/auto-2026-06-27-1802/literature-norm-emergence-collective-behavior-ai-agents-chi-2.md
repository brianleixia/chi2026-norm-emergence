# Literature Review — 2026-06-27
**Query:** norm emergence collective behavior AI agents CHI 2026
**Papers reviewed:** 1

## 1. Open Challenges in Multi-Agent Security: Towards Secure Systems of Interacting AI Agents
- Authors: Christian Schroeder de Witt, Krawiecka, Klaudia, Krawczuk, Igor | Year: 2025 | Venue: arXiv (Cornell University)
- Novelty: ⭐⭐
- Claims:
  - AI agents are beginning to interact with each other directly and across internet platforms and physical environments, creating security challenges beyond traditional cybersecurity and AI safety frameworks.
  - Free-form protocols are essential for AI's task generalization but enable new threats like secret collusion and coordinated swarm attacks.
  - Network effects can rapidly spread privacy breaches across interconnected multi-agent systems.

## Synthesis
**Points of agreement:**

All work surveyed converges on the recognition that multi-agent AI systems introduce security challenges that fundamentally exceed the scope of existing cybersecurity and single-agent AI safety paradigms. The authors agree that the interactive dynamics between agents—negotiation, delegation, coordination, and emergent protocol formation—create new attack surfaces where adversaries can exploit inter-agent trust, manipulate communication channels, or induce cascading failures across agent populations. There is consensus that current frameworks are inadequate because they treat agents as isolated units, failing to account for emergent group behaviors, protocol-level vulnerabilities, and the ways malicious actors can strategically position compromised agents within larger ecosystems. The paper emphasizes that security must be understood as a system-level property emerging from agent interactions, not merely a property of individual models.

**Points of disagreement or tension:**

The primary tension lies between two competing framings of where the greatest risks reside. One perspective prioritizes *technical* vulnerabilities—prompt injection across agent boundaries, compromised tool-use interfaces, and adversarial manipulation of inter-agent protocols—treating multi-agent security as an extension of classical systems security. Another perspective emphasizes *socio-technical* risks, arguing that the most consequential threats emerge from agents acting as proxies for human actors, enabling new forms of fraud, social engineering at scale, and erosion of accountability when actions are distributed across many opaque actors. Additionally, there is unresolved debate about whether the field should focus on *defensive* measures (robust protocols, verification mechanisms, containment architectures) or whether the interactive nature of these systems demands *proactive* governance approaches—audit trails, identity frameworks, and regulatory oversight—before technical defenses mature. The appropriate unit of analysis is also contested: individual agent, dyadic interaction, or population-level dynamics.

**Most urgent open question:**

How can we design multi-agent systems that preserve the benefits of autonomous agent-to-agent coordination while maintaining verifiability, accountability, and containment when any individual agent may be compromised or act in bad faith? This question is urgent because deployment is outpacing the
