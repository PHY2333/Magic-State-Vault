# Notes/WORKFLOWS/design-audit.md

Design Auditor 在正文写作前独立审查 `DIDACTIC_DESIGN.md`。审查 definition cards 与 explanation claims 时必须同时读取并应用 `explanation-contract.md`；它不写正文，也不因“总体方向正确”放过局部隐藏前提。

## 1. 审查项

### 1.1 任务对齐

- 每个 unit 是否服务 Brief 的目标表现；
- 是否偷渡非目标内容；
- 是否把仓库维护目标误写成学习目标。

### 1.2 Domain 关系与来源

- 四类关系方向是否明确；
- 数学依赖是否被错误当成阅读顺序；
- explanation premise inventory 是否足够；
- source-specific 与一般结论是否分开。

### 1.3 Faceted learner evidence

- 无证据是否标为 `unverified`；
- `unseen` 是否有明确首次接触证据；
- identity、context_role、representation、procedure、rationale 是否被错误合并；
- 仓库存在性是否被当成掌握证据。

### 1.4 Concept 与 role 分离

重点检查：

```text
基础概念本身是否未知？
还是只有它在当前构造中的角色是新的？
```

不得因后者而强制从零定义前者。

### 1.5 Definition adequacy

每张 definition card 检查：

- non-circular；
- discriminative；
- operational hook；
- appropriate depth；
- dependency closure；
- 第一行是否退化成词典释义或同义反复。

### 1.6 Claim dependency closure

逐 claim 检查：

```text
surface claim
→ capability dependencies
→ prior claim dependencies
→ closure method
→ source / calculation
```

特别检查“因为、所以、等价、保证、对应”是否有未建模前提。

### 1.7 负荷与 phase

- 一个 phase 是否加入过多对象、关系和符号；
- whole-picture 中哪些标签只定位，哪些要求操作；
- 是否有 consolidation；
- 是否把多个 claims 压在同一句或同一段。

### 1.8 模式适配

- 模式是否匹配目标动作和读者状态；
- 问题驱动是否来自真实问题；
- 整体图景是否过度抽象；
- 操作性内容是否缺示范。

### 1.9 Note type、entry mode 与首句

- 两个维度是否同时存在；
- guided 首句是否建立一个稳定对象；
- 是否无必要地用“既指 A，也指 B”处理术语多义；
- guided onboarding 是否过长到应独立 lesson。

### 1.10 语言合同

- 术语映射是否明确；
- 是否允许中英混合速记泄漏；
- 标题与中文 register 是否适合正式教材；
- Writer packet 是否可独立执行语言规范。

### 1.11 Reader card

- 是否只包含 entry、not-assumed、exit 和阅读场景；
- 是否泄露设计答案或审查结论；
- 是否足以支持 Blind Reader 独立冷读。

## 2. v3/v4 回归测试

以下任一出现即至少为 `major`：

1. no-evidence 被写成 `unseen`；
2. 概念 identity 与当前 role 合并；
3. 用未授权专名解释新术语；
4. explanation claim 有未登记 premise；
5. 半定义或循环定义通过；
6. 一个 phase 同时压入过多新对象和关系；
7. 目标文件只有 note type，没有 entry mode；
8. Domain 仍使用含混统一关系表；
9. Writer packet 仍需 canonical/index；
10. 语言合同缺失，默认复制设计文件中的中英混合表达；
11. Reader card 泄露 packet 或设计答案。

## 3. 输出与返修

生成 `DESIGN_AUDIT.md`：

```yaml
status: pass | changes_required | blocked
```

每个发现写明 severity、位置、影响、return_to 和修法。

- `minor`：Didactic Architect 直接修复；
- `major`：返回 design，修订后重新完整审查；
- `blocker`：来源冲突、范围决定或长期结构选择交给用户。
