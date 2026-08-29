---
status: ready
task_id: 20260828-hgp-v5-pilot
reviewed_draft_revision: 5
manuscript_verdict: pass
target: Notes/07-Lifted-Product Code/Hypergraph product code.md
formal_integration_authorized: false
---

# Integration Preview

## 结论

Revision 5 的 U01/U02 可按下述精确拼接方案进入目标笔记，无需修改两份已审查正文，也无需新增、移动或改写其它 reader-visible bridge。

`ready` 只表示 repository fit 检查通过；本文件不授权正式写入，`formal_integration_authorized` 仍为 `false`。

## 审查输入与指纹

- `MANUSCRIPT_VERDICT.md`：`pass`，只授权只读 Integration Preview。
- U01 SHA-256：`3713ad6565c3f992f402b4372db00efa37b798e56f6ac2d0fde9a04b5a46c585`。
- U02 SHA-256：`b5fe54e31c51308230fb356373ae3c13c86325991805eff92cc43ebb36de531a`。
- 两份实算指纹均与 verdict 登记值一致。
- 本预览没有改写 U01/U02 的字词、公式、标题、callout 或段落顺序。

# Target placement

未来若另获 formal integration 授权，唯一装配顺序为：

1. 在目标文件最前加入本 preview 规划的最小 frontmatter。
2. 用 revision 5 U01 全文作为第一段 reader-visible opening。
3. 紧接 U01 放置 revision 5 U02 全文，保持两个同级标题与全部正文不变。
4. U02 末句之后直接接当前正式正文第 3 行 `### 从两张经典校验矩阵开始`。
5. 删除当前第 1 行旧 opening，不移到其它位置。
6. 保留当前第 3–51 行。
7. 删除当前第 53–70 行的 logical quotient / dual cochain 提前说明。
8. 从当前第 72 行 `### 乘积中间项与物理比特扇区` 起保留其余正文。
9. 拼接边界只保留正常单个空行，不作文字性顺句或补写。

Reader-visible 顺序为：

```text
U01：构造／所得码／输入／输出／对易问题
→ U02-P1：局部交换、重叠奇偶与 H_X H_Z^T=0
→ U02-P2：三个空间、两支映射与零复合
→ 从两张经典校验矩阵开始
→ 乘积中间项与物理比特扇区
→ HGP blocks 与两路径抵消
→ 其余现有参考正文
```

# Replacement / deletion range

| 当前正式范围 | 动作 | 理由 |
|---|---|---|
| 文件首部 | 插入最小 frontmatter | 目标笔记被实质修改时须满足 `NOTE_TYPES.md` |
| 第 1 行 | 以 U01 全文替换 | 旧 opening 与 guided opening 竞争，并提前宣告“自动对易”及路由前置链接 |
| 第 3–38 行 | 逐字保留 | 承担 \(A,B\) 尺寸、二项复形和指标约定 |
| 第 39–51 行 | 逐字保留 | 把 U02 已建立的三空间语义绑定到后续计算使用的 \(\partial_2,\partial_1\) 与 \(H_X,H_Z\) convention |
| 第 53–70 行 | 删除 | logical quotient 与 dual cochain 完整说明已有 owner；当前开头不需要这个提前分支 |
| 第 72–447 行 | 逐字保留 | 乘积扇区、blocks、构造证明、S007、Tanner、参数、qLDPC、LP 与来源 |

当前第 102–165 行的构造性证明必须完整保留。U02 给出所有 CSS 输出必须满足的通用条件；该正式段落则首次写出具体 HGP blocks，并用两条 product paths 抵消证明构造确实满足条件。两者不是重复证明。

# Assembled reading flow

- U01 末句提出“怎样由构造本身保证两类校验彼此对易”。
- U02 首句立即把这一问题的“第一步”限定为可检验矩阵条件。
- U02 末句要求“由 \(A,B\) 构造这两支映射，并证明它们的复合恒为零”。
- 紧接的现有标题“从两张经典校验矩阵开始”随即给出 \(A,B\) 的尺寸、二项链复形和指标，之后进入乘积边界。
- 承诺与兑现之间没有插入链接、提示框或维护说明。

# Local bridge and links

| detail | HGP local bridge | full owner |
|---|---|---|
| 奇偶校验矩阵、输入／输出、行支撑与 CSS 当前要求 | U01 | `CSS码中的cochain complex.md` 承担完整 stabilizer/logical/syndrome |
| 同比特／异比特规则、重叠奇偶、矩阵条件 | U02-P1 | CSS owner 承担更完整结构；当前 local derivation 继续承重 |
| 三空间、两映射、零复合与链复形当前名称 | U02-P2 | `Chain complex 与 cochain complex.md` 承担 generic degree/cycle/boundary/homology/cochain |
| 完整 \(2\times2\) 核验 | U02 optional block | 非出口能力，不进入主线 |
| HGP blocks 与两路径抵消 | 后续正式第 102–165 行 | 当前 HGP 主笔记 |

不新增 U01/U02 inline link。现有 local bridge 已在首次依赖前自足；链接不承担 U01/U02 的核心解释。

# Duplication and ownership check

- 旧第 1 行与 U01 竞争首次入口，删除。
- 旧第 39–51 行不删：它们将读者已理解的映射语义绑定到后续 blocks 推导使用的局部符号约定。
- 旧第 53–70 行删除：其 logical quotient 与 dual direction 不是 U01/U02 出口，也不是 blocks、Tanner 或对易证明的本地前提。
- U02 的 Pauli、重叠与零复合说明是首次依赖前的必要 local bridge，不得换成承重链接。
- U02 不展开 HGP blocks、尺寸、Künneth 或 homology，不与后文竞争。

# Logical-space continuity after deleting old lines 53–70

## 首次出现

模拟删除当前第 53–70 行后，后文首次出现

\[
H_1(\mathcal A\otimes\mathcal B)
\]

仍是当前第 331 行，位于当前第 309 行标题 `### 长度、秩与可选逻辑空间分解` 之下。

紧邻上下文为：

- 当前第 319–326 行先说明 \(H_X,H_Z\) 的生成元数、rank 公式及“这一步不需要 Künneth 分解”；
- 当前第 328 行在公式前明确写道：“若要把逻辑空间进一步分成两个 product sectors，域上的 `[[Künneth 分解#二项复形与 HGP 逻辑空间|Künneth 分解]]` 给出”；
- 当前第 331–335 行随即展示 \(H_1(\mathcal A\otimes\mathcal B)\) 的两个 kernel/cokernel 扇区；
- 当前第 338–359 行定义相应维数并得到 \(K\) 的公式。

## 落点判断

该首次使用具有足够的 logical-space 落点，无需 reader-visible 返修：

1. 标题已把这一分支标为“可选逻辑空间分解”。
2. 公式前的当前第 328 行已明说该式的用途是“把逻辑空间进一步分成两个 product sectors”；因此读者在见到 \(H_1\) 前已知它当前承担的 logical-space 作用。
3. 同一句的精确 owner anchor `Künneth 分解#二项复形与 HGP 逻辑空间` 实存于 `Künneth 分解.md` 当前第 521 行。
4. Owner anchor 当前第 523–560 行先从两个二项链复形推出 degree-\(1\) Künneth 分解；第 565–573 行进一步明确写出
   \[
   H_1(\mathcal A\otimes\mathcal B)
   =\frac{\ker H_X}{\operatorname{im}H_Z^T},
   \]
   并说明它表示 logical \(Z\) support classes，而对偶 \(H^1\) 表示 logical \(X\) support classes。
5. 该 owner 段又反向链接到目标笔记保留的 `Hypergraph product code#从两张经典校验矩阵开始` anchor。
6. 后文只使用该分解解释两个逻辑扇区并计算维数；HGP 构造、CSS 对易、Tanner 边和行／列方向均不依赖读者先掌握一般同调 quotient。

因此不在 U01/U02 中新增 logical homology 内容，也不把旧第 53–70 行移到其它位置。Fit Planner 或 Integrator 不得补写新的 reader-visible 逻辑同调桥梁。

# Frontmatter

目标正式笔记当前没有 frontmatter。若未来获得 formal integration 授权，只在文件顶端加入：

```yaml
---
note_type: reference
entry_mode: guided
status: reviewed
---
```

`reference` 保持 HGP 构造、blocks、乘积扇区和 Tanner 方向的 canonical owner 职责；`guided` 对应 U01/U02 新 opening；`reviewed` 对应已通过 revision 5 manuscript gate 和 repository-fit 检查的正文。Frontmatter 不改变 U01/U02 正文。

# Index / canonical impact

- `Notes/00-index.md`：无需修改。文件名、路径、主路线位置和 HGP 核心入口职责未改；没有新增正式笔记或前置。
- `CANONICAL_KNOWLEDGE.md`：无需修改。HGP owner、CSS logical quotient、generic chain homology 和 Künneth 分解的 ownership 都未迁移。
- 不新建、拆分、合并、改名或移动任何正式笔记。

# Repository checks

## Anchors and links

- `### 从两张经典校验矩阵开始` 保留；来自 `Künneth 分解.md` 与 `Lifted product code.md` 的现有深链接继续有效。
- `### 行与列的乘积方向` 保留；S007 笔记的现有深链接继续有效。
- 删除范围不含标题，不移除现有 heading anchor。
- U02 新增的两个标题与现有标题不重名，不产生 anchor 冲突。
- 当前第 328 行的 Künneth 精确 anchor 已验证存在。
- Frontmatter 与前置插入只改变物理行号，不改变 Obsidian heading anchor。
- 不添加新链接，不修改任何保留链接。

## Git and protection baseline

- HEAD：`d320a790f6f1aea459e2e828280f20e279a1edd7`
- `Hypergraph product code.md` HEAD / worktree blob：`d18e00e59d71aa1615417dbfadf4f60d4b27bd69`
- `Notes/00-index.md` HEAD / worktree blob：`847c0b231fd7471f49a445cb7f0d0426a53285cb`
- `CANONICAL_KNOWLEDGE.md` HEAD / worktree blob：`12b3fdb92c5214f4c6e48b54d3a6777cd76ead67`
- `CSS码中的cochain complex.md` HEAD / worktree blob：`dbdbf098bf73fedcb8a497c9a38eaaba6952cec5`
- `Chain complex 与 cochain complex.md` HEAD / worktree blob：`9439db87d5a5b01c19ff6fa7e763ae8e4966208c`
- `Künneth 分解.md` HEAD / worktree blob：`c359fe37040d959228ce66d176f4410cc8da9418`

`git status --short` 的变更只位于当前 authoring task 目录；目标正式笔记、index、canonical 和相关 owner 均未改变。

# Required return route

当前无需返回 Didactic Design / Writer。Placement、删除范围、assembled flow、duplication、links、logical-space 落点、frontmatter、index/canonical 和保护基线均明确，且整合可逐字保留 revision 5 U01/U02，因此状态为 `ready`。

本 preview **不授权 formal integration**。若未来 Integrator 发现必须修改 U01/U02 任一 reader-visible 字句、公式、标题、段落或 callout，或必须新增／移动 logical-space bridge、链接或扩大删除范围，必须停止并返回 Didactic Design / Writer，新 draft 重跑双审查与 preview。
