# Research Report: BMAD Product Delta Analysis

## Executive Summary

This analysis examines the delta between **Standard BMAD 6.11.0** (an interactive software delivery method), **BMAD Loop** (a deterministic orchestrator for unattended development loops), and the **Battle Map target intent** (a project cognition interface for maintaining project shape over long-term development). The key finding is that both existing systems address different orthogonal axes of the problem space, with Battle Map proposing capabilities that would constitute a new product layer rather than an extension of either existing system.

---

## 1. Existing BMAD Capabilities (Standard BMAD v6)

### 1.1 What Behavior Is Already Sufficient

**Interactive phased delivery workflow** - Already complete in Standard BMAD, no change needed.

From `bmad-method/docs/reference/workflow-map.md` (lines 22-97):

| Phase | Workflows | Output | Status |
|-------|-----------|--------|--------|
| Analysis (Optional) | `bmad-brainstorming`, `bmad-forge-idea`, `bmad-deep-recon`, `bmad-product-brief`, `bmad-prfaq` | Briefs, reports, validated concepts | ✅ Complete |
| Planning | `bmad-prd`, `bmad-ux`, `bmad-spec` | PRD, UX spine, SPEC.md contract | ✅ Complete |
| Solutioning | `bmad-architecture`, `bmad-create-epics-and-stories`, `bmad-sprint-planning` | Architecture decisions, epic/story breakdown, sprint readiness gate | ✅ Complete |
| Implementation | `bmad-build`, `bmad-build-auto`, `bmad-code-review`, `bmad-correct-course`, `bmad-retrospective` | Implemented code with review records | ✅ Complete |

**Named agent personas** - Already implemented via skill dispatch system.

From `bmad-method/docs/reference/agents.md`:

```
| Agent                       | Skill ID             | Primary Workflows                    |
|-----------------------------|----------------------|-------------------------------------|
| Analyst (Mary)              | bmad-agent-analyst   | Brief creation, market research     |
| Product Manager (John)      | bmad-agent-pm        | PRD creation, epic/story planning   |
| Architect (Winston)         | bmad-agent-architect | Architecture decisions              |
| Developer (Amelia)          | bmad-agent-dev       | Implementation, testing             |
| UX Designer (Sally)         | bmad-agent-ux-designer| UX design                           |
```

**SPEC.md canonical contract format** - Already mature.

From `bmad-method/docs/reference/workflow-map.md` (lines 59-61):
> `bmad-spec` produces the canonical machine contract: a five-field kernel (Why, Capabilities, Constraints, Non-goals, Success signal) plus companion files, validated so every load-bearing source claim is preserved.

**State persistence via durable artifacts** - Already established. Each workflow outputs Markdown files with frontmatter that become inputs to downstream workflows.

**Project Context mechanism** - Already exists via `bmad-project-context`.

From `bmad-method/docs/existing-codebases/set-and-maintain-project-context.md`:
> Run `bmad-project-context` — greenfield (seeded from your spec or architecture) or brownfield (discovered from the codebase, verified, then confirmed with you).

### 1.2 Key Design Decisions

**"Three intents in one skill"** - `bmad-prd` handles Create/Update/Validate modes. This reduces cognitive overhead while preserving flexibility.

**"Story Breakdown creates ordered stories.yaml"** - When invoked with a spec-backed epic, `bmad-spec` produces ordered story files under `{output_folder}/stories/<id>-*.md`. This supports multi-session implementation without sprint boards.

**"Spec-backed epic path vs direct build"** - From `bmad-method/docs/reference/workflow-map.md` (lines 98-103):
> Clear one-session work can enter `bmad-build` directly. A spec-backed epic uses Story Breakdown to create several units under one `SPEC.md`.

---

## 2. BMAD Loop Capabilities (Control Plane)

### 2.1 What's Already Working

**Deterministic control loop** - Core innovation: orchestration runs in pure Python with NO LLM calls.

From `bmad-loop/src/bmad_loop/engine.py` (module docstring lines 0-6):
> The deterministic control loop. Per story: dev session -> artifact verification -> bounded review loop -> deterministic verify commands -> orchestrator commit. The engine never edits sprint-status.yaml or spec files; it re-reads them to decide and verify. All creative work happens inside disposable adapter sessions.

**Dual execution modes**:
1. **Sprint mode** - Uses `sprint-status.yaml` as single source of truth (default)
2. **Stories mode** - Uses typed `stories.yaml` dispatched by folder+id (opt-in)

From `bmad-loop/docs/FEATURES.md` (lines 14, 26-37):
> Same loop from either `sprint-status.yaml` (sprint mode, default) or a typed `stories.yaml` dispatched by folder+id (stories mode, opt-in)
> Automated per-story pipeline: `dev → verify → review → verify → commit`, end-to-end, no human in the loop.
> Deterministic control flow in plain Python — story selection, retry budgets, gate checks, and completion checks are code, not an LLM session.

**Trust-nothing verification system** - Before any commit, orchestrator independently validates:
- On-disk artifacts match what session claims
- SPEC.md baseline validity
- Test/lint command success (policy-gated)
- Sprint board state sync

From `bmad-loop/docs/FEATURES.md` (lines 48-55):
> Trust-nothing verification
> Checks on-disk artifacts (spec status, canonical baseline validity, proof after the accepted baseline, sprint sync) + runs your test/lint commands before commit
> Agents claim success without working code; broken builds slip through

**Fresh-context adversarial review** - Dev and review run in separate sessions. Review uses 4 parallel layers:
1. Blind Hunter
2. Edge Case Hunter  
3. Verification Gap
4. Intent Alignment

From `bmad-loop/docs/FEATURES.md` (line 17):
> Fresh-context adversarial review
> Dev and review are separate sessions; review uses 4 parallel layers (Blind Hunter / Edge Case Hunter / Verification Gap / Intent Alignment)
> Self-review anchoring bias; implementer marks own work correct

**Resumable state machine** - Every run maintains on-disk state in `state.json`, resumable after:
- Human gate intervention
- Escalation pauses
- Process crashes

From `bmad-loop/docs/FEATURES.md` (line 18):
> Resumable state machine
> Every run is on-disk state, resumable after gate/escalation/crash

**Hook-based transport** - Coding agents write structured event files via hooks (not terminal scraping). Skills write `result.json` completion markers.

**Worktree isolation** - Each story develops in isolated git worktree, merged via controlled merge strategies (squash/fast-forward/replay).

From `bmad-loop/docs/FEATURES.md` (lines 33-34):
> Worktree isolation
> Each story develops in its own git worktree; merges use squash or fast-forward strategies; replays fix conflicts deterministically
> Flaky merges block progress instead of hiding issues

### 2.2 Control Flow States (Statemachine.py)

From `bmad-loop/src/bmad_loop/statemachine.py` (lines 12-48):

```python
TRANSITIONS = {
    Phase.PENDING: {DEV_RUNNING, TRIAGE_RUNNING},
    Phase.DEV_RUNNING: {DEV_VERIFY},
    Phase.DEV_VERIFY: {DEV_RUNNING, REVIEW_RUNNING, COMMITTING, DEFERRED, ESCALATED},
    Phase.REVIEW_RUNNING: {REVIEW_VERIFY},
    Phase.REVIEW_VERIFY: {REVIEW_RUNNING, DEV_RUNNING, COMMITTING, DEFERRED, ESCALATED},
    Phase.COMMITTING: {DONE, ESCALATED, AWAITING_OPERATOR},
    Phase.TRIAGE_RUNNING: {TRIAGE_VERIFY},
    Phase.TRIAGE_VERIFY: {TRIAGE_RUNNING, DONE, ESCALATED},
    Phase.DONE: {},  # terminal
    Phase.DEFERRED: {},  # terminal  
    Phase.ESCALATED: {},  # terminal
    Phase.AWAITING_OPERATOR: {},  # terminal
}
```

**Key insight**: The phase machine is **non-regressive**. Once DONE/DEFERRED/ESCALATED, never returns to active states.

### 2.3 Sweep Engine (Deferred Work Triage)

From `bmad-loop/docs/FEATURES.md` (lines 176-182):
> Deferred work sweep
> `bmad-loop sweep --deferred` reads the ledger's `deferred:` list from all specs in the repo, builds bundles of related items, triages each bundle in a fresh session, and commits valid changes or escalates ambiguous ones. Repeat mode (`--repeat`) absorbs newly generated deferred work across cycles.

**Triaging workflow**: Bundle collection → Fresh session triage → Verifies → Commits or Escalates

---

## 3. Target Semantics from BATTLE-MAP

### 3.1 What Are The Actual Goals (Intent, Not Spec)

Reading `BATTLE-MAP.md` carefully (section headers and key passages only):

#### 3.1.1 Core Purpose (Section 1, lines 3-14)

> 战役地图方法首先解决的，不是"怎样把项目拆成更小的任务"，而是"怎样在长期开发过程中始终保住项目最终成品的完整形状"。

**Translation/Core Problem**: "The Campaign Map method first solves not 'how to break projects into smaller tasks' but 'how to preserve the complete shape of the final deliverable throughout long-term development'."

The real issue: when projects enter fine-grained execution too early, they dissolve into "locally correct tasks" where each task is implementable/testable/closable, but together they fail to answer: what is the final product made of? how do capabilities connect? what position has the product reached overall?

**Core Objective** (lines 11-14):
> **始终从完整项目看局部施工；用现实持续校准结构，让下一笔投入沿当前最可信、证据边界明确的结构前进。**
> 
> Always view local construction from the perspective of the complete project; continuously calibrate structure with reality, allowing the next investment to advance along the most credible current structure with clear evidence boundaries.

#### 3.1.2 What It's NOT (Section 2, lines 15-31)

> 战役地图首先是一张"项目形状图",其次才是一张"项目推进图"。
> 
> The campaign map is first a "project shape diagram," secondly a "project progression diagram."

**Not a task list.** If a "map" lists many tasks with numbers and statuses but cannot help someone imagine what the finished product looks like, it has failed its core responsibility.

**Visual metaphors are optional**: "战役" (campaign) is merely a visual metaphor for understanding structure, paths, checkpoints, fronts, and progression relationships. Actual project semantics should prioritize natural, accurate functional language, not force technical concepts into war terminology.

#### 3.1.3 Core Objects (Section 3)

**3.1 Project Goal** (lines 35-38):
Describes the ultimate result hoped for in reality. Not a task collection, not an implementation plan, but the reason the entire map exists.

**3.2 Complete Functions** (lines 39-44):
Complete functions are independent capabilities describable by their input, core behavior, output, and contribution to the final system. Function division prioritizes "is function complete" not "can one executor finish it at once." A complete function can later be split into execution units, but initial structure shouldn't degrade into fragmented tasks for convenience.

**3.3 Milestones** (lines 45-50):
Milestones are observable evidence when a complete function or set reaches a meaningful state. Answer "how to know this capability truly exists," describing real observable results, not just files/fields/commits/task-number completion.

**3.4 Structure Relationships** (lines 51-56):
Complete functions must express at minimum: serial, parallel, dependency, convergence. These aren't for drawing convenience but determine real project progression order. Map allows modifying these relationships as real implementation exposes new facts.

**3.5 Initial Checkpoint Map** (lines 57-62):
Initial checkpoint map is a project structure hypothesis based on current understanding. Should cover complete functions, milestones, and major structural relationships for project goals, but isn't final truth. Provides structure starting point for risk probes, real implementation, and formal construction—verifiable, refutable, modifiable.

**3.6 Minimum Complete Experiment** (lines 63-76):
Principle: **"Only reduce scale irrelevant to current structural risks, not the semantics being probed."**

Can have less data sources, fewer interfaces, less performance optimization, fewer edge cases—but deleted conditions cannot be key variables for structural judgment. Must have real input, real core behavior, real output, able to join actual links. Not Mock, not placeholders, not "theoretically works in future" interface shells.

**Not a single-purpose prototype**, but a high-leverage engineering asset providing three values simultaneously:
1. **High-confidence early validation**: Kill wrong boundaries, dependencies, assumptions, serial/parallel judgments early with real behavior
2. **Attackable review entity**: Architecture review, red-team validation, failure experiments face something genuinely runnable, not just "will work in future" description
3. **Emergent capability minimal assembly**: Multiple semantic-complete small capabilities truly connected expose shared state, feedback loops, hidden coupling, new upper-level capabilities not anticipated in original design

Therefore it validates existing judgments AND actively generates new structural information. It's high-leverage probes selected by risk, not requiring every complete function in map to have minimum version first.

**3.7 Minimum Complete Chain** (lines 77-87):
Single minimum complete implementation passing doesn't automatically prove project structure correct. Multiple minimum complete implementations must also connect according to map relationships, letting real input reach observable project goal results.

Focuses on two evidence levels:
1. Whether individual nodes express expected complete behavior under explicit conditions
2. Whether node combinations' links genuinely work under explicit conditions

Both evidence levels must carry coverage scope. Link success increases structural confidence only within its actual covered conditions, not auto-promoting to "whole project structure certified." Uncovered scales, time, failure, ecology, and organization conditions remain explicit unknowns preserved on map.

**3.8 Formal Checkpoint Map** (lines 88-93):
Formal checkpoint map doesn't arise from completion of planning documentation, but when initial map passes minimum complete experiment and real chain calibration, pressing enough key uncertainties to acceptable cost for next-tier investment.

"Formal" is an **investment confidence gate**, not structural truth certification. Indicates current structure hypothesis, covered risks, remaining unknowns, and continuing investment have reached state worthy of bearing subsequent large-scale construction costs. New real evidence still demands re-judgment of structure.

**3.9 Formal Implementation and Minimum Baseline** (lines 94-99):
Formal implementation is complete construction result面向最终 quality, performance, experience, reliability, and engineering requirements.

Validated minimum complete implementation can serve as formal implementation checker and对照物 (reference object), but doesn't default to permanent maintenance. Only retained if continuing to provide independent diagnostic value, contract baseline, or low-cost reproduction capability; otherwise frozen as historical evidence or evolved/adapted by formal implementation directly replacing.

#### 3.1.4 Complete Process (Section 4)

The twelve phases (lines 102-167):

1. **Establish Project Goals** - Describe clearly ultimate desired result in reality. Not rushing to break implementation tasks, not deciding technical structure yet.
2. **Identify Complete Functions** - From project goals reverse-push: what complete capabilities must system possess for ultimate result to hold. Prioritizing protecting complete function shape, avoiding premature fragmentation by construction granularity.
3. **Define Milestones** - For complete functions define observable completion evidence making "function completion" verifiable, not relying on executor self-reporting.
4. **Establish Structure Relationships** - Analyze serial, parallel, dependency, convergence relationships among complete functions, forming first version structure diagram.
5. **Form Initial Checkpoint Map** - Organize project goals, complete functions, milestones, relationships into readable, actionable, modifiable initial map. Map is structure hypothesis, not final design.
6. **Select High-Value Structural Risks and Make Real Probes** - Based on current structure hypothesis, remaining unknowns, error costs, select most worthy uncertainties to reduce cheaply. Create minimum complete implementations where low-cost verification possible; if conditions determining structure only appear at formal scale, directly use formal-grade environments, failure experiments, or local formal implementations as probes. Goal: obtain discriminative real evidence at current most cost-effective way, not mechanically giving every function a minimum version.
7. **Connect Real Chains and Label Evidence Coverage** - Connect suitable real probes, minimum implementations, or partial formal implementations actually combining, verifying whether real input can reach corresponding results along map. Simultaneously record which conditions this chain actually covers, which structural hypotheses excluded, which critical unknowns not touched.
8. **Revise Map Using Implementation Feedback** - Problems exposed during real implementation must distinguish: implementation problems themselves OR structure judgment problems. If problem is just code errors, test failures, boundary condition omissions, implement fixes; if problem indicates function boundaries, dependency relationships, serial/parallel relationships, convergence points, milestones, or function sets themselves don't hold, return to structure layer modifying initial map. Structural failure isn't "adding patches to current task" solved, but project gaining new facts about its own shape.
9. **Form Formal Checkpoint Map** - When an area or investment decision has pressed enough key uncertainties through real evidence, and continuing exploration marginal benefit falls below value entering next-tier investment, that area can enter formalization. Different areas can be at different maturity levels, not requiring whole project map to cross artificial global stage door simultaneously.
10. **Formal Construction** - Formal construction can roll-start in areas reaching investment-confidence-door without waiting for entire project structure to be certifiably complete one-time. Formal checkpoints can continue splitting into finer executable work units, using development, validation, review, recovery mechanisms suitable for stable progress. Formal implementation itself remains new real evidence source: if it exposes function boundaries, dependencies, milestones not holding, map must continue revising. Fine-grained construction serves current most credible complete function structure, but won't therefore let structure hypothesis lose revocability.
11. **Gradually Replace and Continuously Validate** - When an area has minimum chains still providing diagnostic value, formal implementation doesn't need to replace entire chain at once. Can gradually put formal implementations back into real chain:
    ```
    Formal A → Minimum B → Minimum C → …
    Then gradually becomes:
    Formal A → Formal B → Minimum C → …
    ```
    Each replacement continues validating whole chain, locating problems to just-replaced parts, not waiting until all formal implementations complete for first acceptance. If certain minimum chains no longer provide independent information, don't maintain them for ritual completeness.
12. **Overall Completion** - When all formal functions enter real chain, and complete system can continuously satisfy project goals, project truly completes. Completion evidence comes from real behavior, validation, and whole-chain results, not just task statuses all closed.

#### 3.1.5 Two Core Closed Loops (Section 5)

**5.1 Structure Discovery Loop** (lines 172-179):
```
Goals → Complete Functions → Milestones → Initial Map → Risk Selection → Real Probes / Formal-Grade Evidence → Structure Feedback / Capability Emergence → Revise Map → Investment Confidence Update
```

Answer: **At current cost, how far have we been able to recognize the project's real function shape?**

Allows any real implementation to reverse-modify planning because minimum experiments, failure probes, and formal implementations can all bear "measuring structure" responsibilities, possibly exposing new relationships and capabilities. This loop has no globally-closed moment for whole project; works continuously by area until relevant decision's remaining uncertainty is no longer worthy of stopping next-tier investment.

**5.2 Formal Construction Loop** (lines 180-187):
```
Areas reaching investment-confidence-door → Construction breakdown → Implementation → Independent validation/review → Real chain/system validation → New structure evidence → Continue construction or revise map
```

Answer: **How reliably can structurally-worthy areas currently be built into final products while continuously absorbing new evidence from construction?**

Two loops have different cognitive purposes but aren't mutually exclusive temporal stages. Structure discovery prioritizes reducing key uncertainties; formal construction prioritizes stable delivery; both can occur simultaneously in different areas. Map clarifies which structure judgments have what evidence ranges, which remain unknowns, what new evidence suffices to trigger redrawing, preventing one side from falsely treating local success as overall certification while another lets structure drift unlimitedly.

#### 3.1.6 What Map Must Express (Section 6)

**6.1 Product Structure** (lines 190-193): Users see what complete functions compose final product and why their combination achieves project goals.

**6.2 Progression Structure** (lines 194-197): Users see which nodes currently actionable, which blocked by precedence, which parallel, which converge, where current frontline located.

**6.3 Completion Evidence** (lines 198-201): Node/path states backed by traceable evidence like real operation, tests, run results, reviews, or whole-chain behavior, not just executor self-reporting "complete." Must distinguish external facts, system inference, pending judgment, currently adopted structure, showing evidence coverage scope, failure conditions, remaining unknowns. Prevents local chain success from rendering as overall structure certified.

**6.4 Structure Evolution** (lines 202-207): When map changes due to real implementation, need to understand: why originally divided this way, what facts exposed, why new structure more credible. Evolution recording keeps project cognition causal continuity, preventing unintelligible structural jumps during long-term progression.

#### 3.1.7 Core Principles (Section 7)

Seven principles including: complete functions prioritize over construction granularity; milestones must be observable; minimum doesn't equal incomplete; design is structure hypothesis, reality is calibration source; structural failure repairs structure first; local correctness replaces neither overall holding; formal implementation gradually replaces verified chains; map serves understanding not term manufacturing.

#### 3.1.8 Implementation Errors vs Structural Errors (Section 8)

**Implementation errors** mean structure judgment holds, just certain implementation didn't correctly satisfy it. Examples: algorithm errors, boundary condition omissions, interface implementation errors, test failures.

**Structural errors** mean reality negated some map hypothesis. Examples:
- Originally thought two functions independent, actually always must change together
- Originally thought two paths parallel, actually exist hidden strong dependencies
- Originally thought A could directly connect C, actually must have complete B
- Originally defined milestone can't prove function truly exists
- Certain socalled complete functions actually contain two different capabilities, or two nodes actually belong to same inseparable capability

Facing structural errors, correct action isn't forcing reality adapting to original plan, but modifying map, letting subsequent construction rebuild on more credible project structure.

#### 3.1.9 Campaign Map as Software Capability (Section 9)

Campaign map isn't just project promotion method, but independently established software capability. It organizes information originally scattered across requirement documents, design docs, task lists, code commits, test results, running states, and discussion records into a visual structure centered on "complete functions and their relationships," enabling project participants to directly observe project overall, current frontline, and real completion evidence.

From product perspective, campaign map isn't another skin on traditional task kanban. Task kanbans mainly answer "what work, who doing, what step"; campaign maps first answer "what does this project ultimately consist of, why do these parts connect this way, what capabilities currently truly exist, which routes have push conditions."

Also isn't simple architecture diagram. Architecture diagrams mainly describe system design; campaign maps simultaneously describe design structure, reality validation state, progression status, and structure changes, therefore becoming a project cognition interface continuously changing with project real progress.

#### 3.1.10 Own Established Product Value (Section 10)

Ten product values summarized into six key ones:
1. **Keep project overall visibility** - Long-term projects easiest losing overall shape. Campaign map continuously puts complete functions, relationships, and final goals in same view, keeping local construction not submerging project overall.
2. **Make "completion" become understandable capability change** - Traditional progress uses task percentage, closed quantities, or commit quantities, but these numbers hard explaining what product now truly gained. Campaign map expresses progress as "which complete functions and paths have real evidence holding."
3. **Expose real dependencies and blocking** - By explicitly displaying serial, parallel, dependency, convergence relationships, campaign map presents directly "why can't do this step now," "why can these two paths progress in parallel," "why hasn't this convergence point opened."
4. **Lower project re-understanding cost** - Project participants don't need traversing大量 tasks, commits, and historic discussions to recover project overview. Map provides cognitive entry from overall to local, drilling down to specific nodes/evidence as needed.
5. **Support human-AI sharing same project view** - Humans and AI can discuss around same structure chart: what project shape currently adopted, which judgments supported by what evidence ranges, where still uncertainty, which structures need modification. Map therefore becoming public cognition surface in complex long-term collaboration.
6. **Make structure changes interpretable** - When project structure changes due to real implementation, map shows not just "now what," but connects to evidence and decisions triggering "why change happened," keeping project long-term evolution causally continuous.

#### 3.1.11 Core Product Capabilities (Section 11)

Ten product capabilities:
1. **Project global view** - With project goals as top layer, show complete functions, milestones, structure relationships, enabling users to first understand overall then enter local. Global view focuses on project "shape," not stacking all bottom-layer tasks. Detail drills down layer-by-layer as needed.
2. **Checkpoint and function node display** - Each node should express meaningful complete capability, solving what problem, depending on what, outputting what, current status, what evidence supports this status. Node names prioritize business or capability language, letting users understand what product will ultimately possess just viewing map.
3. **Relationship and path display** - Map should visualize serial, parallel, dependency, convergence relationships directly, letting users understand why certain path passable, why blocked, when unlockable. Relationships aren't decorative lines but part of project progression logic.
4. **Frontline and actionable location display** - Campaign map should clearly present project "frontline": which nodes completed, which progressing, which尚未满足 predecessor conditions, which already having push conditions. Making map not only explain project, but directly support next-step action judgment.
5. **Milestone and completion evidence** - Completion status in map should connect to observable milestones and real evidence. Users should continue viewing from certain "completed" node: what behavior, tests, run results, reviews, or whole-chain evidence supporting this judgment.
6. **Minimum and formal implementation co-display** - Same complete function can simultaneously associate minimum complete implementation, risk probes, and formal implementation different evidence carriers. Map should distinguish coverage conditions each carries, express when replacement relationship exists whether formal implementation already replaced minimum entering real chain. Making users see project growing from different intensity real evidence gradually, not presetting every function must first go through same minimum chain stage.
7. **Structure revision** - When real implementation exposes structural errors, map should support modifying node boundaries, dependencies, serial/parallel relationships, convergence points, milestones, retaining cause-effect relations before/after changes. Structure revision is normal capability of campaign map, shouldn't be treated as exception operation after planning failure.
8. **Evidence drill-down** - Map itself keeps high-layer readability, but each key status should allow continuing drilling down to more concrete basis, such as relevant implementation, tests, run records, review conclusions, or decision records. Avoiding piling all detail volumes on map, yet avoiding map becoming abstract layer without basis.
9. **Historical change viewing** - Users should view important changes happening at different time points for certain node or relationship, and what real events or judgments triggered these changes. Historical capability focus isn't saving all operation details, but retaining structure changes changing project understanding.
10. **Multi-level expansion** - Campaign map needs supporting from overall project progressively entering local: from project goals to function areas, from function areas to checkpoints, from checkpoints to concrete construction and evidence. Different layers承担 different cognitive density, avoiding compressing complete project and bottom-layer construction details onto same plane.

#### 3.1.12 Real Usage Workflow (Section 12)

Eight typical interactions: entering project seeing overall map not bottom task list; browsing project structure viewing why certain function exists, depending on which nodes, affecting which successors, position in entire product; viewing current frontline map highlighting currently progressing or already having push condition positions; drilling into node viewing complete function explanation, milestones, predecessors, current status, minimum implementation, formal implementation, construction status, verification evidence, blocking reasons, important structure changes; viewing evidence from node status continuing to verify support status real evidence; handling structure changes seeing change proposals and impacts: which nodes splitting/merging/moving/reconnecting, which milestones changing, which existing paths failing/opening; observing formal replacement user seeing which nodes still by minimum complete implementation/risk probes providing baseline, which already by formal implementation undertaking, whether new real chain or system validation passed; judging overall completion map showing complete functions all entered formal state, key paths and convergence points all have real evidence holding, overall goals validated through whole-chain results.

#### 3.1.13 Interaction Methods with Humans (Section 13)

Main human value isn't requiring users maintaining internal state, but letting humans低成本 understand, audit, and intervene projects. Typical human-map interactions include: viewing overall project shape; selecting nodes viewing capabilities, relationships, evidence; viewing current actionable paths and blocking reasons; auditing whether milestones truly hold; confirming/rejecting/correcting structure modifications; viewing reasons and impacts of certain structure changes; selecting priorities among multiple actionable directions; entering deeper construction/validation/evidence details from map.

#### 3.1.14 Information Presentation Layers (Section 14)

Need adopting progressive disclosure, not piling all information at once. Outermost layer prioritizes showing: project goals, main complete functions, key milestones, main paths, current frontline, overall completion status. Into function areas further showing: area checkpoints, dependency relationships, parallel routes, convergence points, current blocking, structure changes. Into single checkpoint further showing: function definition, completion conditions, minimum implementation, formal implementation, current construction status, verification evidence. Only downward into specific tasks, code, tests, logs, review records, and original evidence.

This layer relationship keeps map keeping "overall readable" yet能成为进入真实工程细节 navigation entry.

#### 3.1.15 Roles in Human-AI Collaboration (Section 15)

Campaign map serves both humans and automation executors, but focus differs. Humans primarily understand project overall, audit structure and milestones, judge priorities, handle major structure changes, deeply check evidence as needed. Automation executors可以利用 map structure relationships, current status, actionable locations, completion conditions understanding their project position, feeding back new implementation results, validation results, and structural problems. Therefore map既是面向人的认知界面，也是不同参与者共享项目结构和推进状态的公共表示.

#### 3.1.16 Product Boundaries (Section 16)

Campaign map not simple task manager. Can associate tasks, but core objects are complete functions, structure relationships, milestones, and real completion states. Not static architecture diagram. Not only describes design but continuously reflects reality validation, progression status, and structure revisions. Not log browser. Can drill into history and evidence, but won't pile all original records directly into main view. Not aiming to stuff all project operations into one interface. Core responsibility is keeping project structure visible, progression relationships understandable, completion states evidenced, structure changes interpretable, providing clear entries for further engineering operations.

#### 3.1.17 Product Overall Definition (Section 17)

As software module, campaign map is **持续项目认知界面 that presents project structure, progression status, milestones, real evidence, and structure evolution unified around complete function structure core**.

Letting users observe current work starting from "what project ultimately becomes," not inferring project overview from discrete tasks backward; letting project states expressed by real capabilities and evidence, not by task quantities; letting structure changes be understood and audited, not quietly occurring during long-term progression.

As method, it continuously calibrates project structure through minimum complete implementation and minimum real chains; as product, turns this structure, evidence, and progression state into reality interface humans can continuously observe, operate, and audit.

---

### 3.2 Execution Contract Constraints

From `NEXT-GREENFIELD-BMAD-EXECUTION-CONTRACT.md`:

**Four Identity Fixtures** (Section 1, lines 5-14): Critical distinction that Battle Map is target reference/specification source, NOT currently available execution engine. Current Standard BMAD and BMAD Loop are BOTH research materials, not future final methods.

**Same-Role Context Continuity** (Section 2-3, lines 16-36): Same BMAD role in same continuous work segment defaults to reusing same long-term context/session. Forbidden to split same-role completion repeatedly into multiple one-shot agents re-understanding/regenerating/overwriting each other. Role continuity prioritized over "fresh context each step."

Fresh context only for cognitive independence boundaries, most typically independent reviews: reviewer doesn't inherit implementer's subjective reasoning but reads their disked specifications, implementations, tests, and evidence. Same-role continuous construction相反: should retain contextual causal chains, avoiding repeating understanding costs. In short: **within-role continuous, between-role isolated as needed; construction continuous, independent validation isolated.**

**Research and Construction Simultaneous, Conclusions Layered** (Section 4, lines 37-47): Each real BMAD/BMAD Loop progression simultaneously produces two types of results: project results (what did current greenfield project advance) and research results (which mechanisms proved valuable/exposed costs/failure in real advancement). Two types must be recorded separately. Cannot because certain BMAD mechanism currently available directly write it into future project map method design;也不能因为 Battle Map materials proposed certain ideal capability pretending current BMAD already possesses it. Future methods only absorb mechanisms proven valuable through本轮真实研究; Battle Map reference materials also can be revised by本轮 evidence.

**Next-Round Installation Position** (Section 8, lines 76-79): This file serves as frozen reference in current feasibility project. When creating true greenfield R&D warehouse, MUST copy this contract as project启动级 rules into Standard BMAD/BMAD Loop role startup context; merely staying in reference directory without entering运行上下文不算落实.

**Standard BMAD Complete Role Chain Sample Validity** (Section 12, lines 99-116): This round takes BMAD itself as research material, therefore formal planning and construction chain must保留 Standard BMAD role layer, cannot only call workflows under roles. For stages having corresponding formal roles, default call sequence: `activate corresponding bmad-agent-* → dispatch corresponding Workflow in same role session → role continuously bears that responsibility until phase ends`. Example: Analyst: first activate `bmad-agent-analyst` (Mary), then dispatch Product Brief / Research etc Analyst responsibilities in that session. Direct calling of workflow skills like `bmad-product-brief`, `bmad-prd` can serve as explicit simplified paths or control experiments,不得被视为 Standard BMAD完整行为样本，也不得在本轮正式链中替代角色激活.

**Context Lifecycle by Position Unit** (Section 13, lines 117-125): BMAD Help's "recommend fresh context each skill"不得机械理解成岗位内部每调用一个附属 Skill 就重开上下文。Agent activation documentation clearly states: role persona, persistent facts, and position identity persist valid in session; subsequently called position menu Skills dispatched by same role and continue carrying that persona. Therefore this project adopts complete behavior interpretation: **position switch establishes fresh context; same position internal, within same context continuously call that position responsibility related Skills until that position本轮 responsibility completed**. Example: Mary activated, can continuously execute Deep Recon, Product Brief, necessary Advanced Elicitation etc in same Analyst session; enter John/PM时才建立新的 PM context. Independent Review/Validation若方法要求认知独立性，可另开 fresh context;属于验证角色/职责边界，不改变岗位内部连续性.

**Formal BMAD Positions Must Reside in Interactive Qoder/tmux Session** (Section 14, lines 127-134): Formal BMAD runs以“岗位级持久交互会话”为 canonical execution surface: each position establishes tmux session, launches Qoder interactive CLI within; that position's Agent activation, menu selection, slash Skill, Workflow interaction, correction and recovery all complete continuously in same Qoder process/context, close upon completing that position responsibility, switching to next position. `qodercli -p/--resume` NOT formal BMAD main chain default execution surface. Actual measurement shows fresh `-p` can load Skills but Harness activation events write to stderr not entering stream-json mainstream; meanwhile trust gates, slash expansion, interactive status control surfaces不可直接 observed in non-interactive calls, and already appeared Deep Recon Skills activated but model only outputs startup sentences ending incomplete execution. Therefore before proving non-interactive actions equivalent, only use `-p` as probes, batch processing, or explicit auxiliary actions. Monitoring formal positions必须同时观察:tmux pane visible interactive status, Qoder session transcript, stderr/Harness activation, VIP socket/route and project artifacts. Must not judge "skill called" solely by JSONL mainstream.

**Qoder Formal Positions Use Harness-Native Agent Running Projection** (Section 15, lines 135-144): Executing formal BMAD positions on Qoder优先使用 Qoder native Session Agent (`--agent`) carrying position personality and high-priority operational constraints, rather than relying merely on context obedience after ordinary skill calls. BMAD's `bmad-agent-*` skills remain method layer authoritative assets; Qoder Agent is runtime projection compiled from that asset,不反向改写 Standard BMAD definition. This both retains BMAD's cross-Harness portability and utilizes Qoder native system-prompt layer improving position identity and activation protocol execution reliability. Position Agent calls original version Workflow Skills in same persistent tmux/Qoder session. If certain Workflow Skill carries local persona causing model temporarily switching to Workflow identity during that link, but task responsibility, input/output, control flow, and artifacts all correctly executed, current Standard BMAD experiment doesn't interrupt therefore; should record as original version composition semantic defect and continue progression. Formal blocking conditions: personality covering causes position responsibility loss, Workflow routing errors, necessary status/evidence loss, erroneous artifacts entering canonical downstream, or inability returning to position control flow. Pure nomenclature/local identity drift not blocking conditions. Future project map method再处理该缺陷：岗位身份作为持久层，Workflow 作为临时能力层，并由显式 activation state / workflow return state保证组合与恢复.

---

## 4. Delta Matrix: BMAD Loop & Standard BMAD → Battle Map

### 4.1 Structural Representation Capability

| Target Capability | Current Status | Delta Type | Required Change |
|-------------------|----------------|------------|-----------------|
| **Project shape visualization** - Users see complete functions, relationships, final goals in single view | ❌ **NOT EXISTS** | Needs new mechanism | Neither Standard BMAD nor BMAD Loop produce visual structure diagrams. Both output text-based specs (PRD, SPEC.md, sprint-status.yaml) without graph-based visualization. Battle Map requires visualization layer that understands functional topology. |
| **Function hierarchy** - Complete functions as primary organizational unit | ⚠️ **PARTIAL** | Needs extension | Standard BMAD produces epics/stories hierarchies (`bmad-create-epics-and-stories`), but not as "complete function shapes." Stories are implementation units, not capability descriptions. Requires semantic shift: epics→functions, stories→sub-implementations. |
| **Relationship expressions** - Serial, parallel, dependency, convergence between functions | ❌ **NOT EXISTS** | Needs new mechanism | No explicit relationship modeling in either system. Dependencies exist implicitly (prerequisites) but aren't visually modeled or enforced as progression logic. Requires graph schema + relationship DSL. |
| **Frontline identification** - Which nodes completed, progressing, blocked, ready | ⚠️ **PARTIAL** | Needs integration | BMAD Loop tracks phases (`pending`, `dev-running`, `done`, etc.) in `sprint-status.yaml` and `state.json`. However, "frontline" concept meaning "current actionable frontier in complex dependency graph" doesn't exist. Requires aggregate computation over dependency graph + phase states. |

### 4.2 Evidence Management

| Target Capability | Current Status | Delta Type | Required Change |
|-------------------|----------------|------------|-----------------|
| **Observable milestones** - Completion tied to measurable capability changes | ⚠️ **PARTIAL** | Needs extension | BMAD Loop verifies code works (test suites, lint gates), but milestones described as "files completed" not "system behaviors changed." Requires milestone-as-behavior specification format. |
| **Evidence drill-down** - Each status linkable to underlying evidence (tests, runs, reviews) | ⚠️ **PARTIAL** | Needs extension | BMAD Loop stores verification logs, test outputs, review transcripts in journal. But no structured linkage from status→evidence. Requires evidence indexing + hyperlink graph. |
| **Coverage scope labeling** - Show which conditions tested/not tested for each node | ❌ **NOT EXISTS** | Needs new mechanism | BMAD Loop verifies test success/failure but doesn't annotate "coverage boundary." Battle Map requires explicit marking of uncovered scales/time/failure/ecology/organization conditions. |
| **Minimum vs formal implementation distinction** - Co-existence with replacement tracking | ❌ **NOT EXISTS** | Needs new mechanism | Neither system models "minimum complete implementation" as distinct from formal. BMAD Loop implements one path only. Requires dual-track implementation + substitution registry. |

### 4.3 Structural Revision Support

| Target Capability | Current Status | Delta Type | Required Change |
|-------------------|----------------|------------|-----------------|
| **Structure vs implementation error distinction** - Separate code bugs from structural hypothesis failures | ❌ **NOT EXISTS** | Needs new mechanism | BMAD Loop treats all failures as "retry budget exhaustion" or "escalation." Doesn't classify error type. Requires error taxonomy + classification UI. |
| **Map revision capability** - Modify node boundaries, dependencies, relationships with causal history | ❌ **NOT EXISTS** | Needs new mechanism | Neither system supports mid-run structural modifications. Sprint boards lock structure until epic completion. Requires structural edit workflow + diff/auditing. |
| **Evolution recording** - Record why map changed, what facts exposed, why new structure more credible | ❌ **NOT EXISTS** | Needs new mechanism | BMAD Loop journals technical events (session start/stop, test results) but not structural decision rationale. Requires structural-change-specific journal schema. |
| **Investment confidence gates** - Formal checkpoint when uncertainty reduced to acceptable cost | ❌ **NOT EXISTS** | Needs new mechanism | BMAD Loop has "readiness gate" (`bmad-sprint-planning`) but it's binary PASS/FAIL, not investment threshold assessment. Requires cost-benefit analysis framework. |

### 4.4 Multi-Agent Coordination

| Target Capability | Current Status | Delta Type | Required Change |
|-------------------|----------------|------------|-----------------|
| **Shared project view for humans+AI** - Public cognition surface for heterogeneous participants | ⚠️ **PARTIAL** | Needs extension | BMAD Loop assumes all participants are automated adapters or operators. Battle Map explicitly designs for human+Aiconsensus scenarios requiring interpretable transitions. Requires human-readable structural summaries. |
| **Role continuity enforcement** - Same role stays in same session across multiple skills | ⚠️ **IMPLEMENTED IN EXECUTION CONTRACT** | N/A | Execution contract mandates this, but Standard BMAD tooling doesn't enforce. Requires harness-level session affinity. |
| **Independent review isolation** - Reviewers don't inherit implementer's subjective reasoning | ⚠️ **PARTIAL** | Needs extension | BMAD Loop's "fresh-context adversarial review" achieves technical isolation, but doesn't prevent review from consuming implementer's documented reasoning as "context." Requires document-level provenance tracking. |

### 4.5 Progressive Disclosure

| Target Capability | Current Status | Delta Type | Required Change |
|-------------------|----------------|------------|-----------------|
| **Multi-layer expansion** - From goals → functions → checkpoints → construction → evidence | ❌ **NOT EXISTS** | Needs new mechanism | Current systems flatten depth: PRD→SPEC→Stories→Code is linear, not navigational. Battle Map requires hierarchical navigation with cognitive-density gating. Requires layered document model + navigation API. |
| **Overall-local balance** - Don't stack all bottom-layer details on main view | ❌ **NOT EXISTS** | Needs new mechanism | No concept of "main view" in either system. Files are accessed by path, not by abstraction level. Requires index/view composition engine. |

---

## 5. Product Decision Gaps

### 5.1 Genuine Choices Requiring Decisions

#### Gap 1: Visualization Format Choice

**Decision**: How to represent campaign maps visually?

**Options**:
1. **Graph database backend** (Neo4j/Cypher queries) + web frontend
2. **Markdown-based graphviz/dot** files + static site generation
3. **Custom DOM-based visualization** embedded in documentation
4. **Pure text-based tree structures** (ASCII art, indented outlines)

**Evidence for consideration**:
- Standard BMAD favors Markdown-first (all artifacts are `.md`)
- BMAD Loop is backend-only (no UI layer)
- Battle Map emphasizes visual intuition ("项目形状图")
- Web bundles already exist for Standard BMAD planning tools

**Impact**: Choosing format determines storage layer, upgrade path, and interoperability with existing Markdown ecosystems.

#### Gap 2: Relationship Modeling Granularity

**Decision**: What relationship types to support?

**Options**:
1. **Minimal**: Just dependency (A→B means B requires A)
2. **Standard BMAD**: Predecessor-successor (sprint-style)
3. **Battle Map full set**: Serial, parallel, dependency, convergence, fork,汇合 (join)
4. **Extensible DSL**: Allow custom relationship schemas per-project

**Evidence for consideration**:
- `bmad-sprint-planning` only models linear preconditions
- Battle Map Section 3.4 specifically calls for four relationship types
- Graph theory suggests more relationships increase cognitive complexity exponentially

**Impact**: Determines data model complexity and whether "false parallelism" or "hidden dependencies" get discovered late.

#### Gap 3: Minimum Implementation Strategy

**Decision**: How to support minimum vs formal implementation coexistence?

**Options**:
1. **Separate branches**: Git feature branches for minimum, develop branch for formal
2. **Specification annotations**: Frontmatter flags marking nodes as `min-version: true`
3. **Parallel tracks**: Entire spec duplicated (`specs/min/` vs `specs/formal/`)
4. **Eliminate distinction**: Don't support minimum implementations; require formal from start

**Evidence for consideration**:
- Battle Map Section 3.6 defines minimum implementations as high-leverage engineering assets
- Section 3.9 says validated minimums "don't default to permanent maintenance"
- BMAD Loop already implements deterministic verification gates suitable for minimum validation

**Impact**: Determines whether minimum implementations become technical debt or persist as diagnostic infrastructure.

#### Gap 4: Structural Edit Authority

**Decision**: Who can modify project structure mid-flight?

**Options**:
1. **Human-only**: Only operator intervention can rewrite relationships
2. **Automated detection**: System auto-detected structural errors, human confirms
3. **Hybrid**: AI proposes structural edits, human approves/rejects
4. **Distributed consensus**: Multiple stakeholders vote on changes

**Evidence for consideration**:
- Execution contract Section 11 says "correct course" follows shortest path: don't require re-running workflows if answer already known
- Battle Map Section 8 distinguishes implementation errors (fix code) from structural errors (fix map)
- BMAD Loop's `bmad-correct-course` handles mid-sprint changes but only within fixed epic boundaries

**Impact**: Determines whether structural changes are rare重大事件 or routine iteration.

#### Gap 5: Investment Confidence Thresholds

**Decision**: What metrics determine "ready for formal implementation"?

**Options**:
1. **Quantitative**: X% test coverage, Y number of successful runs, Z reviewer approvals
2. **Qualitative**: Human signoff based on holistic assessment
3. **Hybrid**: Quantitative gates + qualitative override
4. **Per-area variation**: Each function area defines own thresholds

**Evidence for consideration**:
- Battle Map Section 3.8 says formal checkpoint map arises when "key uncertainties pressed to acceptable cost"
- Section 5.1 notes structure discovery loop has "no globally-closed moment"
- BMAD Loop's readiness gate is binary PASS/FAIL (from `bmad-sprint-planning`)

**Impact**: Determines whether formalization is milestone-driven or organic growth.

### 5.2 Assumptions That May Be Wrong

#### Assumption 1: BMAD Loop Can Handle Structural Complexity

**Claim**: BMAD Loop's deterministic engine can manage battle-map-style dependency graphs beyond linear sprint boards.

**Risk**: Engine's state machine assumes near-linear progression. Adding N-way relationships may require rewriting `statemachine.py` transitions entirely.

**Verification needed**: Can transition table scale from ~10 states to O(N²) relationship states without combinatorial explosion?

#### Assumption 2: Standard BMAD Artifacts Can Extend to Battle Map

**Claim**: PRD/SPEC.md formats can encode battle map metadata without breaking compatibility.

**Risk**: Backwards incompatibility—if battle map adds required fields that older BMAD versions ignore, toolchain breaks.

**Verification needed**: Can new frontmatter fields be marked "optional for v6, required for v7"?

#### Assumption 3: Visualizations Are Add-On Rather Than Core

**Claim**: Battle Map visualization layer can sit on top of existing headless systems without regressive changes.

**Risk**: Visualization may require new data models (graph DB, relationship edges) that feed backwards into BMAD Loop's state machine.

**Verification needed**: Does visual layer need read/write access to `state.json`, or just read-only projections?

---

## 6. Recommendations

### 6.1 Phased Approach

**Phase 1: Data Model Extension (v7.0)**
- Add relationship edges to STORY/EPIC data structures
- Extend SPEC.md frontmatter with milestone-as-behavior format
- Add structural-error tagging to BMAD Loop escalation reasons
- Output: Enhanced artifact formats, no UI changes

**Phase 2: Orchestration Updates (v7.1)**
- Modify `sprintstatus.py` to compute "frontline" from dependency graph
- Add "structural revision" workflow hook in BMAD Loop
- Implement minimum-formal track distinction in dev contract
- Output: Backend logic for battle map mechanics

**Phase 3: Visualization Layer (v7.2)**
- Choose visualization format (markdown-graphviz vs web app)
- Build navigator for progressive disclosure
- Create human-readable structural summaries
- Output: User-facing battle map interface

**Phase 4: Hybrid Mode (v8.0)**
- Enable battle-map mode alongside standard BMAD
- Provide migration guides from linear to graphical
- Document trade-offs and anti-patterns
- Output: Production-ready battle map system

### 6.2 Immediate Next Steps

1. **Validate relationship modeling requirements** - Survey actual battle-map users on required relationship types
2. **Prototype minimum-formal track** - Implement one example minimum implementation → formal replacement cycle
3. **Choose visualization format** - Run 2-week spike on graphviz vs web app approaches
4. **Define investment thresholds** - Gather stakeholder input on acceptable uncertainty levels

### 6.3 Out-of-Scope Clarifications

**NOT within delta scope** (existing capabilities already sufficient):
- Interactive planning workflows (`bmad-prd`, `bmad-spec`, `bmad-architecture`)
- Agent persona system (Mary, John, Winston, Amelia, Sally)
- Core verification gates (test/lint/run validation)
- Deterministic orchestration engine (BMAD Loop's Python control loop)
- Durable artifact persistence (Markdown + YAML files)
- Project context management (`bmad-project-context`)

These are foundational capabilities that battle map builds ON TOP OF, not replacements for.

---

## 7. Conclusion

**Summary of Findings**:

1. **Standard BMAD v6** excels at interactive phased software delivery with named agents, durable artifacts, and flexible planning paths. Its weaknesses are structural representation (no relationship modeling) and visual clarity (linear document chains).

2. **BMAD Loop** excels at unattended deterministic orchestration with trust-nothing verification, fresh-context adversarial review, and resumable state machines. Its weaknesses are assuming linear progressions and lacking human-interpretable structure views.

3. **Battle Map** proposes a fundamentally different abstraction: project shape cognition over long-term development. It's not a refinement of existing systems but a new product layer that needs:
   - Graph-based structural representation
   - Evidence coverage labeling
   - Minimum/formal dual-track implementations
   - Structural revision workflows with causal history
   - Progressive disclosure UI patterns

4. **Delta Reality**: Most battle map capabilities are "needs new mechanism" rather than "needs extension." This is not incremental improvement but complementary product family. Battle Map should launch as separate module alongside Standard BMAD, not as BMAD Loop feature.

5. **Execution Contract Alignment**: Current round treats Standard BMAD + BMAD Loop as research materials. Battle Map development should follow same pattern: treat each enhancement as experiment, document findings separately from project results, avoid prematurely elevating Battle Map to "future method" status.

**Strategic Implication**: Proceed with Battle Map as experimental module, not as Standard BMAD v7 release. Establish separate code path, research journal, and evaluation criteria. This preserves ability to abandon battle map constructs without destabilizing BMAD Method ecosystem.

---

## Appendix: Citations Index

### BATTLE-MAP.md Key Passages
- Core purpose (lines 3-14): Project shape preservation vs task fragmentation
- Not a task list (lines 15-31): Shape diagram before progression diagram
- Core objects (lines 33-99): Project goal, complete function, milestone, relationships, checkpoints
- Twelve-phase process (lines 100-167): From goals establishment to overall completion
- Two loops (lines 168-187): Structure discovery vs formal construction
- Must-express content (lines 188-207): Product structure, progression, evidence, evolution
- Seven core principles (lines 208-237): Functional granularity priority, milestone observability, etc.
- Error distinction (lines 242-257): Implementation vs structural failures
- Product definition (lines 258-390): Campaign map as cognition interface, not task manager

### Execution Contract.md Key Passages
- Four identities (lines 5-14): Standard BMAD ≠ Future Method, BMAD Loop ≠ Battle Map Implementation
- Context continuity (lines 16-36): Same-role sequential skills reuse session, independent reviews isolate
- Research-construction separation (lines 37-47): Project results and research results recorded separately
- Role chain sample validity (lines 99-116): Activate bmad-agent-* first, then dispatch workflows within session
- Context lifecycle by position (lines 117-125): Position switch = fresh context, position internal = continuous context
- Formal position in tmux/Qoder (lines 127-144): Interactive sessions as canonical execution surface

### Standard BMAD v6 Sources
- `workflow-map.md` (lines 22-97): Phase organization and workflow catalog
- `agents.md` (lines 1-36): Named agent personas and triggers
- `build-auto.md` (lines 73-253): Headless execution contracts and story folder dispatch
- `docs/reference/core-tools.md` (lines 48-56): Project context scan and maintenance

### BMAD Loop Sources
- `engine.py` (lines 0-6): Module docstring defining deterministic control loop
- `FEATURES.md` (lines 11-182): Capability summary table and detailed mechanism descriptions
- `statemachine.py` (lines 12-48): Phase transition table
- `verify.py` (lines 1-6): Verification philosophy: "never trust LLM self-reports"
- `src/bmad_loop/model.py` (Phase enum): PENDING, DEV_RUNNING, DEV_VERIFY, REVIEW_RUNNING, REVIEW_VERIFY, COMMITTING, TRIAGE_RUNNING, TRIAGE_VERIFY, DONE, DEFERRED, ESCALATED, AWAITING_OPERATOR
