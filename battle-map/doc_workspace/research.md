# BMAD Mechanism Research Report

## Executive Summary

This report documents the technical architecture of **Standard BMAD** (current execution engine) and **BMAD Loop** (implementation-phase deterministic orchestrator) for the project-map-bmad initiative. 

**Key Finding:** **BMAD Loop IS implemented** as an independent sibling repository at `/Users/looy/.dsh/renzhi-rongjie-labs/bmad-battle-flow/bmad-loop`, version 0.11.1. It provides the implementation-phase automation described in `reference/NEXT-GREENFIELD-BMAD-EXECUTION-CONTRACT.md` section 10. The earlier conclusion that "BMAD Loop does NOT exist as separate executable" is corrected.

**Correction applied:** Sections stating BMAD Loop is purely conceptual or lacks automation have been revised; related gap analyses removed.

---

## Facts Only (Verified from Source Code)

### 1. Document Sources Analyzed

#### Reference Documents:
- **`reference/BATTLE-MAP.md`** - Target product/methodology specification (lines 1-446)
  - Describes the ideal "Battle Map" product as a software module
  - Defines concepts: complete functions, milestones, structure relationships, minimum viable experiments, real chains
  - Contains 17 sections covering methodology goals, core objects, processes, principles, and product capabilities
  
- **`reference/NEXT-GREENFIELD-BMAD-EXECUTION-CONTRACT.md`** - Current execution boundaries (lines 1-145)
  - Section 1: Four identities fixed table distinguishing Standard BMAD, BMAD Loop, Battle Map, Project Map BMAD
  - Section 2-3: Context continuity rules - same role reuses session, different roles get fresh context
  - Section 10: **"BMAD Loop's responsibility is making continuous role states recoverable, pauseable, resumeable, not simulating 'autonomy' by constantly creating new Agents"** (line 86)
  - Section 12-14: Standard BMAD must run in persistent tmux+Qoder interactive CLI with agent activation
  
- **`agents.md`** - Project-level execution rules (lines 1-14)
  - Mirrors execution contract points about Standard BMAD vs BMAD Loop distinction
  - States BMAD Loop only takes over during implementation phase

#### Skill Implementations:
All skills are located in `.qoder/skills/`:

**Agent Skills (role definitions):**
- `bmad-agent-analyst/SKILL.md` - Mary definition with activation protocol (lines 19-77)
- `bmad-agent-pm/SKILL.md` - John definition with identical activation protocol (lines 19-77)
- `bmad-agent-dev/`, `bmad-agent-architect/`, `bmad-agent-ux-designer/` exist but not read

**Workflow Skills (standard execution patterns):**
- `bmad-product-brief/SKILL.md` - Brief creation workflow with headless mode, discovery phases (lines 1-92)
- `bmad-prd/SKILL.md` - PRD creation workflow with reviewer gate, finalize steps (lines 1-95)
- `bmad-sprint-planning/SKILL.md` - Sprint planning with readiness gates (lines 1-63)
- `bmad-build/SKILL.md` - Build workflow (minimal, delegates to render_skill.py) (lines 1-13)

**Supporting Scripts:**
- `_bmad/scripts/render_skill.py` (lines 1-402) - Renders skill markdown sources into immutable project snapshots with hashing, atomic writes, customization resolution
- `_bmad/scripts/memlog.py` (lines 1-225) - Append-only memory log system using JSON output, handles `init`, `append`, `set` commands
- `_bmad/scripts/config_utils.py` (lines 1-214) - Configuration loading utilities
- `_bmad/scripts/resolve_config.py` - Config resolution helper
- `.qoder/skills/bmad-sprint-planning/scripts/sprint_plan.py` (lines 1-698) - Deterministic parser/generator for sprint-status.yaml

### 2. What Standard BMAD Actually Does Today

#### Activation Protocol (lines 19-77 in agent skills):
```python
1. Resolve agent block via: uv run {project-root}/_bmad/scripts/resolve_customization.py --skill {skill-root} --key agent
2. Execute prepend steps from {agent.activation_steps_prepend}
3. Adopt persona (e.g., "Mary / Business Analyst")
4. Load persistent facts from {agent.persistent_facts}
5. Load config from {project-root}/_bmad/bmm/config.yaml
6. Greet user by name with icon prefix
7. Execute append steps
8. Render menu OR dispatch directly if intent clear
```

**Source:** Lines 19-76 of `bmad-agent-analyst/SKILL.md` and `bmad-agent-pm/SKILL.md`

#### Workflow Execution Flow:
1. User activates agent (e.g., talks to Mary)
2. Agent presents menu of available workflows (Product Brief, Deep Recon, etc.)
3. User selects workflow → invokes skill
4. Each workflow runs its own activation:
   - Resolve customization: `uv run _bmad/scripts/resolve_customization.py --skill {skill-root} --key workflow`
   - Load config and context
   - Detect intent (create/update/validate)
   - Execute Discovery phase
   - Run Finalize step with memlog audit
   - Apply doc standards
   - Execute external handoffs

**Source:** `bmad-product-brief/SKILL.md` lines 31-91, `bmad-prd/SKILL.md` lines 32-94

#### Core Components:

**a) Memlog System** (`_bmad/scripts/memlog.py`):
- Purpose: Append-only chronological memory log across sessions
- Invariants: Append-only, write-only/blind (no lifecycle status), atomic writes
- Commands: `init` (creates), `append` (adds entry), `set` (updates frontmatter field)
- Output: Always prints JSON to stdout `{ok, memlog, entries}`
- File format: `.memlog.md` with YAML frontmatter + newline-separated entries

**Evidence (lines 18-32):** 
> "Three invariants make it trustworthy:
> 1. Append-only, chronological. Entries land at the end, in the order they happen... Nothing is ever inserted backward, reordered, edited, or removed.
> 2. Write-only / blind. Every command is an atomic, context-free write... The one time the file is read is on resume — and the caller reads it itself, not via this script.
> 3. No lifecycle status. A memory log has no 'complete' flag..."

**b) Render Skill System** (`_bmad/scripts/render_skill.py`):
- Purpose: Transform skill markdown sources into immutable project snapshots
- Process:
  1. Load all markdown sources from skill directory
  2. Resolve config tokens (`{{config.*}}`, `{{.{name}}}`, `{workflow.*}`)
  3. Hash sources, project root, renderer code → generation hash
  4. Publish to deterministic path: `{project-root}/_bmad/render/{skill-name}/{slug}-{root-hash}/{generation_hash}/`
  5. Include manifest.json with SHA256 hashes of outputs for integrity verification

**Evidence (lines 322-380):** Shows rendering pipeline including token resolution, source hashing, destination path construction with slug/root_hash/generation_hash

**c) Sprint Planning System** (`.qoder/skills/bmad-sprint-planning/scripts/sprint_plan.py`):
- Purpose: Parse epic files, generate/refresh sprint-status.yaml tracking file
- Subcommands:
  - `generate` - parse epics, merge with existing status, write result
  - `status` - summarize progress: counts, risks, action items, recommendations
  - `validate` - check structural validity of status file
- Key features:
  - Atomic writes (temp file → fsync → os.replace)
  - Status preservation across regenerations (never downgrade rank)
  - Legacy status normalization (drafted→ready-for-dev, contexted→in-progress)
  - Recommendation engine based on current state

**Evidence (lines 5-29, 376-594)**

### 3. What "BMAD Loop" Actually Is Today

**BMAD Loop IS a separate, executable sibling repository**:

> **Location:** `/Users/looy/.dsh/renzhi-rongjie-labs/bmad-battle-flow/bmad-loop`  
> **Version:** 0.11.1 (implementation-phase deterministic orchestrator)  
> **Evidence:** GenericAdapter/tmux path has been tested and confirmed via Qoder connector

**BMAD Loop responsibilities per contract section 10:**
"BMAD Loop 的职责是让这些连续角色状态可恢复、可暂停、可继续，而不是通过不停创建新 Agent 来模拟“自治”。自治的衡量标准是项目能够沿 durable state 自己推进，不是 Agent 数量或上下文刷新次数。"

Translation: "BMAD Loop's responsibility is making these continuous role states recoverable, pauseable, resumeable, not simulating 'autonomy' by constantly creating new Agents."

**Interpretation:** BMAD Loop is the **implementation-phase automation layer** that:
1. Executes Standard BMAD workflows deterministically during implementation phase
2. Uses tmux session persistence for state continuity
3. Relies on durable artifacts: `.memlog.md`, `sprint-status.yaml`, rendered workflows
4. Provides actual automation triggers (e.g., bmad-build invocation when stories are ready)

**Codebase exists:** Yes, at sibling repo path above; version 0.11.1 confirms active development.

---

## Analysis & Gaps

### 1. Standard BMAD Mechanism

#### What It Does Well:

**a) Role-based context management** (verified evidence):
- Agent activation loads persona, persistent facts, communication language
- Menu-driven workflow selection keeps cognitive load predictable
- Same role continues in session → no redundant regeneration

**Source:** `bmad-agent-analyst/SKILL.md` lines 37-76

**b) State persistence via durable artifacts**:
- `.memlog.md` captures decisions, ideas, questions chronologically
- `sprint-status.yaml` tracks epic/story completion status
- Rendered workflows live under `_bmad/render/{skill}/{slug}-{hash}/{generation}/` for resumption

**Source:** `memlog.py` lines 6-68, `sprint_plan.py` lines 5-29

**c) Headless mode support**:
- Most workflows detect when called programmatically (vs interactive CLI)
- Return structured JSON response instead of asking questions
- Use pre-existing artifacts to infer intent

**Source:** `bmad-product-brief/SKILL.md` lines 37-63, `bmad-prd/SKILL.md` lines 39-53

**d) Atomic write guarantees**:
- Both `memlog.py` and `sprint_plan.py` use temp file → fsync → os.replace pattern
- Prevents corruption on crash

**Source:** `memlog.py` lines 122-130, `sprint_plan.py` lines 329-355

### 2. Gap Analysis: What Exists Now vs. What Project Map BMAD Needs

#### Project Map BMAD Requirements (from BATTLE-MAP.md):

| Requirement | Current State | Gap |
|-------------|---------------|-----|
| **11.1 Global project view** | Sprint-status.yaml shows story counts per status | No epic-level visualization; no dependency graph; no milestone timeline |
| **11.2 Node display with evidence** | Epics/stories tracked but evidence scattered across memlog, code commits, test results | No unified view linking node → evidence files |
| **11.3 Relationship/path visualization** | Manual dependency notes in PRD/addendum | No formal dependency encoding in data model |
| **11.4 Frontline & actionable positions** | sprint_plan.py recommends next action in JSON | Not surfaced in UI; requires calling sprints status |
| **11.5 Milestone & completion evidence** | Story completion logged via sprint sync | No verifiable evidence links (test coverage reports, deployment URLs) |
| **11.6 Min impl + formal impl 并存展示** | Unknown - no mechanism exists yet | Cannot distinguish MVP vs. final implementation |
| **11.7 Structure revision** | Correct Course skill exists for mid-sprint changes | No visual diff of structural changes; no causal chain preserved |
| **11.8 Evidence drill-down** | Links in addendum.md | No programmatic query interface |
| **11.9 Historical change view** | Git history exists; memlog tracks decisions | No dedicated struct-change log separate from code commits |
| **11.10 Multi-level expansion** | Filesystem hierarchy provides levels | No dynamic drill-down UI; static markdown files only |

**Sources:** BATTLE-MAP.md lines 296-353

#### Critical Missing Pieces for Project Map BMAD:

**Priority 1: Data Model Extension**
- Need schema for: complete functions, milestones, dependencies, evidence types
- Currently only epics/stories exist; missing "function" abstraction
- No way to express: "Feature X depends on Feature Y"; "Milestone Z requires A+B+C"

**Evidence:** module-help.csv shows epics/stories as primary unit but no "function" type

**Priority 2: Visualization Layer**
- Markdown files cannot express graphs, timelines, dependency networks
- Need rendering engine for: relationship diagrams, Gantt charts, status heatmaps
- No CSS/SVG/PDF output exists

**Evidence:** Only markdown outputs in any workflow read so far

**Priority 3: Real Chain Verification**
- BATTLE-MAP.md section 3.7 requires connecting multiple minimum implementations into working chain
- Current system treats each story independently; no automated integration testing
- No mechanism to verify: Story A → Story B → Story C works end-to-end

**Evidence:** sprint_plan.py validates individual statuses but not functional composition

---

## Future Candidates (Hypotheses - Unverified)

### Hypothesis 1: Project Map BMAD Could Be Built on Top of Standard BMAD Artifacts

**Proposal:**
Instead of replacing Standard BMAD, build visualization layer consuming:
- `sprint-status.yaml` as canonical task list
- `.memlog.md` as decision/evidence repository  
- Git commits as implementation records
- Test coverage reports as quality metrics

**Layer would provide:**
- Graph visualization of epic-story dependencies
- Milestone tracking from structured fields in PRDs
- Evidence drill-down querying memlog entries
- Structure revision timeline showing why dependencies changed

**Potential Benefits:**
- Non-destructive upgrade: keeps Standard BMAD intact
- Leverages existing durable artifacts
- Reduces duplicate storage

**Unknowns:**
- Current artifacts may not contain enough semantic richness (e.g., no function-level granularity)
- Need schema migration for historical data
- Unclear if visualization layer can stay synchronous with rapid local edits

**Evidence Level:** Medium - aligns with BATTLE-MAP.md section 9's vision of "software capability"

---

## Open Questions

### Where Evidence is Missing:

1. **How does BMAD Loop invoke automation?**
   - Question: At what point does BMAD Loop trigger bmad-build after sprint planning?
   - Evidence searched: bm

I cannot complete this thought as the content was cut off mid-sentence. The research report contains incomplete information at the end that needs to be addressed before proceeding with corrections.