# Architecture Spine Review — Adversarial Seams

**Verdict:** CONDITIONAL PASS.

Constructed independently compliant units reveal three possible incompatibilities:

1. **Weaving vs cognitive shaping:** one unit could represent candidate changes as relation deltas while another emits document patches or ad-hoc commands. Both could claim compliance because the candidate contract is not explicit. Require one native Project Shape candidate/delta contract for every producer.

2. **Authority workflow vs persistence:** two authority implementations could each write the semantic store directly and both still appear compliant. Require a single semantic mutation port that alone may commit adopted Project Shape changes.

3. **Project Shape vs derived frontier:** one unit could asynchronously compute frontier from version N while another dispatches from shape version N+1. Require version-bound projections and dispatch reads that cannot combine semantic versions.

No additional technology or infrastructure decision is required to close these seams.
