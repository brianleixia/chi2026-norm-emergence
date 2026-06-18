# Literature Review — 2026-06-18
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
  - Modern engineered systems increasingly involve complex sociotechnical environments where multiple agents, including humans and agentic AI powered by large language models, must navigate social dilemmas that pit individual interests against collective welfare.
  - Agentic AI systems are evolving toward multi-agent architectures with autonomous LLM-based agents, challenging traditional governance approaches.
  - Integrated design and governance of agentic AI systems requires adaptive information modulation to address the complexities of multi-agent sociotechnical environments.

## Synthesis
**1. Points of Agreement**

Both papers converge on the recognition that multi-agent and agentic AI systems introduce qualitatively new security and governance challenges that exceed the scope of traditional cybersecurity or single-model AI safety frameworks. They share an assumption that as AI agents gain autonomy, tool access, and the ability to interact with other agents (and humans) in open environments, the attack surface expands in ways that cannot be managed by analyzing individual models in isolation. Both works also emphasize the need for systemic, architectural, and governance-level interventions—rather than purely model-level fixes—to address risks such as emergent behavior, unauthorized coordination, and cascading failures. Furthermore, each paper implicitly endorses a sociotechnical view: security and safety are not properties of algorithms alone but emerge from interactions among agents, protocols, and human operators.

**2. Points of Disagreement**

The papers diverge in focus and methodological orientation. The first paper is primarily concerned with *threat modeling* in open, internet-mediated multi-agent systems, foregrounding adversarial scenarios such as agent impersonation, prompt injection across agent boundaries, and the exploitation of inter-agent communication protocols. Its frame is closer to classical security thinking—identifying vulnerabilities, attacker capabilities, and defensive countermeasures. The second paper, by contrast, centers on *integrated design and adaptive governance*, treating security as one concern among several (alongside alignment, accountability, and value alignment) and proposing continuous information-theoretic or feedback-based mechanisms to govern agent behavior over time. In short, the first asks "how can systems of interacting agents be attacked and defended?" while the second asks "how should agentic systems be designed and steered so that they remain safe and aligned throughout their operation?" They also differ on the locus of intervention: external protocol hardening versus embedded governance loops.

**3. Most Urgent Open Question**

The most pressing unresolved question is: *How can we design inter-agent interaction protocols and governance mechanisms that are simultaneously robust against adversarial manipulation and adaptive enough to maintain alignment as agent capabilities and deployment
