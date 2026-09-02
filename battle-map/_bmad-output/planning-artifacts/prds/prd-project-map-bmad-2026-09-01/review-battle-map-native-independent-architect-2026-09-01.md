# Battle Map PRD 架构审查报告

**审查者**: Winston (独立架构审查者)  
**审查日期**: 2026-09-01  
**审查对象**: /Users/looy/.dsh/renzhi-rongjie-labs/bmad-battle-flow/project-map-bmad/_bmad-output/planning-artifacts/prds/prd-project-map-bmad-2026-09-01/prd.md  
**源材料**: BATTLE-MAP.md, brief.md, addendum.md  

---

## 总体判决

### ✅ 有条件通过

PRD 在**外部本体清理**和**七层架构完整性**上表现良好，但在**数据流闭环的操作性定义**、**自动关联的越权边界落实**、**认知运行时组合模型与 BMAD 角色复用的冲突处理**、**推进发动机与施工内环的调度隔离硬约束**等关键结构性问题上仍缺少足够的实施级规范。这些问题不是语义不清，而是会导致下游实现出现**职责争夺**、**状态漂移**或**人工介入点模糊**的系统性风险。

---

## 系统主骨架复述（证明理解）

根据 PRD 文档，当前体系由以下主骨架构成：

### 核心主语：Project Map（战役地图）
- **表达内容**: project goals → complete functions → regions → milestones → structure relations → frontier → evidence boundaries → unknowns
- **用户接口**: 单一 Project Map 界面，通过 action class selection（explore/shape/implement/verify/close）分发工作
- **目标**: 让人工和自动化围绕同一张结构图讨论，成为人机公共认知表面

### 七层架构层次

| Layer | 名称 | 核心职责 |
|-------|------|----------|
| L7 | Source/Adapter Layer | 翻译原始执行事件到统一格式（BMAD artifacts、Git、tests、reviews、harness） |
| L6 | Execution/Verification Runtime | Worker Executors、Deterministic Inner Loops、Terminal Status Writers |
| L5 | Composable Cognitive Runtime | Persona Manager、Authority Scope Resolver、Skill Bundle Loader、Handoff Contract Enforcer、Session Identity Manager |
| L4 | Advancement/Command Engine | Advancement Coordinator 选择哪个 worker 运行、Bootstrap Compiler 组装上下文快照 |
| L3 | Project Weaving/Auto-Association | Triggers、Incremental Delta Reader、Fact Extractor、Auto-Association Engine、Narrative Synthesizer |
| L2 | Project Map Core/Semantic DB | Semantic DB + Materialized Views（current state、region details、frontier blockers、adopted/candidate structures） |
| L1 | Experience/Projection Layer | UI projection of current state + next-move rationale |

### 数据/控制流主环

```
User opens Project Map → System presents actions → User selects/dispatches work
→ Advancement Coordinator reads Map DB & compiles bootstrap context
→ Worker executes through deterministic workflow → Produces terminal status
→ Weaving triggers on artifact changes → Performs incremental delta read
→ Auto-associates facts to Project Map → Updates candidate deltas/narrative
→ Materialized views refresh → Next move rationale presented
```

**关键断言**: 
- Coordinator chooses WHICH worker runs; Worker's internal logic remains fully deterministic with NO influence from Project Map
- Weaving feeds information only; NEVER makes route selections or adopts structural changes autonomously
- Candidate ≠ Adopted; semantic state transitions governed SEPARATELY by evidence criteria and proper authority

---

## 阻断性结构问题（必须修正才能落地）

### #1. 自动关联引擎的"高置信度直接提交"规则与"语义状态转变权限分离"原则存在不可调和冲突

**位置**: PRD Section F.4 (lines 451-470)

**问题描述**:
F.4 写道:
> "High-confidence associations COMMIT TO DB immediately... Strong factual matches (spec says X, implementation implements X verified by test)"

但 K.1-K.2 明确声明:
> "CANNOT conclude function complete, change milestone status, or adopt structural changes merely because association strength is high... Semantic state transitions governed SEPARATELY by evidence criteria and proper authority/adoption processes"

**矛盾点**:
- "Commit to DB" vs "Cannot change milestone status":如果 fact extractor 将"spec says X + implementation implements X verified by test"作为 STRONG confidence commit 到 DB，这**本身**就改变了 L2 中该节点的支持证据计数、evidence coverage materialized view、以及 frontier computation 的输入
- 即使不显式标记 "complete"，**隐式地**增加证据权重已经影响 downstream queries（如 `get-relevant-evidence-unknowns` 返回的 evidence refs 列表）、`getting-started-view` 编译的 context、以及 coordinator 选择 next action 时的 evidence-gap analysis
- F.6 的 candidate output format 有 `awaiting_validation_by` 字段，暗示需要 validation；但 F.4 又对 strong facts 说直接 commit——**validation 发生在哪里？何时触发？谁执行？**

**系统性风险**:
1. **Weaving 获得隐性权力**: 虽然 F.6 说 weaving never executes，但 F.4 的"commit links and provenance only"本身就是一种 execution——它修改了 semantic DB 的状态，而 downstream consumers（coordinator、UI、bootstrap compiler）会立即看到这个变化
2. **Evidence coverage drift**: 随着时间累积，大量"strong factual matches"被 commit 后，materialized views 可能显示"X conditions covered"，但实际上这些覆盖关系未经 owner/coordinator validation，可能与真实情况不符
3. **Escalation threshold bypass**: G.3 定义了 escalation to owner 的场景（product meaning judgment、irreversible commitments 等），但如果 weaving 通过大量 strong facts commit 隐性塑造了 map state，owner 的决策实际上基于一个未经验证的投影

**需要的结构修正**:
必须在 F.4 增加**明确的 authority gate**:
```yaml
# Proposed addition to F.4
CRITICAL DISCIPLINE:
- High-confidence links COMMIT ONLY PROVENANCE EDGES, NOT SEMANTIC STATE
- Provenance edges = "fact F derived from source S at time T with confidence C"
- Semantic state transitions (evidence coverage increment, milestone status change, frontier shift) require EXPLICIT coordination via:
  a) Advancement Coordinator evaluation (for routine evidence integration within policy bounds)
  b) Owner authority approval (for escalations per G.3 thresholds)
- Weaving output format distinguishes:
  - provenance_only: <links only, no state impact>
  - semantic_delta: <requires validation before state change>
```

**为什么这是阻断性的**: 如果不澄清这一点，L3 和 L4 的职责边界就是模糊的——weaving 到底"只 feed 信息"还是"actually modifies state"？实现团队会得出不同结论，导致系统行为不一致。

---

### #2. Session Continuity Rules 与 Composable Runtime 假设存在冲突

**位置**: PRD Section H.1-H.4 (lines 606-682) vs Agents.md (line 17)

**问题描述**:
Agents.md 第 17 行明确要求:
> "同一个 BMAD 角色在同一连续职责内必须复用同一 Qoder session；角色变化或真正独立 Review/Validation 才切换上下文。切换后从 durable artifacts 恢复，不重新生成同一问题。"

但 H.1-H.4 描述的 composable runtime 假设是:
> "At action dispatch time: Runtime composes persona + authority + skill + workflow + handoff + session_identity... Worker spawns with composed role bound to execution lifecycle."

**矛盾点**:
1. **Session identity 的来源**: H.4 的例子中说`session_identity = story-implementer-{story-id} session token`，但这暗示每 storiesession 创建一个新 token。而 Agents.md 要求同一角色（如 implementer）**在同一连续职责内复用同一 session**——这意味着如果 Epic A 包含 Story 1/2/3，implementer 应该用同一个 session 贯穿三个 story，而不是每个 story 一个新 token
2. **Context restoration vs session reuse**: Agents.md 说"切换后从 durable artifacts 恢复，不重新生成同一问题"——这意味着 context switching 时，新 session 应该从 SPEC.md/terminal status/architecture spine 读取状态并继承之前 session 的认知。但 H.4 的 bootstrap compilation (G.4) 只提到"FROZEN SNAPSHOT at dispatch time"，没有说明如何跨越多个 story/epic 保持 continuity beyond the snapshot
3. **Coordinator session lifespan**: H.1 说 Advancement Coordinator 的 session identity 是"Coordinator Instance Lifespan"——这意味着 coordinator 应该是一个长期运行的实体，在不同 action class 之间保持会话。但如果 coordinator 调用 implementer worker，而 implementer 又是"每个 story 一个新 session"，那么 coordinator 如何确保 implementer 从 previous story 的 durable artifacts 恢复 context？

**系统性风险**:
1. **Context fragmentation**: 如果每个 story 都 fresh bootstrap 而不复用 prior session 的认知，会出现"记忆丢失"——implementer 可能重复问过之前 already answered 的问题，或者忽略 prior story 的 learning
2. **Token waste**: 违反 Agents.md 的 continuity rules 意味着每次 switch 都要重新 load 整个 workspace context，造成 token 浪费
3. **Coherence loss**: Agents.md 设计 continuity rules 是为了跨 multi-turn conversation 保持 depth。如果 composable runtime 的 session spawning 忽略这一点，会破坏 BMAD Loop 已验证的最佳实践

**需要的结构修正**:
必须在 H.1-H.4 增加**与 Agents.md 的兼容层**:
```yaml
# Proposed clarification in H.1
Session Identity Policy:
- Role activation follows Agents.md continuity rules: same role in same continuous responsibility REUSES same Qoder session
- Session boundary occurs only when:
  a) Genuine role transition (implementer → verifier)
  b) Independent review/validation required (build completes → review starts)
  c) Durable artifact recovery point reached (epic closure, sprint boundary)
  
- Session identity encoding:
  - story-implementer-{story-id}: NEW session IF this story requires fresh implementer perspective
    (e.g., cross-story defect found in prior story → new implementer needed for independent fix)
  - epic-implementer-{epic-key}: REUSED session across multiple stories WHEN:
    * Stories share same region/concern
    * No independent review triggered between stories
    * Continuous implementation flow maintained
    
- Context restoration protocol:
  - On session resume: read durable artifacts (SPEC.md, terminal status, prior memlog entries)
  - Reconstruct prior judgments/questions/insights BEFORE presenting bootstrap context
  - Avoid regenerating questions already answered in prior session
```

**为什么这是阻断性的**: 如果不解决这个冲突，实现团队会不知道如何在 composable runtime 的灵活性与 Agents.md 的硬性 continuity requirement 之间取舍。最终可能导致系统行为违背 BMAD 已验证的最佳实践。

---

### #3. "Deterministic Inner Loop Guarantee"缺乏对 LLM 调用的硬隔离实现规范

**位置**: PRD Section I.2 (lines 702-720)

**问题描述**:
I.2 声称:
> "Hard invariant: Once worker starts execution, NO external system influences its internal decision-making logic."

并列出了 forbidden 和 allowed 操作。但这是一个**行为断言**而非**实现规范**。问题是：
1. **如何 enforce?** 如果 worker 是"AI coding session"，而这个 session 本质上是 LLM 驱动的，那么"NO LLM calls in orchestration loop"的边界在哪里？Worker 内部可以有 LLM 调用（否则如何实现 coding？）；协调器如何选择不让orchestration LLM call 干扰 worker 的 deterministic loop？
2. **Disposable worker sessions 的定义**: I.2 说"LLMs run only inside disposable coding-CLI sessions spawned by orchestrator"——但什么是"disposable"？是：
   - 每个 worker invocation 创建新 process？
   - 每个 worker 有独立的 environment variables / git repo / tmux session？
   - 还是只是逻辑上的隔离（如不同的 system prompt）？
3. **Real-time Map state pulls 的检测**: I.2 禁止"Real-time Map state pulls during worker execution"——但如果 worker 的代码中调用了某个 API，而这个 API 的内部实现读取了 Map DB，这算违规吗？如何静态/动态检测？

**系统性风险**:
1. **Orchestration contamination**: 如果边界不够硬，Coordinator 可能在 worker execution 过程中间接影响其 decision logic（如通过共享状态、环境变量、或 API hook）
2. **Non-deterministic behavior**: 如果 worker 的"internal logic"受到外部影响，会导致 build results 不可预测——同样的 story 在不同时间运行产生不同结果
3. **Accountability ambiguity**: 当系统出现 bug 时，无法定位责任归属——是 worker 实现错误，还是 coordinator/orchestration污染了 worker 的决策空间？

**需要的结构修正**:
必须在 I.2 增加**实现级隔离规范**:
```yaml
# Proposed addition to I.2
Process Isolation Model:
- Each worker runs in CONTAINERIZED ENVIRONMENT (tmux multiplexed detached session OR Docker-like sandbox)
- Container lifecycle:
  - Spawn: orchestrator creates isolated container with frozen bootstrap context (read-only mount)
  - Execution: container has NO NETWORK ACCESS to Project Map DB or Coordinatorendpoints
  - Termination: container dumps terminal status + artifact diffs → orchestrator consumes → container destroyed
  
- LLM Call Boundary:
  - Worker internal LLM calls ALLOWED within container process
  - Orchestration LLM calls FORBIDDEN (no coordinator agent polling/injecting during worker execution)
  - Detection mechanism: network egress rules block outbound requests to Map DB/coordinator endpoints
  
- State Isolation Guarantees:
  - Worker reads SNAPSHOTS compiled at dispatch (immutable after spawn)
  - Worker writes ONLY to its own writable mount (isolated from main repo until commit)
  - No shared mutable state between coordinator and worker processes
```

**为什么这是阻断性的**: 这是一个 safety critical 的 invariant（"deterministic inner loop"是整个方法可靠性的基石）。如果没有实现级的隔离规范，团队会写出各种"差不多隔离"的方案，最终导致 invariant 被打破。

---

### #4. 项目语义 DB 的 Query Model 缺少对"Candidate vs Adopted"状态的并发访问一致性保证

**位置**: PRD Section E.2-E.3 (lines 362-397)

**问题描述**:
E.2 定义了多个 queries，其中`get-adopted-candidate-structures`同时返回 adopted 和 candidate 状态。E.3 的 materialized views 包括 MV4 ("Adopted/Candidate Structures")。

但在实际运行时，会有以下并发场景:
1. **Weaving 写入 candidates**: L3 的 weaving 持续输出 candidate deltas，更新 MV4
2. **Coordinator 读取 candidates 做决策**: L4 的 coordinator 调用`get-adopted-candidate-structures`来评估 available action classes
3. **Owner 批准/reject candidates**: 当 owner 做出 adoption/rejection 决定时，MV4 需要从"candidate"迁移到"adopted"或关闭 candidate

**问题**:
- **Read-modify-write race**: 如果 coordinator 读取 candidate list 时，weaving 正在添加新的 candidate，coordinator 看到的可能是"inconsistent snapshot"（部分看到旧 candidate，部分看到新 candidate）
- **Adoption side effects**: 当 owner 批准一个 candidate，这个 action 可能触发 downstream consequences（如刷新其他 materialized views、trigger other workers）。但这些副作用应该在"adoption transaction"中原子执行，还是异步 propagate？
- **Bootstrap consistency**: G.4 说 bootstrap 是"FROZEN SNAPSHOT at dispatch time"。但如果 coordinator 在 compiling bootstrap 时，weaving 正在修改 candidate list，worker 收到的 context 是否与 coordinator 决策时的 state一致？

**系统性风险**:
1. **Decision-context mismatch**: Coordinator 基于 candidate A+B 决定 dispatch worker W，但 worker 启动时 candidate B 已被 weaving 移除（或被 owner reject），导致 worker 接收的 context 与实际 frontier 不符
2. **State divergence**: Materialized views 不一致导致 UI 显示的 candidate 列表与 coordinator 内部状态不同步，user 看到混乱的界面
3. **Non-deterministic bootstraps**: Worker 的 bootstrap context 依赖于 coordinator 读取时机，如果 weaving 的 timing 变化，同样的 user action 可能触发不同的 worker context

**需要的结构修正**:
必须在 E.2-E.3 增加**并发一致性协议**:
```yaml
# Proposed addition to E.2
Query Consistency Model:
- All queries return SNAPSHOT ISOLATION consistent at query start time T
- Snapshot stored as immutable versioned object (snapshot_id = hash(state_at_T))
- Weaving updates create NEW versions only at well-defined checkpoint boundaries:
  - After batch processing complete (not incrementally per-fact)
  - Version number incremented atomically
  
- Coordinator reads must use:
  - Pre-dispatch snapshot: coordinator captures snapshot_id BEFORE evaluating action classes
  - Bootstrap compiles FROM THAT SAME snapshot_id (not re-read live DB)
  - Worker receives snapshot_id in bootstrap (provenance for reproducibility)
  
- Adoption transactions:
  - When owner approves/rejects candidate, execute as ACID-like transaction:
    1. Validate candidate still exists (optimistic locking)
    2. Apply state transition (candidate → adopted OR close candidate)
    3. Trigger materialized view refreshes as part of same transaction
    4. Emit event "adoption_complete {snapshot_id}" for downstream consumers
  - If validation fails (candidate removed by weaving), abort and re-present to owner
```

**为什么这是阻断性的**: 并发一致性是 distributed system 的基本功，但 PRD 把 Project Map DB 当作"single source of truth"却没有定义它的 consistency model。实现团队会各自实现，导致 race condition 和 non-deterministic behavior。

---

## 重要但非阻断结构问题（应在下一轮 PRD 修订中解决）

### #5. Layer 1 UI 与 Layer 2 DB 的耦合过紧，违反分层原则

**位置**: PRD Section L1 (lines 189-198)

**观察**: L1 的 UI components（Global Project View、Regional Drilldown、Frontier Visualization 等）直接映射到 MV1-MV7 materialized views。虽然这在性能上有好处（预计算加速查询），但造成了:
- UI 概念直接渗透到 DB schema（MV3 "Frontier Blockers"是为 UI 服务的，还是通用 query？）
- 如果有多个 different UI clients（web dashboard、CLI interface、mobile app、API consumers），每个 client 都需要自己的 MV 集吗？
- **更严重的是**: L1 的描述中有"Next Move Recommendation"（UI8），但 recommendation 的逻辑应该在 L4（Coordinator），L1 只负责 display。如果 MV7 "Current Action + Escalation Contract"是 pre-computed in L2，那就把 L4 的逻辑下沉到了 L2，违反分层职责。

**建议修正方向**:
- 澄清哪些 MV 是通用 query optimization（L2 职责），哪些是特定 UI 的 optimization（应移到 L1 或 client layer）
- Next Move Rationale 的计算必须保留在 L4，L1 只渲染 coordinator 返回的结果

---

### #6. Evidence Coverage 的"覆盖范围"概念缺少形式化定义

**位置**: PRD Section B.7 (lines 85-102)

**观察**: B.7 定义了 Evidence Coverage 的五个维度（implementation verified locally、integration verified at join points、full chain verified end-to-end、performance/scalability verified、review/approval completed），但这些都是**二元判断**（verified / not verified）。

然而在实际系统中，coverage 应该是**程度性的**:
- "Local verified"意味着什么？单元测试通过？手动测试？还是 developer assertion？
- "Integration verified at join points"——如果 A→B→C是一条链，A→B verified 但 B→C 还没跑过，coverage 是多少？
- **Missing dimension**: "Evidence freshness"—昨天的 coverage 和今天的 coverage 可能不同（如果代码改变了），但系统没有 tracking evidence validity period

**潜在影响**:
- Frontier computation 依赖 coverage 状态（blocked vs ready）。如果 coverage 被错误标记为"full chain verified"，可能会错误地把 dependent work 标记为 ready
- Owner 投资决策依赖 accurate coverage picture。如果 coverage inflated，可能导致 premature formal investment

**建议修正方向**:
- 引入 coverage confidence score（如 0-1 连续值，或 low/medium/high三档）
- 定义 evidence decay mechanism（如 code change invalidates previous coverage）
- 区分"evidence exists"和"evidence applicable to current state"

---

### #7. Narrative Synthesis 的因果连续性缺少对"false positive narrative entry"的处理

**位置**: PRD Section F.5 (lines 471-489)

**观察**: F.5 定义了 narrative entry 的结构（prior judgment → triggering event → new judgment → impact），但没有说明如果"new judgment"后来被证明是错误的怎么办。例如：
1. Weaving 发现"A 的实现不符合 spec X"，创建 narrative entry 认为"需要修 spec 或修实现"
2. Owner 基于这个 narrative 做出 decision（如决定修 spec）
3. 后来发现 weaving 的判断错了（其实是实现符合 spec，只是 weaving 误读了 spec）

**问题**: Narrative 应该有"retracted"或"overridden"状态，但 F.5 没有定义。

**建议修正方向**:
- 增加 narrative entry 的生命周期状态（created → reviewed → acted-upon → closed/retracted）
- 允许后续 narrative entry override 先前 entry（形成 narrative chain）
- UI 展示时应高亮"resolved"vs"open"narrative

---

### #8. 七层架构缺少"Observability/Ops Layer"

**位置**: 整体架构缺失

**观察**: 七层架构描述了功能层面的 data/control flow，但没有:
- How do operators monitor weaving backlog?
- What happens if worker execution hangs?
- How to debug why coordinator made a certain decision?
- Metrics to track: candidate accumulation rate、average time from candidate creation to owner decision、worker success/failure rates

**建议新增 Layer 0 或横切 concern**:
```yaml
Layer 0: Observability & Operations
- Event logging: all state transitions logged with timestamp + actor + snapshot_id
- Health checks: weaving queue length、worker pool status、db replication lag
- Debug query APIs: trace narrative evolution for specific node、replay weaving decisions
- Alerting: candidate retention > X days、weaving error rate > Y%、coordinator escalation backlog
```

这不是阻断性的（系统可以 without monitoring tools 运行），但对于 production deployment 是必要的。

---

## 已经成立、不应再改回去的关键设计

### ✅ L7-L6-L5 的"执行/认知/指挥"三层分离保持了良好的职责边界

PRD 清楚地区分:
- L7 (Sources): 只做 event translation，不干涉业务逻辑
- L6 (Execution): deterministic inner loop，零 orchestration LLM calls
- L5 (Cognition): composable roles，但不决定 action selection

这个分离防止了"orchestration LLM contaminating execution loop"的经典反模式。**应维持**。

---

### ✅ L3 Weaving 的"Candidate vs Adopted"双状态模型是对的

尽管 F.4/F.6 的实施细节需要澄清（见#1），但**双状态模型的 principle 是正确的**:
- Candidate 允许"immediate capture of findings without claiming authority"
- Adopted 保持"decisions surviving validation process"
- 两者同时可见，user 理解 settled vs debated

**应维持**,只在细节层面修正。

---

### ✅ Terminal Status Semantics 的四值分类（OK/FAILURE/BLOCKED/PARTIAL）简洁有效

I.3 的 terminal status 模型避免了 over-complicated 的状态机，四个值覆盖了所有可能性，并且每个值都有明确的 handling policy:
- OK → continue to next action
- FAILURE → triage findings, decide whether to retry/block
- BLOCKED → escalate to human/orchestrator
- PARTIAL → partial progress noted, may continue later

**应维持**,不需要扩展到更多状态。

---

### ✅ G.4 Bootstrap Compilation 的"FROZEN SNAPSHOT"原则是正确的

G.4 强调 bootstrap 是 dispatch time 的 snapshot，不是 bi-directional sync 或 live pulling。这保证了:
- Worker 有 coherent context that won't shift beneath it mid-run
- Deterministic reproducibility（同样的 snapshot → 同样的 worker execution）
- Clear boundary between coordinator (pre-execution) and worker (during execution)

**应维持**,这是 I.2 的 deterministic inner loop invariant 的前提条件。

---

## 建议的最小结构修正

基于以上分析，我建议按优先级执行以下最小修正：

### P0（必须在进入下一阶段前完成）

#### 修正 1: 澄清 F.4 的"high-confidence commit"规则
- 增加 provenance-only vs semantic-delta 的区分
- 明确 validation trigger 和 authority gate

#### 修正 2: 对齐 H.1-H.4 的 session 策略与 Agents.md
- 引入 session reuse policy
- 澄清 context restoration protocol

#### 修正 3: 增强 I.2 的 isolation 实现规范
- 定义 container/process isolation model
- 明确 LLM call boundary 的 enforcement mechanism

#### 修正 4: 补充 E.2-E.3 的并发一致性协议
- Snapshot isolation guarantee
- Versioned materialized views
- Atomic adoption transactions

### P1（建议在 UX Design 阶段前完成）

#### 修正 5: 解耦 L1 UI 与 L2 MV 的直接映射
- 区分通用 MV vs UI-specific optimization
- 确认 Next Move Rationale 计算位置在 L4

#### 修正 6: 形式化 Evidence Coverage 的语义
- 引入 confidence scoring
- 定义 evidence decay mechanism

#### 修正 7: 扩展 Narrative 生命周期管理
- 增加 retracted/overridden 状态
- 支持 narrative chain tracing

### P2（可选，production deployment 前建议完成）

#### 修正 8: 新增 Observability Layer
- Event logging schema
- Health check endpoints
- Debug query APIs

---

## 结语

这份 PRD 在**外部本体清理**上做得非常好——七层架构清楚地表达了"battle-map-native"的身份，BMAD 机制被定位为"internal reference engine"而非用户 vocabulary。Stage-1 target behaviors 的 validation observation model 也体现了 null hypothesis discipline（默认不进化，除非 evidence 证明必要）。

主要问题集中在**L3-L4-L5 的交叉地带**：weaving、coordinator、composable runtime 之间的职责边界需要更硬的规范，否则实现团队会走样。这些问题不是设计缺陷，而是 specification granularity 不足。

建议在进入 UX Design 阶段前，至少完成 P0 修正，确保结构可行性再投入 UI/interaction design。
