# Structural Review: Project Map BMAD PRD

**Date**: 2026-09-01  
**PRD**: `prd-project-map-bmad-2026-09-01/prd.md`  
**Reviewer**: Qoder (structural reviewer gate)

---

## Verdict: **PASS**

All 7 structural tests satisfied. No phase-blocking blockers detected. Finalization may proceed pending prose/polish review.

---

## Critical Findings by Test

### TEST 1: SYSTEM COMPLETENESS ✅
**Requirement**: Can reader reconstruct complete modified method from PRD alone? All 8 sections A-J present with substantive content?

**Result**: PASS - All sections present with substantial detail:
- ✅ Section A (thesis/boundary): lines 10-26, clear棕色场 identity + 7 core principles
- ✅ Section B (baseline system): lines 29-96, complete Phase 1-4 workflow inventory with artifacts
- ✅ Section C (target skeleton): lines 98-242, full diagram visible including all native workflows as distinct nodes/clusters
- ✅ Section D (delta matrix): lines 244-267, node-by-node处置 with Preserve/Add/Re-route rationale
- ✅ Section E (concept state model): lines 270-296, adopted/candidate definitions with fields
- ✅ Section F (coordination semantics): lines 298-321, auto vs escalate conditions clearly bounded
- ✅ Section G (stage-1 mapping): lines 323-332, five properties mapped across lifecycle nodes
- ✅ Section H (validation plan): lines 335-349, qualitative criteria only
- ✅ Section I (open decisions): lines 351-361, honest acknowledgment of unresolved specificity
- ✅ Section J (handoff expectations): lines 364-393, downstream role responsibilities clarified
- ✅ Summary section: lines 395-411, reconstruction instructions explicit

**Evidence**: Mermaid diagram (lines 130-238) contains complete skeleton with ALL native workflows shown as distinct subgraphs/nodes. Reader can reconstruct system without external references beyond official BMAD docs for baseline details.

---

### TEST 2: AUTHORITY CONSISTENCY ✅
**Requirements checked**:
1. Asymmetric PRD→SPEC authority explicit? ✅
2. Multiple entry paths visible? ✅
3. Coordinator vs inner-loop boundary clear? ✅
4. Map adopted/candidate causal order correct? ✅
5. Execution state reconciliation clarified? ✅

**Findings**:

**Asymmetric Authority** (explicit, multiple locations):
- Line 21: "当 PRD 存在时，product-level 答案起源于 PRD；SPEC 从中推导。如果 SPEC 发现缺失的 product answer，先路由到 PRD Update，然后 re-derive SPEC"
- Line 109: English restatement in core principles
- Diagram line 159-161: PRD box shows "product-level answers originate here; if SPEC finds missing product answer → PRD Update → re-derive SPEC"
- **No ambiguity** found

**Multiple Entry Paths** (clearly visible):
- Lines 20, 86-88, 103-105, 144-148: Direct unit / SPEC-backed epic / Multi-epic project path documented at concept level and diagram level
- Diagram explicitly shows three parallel PATHS subgraph nodes

**Coordinator vs Inner Loop Boundary** (hard boundary preserved):
- Line 22: "Coordinator 选择 ACTION CLASS，而不是在已分派的内环中选择具体的 story key"
- Line 111: English statement + policy reference to sprint-status.yaml/stories.yaml deterministic selection
- Line 259: Table entry "**硬边界：Map 在内环确定性控制中零影响** | bmad-loop 硬不变量：control loop 中无 LLM"
- Diagram line 173: LOOP box explicitly states "Map has ZERO influence inside this inner loop"
- Line 319: "边界保证：Coordinato 和 Map 操作严格高于工作流分派。在 bmad-build、bmad-build-auto 和 bmad-loop 内部，没有任何改变"

**Map Causal Order** (reconciliation transaction as contract):
- Lines 115-124: Transaction protocol fully specified with 5-step flow
- Line 126: "Map Updates are workflow-boundary reconciliation edges, not agent memory rules"
- Diagram lines 140-141: CAND --> TXN --> ADOPTED visualized
- Line 263: Correct Course routes through reconciliation transaction as default causal order

**Execution State Reconciliation** (derived reality updates clarified):
- Line 113: "Deterministic runtime/story status (done/blocked/deferred) is derived reality, updated at workflow boundaries without Owner approval"
- Explicit distinction: semantic changes require authority approval, but runtime status is derived reality
- This prevents "adopted only after authority approval" blocking (addressing the identified issue)

**NO ISSUES FOUND** on Test 2.

---

### TEST 3: TARGET DIAGRAM RECONSTRUCTABILITY ✅
**Requirement**: Full target skeleton visible in diagram itself, not just delta table? Native workflows shown as distinct nodes/clusters?

**Result**: PASS

**Diagram completeness evidence** (lines 130-238):
- ✅ COORD subgraph with dispatch/escalate functions
- ✅ MAP subgraph with ADOPTED/CANDIDATE/TXN components
- ✅ PATHS subgraph with 3 entry path nodes
- ✅ P1_TOOLS subgraph with all 5 analysis tools (BS, FI, DR, PB, PF)
- ✅ P2_PLANNING subgraph with PRD/UX/SPEC as distinct nodes
- ✅ P3_SOLUTION subgraph with ARCH/EPIC/SPR as distinct nodes
- ✅ P4_IMPLEMENT subgraph with BUILD/BAUTO/LOOP/JJOIN/RETRO/CC as distinct nodes
- ✅ XS subgraph showing cross-cutting state preservation
- ✅ All arrows show data flow and evidence routing
- ✅ Backflow paths shown (CAND → PRD/ARCH/UX at lines 209-211)
- ✅ Join verification as distinct node (line 174), not Real-Chain module

**Native workflows as distinct nodes**: Every official BMAD workflow appears as its own subgraph or node, not collapsed. The diagram IS the complete skeleton, not a summary.

**NO ISSUES FOUND**.

---

### TEST 4: NO INVENTED SOLUTION MODULES ✅
**Requirement**: Stage-1 behaviors remain cross-cutting properties, not five separate modules/gates. Only one system-level addition (Project Map + Coordinator)?

**Result**: PASS

**Single addition stated explicitly**:
- Line 18: "单一系统级添加：只引入一个新增系统组件——Project Map（包含 adopted/candidate 两层状态）和 Advancement Coordinator 函数。没有并行错误分类层、证据边界协议、实时链模块、投资门或跨单元认知缓存等新模块"
- Line 246: "Preserve 是默认选项。唯一的 Add 是 Project Map 状态平面加上 Coordinator 功能。所有先前拒绝的模块仍然被拒绝"
- Line 401: Summary states "一个状态平面：两个类（adopted/candidate），一个 reconciliation transaction 连接它们"
- Line 402: "一个调度函数：Advancement Coordinator"

**Five Stage-1 properties NOT mapped one-to-one**:
- Section G (lines 323-332) explicitly shows each property realized BY existing nodes with reconciliation edges added, NOT new modules
- Example line 328: "结构错误的显式分类 | 现有的 build triage...保留；retro aggregate views | 是的——triage 已经分类和路由；这一方面保留不变"
- Table column "标准 BMAD 中已有满足" shows what's already sufficient
- Table column "目标系统中的实际差分" shows minimal augmentation

**NO INVENTED MODULES FOUND**.

---

### TEST 5: NO NUMERIC THRESHOLDS ✅
**Requirement**: Validation section H has qualitative criteria only, no percentages or sample counts?

**Result**: PASS

**Section H analysis** (lines 335-349):
- Line 341 success criteria: "实施前识别的关键依赖问题减少，而不会因误报导致过度延迟" — QUALITATIVE
- Line 342 success criteria: "在 join 点的提前验证捕获了原本会逃逸的 defects，减少了 downstream rework" — QUALITATIVE
- Line 343 success criteria: "大多数投资判断由协调员处理且质量良好；仅有真正不可逆的高成本决策上升到 Owner" — QUALITATIVE ("大多数" is not a numeric threshold)

**Explicit rejection of numeric thresholds**:
- Line 347: "**No invented numeric thresholds**：所有成功标准都是 qualitative observable tied to whether timing/decision would materially change next advancement and whether added ceremony/complexity has net value。Invented sample counts or percentages rejected."

**NO NUMERIC THRESHOLDS FOUND**.

---

### TEST 6: FIVE STAGE-1 BEHAVIORS MAPPED ACROSS SYSTEM ✅
**Requirement**: Not one-to-one module mapping; show which lifecycle nodes jointly realize each property?

**Result**: PASS

**Section G table** (lines 323-332) correctly maps each property across multiple nodes:

| Property | Nodes/E edges realizing it |
|----------|---------------------------|
| 持续结构认知 | Project Map adopted+candidate + **每个生命周期节点的 workflow-boundary reconciliation edges** |
| 结构错误分类 | 现有的 build triage + retro aggregate views |
| 复合现实验证 | 依赖/join 边界在 Map 中表示 + Coordinator 调度现有 verify/review/test + Retro仍是epic closure |
| 未知/证据边界 | Map 状态携带 evidence support + retro missing-evidence rule |
| 可辩护投资判断 | 区域成熟度转换处决策 + Coordinator/Owner judgment |

Each property clearly described as **cross-cutting realization** through existing nodes with Map augmentation, NOT new modules.

**NO ONE-TO-ONE MAPPING FOUND**.

---

### TEST 7: NULL HYPOTHESIS PRESERVED ✅
**Requirement**: Readiness extension, join timing, investment transitions start from current behavior observation, not implementing delta first?

**Result**: PASS

**Null hypothesis explicit statements**:
- Line 24: "验证意图（非承诺要求）"
- Line 337: "以下差分需要实证验证，null hypothesis 是维持现状（'evolution needed'仅在观察到需要变更的行为证据时成立）"
- Line 337 bold: "**Validation starts from current behavior observation, NOT implementing the delta first**"

**Per-delta null hypothesis preservation**:
- Line 341 readiness gate: "**首先观察**现有 readiness 门是否允许 work 通过，而这些 work 后来被 Map-visible unresolved cross-region dependencies 证明为不安全；**仅在证据不足或显示 live problem 时**consider extension"
- Line 342 join timing: "**首先观察**naturally occurring joins 和 late-discovery/rework；**仅在证据 insufficient 或显示 live gap 时**consider earlier intervention"
- Line 343 escalation threshold: "**首先观察**actual commitment decisions 和 escalation burden"

**Explicit collapse to status quo**:
- Line 345: "**空假设保持力量**：任何候选差分可以简化为'无需进化'如果现有机制证明充分。没有观测到的行为失败或摩擦值得改变。"
- Column 4 of validation table (lines 341-343): "崩溃条件（null hypothesis 获胜）" lists when to abort evolution

**NO DELTA-FIRST ASSUMPTIONS FOUND**.

---

## Overall Assessment

**Strengths**:
1. **Exceptional structural clarity** — all 7 tests passed with no ambiguities
2. **Authority directions explicit** — PRD→SPEC route back mechanism crystal clear
3. **Hard boundaries preserved** — Coordinator/inner-loop separation maintained with "zero influence" language repeated
4. **Single addition discipline** — genuinely only Project Map + Coordinator, not feature creep
5. **Null hypothesis honored** — all candidate deltas require observational evidence before implementation
6. **Diagram as complete specification** — mermaid graph contains full system skeleton, not summary
7. **Qualitative validation only** — section H rejects numeric thresholds explicitly

**No phase-blocking issues detected.**

**Recommendation**: APPROVE for Finalization. Prose polish and standard rubric can proceed separately.

---

## File Reference

**Reviewed file**: `_bmad-output/planning-artifacts/prds/prd-project-map-bmad-2026-09-01/prd.md`  
**Lines reviewed**: 1-415 (full file)  
**Key sections**: A(10-26), B(29-96), C(98-242), D(244-267), E(270-296), F(298-321), G(323-332), H(335-349), I(351-361), J(364-393), Summary(395-411)

---

**End of Structural Review**
