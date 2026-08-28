# Notes/WORKFLOWS/authoring.md

本文件规定 Notes v5 主流程。模板集中在 `task-artifacts.md`。

## 1. 适用范围

完整流程用于新增或大段重写、调整教学顺序／entry mode／文件类型、长证明、论文导读，以及用户反馈“像百科、术语突然、局部懂但目标丢失、解释过长或重复”。短小不改变主线的修正可简化。

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
├── INTEGRATION_PREVIEW.md
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
→ integration_previewed
→ integrating
→ published
```

任意阶段可进入 `blocked`；published 后可因读者反馈进入 `reopened`。

## 4. 主流程

### Brief

把“理解 X”改成可观察表现，并限定当前主问题。

### Domain mapping

输出知识单元、来源、四类关系、explanatory premises 和已有 canonical detail inventory。

### Learner snapshot

建立 faceted capability snapshot。Evidence state 不决定解释深度。

### Didactic design

决定 note type、entry mode、units/phases、concept actions、definitions/claims、explanation depth、detail placement、mainline contract、notation/load 与语言合同。

### Design audit

独立检查 claim closure、depth、主线比例与 duplication rationale。

### Packet 与 Reader Card

编译隔离 Writer packets 和 Blind Reader cards。

### Staged drafting

Writer 在新上下文中逐 unit 写入 DRAFTS，默认不修改正式文件。

### Contract Audit

检查数学、来源、definition/claim、depth placement、phase 和 mainline contract。

### Blind Cold-Read Audit

只读 reader card、draft 和语言规范；检查真实阅读、mainline latency、比例性与 optional skip test。

### Manuscript Verdict

两道审查均 pass 才得到 manuscript pass。

### Integration Preview

只读生成仓库适配方案；不得更改已通过文本。若需要 reader-visible 改动，返回 design/writer 并重新双审查。

### Integration

Preview ready 后写入正式文件，删除旧竞争文本并处理链接、index、canonical。

## 5. 内部返修

同一次运行默认允许三轮 design/manuscript 返修。相同 major 仍未闭合则 blocked，并说明根因。

## 6. 用户决定边界

只有文件结构、学习目标、互斥长期路线、关键来源冲突或新外部研究需要用户决定。用户不负责逐项审批 learner state、depth 或 claim ledger。

## 7. 阶段门

- mapped 前不得设计顺序；
- learner_ready 前不得推断掌握；
- design_validated 前不得生成 packet；
- packet_ready 前不得启动 Writer；
- 双审查前不得修改正式笔记；
- manuscript pass 前不得做 integration preview；
- preview ready 前不得写正式文件。

## 8. 失败路由

| 问题 | 返回阶段 |
|---|---|
| 数学、来源、约定、detail owner | mapped |
| learner facet 错配 | learner_ready |
| definition、claim、depth、mainline、模式、负荷 | designed |
| packet/reader card 缺失或污染 | packet_ready |
| 局部正文执行 | drafting |
| 仓库重复、链接、索引、ownership | integration preview / integrating |

## 9. Retention

`retain_mode: full | summary`。Pilot 保留全部；正式发布任务可只保留 summary、verdict、preview 与 integration report。
