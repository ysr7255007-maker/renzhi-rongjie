# DeepSeek Harness 环境与三级闭环实测

日期：2026-08-27

## 结论

本机 DeepSeek Harness 已达到“认知融接”第一阶段自举所需的执行与证据底座要求。三级结构已经用真实 Agent、真实工具调用和数据库关系跑通；当前唯一不能直接由官方 Workflow 满足的核心要求是跨进程可恢复的 Durable Workflow。

## 本机基线

- DeepSeek Harness：`0.1.1-rc.2`
- 现有 Web：`127.0.0.1:3080`，验收时 HTTP 200
- 权限预设：`danger-full-access`
- 默认 Agent preset：已从 `minimal` 调整为 `standard`
- 默认模型：`deepseek-v4-flash-vision-exp`
- reasoning effort：`high`

官方 `workflow` 工具、`dsh-workflow-worker-thread`、Session Persistence、Session Query 等包均已随当前 DSH 安装存在。官方 Workflow 已实测可并行启动子 Agent，并在父 Session 中留下完整 workflow 生命周期事件。

## 认知融接专用 Profile

建立本机 Profile：`~/.dsh/profiles/renzhi-rongjie`。

- bundles：`@deepseek-ai/dsh-base` + `@deepseek-ai/dsh-headless`
- 额外依赖：`@deepseek-ai/dsh-session-persistence-sqlite@0.1.1-rc.2`
- 禁用默认 JSONL Session Persistence
- 原始 Session 事件数据库：`~/.dsh/renzhi-rongjie/session-events.sqlite3`
- SQLite 使用 WAL；持久化强度由官方 provider 负责
- Workflow worker-thread 与 `workflow` 工具保持启用

## Workflow 与证据实测

第一次 Workflow 验收强制主 Agent 使用 `workflow` 并并行启动 A、B 两个子 Agent。实际结果：

- 父 Session 记录 `tool/call(workflow)`；
- 记录 `tool-workflow/run-start`；
- 记录两个 `tool-workflow/agent-start`，并带真实 `childId`；
- 两个子 Session 均有 `parent_session` 指向父 Session，`delegation_depth=1`；
- 两个 `agent-end` 均为 `completed`；
- `run-end.stopReason=completed`；
- `tool/result` 返回 A=`L1_A_OK`、B=`L1_B_OK`。

在认知融接专用 SQLite Profile 中重复验证后，Session 数从 1 增至 4：一个新的父 Session、两个 Workflow 子 Session，加上此前基线 Session；workflow 生命周期事件全部可直接 SQL 查询。

## 三级闭环实测

第一层执行 AI 在临时工作区读取 `numbers.txt`（2、3、4），创建 `sum.txt`，再通过重读文件与 `awk` 独立重算两条渠道验证结果为 9。Harness 保存了真实 reasoning、tool/call、tool/result、step/turn 事件。

第二层叙事 AI 不读取执行者汇报，直接读取 DSH SQLite 中指定父 Session 的真实 workflow/tool 事件，并把中文因果叙事写入独立语义数据库。结果：3 段中文叙事、9 条 `session_id:seq` 证据引用；每条引用均重新查询 DSH 原始数据库确认存在。
第三层总工程师 AI 只读叙事库，不读 DSH 原始事件，然后分别写入：

- `execution_decision`：面向第一层的工程方向/约束；
- `narrative_calibration`：面向第二层的观察/采样/叙事方法校准。

两类记录分别通过 `active_execution_decisions` 与 `active_narrative_calibrations` View 提供给下一轮对应角色。另一轮 Agent 实测证明，执行层只读执行 View、叙事层只读校准 View 时均能正确取得各自信息。

最终验证：

- 语义数据库 `PRAGMA integrity_check = ok`；
- DSH Session SQLite `PRAGMA integrity_check = ok`；
- 叙事孤立证据关系 = 0；
- 决策孤立叙事关系 = 0；
- 校准孤立叙事关系 = 0；
- 9/9 个叙事证据引用均能解析回真实 DSH Session Event。

## 当前缺口

官方 `dsh-workflow` 当前明确没有 workflow journaling/resume：脚本、中间值和子任务进度不会形成可跨进程恢复的 Workflow checkpoint。Session 本身是 durable 的，Workflow 的显示事件也是 durable 的，但进程被杀后不能继续原 workflow run。

因此目前结论是：

`DeepSeek Harness 执行层 + SQLite 证据源 + 二/三层 AI` 已成立；`Durable AI Workflow` 尚未成立。

下一步优先路线仍是：先尝试在 `ctx.workflowEngine` seam 后实现/接入可恢复引擎；若代价不合适，再让 DBOS 作为 Durable Workflow 内核接回 DSH。

## 数据库边界

实测中直接 SQL 读取 DSH SQLite 适合验证，但正式叙事插件不应依赖其当前物理 schema。官方 SQLite provider 会打包 chunk、压缩大 payload，且处于 pre-release。正式接缝应优先通过 DSH 的 Session Persistence / Query 服务读取逻辑事件，以稳定的 `session_id:seq` 作为证据身份；认知融接自己的叙事、决策和校准关系放在独立语义数据库中，避免向 DSH 内部数据库添加自定义表。
