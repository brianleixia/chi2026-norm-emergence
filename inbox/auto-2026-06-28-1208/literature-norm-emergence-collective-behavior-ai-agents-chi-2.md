# Literature Review — 2026-06-28
**Query:** norm emergence collective behavior AI agents CHI 2026
**Papers reviewed:** 1

## 1. Open Challenges in Multi-Agent Security: Towards Secure Systems of Interacting AI Agents
- Authors: Christian Schroeder de Witt, Krawiecka, Klaudia, Krawczuk, Igor | Year: 2025 | Venue: arXiv (Cornell University)
- Novelty: ⭐⭐
- Claims:
  - AI agents are beginning to interact with each other directly and across internet platforms and physical environments, creating security challenges beyond traditional cybersecurity and AI safety frameworks.
  - Free-form protocols are essential for AI's task generalization but enable new threats like secret collusion and coordinated swarm attacks.
  - Network effects can rapidly spread privacy breaches, di[srupting systems].

## Synthesis
Based on the single paper provided, here is a synthesis:

**1. What does it agree on?**

Since only one paper is available, this synthesis reflects the internal consensus the paper establishes with the broader research community on multi-agent AI security. The paper agrees with existing literature that traditional cybersecurity and AI safety frameworks are insufficient for addressing the emerging security challenges posed by networks of interacting AI agents. It aligns with prior work recognizing that as AI systems gain greater autonomy, agency, and the ability to communicate directly with one another across digital and physical environments, the attack surface expands beyond isolated model vulnerabilities to encompass inter-agent trust, coordination failures, and emergent adversarial dynamics. The paper also converges with established views that securing multi-agent systems requires interdisciplinary thinking, drawing from cryptography, distributed systems, game theory, and formal verification.

**2. Where does it disagree?**

With only one source, there is no inter-paper disagreement to report. However, the paper likely takes positions that depart from narrower treatments in the field—for instance, by emphasizing the inadequacy of single-agent adversarial ML perspectives or by challenging the assumption that safety guarantees can be enforced at the individual model level alone. These implicit tensions with more siloed approaches in adversarial machine learning or classical multi-agent systems research would benefit from triangulation against additional sources.

**3. Most urgent open question?**

The most urgent open question raised is: *how can we formally specify, verify, and enforce security properties in systems composed of multiple interacting AI agents whose behaviors are learned, non-deterministic, and evolving in open environments?* In particular, the field lacks scalable mechanisms for establishing trust and secure communication protocols between AI agents whose policies may be partially opaque, adversarially corrupted, or themselves compromised by indirect prompt injection and manipulation through other agents in the network. Addressing this requires not only new cryptographic and protocol-level tools, but also rigorous benchmarks and threat models that capture the unique dynamics of agent-to-agent adversarial interaction—something the paper positions as a critical and currently unmet research priority.
