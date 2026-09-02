# PRD Quality Review — Project Map BMAD — Method Evolution Validation PRD

## Overall verdict

Focused re-review after the 8 direct-text audit corrections. All six audit targets verify clean: no invented numeric thresholds remain (measurement items like "lookup count" are observed quantities, not thresholds); Protocols #3/#5 are natural-observation-primary with explicitly labeled second-stage interventions; canonical Stage-1 gate names are used in all headings and gate bodies; no synthetic probe scheduling remains (Next Steps observes first natural events, Gates #2/#5 state "Do not manufacture an event and do not invent a calendar deadline"); Study Completion is disposition-state-based with an explicit "not gate counts" rule. Remaining issues are all low-severity hygiene: one owner question (Q1) that the PRD's own machinery already answers, unsourced confidence tiers in the Exec Summary table, a missing Assumptions Index, residual noun drift, and one gate-name order inversion in the summary table. The PRD is decision-ready for downstream execution.

---

## Decision-readiness — strong

The gate machinery is fully decision-grade after the corrections: each gate carries a behavioral question, natural observation point, collapse/promote criteria, a Decide Now / Defer to Later split, and event-absence handling ("If this event does not occur in the current lifecycle window, status = deferred/not-observed with explicit revisit trigger" — Gates #2/#5). Success metrics all name their adjudicator ("Owner judges adequacy based on recorded artifacts at review point"). Q2 is explicitly marked "(RESOLVED FROM EXISTING POLICY)" with promote/collapse/defer/aggregate rules. One leftover open question is not genuinely open.

### Findings

- **low** Q1 is largely answerable from policy already in the document (§ Open Questions, Q1) — Q1 asks "Under what conditions should we expand evidence collection beyond observed natural events when results are ambiguous, context-specific, or contradicted?" but the PRD already encodes the answer in three places: Protocols #3/#5 second-stage activation ("activated only if natural evidence from primary protocol is insufficient to discriminate the hypothesis"), the bounded collapse criteria with reopen conditions (context-specificity handling), and Q2's defer rule for absent events. The execution contract's batching rule ("resolves questions already answered by durable owner decisions, project evidence, or low-risk defaults. Only genuinely owner-level unresolved decisions are escalated") says such a question should not sit open. *Fix:* mark Q1 RESOLVED FROM EXISTING POLICY as Q2 was, citing those three mechanisms; the only residue (who declares natural evidence insufficient) is already answered by the Validation Observation Model (Owner).

---

## Substance over theater — strong

No personas, no NFR boilerplate, no swappable Vision; the thesis ("Cannot invent reasons to evolve just to justify project existence") is specific and load-bearing, the null hypothesis is structurally preserved, and collapse/promote criteria remain qualitative-falsifiable with the "no invented percentages" discipline rule intact. The prior pseudo-precision ("one lookup pass", calendar deadlines, gate-count thresholds) is gone. One residual unsourced assessment remains.

### Findings

- **low** Confidence tiers in the Exec Summary table have no stated provenance (§ Executive Summary table, rows #1/#2/#4) — "Still live (medium confidence)", "low-mid confidence", and "mid confidence" trace to nothing in the upstream artifacts (the stage-2 brief and addendum carry no such tiers), and the PRD presents them without a source note. Carried over from the prior review's watch-item, still unaddressed. *Fix:* add a provenance clause (e.g., "preliminary conviction inherited from the stage-2 brief scan") or drop the parenthetical tiers and keep only "Still live / Deferred to downstream".

---

## Strategic coherence — strong

The reference model → gates → preserved strengths → protocols → open questions arc is intact and now internally consistent: the prior circularity (Next Steps pre-judging an open scheduling question) is resolved — Next Steps now says "Observe: Each gate at its first natural applicable event; if absent, mark deferred/not-observed", which matches the gate-level defer rules rather than anticipating them. Gate #5's counter-metric logic (ceremony cost vs. ambiguity reduction) remains thesis-protecting. No remaining findings.

---

## Done-ness clarity — strong

Every success metric now binds its adjective to a named adjudicator and a recorded-artifact basis ("Owner judges whether defect discovery timing and rework magnitude show a difference that materially affects next-move decisions" — Protocol #3); Gate #3's bounded collapse is scoped to the observed evidence boundary with an explicit reopen condition; Gate #4's collapse criterion anchors on "a non-writer participant (different from the story implementer)" rather than "any stakeholder". Measurement lists (artifacts consulted, time, lookups/backtracks) are observation items, not thresholds. No remaining findings.

---

## Scope honesty — adequate

Deferrals are explicit per gate, the "Defer to Later" lists function as non-goals, event-absence handling is written into Gates #2/#5, and the two genuinely inferential dependencies now carry `[ASSUMPTION]` tags (fresh participant for Gate #1; intent_gap occurrence for Gate #2). Coverage of that tagging is not complete.

### Findings

- **low** Assumption tagging is asymmetric and unindexed (§ Gate #4 Collapse Criterion; document end) — Gate #4's collapse criterion likewise depends on a non-writer participant ("A non-writer participant (different from the story implementer) can generate a coverage summary") but carries no parallel availability assumption, unlike Gate #1; and the two inline `[ASSUMPTION]` tags have no Assumptions Index to roundtrip against. *Fix:* tag Gate #4's participant availability (or state it is covered by Gate #1's assumption) and add an Assumptions Index listing both/all tags.

---

## Downstream usability — adequate

Structurally clean and now terminologically stable where it matters most: gate names are canonical across the Behavior, Gate, and table sections, Protocol #N ↔ Gate #N mapping is contiguous, each gate block is self-contained, and Next Steps #3 correctly declares the Exec Summary table names as the canonical memlog tag vocabulary. What remains is the absence of a Glossary and drift in secondary nouns.

### Findings

- **low** Core non-gate nouns still drift (§ throughout) — "coverage statement" / "coverage summary" / "coverage relations" are used interchangeably (Exec Summary table row #4, Behavior #4 definition, Gate #4 collapse, Protocol #4), as are "project topology" / "project shape" (Behavior #1 definition vs. Gate #1/Protocol #1) and "candidate differential" / "validation gate" / "gate". *Fix:* a short Glossary picking one canonical noun per concept; gate names no longer need fixing.

---

## Shape fit — strong

Brownfield identity declared up front, existing mechanisms itemized per gate, new-vs-existing distinguished throughout, and the prior structural absence is now filled: "Study Completion & Handoff Criteria" defines the study-level done state as every gate holding an explicit evidence state `{collapsed-for-current-scope, promoted-to-provisional-requirement, live/deferred-with-revisit-trigger}` with deferred gates non-blocking when trigger and owner/observer are explicit — a qualitative, disposition-based completion rule that matches the method-study shape. No remaining findings.

---

## Mechanical notes

- **Gate #5 name order inversion**: Exec Summary table row 5 reads "Investment Gate Operationalization (Justifiable Investment Judgment)" while Behavior #5 / Gate #5 headings lead with the canonical "Justifiable Investment Judgment (Investment Gate Operationalization)". Since Next Steps #3 makes the table the canonical memlog tag source, the table should lead with the canonical name.
- **Fill-in placeholders**: Gate #3's "Evidence boundary: [specific stories/features examined]" and Gate #5's "[specific MVP regions and transitions examined]" are intentional fill-at-observation fields; mark them as such (e.g., "to be recorded at observation time") so downstream readers don't treat them as missing text.
- **Behavioral Question grammar**: Gate #4's "Behavioral Question" is a declarative statement with no question form ("Teams can reliably assemble coverage statements..."), and Gate #5's is a statement with a trailing "?". Cosmetic; rephrase as questions for parallel structure with Gates #1/#3.
- **ID continuity**: Behavior/Gate/Protocol 1–5 contiguous and unique; Q numbering is now Q1–Q2 after the Q2/Q5 merge; all Protocol↔Gate cross-references resolve.
- **Appendix roundtrip**: all four cited upstream paths exist on disk (stage-2 brief + addendum, stage-1 brief, `reference/BATTLE-MAP.md`).
- **Assumptions Index roundtrip**: 2 inline `[ASSUMPTION]` tags, no index — see Scope honesty finding.
- Prior mechanical issues confirmed fixed: no CJK fragments, no duplicated frontmatter observation model.

---

## Finding summary

| Severity | Count | Findings |
|----------|-------|----------|
| **Critical** | 0 | — |
| **High** | 0 | — |
| **Medium** | 0 | — |
| **Low** | 4 | Q1 resolvable from existing policy; unsourced confidence tiers; asymmetric assumption tagging + no Assumptions Index; core noun drift |

**Overall**: All six focused audit targets pass; remaining issues are low-severity hygiene that can be cleaned up before or alongside the review gate.
