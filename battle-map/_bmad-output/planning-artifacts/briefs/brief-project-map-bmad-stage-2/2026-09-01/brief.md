---
title: Project Map BMAD — Phase II Method Evolution Hypothesis
status: draft
created: 2026-09-01
updated: 2026-09-01
scope: product problem framing for brownfield evolution research
topic: Project Map BMAD — Phase II Method Evolution Hypothesis
---

# Project Map BMAD — Phase II

## Working Definition

**Project Map BMAD Phase II is a method evolution hypothesis study**: whether existing Standard BMAD (v6.11.0) and BMAD Loop (v0.11.1) should be evolved toward Stage-1 target behaviors identified in BATTLE-MAP.md.

**Brownfield constraint**: This is an evolution project within Standard BMAD + BMAD Loop ecosystem, not a parallel Battle Map product layer. Implementation workspace can be greenfield, but the product/method nature is brownfield evolution — studying what to preserve, what might need changing, and minimal necessary differentials.

**Allowable conclusions** (no forced narrative):
1. ✅ **Evolution needed** — Standard BMAD lacks capabilities that Stage-1 model provides
2. ❌ **No evolution needed** — Existing mechanisms already sufficiently实现 Stage-1 goals
3. ⚠️ **Partial evolution** — Some areas need change, others don't

**Key principle**: Cannot invent reasons to evolve just to justify project existence. Value lies in validating evolution hypothesis, not forcing confirmation.

---

## Research Motivation

### The Core Question

Standard BMAD + BMAD Loop form a mature development practice system with proven value in:
- Role-based context continuity (Agent → Menu → Workflow)
- Artifact progressive convergence (brief → prd → spec → code)
- Recoverable/auditable state (memlog, sprint-status, rendered workflows)
- Implementation closure rhythm (build → verify → integrate)
- Reliable deterministic control (no LLM in orchestration loop)

Stage-1 (from Phase I) identified a **candidate model for long-term complex projects**: one that sustains awareness of "current project shape, why this judgment, what remains unknown, how reality changes structure, and why next investment is justified" throughout project advancement.

**Core purpose** (Battle Map as advancement method, not archive):
Battle Map is a **campaign command/advancement methodology**, not an information archive. Its five target behaviors all serve the question: **"Given current project state, what is the most reasonable next move?"** — whether that's risk probe selection, MVP→formal investment decision, or structural revision triggered by real-world feedback. The value is in advancing projects intelligently through uncertainty, not in making records more complete per se.

**Research question**: **"Whether evolving existing BMAD toward this target behavior model yields net benefit versus keeping current practices."**

### Why This Research Matters

Long-term uncertain projects face a specific risk: as work fragments into tasks/stories, teams lose sight of:
- What the project's current best-understood topology is
- Which judgments have evidence support and which remain assumptions
- How real implementation results should change structural understanding
- Why investing in certain areas now is justified over others
- What the most reasonable next move is, given current state

**Current understanding**: Standard BMAD has distributed mechanisms supporting some aspects of these questions (memlog entries, Open Questions sections, review triage logs), but whether these form a **stable, recoverable, actionable project-level structural representation** is unproven. The question is not about centralized visualization (a replaceable projection), but about authoritative/project-level representation that can actually guide advancement decisions.

---

## Stage-1 Target Model (From BATTLE-MAP.md)

*Reference only — not assumed as ideal that must be achieved.*

The Battle Map methodology describes five interconnected target behaviors, all serving **advancement/investment judgment**:

1. **Persistent Structural Cognition** — Participants can answer "What is current adopted project shape? What evidence supports it? Why this judgment was made?" at project level without reconstructing from unrelated fragments
2. **Explicit Classification of Structural Errors** — Test failures classified as implementation error vs. structural error; structural issues trigger map revision workflow that maintains causal continuity between real feedback and structure change
3. **Composite Reality Verification** — Cross-story end-to-end verification at intermediate checkpoints during implementation, not just post-epic — enables earlier detection of serial/parallel assumption errors
4. **Unknown and Evidence Boundary Marking** — Completion status expresses "X conditions covered by Y evidence, Z conditions remain uncovered" with explicit coverage relations
5. **Justifiable Investment Judgment** — MVP→formal impl transition checkpoint with traceable rationale grounded in concrete evidence and decision criteria

**Important**: These form a "behavior family" — not mutually exclusive features, but interrelated capabilities expressing "maintainability of project shape awareness for advancement purposes."

---

## Baseline Coverage Analysis (Third Round Discovery)

*Based on systematic scan of Standard BMAD + BMAD Loop source code, workflows, and documented behaviors.*

**Evidence discipline reminder**: Having fragmented mechanisms (memlog, open questions, review triage) does not prove stable project-level behavior. We distinguish:
- **Fragment exists**: BMAD has component X somewhere
- **Stable behavior**: Team can consistently rely on X to answer Y question at project level
- **Candidate differential**: Gap between fragment and stable behavior, where behavioral impact needs validation

---

### 🟡 Candidate Differentials (Partial Coverage — Behavioral Impact Unknown)

#### #1. Persistent Structural Cognition

**Existing mechanisms** (evidence-sourced):
- `bmad-agent-* activation protocol`: persona + persistent facts + config loading → context continuity across session
- `.memlog.py`: append-only decision/question/insight tracking with JSON output
- `build/spec-template.md::Open Questions`: explicit unknowns section with defensible options+consequences per entry
- `correct-course::checklist.md Section 2-3`: cross-artifact impact analysis (PRD/epics/architecture/UX)
- `module-help.csv skill catalog`: maps each skill to phase/artifact dependency

**Fragment analysis**: All components exist. Each answers part of "what happened, why decided":
- memlog tracks chronology of decisions/questions
- Open Questions captures known intent gaps with alternatives
- Review Triage Log records verdict/evidence per finding
- Correct Course assesses cross-artifact impact when changes occur

**Target behavior gap (unvalidated)**: Whether these fragments combine into **stable, recoverable project-level representation** that participants can use to answer "What's our current shape and why?" without reconstruction work.

**Behavioral hypothesis needing evidence**: 
- Do teams successfully maintain project topology awareness using these tools?
- Or do they spend significant time reconstructing structure from scattered sources?
- When would centralized/structured representation save meaningful effort?

**Status**: Partial coverage confirmed; stable project-level cognition capability needs empirical validation.

---

#### #2. Explicit Classification of Structural Errors

**Current state** (evidence-sourced):
- `build step-04-review::Classify`: triage categories—`intent_gap` (root cause inside frozen-after-approval/structural), `bad_spec` (spec clarity issue), `patch` (implementation), `defer` (pre-existing)
- `intent_gap` triggers loopback to human for intent renegotiation before re-derivation
- `bad_spec` triggers spec reconciliation action item with KEEP instructions
- `bmad-correct-course`: epic-level structural change management

**Battle Map target**: Binary classification ("implementation error vs. structural error") with explicit linkage to project map revision workflow; structural issues automatically signal topology reconsideration

**Candidate differential** (未验证行为影响):
1. Terminology differs (`intent_gap` / `bad_spec` vs. "structural error" label)
2. Routing/timing: build handles story-level; Correct Course handles epic-level; unclear if project-level structural revision is automatic consequence
3. Causal continuity implicit rather than marked: no explicit signal linking findings to "map revision opportunity"

**Behavioral hypothesis needing evidence**: Does terminology/routing/timing difference cause teams to miss structural improvement opportunities? Examples:
- `intent_gap` found → developer fixes code instead of asking "should we change project topology?"
- Missing opportunity because structural implication not surfaced

**Status**: Substantial partial coverage confirmed; routing/project-level propagation behavioral impact unproven.

---

#### #3. Composite Reality Verification

**Current state** (evidence-sourced):
- `bmad-retrospective Phase 2::Behavior check`: "exercise changed flows end-to-end and record what you observed. Passing tests do not substitute for running system."
- Aggregate views detect cross-story defects: architecture delta, duplication map, spec-to-implementation reconciliation
- `git_evidence.py`: per-story commit attribution + epic-wide diff range

**Battle Map target**: Intermediate checkpoints between story groups (e.g., after Story A+B complete, verify A→B flow before starting Story C)

**Candidate differential** (timing difference needing validation):
- **BMAD**: Cross-story verification performed at epic retrospective (post-epic completion)
- **Battle Map**: Intermediate checkpoints during implementation (between story groups)

**Behavioral hypothesis**: Earlier detection of serial/parallel assumption errors could prevent late-stage integration crises. But does delayed timing cause measurable problems in practice?

**Needs evidence**: 
- How often do projects experience "Story A + Story B done individually but链路不通"?
- When discovered? During retro or before?
- How much rework cost attributed to late verification?

**Status**: Timing difference candidate; need empirical evidence of negative impact before claiming true gap.

---

#### #4. Unknown and Evidence Boundary Marking

**Existing mechanisms**:
- `memlog.py entry types`: `(question)` / `(assumption)` / `(gap)` / `(decision)` / `(insight)` / `(event)`
- `build/spec-template.md::Open Questions`: one entry per unresolved intent gap with defensible options+consequences
- `build step-04-review::Review Triage Log`: verdict per finding (`high`/`medium`/`low`/`false`/`maybe-false`) + evidence needed to settle
- `retrospective/evidence-gathering.md::Missing evidence`: each analysis declares what it needs and records narrowed scope
- `bmad-product-brief/addendum`: rejected alternatives/options/technical constraints captured during discovery

**Fragment analysis**: BMAD captures unknowns locally:
- Memlog tracks questions/assumptions/gaps per session
- Spec Open Questions lists unresolved decisions with options
- Review triage log notes what evidence would settle maybe-false findings
- Retro evidence gathering flags missing inputs

**Target behavior gap (unvalidated)**: Whether these fragments provide **explicit coverage relation statements** like "Story X completed, Y conditions tested via Z evidence, W boundary conditions not yet covered."

**Behavioral hypothesis needing evidence**:
- Can team look at any node and say "these are the conditions we've verified, these remain untested"?
- Or do they need to search scattered sources to reconstruct coverage picture?
- When would explicit coverage statement improve decision quality?

**Status**: Substantial partial coverage confirmed; global evidence-boundary visibility behavioral impact unproven.

---

#### #5. Investment Gate Operationalization

**Current state** (evidence-sourced):
- `readiness-gate.md`: assesses whether plan implementable without inventing decisions nothing records
- `sprint-planning readiness verdict`: PASS/CONCERNS/FAIL with reasoning
- `correct-course Section 4`: path forward evaluation (Direct Adjustment/Rollback/PRD MVP Review) with effort/risk estimates
- `retrospective acceptance-verdict`: Accepted/Accepted-with-open-items/Rejected rubric + unfinished-stories gate

**Battle Map target**: Mid-implementation checkpoint—"MVP region proved stable → justify formal investment" with traceable rationale

**Candidate differential** (decision behavior possibly missing):
- BMAD gates assess plan readiness OR post-completion acceptance
- **Possibly missing**: Explicit "MVP region ready for formal investment" midpoint judgment with evidence-sufficiency criteria and traceable rationale
- Concrete manifestation (schema/workflow/skill) remains open pending gap validation

**Behavioral hypothesis needing evidence**:
- Do teams currently skip explicit MVP stability assessment before committing to formal implementation?
- How often does premature formal implementation cause rework due to instability?
- Would adding midpoint checkpoint improve decision quality relative to operational cost?

**Status**: Decision behavior possibly missing; concrete manifestation (schema/workflow) remains solution-space speculation until gap validated.

---

## Owner Decision Framework (Absorbed from Conversation)

These principles guide how we evaluate candidate differentials:

### Gap Threshold Criterion (Strict)
术语不同、文件位置不同、表达不集中，本身都不足以叫 gap。一个候选差分只有当它导致可观察的方法行为差异、能力缺失、错误路由、明显更晚/更弱的反馈，或系统性地无法达到 Stage-1 target behavior 时，才有资格升级成真正 gap。语义近似但命名不同的机制，应优先视为已有覆盖；除非研究能证明这种命名/路由/时机差异会改变实际行为。

### Brownfield Evolution Principle
默认不因为"表达更像 Battle Map"或"标签更清楚"就修改 BMAD。纯语义增量只有在它产生可观察价值时才值得，例如：明显降低错误判断、跨岗位协调成本、自动化推断成本、证据追踪成本，或让原本容易漏掉的决策/状态稳定进入后续工作流。若只是给已有隐含状态换一个显式名字，而没有实际方法行为或操作成本收益，应优先不改。成熟参考形状默认保留，差异需要证据。

### Research Direction — No Artificial Prioritization
不要为了流程推进人为制造排序。Brief/PRD 都可以继续并行研究这些候选差分。只有证据显示某项风险、价值、依赖或可逆性显著不同，或者实际资源约束迫使排序时，才排序。当前没有这个证据，也没有"PRD 必须先从 ONE 开始"的约束。

### Evidence-Based Decision Thresholds (Qualitative, Not Quantitative)
Avoid invented X%/Y% numbers without data sources. Write each candidate differential as falsifiable/evidencable conditions rather than pseudo-precise percentages:
- **Not a real gap**: If existing BMAD mechanisms already stably produce equivalent behavior at correct timing, with no systemic failure patterns
- **Real gap but no evolution warranted**: If确有行为缺口，但改造成本/复杂度/兼容性损失明显超过已观察价值，可以保留为已知差异而不演化
- **Support evolution**: If 缺口能被真实失败案例或重复出现的工作流问题证明，并且最小差分能显著降低该问题，同时保留 BMAD 成熟机制

Only when real quantitative statistics become available in PRD can we establish numeric thresholds based on evidence.

### Allowable Conclusion — No Forced Narrative
This brief allows three conclusions: evolution needed, no evolution needed, or partial evolution. Cannot force confirmation by inventing gaps. Value lies in validating evolution hypothesis honestly.

---

## Preliminary Conviction (Tentative, Subject to Change)

Based on third-round discovery:

1. **All five target behaviors show partial BMAD coverage** — none are completely absent. Fragment mechanisms exist across the method chain (memlog, spec templates, review logs, retros).

2. **Many Phase-I apparent gaps collapse into partial-coverage questions** — the real investigation is whether these fragments form stable, project-level behavioral guarantees, not whether components exist.

3. **Three strongest candidate behavioral differentials**:
   - **#2 Structural Error Routing**: Whether routing/timing differences cause missed structural improvement opportunities
   - **#3 Real-Chain Timing**: Whether later verification causes costly late-stage integration crises
   - **#5 Investment Gate**: Whether missing midpoint checkpoint leads to premature formal commitment

4. **Two other candidates (#1, #4)** may also have behavioral gaps, but require empirical validation of whether teams struggle to reconstruct project shape/evidence coverage from scattered sources.

5. **No evolution conclusion remains valid** — if future evidence shows existing fragments already provide sufficient behavioral guarantees, the right answer is "don't evolve."

6. **Evolution direction depends on evidence** — should follow wherever data points, not predetermined blueprint. Solution forms (schema additions, new skills, workflow enhancements) should only emerge after gaps confirmed AND benefits exceed costs.

---

## Next Steps (PRD Phase Study Mandate)

Phase III PRD continues this discovery with mandate to:

1. **Study all candidate differentials in parallel** (unless evidence later justifies prioritization)
2. **Collect empirical evidence** for behavioral hypotheses (not just mechanism mapping)
3. **Test null hypothesis** — can we conclude "no evolution needed" based on gathered data?
4. **Define concrete evolution方案 only if gaps confirmed AND benefits exceed costs** — avoid premature schema/module/UI proposals

PRD may复核、推翻和深化 these conclusions. Brief serves as starting point, not final authority.

---

## Key Uncertainties (For PRD Investigation)

| Candidate | Key Unknown | Why It Matters |
|-----------|------------|---------------|
| #1 Structural Cognition | Do teams successfully maintain project topology awareness from scattered sources, or reconstruct manually? | Determines if structured representation adds real cognitive value |
| #2 Structural Error Routing | Are structural improvement opportunities missed due to terminology/routing differences? | Validates whether explicit "map revision signal" improves outcomes |
| #3 Real-Chain Timing | How often do projects experience late-stage integration crises due to delayed cross-story verification? | Supports/weakens case for intermediate checkpoints |
| #4 Evidence Boundary Visibility | Can teams reliably state "what's covered, what's not" from current artifacts? | Determines if explicit coverage statements improve decision quality |
| #5 Investment Gate | Do teams skip MVP stability assessment? What rework occurs from premature formal commitment? | Validates need for midpoint checkpoint with traceable rationale |

---

*Addendum contains: detailed baseline scan findings, evidence citations from source code, alternative interpretation notes, rejected hypotheses with rationales, non-binding solution-space examples*
