# 来源范围

## S01 — 目标 HGP 正式笔记

- source：`Notes/07-Lifted-Product Code/Hypergraph product code.md`。
- version：pilot 基线 SHA-256 `FC30E26164B54072784F12402CB290FDD1F13347480A3381DCF415FF6FED6366`。
- location：开头；“从两张经典校验矩阵开始”；“HGP 校验矩阵与对易”。
- classification：`repository-derived`。
- supported_claim：HGP 从 \(A,B\) 构造 \(H_X,H_Z\)；采用 \(H_X=\partial_1,H_Z=\partial_2^T\)；\(H_XH_Z^T=0\) 来自连续边界复合为零。
- unsupported_or_missing：开头没有为首次接触者逐步建立 CSS 对易问题；外部论文未在本 pilot 中重新核对。
- intended_use：支撑 HGP 类别、输入／输出、三项 chain convention 和自动对易承诺。

## S02 — CSS 矩阵的一般解释

- source：`Notes/06-CCZ Distillation/CSS码中的cochain complex.md`。
- version：当前 worktree 版本。
- location：“CSS 码先给出两张矩阵”；“把 CSS 商空间写成 cochain 语言”；“注意 convention”。
- classification：`repository-derived`。
- supported_claim：\(H_X,H_Z\) 的行分别给出两类 check supports；共享列空间对应同一批物理量子比特；\(H_ZH_X^T=0\) 是 CSS 对易条件；对偶方向使用 \(H_XH_Z^T=0\)。
- unsupported_or_missing：该笔记的现有开头使用 stabilizer 等专名，不能直接作为 U01 的局部 CSS 解释。
- intended_use：只抽取 rows、共享物理 columns 和矩阵对易条件，不授权 stabilizer、logical quotient 或 cohomology 语言。

## S03 — Chain complex 的一般定义

- source：`Notes/06-CCZ Distillation/Chain complex 与 cochain complex.md`。
- version：当前 worktree 版本。
- location：“chain complex：边界映射连续两次为零”。
- classification：`repository-derived`。
- supported_claim：三项线性映射满足相邻复合为零时符合 chain-complex condition。
- unsupported_or_missing：degree、cycle、boundary、homology 和 cochain 对偶均超出 U01/U02 当前用途。
- intended_use：在三项箭头和零复合已经得到解释后，授权名称“链复形”。

## S04 — Canonical HGP 条目

- source：`CANONICAL_KNOWLEDGE.md`。
- version：pilot 基线 SHA-256 `19E2E8A4F4F0368944E25F321A1A2AA04AA8484973CE5703BD83930D01563865`。
- location：“Hypergraph product code”。
- classification：`repository-derived`。
- supported_claim：HGP 主笔记 ownership、chain convention、blocks 和 \(H_XH_Z^T=0\) 与目标文件一致。
- unsupported_or_missing：canonical 条目是 Mapper/Integrator 依据，不得进入 Writer packet 或读者正文。
- intended_use：只用于 mapping 交叉核对，不授权 Writer 读取。

## S05 — 用户指定的 learner 与教学边界

- source：本任务用户指令与 `BRIEF.md`。
- version：2026-08-28 收到的任务指令；task_id 按用户指定为 `20260827-hgp-v3-pilot`。
- location：目标表现、Learner evidence、U01/U02 约束、停止点。
- classification：`source-derived`。
- supported_claim：learner evidence states、文件决策、单元范围、禁用词、隔离与不整合要求。
- unsupported_or_missing：不作为数学事实来源。
- intended_use：约束 design、packet 和 audit。

## S06 — 任意矩阵对可能不对易

- source：K03、K04 的直接线性代数推论。
- version：当前 mapping。
- location：`DOMAIN_MODEL.md` 的 K04、K05。
- classification：`inference`。
- supported_claim：相同列数不推出 \(H_XH_Z^T=0\)，所以自动对易需要额外构造保证。
- unsupported_or_missing：不提供具体反例矩阵，因为当前目标只需建立障碍。
- intended_use：为 U01 结尾与 U02-P1 提供真实动机。

# 术语与约定

- HGP：hypergraph-product construction/code。
- \(A,B\)：两张经典二进制校验矩阵；U01 不给尺寸。
- \(H_X,H_Z\)：输出的两类 CSS check matrices。
- CSS 的唯一授权局部解释：两组作用在同一批物理量子比特上的 \(X\)-type 和 \(Z\)-type checks，并且它们需要彼此对易。
- 三项方向固定为
  \[
  C_2\xrightarrow{H_Z^T}C_1\xrightarrow{H_X}C_0.
  \]
- \(C_1\)：物理量子比特 support 空间；两侧分别由 \(Z\)-type check combinations 和 \(X\)-type overlap results 承载。
- “链复形”只能在读者看到三项箭头及其零复合用途后出现。

# 公式、图表和定理锚点

- CSS pairwise commutation：
  \[
  H_XH_Z^T=0.
  \]
- Three-term overview：
  \[
  C_2\xrightarrow{H_Z^T}C_1\xrightarrow{H_X}C_0.
  \]
- Composition：
  \[
  H_X\circ H_Z^T=H_XH_Z^T=0.
  \]
- U01/U02 不授权 HGP Kronecker block 公式、矩阵尺寸、total-degree 公式或 \(A\otimes B+A\otimes B=0\)。

# 禁止补猜

- 不得把没有 learner evidence 的能力写成已掌握或 `unseen`。
- 不得用 stabilizer code、stabilizer group、logical quotient 解释 CSS。
- 不得说明 Künneth 的用途，也不得写“不是前置”。
- 不得推导 \(A,B\) 的尺寸、Kronecker blocks、\(\mathbb F_2\) 两路径抵消、距离、qLDPC 或 LP。
- 不得从 canonical/index 复制维护句子到 packet 或正文。
- 不得声称本 pilot 已重新核验外部论文。
