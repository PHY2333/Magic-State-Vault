# Notes/AGENTS.md

本文件是 `Notes/` 的稳定入口。它只负责路由、角色边界、权威顺序和上下文隔离；模板与检查项在 `Notes/WORKFLOWS/`。

## 1. 必读入口

涉及新增、重写、拆分、教学顺序或读者反馈时，先读取：

1. `Notes/NOTE_TYPES.md`
2. `Notes/LANGUAGE_PROFILE.md`
3. `Notes/WORKFLOWS/authoring.md`
4. 当前角色对应 contract
5. `Notes/WRITING_GUIDE.md`，仅在设计、写作或审查读者正文时读取

错字、链接和不改变知识引入顺序的纯格式修改可跳过完整流程。

## 2. 角色

- **Orchestrator**：维护状态机、分配角色和返修路由；不替代专业角色直接写正文。
- **Repository Mapper**：建立 `DOMAIN_MODEL.md` 与 `SOURCE_PACKET.md`，登记来源、premises 和已有 canonical detail，不设计教学顺序。
- **Learner Modeler**：建立 faceted `LEARNER_SNAPSHOT.md`，只依据证据。
- **Didactic Architect**：设计 units、phases、讲解模式、definition/claim ledger、explanation depth、mainline contract 与 detail placement。
- **Design Auditor**：独立审查设计；不写正文。
- **Packet Builder**：把通过的设计编译成 `PACKETS/` 与 `READER_CARDS/`。
- **Writer**：在干净上下文中只读取当前 packet、授权来源和目标片段，生成 staged draft。
- **Contract Auditor**：读取 packet、来源和 draft，检查数学、claims、depth、mainline 与合同执行。
- **Blind Reader**：只读取 reader card、draft 和语言规范，进行冷启动阅读与比例性审查。
- **Manuscript Gatekeeper**：合并两道独立审查，生成 `MANUSCRIPT_VERDICT.md`。
- **Repository Fit Planner**：在 manuscript pass 后只读正式仓库，生成 `INTEGRATION_PREVIEW.md`；不写正式文件。
- **Repository Integrator**：preview ready 后按预览写入正式文件并处理链接、索引与 canonical。

这些是逻辑角色，可由主 agent、subagent 或多次独立调用承担。角色边界不能因工具限制而省略。

## 3. 权威顺序

发生冲突时按以下顺序处理：

1. 用户最新的明确学习目标与范围；
2. 已核对来源、数学事实和当前仓库事实；
3. 有证据的 faceted learner capability；
4. 已通过 `DESIGN_AUDIT.md` 的教学设计；
5. 当前 Writer packet；
6. `Notes/LANGUAGE_PROFILE.md` 与 `Notes/WRITING_GUIDE.md`；
7. 已通过的 `INTEGRATION_PREVIEW.md`；
8. 仓库整合规则。

不得静默调和冲突。来源或数学冲突返回 mapping；读者状态冲突返回 learner model；定义、claim、解释深度或主线比例返回 design。

## 4. 上下文隔离

### Writer

只可读取：当前 packet、packet 授权来源、目标正文片段和 packet 内嵌语言子集。不得读取 Brief、Domain、Learner、完整 Design、canonical、index 或 audit。

### Contract Auditor

可读取：当前 packet、授权来源、staged draft 和语言规范。不得先看 Blind Reader 的 verdict。

### Blind Reader

只可读取：Reader Card、Draft、语言规范。不得读取 packet、design、domain、source、canonical、index、Contract Audit 或旧 audit。

### Repository Fit Planner

只在 manuscript pass 后读取：通过的 drafts、目标正式文件、note type、通过设计中与目标 unit 对应的 depth/placement ledger、index/canonical 和相关链接。Ledger 只用于核对 duplication rationale；不得更改 reader-visible text，发现需要文本变化时返回设计阶段。

若环境不能保证相应隔离，流程停在前一阶段。

## 5. 内部返修

非阻塞问题在同一次任务中自动返回正确阶段修复并重新审查。只有以下情况需要用户决定：

- 删除、移动、合并、拆分或重命名正式文件；
- 改变学习目标或显著扩大范围；
- 两条互斥路线会产生不同长期知识结构；
- 来源冲突或缺失使关键承诺无法确定；
- 需要新增外部研究任务。

## 6. 正式文件与任务文件

- 正式 Notes 不得引用 `Notes/WORKING/`。
- 任务产物只放在 `Notes/WORKING/authoring-tasks/<task-id>/`。
- Writer 默认只写 staged drafts；Integrator 才修改正式文件。
- `CANONICAL_KNOWLEDGE.md` 管理知识归属；`Notes/00-index.md` 管理读者路线。
- 发布后按 `retain_mode` 处理任务产物。

## 7. 阶段回执

```md
### Notes v5 流程回执
- task_id：
- 当前状态：
- 已完成产物：
- design 返修次数：
- manuscript 返修次数：
- integration preview 状态：
- blocker：
- 下一位角色：
- 下一步唯一动作：
```

不得在阶段门未满足时自动越级。
