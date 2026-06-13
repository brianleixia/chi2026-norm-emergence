# Literature Review — 2026-06-13
**Query:** norm emergence collective behavior AI agents CHI 2026
**Papers reviewed:** 2

## 1. Open Challenges in Multi-Agent Security: Towards Secure Systems of Interacting AI Agents
- Authors: Christian Schroeder de Witt, Krawiecka, Klaudia, Krawczuk, Igor | Year: 2025 | Venue: arXiv (Cornell University)
- Novelty: ⭐⭐
- Claims:
  - Free-form protocols are essential for AI's task generalization but enable new threats like secret collusion and coordinated swarm attacks.
  - Network effects can rapidly spread privacy breaches, dis...

## 2. Integrated Design and Governance of Agentic AI Systems through Adaptive Information Modulation
- Authors: Qiliang Chen, Sepehr Ilami, Nunzio Lorè | Year: 2024 | Venue: arXiv (Cornell University)
- Novelty: ⭐⭐⭐
- Claims:
  - Modern engineered systems increasingly involve complex sociotechnical environments where multiple agents must navigate social dilemmas that pit individual interests against collective welfare.
  - Agentic AI powered by large language models are emerging as a new paradigm of agents in multi-agent architectures.
  - Traditional governance approaches are insufficient for multi-agent architectures with autonomous LLM-based agents.

## Synthesis
# Research Synthesis: Multi-Agent AI Security and Governance

**1. Points of Agreement**
Both papers recognize that the emergence of multi-agent AI systems—particularly those involving LLM-powered agentic AI—represents a fundamental shift beyond traditional cybersecurity paradigms. They converge on the view that conventional security and safety frameworks, designed for single-system or human-only contexts, are insufficient for environments where autonomous agents interact with each other, with humans, and across digital-physical boundaries. Both works also acknowledge that governance cannot be an afterthought bolted onto technical design; rather, security, alignment, and coordination mechanisms must be embedded throughout the system lifecycle. They share an underlying concern that as agents gain greater autonomy and inter-agent communication capabilities, the attack surface expands in qualitatively new ways, including novel vectors like prompt injection across agent channels, collusion, and emergent unsafe behaviors arising from agent-to-agent dynamics.

**2. Points of Disagreement**
The papers diverge in their primary framing of the core problem. The first paper foregrounds *security* in a relatively conventional threat-modeling sense—emphasizing adversarial attacks, vulnerabilities, and defensive measures against malicious actors exploiting multi-agent interactions. The second paper adopts a broader *governance and design* lens, treating security as one concern among many within a sociotechnical system that includes human stakeholders, institutional processes, and adaptive information architectures. There is also a tension in proposed solutions: the security-focused work tends toward technical safeguards (authentication, sandboxing, cryptographic verification of agent communications), while the governance-focused work emphasizes co-design methodologies, feedback loops between design and deployment, and adaptive mechanisms that evolve with system behavior. The first implicitly treats humans as potential threats or operators to be protected from, whereas the second positions humans as integral co-agents whose values and oversight must be architecturally supported.

**3. Most Urgent Open Question**
The most pressing unresolved question is: **How can we develop security and governance frameworks for multi-agent AI systems that are simultaneously technically robust against adversarial threats AND adaptive enough to preserve
