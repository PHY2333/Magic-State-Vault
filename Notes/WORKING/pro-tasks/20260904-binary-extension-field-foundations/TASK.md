---
task_id: 20260904-binary-extension-field-foundations
route: pro-write-review
status: R01_APPLIED
target_files:
  - Notes/08-Binary Extension Field Non Clifford Module/二元扩域.md
integration_files:
  - Notes/00-index.md
  - CANONICAL_KNOWLEDGE.md

integrity: fast
review_policy: fresh
audit_retention: errors-only

format_handling:
  policy: codex-contextual
  auto_repair: true
  rule_based_fixer: false
  allow_markdown_and_delimiter_repair: true
  allow_unambiguous_latex_syntax_repair: true
  escalate_only_when_meaning_is_ambiguous: true

git:
  remote: main
  branch: codex/binary-extension-field-foundations-20260904
  base_commit: b3895c6cf1ec751dce9a340c1ec965cf59685508

automation:
  run_to_completion: true
  standing_authorization: true
  auto_commit: true
  auto_push: true
  merge_to_main: false
  max_author_rounds: 2
  max_review_rounds: 1
  preauthorized_browser_rounds:
    - R01
    - R02
  stop_only_on:
    - permission_required
    - account_mismatch
    - needs_context
    - decision_required
    - blocked
    - source_conflict
    - structural_file_change
    - path_outside_allowlist
    - ambiguous_format_or_latex_repair
    - math_content_uncertain
    - format_check_failed_after_codex_repair
    - push_failure
    - merge_to_main
---

# 用户目标

在 `Notes/08-Binary Extension Field Non Clifford Module/` 新写一篇关于二元扩域 $\mathbb F_{2^s}$ 的完整中文教学笔记。读者应从“如何让 $s$ 个二进制坐标不仅能相加，还能组成一个域”出发，掌握具体构造、实际运算、主要结构映射以及二进制线性表示，并能看懂它为什么是后续伽罗瓦 qudit 与非 Clifford 门讨论的代数底座。

# 当前真实问题

目标目录当前为空，正式 Notes 与 `CANONICAL_KNOWLEDGE.md` 中也没有有限域或二元扩域的既有 owner。因此本任务不是把背景补进某篇下游笔记，而是建立唯一的基础主笔记。正文必须既能独立承担 $\mathbb F_{2^s}$ 的入门，又不提前接管后续 qudit 门、Clifford 层级、扩域码或蒸馏协议的完整内容。

# 本次授权

- 由 ChatGPT Pro 新写唯一目标文件的完整正文；
- 允许为形成连续教学主线，自行选择章节结构、一个贯穿的 $\mathbb F_4$ 算例、必要的证明和紧凑对照；
- 允许解释不可约多项式商构造、基与坐标、域运算、Frobenius、乘法群、子域、迹、范数、迹配对、二进制矩阵表示及最短量子信息接口；
- Codex按上下文修复纯 Obsidian / Markdown / 唯一确定的 LaTeX 格式问题；
- 完成 R01 后，由全新 Pro 会话运行 R02 全文审查；
- R02 通过后，Codex按本文件预定文字机械更新索引与 canonical 记录；
- 在本任务分支自动 commit/push。

# 预定机械集成文字

在 `Notes/00-index.md` 的第 7 节之后、分隔线之前插入：

```md
8. 二元扩域与非 Clifford 模块
   - [[二元扩域]]：从不可约多项式商构造 $\mathbb F_{2^s}$，建立基坐标、域运算、Frobenius、迹与范数，并说明这些结构如何变成 $s$ 比特上的二进制线性表示。
```

在 `Notes/00-index.md` 的“当前目录归属”中，紧接 `Notes/07-Lifted-Product Code/` 条目后插入：

```md
- `Notes/08-Binary Extension Field Non Clifford Module/`：二元扩域的代数基础、二进制坐标表示，以及后续伽罗瓦 qudit 与扩域非 Clifford 门所需的接口。
```

在 `CANONICAL_KNOWLEDGE.md` 的“当前范围”首段末尾，把句号前补入：

```md
，以及 `Notes/08-Binary Extension Field Non Clifford Module/` 中二元扩域的构造、算术、结构映射与二进制表示
```

在 `CANONICAL_KNOWLEDGE.md` 的“主路线图”条目之后、`## 二进制空间、补空间与正交补` 之前插入：

```md
## 二元扩域 $\mathbb F_{2^s}$

- 主笔记：[[二元扩域]]，路径 `Notes/08-Binary Extension Field Non Clifford Module/二元扩域.md`。
- 前置依赖：$\mathbb F_2$ 上的向量、线性映射与矩阵，以及多项式加法、乘法和整除的基本概念。
- 已有结论：对次数为 $s$ 的不可约多项式 $f(x)\in\mathbb F_2[x]$，商 $\mathbb F_2[x]/(f)$ 是含 $2^s$ 个元素的域；每个元素有唯一的次数小于 $s$ 的代表元，并在选定基后对应 $\mathbb F_2^s$ 中的坐标。加法、固定元素乘法与 Frobenius 都是 $\mathbb F_2$-线性映射；一般乘法是双线性的。主笔记还固定绝对迹、绝对范数、迹配对、对偶基和乘法矩阵的记号与适用范围。
- 当前笔记只保留：抽象域与具体表示的区别、不可约多项式商构造、可计算的域运算、有限域的必要结构、迹／范数／基与二进制矩阵接口，以及进入伽罗瓦 qudit 语境前所需的最短桥梁。
- 写新内容时引用它：涉及 $\mathbb F_{2^s}$ 元素的坐标展开、无进位加法、模不可约多项式乘法、Frobenius、子域、迹与范数、二元化矩阵，或判断某个扩域算术操作是否为 $\mathbb F_2$-线性时引用这里。
- 不要在当前笔记重复：具体 qudit Pauli/Clifford 形式、非 Clifford 门分类、扩域 CSS 码、Reed–Solomon／代数几何码以及 magic-state distillation 协议应由后续独立笔记承担。
- 边界：$\mathbb F_{2^s}$ 的抽象同构类型唯一，但基和不可约多项式给出的坐标表示并不典范；它的特征为 $2$，不能与整数剩余类环 $\mathbb Z/2^s\mathbb Z$ 混同。本文中的迹与范数默认指到 $\mathbb F_2$ 的绝对迹与绝对范数。
- 状态：已整理。
```

# 本次不处理

- 不新增第二篇前置笔记；
- 不把 S008 的具体门、码、协议、数值参数或论文综述塞进这篇基础笔记；
- 不完整展开伽罗瓦 qudit Pauli 群、Clifford 层级、qudit-to-qubit 映射或任意具体非 Clifford 门；
- 不讲 Reed–Solomon 码、Reed–Muller 码、代数几何码或蒸馏正交条件；
- 不修改现有正式笔记、Papers、Translations 或其它任务产物；
- 不删除、移动、拆分、合并或重命名正式文件；
- 不合并主分支。

# 当前阶段

`R01_APPLIED`：GitHub checkpoint 已推送；R01 已完成绑定、解析、上下文格式规范化、数学与 ownership 预审并应用到唯一目标文件。下一步提交并推送 R01 application commit，再从全新 ChatGPT Pro 会话运行 R02 全文审查。
