# Project Map BMAD — Phase II Addendum

*Supplementary material for brief.md: evidence details, rejected hypotheses, alternative interpretations, and non-binding solution-space exploration.*

---

## Table of Contents

1. [Detailed Baseline Scan Findings](#evidence-detailed-findings)
2. [Rejected/Softened Hypotheses](#rejected-hypotheses)
3. [Alternative Interpretations](#alternative-interpretations)
4. [Non-Binding Solution-Space Exploration](#solution-space-examples)

---

## Evidence: Detailed Findings <a name="evidence-detailed-findings"></a>

### #1. Persistent Structural Cognition — Component Mapping

**Claim**: Partial coverage confirmed; stable project-level cognition capability unproven.

#### Source Mechanisms (with line references):

| Mechanism | Location | What It Captures | Scope Limitation |
|----------|----------|------------------|-----------------|
| **Agent activation protocol** | `bmad-agent-analyst/SKILL.md` lines 19-76; `bmad-agent-pm/SKILL.md` identical | Persona + persistent facts + config → context continuity across session | Per-role/session only; no explicit project topology representation |
| **Memlog system** | `_bmad/scripts/memlog.py` lines 6-130 | Append-only decision/question/insight tracking with JSON output | Chronological, not structural; no topology linkage |
| **Spec Open Questions** | `build/spec-template.md` lines 46-55 | Unresolved intent gaps with defensible options+consequences per entry | Per-story scope; not aggregated to epic/project level |
| **Correct Course impact analysis** | `correct-course/checklist.md` Section 2-3 (lines 42-134) | Cross-artifact impact assessment (PRD/epics/architecture/UX) | Reactive (triggered by change); not proactive maintenance tool |
| **Skill catalog dependencies** | `module-help.csv` | Maps each skill to phase/artifact dependency | Reference metadata; doesn't create usable representation |

#### Evidence Gap Analysis:

What we **can prove exists**: Each component answers part of "what happened, why decided."

What we **cannot yet prove**: Whether team can reliably answer *"What's our current adopted project shape at project level, what evidence supports it, why was this judgment made?"* without reconstructing from multiple sources.

**Behavioral hypothesis needing validation**: 
- Scenario A: Team navigates memlog + Open Questions sections + review logs to construct current picture → works but time-costly
- Scenario B: Team maintains informal mental model or external documentation → fragments diverge from reality
- Scenario C: Scattered sources naturally cohere → participants can answer question without reconstruction burden

Only empirical observation can distinguish these.

---

### #2. Structural Error Classification — Triaging Logic

**Claim**: Substantial partial coverage confirmed; routing/project-level propagation behavioral impact unproven.

#### Source Mechanisms:

| Mechanism | Location | Classification Schema | Action Triggered |
|----------|----------|---------------------|-----------------|
| **Build review triage** | `build step-04-review.md` lines 29-70 | `intent_gap` / `bad_spec` / `patch` / `defer` / `false` / `maybe-false` | `intent_gap`: loopback to human renegotiation<br/>`bad_spec`: spec reconciliation with KEEP instructions<br/>`patch`: auto-fix<br/>`defer`: append to deferred-work.md |
| **Intent gap handling** | Same file, lines 54-61 | Root cause inside `<frozen-after-approval>` | Revert code changes, human resolves intent, re-derive from updated spec |
| **Bad spec handling** | Same file, lines 55-61 | Spec clarity issue outside frozen section | Extract KEEP instructions, amend non-frozen sections, re-derive |
| **Correct Course epic changes** | `correct-course/checklist.md` lines 42-82 | Epic-level modification assessment | Can modify/def/remove/redefine epics based on trigger |

#### Comparison with Battle Map Target:

| Dimension | BMAD Current | Battle Map Expected | Candidate Differential? |
|----------|-------------|--------------------|------------------------|
| **Classification granularity** | Multi-category (`intent_gap`, `bad_spec`, `patch`) | Binary (implementation vs. structural) | Terminology difference only |
| **Structural identification** | `intent_gap` ≈ structural, `bad_spec` ≈ design clarity | Explicit "structural error" label | Semantics close; label differs |
| **Routing consequence** | Loopback + spec amendment; Correct Course at epic level | Map revision workflow triggered automatically | Timing/routing may differ |
| **Project-level propagation** | Story-level handled by build review; epic-level by Correct Course | Single unified map revision process | Possible propagation gap |

#### Behavioral Question (unvalidated):

Does a developer who finds `intent_gap` during story implementation recognize this as signal to reconsider project topology? Or do they just revert and ask human for intent clarification (missing the structural implication)?

**Current evidence**: Protocol supports both paths; unclear which is default practice.

---

### #3. Composite Reality Verification — Timing Differences

**Claim**: Substantial verification exists at epic retrospective timing; intermediate checkpoint behavioral benefit unmeasured.

#### Source Mechanisms:

| Mechanism | Location | When Executed | What It Checks |
|----------|----------|--------------|---------------|
| **Retro behavior check** | `retrospective SKILL.md` lines 78-79, Phase 2 description | After full epic completion | "Exercise changed flows end-to-end and record what you observed. Passing tests do not substitute for running system." |
| **Aggregate views** | `retrospective references/aggregate-views.md` | Post-epic diff analysis | Architecture delta, duplication map, god-class growth, pattern divergence, spec-to-implementation reconciliation |
| **Git evidence pre-pass** | `retrospective references/evidence-gathering.md` lines 11-20 | Precedes aggregate views | Per-story commit attribution + epic-wide diff range |

#### Comparison with Battle Map Target:

| Dimension | BMAD Current | Battle Map Expected | Difference Type |
|----------|-------------|--------------------|----------------|
| **Timing** | At epic retrospective (post-completion) | Intermediate checkpoints between story groups | **Timing difference** |
| **Scope** | Full epic behavior + cross-story defects | Incremental A→B validation before starting C | Scope granularity |
| **Defect detection** | Architecture delta, layering violations, cycles detected post-hoc | Serial/parallel assumption errors caught early | Detection latency |

#### Behavioral Hypothesis (needs empirical data):

Early hypothesis: Earlier checkpoints prevent costly late-stage integration crises.

But does this actually happen in practice? Evidence questions:
- How often do projects report "Story A + Story B done individually but链路不通"?
- When discovered? During retro or when trying to connect stories?
- Rework cost estimate when discovered late vs. early

**Current constraint**: No quantitative data available; cannot claim gap magnitude.

---

### #4. Unknown/Evidence Boundary Marking — Local Capture vs. Global Visibility

**Claim**: Local unknown/evidence capture exists; global coverage visibility unvalidated.

#### Source Mechanisms:

| Mechanism | Location | Captures What | Granularity |
|----------|----------|--------------|------------|
| **Memlog entry types** | `memlog.py` lines 46-59 | `(question)` / `(assumption)` / `(gap)` / `(decision)` / `(insight)` / `(event)` | Per-session entry level |
| **Spec Open Questions** | `build/spec-template.md` lines 46-55 | Unresolved intent gaps with defensible options+consequences | Per-story spec level |
| **Review Triage Log** | `build step-04-review.md` lines 89-94 | Verdict (`high`/`medium`/`low`/`false`/`maybe-false`) per finding + what evidence would settle | Per-finding level |
| **Missing evidence rule** | `retrospective references/evidence-gathering.md` lines 22-31 | Declares what each analysis needs; records narrowed scope when absent | Per-analysis declaration |
| **Brief addendum capture** | `product-brief SKILL.md` constraints section | Rejected alternatives/options/technical constraints captured during discovery | Brief-level summary |

#### Comparison with Battle Map Target:

| Dimension | BMAD Current | Battle Map Expected | Gap Question |
|----------|-------------|--------------------|-------------|
| **Local capture** | ✅ All components exist | Similar local capture needed | None — well-supported |
| **Coverage relations** | Implicit per-component | Explicit "X conditions covered by Y evidence, Z conditions remain uncovered" | Do teams aggregate local captures into global statement? |
| **Query interface** | Scattered sources | Drill-down from node to supporting evidence chain | Is reconstruction necessary or automatic? |

#### Behavioral Question (unvalidated):

When a team member asks "What conditions has Story X been tested against?", can they get immediate answer from any single source, or must search memlog + spec + review logs + retro?

This is a **cognitive burden question**, not capability absence.

---

### #5. Investment Gate Operationalization — Decision Behavior Possibly Missing

**Claim**: Midpoint judgment possibly missing; concrete manifestation remains speculative.

#### Source Mechanisms:

| Mechanism | Location | What It Assesses | Timing |
|----------|----------|-----------------|--------|
| **Readiness gate** | `sprint-planning references/readiness-gate.md` | Plan implementability without inventing decisions | Before sprint begins |
| **Readiness verdict** | Same file lines 16-20 | PASS/CONCERNS/FAIL with reasoning | Pre-flight |
| **Correct Course path evaluation** | `correct-course/checklist.md` lines 137-180 | Direct Adjustment / Rollback / PRD MVP Review with effort/risk estimates | Mid-sprint when changes occur |
| **Acceptance verdict** | `retrospective references/acceptance-verdict.md` lines 31-54 | Accepted / Accepted-with-open-items / Rejected rubric + unfinished-stories gate | Post-epic completion |

#### Comparison with Battle Map Target:

| Dimension | BMAD Current | Battle Map Expected | Possible Gap |
|----------|-------------|--------------------|-------------|
| **Pre-start gate** | ✅ Readiness gate assesses plan quality | N/A — different purpose | None |
| **Midpoint gate** | ❌ No explicit "MVP region stable enough for formal investment" checkpoint | Required before formal implementation begins | **Decision behavior possibly absent** |
| **Post-completion gate** | ✅ Acceptance verdict judges epic met criteria | N/A — different purpose | None |
| **Change management** | ✅ Correct Course handles mid-sprint course corrections | Related but different scope | May need augmentation |

#### Hypothesized Missing Behavior:

Teams might proceed directly from "MVP implementation started" to "formal implementation committed" without explicit midpoint judgment like:
> "We have evidence that MVP region is stable because: [A] tests pass, [B] real-chain verified, [C] structural assumptions validated through [D]. Remaining unknowns [E] deemed acceptable given [F]. Therefore justified to invest in formal implementation."

**Current uncertainty**: Does this judgment happen implicitly? If so, is implicit better or worse than explicit?

---

## Rejected/Softened Hypotheses <a name="rejected-hypotheses"></a>

### Hypothesis #1 (Initial, rejected in Round 2)
**Claim**: BMAD lacks structural error classification entirely.

**Evidence found**: `build step-04-review` triage logic shows clear `intent_gap` / `bad_spec` / `patch` distinction.

**Conclusion**: **Not a gap** — mechanism exists, terminology differs from Battle Map binary but semantics comparable.

**Softer framing**: Routing/project-level propagation effects unproven.

---

### Hypothesis #2 (Initial, rejected in Round 2)
**Claim**: BMAD has no composite reality verification mechanism.

**Evidence found**: `bmad-retrospective Phase 2` includes behavior checks + aggregate views detecting architecture delta, duplication maps, spec reconciliation.

**Conclusion**: **Not a gap** — verification exists, timing differs (retro vs. intermediate).

**Softer framing**: Whether later timing causes measurable problems unproven.

---

### Hypothesis #3 (Initial, rejected in Round 2)
**Claim**: sprint-status.yaml 只有简单 status，无 evidence_boundary 字段，因此缺乏未知标记能力。

**Evidence found**: Memlog entry types + spec Open Questions + review triage verdicts all capture unknowns locally.

**Conclusion**: **Partial coverage, not absence**. Fragment mechanisms exist globally scattered.

**Softer framing**: Whether team can reconstruct global coverage efficiently unproven.

---

### Hypothesis #4 (Initial, softened in Round 3)
**Claim**: #1 and #4 behaviors are "Well Covered / functionally equivalent / no observable behavioral difference."

**Correction from Round 3 review**: Having fragments ≠ stable behavior guarantee. Need to validate whether team can use scattered sources to answer project-level questions without reconstruction burden.

**New framing**: Partial coverage confirmed; project-level cognitive behavior unproven.

---

## Alternative Interpretations <a name="alternative-interpretations"></a>

### Alternative #1: Distributed Cognition Works Fine

**Hypothesis**: Teams successfully maintain mental models of project structure using scattered sources (memlog, Open Questions, etc.). Reconstruction cost is low because:
- Participants know where to look
- Sources are small/enough to traverse quickly
- Mental aggregation happens naturally

**Counterevidence concerns**:
- No empirical study of actual team behavior available
- Could be true for small teams/projects, break down at scale

**Validation approach**: Ethnographic observation + time-motion studies during sprint meetings.

---

### Alternative #2: Terminology Differences Matter More Than Functional Equivalence

**Hypothesis**: Even if `intent_gap` ≈ "structural error" semantically, terminology matters because:
- Developers don't immediately connect `intent_gap` findings to topology reconsideration
- Training/onboarding uses simpler language ("fix bug" vs. "intent gap")
- Cognitive load increases when mapping unfamiliar terms to mental models

**Counterevidence concerns**:
- BMAD already uses specialized vocabulary consistently
- Teams adapt to terminology over time

**Validation approach**: Survey developers about their understanding/action taken upon encountering `intent_gap`.

---

### Alternative #3: Later Verification Timing Has Benefit Too

**Hypothesis**: Post-epic verification (BMAD current) may have advantages over intermediate checkpoints:
- Less frequent overhead (no interrupting flow between stories)
- Fresh perspective after completing entire epic
- Cleaner git boundaries for diff analysis

**Counterevidence concerns**:
- Late detection = late rework cost
- Cannot course-correct until too late

**Validation approach**: Measure rework cost distribution: how much spent fixing integration issues vs. story-level bugs?

---

### Alternative #4: Existing Gates Suffice Without New Checkpoints

**Hypothesis**: Current gates (readiness → sprint sync → acceptance) plus Correct Course provide sufficient decision points. Adding explicit MVP→formal gate is redundant.

**Counterevidence concerns**:
- Current gates focus on *plan quality* or *completion acceptance*, not *midpoint stability*
- Teams might skip implicit judgments

**Validation approach**: Interview product managers/architects about when/how they decide to move from MVP to formal implementation.

---

## Non-Binding Solution-Space Exploration <a name="solution-space-examples"></a>

*These are candidate solutions that MIGHT address identified gaps. None should be treated as requirements or conclusions. They await gap validation BEFORE consideration.*

### Example A: Sprint Status Schema Extension (for #5 Investment Gate)

**Idea**: Add new status value to `sprint-status.yaml`:
```yaml
development_status:
  epic-1: mvp-ready  # instead of just backlog/in-progress/done
  1-1-auth-story: mvp-in-progress
  1-2-payments-story: backlog
```

**Plus optional fields**:
```yaml
mvp_readiness_evidence:
  - test_evidence: <observed evidence from actual implementation>
  - real_chain_verified: true
  - structural_assumptions_validated: ["dependency-A", "workflow-B"]
  - remaining_unknowns: ["scale-C", "failure-mode-D"]
  - investment_rationale: "<qualitative justification grounded in evidence>"
```

**Assumption being tested**: That adding explicit MVP status value improves decision traceability and prevents premature formal commitment.

**Counterargument**: Might be over-formalization if teams already make this judgment informally.

**Status**: Pure speculation pending gap confirmation.

---

### Example B: New Skill Gate for Investment Judgment (for #5)

**Idea**: Create `bmap-assess-investment-gate` skill that runs between MVP and formal phases:

```yaml
# Invocation format (hypothetical)
uv run _bmad/scripts/render_skill.py \
  --skill bmap-assess-investment-gate \
  --epic <epic-key> \
  --region <region-name>
```

**Deliverables**:
- Structured justification document
- Evidence checklist (tests passed, chains verified, assumptions validated)
- Risk register (known unknowns, mitigation plans)
- Recommendation: proceed/defer/postpone with rationale

**Assumption being tested**: That structured gate improves decision quality relative to ad-hoc judgment.

**Counterargument**: Could add unnecessary ceremony; teams might bypass or game the assessment.

**Status**: Pure speculation pending gap confirmation.

---

### Example C: Correct Course Enhancement for Structural Routing (for #2)

**Idea**: Enhance `correct-course` logic to automatically link `intent_gap` / `bad_spec` findings to map revision triggers:

```yaml
# Pseudo-schema for enhancement (not proposal)
if finding.classification == "intent_gap":
  append_to_project_map:
    node_id: <affected-node>
    reason: "intent_gap detected during implementation"
    action_required: "reconsider topology assumptions"
    evidence_link: "<finding-id>"
```

**Assumption being tested**: That explicit structural routing prevents missed improvement opportunities.

**Counterargument**: Might clutter project map with noise; teams could ignore structural suggestions.

**Status**: Pure speculation pending gap confirmation.

---

### Example D: Intermediate Real-Chain Verification Hooks (for #3)

**Idea**: Add hooks to BMAD Loop worktree_flow.py that trigger cross-story validation at natural boundaries:

```python
# Conceptual sketch (not implementation plan)
def maybe_trigger_real_chain_verification(self, task: StoryTask):
    """Check if accumulated stories form natural integration point"""
    if self._has_natural_integration_point(task):
        return self.trigger_end_to_end_check()
```

**Natural integration point heuristics**:
- Stories A+B share same user-facing feature boundary
- Story B depends on Story A output
- Both stories completed in same sprint window

**Assumption being tested**: That earlier integration feedback prevents costly late rework.

**Counterargument**: Might fragment development flow; too many checkpoints add cognitive overhead.

**Status**: Pure speculation pending gap confirmation.

---

### Example E: Unified Coverage View Aggregation (for #4)

**Idea**: Build query interface that aggregates coverage statements from scattered sources:

```yaml
# Query: What's the coverage status for Story X?
# Response schema (hypothetical):
story: 1-1-authentication
conditions_covered:
  - condition: "happy-path login"
    evidence: [test-report-id, deployment-url]
    verified_via: unit-test + manual-check
  - condition: "invalid-password handling"
    evidence: [review-log-entry]
    verified_via: peer-review
conditions_uncovered:
  - condition: "session timeout recovery"
    reason: "not yet designed"
  - condition: "brute-force protection"
    reason: "depends on security requirement clarification"
coverage_completeness_estimate: "core flows tested, edge cases pending"
```

**Assumption being tested**: That unified view reduces reconstruction burden and improves decision speed.

**Counterargument**: Aggregation itself creates maintenance overhead; sources may drift out of sync.

**Status**: Pure speculation pending gap confirmation.

---

## Methodological Notes

### Evidence Discipline Applied Throughout

1. **Component existence ≠ behavioral guarantee**: Just because memlog exists doesn't mean team maintains project topology awareness from it.

2. **Terminology differences ≠ functional gaps**: `intent_gap` may be semantically equivalent to "structural error" even if naming differs.

3. **Timing differences need measured impact**: Later verification might be fine IF no measurable problems occur.

4. **Solution proposals await gap confirmation**: All examples A-E remain speculative until gaps validated.

5. **No invented numbers**: Avoid X%/Y% thresholds without empirical data sources. Qualitative falsifiable conditions preferred.

### Sources Consulted (With Line References)

All evidence cited above comes from documented locations with specific line references. This enables independent verification and avoids impression-based claims.

**Key repositories scanned systematically**:
- `/Users/looy/.dsh/renzhi-rongjie-labs/bmad-battle-flow/project-map-bmad/.qoder/skills/` — Standard BMAD skills
- `/Users/looy/.dsh/renzhi-rongjie-labs/bmad-battle-flow/bmad-loop/src/bmad_loop/` — BMAD Loop orchestrator
- `_bmad/scripts/` — Shared scripts (memlog, render_skill, resolve_config, sprint_plan)
- `reference/BATTLE-MAP.md` — Stage-1 target model reference

**Discovery timeline**: Three rounds of systematic scanning (Round 1: initial gap hypotheses; Round 2: corrected false positives; Round 3: refined candidate differentials with strict evidence discipline).

---

*End of Addendum*
