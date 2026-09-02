---
topic: Battle Map — Project Semantic System and Execution Engine
status: final
created: 2026-09-01
updated: 2026-09-02
---

# Battle Map: A Project Semantic System for Complete-Shaped Development

## A. Product Thesis and User-visible Identity

**What this is:**  
Battle Map is a project-level semantic system that keeps track of what a developing system is becoming, why that shape was chosen, what's being built now, what evidence exists that it's actually working, and what unknowns remain. It presents projects as **project goals → complete functions → regions → milestones → structure relations → frontier → evidence boundaries → unknowns**, not as task lists or role-based work queues.

**Core thesis:**  
Long-term development loses the complete shape when too much detail accumulates before the product structure is established and continuously validated. Projects need a persistent projection layer that maps real implementation progress back onto an evolving model of what the final system should be, making each local decision understandable within the global shape while remaining openly revisable when evidence contradicts earlier assumptions.

**User-visible identity:**  
Users interact with Battle Map through a single system interface called "Project Map" showing current goal, function structure, frontier state, evidence coverage, and next-move rationale. They dispatch work by selecting action classes (explore, shape, implement, verify, close) which trigger autonomous workers configured for that action type. No role titles, no phase names, no external terminology required to understand or use the system.

**Internal engine:**  
The cognitive and execution layers absorb durable mechanisms from existing method systems (persistent persona patterns, multi-round workflows, durable handoff artifacts, explicit authority boundaries, deterministic implementation loops, session continuity, source-of-truth discipline) but digest them into generic composable parts. Users don't need to know these origins; they just get consistent cognition across rounds, clean handoffs between actions, and reliable verification.

---

## B. Core Ontology and Observable Project Semantics

### B.1 Project Goal

**Definition:** The ultimate result the system should achieve in reality. Not a feature list, not an implementation plan, but the observable condition that defines success.

**Observable criteria:** Must be expressible as concrete behaviors or conditions verifiable against actual system operation, not document completion.

**Example format:** "When deployed, the system accepts request X and produces response Y within Z latency under condition C, handling failure F gracefully."

### B.2 Complete Functions

**Definition:** Independent capabilities the system must possess to achieve the project goal. Each has defined inputs, core behavior, outputs, and contribution to the whole.

**Not task units:** Functions are divided by capability completeness, not by single-session execution scope. Later they may break into smaller execution units, but the initial structure expresses full capabilities first.

**Structure:** Each complete function includes:
- Input requirements
- Core behavioral contract
- Output guarantees
- Contribution to project goal

### B.3 Regions

**Definition:** Clusters of related complete functions that share concerns or dependencies. Regions allow grouping without forcing rigid hierarchies.

**Examples:** Authentication region, data processing region, integration region, UI/UX region.

### B.4 Milestones

**Definition:** Observable evidence that a complete function or region has achieved its intended capability. Milestones describe real behavioral changes, not document states or commit counts.

**Requirements:** 
- Must be verifiable against actual system behavior
- Cannot rely solely on execution status or artifact creation
- Should communicate what capability the system now possesses

### B.5 Structure Relations

**Definition:** Dependencies, parallelism, joins, and convergence relationships between functions and regions.

**Four primary relation types:**
- **Serial:** One thing must complete before another begins
- **Parallel:** Multiple things can proceed independently
- **Dependency:** Thing A requires capability B, but doesn't block its development
- **Join/Merge:** Multiple paths converge into single downstream work

**Dynamic modification:** Structure relations change when real implementation exposes false assumptions about independence, hidden dependencies, or missing intermediate capabilities.

### B.6 Frontier

**Definition:** Current executing state showing which functions/regions are active, blocked, completed, or ready to begin. Shows available next moves based on structure relations and milestone evidence.

**Elements:**
- Active work (currently implementing)
- Ready work (prerequisites met, waiting selection)
- Blocked work (waiting on specific dependencies/evidence)
- Completed work (milestone evidence confirmed)

### B.7 Current Validity Boundaries and Unknowns

Battle Map does **not** persist a forensic evidence archive. It keeps the compressed project meaning that remains useful for future advancement:

- **Current-validity boundary:** which functions, relations, milestones, or assumptions are presently treated as established enough to advance from.
- **Unknown boundary:** what is still structurally uncertain, untested, unexplored, or likely to change the route.
- **Invalidated boundary:** which previously accepted relation or assumption should no longer guide advancement.
- **Method constraint / lesson:** what research method, reasoning pattern, workflow step, or decomposition approach should be repeated or avoided next time.

Raw tests, diffs, review threads, tool calls, and execution logs remain in their native source systems. During an active judgment window, Battle Map may retain a lightweight source reference so a worker or owner can inspect the original context. That reference is **supporting context, not durable project knowledge**.

Once weaving has distilled a fact into a structural relation, route change, unknown boundary, or reusable lesson, the durable project state keeps the distilled meaning rather than copying the original fact trail.

**Critical principle: remove facts, retain relations.** Local success or failure matters only insofar as it changes the project shape, the next move, or a reusable method lesson. Fine-grained gates can be redone; the durable value is knowing how the gate relates to the larger route and what should be done differently next time.

### B.8 Candidate Structural Changes

**Definition:** Proposed revisions to the current map shape derived from distilled structural implications, newly exposed dependencies, changed unknown boundaries, or lessons that invalidate the present route.

**Properties:**
- Can be raised immediately from current reality without pretending the adopted map has already changed.
- Describe the proposed relationship/route change and why it matters at project level.
- May carry a temporary source reference while the judgment is active, but do not require permanent preservation of the underlying factual trail.
- Await the appropriate authority decision before becoming adopted structure.
- Can be accepted, rejected, deferred, or superseded.

**Why candidate layer matters:** It lets the system preserve new project understanding immediately while keeping a clean distinction between "what we have noticed" and "what now defines the project."

### B.9 Causal Narrative

**Definition:** An append-only explanation of how the project route, structural understanding, research method, or workflow approach evolved over time.

Each durable narrative entry should preserve only what remains useful after the incident itself is forgotten:
- **Prior direction / assumption:** what route or method the project was following.
- **Triggering realization:** the compressed reason that route became questionable; not a replay of the raw incident.
- **New judgment:** what changed in the project understanding, method, or process.
- **Impact:** which map relations, gates, routes, or future working rules changed as a result.
- **Lesson:** what should be repeated, avoided, or tested earlier in similar situations.
- **Supersedes link:** which earlier interpretation this entry corrects or replaces.

The narrative is not an audit log and is not responsible for reconstructing the exact factual state of every historical moment. Its job is to explain **why the project became shaped this way and what was learned along the route**.

Battle Map and Project Narrative remain separate views of the same evolving project: Battle Map answers "what is the current shape and how do we advance?"; Narrative answers "why did this shape and method evolve this way?" They connect through map nodes, relations, route revisions, and lessons—not through a copied evidence archive.

### B.10 Next Move Rationale

**Definition:** When recommending what to do next, explain WHY based on:
- Current frontier state (what's ready vs. blocked)
- Structural risk reduction potential (which choice lowers highest uncertainties)
- Unknown-boundary reduction value (which choice clarifies the most consequential uncertainty)
- Owner policy alignment (respects known constraints/preferences)

**NOT arbitrary scheduling:** Every recommendation ties back to explicit project structure, unknown boundaries, route lessons, and authority constraints—not to archived evidence volume or default orderings.

---

## C. Seven-Layer Native Architecture and Data/Control Loop

```mermaid
graph TB
    subgraph L7["Layer 7: Source / Adapter Layer"]
        S1[External Method Artifacts Adapter<br/>Requirement docs · Design records · Implementation artifacts]
        S2[Harness/IDE Adapter<br/>Execution events, tool calls]
        S3[Git Adapter<br/>Commits, diffs, branches]
        S4[Test Runner Adapter<br/>Results, coverage, traces]
        S5[Review System Adapter<br/>Code reviews, QA reports]
    end
    
    subgraph L6["Layer 6: Execution / Verification Runtime"]
        E1[Worker Executors<br/>Action-specific workers]
        E2[Deterministic Inner Loops<br/>Implementation verification cycles]
        E3[Terminal Status Writers<br/>Handoff projection updates, result records]
    end
    
    subgraph L5["Layer 5: Composable Cognitive Runtime"]
        C1[Persona Manager<br/>Role composition engine]
        C2[Authority Scope Resolver<br/>Decision jurisdiction]
        C3[Skill Bundle Loader<br/>Workflow protocols]
        C4[Handoff Contract Enforcer<br/>Artifact boundaries]
        C5[Session Identity Manager<br/>Continuity tracking]
    end
  
    subgraph L4["Layer 4: Advancement / Command Engine"]
        ADV[Advancement Coordinator<br/>Reads Project Map DB → Selects Action Class → Compiles Bootstrap Context]
        BOOT[Bootstrap Compiler<br/>Assembles context snapshot at handoff]
    end
    
    subgraph L3["Layer 3: Project Weaving / Auto-Association"]
        W1[Triggers & Event Plumbing<br/>Workflow completion, artifact changes, Git/test/review events]
        W2[Incremental Delta Reader<br/>Cursor-based per-source reads]
        W3[Semantic Distiller<br/>Relations · boundaries · route implications · lessons]
        W4[Auto-Association Engine<br/>Strong links commit; weak links stored as candidates]
        W5[Narrative Synthesizer<br/>Causal threads: prior→trigger→new→impact]
    end
    
    subgraph L2["Layer 2: Project Map Core / Project Shape Semantic Store"]
        PSS[(Project Shape Semantic Store)]
        MV1[Materialized View: Current Map State]
        MV2[Materialized View: Region/Function Details]
        MV3[Materialized View: Frontier Blockers]
        MV4[Materialized View: Adopted/Candidate Structures]
        MV5[Materialized View: Current Boundaries / Applicable Lessons]
        MV6[Materialized View: Causal Narrative Slice]
        # No MV7 for next-move recommendation—calculation belongs to Advancement Engine
    end
    
    subgraph L1["Layer 1: Experience / Projection Layer"]
        UI1[Global Project View<br/>Goal · Functions · Regions · Overall Progress]
        UI2[Regional Drilldown<br/>Detailed function map · Dependencies · Milestones]
        UI3[Frontier Visualization<br/>Active/Ready/Blocked/Completed]
        UI4[Joins Interface<br/>Integration points · Verification triggers]
        UI5[Context Peek<br/>Open source context only when needed]
        UI6[Candidate Changes Panel<br/>Proposed relations / boundaries / route changes]
        UI7[Narrative Timeline<br/>Temporal view of structural evolution]
        UI8[Next Move Recommendation<br/>Rationale · Alternative options (computed by Advancement Engine)]
    end

    L7 -->|raw events/logs| L6
    L6 -->|terminal status| L5
    L5 -->|role bindings| L4
    L4 -->|bootstrap context| L6
    L6 -->|execution outcomes| L3
    L3 -->|distilled shape/boundary candidates| L2
    L2 -->|materialized views| L1
    L1 -->|user selects action | L4
    L4 -.->|escalate owner decision| OWN[Owner Authority]
    OWN -->|approval | L2
    style OWN fill:#f9f,stroke:#333,stroke-width:2px
    style PSS fill:#bbf,stroke:#333,stroke-width:2px
```

**Data/Control Loop Flow:**

1. **User opens Project Map** → sees global view (goal, functions, structural relations, frontier, current-validity boundaries, unknowns)

2. **System presents available actions** → based on frontier state and advancement rationale

3. **User selects/dispatches work** → e.g., "implement current complete function / current execution unit"

4. **Advancement Coordinator reads current project shape** → compiles bootstrap context from the same shape revision: current complete function, milestones/acceptance criteria, regional invariants, upstream/downstream relations, current validity/unknown boundaries, applicable route/method lessons, active frontier, authority/feedback contracts

5. **Worker executes** → configured for selected action class (implement/verify/explore/shape), runs through deterministic inner loop

6. **Worker produces terminal status** → updates canonical snapshot, writes execution result, commits changes

7. **Weaving triggers** → reads only new source material into a temporary fact workset, associates it for the current interpretation, and distills durable relation/boundary/route/lesson implications

8. **Map/narrative update** → adopted/candidate project-shape views refresh; Project Narrative is appended only when the change carries a meaningful route/method lesson

9. **Next move rationale presented** → explanation of why that action follows from the current shape, blockers, unknown boundaries, route state, and applicable lessons

**Hard boundary:** Advancement Coordinator chooses WHICH worker runs. Worker's execution operates under deterministic control-plane discipline: dispatch snapshot frozen at start, auditable protocol steps and state transitions, explicit terminal states, outer layers cannot inject new decisions mid-execution. Worker internal cognition may be LLM-driven (not claimed deterministic); quality comes from workflow protocol + review separation, not internal determinism. Coordinator influences action class selection only, never execution logic or bootstrap recalculation mid-run.

---

## D. Battle Map User Operational Loop

### Step 1: Open Project Map

**Initial screen shows:**
- **Project Goal:** what the finished system is meant to become
- **Complete Functions / Regions / Milestones:** the map's main structural objects
- **Structural Relations:** serial, parallel, dependency, join, containment, replacement, blocking, and other project-level relations
- **Current Frontier:** which parts are active, ready, blocked, or closed
- **Current Validity / Unknown Boundaries:** where the current route is considered sufficiently established and where uncertainty still blocks investment
- **Recent Meaningful Route Revisions:** only changes that altered how the project should be understood or advanced

The first screen must answer: **what does this project become, where are we, what routes are open/blocked, and why is the next move reasonable?**

### Step 2: Understand Shape, Front, and Boundaries

At regional/function level the user sees the local structural neighborhood: upstream/downstream relations, joins, blockers, milestones, current frontier, active candidate overlays, and relevant unknown boundaries.

Battle Map does not present a permanent evidence ledger. If a current decision genuinely requires factual detail, the user/worker can open the original source context on demand. Returning to the map means distilling that detail into a relation, boundary, route revision, or lesson—not attaching the raw fact permanently to the node.

### Step 3: System Chooses or User Selects Action

Available action classes include exploring an unknown, shaping project structure, implementing a ready unit, verifying a join/chain, closing a function/region, or correcting course.

Recommendations explain the structural reason: which dependency became available, which blocker/unknown dominates, which route is most credible, or which prior method lesson applies. Alternatives are shown when more than one route remains reasonable.

### Step 4: Worker Executes and Produces Reality

A worker receives a frozen bootstrap built from one consistent project-shape revision. The worker may reason with models and use its own local plan/Todo, but the outer project shape is not hot-rewritten into its context mid-run.

Worker outputs remain in their native execution/source systems. Terminal results return to the weaving pipeline; the worker does not write raw results directly into the Project Shape Semantic Store.

### Step 5: Weaving Distills New Reality

Weaving incrementally reads only new source material into a temporary workset. It then asks whether the new reality changes:
- a project relation
- a current validity / unknown / blocking / frontier boundary
- the active route or project decomposition
- a reusable reasoning / research / workflow lesson

If none applies, nothing durable needs to be added to Battle Map. If one applies, weaving emits the corresponding semantic candidate and routes it to the responsible authority.

### Step 6: Project Shape Updates

After authority adoption, the affected project-shape relations and advancement boundaries become visible together across one atomic consistency boundary. Derived frontier and other views refresh from the new shape.

Project Narrative is appended only when the change carries a meaningful causal/method lesson. Rejected or obsolete operational candidates do not need permanent archival retention unless they produced such a lesson.

### Step 7: System Presents Next Move Rationale

For the next recommended action, Battle Map explains:
- what current relation/frontier condition makes the action possible
- which blocker or unknown it addresses
- how it affects the active route or join
- which relevant prior lesson changes how the action should be approached
- whether the required decision is delegated or must escalate

---

## E. Project Shape Semantic Store: Query Model and Projections

### E.1 Persistence Boundary

**The Project Shape Semantic Store owns the current durable project shape, not project history as a fact archive.**

Long-lived contents:
- minimal meaning of project goals, complete functions, regions, and milestones
- first-class structural/advancement relations between those objects
- adopted shape plus active candidate overlays
- current validity, unknown, blocking, frontier, and closure boundaries needed to advance
- meaningful route revisions that changed the project's structural interpretation

Long-lived contents do **not** include raw Git/Test/Review/Harness streams, local Todo/tool calls, diffs, full logs, review threads, complete rejected-candidate histories, or a forensic record of every source event.

**Separate responsibilities:**
- **Project Narrative:** durable causal/method/process lessons explaining why important route/structure changes happened
- **Weaving operational state:** source cursors, temporary fact worksets, dedupe state, active source references
- **Cognitive/Execution runtime state:** current action/session bindings and worker-local progress

These may be persisted by implementation, but they are not part of the canonical project-shape truth.

### E.2 Query Model Interfaces

**Query: get-current-project-shape**
Returns current goal, functions, regions, milestones, adopted relation network, active candidate overlays, frontier, current validity/unknown boundaries, and current route.

**Query: get-local-shape {region_or_function}**
Returns the selected object's structural neighborhood: containing region, upstream/downstream dependencies, parallel paths, joins, blockers, milestones, candidate overlays, and current boundaries.

**Query: get-frontier-and-legal-moves**
Returns active/ready/blocked/closed parts and the structural reasons behind those classifications.

**Query: get-candidate-overlays**
Returns currently operational shape/boundary/route candidates that may affect further investigation or authority decisions. It is not a permanent history query.

**Query: get-applicable-lessons {target}**
Resolves relevant Project Narrative lessons for the current node/region/route without merging Narrative into the shape store.

**Query: get-current-action-context**
Returns the action target, frozen shape revision/snapshot identity, authority scope, escalation contract, and runtime binding needed to inspect current work.

**Shape revision semantics:**
- Dispatch decisions and bootstrap compilation bind to the SAME immutable project-shape revision/snapshot
- A running worker keeps that frozen view even if a newer project shape is adopted later
- An adopted shape change creates a new meaningful shape revision boundary when needed for consistency and route understanding
- The product does not require every source event or every intermediate judgment to remain reconstructable forever

### E.3 Derived Views and Indexes

Derived views may include current global map, local relation neighborhood, frontier/blockers, candidate overlays, join preparation, and current action context.

These are **rebuildable projections** of the Project Shape Semantic Store (optionally enriched with relevant Narrative lessons). Specialized graph/full-text/vector indexes may also be derived later. No derived index becomes an independent semantic authority.

---

## F. Project Weaving: Background Pipeline and Narrative Model

### F.1 Triggers and Event Plumbing

**Purpose:** Triggers wake the weaving pipeline; they do not create durable project facts by themselves.

**Typical triggers:**
- Cognitive workflow reaches a stable handoff or terminal point
- A tracked artifact changes materially
- Git / test / review / runtime sources report new activity
- A worker returns a terminal result

**Boundary:** Trigger payloads enter a TEMPORARY FACT WORKSET. They are operational input for interpretation and may be discarded after distillation. A trigger is never itself a durable Battle Map object.

### F.2 Incremental Read Strategy

**Per-source operational cursors** track only enough position to read new material without rereading the entire source.

**Delta reading:** Load only source changes since the last acknowledged cursor, deduplicate repeated source events, and keep the resulting raw material in the temporary workset.

**Recovery discipline:** If weaving stops, resume from the last acknowledged cursor. Cursor state belongs to weaving operations, not to the long-lived Project Shape Semantic Store.

**Retention discipline:** Raw deltas are not promoted merely because they were processed successfully. Only distilled project relations, current boundaries, meaningful route revisions, or narrative/method lessons may cross the durable boundary.

### F.3 Fact Extraction Heuristics

The weaving pipeline asks four project-level questions of new source material:

1. **Relation implication:** Does this change how two project objects depend on, block, parallel, join, contain, replace, or enable one another?
2. **Boundary implication:** Does this expose, resolve, or move a current-validity / unknown / frontier boundary?
3. **Method implication:** Does this reveal a reusable problem in the reasoning method, research order, decomposition, workflow, or coordination approach?
4. **No durable implication:** If none of the above applies, the source material is consumed for the current judgment and then left in its native source.

Extraction may use deterministic parsing, semantic reasoning, or both. The durable output is the distilled implication, not a compressed copy of the source.

### F.4 Auto-Association Rules and Discipline

Auto-association has two different jobs and neither is allowed to create adopted project meaning by itself.

**① Working association:** During the temporary fact workset, explicit identifiers, paths, run references, session context, or semantic matching may associate source material with likely map objects. This association exists to help distillation. It is not automatically a long-lived provenance ledger.

**② Durable semantic candidate:** When the working material implies a project-level change, weaving emits one or more candidates:
- relation change (add/remove/replace/reclassify a structural or advancement relation)
- boundary change (unknown/current-validity/frontier/blocking boundary)
- route revision (a meaningful change in the path being pursued)
- narrative / method lesson candidate

**Critical discipline:**
- Explicit source matching may make a working association reliable, but it does not grant authority to change project shape.
- Ambiguous semantic association remains a candidate until the appropriate authority resolves it.
- Source detail stays external. If a current decision needs to inspect it, open it on demand; after the decision, persist the resulting project relation/boundary/lesson rather than the source detail.
- A source event that produces no durable project implication may leave no long-lived Battle Map record.

### F.5 Narrative Synthesis Pattern

Project Narrative is NOT a stream of every source event or every map mutation.

Create a narrative entry only when the project learned something worth preserving about **why the route changed** or **how the reasoning / research / workflow should change next time**.

A durable narrative entry should capture, at the semantic level:
- previous route or working belief that mattered
- what kind of trigger forced reconsideration (summary, not forensic transcript)
- revised understanding or method lesson
- effect on the project route / decomposition / workflow
- links to the relevant map objects or meaningful route revision

Narrative may supersede earlier explanations without deleting them. It does not need to preserve every historical fact, and Battle Map correctness must not depend on replaying the narrative.

### F.6 Candidate Output Format

Weaving may produce four durable candidate classes:

- **Shape candidate:** proposed change to nodes or first-class relations
- **Boundary candidate:** proposed change to unknown, validity, blocking, frontier, or closure boundaries
- **Route candidate:** proposed change in which path/region should be treated as the active structural route
- **Narrative / lesson candidate:** proposed method/process/causal lesson worth retaining

Candidates carry enough rationale to support authority review and may temporarily reference external source context while that review is active. They do not become adopted project shape until the responsible authority accepts them.

Rejected or abandoned candidates do not need permanent archival retention. If a rejection itself teaches a reusable lesson or changes the route, preserve that lesson/route change in Project Narrative; otherwise the candidate may disappear after it is no longer operationally relevant.

## G. Advancement / Command Engine and One-Click Bootstrap

### G.1 Advancement Coordinator Responsibilities

**Coordinator DOES:**
- Reads the current adopted project shape, candidate overlays, unknown/current-validity boundaries, frontier, current actions, and applicable owner policy from one consistent snapshot
- Evaluates which action classes are currently legal and useful from that shape
- Chooses the next action class / target according to structural dependencies, blockers, unknowns, route state, and applicable lessons
- Compiles a frozen bootstrap snapshot from the SAME project-shape revision
- Monitors worker terminal status and routes new results back into weaving
- Escalates only when the applicable authority policy requires it

**Coordinator does NOT:**
- Read raw source material and invent structural meaning directly
- Mutate adopted project shape
- Influence a running worker by hot-injecting new outer decisions
- Replace independent verification or the owning authority
- Turn rejected candidates or historical source material into a permanent archive

### G.2 Action Classes

**① Analysis/Discovery**
- Purpose: Explore decisions requiring research, validate assumptions, pressure-test ideas
- Workers: deep-recon agent, brainstorm facilitator, forge-idea stress tester, PRFAQ analyst
- When used: At project start, before major shaping decisions, when unknowns block progress

**② Planning/Shaping**
- Purpose: Define requirements, design experiences, establish architecture, create specs
- Workers: discovery worker, experience-shaping worker, structural-constraint worker, execution-contract worker
- When used: After discovery uncovers needs, before implementation, when structure requires clarification

**③ Implementation**
- Purpose: Build execution units, implement features, deliver working changes
- Workers: construction worker (manual checkpoint), autonomous builder (unattended)
- When used: When execution units ready for development, during sprint execution, for continuous delivery

**④ Verification at Joins**
- Purpose: Run integration checks before dependent work proceeds, validate composition
- Workers: review triage, test automation, integration validators
- When used: At natural join points (dependencies converge), before merging parallel paths, when prior closure review flagged risks

**⑤ Function/Region Closure**
- Purpose: Aggregate review of completed work against acceptance criteria, retrospective on lessons learned
- Workers: retrospective facilitator, closure verdict enforcer
- When used: When function/region considered complete, before marking milestone done, periodically for reflection

**⑥ Correct Course / Reconciliation**
- Purpose: Process structural contradictions, mediate between reality and map, propose adaptations
- Workers: correct-course analyst, reconciliation transaction executor
- When Used: When evidence conflicts with adopted structure, when candidate changes accumulated sufficient weight, when significant deviation from original shape detected

### G.3 Escalation Thresholds to Owner Authority

**Coordinator escalates autonomously when:**
- Product meaning requires judgment beyond observable evidence
- Unresolved preference choices (reasonable options exist, no clear best answer)
- Irreversible or high-cost commitments (architecture paradigm shifts, platform migrations)
- Scope/strategy changes beyond current region/function boundaries
- Product-definition authority accepts/rejects decisions
- Major architecture范式变更超出现有 spine 的适用范围
- Owner-policy defined thresholds crossed (configurable per project)

**All other decisions:** Coordinator handles autonomously, logs rationale in Project Map, proceeds without blocking.

**Escalation format:** Presents Owner with specific question, context summary, recommended option with justification, alternative options with tradeoffs. Owner returns approve/reject/modify decision.

### G.4 Bootstrap Context Compilation

**Before dispatching worker, Coordinator assembles:**

**For implementation worker:**
- Current execution unit specification and companion files from Project DB
- Regional invariants affecting this unit
- Prior execution units' terminal statuses from same region (continuity)
- Sprint status showing unit order and dependencies
- Open questions and assumptions from current specification
- Known integration points from adjacent units

**For exploration worker:**
- Current unknown boundaries and why they matter to the active route
- Related artifacts (brief, prior recon reports, competitive analyses)
- Previous failed hypotheses or dead ends
- Owner constraints/preferences relevant to exploration

**For verification worker:**
- Upstream units' terminal statuses and evidence refs
- Documented interface assumptions from adjacent implementations
- Expected integration points from design constraints
- Known defect patterns from previous closures

**Principle:** Bootstrap is FROZEN SNAPSHOT at dispatch time—not bi-directional sync, not live pulling during worker execution. Worker gets coherent context that won't shift beneath it mid-run.

---

## H. Cognitive Runtime: Composable Persona/Authority/Skill/Workflow/Handoff/Session Model

### H.1 Role as Composition, Not Fixed Titles

**Stable templates EXIST but are NOT fixed ontology.** For each action, runtime composes needed role from parts:

```yaml
role_instantiation:
  persona: <cognitive stance / thinking mode>
  authority_scope: <decision jurisdiction / escalation rules>
  skill_bundle: <workflow protocol / toolkit>
  workflow_protocol: <step sequence / gate sequence>
  handoff_contract: <artifact inputs/outputs / termination criteria>
  session_identity: <continuity token / durable storage ref>
```

**Examples:**
- **Advancement Coordinator:** Persona=Strategic Analyst | Authority=Action Selection Only | Skill=Map Reading + Frontier Analysis | Handoff=Bootstraps Worker | Session=Coordinator Instance Lifespan
- **Function Implementer:** Persona=Craftsman + Problem Solver | Authority=Execution Unit Implementation Within Specification | Skill=Construction Protocol | Handoff=Terminal Status + Commits | Session=Unit Lifespan
- **Independent Verifier:** Persona=Skeptic + Detail Oriented | Authority=Triage Verdict Only | Skill=Review Protocol | Handoff=Triage Log + Defects | Session=Verification Round
- **Project Shaper:** Persona=Architect + System Thinker | Authority=Design Within Constraints | Skill=Structure Constraint Protocol | Handoff=Design Constraints + Decisions | Session=Region Lifespan
- **Owner:** Persona=Product Leader + Decision Maker | Authority=Final Approval on Escalations | Skill=Policy Setting + Gate Decisions | Handoff=Direction + Constraints | Session=Project Lifespan

**Template examples (NOT definitions):**
- Product-shaping template = Persona=Product Visionary + Authority=Product-definition Decisions + Skill=Shaping Protocol
- "Architect-style" = Persona=System Designer + Authority=Cross-unit Invariants + Skill=Architecture Protocol
- Implementation template = Persona=Craftsman + Authority=Implementation Within Execution Contract + Skill=Construction Protocol

**These are examples only.** System recognizes role patterns emerge from combinations, not predefined job titles.

### H.2 Cognitive Runtime Principles (Native Product Rules)

**Cognitive discipline:**
- **Persistent role persona:** Same role maintains cognitive stance across multi-turn conversation for depth
- **Role-vs-skill separation:** Distinction between WHO (persona/authority) and WHAT (skill/workflow)
- **Multi-round workflows:** Complex tasks broken into phases with checkpoints, not single-call operations
- **Durable handoff discipline:** Stable semantic projections ensure context survives session boundaries
- **Explicit authority boundaries:** Each role knows what decisions it owns vs. what escalates upward
- **Fresh independent review:** Implementation completes → separate review pass occurs → triage happens
- **Feedback/correct-course semantics:** Significant changes trigger structured adaptation, not ad-hoc patches
- **Deterministic control-plane discipline:** Input snapshot frozen at worker start, auditable state transitions, explicit terminal states, no mid-run injection from outer layers
- **Responsibility continuity policy:** Session persistence depends on whether same cognitive responsibility is continuous, whether causal context needs preservation, whether workflow demands independent judgment—not fixed按特定对象名称切割
- **Session binding discipline:** Fresh context用于真正的职责切换、独立验证、上下文损坏/容量等需要认知隔离的边界；新 session 必须从 durable handoff / project DB snapshot 恢复，而不是重新问同样问题
- **Source-of-truth discipline:** Canonical writers per domain prevent competing authorities; readers reference but don't mutate

**File formats and storage:** Native system prefers semantic DB as source of truth, exports to compatible formats at handoff boundaries.

### H.3 Intentional Negative Constraints (External Identity)

**Do NOT expose as product ontology:**
- Hardcoded job titles as user-facing structure
- Fixed step sequences as mandatory workflows
- Phase-gate terminology as user-facing navigation
- Any vocabulary requiring external reference for understanding

**Reason:** Product must be fully understandable WITHOUT prerequisite knowledge of internal mechanisms. Public vocabulary stands alone; internal details belong in documentation or compatibility layer.

### H.4 Composable Runtime Instantiation

**At action dispatch time:**
```
User selects: "implement current region execution unit"

Runtime composes:
  persona = Function Implementer (craftsman + problem solver mode)
  authority_scope = implement within execution-contract constraints, escalate execution-contract conflicts
  skill_bundle = build-protocol (clarify→plan→implement→review→triage)
  workflow_protocol = battle-native construction flow OR compatible external protocol
  handoff_contract = terminal status → canonical snapshot update, commits pushed
  session_identity = responsibility-continuity-key bound to action lifecycle (e.g., {action-type}-{target-unit} binding pattern, implementation-specific)

Worker spawns with composed role bound to execution lifecycle.
```

**Result:** User sees "implementing current region execution unit" not specific persona names. Internally, system composes appropriate cognition stack for that action. Consistency preserved through responsibility continuity policies based on execution unit lifespans, not fixed role activation patterns.

---

## I. Execution/Verification Runtime and Deterministic Inner-Loop Boundary

### I.1 Worker Types

**Autonomous Workers (unattended):**
- implementation worker: Implement execution units without human intervention, terminate with status
- verification-auto: Run automated checks, produce triage results
- analysis-auto: Execute research prompt, synthesize findings
- narrative-auto: Trigger weaving incrementally, produce candidate deltas

**Interactive Workers (checkpoint-required):**
- implementation-manual: Implement with human review at key junctures
- shaping-manual: Multi-round collaboration on requirements/architecture
- verification-manual: Human-led review with adversarial critique modes
- closure-manual: Facilitated retrospective requiring participant input

**Common trait:** All workers receive composed role + bootstrap context, execute through deterministic workflow protocol, produce terminal status.

### I.2 Deterministic Inner Loop Guarantee

**What "deterministic" means:**

**Control Surface Determinism (guaranteed):**
- Input snapshot frozen at dispatch time: bootstrap context immutable during execution
- Protocol steps/state transitions auditable: workflow protocol clearly defined, state machine traceable
- Terminal state explicit: worker exits with definitive OK/FAILURE/BLOCKED/PARTIAL and rationale
- No mid-run injection: outer layers cannot recompile bootstrap or inject new decisions during execution
- Decision boundary enforced: worker may exit early with terminal status if new facts require上层决策，而不是热修改当前执行目标

**Worker Internal Behavior (NOT claimed mathematically deterministic):**
- Worker may be LLM-driven, stochastic cognition accepted
- Internal reasoning not exposed as product contract
- Quality comes from workflow protocol + review separation, not internal determinism

**Hard invariant:** Once worker starts execution, NO external system influences its internal decision-making logic OR re-compiles bootstrap context mid-run.

**Specifically forbidden:**
- Project Map injecting dependency-graph inference into execution-unit scheduler
- LLM calling in orchestrator control loop
- Real-time Map state pulls during worker execution
- Dynamic bootstrap recalculation mid-run
- Coordinator overriding worker verdict after execution completes
- Any layer attempting to modify execution target based on new evidence discovered mid-run

**What IS allowed:**
- Coordinator selecting WHICH worker runs next
- Worker reading SNAPSHOTS of context compiled at dispatch time
- Worker writing terminal status upon completion
- Weaving consuming terminal status as EVENT for future Map updates
- Worker exiting with BLOCKED/PARTIAL/FAILURE when new facts require owner/coordinator decision, entering next advance cycle with recompiled bootstrap

**Terminal status as decision point:** When worker encounters new facts requiring decisions beyond its authority scope, it should EXIT with appropriate terminal status (BLOCKED for missing context, FAILURE for execution-contract conflicts, PARTIAL for incomplete progress), letting coordinator re-compile fresh bootstrap and decide next action class. This preserves clear boundaries between execution autonomy and strategic direction.

**Boundary enforcement:** This rule applies equally to all worker variants. The control plane remains deterministic and auditable, while worker internal cognition may be LLM-driven. Implementation-specific isolation belongs in architecture design rather than the product-requirement contract.

### I.3 Terminal Status Semantics

**Worker terminates with one of:**
- **OK:** Successfully completed, produced expected artifacts, no blocking issues
- **FAILURE:** Completed but found blockers (defects, intent mismatches, execution-contract violations)
- **BLOCKED:** Could not proceed (missing context, ambiguous requirements, environmental issues)
- **PARTIAL:** Made progress but didn't reach completion state

**Terminal status MUST include:**
- Final `status:` field machine-readable for orchestration
- `blocking_condition:` if blocked/failure (clear reason)
- `followup_review_recommended:` boolean flag for review pass suggestion
- `baseline_revision:` git hash before this run (or NO_VCS)
- `deferred:` list of findings triaged elsewhere (summary, evidence, location, severity)
- `files_changed:` inventory of modified/created files
- `results_summary:` human-readable account of what happened

**Orchestrator responsibility:** Monitor terminal status, act on it rather than inferring from chat output alone. Treat BLOCKED as routing signal requiring human/orchestrator takeover, not just failure notification.

### I.4 Verification and Review Separation

**Implementation completes → Independent review runs:**
- Separate cognitive stance (skeptic vs. creator)
- Separate authority scope (triage verdict only, no implementation decisions)
- Access to same bootstrap context but independent judgment
- Produce triage log with findings classified by severity

**Triage classification:**
- **High:** Blocking defects requiring immediate attention
- **Medium:** Important issues impacting quality but not stopping progress
- **Low:** Minor improvements worth noting but not urgent
- **False Positive:** Reviewed items not actually problems
- **Maybe False Positive:** Borderline cases needing discussion

**Deferred findings:** Items belonging to other functions/regions/epics get logged separately rather than blocking current work. Orchestrator decides如何处理 (create tickets, queue for later, or ignore).

---

## J. Source/Adapter Layer and On-Demand Context Access

### J.1 Adapter Design Principles

**Purpose:** Adapters translate each external system's native change signal into a TEMPORARY WORKING INPUT that weaving can incrementally read. They do not normalize the world into a permanent Battle Map fact warehouse.

Typical sources include method artifacts, Harness/IDE sessions, Git, tests, reviews, runtime systems, and future custom systems.

Each adapter owns only:
- source identity and access method
- incremental/cursor read behavior
- enough transient structure for weaving to inspect the new material
- a way to reopen the original source when a current judgment needs detail

**Durable boundary:** An adapter never decides project meaning. Only the weaving → authority → project-shape commit path may create durable Battle Map semantics.

### J.2 On-Demand Source Context

When a current judgment cannot be made from distilled project semantics alone, the user or worker may open the original source context on demand:

**Possible source contexts:**
- **Source Artifact Link:** Click-through to original document (requirement/specification, design decisions, implementation records, etc.)
- **Run Logs:** Terminal output or session transcript showing execution
- **Terminal Status File:** Machine-readable result with verdict and metrics
- **Code Diff:** Side-by-side comparison of changes made
- **Commit History:** Git log entries related to this work
- **Test Results:** Pass/fail breakdown, coverage percentages, flaky test flags
- **Review Comments:** All review findings with severity classifications
- **Related Narrative Entries:** Chronological context showing prior decisions this evidence challenges/supports

**Context shown alongside the source:**
- This evidence belongs to which node/function/region
- Which current map relation / unknown / candidate caused this source to be opened
- What decision is currently being made
- What project-level implication should be distilled before returning to the map

**Retention rule:** Opening source material does not make it part of Battle Map. After the judgment is distilled, durable storage keeps the resulting relation, boundary, route revision, or lesson; the raw source remains external.

---

## K. Adoption/Candidate Structural Evolution and Authority Semantics

### K.1 Two Conceptual State Classes

**ADOPTED PROJECT SHAPE:**
- The current authoritative network of project objects, first-class relations, and the small set of current validity / unknown / frontier / closure boundaries needed to advance the project
- Changes only when the responsible authority accepts a semantic change and the complete affected shape update crosses one atomic consistency boundary

**CANDIDATE / PENDING SHAPE:**
- Proposed relation, boundary, route, or shape changes produced by weaving or cognitive work
- Visible as an overlay because they may affect what should be investigated next, but they do not redefine current project shape before adoption

**Retention principle:** Candidate history is not an archaeology target. Keep candidates while they matter operationally; preserve only meaningful route/method lessons when they deserve long-lived memory.

### K.2 Reconciliation Transaction Protocol

**Correct causal order for a project-shape change:**
```
External reality / cognitive finding
  ↓
Temporary fact workset (when raw source material exists)
  ↓
Weaving / cognition distills a relation, boundary, route, or shape candidate
  ↓
Resolve the responsible authority scope
  ↓
Authority accepts / rejects / modifies the semantic candidate
  ↓
If accepted: atomically apply the complete affected project-shape change
  ↓
Refresh frontier / bootstrap / other derived projections
  ↓
If the change carries a reusable route or method lesson: append Project Narrative
```

**Atomicity invariant:** Any adopted change that alters the current project shape must make the related relations and advancement boundaries visible together or not at all. The architecture does not prescribe a specific database transaction mechanism here.

**Rejection discipline:** Rejection does not require a permanent evidence trail. If the rejected path reveals a reusable lesson, retain the lesson; otherwise the operational candidate may be discarded.

**Map updates are semantic reconciliation boundaries, not agent-memory rules.** Workers and external sources remain authoritative for their own raw execution facts; the Project Shape Semantic Store owns only the distilled project meaning.

### K.3 Regional Maturity States

**Each region/function/current execution unit tracks maturity:**

- **Exploration:** Actively exploring, not yet formalized, structure uncertain
- **Formal Construction:** Structured work in progress, product definition / structural constraints / execution contracts sufficiently formalized, implementation underway
- **Closed:** Verified and closed, closure verdict passed, milestone evidence confirmed
- **Deferred:** Temporarily postponed, waiting for more evidence or conditions met

**Transitions driven by evidence sufficiency, not calendar dates.** Coordinator asks: "Does evidence justify moving Exploration→Formal?" Owner answers for irreversible/high-cost transitions.

### K.4 Investment Judgment as Map State Decision

**At maturity transitions, coordinate/owner evaluates:**
- Does accumulated evidence support progressing to next phase?
- Are remaining unknowns acceptable for forward movement?
- Is postponement wiser than proceeding?
- What additional evidence would de-risk further?

**This IS investment judgment** without requiring formal investment-gate ceremony. Evidence collected naturally throughout workflow serves as justification for progression. Regular transitions handled autonomously by coordinator. Only truly irreversible/high-cost/significant-meaning ones escalate to owner.

**Documentation:** Each maturity transition logs rationale in causal narrative: prior state, evidence reviewed, decision made, who approved, why justified.

---

## L. Validation Plan and Open Decisions

### L.1 Null Hypothesis Preservation

**Default assumption:** Existing mechanisms already sufficient unless observed behavior proves otherwise. Evolution needed ONLY when empirical evidence shows recurring friction worth changing.

**Burden of proof:** Candidate deltas (weaving findings, adoption proposals) start with null hypothesis "no change needed." Promotion to confirmed gaps requires demonstrating material ambiguity/premature commitment/rework/coordination cost that justifies added ceremony.

### L.2 Validation Observation Model

**Key actors in validation:**
- **Owner:** Final decision authority on escalated items
- **Chief Engineer:** Orchestration artifact-handoff coordination (non-authoritative observation role)
- **Active role at lifecycle point:** Executor/observer for current action (implementing developer, reviewing architect, etc.)
- **Independent reviewers/Closure:** Evidence-producing review, not stakeholder approvals
- **Runtime system:** Deterministic evidence sources, not stakeholders

**Note:** Remove "stakeholders" frontmatter. Observers provide evidence, final decisions rest with Owner or delegated Coordinator within policy bounds. Measurement protocol neutral; promote new behavior only if evidence shows material benefit.

### L.3 Stage-1 Behavior Acceptance Criteria

Battle Map system demonstrates five core properties:

**① Persistent Structure Cognition:**
- Criterion: Cross-lifecycle, cross-region projected awareness maintained via workflow-boundary reconciliation edges refreshing adopted/candidate states
- Observable: Moving beyond single artifact/unit continuity toward persistent project-shape awareness across region boundaries

**② Explicit Structural Error Classification:**
- Criterion: Existing execution feedback classification retained; structural consequence evidence gets landing point via candidate Map delta → reconciliation transaction → owning authority
- Observable: No new parallel classification layer needed; existing mechanism augmented by Map representation

**③ Composite Reality Verification:**
- Criterion: Dependencies/join points represented in Map; Coordinator dispatches existing verify/review/test workflows at natural joins before dependent work proceeds; function/region closure remains primary review mechanism
- Observable: Integration defects caught earlier in join points rather than surfacing at completion or production

**④ Unknown and Evidence Boundary Marking:**
- Criterion: Map state carries per-region/dependency evidence support + uncovered boundaries derived from Project DB adopted state + source refs / stable handoff projections; missing-evidence rule preserved
- Observable: Boundaries become first-class Map state exported from canonical references without requiring claim-marking everywhere

**⑤ Justifiable Investment Judgment:**
- Criterion: Next-step decision at maturity/promotion transition cites evidence supporting exploration→formal, defer, or more-evidence paths with recorded justification
- Observable: Transitions become explicit evidence-cited Map state decisions rather than implicit readiness checks

### L.4 Open Decisions (Resolvable Through Downstream Observation)

**These will clarify in actual execution, not predetermined here:**

1. **Investment transition escalation weight:** What qualifies as "high-cost"? What counts as "meaning-laden"? Configurable per project; learn from observing escalation patterns.

2. **Natural join boundary definition:** Which dependency patterns constitute "joins" requiring verification dispatch? Adjust based on actual defect patterns observed in real multi-region / multi-execution-unit deployments.

3. **Region maturity state granularity:** How many maturity levels optimal? Precise transition criteria? Refine empirically rather than theorizing upfront.

4. **Candidate lifecycle / staleness handling:** Candidates become stale when source evidence expires, superseded by subsequent evidence, adopted/rejected, or target structure versions change; time-based cleanup policies are architecture/operations decisions, not predefined at product-requirement level.

5. **Weaving trigger frequency:** Time threshold vs. event-threshold balance? Too frequent = noise overhead; too rare = stale Map. Tune based on project velocity.

6. **Autonomy boundary quality:** Which categories can advancement coordinator handle autonomously, which must escalate? Observe through mis-escalation rate, failure to escalate events, repeated unnecessary interruptions, directional misjudgments — do not reduce to ratio metrics.

### L.5 Success Metrics (Qualitative, No Numeric Thresholds)

**Victory conditions for Battle Map evolution:**
- Owners report clearer understanding of project shape and current frontier
- Reduction in premature commitment or discover-late structural errors
- Smooth brownfield transition without losing mature mechanisms
- Routine advancements can be autonomously completed within established authority boundaries without unnecessary Owner interruption, while directional/high-cost decisions are correctly escalated
- Integration defects caught progressively at join points rather than accumulating
- Narrative explains structural changes causally, not just chronologically
- Battle Map vocabulary fully understandable without prerequisite knowledge

**Failure conditions (null hypothesis wins):**
- Coordination overhead exceeds benefits gained
- Weaving produces excessive candidate noise requiring manual cleanup
- Owners prefer simpler existing workflow without Map overlay
- Integration failures pattern unchanged from baseline
- Complexity introduced not justified by observable improvement
- Brownfield compatibility creates more friction than value

---

## M. Mechanisms Absorbed from Standard BMAD/BMAD Loop + Brownfield Compatibility

### M.1 What Was Absorbed (Internal Reference Engine)

**Durable mechanisms digested into battle-map-native components:**

**From Standard BMAD:**
- **Persona/skills separation:** Distinct cognitive stances (analyst, shaper, implementer, verifier) paired with workflow protocols (brainstorm, spec, build, review)
- **Workflow protocols:** Multi-round disciplined flows (clarify→plan→implement→review→triage→commit) preserving depth over single-call shortcuts
- **Durable handoff artifacts:** SPEC.md, ARCHITECTURE-SPINE.md, epic records, memlogs ensuring context survives session boundaries
- **Authority boundaries:** PRD owns product definition, Architecture owns cross-unit invariants, SPEC derives implementation contract, Retro closes epics with acceptance verdict
- **Independent review model:** Implementation completes → separate skeptic mindset runs review → triage verdict independent of implementer
- **Feedback/correct-course semantics:** Significant deviations trigger structured adaptation protocol rather than ad-hoc patches
- **Responsibility continuity policy:** Session persistence depends on whether same cognitive responsibility is continuous, whether causal context needs preservation, whether workflow demands independent judgment; fresh context for true role transitions/independent verification/boundary isolation; new sessions restore from durable handoff / project state snapshot, not re-ask questions
- **Source-of-truth discipline:** Canonical writers per artifact prevent competing authorities; readers reference but don't mutate
- **Brownfield entry patterns:** Start from existing codebase/PRDs with gradual formalization rather than greenfield-only assumptions

**From BMAD Loop:**
- **Deterministic control-plane discipline:** Dispatch input snapshot frozen at worker start, schedulable state transitions auditable, terminal states explicit, outer layers cannot inject new decisions mid-execution. Worker internal cognition may be LLM-driven (not claimed deterministic); quality from workflow protocol + review separation, not internal determinism.
- **Terminal status discipline:** Each worker exits with definitive status field, blocking condition, and actionable followup suggestions
- **One-worker-per-unit semantics:** Single coherent work item per invocation provides clean boundary between execution autonomy and coordination direction (implementation-specific patterns like folder+id dispatch or story ordering are compatibility paths, not native requirements)

**Brownfield compatibility implementations (available but NOT native defaults):**
- Spec-folder-based story organization with ordered yaml manifests
- Optional git worktree isolation for experimental runs
- Recovery-flow patterns for interruption handling
- Zero-token E2E testing guarantees (platform-specific)

**Principle:** Only proven cross-context value gets absorbed as native mechanism. Implementation-specific patterns stay as brownfield compatibility options.

**Absorption philosophy:** These mechanisms survive because they demonstrably improve quality, consistency, and reliability. They're not copied as dogma but retained as proven patterns worthy of preservation.

### M.2 What Was NOT Copied (External Vocabulary)

**Deliberately NOT exposed as product ontology:**
- `bmad-*` skill name prefixes replaced with native equivalents (build, spec, architecture, review, retro renamed to action verbs)
- Mary/John/Winston/Amelia persona names replaced with functional descriptions (Analyst, Shaper, Implementer, Verifier)
- Four-phase BMAD labeling (Analysis/Planning/Solutioning/Build) replaced with action class selection (Explore, Shape, Implement, Verify, Close)
- Markdown forest as sole storage replaced with Project Map DB + compatibility export layer
- Phase-gate ceremonies replaced with evidence sufficiency and natural checkpoints
- Fixed step sequences made configurable templates rather than hard mandates

**Reason:** Battle Map must stand alone understandable without BMAD prerequisite knowledge. Internal mechanisms may freely borrow; public vocabulary must be self-contained.

### M.3 Brownfield Transition Path

**Three-phase migration for existing BMAD users:**

**Phase 1: Dual Operation (compatibility layer active)**
- BMAD skills remain callable with native vocabulary (`bmad-prd`, `bmad-build`, etc.)
- Weaving extracts output artifacts into Project Map DB automatically
- Users see both BMAD view and Battle Map view side by side
- Coordinator can dispatch either BMAD workers or battle-native workers
- Evidence: Minimal disruption, smooth onboarding, learning curve softening

**Phase 2: Semantic Unification (Project Map DB becomes single source of truth)**
- BMAD artifacts still writable but viewed as compatibility projections
- Project Map queries serve as canonical source for bootstrap compilation
- Native vocabulary becomes default in documentation/UI
- BMAD skill names still available but redirect to battle-native equivalents internally
- Evidence: Reduced duplication, cleaner mental model, less context loss

**Phase 3: Native Default (battle-map-native ontology primary)**
- Battle Map vocabulary primary in all user-facing contexts
- BMAD skills available as optional compatibility shim for teams not ready to migrate
- Documentation focuses on native concepts; BMAD mappings provided for reference
- New projects initialized with native ontology by default
- Evidence: Clean external identity, BMAD origins secondary/internal only

### M.4 Mapping Table: BMAD Mechanism → Battle-Map-Native Layer

| BMAD Mechanism | Maps To | Battle-Map-Native Layer | Notes |
|----------------|---------|------------------------|-------|
| `bmad-prd` workflow | Project Goal + Complete Functions Definition | Layer 2 (Semantic DB) + Layer 1 (UI) | PRD writing becomes "Shaping" action class |
| `bmad-spec` derivation | Milestones + Evidence Contracts | Layer 2 (Semantic DB) | Spec becomes milestone definition +验收标准载体 |
| `bmad-architecture` spine | Regional Invariants + AD-n Stability | Layer 2 (Semantic DB) | Architecture decisions stored as adopted structure |
| `bmad-build` implementation | Function Implementation Work | Layer 6 (Execution Runtime) | Build workflow = Implement action class worker |
| `bmad-build-auto` unattended | Autonomous Implementation | Layer 6 (Execution Runtime) | Same deterministic control-plane discipline, worker may be LLM-driven |
| `bmad-retrospective` | Narrative Entry + Epic Closure | Layer 3 (Weaving) + Layer 2 (Semantic DB) | Retro verdict becomes causal narrative entry |
| BMAD Loop orchestrator | Advancement Coordinator | Layer 4 (Command Engine) | Coordinator reads Map, selects action, dispatches worker |
| `bmad-correct-course` | Reconciliation Transaction | Layer 4 (Command Engine) | Correct course implements adoption/candidate protocol |
| Memlogs | Narrative Foundation | Layer 3 (Weaving) | Memlog entries become narrative fragment inputs |
| Stories.yaml | Story Order + Bootstrap Context | Layer 2 (Semantic DB) | Story inventory feeds bootstrap compilation |
| `agents.md` | Session Continuity Rules | Layer 5 (Composable Runtime) | Continuity policies bind to session identity manager |

**Principle:** BMAD mechanisms inform battle-map-native design but don't dictate external identity. Users get same quality guarantees without needing BMAD terminology.

### M.5 Compatibility Contract Guarantees

**For teams adopting Battle Map gradually:**
- All existing BMAD artifacts remain readable and valid
- Weaving can ingest existing PRD/SPEC/ARCH/eopic records without recreation
- Export function generates BMAD-compatible files from Project Map DB
- `bmad-*` skill invocations continue working via compatibility shim
- Existing workflows don't break; Battle Map augments rather than replaces initially

**Migration incentive:** Teams stay on BMAD as-is if sufficient. Move to Battle Map when they want better project-shape visibility, automatic weaving, and improved coordination without BMAD vocabulary exposure.

---

## Summary: What is Battle Map?

Battle Map is a project-level semantic system presenting projects as **goals → functions → regions → milestones → structure → frontier → evidence → unknowns**. Users interact through a single Project Map interface, dispatch work by selecting action classes, and watch autonomous workers execute through deterministic control-plane disciplined workflows (frozen input snapshot + auditable protocol steps + explicit terminal state, worker internal cognition may be LLM-stochastic).

Internally, the system absorbs BMAD's durable mechanisms (persona patterns, workflow protocols, durable handoffs, authority boundaries, independent review, deterministic execution discipline) but digests them into generic composable parts. Users don't need BMAD knowledge to benefit from Battle Map's project-shape visibility, evidence discipline, and structural clarity.

The seven-layer architecture separates Concerns cleanly:
- **Layer 7 (Sources)**: Native systems stay authoritative for their domain
- **Layer 6 (Runtime)**: Deterministic control-plane workflows with frozen snapshots + auditable state transitions + explicit terminal states; worker internal cognition may be LLM-stochastic
- **Layer 5 (Cognition)**: Composable roles assembled from persona/authority/skill/handoff/session
- **Layer 4 (Command)**: Coordinator selects actions, compiles bootstraps, escalates appropriately
- **Layer 3 (Weaving)**: Background pipeline extracting facts, associating evidence, synthesizing narrative
- **Layer 2 (Semantic DB)**: Single source of truth for stable project semantics
- **Layer 1 (Experience)**: Battle-map-native UI projecting current state and next-move rationale

Five Stage-1 behaviors realized as cross-cutting properties, not modules: persistent structure cognition, explicit error classification, composite verification, unknown boundaries, justifiable investment judgment.

Evolution follows null hypothesis discipline: preserve mature mechanisms unless observed friction proves change worthwhile. Candidate deltas start presuming "no change needed"; promotion requires demonstrated material benefit justifying added complexity.

This is the complete Battle Map system. To deploy it: initialize a project, open Project Map, select first action from recommended frontier, watch worker execute, observe weaving associate findings, review next-move rationale, repeat. BMAD mechanisms work internally but remain invisible unless you choose to explore them.

---

**Status:** Draft. Pending structural reviewer gate evaluating system completeness and authority consistency. Chief Engineer approval required before advancing to UX specifications and implementation planning.
