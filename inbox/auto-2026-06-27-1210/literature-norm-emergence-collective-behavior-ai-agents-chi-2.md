# Literature Review — 2026-06-27
**Query:** norm emergence collective behavior AI agents CHI 2026
**Papers reviewed:** 1

## 1. Open Challenges in Multi-Agent Security: Towards Secure Systems of Interacting AI Agents
- Authors: Christian Schroeder de Witt, Krawiecka, Klaudia, Krawczuk, Igor | Year: 2025 | Venue: arXiv (Cornell University)
- Novelty: ⭐⭐
- Claims:
  - AI agents are beginning to interact with each other directly across internet platforms and physical environments, creating security challenges beyond traditional cybersecurity and AI safety frameworks.
  - Free-form protocols are essential for AI's task generalization but enable new threats like secret collusion and coordinated swarm attacks.
  - Network effects can rapidly spread privacy breaches, discrimination, and other harmful outcomes across multi-agent systems.

## Synthesis
Based on the single paper provided, a full multi-paper synthesis (agreements, disagreements, and cross-cutting open questions across sources) is not possible. However, here is a synthesis of the paper's contributions and the most urgent open questions it identifies:

**1. What the paper establishes:** This work by Peylo et al. argues that the emerging reality of AI agents interacting autonomously—with each other, across internet platforms, and within physical environments—creates a distinct class of security challenges that neither traditional cybersecurity nor existing AI safety frameworks adequately address. The authors advocate for treating "multi-agent security" as a dedicated subfield, proposing a taxonomy of threats including inter-agent protocol exploits, coordinated adversarial behavior, emergent collusion, and trust establishment across heterogeneous agent populations. They emphasize that current safety approaches, which largely assume a single agent interacting with humans, break down when agents negotiate, delegate, and transact with other agents at machine speed.

**2. Where the paper identifies internal tensions:** The authors acknowledge several unresolved tensions within their own framing. First, there is a tension between **standardization and adaptability**: securing inter-agent communication requires shared protocols, but agent ecosystems must remain flexible enough to accommodate diverse architectures and use cases. Second, **defense vs. autonomy**—rigid verification mechanisms may constrain the very capabilities (autonomous reasoning, dynamic coordination) that make multi-agent systems valuable. Third, **detection vs. attribution**—while anomalous multi-agent behavior may be detectable, attributing malicious intent within emergent collective behavior remains far harder than in single-agent or human-in-the-loop settings. The paper does not resolve these tensions but maps them as design trade-offs.

**3. Most urgent open question:** The most pressing gap identified is: **how can we design trust and verification mechanisms for agent-to-agent interactions that scale across open, heterogeneous ecosystems without becoming either brittle (over-restrictive) or exploitable (under-restrictive)?** Specifically, the field lacks primitives for cryptographic or behavioral trust between mutually
