# Notes/WORKFLOWS/design-audit.md

Design Auditor 在正文前独立审查。它不写正文，也不因“总体方向正确”放过局部隐藏前提或比例问题。

Explanation depth、detail placement 与 mainline 的审查以 `depth-and-mainline.md` 为规则来源。

## 1. 审查项

### 任务、Domain、Learner

- units 服务 Brief；
- 四类关系与 premises 足够；
- no-evidence 为 `unverified`；
- identity、role、representation、rationale 不混合；
- owner 不充当掌握证据。

### Definition 与 claim closure

- definitions 非循环、可区分、有操作落点；
- closure deadline 在首次 dependent use 前；
- 不为 same-sentence closure 形成过载长句；
- claims 的 capability/prior claim/source 全部闭合。

### Explanation depth

- 每个 `unverified` 或 supporting detail 都有 depth 决策；
- 未把 `unverified` 自动升级为 full derivation；
- full/optional/upstream placement 与 exit capability 相称；
- optional block 可跳过；
- canonical detail 重复有 rationale。

### Mainline

- main question、result、return point 明确；
- latency budget 可执行；
- 支持性细节没有压过当前对象；
- 超预算有充分理由或已拆分；
- phase 仍有 consolidation。

### Note type、entry mode、语言与 Reader Card

- guided 首句稳定且不过载；
- language contract 完整；
- Reader Card 不泄露答案；
- Writer packet 不需 canonical/index。

## 2. v5 回归测试

以下任一至少为 `major`：

1. no-evidence 写成 unseen；
2. concept 与 role 合并；
3. claim 有未登记 premise；
4. definition 循环或 closure 过晚；
5. 以“必须同句闭合”为由写过载首句；
6. `unverified` 默认 full derivation；
7. 支持性推导没有 depth/placement；
8. optional detail 不可跳过；
9. mainline latency 无预算或无回返；
10. 已有 canonical full detail 被整段复制却无 rationale；
11. note type 无 entry mode；
12. language contract 或 Reader Card 失效。

## 3. 输出与返修

生成 `DESIGN_AUDIT.md`，写 severity、位置、影响、return_to 和 suggested_fix。Major 返回 design 完整重审；blocker 才交用户。
