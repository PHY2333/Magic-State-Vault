# Notes/NOTE_TYPES.md

正式 Notes 有三个独立维度：知识职责、读者入口和审查状态。

## 1. Frontmatter

新建或实质修改的正式笔记至少写：

```yaml
---
note_type: reference | lesson | derivation | paper-guide | index
entry_mode: guided | direct | lookup
status: draft | partially-reviewed | reviewed | stable | deprecated
---
```

可选：

```yaml
review_scope:
  - <稳定标题或语义范围>
```

## 2. note_type

- `reference`：保存一个概念、构造、定理或判断标准的 canonical 表述。
- `lesson`：完成一次明确的入口能力到出口能力转变，可跨越多个 canonical concepts。
- `derivation`：保存完整证明、计算或算法论证。
- `paper-guide`：服务特定来源阅读，保留版本、记号和 source-specific 边界。
- `index`：只负责导航和顺序。

## 3. entry_mode

- `guided`：正文承担首次或不稳定接触的入口责任。
- `direct`：面向已有 operational/fluent 证据的读者。
- `lookup`：主要供查询，不承诺连续首次阅读。

`reference + guided` 只说明入口受引导，不自动证明整篇都具有教材连续性。

## 4. status 的严格语义

- `draft`：整篇尚未通过混合流程的 whole-note gate。
- `partially-reviewed`：只有明确列出的 `review_scope` 通过；其余内容不得被解释为已审查。
- `reviewed`：完整 `ASSEMBLED_DRAFT.md` 已同时通过 Sol Contract Audit 与 Pro Whole-Note Review，并按同一指纹精确整合。
- `stable`：在 `reviewed` 基础上，来源、ownership、links 与长期职责已稳定。
- `deprecated`：不再作为有效入口。

Unit-level pass、Integration Preview 或 coverage audit 均不得单独把整篇升级为 `reviewed`。

## 5. 拆分判断

考虑拆分的情况：

- 一个文件长期承担冲突的 note types；
- source-specific adapter 打断一般理论主线；
- optional derivation 实际成为后文隐藏前置；
- 一个证明或背景推导压过主要对象；
- whole-note Pro design 判断两条读者路线不可兼容。

拆分、移动和改名需要用户决定；technical unit 边界不需要用户审批。
