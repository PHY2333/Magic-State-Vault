# Notes/WORKFLOWS/domain-contract.md

Repository Mapper 只建立知识事实和来源模型，不决定教学顺序，也不推断读者状态。

## 1. 输入与输出

读取 TASK、BRIEF、note types、目标文件、相关正式笔记、canonical/index 与任务来源。输出 `DOMAIN_MODEL.md`、`SOURCE_PACKET.md`。

## 2. 知识单元

每个单元记录 id、formal statement、conditions、canonical owner、source anchors 与 verification：`source-verified | calculation-verified | inference | unverified`。

## 3. 四类关系

- Formal dependency：`dependent | requires | reason`
- Explanatory dependency：`target_explanation | requires_reader_capability | reason`
- Motivational relation：`predecessor_problem_or_result | motivates | reason`
- Reference relation：`knowledge_unit | owner | owned_scope`

不得混为“前置”。

## 4. Explanatory premise inventory

对机制、等价、因果和保证关系登记 premise：

```md
| premise_id | statement | supports_claims | source_anchor | verification |
```

## 5. Canonical detail inventory

为可能需要展开的上游细节登记：

```md
| detail_id | topic | canonical_owner | available_depth | stable_anchor | local_restatement_allowed | notes |
```

`available_depth`：`statement | compact_derivation | full_derivation | example`。该表只供 Architect 选择解释深度，不决定教材顺序。

## 6. Source Packet

每项来源记录文件／文献、版本、位置、classification、supported claim、unsupported/missing 与 intended use。局部推导必须可复算。

## 7. 边界

Mapper 不得决定先讲什么、选择模式或解释深度、把 owner 当读者前置、把来源存在当 learner evidence、写教材开头，或因 guided note 局部重述就判重复错误。

## 8. 完成条件

- 目标表现所需单元覆盖；
- 四类关系方向明确；
- 关键 claims 有 premises；
- 可复用 detail owner 和已有深度已登记；
- 一般与 source-specific 分开；
- 约定已核对或标记；
- Architect 无需重新遍历仓库。
