# Architecture Spine Review — Rubric

**Verdict:** CONDITIONAL PASS — concise and aligned with the product philosophy; three cross-unit seams require tightening before finalization.

## High findings

1. **Candidate production is under-specified.** AD-3 correctly makes Weaving the only ingress from *raw external reality*, but the structural seed visually makes Weaving the only producer of semantic candidates. Cognitive shaping/discovery must also be able to propose native Project Shape candidates without pretending they came from raw facts.

2. **Shape adoption and derived-view consistency are conflated.** AD-4 currently says dependent boundary state becomes visible in the same atomic transition, while AD-8 says frontier/views are rebuildable projections. The invariant should be semantic-version consistency: adopted shape receives one coherent version; every derived view must declare/resolve against that same version and must never mix versions.

3. **Canonical writer is implicit, not explicit.** AD-3 blocks raw facts and AD-7 blocks workers, but independent authority workflows could still implement separate persistence writers. All adopted Project Shape mutations need one semantic mutation port/committer.

## Medium findings

- Project Narrative is correctly non-forensic, but its write path should allow an adopted method/process lesson even when no shape relation changes.
- Operational/deployment concerns are explicitly deferred, satisfying initiative-altitude breadth without inventing infrastructure.
- No named technology/version appears, so freshness verification has no binding-technology finding.
