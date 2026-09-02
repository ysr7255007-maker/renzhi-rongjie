# ADR-0002：自举阶段采用 DeepSeek Harness + SQLite 作为执行与证据底座

- 日期：2026-08-27
- 状态：accepted（自举阶段）

## 背景

认知融接第一阶段需要一个权限充分、可扩展、可观察的 AI Harness，同时需要让第二层叙事 AI 能从执行事实而非执行者汇报中恢复因果链。

本机 DeepSeek Harness `0.1.1-rc.2` 已实际验证其 Workflow、子 Agent、Session Event 和 SQLite Session Persistence 能力。

## 决定

自举阶段优先采用 DeepSeek Harness 作为第一层执行底座，并建立专用本机 Profile `renzhi-rongjie`：

- 使用官方 `dsh-base + dsh-headless`；
- 使用官方 `workflow` 工具与 worker-thread Workflow Engine；
- 使用官方 `dsh-session-persistence-sqlite@0.1.1-rc.2` 保存原始 Session Event；
- DSH 原始证据数据库与认知融接语义数据库保持物理分离；
- 证据关系使用稳定逻辑身份 `session_id:seq`；
- 第二层只做中文叙事与证据绑定；
- 第三层分别产生执行决策与叙事校准，并通过不同 SQL View 供两层消费。

## 已验证
真实实验已经跑通：

1. 主 Agent 调用 Workflow，并行启动两个真实子 Session；
2. 父子关系、Workflow 生命周期、工具结果全部进入 DSH SQLite；
3. 第二层 Agent 直接从 DSH 证据源生成 3 段中文叙事，并建立 9 条证据引用；
4. 第三层 Agent 只读叙事，分别写入执行决策与叙事校准；
5. 两个角色分别只读取自己的 active View，信息不会串线；
6. DSH 原始数据库与语义数据库完整性检查均通过，全部叙事证据引用可反查。

详细证据见：`docs/experiments/2026-08-27-deepseek-harness-three-layer-spike.md`。

## 未解决边界

当前官方 Workflow 不支持 journaling/resume，进程重启不能继续原 run，因此不能把现有 `dsh-workflow-worker-thread` 冒充 Durable AI Workflow。

下一步优先在 `ctx.workflowEngine` 接缝后寻找或实现 durable engine；若该路线不经济，则采用 DBOS 作为持久 Workflow 内核，再通过薄接缝接回 DeepSeek Harness。

本 ADR 只确定自举执行与证据底座，不把 DeepSeek Harness 永久绑定为认知融接不可替换的实现。
