# Literature Review — 2026-06-21
**Query:** norm emergence collective behavior AI agents CHI 2026
**Papers reviewed:** 2

## 1. Open Challenges in Multi-Agent Security: Towards Secure Systems of Interacting AI Agents
- Authors: Christian Schroeder de Witt, Krawiecka, Klaudia, Krawczuk, Igor | Year: 2025 | Venue: arXiv (Cornell University)
- Novelty: ⭐⭐
- Claims:
  - Free-form protocols are essential for AI's task generalization but enable new threats like secret collusion and coordinated swarm attacks.
  - Network effects can rapidly spread privacy breaches across interacting AI agents.
  - Multi-agent AI interactions create security challenges beyond traditional cybersecurity and AI safety frameworks.

## 2. Integrated Design and Governance of Agentic AI Systems through Adaptive Information Modulation
- Authors: Qiliang Chen, Sepehr Ilami, Nunzio Lorè | Year: 2024 | Venue: arXiv (Cornell University)
- Novelty: ⭐⭐⭐
- Claims:
  - Modern engineered systems increasingly involve complex sociotechnical environments where multiple agents, including humans and LLM-based agentic AI, must navigate social dilemmas that pit individual interests against collective welfare.
  - Engineered systems are evolving toward multi-agent architectures with autonomous LLM-based agents, rendering traditional governance approaches insufficient.
  - The work proposes integrated design and governance of agentic AI systems through adaptive information modulation as a solution to address collective action problems in multi-agent sociotechnical settings.

## Synthesis
# Research Synthesis

## Points of Agreement

Both papers converge on the recognition that multi-agent and agentic AI systems introduce fundamentally new security and governance challenges that cannot be adequately addressed by extending traditional cybersecurity or AI safety frameworks in isolation. They share a sociotechnical perspective, emphasizing that these systems involve complex interactions between AI agents, human actors, and digital-physical environments, requiring analysis that accounts for emergent behaviors, coordination dynamics, and trust relationships. Both also implicitly endorse a move toward adaptive, layered, or integrated governance mechanisms rather than static, rule-based controls, and they acknowledge that current technical and policy infrastructures are insufficient for the scale and autonomy of agentic deployments. Additionally, each frames the problem as urgent and under-studied, calling for cross-disciplinary approaches that bridge computer science, systems engineering, and governance theory.

## Points of Disagreement

The papers differ substantively in scope, framing, and proposed solutions. The first paper adopts a *threat-centric* posture, concentrating on adversarial risks, attack surfaces, and defensive postures in systems of interacting AI agents — treating security largely as a problem of preventing misuse, manipulation, and exploitation among agents. The second paper takes a *design-centric and governance-oriented* posture, treating security and trustworthiness as properties to be engineered into agentic systems from the outset via adaptive information governance, with less emphasis on adversarial scenarios and more on alignment, coordination, and institutional mechanisms. Relatedly, they diverge on locus of intervention: the first prioritizes runtime protections and detection across agent interactions at internet and physical scale, while the second emphasizes upstream design choices, information architectures, and governance frameworks that shape agent behavior. Their epistemological orientations also differ — the first is closer to a red-team/attacker-defender paradigm, whereas the second is closer to a systems-engineering and institutional-design paradigm.

## Most Urgent Open Question

The most pressing open question is: **How can we develop unified theoretical and engineering frameworks that simultaneously (a) characterize and mitigate adversarial risks in open, internet
