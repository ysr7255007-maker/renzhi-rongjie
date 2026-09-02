# 项目地图版 BMAD：项目级执行规则

- 当前这一轮的现役推进方法是 Standard BMAD；BMAD Loop 只在它真实负责的 implementation phase 接管持续施工与恢复。
- Standard BMAD 与 BMAD Loop 同时是研究材料。观察到的当前事实、对机制的研究判断、未来方法候选和证据位置必须分开记录。
- `reference/BATTLE-MAP.md` 是目标方法/产品参考与未来发动机的规格来源，不是当前已经存在的执行能力。
- 本轮目标产物是“项目地图版 BMAD”；只有本轮完成并冻结后，下一轮才能把它当成推进发动机，禁止追溯性自举。
- 旧 `battle-map-bmad` 的 Project World、Story=Level、7 Epic/23 Story 等 Hard Stop 设计不作为默认输入或答案。
- 同一个 BMAD 角色在同一连续职责内必须复用同一 Qoder session；角色变化或真正独立 Review/Validation 才切换上下文。切换后从 durable artifacts 恢复，不重新生成同一问题。
- 对存在正式 BMAD 角色的阶段，必须先激活对应 `bmad-agent-*`，再由该角色在同一 session 内 dispatch 其 Workflow；直接调用 Workflow 只允许作为显式简化/对照样本，不能代表正式 Standard BMAD。
- 每个 Workflow 开始前读取 `reference/NEXT-GREENFIELD-BMAD-EXECUTION-CONTRACT.md`；涉及 Battle Map 目标语义时读取 `reference/BATTLE-MAP.md`。
- 不把局部真实链成功写成整体结构已认证；所有结构判断保留证据覆盖范围、剩余未知和可撤销性。
- 纠错遵循最短路径：上层已经能确定答案时，直接在当前角色原 session 中指出错误与正确边界并局部修正；只有目标、事实来源或核心结构确实失真且现有证据不足时，才重新研究或重跑 Workflow。
- Context 生命周期以岗位为单位：岗位切换时 fresh context；同一岗位激活后，在同一个 session 内连续 dispatch 该岗位相关 BMAD skills，直到岗位职责完成；不得把每个附属 skill 机械理解成需要新窗口。
- 正式 BMAD 岗位必须运行在持久 tmux + Qoder 交互 CLI 中；岗位内 Agent/Skill/Workflow 全部在同一交互进程继续。`qodercli -p/--resume` 仅用于经验证的辅助/探针动作，不作为正式 BMAD 主链。
