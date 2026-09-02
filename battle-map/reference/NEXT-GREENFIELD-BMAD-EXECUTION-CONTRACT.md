# 下一轮绿地项目：BMAD 执行契约

这份契约不是新方法设计，而是下一轮绿地研发项目使用 Standard BMAD / BMAD Loop 时必须遵守的运行边界。它直接吸收旧 `battle-map-bmad` Hard Stop 暴露出的执行浪费与身份混乱。

## 1. 四重身份固定

| 对象 | 当前这一轮的身份 | 不得误认成 |
|---|---|---|
| Standard BMAD | 当前项目的现役推进方法；同时是研究材料 | 未来最终方法 |
| BMAD Loop | 当前项目的现役持续推进/恢复控制面；同时是研究材料 | Battle Map 的实现本身 |
| Battle Map | 目标方法与产品参考资料；未来推进手段的规格来源 | 当前已经可用的推进发动机 |
| 项目地图版 BMAD | 当前研发项目的目标产物 | 当前这一轮的执行方法 |

启动任何角色、Workflow、Agent 或 Review 前，都必须保留这个身份矩阵。若某项设计判断依赖“未来的项目地图版 BMAD 已经存在”，则该判断越界，必须退回当前 Standard BMAD 的现实能力重新判断。

## 2. 同角色上下文连续性

同一个 BMAD 角色在同一连续工作段内，默认复用同一个长期上下文/session，连续读取自己的前文、工件和已经形成的判断继续工作。

禁止把一个本应连续完成的角色工作反复拆成多个一次性 Agent，让每个 Agent 从同一个问题重新理解、重新生成、再互相覆盖。角色连续性优先于“每一步都 fresh context”。

只有以下边界允许主动换上下文：

- 角色发生变化，例如 Analyst → PM → Architect；
- 方法明确要求真正独立的 Review / Validation；
- 当前角色的一个完整职责已经结束，进入新的独立职责；
- session 损坏、上下文容量或工具故障使原会话无法可靠继续。

若必须换上下文，新会话必须先从该角色已经落盘的 durable artifact、状态和必要证据恢复当前位置；不得把“重新问一遍同样的问题”当作恢复机制。

## 3. Fresh context 的正确边界

Fresh context 只用于需要认知独立性的边界，而不是普遍的执行习惯。最典型的是独立 Review：Reviewer 不继承 Implementer 的主观推理，但读取其已落盘的规格、实现、测试与证据。

同角色连续施工则相反：应保留上下文中的因果链，避免重复支付理解成本。换言之：**角色内连续，角色间按需要隔离；施工连续，独立验证隔离。**

## 4. 研究与施工同时发生，但结论分层

当前 BMAD/BMAD Loop 的每一次真实推进，都同时产生两类结果：

1. **项目结果**：当前绿地研发项目真正向前推进了什么；
2. **研究结果**：BMAD/BMAD Loop 的哪种机制在真实推进中证明有价值、暴露代价或失效。

两类结果必须分开记录。不能因为某个 BMAD 机制当前可用，就直接把它写成未来项目地图版 BMAD 的设计；也不能因为 Battle Map 资料提出了某个理想能力，就假装当前 BMAD 已经具备它。

未来方法只吸收经过本轮真实研究确认的机制；Battle Map 参考资料同样可以被本轮证据修订。

## 5. 下一轮启动时的硬检查

绿地项目创建后，在第一个 Standard BMAD Workflow 开始前确认：

- 当前执行发动机仍是 Standard BMAD + BMAD Loop；
- `reference/BATTLE-MAP.md` 是目标参考，不是执行状态；
- 本文件已进入项目启动上下文；
- 每个 BMAD 角色有可复用 session 身份；
- 独立 Review 与同角色连续工作使用不同的上下文策略；
- 旧 `battle-map-bmad` 的 Project World、Story=Level、7 Epic/23 Story 不作为默认结构导入。

## 6. 一句执行判据

遇到“要不要开新 Agent”时先问：这是需要独立判断，还是同一角色在继续完成同一职责？前者切换上下文，后者保持原上下文。

遇到“这是谁的能力”时先问：这是当前 BMAD/BMAD Loop 已经具备的现实能力，还是 Battle Map 对未来发动机提出的目标能力？两者不得混写。

## 7. 研究结论的最小记录格式

每次从真实 BMAD 推进中抽取未来方法认识时，至少分开记录：

- `当前事实`：BMAD/BMAD Loop 实际做了什么；
- `研究判断`：这一机制为什么有效、代价是什么、边界在哪里；
- `未来候选`：是否值得项目地图版 BMAD 吸收；
- `证据位置`：对应 Workflow、工件、运行记录或失败现场。

没有真实推进证据时，只能保留为 Battle Map 目标假说，不能升级成对 BMAD 的研究结论。

## 8. 下一轮安装位置

本文件在当前可行性项目中作为冻结参考。创建真正的绿地研发仓库时，必须把这份契约复制为该项目的启动级规则，并接入 Standard BMAD/BMAD Loop 的角色启动上下文；仅留在参考目录而不进入运行上下文，不算落实。

## 9. 验收失败条件

出现以下任一情况即视为执行契约未落实：同角色无必要频繁重开一次性 Agent；Review 与施工上下文混成同一主观链；把 Battle Map 目标能力当成当前 BMAD 事实；把 BMAD 当前行为未经研究直接升级为未来设计；新绿地项目启动时未加载本契约。

## 10. 与 BMAD Loop 的关系

BMAD Loop 的职责是让这些连续角色状态可恢复、可暂停、可继续，而不是通过不停创建新 Agent 来模拟“自治”。自治的衡量标准是项目能够沿 durable state 自己推进，不是 Agent 数量或上下文刷新次数。

## 11. 纠错优先直接修正，不制造复审循环

总工程师或上层监督已经能确定正确答案时，不要求角色重新研究、重跑同一 Workflow 或再次独立生成同一问题。应直接把具体错误、正确边界和必要修改告诉当前角色，并在原 session 中完成纠正。

纠错按成本分三级：

- **明确小错**：事实措辞、无依据扩张、遗漏边界、明显误读等，直接给出正确答案并修改；
- **局部理解偏差**：说明错在哪里、正确关系是什么、哪些内容保留，要求角色基于现有上下文局部修正；
- **实质性目标/结构偏离**：只有当现有证据不足以确定答案，或角色对目标、事实来源、核心结构的理解已经失真时，才要求重新研究或重新执行相应 Workflow。

独立 Review 的价值是发现未知问题，不是把已经确定的修改再包装成“重新研究 → 重写 → 再挑刺”的循环。纠错目标是最短路径恢复正确状态，同时保留角色上下文与已完成的有效工作。
## 12. Standard BMAD 完整角色链的样本有效性

本轮以 BMAD 本身为研究材料，因此正式规划与施工链必须保留 Standard BMAD 的角色层，不能只调用角色名下的 Workflow skill。

对存在对应正式角色的阶段，默认调用顺序为：

`激活对应 bmad-agent-* → 在同一角色 session 内 dispatch 对应 Workflow → 角色持续承担该职责直到阶段结束`

例如：

- Analyst：先激活 `bmad-agent-analyst` (Mary)，再由该 session dispatch Product Brief / Research 等 Analyst 职责；
- PM：先激活 `bmad-agent-pm` (John)，再由该 session dispatch PRD / Epics & Stories / readiness 等 PM 职责；
- Architect、Dev 等角色遵循同一原则。

直接调用 `bmad-product-brief`、`bmad-prd` 等 Workflow 可以作为显式的简化路径或对照实验，但不得被视为 Standard BMAD 的完整行为样本，也不得在本轮正式链中替代角色激活。若已经产生工件，应保存为非 canonical research baseline，不作为后续正式输入。

Headless / Fast path / Coaching path 属于 Workflow 自己提供的合法运行模式，不与“是否激活 Agent”混为一谈；研究记录必须注明实际采用的模式，以便判断行为来自角色原则、Workflow 规则还是运行模式。

## 13. Context 生命周期以岗位为单位，而不是以 Skill 为单位

BMAD Help 中“每个 skill 推荐 fresh context”在 Agent 模式下不得机械理解成“岗位内部每调用一个附属 Skill 就重开上下文”。Agent 激活文档明确规定：角色 persona、persistent facts 与岗位身份在 session 内持续生效，后续调用的岗位菜单 Skill 由同一角色 dispatch，并继续携带该 persona。

因此本项目采用的完整行为解释为：**岗位切换时建立 fresh context；同一岗位内部，在同一 context 中连续调用该岗位职责下的相关 Skill，直到该岗位本轮职责完成。** 例如 Mary 激活后，可在同一 Analyst session 内连续执行 Deep Recon、Product Brief、必要的 Advanced Elicitation 等；进入 John/PM 时才建立新的 PM context。

独立 Review/Validation 若方法要求认知独立，可另开 fresh context；这属于验证角色/职责边界，不改变岗位内部连续性。



## 14. 正式 BMAD 岗位必须驻留在交互式 Qoder/tmux 会话

正式 BMAD 运行以“岗位级持久交互会话”为 canonical execution surface：每个岗位建立一个 tmux 会话，在其中启动 Qoder 交互 CLI；该岗位的 Agent 激活、菜单选择、slash Skill、Workflow 交互、纠错与恢复都在同一个 Qoder 进程/context 内连续完成，岗位职责结束后才关闭并切换到下一岗位。

`qodercli -p/--resume` 不是正式 BMAD 主链的默认执行面。实测表明 fresh `-p` 可以加载 Skill，但 Harness activation 事件写入 stderr 而不进入 stream-json 主流；同时信任门、slash 展开、交互状态等控制面在非交互调用中不可直接观察，且已出现 Deep Recon Skill 已激活但模型只输出启动语句即结束的非完整执行。故在单独证明某个非交互动作等价之前，只将 `-p` 用作探针、批处理或明确的辅助动作。

监控正式岗位时必须同时观察：tmux pane 可见交互状态、Qoder session transcript、stderr/Harness activation、VIP socket/route 与项目工件。不得再仅凭 JSONL 主流判断“Skill 是否调用”。

## 15. Qoder 正式岗位采用 Harness-native Agent 运行投影

在 Qoder 上执行正式 BMAD 岗位时，优先使用 Qoder 原生 Session Agent（`--agent`）承载岗位人格与高优先级运行约束，而不是仅依赖普通 Skill 调用后的上下文服从。

BMAD 的 `bmad-agent-*` Skill 仍是方法层权威资产；Qoder Agent 是由该资产解析/编译得到的运行时投影，不反向改写 Standard BMAD 定义。这样既保留 BMAD 的跨 Harness 可移植性，也利用 Qoder 原生 system-prompt 层提高岗位身份和 activation 协议的执行可靠性。

岗位 Agent 在同一持久 tmux/Qoder session 内调用原版 Workflow Skills。若某个 Workflow Skill 自带局部 persona，导致模型在该环节暂时改用 Workflow 身份，但其任务职责、输入输出、控制流和工件仍正确执行，则当前 Standard BMAD 实验不因此中断；应记录为原版组合语义缺陷并继续推进。

正式阻断条件是：人格覆盖导致岗位职责丢失、Workflow 路由错误、必要状态/证据遗失、错误工件进入 canonical 下游，或无法返回岗位控制流。单纯称谓/局部身份漂移不是阻断条件。

未来项目地图版 BMAD 再处理该缺陷：岗位身份作为持久层，Workflow 作为临时能力层，并由显式 activation state / workflow return state 保证组合与恢复。
## 16. 完整 BMAD 研究基线禁止用 Headless 替代交互式岗位流程

Headless 是 BMAD 的合法自动化模式，但不是 Product Brief、PRD 等交互式规划 Workflow 的行为等价物。Headless 契约明确要求“不要询问，利用现有输入自行完成 intent”；因此它会主动压缩 Discovery、追问、假设确认、用户判断、草稿审阅和 Finalize，不能用来代表 Standard BMAD 在正常人机协作下的完整方法能力。

本项目研究 Standard BMAD 时，Analyst / PM / UX / Architect 等规划岗位默认必须使用持久交互 session，并遵守 Workflow 自己的自然轮次：intent → workspace/draft skeleton → Discovery → working mode → 岗位判断/用户交互 → draft → review/reconcile → Finalize。不得为了减少轮次把整个阶段写成一条“自动完成所有事情”的总提示词。

Headless 只用于以下情况：输入、目标和决策边界已经被冻结的批处理；经单独验证与交互流程语义等价的机械步骤；或明确标记的对照实验。任何只在 Headless 样本中出现的过度规格化、方案补齐、路径猜测或工具捷径，在交互模式复现前不得升级为 BMAD 方法缺陷。

跨岗位交接必须显式携带上游 canonical artifact 的确切路径；下游岗位不得因为缺少交接信息而自行猜 `product-brief.md`、`prd.md` 等名字。若 Workflow 自带内容扫描规则，应按内容识别工件而不是依赖文件名模式；若没有，则由运行层/role registry 提供 canonical path。

## 16. 岗位职责与 Workflow 边界必须从 Standard BMAD 原文解析

不得凭角色名称、传统软件阶段印象或总工程师自己的抽象，预先规定 Analyst/PM/UX/Architect/Dev “只能做什么”。正式运行前，以对应 `bmad-agent-*`、实际被 dispatch 的 Workflow Skill、以及 Standard BMAD 官方 planning/build 文档为权威解释。

BMAD 的职责结构是“文档/决策有主权，探索与验证可重叠”：Brief 可广泛 discovery 与初步验证；PRD 继续 discovery 并把 what/why 压成组织产品契约；UX 可领先、跟随或独立；Architecture 默认 Coaching，棕地先调查真实代码，重大调用需向用户展示取舍；Epic/Story 创建逐步协作并要求显式批准；Readiness 是跨 PM/Architect 的实现边界；Build 先调查并形成可批准 spec，再实现与 review；Retrospective 判断跨 Story 的 epic 整体；Correct Course 负责重大变更的跨工件导航。

因此监督重点不是限制探索范围，而是检查：事实/判断/假说/正式承诺是否区分，写入是否落在正确权威工件，Workflow 规定的人类批准点是否真实发生，以及 Headless 是否被误用来替代本应交互的认知过程。


## Interaction batching for owner decisions

Interactive BMAD remains multi-round. Do not collapse discovery, coaching, planning, or design into a one-shot headless completion. However, adapt the human interaction surface to this project: within each cognitive round, collect all currently known owner-level questions and present them together, grouped by theme, instead of serially asking one question per turn.

The supervising assistant resolves questions already answered by durable owner decisions, project evidence, or low-risk defaults. Only genuinely owner-level unresolved decisions are escalated. Batch questions, not conclusions: do not guess answers merely to reduce the batch, and do not skip later rounds when new evidence creates new questions.
