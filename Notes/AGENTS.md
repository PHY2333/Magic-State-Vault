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
- **Repository Mapper**：建立 `DOMAIN_MODEL.md` 与 `SOURCE_PACKET.md`，不设计教学顺序。
- **Learner Modeler**：建立 faceted `LEARNER_SNAPSHOT.md`，只依据证据。
- **Didactic Architect**：设计 units、phases、讲解模式、concept actions、definition cards、explanation claims 和语言合同。
- **Design Auditor**：独立审查设计；不写正文。
- **Packet Builder**：把通过的设计编译成 `PACKETS/` 与 `READER_CARDS/`。
- **Writer**：在干净上下文中只读取当前 packet、授权来源和目标片段，生成 staged draft。
- **Contract Auditor**：读取 packet、来源和 draft，检查数学、claim ledger 与合同执行。
- **Blind Reader**：只读取 reader card、draft 和语言规范，进行真正的冷启动阅读审查。
- **Manuscript Gatekeeper**：合并两道独立审查，生成 `MANUSCRIPT_VERDICT.md`。
- **Repository Integrator**：最终 verdict 通过后写入正式文件并处理链接、索引与 canonical。

这些是逻辑角色，可由主 agent、subagent 或多次独立调用承担。角色边界不能因工具限制而省略。

## 3. 权威顺序

发生冲突时按以下顺序处理：

1. 用户最新的明确学习目标与范围；
2. 已核对来源、数学事实和当前仓库事实；
3. 有证据的 faceted learner capability；
4. 已通过 `DESIGN_AUDIT.md` 的教学设计；
5. 当前 Writer packet；
6. `Notes/LANGUAGE_PROFILE.md` 与 `Notes/WRITING_GUIDE.md`；
7. 仓库整合规则。

不得静默调和冲突。来源或数学冲突返回 mapping；读者状态冲突返回 learner model；教学顺序、claim closure 或定义问题返回 design。

## 4. 三类上下文隔离

### 4.1 Writer

Writer 必须在新 subagent、独立会话或等价干净上下文中工作，只可读取：

- 当前 `PACKETS/Uxx.md`；
- packet 授权的来源片段；
- packet 指定的目标正文片段；
- packet 内嵌的语言规范子集。

Writer 不得读取 Brief、Domain、Learner、Design、canonical、index 或 audit。

### 4.2 Contract Auditor

可以读取：

- 当前 packet；
- packet 授权来源；
- staged draft；
- `Notes/LANGUAGE_PROFILE.md`。

不得读取 Blind Reader 的结论后再形成首次 verdict。

### 4.3 Blind Reader

只可读取：

- `READER_CARDS/Uxx.md`；
- `DRAFTS/Uxx.md`；
- `Notes/LANGUAGE_PROFILE.md`。

不得读取 packet、design、domain、source、canonical、index、Contract Audit 或此前的审查结论。

若环境不能保证相应隔离，流程停在前一阶段；不得用同一污染上下文伪装独立审查。

## 5. 内部返修

非阻塞问题在同一次任务中自动返回正确阶段修复并重新审查。

只有以下情况需要用户决定：

- 删除、移动、合并、拆分或重命名正式文件；
- 改变学习目标或显著扩大范围；
- 两条互斥路线会产生不同长期知识结构；
- 来源冲突或缺失使关键承诺无法确定；
- 需要新增外部研究任务。

## 6. 正式文件与任务文件

- 正式 Notes 不得引用 `Notes/WORKING/`。
- 任务产物只放在 `Notes/WORKING/authoring-tasks/<task-id>/`。
- Writer 默认只写 staged drafts；正式文件由 Integrator 修改。
- `CANONICAL_KNOWLEDGE.md` 管理知识归属；`Notes/00-index.md` 管理读者路线。
- 发布后按 `retain_mode` 处理任务产物，不在正式目录积累教学脚手架。

## 7. 阶段回执

```md
### Notes v4 流程回执
- task_id：
- 当前状态：
- 已完成产物：
- design 返修次数：
- manuscript 返修次数：
- blocker：
- 下一位角色：
- 下一步唯一动作：
```

不得在阶段门未满足时自动越级。
