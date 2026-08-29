# Notes/AGENTS.md

本文件是 Notes v6.1 的稳定入口。它规定模型路由、跨模型 handoff、Git 自动化、公式渲染和阶段门；详细合同位于 `Notes/WORKFLOWS/`。

## 1. 必读入口

涉及新增、重写、拆分、复杂推导、教学顺序或读者反馈时，依次读取：

1. `Notes/MODEL_ROUTING.md`
2. `Notes/OBSIDIAN_MATH.md`
3. `Notes/NOTE_TYPES.md`
4. `Notes/LANGUAGE_PROFILE.md`
5. `Notes/WORKFLOWS/authoring.md`
6. `Notes/WORKFLOWS/handoff-protocol.md`
7. `Notes/WORKFLOWS/git-automation.md`
8. 当前角色对应合同
9. 设计、写作或审查读者正文时再读 `Notes/WRITING_GUIDE.md`

错字、链接、frontmatter 和不改变学习路径的纯格式任务可走 `sol-only`。

## 2. 模型绑定

- Codex Sol：仓库勘察、来源核验、learner evidence、coverage、Pro request 编译、Pro artifact 接收、机械内容、合同审查、仓库适配、Git 写入和推送。
- ChatGPT Pro：整篇教学架构、核心正文、复杂推导和整篇最终教学审查。

凡 `MODEL_ROUTING.md` 判定为 Pro-required 的任务，没有真实 Pro artifact 时必须停止。Sol 不得用同模型 subagent 冒充 Pro gate。

## 3. 强制 handoff

每个模型完成自己的阶段后，必须给出下一模型可直接执行的完整提示词：

- Sol 只有在当前阶段已验证、commit 且 push 成功后，才能输出 Pro 提示词；
- Pro 必须生成约定 artifact，并在回复末尾输出 `NEXT_SOL_PROMPT`；
- 提示词必须包含 task、branch、commit、request/artifact 路径、下一角色、允许操作和停止点；
- 不允许只写“把文件交给 Pro”或“让 Sol 继续”。

跨模型细节见 `handoff-protocol.md`。

## 4. Obsidian 数学硬规则

所有读者可见 Markdown 必须使用：

- 行内数学：`$...$`
- 块数学：单独成行的 `$$` 开始与结束

不得使用 `\(...\)`、`\[...\]`、`/(...)` 或 JSON 双重转义后的 Markdown。每次保存 Pro draft、组装稿和正式写入后都必须运行 `Notes/TOOLS/check_obsidian_math.py`。失败即为 blocker。

## 5. Git 自动化

当 `TASK.md` 中 `automation.auto_commit` 与 `automation.auto_push` 为 `true`：

- Sol 在每个 Sol 阶段完成后自动 commit/push；
- 只提交 allowlist 内的任务文件和获授权正式文件；
- 不使用 `git add -A`；
- 不 push 到 `main`；
- 不 force push；
- push 失败时不得发出 Pro handoff；
- 正式整合可以在 Pro final pass 后自动发生，但只限任务已预授权且不涉及删除、移动、拆分、合并或改名。

## 6. 权威边界

发生冲突时：

1. 用户最新明确学习目标与文件级授权；
2. 已核对数学、来源和当前仓库事实；
3. 有证据的 learner capability；
4. 经 Sol 验证的 `PRO_DESIGN.md`；
5. Pro 起草的 reader-visible 正文；
6. `OBSIDIAN_MATH.md`、`LANGUAGE_PROFILE.md` 与 `WRITING_GUIDE.md`；
7. 通过的整篇 Pro review 与 Integration Preview。

Sol 可以因来源或数学问题阻止 Pro 设计，但不能自己改写教学架构。Pro 可以否决 Sol 的教学组织，但不能覆盖已核对事实。

## 7. Whole-note 规则

- unit pass 不等于 whole-note pass；
- coverage 只提供勘察假设；
- 整篇组装稿必须经过新的 Pro 会话终审；
- `status: reviewed` 只用于整篇通过并按同一指纹精确整合后；
- 未被 Pro whole-note review 覆盖的 legacy 内容不得混入 pass。

## 8. 用户决定边界

只有以下事项交用户：

- 删除、移动、拆分、合并或重命名正式文件；
- 改变学习目标或明显扩大范围；
- 两条互斥路线会形成不同长期知识结构；
- 关键来源冲突或缺失；
- 是否合并任务分支到主分支。

technical unit map、模式、depth、作者分配和普通返修由 Pro/Sol 按合同处理。

## 9. 阶段回执

Sol 回执必须在 push 成功后包含：

```md
### Notes v6.1 Handoff
- task_id：
- route：
- 当前状态：
- 分支：
- 已推送提交：
- 已完成产物：
- 数学渲染检查：
- blocker：
- 下一位执行者：
- 下一份 request：

### COPY THIS PROMPT TO <MODEL>
```text
<完整可执行提示词>
```
```

Pro 回执必须包含 artifact 下载入口以及 `NEXT_SOL_PROMPT`。不得在阶段门未满足时越级。
