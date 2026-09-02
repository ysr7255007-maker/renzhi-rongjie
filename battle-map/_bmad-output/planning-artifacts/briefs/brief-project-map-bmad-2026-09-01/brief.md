---
title: Project Map BMAD — Method Specification and Durable Artifacts
status: draft
created: 2026-09-01
updated: 2026-09-01
scope: method + durable artifacts + operational semantics
---

# Project Map BMAD

## Working Definition

Project Map BMAD is the **method specification itself** — not a visualization tool, web dashboard, or CLI. It defines:

1. **Durable authoritative artifacts**: what data structures encode project structure, evidence coverage, unknowns, failure conditions
2. **Relations between artifacts**: how epics/stories/functions depend on each other, how evidence links to nodes
3. **Operational semantics**: when/how the map advances (region investment decisions, real chain verification triggers)

**Visualization layers** (mermaid diagrams, web dashboards, CLI trees) are replaceable projections of the core method artifacts — they may change as user needs evolve, but the underlying spec remains stable.

---

## Core Principles

### 1. **Reuse before abstraction**
Any mechanism that Standard BMAD / BMAD Loop / git / memlog / sprint-status.yaml already supports must be reused directly. The new layer only adds:
- Structural relations that existing artifacts cannot express (dependencies, milestone chains)
- Evidence/unknown tracking (what claims lack sources)
- Evolution history (why relationships changed)
- Progression conditions (when regional gates allow investment)

### 2. **No legacy inheritance by default**
Old `battle-map-bmad` designs (7 Epic / 23 Story Hard Stop architecture, v6-shims forwarding) do **not** carry forward automatically. A mechanism from the legacy codebase can enter only if independently re-proven by本轮证据（e.g., memlog design patterns, atomic writes）。

### 3. **Map = most credible current structure**
The map represents:
- Current best understanding of project topology
- What evidence covers each node
- What remains unknown (explicitly tagged)
- Failure conditions (when this map would invalidate itself)
- Next discriminative probes / regional investment decisions

---

## Key Components (Tentative)

### Component A: Durable Artifact Schema Extension

**Current state (from TR research):**
- Epics/Stories tracked in `sprint-status.yaml`
- Decisions logged chronologically in `.memlog.md`
- Rendered workflows live under `_bmad/render/{skill}/{slug}-{hash}/{generation}/`

**Gap identified:**
No "function" abstraction exists; cannot express:
- Feature X depends on Feature Y
- Milestone Z requires A+B+C
- MVP implementation vs. formal implementation distinction

**Requirement:**
Extend schema to support complete functions, milestones, dependencies, evidence types without replacing Standard BMAD artifact formats.

---

### Component B: Evidence Drilling Semantics

**What exists:**
- Git commits track code changes
- Memlog tracks decisions/questions
- Sprint sync logs story completion

**Gap:**
No unified view linking node → evidence files (test reports, deployment URLs, architecture diagrams)

**Requirement:**
Define query interface to drill down from any epic/story/function to its supporting evidence chain.

---

### Component C: Real Chain Verification

**Concept from BATTLE-MAP.md section 3.7:**
Connect multiple minimum implementations into working chain.

**Unknown:**
How does Standard BMAD trigger integration test across stories? Current system treats each story independently.

**Requirement:**
Specify automation point where Story A → Story B → Story C end-to-end verification happens. Is this BMAD Loop responsibility？Standard BMAD advisory step？Both？

---

### Component D: Regional Investment Confidence Gate

**Clarified interpretation (from user correction):**
NOT a numeric scorecard. Expresses **"regional investment judgment"** — qualitative decision whether MVP is stable enough to commit to formal implementation.

**Unknown:**
What signals count toward this judgment? Examples being considered:
- Test coverage threshold met？
- Architecture review passed？
- User feedback validated core workflow？
- No critical blockers in sprint status？

**Requirement:**
Define observable criteria (not numeric scores) that stakeholders use to answer: "Are we ready to invest formally?"

---

## Scope Boundaries (Explicit)

### In Scope for Project Map BMAD:

✅ Method specification for durable artifacts
✅ Relations/dependencies encoding
✅ Evidence tracking semantics
✅ Operational semantics for map advancement
✅ Visualization *projections* (but not coupled to specific tech)

### Out of Scope (for now):

❌ Choosing specific visualization technology (mermaid vs. SVG vs. web dashboard)
❌ Building abstraction layer unless existing artifacts demonstrably insufficient
❌ Reusing old battle-map-bmad structures without independent validation
❌ Numeric confidence scoring systems

---

## Open Questions (Known Unknowns)

| Question | Owner | Why it matters |
|----------|-------|----------------|
| When exactly does BMAD Loop take over from Standard BMAD？Who signals handoff？| Implementation phase transition | Affects sprint planning → build trigger flow |
| What are minimal evidence requirements for "real chain verified" status？| Quality gate definition | Determines integration testing automation |
| How should "function" abstraction relate to existing epic/story model？| Data model extension | Avoids breaking sprint-status.yaml compatibility |
| Who owns final regional investment judgment calls？Product？Architecture？Team？| Decision rights | Shapes addendum documentation flow |

---

## Success Criteria

Project Map BMAD Brief is validated when:

1. Stakeholders can read brief and agree: "This describes the method I'd use"
2. Implementation team can identify which components to build first
3. Legacy mechanisms can be tested against new requirements without automatic inheritance

---

## Formal Handoff

Proceed to the Standard BMAD PRD stage with the known unknowns preserved. Downstream planning may turn an unknown into a decision only when new evidence or explicit owner judgment supports it; it must not fill the gap merely to make the artifact look complete.

---

*Addendum contains: detailed gap analysis from TR report, alternative options considered (numeric scores vs. qualitative gates), technical constraints from Standard BMAD artifacts*
