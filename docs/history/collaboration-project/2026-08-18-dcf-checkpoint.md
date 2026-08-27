# DCF 历史项目检查点

> 迁移自 `ai-collaboration-state` 的 project 事件。它描述的是旧 DCF 仓库在当时的观察位置，不代表“认知融接”的当前工程实现。

---

## DCF — `ysr7255007-maker/dcf-chatgpt-microcore`

- event_id: `928a79c3-073d-5f96-92cd-ef969c314365`
- occurred_at: `2026-08-18T00:00:00+08:00`
- branch: `main`
- commit: `7398adb6e5a06996f13070f2b6988be1dd33941a`

状态：tracked / observed

关注分支：`main`

最后确认提交：`7398adb6e5a06996f13070f2b6988be1dd33941a`

提交信息：`docs: add seam runtime fault revelation discipline`

GitHub 提交时间：`2026-08-08T22:33:41Z`

网页端确认日期：2026-08-18

本次检查性质：首次建立长期协作项目检查点；没有更早的 `/长期协作/` 项目 SHA 可供比较，因此本次只建立基线，不能表述为“今天发生了新的 GitHub 工程推进”。

### 当前已确认工程位置

根据 `AGENTS.md`、README 和 `docs/current-state.md` 的当前权威关系：

- `main` 是历史与事实母线，不是新 DCF 的旧代码结构母本；新原生实现从 `native/` 重新生长。
- Capability Discovery 已收口：Capability Registry v1 固定为 15 项；“现实闭环行动”继续保持 `DISCOVERY_DEFERRED`。
- 当前普通后台架构已经收敛到 `ECS / Shared World + Executable Semantic Seam + Standalone Minimal Realization + single-provider + Composition Compiler + Minimal Emergence Proof` 这一方向。
- 普通后台与 AI Workflow 保持分离；Conductor 仍属于 AI Workflow 专项方向，不作为整个 DCF 的统一运行时。
- 当前主要底层开放选择是 `Bevy ECS vs Flecs`，以及与之绑定的 Ordinary Backend 最终语言与运行形态。该层收口后，再回到 15 项 Capability 逐项定稿。
- Godot 仍是高表现力实时交互运行时强候选，但尚未决定成为唯一 Surface Runtime。

### 当前仍可见的维护 / 验收工作

GitHub 仍有面向既有浏览器 DCF 的真实验收与维护工作，例如 Issue #70（全功能真实浏览器验收）和 Issue #68（BrowserClaw 维护 harness）。这些 Issue 是当前仓库中的真实开放事项，但不得反向覆盖 `docs/current-state.md` 对新 DCF 架构与施工位置的当前定义。

### 下一次比较起点

下一次维护先比较：

`7398adb6e5a06996f13070f2b6988be1dd33941a..main`

只有出现新的提交或其他足以改变工程判断的 GitHub 变化时，才更新本项目检查点。
