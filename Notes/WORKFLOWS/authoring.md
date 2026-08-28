# Notes/WORKFLOWS/authoring.md

本文件规定 Notes v4 主流程。模板集中在 `task-artifacts.md`。

## 1. 适用范围

完整流程用于：

- 新建正式笔记；
- 整篇或大段重写；
- 调整教学顺序、entry mode 或文件类型；
- 长证明、论文导读或来源转写；
- 用户反馈“像百科”“术语突然出现”“知道局部但失去目标”“模型默认我会很多东西”“句子正确但不像教材”。

错字、链接和不改变数学主线及引入顺序的短小修改可简化。

## 2. 任务目录

```text
Notes/WORKING/authoring-tasks/<task-id>/
├── TASK.md
├── BRIEF.md
├── DOMAIN_MODEL.md
├── SOURCE_PACKET.md
├── LEARNER_SNAPSHOT.md
├── DIDACTIC_DESIGN.md
├── DESIGN_AUDIT.md
├── PACKETS/
├── READER_CARDS/
├── DRAFTS/
├── CONTRACT_AUDIT.md
├── COLD_READ_AUDIT.md
├── MANUSCRIPT_VERDICT.md
├── INTEGRATION_REPORT.md
└── AUTHORING_SUMMARY.md
```

只创建当前阶段需要的文件。正式笔记不得链接任务目录。

## 3. 状态机

```text
brief_ready
→ mapped
→ learner_ready
→ designed
→ design_validated
→ packet_ready
→ drafting
→ contract_audited
→ cold_read_audited
→ manuscript_validated
→ integrating
→ published
```

任意阶段可进入 `blocked`；published 后可因读者反馈进入 `reopened`。

## 4. 主流程

### 4.1 Brief

用户只提供学习目标、目标材料和真实问题。Orchestrator 把“理解 X”改成可观察表现。

### 4.2 Domain mapping

Repository Mapper 输出 `DOMAIN_MODEL.md` 与 `SOURCE_PACKET.md`，包括知识单元、来源、四类关系和 explanatory premise inventory。

### 4.3 Learner snapshot

Learner Modeler 建立 faceted capability snapshot。缺少证据标 `unverified`；概念本身与当前角色分开。

### 4.4 Didactic design

Didactic Architect 决定：

- note type 与 entry mode；
- units、phases 与讲解模式；
- capability actions；
- definition cards；
- explanation claim ledger；
- notation/load budget；
- language contract；
- reader cards。

### 4.5 Design audit

Design Auditor 独立审查。可解决 major 自动返回 design；只有 blocker 询问用户。

### 4.6 Packet 与 Reader Card 编译

Packet Builder 生成隔离 Writer packets 和 Blind Reader cards，完成 preflight。

### 4.7 Staged drafting

Writer 在新上下文中逐 unit 写入 DRAFTS，默认不修改正式文件。

### 4.8 Contract Audit

Packet-aware 审查数学、来源、definitions、claims、phase 和语言合同。

### 4.9 Blind Cold-Read Audit

Blind Reader 在新上下文中只读取 reader card、draft 和语言规范。

### 4.10 Manuscript Verdict

Gatekeeper 合并两道独立审查。两者都 pass 才能进入 integration。

### 4.11 Integration

Integrator 将 staged drafts 写入正式文件，清除旧竞争文本，必要时更新 frontmatter、链接、index 和 canonical。

## 5. 内部返修

同一次运行内允许自动返修。默认最多两轮；两轮后仍有同类 major，标记 blocked 并说明根因。

## 6. 用户决定边界

只有以下情况询问用户：

- 删除、移动、合并、拆分或重命名正式文件；
- 改变目标或显著扩大范围；
- 两种设计形成不同长期学习路线；
- 关键来源冲突或缺失；
- 需要新增外部研究。

用户不负责逐项审查 learner state、claim ledger 或教学模式。

## 7. 阶段门

- mapped 前不得设计顺序；
- learner_ready 前不得推断读者掌握；
- design_validated 前不得生成 packet；
- packet_ready 前不得启动 Writer；
- 两道审查和最终 verdict 前不得修改正式笔记；
- integration 结束前不得标 published。

## 8. 失败路由

| 问题 | 返回阶段 |
|---|---|
| 数学、来源、约定 | mapped |
| learner facet 错配 | learner_ready |
| definition、claim、unit、模式、负荷 | designed |
| packet/reader card 缺失或污染 | packet_ready |
| 局部正文执行 | drafting |
| 链接、索引、ownership | integrating |

## 9. Retention

TASK frontmatter 可设：

```yaml
retain_mode: full | summary
```

- `full`：pilot 或研究性任务保留全部产物；
- `summary`：发布后保留 `AUTHORING_SUMMARY.md`、`MANUSCRIPT_VERDICT.md`、`INTEGRATION_REPORT.md`，其余过程文件在用户确认后删除或归档。
