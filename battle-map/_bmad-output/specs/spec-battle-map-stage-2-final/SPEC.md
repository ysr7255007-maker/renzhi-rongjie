---
id: spec-battle-map-stage-2-final
companions:
  - '_bmad-output/planning-artifacts/architecture/architecture-project-map-bmad-2026-09-02/ARCHITECTURE-SPINE.md'
sources:
  - '_bmad-output/planning-artifacts/prds/prd-project-map-bmad-2026-09-01/prd.md'
  - 'reference/BATTLE-MAP.md'
---

# Battle Map Stage-2 Final — Project Semantic System and Execution Engine

## Why

**A pain to solve:** Long-term development loses the complete shape when too much detail accumulates before product structure is established and continuously validated. Projects have no persistent projection layer that maps real implementation progress back onto an evolving model of what the final system should be, making local decisions unintelligible within global shape and unrevisable when evidence contradicts earlier assumptions.

**Who is affected:** Product owners, developers, and AI workers executing on behalf of projects struggle to understand project goals, complete functions, current frontier state, evidence coverage, and next-move rationale without prerequisite knowledge of internal mechanisms or external methodologies.

**Backdrop:** Existing BMAD mechanisms (persistent persona patterns, multi-round workflows, durable handoff artifacts, explicit authority boundaries, deterministic control-plane discipline) are proven but currently exposed through methodology-specific terminology; Battle Map absorbs these durable mechanisms into battle-map-native components while digesting BMAD origins as internal reference only.

This is the anchor every downstream trade-off resolves against.

## Capabilities

- **CAP-1** Users can interact with Battle Map through a single system interface showing current goal, function structure, frontier state, evidence coverage, and next-move rationale.
  - **intent:** User opens Project Map and understands project shape without needing BMAD terminology or external reference.
  - **success:** First screen answers "what does this project become, where are we, what routes are open/blocked, and why is the next move reasonable?"

- **CAP-2** Users can dispatch work by selecting action classes (explore, shape, implement, verify, close) which trigger autonomous workers configured for that action type.
  - **intent:** User selects action class from recommended frontier and worker executes under deterministic control-plane discipline.
  - **success:** Worker produces terminal status (OK/FAILURE/BLOCKED/PARTIAL) with blocking condition and followup recommendations; coordinator recompiles fresh bootstrap based on weaving results.

- **CAP-3** Battle Map presents projects as goals → complete functions → regions → milestones → structure relations → frontier → evidence boundaries → unknowns, not as task lists or role-based work queues.
  - **intent:** User views project structure in capability-complete form rather than execution-unit granularity.
  - **success:** Each structural element has observable criteria; user can trace how nodes combine to achieve project goal.

- **CAP-4** Battle Map maintains project-level semantics: goals defining success in observable conditions; complete functions with defined inputs/core behavior/outputs/contribution; regions grouping related functions; milestones as verifiable behavioral evidence; structure relations (serial/parallel/dependency/join) between nodes; frontier showing active/ready/blocked/completed states.
  - **intent:** System preserves durable project cognition as semantic relationships rather than raw facts.
  - **success:** Query interfaces return coherent project shape with applied validity boundaries and candidate overlays.

- **CAP-5** Battle Map tracks current-validity/unknown/blocking/frontier boundaries; shows which functions/relations/assumptions are treated as established enough to advance from; what is structurally uncertain/untested/likely to change; which previously accepted relation should no longer guide advancement.
  - **intent:** User knows exactly which parts of project structure are confidence vs speculation.
  - **success:** Frontier visualization highlights blocked paths with blocker reasons; unknown boundaries are explicitly marked with impact assessment.

- **CAP-6** Battle Map supports candidate structural changes derived from distilled implications; maintains adopted vs pending shape distinction; Project Narrative as append-only explanation of how project route/method/understanding evolved over time with causal links between prior direction/trigger/new judgment/impact.
  - **intent:** Structural revision is immediate yet distinguished from adopted reality.
  - **success:** Candidate overlay visible without becoming adopted; narrative entry explains route change causality without replaying raw incident.

- **CAP-7** Battle Map implements seven-layer native architecture: Layer 7 (Sources/Adapter); Layer 6 (Execution/Verification Runtime with deterministic control-plane discipline); Layer 5 (Composable Cognitive Runtime - Persona/Authority/Skill bundle/Handoff contract/Session identity); Layer 4 (Advancement/Command Engine with coordinator that reads shape/selects action/compiles bootstrap); Layer 3 (Project Weaving/Auto-Association pipeline); Layer 2 (Project Shape Semantic Store with materialized views); Layer 1 (Experience/Projection Layer UI).
  - **intent:** Clear separation between raw fact sources, semantic ingestion, cognitive composition, command orchestration, durable storage, and user presentation.
  - **success:** Seven-layer data/control loop flows coherently; each layer has single responsibility; provider-specific concepts contained behind adapters.

- **CAP-8** Battle Map supports composable role instantiation: Persona + Authority scope + Skill bundle + Workflow protocol + Handoff contract + Session identity; responsible continuity policy based on whether same cognitive responsibility is continuous; fresh context for true role transitions/independent verification/boundary isolation.
  - **intent:** Role is assembled from parts at dispatch time rather than being fixed job title.
  - **success:** Composed role persists for responsibility lifecycle; session resumes from durable handoff / project DB snapshot when fresh context required.

- **CAP-9** Battle Map implements deterministic worker execution: one worker per unit; frozen bootstrap at dispatch; auditable protocol steps/state transitions; explicit terminal states (OK/FAILURE/BLOCKED/PARTIAL); no mid-run injection from outer layers; control surface guaranteed deterministic while worker internal cognition may be LLM-stochastic.
  - **intent:** Execution boundary guarantees coordinator selects worker but cannot inject new decisions mid-run.
  - **success:** Terminal status includes status field/blocking_condition/followup_review_recommended/baseline_revision/files_changed/results_summary; orchestrator acts on verdict rather than inferring from chat output.

- **CAP-10** Battle Map implements Project Weaving pipeline: incremental delta reader with per-source cursors; semantic distiller extracting relations/boundaries/route implications/lessons; auto-association engine distinguishing working association from durable semantic candidate (relation change/boundary change/route revision/narrative lesson).
  - **intent:** External source events enter temporary fact workset and only distilled implications become durable.
  - **success:** Weaving emits candidates to authority workflow; rejected candidates leave no permanent record unless they taught reusable lesson.

- **CAP-11** Battle Map provides source adapter layer translating external systems (method artifacts/Harness/IDE/Git/tests/reviews/runtime) into temporary working input for weaving; supports on-demand source context access when current judgment cannot be made from distilled semantics alone.
  - **intent:** Raw source systems remain authoritative; Battle Map owns only distilled meaning.
  - **success:** Adapter provides cursor-based delta reading; original source re-openable on demand with context showing which decision needs it and what should be distilled.

- **CAP-12** Battle Map implements Advancement Coordinator responsibilities: reads current adopted project shape/candidates/boundaries/frontier from one consistent snapshot; evaluates which action classes are legal/useful (Analysis/Discovery, Planning/Shaping, Implementation, Verification at Joins, Function/Region Closure, Correct Course); compiles frozen bootstrap; escalates only when authority policy requires it.
  - **intent:** Action selection is autonomous except for irreversible/high-cost/significant-meaning decisions.
  - **success:** Coordinator chooses worker and compiles bootstrap; escalation format presents specific question/context summary/recommended option with justification/alternative options with tradeoffs.

- **CAP-13** Battle Map provides next move rationale explaining why recommended action follows from current shape/blockers/unknown boundaries/route state/applicable lessons; shows what relation makes action possible, which blocker addressed, how it affects route/join, which lesson applies, and whether decision is delegated or escalates.
  - **intent:** Recommendation is justifiable from structure, not arbitrary scheduling.
  - **success:** Next move explanation ties back to explicit project structure/unknown boundaries/route state/applicable lessons; alternatives shown when multiple routes remain reasonable.

- **CAP-14** Battle Map Project Shape Semantic Store owns current durable project shape (minimal meaning of goals/functions/regions/milestones; first-class relations; adopted shape + active candidate overlays; current validity/unknown/frontier boundaries needed to advance; meaningful route revisions); does not own raw Git/Test/Review/Harness streams or forensic evidence archive.
  - **intent:** Semantic core preserves project meaning without becoming archaeological record.
  - **success:** Project Narrative separate responsibility; Weaving operational state (cursors/temporary worksets) distinct from long-lived truth; runtime state (session bindings) ephemeral.

- **CAP-15** Battle Map exposes query model interfaces: get-current-project-shape; get-local-shape {region_or_function}; get-frontier-and-legal-moves; get-candidate-overlays; get-applicable-lessons {target}; get-current-action-context.
  - **intent:** Client code retrieves coherent shape views for specific purposes without combining versioned snapshots.
  - **success:** Each query returns semantically consistent view; shape revision tracking binds dispatch to immutable snapshot.

- **CAP-16** Battle Map implements verification at joins: dependency patterns trigger verification dispatch before dependent work proceeds; integration defects caught earlier at join points rather than accumulating at completion; function/region closure remains primary review mechanism with retrospective on lessons learned.
  - **intent:** Integration testing progressive at natural junctions, not deferred to completion.
  - **success:** Join verification worker runs triage with high/medium/low/false positive/maybe false positive classification; deferred findings logged separately with severities.

## Constraints

- **AD-1 — [ADOPTED]** Project Shape is the durable semantic authority; durable project cognition expressed as minimal node semantics plus first-class project relations and small current validity/unknown/advancement boundaries; raw execution facts never the canonical project semantics.

- **AD-2 — [ADOPTED]** Map, Narrative, and temporary facts are separate responsibility classes; Battle Map preserves current shape and route structure; Project Narrative preserves only route/method/process lessons worth reusing; raw facts remain in external sources or non-canonical temporary workset.

- **AD-3 — [ADOPTED]** Weaving is the only raw-reality semantic ingress; external changes must pass through incremental reading and semantic distillation before they may become relation/boundary/lesson candidates; undistilled facts cannot write adopted Project Shape.

- **AD-4 — [ADOPTED]** Shape adoption has one semantic-version consistency boundary; adopted change that alters Project Shape creates one coherent semantic version; derived frontier/route availability/projections must identify against their source semantic version; readers may not combine versions in one decision/bootstrap.

- **AD-5 — [ADOPTED]** Advancement reads and dispatches; it does not discover structure or derive structural candidates from raw facts or inject new project decisions into a running worker.

- **AD-6 — [ADOPTED]** Cognitive responsibility is composable and version-bound; composed from Persona + Authority + Skill bundle + Workflow protocol + Handoff contract + Session identity; reusable definitions versioned independently; each bootstrap binds exact definitions used.

- **AD-7 — [ADOPTED]** Workers cannot mutate durable project semantics directly; workers execute only within frozen bootstrap and native runtime; worker-local plans/tool calls/raw outcomes stay local or external; meaningful outcomes return through Weaving; independent verification crosses genuine cognitive-responsibility boundary.

- **AD-8 — [ADOPTED]** Frontier and specialized views are derived, never authoritative; derived from current relations plus satisfied/unknown/blocking boundaries; UI views/specialized graph/text/semantic indexes are rebuildable projections cannot become competing semantic authorities.

- **AD-9 — [ADOPTED]** Compatibility providers never define Battle Map ontology; external systems retain authority over their raw facts but Project Shape remains Battle-Map-native; provider-specific concepts may appear only inside adapters and compatibility mappings.

- **AD-10 — [ADOPTED]** One candidate contract and one canonical mutation port; every semantic-candidate producer emits the same Battle-Map-native Project Shape Candidate Delta contract; Owning authority returns decision against that contract; only Semantic Mutation Port may commit adopted Project Shape.

- **User-facing identity constraint:** Battle Map vocabulary fully understandable without prerequisite knowledge of BMAD (Mary/John/Winston/Amelia personas, skill name prefixes, phase-gate terminology, method-specific vocabulary).

- **Technology neutrality constraint:** Do not select physical database/graph engine/ORM/UI framework/model supplier/deployment topology/sync algorithm; choose after observing real data shape/access patterns/deployment constraints.

- **No numeric thresholds constraint:** Success metrics qualitative (owner clarity, reduced premature commitment, smooth brownfield transition) rather than quantitative ratios; do not reduce autonomy to ratio metrics.

- **Brownfield optional pattern constraint:** Spec-folder story organization/git worktree isolation/recovery-flow patterns available as compatibility shims but NOT native defaults; native ontology primary.

## Non-goals

- **Not a task list or role-based work queue:** Battle Map presents capability-complete structure (goals → functions → regions → milestones → relations → frontier), not execution units or assigned work items.

- **Not requiring BMAD knowledge:** User does not need to know Mary/John/Winston/Amelia persona names, `bmad-*` skill prefixes, four-phase labels (Analysis/Planning/Solutioning/Build), or Standard BMAD internals to understand or use the system.

- **Not a forensic evidence archive:** Battle Map does not preserve raw Git/Test/Review/Harness streams, diffs, full logs, review threads, complete rejected-candidate histories, or forensic record of every source event.

- **Not a static architecture diagram:** Battle Map continuously reflects real validation,推进状态，and structural revision; it is not design-aspiration frozen at one point.

- **Not a log browser:** Battle Map may provide on-demand source context access but does not堆砌原始记录 in main view; raw facts remain in external sources.

- **Not monolithic operation界面:** Battle Map's core职责是保持项目结构可见、推进关系可理解、完成状态有证据、结构变化可解释; it does not require所有项目操作都在一个界面完成.

- **Not predetermined technology choices:** Physical semantic-store carrier, deployment topology, sync algorithm, authority-policy representation, projection technology deferred until real collaboration/deployment requirement observed.

## Success signal

**Owners report clearer understanding of project shape and current frontier; reduction in premature commitment or discover-late structural errors; smooth brownfield transition without losing mature mechanisms; routine advancements completed autonomously within authority boundaries while directional/high-cost decisions correctly escalated; integration defects caught progressively at join points rather than accumulating; Narrative explains structural changes causally, not just chronologically; Battle Map vocabulary fully understandable without prerequisite knowledge.**

Additionally: **Humans and AI can collaborate around same structural map with current adopted shape/evidence support/uncertainty status/needed revisions; next-step decision cites evidence supporting progression with recorded justification.**

## Assumptions

- **Assumed:** Battle Map absorbs durable mechanisms from Standard BMAD (persona patterns, workflow protocols, durable handoffs, authority boundaries, independent review model, deterministic control-plane discipline, source-of-truth discipline, brownfield entry patterns) but digests them into native components without exposing BMAD terminology; users get same quality guarantees without needing BMAD knowledge.

- **Assumed:** Brownfield compatibility mechanisms (spec-folder story organization, optional git worktree isolation, recovery-flow patterns, zero-token E2E testing guarantees) are available as compatibility shim but NOT native defaults; battle-map-native ontology primary in documentation/UI; existing BMAD artifacts readable via export function.

- **Assumed:** Stage-1 validation observes five cross-cutting properties (persistent structure cognition, explicit structural error classification, composite verification, unknown/evidence boundary marking, justifiable investment judgment) realized as system behaviors not discrete modules; null hypothesis discipline applied—preserve mature mechanisms unless observed friction proves change worthwhile.

- **Assumed:** Adoption/candidate evolution is autonomous boundary where structural candidates accumulate sufficient weight; not all candidate changes require Owner authority—routine shape updates handled by Coordinator within policy bounds; truly irreversible/high-cost/significant-meaning ones escalate.

## Open Questions

<!-- No open questions from input richness; all five-field kernel fields fully specified in PRD and Architecture Spine. -->
