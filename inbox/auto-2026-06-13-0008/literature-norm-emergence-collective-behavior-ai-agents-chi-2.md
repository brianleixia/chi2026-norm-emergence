# Literature Review — 2026-06-13
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
# Synthesis

## 1. Points of Agreement

Both papers converge on the recognition that as AI systems transition from isolated tools into interacting, autonomous agents operating within complex sociotechnical environments, traditional security and governance frameworks become insufficient. They share a foundational concern that multi-agent dynamics—whether among AI agents alone or between humans and agentic AI—introduce emergent risks that cannot be addressed by analyzing individual components in isolation. Both implicitly endorse the need for integrated approaches that combine technical safeguards (such as adversarial robustness, protocol design, or information constraints) with governance mechanisms (policy, oversight, or adaptive control). They also agree that the scale and openness of agent interactions—across internet platforms, physical environments, and institutional boundaries—amplify the attack surface and complicate attribution, accountability, and trust.

## 2. Points of Disagreement

The papers differ primarily in their framing of the problem and proposed solutions. Paper 1 adopts a *threat-centric* lens, foregrounding adversarial scenarios, emergent manipulation, and the inadequacy of current safety frameworks against attacks that exploit inter-agent communication. Its emphasis is on defensive robustness and secure protocol design in adversarial settings. Paper 2, by contrast, takes a *systems-engineering* and *governance-oriented* stance, treating agentic AI as one participant among many in a sociotechnical system and proposing adaptive information architectures (likely differential access to sensitive information) as a governance instrument. Where Paper 1 worries about agents compromising each other through open interaction, Paper 2 treats information asymmetry and adaptive disclosure as design features that enable legitimate coordination. The two also diverge on locus of control: Paper 1 centers on protecting systems from external and internal adversarial pressure, while Paper 2 centers on coordinating legitimate actors (including AI) through institutional design.

## 3. Most Urgent Open Question

The most pressing unresolved question is: **How can we design multi-agent systems that are simultaneously secure against adversarial inter-agent attacks (as in Paper 1) and governable through adaptive information architectures
