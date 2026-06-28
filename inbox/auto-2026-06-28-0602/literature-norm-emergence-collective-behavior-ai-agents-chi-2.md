# Literature Review — 2026-06-28
**Query:** norm emergence collective behavior AI agents CHI 2026
**Papers reviewed:** 1

## 1. Open Challenges in Multi-Agent Security: Towards Secure Systems of Interacting AI Agents
- Authors: Christian Schroeder de Witt, Krawiecka, Klaudia, Krawczuk, Igor | Year: 2025 | Venue: arXiv (Cornell University)
- Novelty: ⭐⭐
- Claims:
  - AI agents are beginning to interact with each other directly across internet platforms and physical environments, creating security challenges beyond traditional cybersecurity and AI safety frameworks.
  - Free-form protocols, while essential for AI's task generalization, enable new threats such as secret collusion and coordinated swarm attacks.
  - Network effects in multi-agent AI systems can rapidly spread privacy breaches.

## Synthesis
# Research Synthesis: Multi-Agent Security

## Points of Agreement

The single paper, *Open Challenges in Multi-Agent Security*, establishes a foundational consensus that as AI agents increasingly interact with each other—across internet platforms, physical environments, and enterprise systems—the resulting security challenges cannot be adequately addressed by traditional cybersecurity or single-agent AI safety frameworks alone. There is implicit agreement that the field is nascent and that a dedicated discipline must emerge to study the emergent vulnerabilities, attack surfaces, and defensive postures unique to systems of interacting AI agents. The paper positions multi-agent interaction as a qualitatively distinct problem space requiring new theoretical foundations, not merely an extension of existing work in adversarial machine learning, agent-based modeling, or distributed systems security.

## Points of Disagreement

With only a single source provided, there is no internal set of competing claims to adjudicate. However, the paper's framing implicitly identifies tensions within the broader research community that the synthesis it provides is meant to resolve or surface: for instance, between researchers who frame multi-agent risks as fundamentally an *AI alignment* problem (focused on individual agent goals and values) versus those who frame it as a *systems security* problem (focused on protocols, trust, and communication channels). The paper's integrative scope suggests these communities have not yet converged on shared terminology, threat models, or evaluation methodologies.

## Most Urgent Open Question

The most urgent open question raised is: **How can we formally model and reason about adversarial interactions between autonomous AI agents operating at scale across open environments, where the set of agents, their capabilities, and their objectives are not known a priori?** Without such a formalism, it remains impossible to rigorously characterize which multi-agent configurations are safe, to design provably secure interaction protocols, or to predict emergent behaviors—such as collusion, manipulation, or cascading failures—before they manifest in deployed systems. This foundational gap blocks progress on nearly every downstream challenge the paper identifies, from detection of coordinated agent attacks to the design of trustworthy agent-to-agent communication
