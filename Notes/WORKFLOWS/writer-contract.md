# Notes/WORKFLOWS/writer-contract.md

本文件规定 Packet Builder、Reader Card Builder 与 Writer 的接口。

## 1. Packet Builder 输入

只在 `DESIGN_AUDIT.md: pass` 后运行。可以读取：

- 已通过的 `DIDACTIC_DESIGN.md`；
- `LEARNER_SNAPSHOT.md`；
- `SOURCE_PACKET.md`；
- `Notes/LANGUAGE_PROFILE.md`；
- 当前目标片段。

输出：

```text
PACKETS/Uxx.md
READER_CARDS/Uxx.md
```

## 2. Writer Packet 必须包含

- note type、entry mode、目标位置；
- reader entry capabilities；
- unit exit capability；
- phase 顺序；
- faceted concept actions；
- definition cards 的可执行版本；
- explanation claim ledger 的可执行版本；
- notation/load budget；
- 必须写出的数学与例子；
- source excerpts/anchors；
- opening、transition、link 与 language contract；
- forbidden language/topics。

## 3. Reader Card 必须包含

- reading situation；
- assumed entry capabilities；
- explicitly not assumed；
- expected exit capability；
- language register 摘要。

不得包含：

- packet phase 指令；
- claim ledger；
- 标准答案；
- source anchors；
- design/audit 状态；
- 旧正文评价。

## 4. Packet 必须删除

- canonical ownership；
- 仓库前置清单；
- “不是前置”“只在某处使用”；
- task status、agent、审批、audit；
- index/canonical 更新说明；
- 可被直接复制成维护者视角开头的句子。

目标旧片段只用于定位替换，不是语言风格来源。

## 5. Packet preflight

检查：

- 每个 capability 有 action；
- concept identity 与 context role 分开；
- definition cards 可执行；
- 每个 explanation claim 前提闭合；
- source anchors 足够；
- phase budget 与设计一致；
- language contract 完整；
- packet 单独阅读即可写作；
- reader card 不泄露答案。

## 6. Writer 强隔离

Writer 必须在新 subagent、独立会话或等价干净上下文中启动，只读取当前 packet、授权来源和目标片段。

不能保证隔离时，流程停在 `packet_ready`。

## 7. Staged draft

默认写入 `DRAFTS/Uxx.md`。Writer 不直接修改正式文件。

## 8. Writer 规则

- 严格遵守 phase 和 claim 首次允许位置；
- 句子层面可以自然重组，但不能改变 claim 依赖顺序；
- definition card 必须转成自然正文，不写表格字段；
- 遵守中文 language contract；
- 不通过“相关内容见……”逃避局部解释；
- 不重新设计 unit 或引入新概念；
- 信息不足时提出 packet 补充请求；
- 不顺手重写未授权段落；
- 正文不能显得像把 checklist 逐项改写成句子。

## 9. 交付

每个 unit 只报告：

- staged draft 路径；
- 完成的 exit capability；
- 是否请求 packet/design 变更；
- 尚未处理单元。
