# Notes/WORKFLOWS/note-writing.md

本文件只规定复杂笔记任务的阶段、交接和停止条件。正文写法见 `Notes/WRITING_GUIDE.md`；规划、执行和检查细则分别见对应 contract。

## 1. 适用范围

必须使用本流程：

- 新增正式笔记；
- 整篇或大段重写；
- 长推导整理；
- 从论文或翻译迁移为概念笔记；
- 合并、拆分或重组学习路径。

可跳过本流程：改错字、修链接、移动文件、纯格式化，以及用户明确指定且不改变数学主线的短小局部修改。

## 2. 单次任务目录

复杂任务使用：

```text
Notes/WORKING/note-tasks/<task-id>/
├── TASK.md
├── CONTEXT.md
├── PLAN.md
└── REVIEW.md
```

只创建当前阶段需要的文件。该目录不属于正式知识，不进入主题索引，也不得被正式笔记引用。

## 3. 状态与阶段门

整体状态记录在 `TASK.md`：

```text
new
→ context_ready
→ plan_proposed
→ plan_approved
→ executing
→ review_required
→ done
```

规则：

- Context Builder 只能推进到 `context_ready`。
- Planner 生成 `PLAN.md` 后只能推进到 `plan_proposed`。
- 只有用户明确批准计划，才能进入 `plan_approved`。
- Executor 只有在计划已批准且上下文版本匹配时才能修改正式笔记。
- 草稿完成后进入 `review_required`；检查未通过或出现语义冲突时保持该状态，不得标记为 `done`。
- `done` 之前必须完成必要的索引更新，并清除未说明的 TODO、临时引用和工具痕迹。

用户批准计划的标准回复为：

```text
批准任务 <task-id> 的 PLAN，进入执行。
```

若 `CONTEXT.md` 被补充或重建，必须递增 `context_version`；已有 `PLAN.md` 自动失效，重新回到 `context_ready`。

## 4. 主流程

### 4.1 建立任务

由用户或 Sol 明确目标、当前卡点、范围、非目标和完成标准，创建 `TASK.md`。

### 4.2 构造上下文

Sol 按 `planning-contract.md` 读取仓库并生成 `CONTEXT.md`。此阶段不设计正文主线，不修改正式笔记。

### 4.3 生成计划

Pro 按 `planning-contract.md` 读取 `TASK.md`、`CONTEXT.md` 和必要材料：

- 上下文不足：只提出补充请求，不生成计划；
- 上下文足够：生成 `PLAN.md`，并保持 `approval: pending`。Planner 不能写仓库时，由用户或 Sol 原样保存计划，并把 `TASK.md` 改为 `plan_proposed`。

### 4.4 用户批准

用户检查主线、范围、拆分方案和关键数学承诺。未经明确批准，不得执行。收到标准批准语句后，Sol 可以只更新 `PLAN.md` 的 `approval` 与 `TASK.md` 的状态，然后进入执行前检查。

### 4.5 执行

Sol 按 `execution-contract.md` 做执行前检查，随后编辑正式笔记。发现需要改变主线、范围、证明策略或拆分方案时停止，并写入 `REVIEW.md`。

### 4.6 检查

复杂任务完成草稿后，将 `TASK.md` 改为 `review_required`，再按 `subagents.md` 做只读检查。Executor 负责修订；subagent 不改文件。

### 4.7 收尾

检查通过后：

- 必要时更新 `CANONICAL_KNOWLEDGE.md`；
- 必要时更新 `Notes/00-index.md`；
- 必要时更新论文关系文件；
- 将任务标记为 `done`；
- 说明任务目录是删除、暂留还是归档。

## 5. 强制交接

每个阶段结束时必须按 `AGENTS.md` 输出“流程回执”。“下一步唯一动作”只能指向紧邻的下一阶段，不得一次跨越多个阶段。

典型交接：

- `context_ready`：让 Pro 依据 `TASK.md` 与 `CONTEXT.md` 生成 `PLAN.md`。
- `plan_proposed`：请用户审阅并明确批准或要求修改。
- `plan_approved`：让 Sol 做执行前检查并执行。
- `review_required`：请用户或 Planner 决定列出的语义问题，或让 Executor 修复列出的实现问题。
- `done`：建议删除或保留任务目录，并给出下一项可独立开展的任务；不得自动开始该任务。
