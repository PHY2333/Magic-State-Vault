# Notes/WORKFLOWS/domain-contract.md

Repository Mapper 只建立知识事实和来源模型，不决定教学顺序，也不推断读者状态。

## 1. 输入与输出

至少读取：

- `TASK.md`、`BRIEF.md`；
- `Notes/NOTE_TYPES.md`；
- 目标文件、相关正式笔记、canonical/index；
- 任务指定来源。

输出：

- `DOMAIN_MODEL.md`；
- `SOURCE_PACKET.md`。

## 2. 知识单元

每个知识单元必须是可验证的具体内容：定义、公式、构造、证明步骤、约定、边界或 source-specific 事实。

每个单元记录：

- `id` 与名称；
- formal statement；
- conditions；
- canonical owner；
- source anchors；
- verification：`source-verified | calculation-verified | inference | unverified`。

`calculation-verified` 必须写出可以在任务中直接检查的局部计算，不得用模型记忆冒充来源。

## 3. 四类知识关系

### Formal dependency

```md
| dependent | requires | reason |
```

### Explanatory dependency

```md
| target_explanation | requires_reader_capability | reason |
```

这里的 capability 应尽量写明 facet，例如“能读取矩阵行的支撑”而不是笼统写“懂矩阵”。

### Motivational relation

```md
| predecessor_problem_or_result | motivates | reason |
```

### Reference relation

```md
| knowledge_unit | owner | owned_scope |
```

四类关系不得混为“前置”。

## 4. Explanatory premise inventory

对于任务目标中可能出现的机制、等价、因果或保证关系，Mapper 还应登记可用 premise：

```md
| premise_id | statement | supports_claims | source_anchor | verification |
```

例如：

```text
同一量子比特上的 X、Z 反对易；不同量子比特上的 Pauli 作用彼此对易。
```

这不是教学顺序，只是让 Didactic Architect 能建立 claim dependency closure。

## 5. Source Packet

每项来源记录：

- 文件或文献、版本；
- 稳定位置；
- classification：`source-derived | repository-derived | local-derivation | inference | unverified`；
- supported claim；
- unsupported or missing；
- intended use。

不得用模型记忆补齐来源缺口。推断与局部推导必须列出依据。

## 6. 边界

Repository Mapper 不得：

- 决定先讲什么；
- 选择讲解模式；
- 把 canonical owner 当成读者前置；
- 把来源存在当成 learner evidence；
- 写教材开头；
- 因 lesson 需要局部重述而判为重复错误。

## 7. 完成条件

- 目标表现所需知识单元已经覆盖；
- 四类关系方向明确；
- 关键 explanation claims 有 premise inventory；
- 一般结论与 source-specific 事实分开；
- 约定和条件已核对或标记；
- Didactic Architect 无需重新遍历整个仓库即可设计。
