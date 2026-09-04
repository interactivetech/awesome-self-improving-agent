# Awesome Self-Improving Agents

A curated, **paper-first** index of research and public codebases for LLM agents and agent systems that improve a persistent part of themselves: prompts/context, skills, harnesses, workflows, multi-agent topology, routing, policy/model parameters, or reusable procedural knowledge.

Inspired in part by [DEEP-JLU/Awesome-Graph-Engineering](https://github.com/DEEP-JLU/Awesome-Graph-Engineering), with a narrower focus on **self-improvement, harness evolution, and system evolution**.

> **Inclusion rule:** a method should change something reusable across tasks or runs. A one-off critique/retry loop is normally classified as *self-correction*, not persistent self-improvement.

## Research map

We track methods across:
- **Prompt & context evolution**
- **Skill & memory evolution**
- **Harness & runtime evolution**
- **Workflow & agent-architecture evolution**
- **Multi-agent topology, routing & coordination evolution**
- **Policy/model evolution**
- **Reusable procedural/environment knowledge**

## Papers with verified public code

| Method | Paper | Venue | Code | What improves | Code status |
|---|---|---|---|---|---|
| **TextGrad** | [TextGrad: Automatic “Differentiation” via Text](https://arxiv.org/abs/2406.07496) | arXiv 2024 | [zou-group/textgrad](https://github.com/zou-group/textgrad) | Prompts / textual variables | `official` |
| **Self-Harness** | [Self-Harness: Harnesses That Improve Themselves](https://arxiv.org/abs/2606.09498) | arXiv 2026 | [qzzqzzb/Self-Harness](https://github.com/qzzqzzb/Self-Harness) | Harness / runtime | `official` |
| **Meta-Harness** | [Meta-Harness: End-to-End Optimization of Model Harnesses](https://arxiv.org/abs/2603.28052) | arXiv 2026 | [stanford-iris-lab/meta-harness](https://github.com/stanford-iris-lab/meta-harness) | Harness / context plumbing | `official` |
| **HarnessFix** | [From Failed Trajectories to Reliable LLM Agents: Diagnosing and Repairing Harness Flaws](https://arxiv.org/abs/2606.06324) | arXiv 2026 | [HarnessFix/HarnessFix](https://github.com/HarnessFix/HarnessFix) | Harness / runtime | `official` |
| **Agentic Harness Engineering** | [Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses](https://arxiv.org/abs/2604.25850) | arXiv 2026 | [mqbazhaoyu/ahe](https://github.com/mqbazhaoyu/ahe) | Harness / runtime | `third-party` |
| **ReCreate** | [ReCreate: Reasoning and Creating Domain Agents Driven by Experience](https://aclanthology.org/2026.acl-long.1432/) | ACL 2026 | [zz-haooo/ReCreate](https://github.com/zz-haooo/ReCreate) | Agent scaffold / domain architecture | `official` |
| **SkillGraph** | [SkillGraph: Self-Evolving Multi-Agent Collaboration with Multimodal Graph Topology](https://arxiv.org/abs/2604.17503) | arXiv 2026 | [niez233/skillgraph](https://github.com/niez233/skillgraph) | Skills + multi-agent topology | `official` |
| **Swarm Skills / JiuwenSwarm** | [Swarm Skills: A Portable, Self-Evolving Multi-Agent System Specification for Coordination Engineering](https://arxiv.org/abs/2605.10052) | arXiv 2026 | [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | Shared swarm skills / coordination | `reference` |
| **APEX** | [APEX: Autonomous Policy Exploration for Self-Evolving LLM Agents](https://arxiv.org/abs/2605.21240) | arXiv 2026 | [liushiliushi/APEX1](https://github.com/liushiliushi/APEX1) | Policy / persistent strategy map | `official` |
| **AgentNet** | [AgentNet: Decentralized Evolutionary Coordination for LLM-based Multi-Agent Systems](https://arxiv.org/abs/2504.00587) | NeurIPS 2025 | [zoe-yyx/AgentNet](https://github.com/zoe-yyx/AgentNet) | Coordination topology + agent specialization | `official` |
| **Harness-RL** | [Harness-RL: Black-Box Reinforcement Learning with Action-Args Decoupling for Central-Agent Multi-Agent Harnesses](https://arxiv.org/abs/2608.29641) | PCC 2026 | [jiangxinke/Harness-RL](https://github.com/jiangxinke/Harness-RL) | Central-agent policy / multi-agent harness coordination | `official` |
| **SafeEvolve** | [SafeEvolve: Harness-Policy Co-Evolution from Agent Experience for Safety Alignment](https://arxiv.org/abs/2609.02786) | arXiv 2026 | [MaoPopovich/SafeEvolve](https://github.com/MaoPopovich/SafeEvolve) | Safety prompt + hierarchical skills + policy | `official` |
| **Self-Refine** | [Self-Refine: Iterative Refinement with Self-Feedback](https://arxiv.org/abs/2303.17651) | NeurIPS 2023 | [madaan/self-refine](https://github.com/madaan/self-refine) | Current output | `official-borderline` |
| **GPTSwarm** | [GPTSwarm: Language Agents as Optimizable Graphs](https://arxiv.org/abs/2402.16823) | ICML 2024 | [metauto-ai/GPTSwarm](https://github.com/metauto-ai/GPTSwarm) | Agent graph | `official` |
| **ADAS** | [Automated Design of Agentic Systems](https://arxiv.org/abs/2408.08435) | ICLR 2025 | [ShengranHu/ADAS](https://github.com/ShengranHu/ADAS) | Agent architecture / program | `official` |

## Papers being watched for code

| Method | Paper | Venue | What improves | Current status |
|---|---|---|---|---|
| **RHO** | [Evolving Agents in the Dark: Retrospective Harness Optimization via Self-Preference](https://arxiv.org/abs/2606.05922) | arXiv 2026 | Harness / runtime | `paper-only` |
| **HARBOR** | [HARBOR: Automated Harness Optimization](https://arxiv.org/abs/2604.20938) | arXiv 2026 | Harness / runtime | `paper-only` |
| **EvoHarness-RL** | [EvoHarness-RL: Learning Self-Evolving Runtime Harness for Long-Horizon LLM Agents](https://arxiv.org/abs/2608.05446) | arXiv 2026 | Harness state + harness-use policy | `paper-only` |
| **Living-Harness** | [Living-Harness Is an Interactive-Agent Evolver](https://arxiv.org/abs/2607.26598) | arXiv 2026 | Harness / interactive agent | `paper-only` |
| **QueenBee Planner** | [QueenBee Planner: Skill-Evolving Communication Topologies for Token-Efficient LLM Multi-Agent Systems](https://arxiv.org/abs/2606.27492) | arXiv 2026 | Skills + communication topology | `preview` |

> Agentic Harness Engineering has a tracked third-party implementation, but remains on the structured watchlist for an author-released implementation.

## Code-backed projects whose paper metadata is still being verified

These repositories stay in the project index while their canonical paper relationship is verified. The updater should promote them into the paper table only when the paper↔code connection is supported.

| Project | Paper metadata |
|---|---|
| **ACE** | Public code is tracked; canonical paper metadata is queued for verification. |
| **SAGE** | Public code is tracked; canonical paper metadata is queued for verification. |
| **Agent Lightning** | Public code is tracked; canonical paper metadata is queued for verification. |
| **Adaptive Auto-Harness** | Public code is tracked; canonical paper metadata is queued for verification. |
| **Evo-Harness** | Public code is tracked; canonical paper metadata is queued for verification. |
| **AutoFlow** | Public code is tracked; canonical paper metadata is queued for verification. |
| **AFlow** | Public code is tracked; canonical paper metadata is queued for verification. |
| **A2Flow** | Public code is tracked; canonical paper metadata is queued for verification. |
| **MermaidFlow** | Public code is tracked; canonical paper metadata is queued for verification. |
| **TacoMAS** | Public code is tracked; canonical paper metadata is queued for verification. |
| **EvolveRouter** | Public code is tracked; canonical paper metadata is queued for verification. |
| **Meta-Team** | Public code is tracked; canonical paper metadata is queued for verification. |
| **ProPlay** | Public code is tracked; canonical paper metadata is queued for verification. |

## How we classify code

- `official` — released by the paper/project authors, their lab/company, or explicitly linked as the official implementation.
- `reference` — an official or closely associated reference platform implementing the method.
- `third-party` — independent reproduction.
- `official-borderline` — official code relevant to the topic but closer to self-correction than persistent self-improvement.
- `paper-only` — paper verified, but no public implementation verified.
- `preview` — public research preview exists but is not yet treated as a mature implementation.

## Paper ↔ code lifecycle

`paper-only → preview/third-party code → official code → mature/reproducible release`

The repository preserves that lifecycle instead of treating research papers and GitHub repositories as interchangeable.

## Data

- [`data/papers.yml`](data/papers.yml) — paper-centric registry.
- [`data/projects.yml`](data/projects.yml) — code-backed project registry.
- [`data/watchlist.yml`](data/watchlist.yml) — methods to re-check for releases and verification upgrades.

## Maintenance

Reviewed **every three days** for:

- newly published self-improving-agent, self-evolving-agent, and harness-evolution papers,
- new papers added to upstream surveys and awesome lists,
- venue/publication updates for existing papers,
- newly released official code,
- useful third-party reproductions,
- paper-only methods gaining code,
- preview code becoming runnable/mature,
- corrected paper ↔ repository relationships.

Every meaningful maintenance pass should update the README **and** structured data. No-change checks should not create commits.

Last meaningful verification: **2026-09-04**.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Research-backed submissions should include both the **canonical paper** and the **code provenance**.

## Related resources

- [Awesome Graph Engineering](https://github.com/DEEP-JLU/Awesome-Graph-Engineering)
- [A Survey of Self-Evolving Agents](https://arxiv.org/abs/2507.21046)
- [Agent Harness Engineering: A Survey](https://openreview.net/forum?id=eONq7FdiHa)

## License

MIT. See [LICENSE](LICENSE).
