# Notes/WORKFLOWS/cold-read-audit.md

Blind Reader 进行真正独立的冷启动阅读审查。它不核对 packet 是否执行，而判断正文是否实际像教材。

## 1. 允许读取

只读取：

- `READER_CARDS/Uxx.md`；
- `DRAFTS/Uxx.md`；
- `Notes/LANGUAGE_PROFILE.md`。

不得读取：

- packet；
- design、domain、learner snapshot；
- source packet；
- canonical/index；
- Contract Audit；
- 以前的 audit 结论。

## 2. Reader trace

逐段记录：

```text
读完本段后我知道什么？
本段要求我预先接受什么？
哪一句产生自然问题？
下一段是否回答或推进该问题？
我需要同时记住什么？
```

## 3. 审查项

### 3.1 首句与对象落点

- 第一句是否建立一个稳定对象；
- 是否无必要地处理术语多义；
- 是否像词典条目或百科摘要；
- 是否知道当前正在学习什么。

### 3.2 定义质量

- 是否同义反复或半定义；
- 是否能识别该对象；
- 是否能与相邻对象区分；
- 是否只补当前需要的深度。

### 3.3 隐含 claim premises

对每个“因为、所以、意味着、等价、保证”等句子，独立追问：

> 我凭前文为什么可以接受这句话？

若答案依赖 reader card 未授权、正文也未说明的事实，标记 hidden premise。

### 3.4 问题流与总体方向

- 问题是否真实产生；
- 工具是否在需求后出现；
- 局部解释后是否回到总体问题；
- 正文是否只是 checklist 的句子化。

### 3.5 认知负荷

- 一次新增多少对象、关系和符号；
- 是否有 consolidation；
- 是否需要回读才能知道代词和符号所指。

### 3.6 中文教材语体

- 是否自然统一；
- 是否中英混用；
- 标题是否像教材；
- 是否有 AI 技术说明口吻；
- 是否存在正确但没有形成理解的空泛句子。

### 3.7 Exit capability

在不看 packet 的情况下，正文是否足以让读者完成 reader card 中的出口能力。

## 4. 输出

生成 `COLD_READ_AUDIT.md`：

```yaml
status: pass | changes_required | blocked
reviewed_draft_revision: <n>
```

必须包含 reader trace、findings 和最终 verdict。

## 5. 路由

- 隐含前提、定义设计、问题流、负荷：Didactic Architect；
- 中文自然度和局部表达：Writer；
- reader card 与正文目标矛盾：Learner Modeler / Didactic Architect；
- blocker：用户。
