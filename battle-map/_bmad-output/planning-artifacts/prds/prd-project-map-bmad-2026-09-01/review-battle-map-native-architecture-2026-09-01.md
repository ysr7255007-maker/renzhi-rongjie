# Battle Map Native Architecture Review Package

**Purpose**: Complete target architecture before rewriting the full PRD.  
**Status**: Review gate — Chief Engineer must approve this seven-piece package before PRD rewrite begins.

---

## 1. Complete Battle-Map-Native Target Architecture Diagram

```mermaid
graph TB
    subgraph LAYER7["LAYER 7: SOURCE / ADAPTER LAYER<br/>Unified read interface to all execution sources"]
        BMAD["Standard BMAD artifacts adapter<br/>PRD/Spec/ARCH/Sprint/Retro files<br/>Compatible internal path only"]
        HARNESS["Harness/IDE session persistence DB"]
        GIT["Git repository (commits/diffs)"]
        TESTS["Test/runtime logs & results"]
        REVIEWS["Review evidence (code review, retro)"]
        ADAPTERS["Adapters → canonical event stream<br/>incremental delta read, not full history"]
    end

    subgraph LAYER6["LAYER 6: EXECUTION / VERIFICATION RUNTIME<br/>Selected work executes here; returns to sources"]
        WORKER_RUNTIME["Agent/Harness worker session<br/>Plan/Todo remains worker-local<br/>Fresh context at responsibility boundaries"]
        VERIFY_LOOP["Deterministic verification loop<br/>implement→verify→review→commit<br/>No Map influence inside inner loop"]
        EVIDENCE_RETURN["Evidence returns to native sources:<br/>Git commit → Git<br/>Test result → Test system<br/>Review findings → Review system"]
    end

    subgraph LAYER5["LAYER 5: COGNITIVE RUNTIME — OUR OWN ROLE/SKILL/WORKFLOW MODEL<br/>NOT a copy of BMAD job titles"]
        ROLE_MODEL["Role Persona Model<br/>persistent cognitive stance +<br/>authority scope +<br/>permitted skill bundle +<br/>handoff contract +<br/>session identity"]
        SKILLS_BUNDLE["Skills = reusable capabilities<br/>Role may use several skills;<br/>skill may serve multiple roles"]
        WORKFLOW_PROTOCOL["Workflow = multi-round interaction protocol<br/>Not identical to role or skill"]
        HANDOFF_CONTRACT["Durable handoff contracts:<br/>project-DB-backed canonical facts/snapshots<br/>+ generated/frozen artifact projections<br/>at human/agent boundaries"]
        CONTINUITY_RULES["Session continuity by responsibility:<br/>fresh context at true responsibility<br/>or independent-review boundaries"]
    end

    subgraph LAYER4["LAYER 4: ADVANCEMENT / COMMAND ENGINE<br/>Reads Project Map DB, chooses next ACTION CLASS"]
        FRONTIER_ANALYSIS["Analyzes frontier, blockers,<br/>structural risk, evidence/unknown boundaries"]
        ACTION_SELECTOR["Selects next action class from policy:<br/>① Continue discovery<br/>② Resolve product intent<br/>③ Structure design<br/>④ Risk probe<br/>⑤ Decompose<br/>⑥ Implementation<br/>⑦ Join/system verification<br/>⑧ Correct structure<br/>⑨ Retrospective/synthesis<br/>⑩ Pause/defer<br/>⑪ Maturity/investment transition"]
        BOOTSTRAP_COMPILER["Compiles one-click bootstrap context:<br/>who/what role needed<br/>current project shape<br/>current region/function<br/>goal, upstream/downstream<br/>relevant evidence/unknowns<br/>authoritative artifacts/DB views<br/>allowed skills<br/>feedback/escalation contract"]
        ROUTINE_AUTO["Routine/reversible advancement is autonomous"]
        ESCALATION_GATE["Genuine owner-level semantic/irreversible/high-cost decisions escalate"]
    end

    subgraph LAYER3["LAYER 3: PROJECT WEAVING / AUTO-ASSOCIATION LAYER<br/>NEW layer explicitly missing in previous PRD"]
        TRIGGER_DISPATCH["Triggers (continuous or event-driven):<br/>• Workflow/turn/session completion<br/>• Durable artifact changes<br/>• Git/test/review/runtime events<br/>• Optional: time/tool-count thresholds"]
        INCREMENTAL_READ["Incrementally reads ONLY new deltas<br/>from source systems (Layer 7)"]
        FACT_EXTRACTION["Extracts stable project facts:<br/>decisions, evidence, unknowns,<br/>route changes, structural implications"]
        AUTO_ASSOCIATION["Auto-associates extracted facts to:<br/>map nodes/edges/milestones + source refs<br/>Strong/deterministic links → committed derived facts<br/>Semantic/uncertain links → candidate associations with provenance"]
        NARRATIVE_WEAVER["Weaves causal Project Narrative:<br/>prior judgment → triggering evidence/event<br/>→ new judgment → impact/route change<br/>Narrative is semantic expansion of map,<br/>not separate diary"]
        CANDIDATE_OUTPUT["Outputs:<br/>candidate map deltas<br/>association updates<br/>narrative fragments<br/>NOT route selection decisions"]
    end

    subgraph LAYER2["LAYER 2: PROJECT MAP CORE / PROJECT SEMANTIC DATABASE<br/>Primary durable store for project-level semantics"]
        STORE_PROJECT_GOAL["Project goal (终极结果定义)"]
        STORE_COMPLETE_FUNCTIONS["Complete functions (完整功能库)"]
        STORE_MILESTONES["Milestones (里程碑定义 + 可观察证据标准)"]
        STORE_REGIONS["Regions / Functional zones"]
        STORE_DEPENDENCIES["Dependency/parallel/join relations"]
        STORE_ADOPTED_VERSIONS["Adopted/candidate map versions (versioned)"]
        STORE_MATURITY_FRONTIER["Region maturity + active frontier state"]
        STORE_UNKNOWNS["Explicitly tracked unknowns + coverage gaps"]
        STORE_EVIDENCE_REFS["Evidence references + coverage metrics<br/>(references back to Layer 7 sources)"]
        STORE_DECISIONS["Decisions with rationale/evidence"]
        STORE_STRUCTURE_HISTORY["Structural-change history (causal)"]
        STORE_NARRATIVE_ENTRIES["Causal narrative entries (layer 3 output)"]
        STORE_CURRENT_ACTIONS["Current/project actions"]
        STORE_ROLE_SESSION_BINDINGS["Role-session bindings (who is working on what)"]
        STORE_AUTO_ASSOCIATIONS["Automatic associations (strong + candidate)"]
        NOTE_DB_NOT_RAW_HISTORY["DO NOT blindly copy all raw execution history into this DB.<br/>Native sources remain physical source-of-truth.<br/>This stores stable semantics + source refs + extracted facts."]
    end

    subgraph LAYER1["LAYER 1: BATTLE MAP EXPERIENCE / PROJECTION LAYER<br/>Visual/web/CLI views are replaceable projections"]
        GLOBAL_VIEW["Global project map<br/>project goal visualization"]
        REGION_DRILLDOWN["Region/map drilldown interfaces"]
        CURRENT_FRONTIER["Current frontier display<br/>blocked/unlocked routes"]
        JOINS_DISPLAY["Join points and汇合点 visibility"]
        MILESTONE_EVIDENCE["Milestone/evidence state view"]
        CANDIDATE_CHANGES["Candidate structural changes presentation"]
        HISTORY_VIEW["History of structural changes"]
        CAUSAL_NARRATIVE["Causal project narrative browsing"]
        EVIDENCE_DRILLDOWN["Evidence drilldown to source refs"]
        NEXT_MOVE_RATIONALE["Current recommended next move + rationale"]
        VIEWS_PROJECTIONS["Views are projections:<br/>Web UI · CLI · API · Other visualizations<br/>Replaceable; outward identity = Battle Map system"]
    end

    LAYER7 -->|canonical events| LAYER3
    LAYER7 -->|native source access| LAYER6
    LAYER3 -->|candidate deltas + narrative| LAYER2
    LAYER2 -->|project state| LAYER4
    LAYER2 -->|semantic queries| LAYER1
    LAYER4 -->|dispatch command| LAYER5
    LAYER5 -->|worker execution| LAYER6
    LAYER6 -->|evidence return| LAYER7
    LAYER7 -->|adapter read| LAYER3
    LAYER2 <--|cross-source unified query/views| LAYER7

    style NOTE_DB_NOT_RAW_HISTORY fill:#ffe0b2
    style CANDIDATE_OUTPUT fill:#e3f2fd
    style ESCALATION_GATE fill:#fff3e0
```

**Data/Control Loop (完整数据/控制流):**
```
User opens Battle Map → sees project goal + complete functions + current frontier + evidence coverage
     ↓
Advancement Engine reads Project Map DB → analyzes frontier/blockers/risks → selects next action class
     ↓
Compiles bootstrap context → dispatches appropriate Role/Session to execute work
     ↓
Worker executes in Harness/IDE runtime → produces reality (code/tests/docs) → evidence returns to native sources
     ↓
Weaving Layer triggers (event-driven or continuous) → incrementally reads new deltas → extracts facts → auto-associates → weaves narrative → outputs candidate map deltas
     ↓
Candidate deltas enter Map's CANDIDATE state → await validation → if accepted, refresh ADOPTED state
     ↓
Project Map DB updated → Advancement Engine sees new state → chooses next action
     ↓
Battle Map Experience layer reflects new adopted state + next move rationale → user sees updated picture
```

---

## 2. User-Facing Operational Loop

**从“打开项目地图”到“下一次行动推荐”的完整用户可见流程:**

### Step 1: Open Project Map（打开项目地图）

**User sees:**
- **项目目标**: The ultimate result the system must achieve
- **Complete functions**: All identified完整功能 and their status
- **Current frontier**: Which nodes are completed, in-progress, blocked, or unlocked
- **Evidence coverage**: For each node/path, what evidence supports its status (tests, runs, reviews, implementation)
- **Unknowns**: Explicitly marked uncovered conditions and remaining hypotheses
- **结构关系**: Serial/parallel/dependency/join relations between nodes

**No need to know:** Mary/John/Winston/Amelia, "Phase 1/2/3/4", "PRD/SPEC/ARCH" file names

---

### Step 2: Understand Shape/Front/Evidence（理解形状/前线/证据）

**User can:**
- **Browse global view** → understand overall product shape
- **Drill down into regions** → see functional zones and关卡 within
- **View current frontier** → identify which paths are ready to advance
- **Check evidence** → click any "completed" node → see supporting tests/runs/reviews/implementation
- **See unknowns** → understand what's still hypothesis vs. what has real-chain evidence
- **View causal narrative** → understand why a node was structured this way, what evidence led to it

**System provides:** Clear distinction between ADOPTED structure (currently believed) and CANDIDATE changes (proposed, pending validation).

---

### Step 3: System Chooses/Dispatches Work（系统选择/分派工作）

**Advancement Engine decides:**

Based on:
- Current frontier state (what's ready)
- Blockers (what dependencies are missing)
- Structural risk (which areas have most uncertainty)
- Evidence/unknown boundaries (where more evidence would be highest leverage)
- Owner policy (investment preferences, constraints)

**Selects ONE action class**, for example:
- `继续探索`: Run deep-recon on an uncertain dependency
- `resolve_product_intent`: Update project goal or function definition
- `structure_design`: Architecture spine update for a region
- `risk_probe`: Build minimal complete implementation to test a hypothesis
- `decompose`: Break a功能 into actionable关卡
- `implementation`: Start正式施工 for a成熟区域
- `join_verification`: Run integration test at a汇合点
- `correct_structure`: Major structural revision due to failed hypothesis
- `retrospective/synthesis`: Close an epic/region with full evidence review
- `pause/defer`: Wait for external condition or more evidence

**Compiler generates one-click bootstrap context** including:
- Who/what role is needed
- Current project shape and region context
- Goal and upstream/downstream
- Relevant evidence and unknowns
- Authoritative artifacts/DB views to reference
- Allowed skills and tools
- Feedback/escalation contract

**Dispatches to appropriate Role Session.**

---

### Step 4: Worker Produces Reality（工作者产生现实）

**Worker executes:**
- In Harness/IDE runtime (can be AI agent or human)
- Accesses current project shape from Project Map DB
- Follows bootstrap context (goal, region, evidence, constraints)
- Produces: code changes, test results, documentation, decision records
- Returns evidence to **native source systems** (Git, test runners, review tools)

**Important:** Local Plan/Todo remains worker-local; Map does not become a micro-task manager.

---

### Step 5: Weaving/Auto-Association（编织/自动关联）

**Weaving Layer triggers** (any of):
- Workflow/turn/session completion
- Durable artifact changed (new spec, new architecture decision)
- Git push / test run / review completed
- Optional: time threshold or tool-call count threshold

**Performs:**
1. **Incremental read**: Only NEW deltas from source systems (not full history re-read)
2. **Fact extraction**: Identify stable facts—decisions made, evidence obtained, unknowns resolved/changed, structural implications
3. **Auto-association**: Link extracted facts to:
   - Map nodes/edges/milestones where relevant
   - Source references (Git commit SHA, test ID, review link)
4. **Confidence levels**:
   - Strong/deterministic links → committed as **derived facts** in Project Map DB
   - Semantic/uncertain links → stored as **candidate associations** with provenance until validated
5. **Narrative synthesis**: weave causal chain—`prior judgment → triggering event → new judgment → impact on route/structure`
6. **Output candidate deltas**: Proposed map updates, association additions, narrative fragments

**Does NOT decide project route**—that belongs to Advancement Engine. Weaving only informs.

---

### Step 6: Map/Narrative Update（地图/叙事更新）

**Candidate states merge into Project Map DB:**
- New evidence updates evidence coverage metrics
- New decisions recorded in decision store
- Structural changes enter CANDIDATE version first
- Narrative entries appended to causal history

**If candidate becomes adopted** (via validation workflow or owner approval):
- ADOPTED map version advances
- Frontier may shift (new nodes unlock, new blocks appear)
- Maturity states update for completed regions

**All changes retain causal traceability:** who, when, what evidence, what rationale.

---

### Step 7: Next Move Rationale（下一步依据）

**Advancement Engine re-evaluates** with updated DB state:
- What is now ready to proceed?
- What new blockers emerged?
- Where should investment focus next?

**Updates "current recommended next move"** in Battle Map Experience:
- Shows chosen action class
- Explains rationale based on:
  - Frontier state
  - Structural risk reduction potential
  - Evidence gap closure value
  - Owner policy alignment

**User sees:** Clear statement like:
> "Recommended: Begin implementation for [Function X Region Y]
> Rationale: Evidence coverage ≥80% on critical paths; no blocking dependencies; high-value capability unblock after [previous function] completed; remaining unknowns limited to performance scale."

**Loop repeats** from Step 3.

---

## 3. Internal Cognitive-Runtime Model

**吸收 vs. 不复制：Our Role/Persona/Skill/Workflow/Handoff model**

| Aspect | Absorbed from Standard BMAD/BMAD Loop | Intentionally NOT copied / Battle-Map-Native Design |
|--------|---------------------------------------|-----------------------------------------------------|
| **Persistent role persona** | ✓ Yes — roles carry persistent cognitive stance across sessions | ✗ Not "Mary/John/Winston/Amelia" job titles<br/>✓ Generic **Role Persona Model**: cognitive stance + authority scope + skill bundle + handoff contract |
| **Role-vs-skill separation** | ✓ Yes — skills are reusable capabilities; roles compose skills | ✗ No fixed PM/Architect/Dev/etc. roles<br/>✓ Battle-Map-native roles justified by method needs (see below) |
| **Multi-round workflow protocols** | ✓ Yes — workflows define multi-turn interaction patterns | ✗ No "Step 1/2/3/4/5" hardcoded sequences per role<br/>✓ Flexible protocols driven by action class and region maturity |
| **Durable intermediate handoff artifacts** | ✓ Yes — boundaries need stable contracts | ✗ No forest of Markdown files (SPEC.md, ARCHITECTURE-SPINE.md, etc.) as primary storage<br/>✓ Project-DB-backed canonical facts/snapshots + generated/frozen artifact projections at human/agent boundaries |
| **Explicit authority boundaries** | ✓ Yes — clear ownership of product definition, invariants, implementation | ✗ Not tied to specific documents ("PRD authority")<br/>✓ Authority mapped to semantic layers: Project Goal (owner), Functions/Regions (shared), Implementation (worker) |
| **Fresh independent review** | ✓ Yes — cognitive isolation where useful for validation | ✗ No mandatory adversarial subagent at every boundary<br/>✓ Independent verification scaled to risk; automatic at join points and region closure |
| **Feedback/correct-course semantics** | ✓ Yes — structural errors require structural correction | ✗ Not implemented as separate "Correct Course workflow"<br/>✓ Integrated into weaving layer + candidate deltas flow |
| **Deterministic implementation inner loop** | ✓ Yes — implement→verify→review→commit without orchestration interference | ✓ Preserved exactly as deterministic queue semantics inspired by BMAD Loop<br/>✗ No Map/LLM influence inside inner loop; queue policy owned by executor |
| **Session continuity rules** | ✓ Yes — continuity by responsibility, fresh context at true boundaries | ✗ Not "same Qoder session for same role"<br/>✓ Continuity based on responsibility chains; natural breaks at responsibility/verification boundaries |
| **Source-of-truth discipline** | ✓ Yes — execution evidence lives in native systems (Git, tests, logs) | ✗ Not all history ingested into project DB<br/>✓ Project DB stores stable semantics + source refs + extracted facts; raw history stays in native sources |

**Proposed Battle-Map-Native Roles/Jobs Families** (only if justified by method):

| Role Family | Responsibility | Authority Scope | Skills May Use | Handoff Contract |
|-------------|---------------|-----------------|----------------|------------------|
| **Advancement Coordinator / Chief Engineer** | Reads Project Map DB, selects next action class, compiles bootstrap context | Dispatch authority; escalates irreversible/high-cost/meaning-laden decisions to Owner | Frontier analysis, policy evaluation, context compilation | One-click dispatch command with full context snapshot |
| **Project Shaping / Structural Cognition** | Identifies完整功能，defines regions, proposes structural hypotheses, detects drift | Structure proposal authority; requires validation before adoption | Deep recon, pattern recognition, evidence aggregation | Candidate structural delta + narrative rationale |
| **Function Implementer** | Builds正式实现 for成熟区域, writes tests, produces evidence | Implementation authority within function boundary | Coding, testing, local verification | Implemented code + test results + evidence refs |
| **Independent Verifier** | Conducts risk probes, join verification, retrospective synthesis | Validation authority; can reject claim without implementing | Adversarial review, behavior testing, aggregate analysis | Verification report + pass/fail + evidence |
| **Project Weaver** | Executes weaving layer: incremental fact extraction, auto-association, narrative synthesis | Association proposal authority; strong links auto-committed, weak links candidate | Fact extraction, semantic linking, causal reasoning | Candidate associations + narrative fragments |
| **Owner / Strategic Decision Maker** | Sets project goal, approves structural changes, makes irreversible commitments | Ultimate authority on project meaning, scope, strategy | High-level evaluation, policy setting | Approved/rejected candidate deltas + rationale |

These are **generic, responsibility-based** roles—not named after people or legacy BMAD titles. They emerge from method needs, not inherited templates.

---

## 4. Data Ownership Matrix

| Data Type | Lives In | Why Here | How Cross-References Work | Auto-Association Method |
|----------|----------|----------|---------------------------|------------------------|
| **Project Goal** | Project Map DB (Layer 2) | Stable semantic anchor for entire project | References: none upstream; downstream refs via function relationships | Initial input by Owner; revised via structural-change workflow |
| **Complete Functions** | Project Map DB (Layer 2) | Core semantic objects; visible to users | Each function refs: milestones, regions, evidence, implementation artifacts | Weaving layer extracts function definitions from planning artifacts; creates candidate nodes |
| **Milestones** | Project Map DB (Layer 2) | Observable completion criteria | Each milestone refs: evidence sources (test IDs, commit SHAs, review links) | Auto-extracted from planning docs (SPEC.md, PRD); validated against actual test results |
| **Regions / Functional Zones** | Project Map DB (Layer 2) | Grouping for scalability and parallelism | Relationships: dependencies to other regions, parent project, contained functions | Structured via function clustering; proposed as candidate, adopted via validation |
| **Dependencies / Parallel / Join Relations** | Project Map DB (Layer 2) | Determines推进顺序；critical for frontier calculation | Graph edges between nodes; edge metadata includes confidence level | Extracted from architecture decisions, implementation constraints; candidate associations start uncertain, strengthen with evidence |
| **Adopted/Candidate Map Versions** | Project Map DB (Layer 2) | Versioned state allows rollback and audit | Each version tagged with timestamp, author, rationale, evidence support | Snapshot at key transitions; candidate deltas merge into next version upon approval |
| **Region Maturity + Frontier State** | Project Map DB (Layer 2) | Drives advancement engine decisions | Derived from milestone completion, evidence coverage, join verification | Updated by weaving layer on evidence arrival; refreshed by advancement engine on dispatch |
| **Explicit Unknowns** | Project Map DB (Layer 2) | Makes uncertainty visible; prevents over-certainty | Each unknown tags: related nodes, what would resolve it, confidence level | Extracted from open questions in planning artifacts; surfaced by weaving as gaps |
| **Evidence References + Coverage** | Project Map DB (Layer 2) | Links map state to real-world validation | Points back to: Git commits, test runs, review findings, deployment logs | Weaving layer associates evidence to nodes; calculates coverage % automatically |
| **Decisions (with rationale)** | Project Map DB (Layer 2) | Maintains causal continuity of structure evolution | Each decision refs: who, when, context, evidence, alternatives considered | Extracted from meeting notes, PRD updates, architect discussions; woven into narrative |
| **Structural-Change History** | Project Map DB (Layer 2) | Audit trail for map revisions | Links old version → new version; documents reason for change | Weaving layer captures structural shifts detected via diffs or review feedback |
| **Causal Narrative Entries** | Project Map DB (Layer 2) | Semantic expansion of map; explains evolution | Chains: prior judgment → event → new judgment → impact | Generated by weaving layer; combines decision logs + evidence arrivals + structural changes |
| **Current/Project Actions** | Project Map DB (Layer 2) | Tracks ongoing work and responsibility | Links to: role session, region, expected outcome, deadline | Updated by advancement engine on dispatch; cleared on completion |
| **Role-Session Bindings** | Project Map DB (Layer 2) | Knows who is working on what | Links to: harness session ID, start time, current task | Set on dispatch; cleared on session completion or handoff |
| **Automatic Associations (Strong + Candidate)** | Project Map DB (Layer 2) | Captures inferred relationships and evidence links | Confidence level, provenance source, acceptance status | Output of weaving layer; strong links auto-committed, candidate awaits validation |
| **Raw Execution Events (Git, Tests, Logs)** | Native Sources (Layer 7) | Physical source-of-truth; not all history fits in semantic DB | Referenceable via SHAs, IDs, URLs from Project Map | Weaving layer incrementally reads deltas; extracts facts; stores refs in Project Map |
| **Harness/IDE Session Persistence** | Harness DB (Layer 7) | Complete worker context; workspace state | Linked to role-session binding in Project Map | Weaving reads session completion events; extracts decisions/artifacts produced |
| **Plan/Todo (Worker-Local)** | Worker Session (Layer 6) | Tactical task list; not project-level semantics | Not stored in Project Map unless elevated to milestone | Ignored by weaving unless promoted to formal commitment |
| **Generated Artifact Projections** | Project Map DB (Layer 2) + External Storage | Human-readable snapshots at handoff boundaries | Links back to canonical DB state; frozen at projection time | Produced on demand for human/agent boundaries; not live source |

**Cross-Source Unified Query/Vision Strategy:**
- Project Map DB maintains **indices into native sources** (commit SHAs, test IDs, review hashes)
- Incremental projection computes derived metrics (coverage %, maturity state) without full-history reread
- On-demand materialization joins raw data for drilldown (e.g., "show me all tests for Function X")
- **Never** copies entire execution history into Project Map DB; keeps semantic core lean while preserving traceability

---

## 5. Project Weaving Design

**Triggers (事件触发或连续模式):**

| Trigger Type | When Fires | What Read | Latency Expectation |
|--------------|-----------|-----------|---------------------|
| **Workflow/turn/session completion** | Agent/human session ends | New artifacts produced (specs, plans, decisions), evidence generated | Immediate (within seconds of session close) |
| **Durable artifact change** | File modified/written in planning artifacts | Full artifact diff; identifies new/changed sections | Near-real-time (file watcher) |
| **Git push/commit** | New commit pushed to repo | Commit message, files changed, diff content | Sub-minute (webhook) |
| **Test run completed** | Test suite finishes | Results (pass/fail), coverage report, execution logs | Sub-minute (test runner webhook) |
| **Review completed** | Code review/retr ospective finishes | Findings, verdicts, action items | Sub-minute (review tool webhook) |
| **Time threshold (optional)** | Every N minutes/hours | Delta since last weave cycle | Configurable (e.g., every 15 min) |
| **Tool-count threshold (optional)** | After N tool calls/actions | Recent actions log | Configurable (e.g., every 50 actions) |

**Incremental Read Strategy:**
- Maintain **cursor/checkpoint** per source (last processed commit SHA, last event ID)
- On trigger, request **only new deltas** since last cursor
- Parse and normalize into **canonical event schema**
- Skip already-processed events (idempotent)

**Fact Extraction (提取稳定项目事实):**

| Fact Category | Examples | Extraction Heuristics | Confidence Level |
|---------------|----------|----------------------|------------------|
| **Decisions** | "Chose PostgreSQL over MongoDB", "API version 2 required" | Keywords: decided, chose, will use, confirmed; appears in specs/architecture | Strong if explicit; candidate if implicit |
| **Evidence Obtained** | "Test X passed", "Integration verified", "Review approved" | Test result webhooks, commit messages referencing verification, review completion events | Strong if machine-readable; candidate if human language |
| **Unknowns Resolved** | "Discovered dependency on auth service", "Performance requirement clarified" | Open questions section empties; new constraints added to artifacts | Strong if matched to prior unknown |
| **Route Changes** | "Function A now depends on B", "Two paths merged here" | Dependency graph diffs; architectural decision changes | Candidate initially; strengthens with implementation evidence |
| **Structural Implications** | "This change affects three downstream functions", "New汇合点 required" | Cross-reference analysis; scope-of-change calculation | Candidate; requires validation |

**Auto-Association Rules (自动关联规则):**

```
FOR EACH extracted fact F:
    IF F matches known node/nedge/milestone pattern P:
        CREATE association A(F, P)
        A.confidence = high IF pattern match deterministic (exact ID, explicit ref)
        A.confidence = medium IF semantic similarity (name match, context aligned)
        A.confidence = low IF speculative (inferred, needs validation)
        
        IF A.confidence == high:
            COMMIT A to Project Map DB (strong link)
            UPDATE node status accordingly
        ELSE:
            STORE A as CANDIDATE association with provenance
            FLAG for human/validation review if medium confidence
```

**Narrative Synthesis (因果叙事编织):**

Pattern:
```
[Time T1] Prior Judgment J1: "Function X can be built independently"
    ↓
[Time T2] Triggering Event E: "Implementation revealed hidden dependency on Y"
    ↓
[Time T3] New Judgment J2: "X and Y must be developed in tandem; split was wrong"
    ↓
[Time T4] Impact/Route Change: "Added cross-dependency; delayed Z; reshaped timeline"
```

**Algorithm:**
- Track **state transitions** for each node/region
- Link transition to **triggering events** (fact extraction output)
- Record **judgment change** (before → after)
- Compute **impact propagation** (affected downstream nodes)
- Store as **narrative entry** in Project Map DB
- Present as **chronological thread** in Battle Map Experience

**Example Narrative Entry:**
> **节点**: Function A 用户认证模块
> **T1 (2026-08-01)**: 初始假设—"认证功能可以独立开发，不依赖其他服务"
> **T2 (2026-08-15)**: 实现证据——发现必须与权限服务共享状态
> **T3 (2026-08-16)**: 结构调整——标记 A 与权限服务为强耦合，需并行开发
> **T4 (2026-08-17)**: 路线影响——原计划串行改为并行; Z 功能延迟 2 周
> **证据来源**: Git commit abc123 (impl/src/auth.rs), Review finding #47

**Candidate Map Delta Output:**

Weaving layer does NOT make route decisions; only proposes:
- **Node additions**: New功能 discovered
- **Node deletions**: Obsolete功能 removed
- **Relation updates**: Dependency direction/strength changed
- **Milestone adjustments**: Completion criteria refined
- **Evidence gap flags**: Areas needing more validation
- **Narrative fragments**: Causal threads to append

These go into **CANDIDATE state** in Project Map DB, awaiting validation (via review workflow, owner approval, or implementation confirmation).

**Non-Interference with Route Selection:**

- Weaving only **feeds information** to Advancement Engine
- Does **NOT** propose next action class
- Does **NOT** override owner/advancement decisions
- Acts as **observational layer** producing structured observations

---

## 6. Standard BMAD as Internal Provider Path

**How Standard BMAD executes UNDER Battle Map Native System during brownfield transition:**

### Integration Pattern: BMAD as Compatibility Mode

```
┌───────────────────────────────────────────────────────┐
│          Battle Map Native System (Outer Identity)     │
├───────────────────────────────────────────────────────┤
│                                                       │
│  Advancement Engine → selects "BMAD-compatible path" │
│         ↓                                             │
│  Role Session → uses BMAD-style roles (Mary/John...) │
│         ↓                                             │
│  Skill Bundle → invokes bmad-prd, bmad-spec, etc.    │
│         ↓                                             │
│  Workflow → follows BMAD step sequence                │
│         ↓                                             │
│  Artifacts → writes SPEC.md, ARCHITECTURE-SPINE.md…  │
│         ↓                                             │
│  Weaving Layer → reads BMAD artifacts → extracts     │
│                  → maps to Project Map semantic nodes │
│         ↓                                             │
│  Project Map DB ← adopted/candidate updates           │
│                                                       │
└───────────────────────────────────────────────────────┘
```

### Mapping: BMAD Mechanisms → Battle-Map-Native Layers

| BMAD Mechanism | Absorbed Into Which Layer/Contract | Migration Path |
|----------------|------------------------------------|----------------|
| **bmad-prd** | Invoked by Project Shaping role → Project Goal + Complete Functions nodes | Phase-out gradual; goal/functions become native objects |
| **bmad-spec** | Invoked by Function Implementer → Milestones + Evidence refs | Migrates to milestone definition in Project Map DB |
| **bmad-architecture** | Invoked by Project Shaping → Regions + Dependencies | Arch spine becomes regional invariant store |
| **bmad-build** | Worker execution mode under Function Implementer | Direct mapping; implementation continues |
| **bmad-retrospective** | Invoked by Independent Verifier at region closure → Narrative entry | Retro verdict feeds narrative synthesis |
| **bmad-correct-course** | Weaving layer detects structural shifts → candidate delta → validation | Integrated into candidate flow |
| **BMAD Loop** | Deterministic execution runtime (preserved exactly) | Already native; no migration needed |
| **Memlog** | Extracted facts → decision store + narrative | Memlog becomes source adapter for weaving |
| **Sprint-status.yaml** | Read by weaving → updates Current Actions + Frontier | Sprint status consumed as event source |

### Brownfield Transition Phases:

**Phase 1: Dual Operation (Current)**
- Battle Map Experience layer shows BMAD project
- BMAD skills run as normal; weaving extracts from their artifacts
- Project Map DB accumulates semantic state alongside BMAD file tree
- Users see BMAD terminology; battle-map experience adds overlays

**Phase 2: Semantic Unification**
- BMAD artifacts remain but become compatibility sources
- Project Map DB becomes single source of truth for semantics
- Advanced UI offers "battle-map native view" replacing BMAD filenames
- Gradual migration: function nodes replace story lists; milestones replace spec frontmatter

**Phase 3: Native Default**
- New projects default to Battle Map native ontology
- BMAD skills仍可 invoke as compatibility path for existing workflows
- Project Map DB fully detached from BMAD file structure
- User-visible vocabulary entirely battle-map-native (no Mary/John/phase names)

### Compatibility Contracts:

When BMAD artifacts are written:
- Weaving layer watches `*.md` files in planning artifacts folder
- On write event: parses YAML frontmatter, extracts kernel fields
- Maps to Project Map semantic objects:
  - `SPEC.md` → Milestone + Capabilities
  - `ARCHITECTURE-SPINE.md` → Regional invariants
  - `sprint-status.yaml` → Current Actions + Frontier
- Creates strong associations; commits updates to Project Map DB

When Battle Map Native system writes:
- Generates canonical snapshots (JSON-backed)
- Optionally exports to BMAD-format Markdown if BMAD path requested
- Bi-directional sync via weaving layer

---

**Architecture Review Package Complete.**

**Required Chief Engineer Approval Before PRD Rewrite:**
1. ✓ Seven-layer architecture diagram complete and correct?
2. ✓ User-facing operational loop accurately describes full cycle?
3. ✓ Cognitive-runtime model correctly specifies absorbed vs. not-copied?
4. ✓ Data ownership matrix accurate? Is weaving layer explicitly defined?
5. ✓ Standard BMAD integration path clear and non-authoritarian?
6. ✓ Battle Map native ontology (functions, regions, milestones, joins) central—not BMAD concepts?

**Do NOT Finalize current PRD. Stop here and await approval to begin full PRD rewrite around this battle-map-native architecture.**
