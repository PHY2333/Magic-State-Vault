# Notes/WORKFLOWS/depth-and-mainline.md

本文件规定 explanation depth、detail placement、mainline contract 与 duplication rationale。

## 1. Explanation depth

Evidence state 不直接决定正文长度。每项需解释内容选择一种 depth：

- `use`：直接使用；通常要求 `operational/fluent`。
- `reminder`：一两句或一个公式恢复当前用法。
- `compact_derivation`：只写支撑主结论的少量关键步骤。
- `full_derivation`：完整展开；仅当推导本身是出口能力、错误风险高且无可替代桥梁时采用。
- `optional_derivation`：完整细节放可跳过块；主线保留必要桥梁。
- `upstream_bridge`：本地解释到足以继续阅读，再链接 canonical detail。
- `delay`：当前不引入。

## 2. Depth 选择依据

逐项判断：

- 是否直接属于 unit exit capability；
- 若省略会造成什么具体误解；
- learner evidence 与风险；
- 对主线的段落／符号成本；
- canonical 上游是否已有稳定推导；
- 是否需要在当前语境迁移，而非重新证明。

`unverified` 不得自动选择 `full_derivation`。

## 3. Detail placement

```text
mainline
optional_block
upstream_bridge
separate_derivation
delay
```

- `optional_block` 必须可跳过，且跳过后主线 claims 仍闭合；
- `upstream_bridge` 的本地句子必须独立成立，链接不能承担核心解释；
- `separate_derivation` 需要独立 note 或已有 owner；
- full derivation 在 guided reference 中重复 canonical 内容时必须给 duplication rationale。

## 4. Mainline contract

每个 unit 和 phase 记录：

```md
- main_question:
- mainline_result:
- supporting_details:
- return_to_mainline:
- latency_budget:
  - max_supporting_paragraphs:
  - max_new_notation_groups:
- optional_skip_test:
- proportionality_rationale:
```

数字是设计预算，不是普遍定律；超出时必须说明为什么该推导本身就是当前出口能力，并提供 advance organizer 或拆分方案。

## 5. Mainline latency

从主问题提出到读者获得阶段主结论之间，记录经过的支持性段落和新记号。支持性细节结束后必须有显式回返句，说明它怎样推进当前对象。

## 6. Explanation proportionality

检查：

- 辅助概念的篇幅是否压过当前主要对象；
- 完整证明是否真的属于本 unit；
- reader 能否在不读 optional block 时保留主线；
- 局部 bridge 与 canonical detail 是否职责清楚。

## 7. Depth and placement ledger

```md
| item_id | capability_or_claim | centrality | explanation_depth | placement | closure_deadline | mainline_cost | canonical_detail | duplication_rationale |
```

`centrality`：`core | bridge | supporting | optional`。

## 8. 禁止事项

- 不能因怕漏前提而把所有 premise 全部展开成教科书级证明；
- 不能把关键 bridge 全部移到链接或 optional block；
- 不能在 staged draft 通过后由 Integrator 静默改变 depth 或 placement。
