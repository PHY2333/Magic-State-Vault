---
task_id: 20260831-kunneth-pro-rewrite
request_id: R01
request_type: rewrite
route: pro-write-review
output_mode: full-file
review_policy: fresh
binding_id: 6fbc0d8d6d2f48c7adf5bdecf67bb248
target_files:
  - Notes/07-Lifted-Product Code/Künneth 分解.md
---

# 用户目标

内部自行完成教学规划，整篇重写 Künneth 分解笔记。完成后，读者应能够：

1. 说清楚问题“何时可以先分别求 $C,D$ 的同调，再通过 tensor product 读出 $C\otimes D$ 的同调”；
2. 定义比较映射 $\kappa_n$，解释它为什么不依赖 cycle 代表元的选择；
3. 说明域上证明的整体机制：把每个复形拆成同调代表元部分与可缩部分，tensor 后只有前者的 tensor product 对同调有贡献；
4. 区分自然的比较同构与证明中非典范、一般不自然的补空间选择；
5. 对两个二项复形推出 degree-$1$ 的两个 Künneth 直和项，并把它们准确翻译成 HGP 的两类逻辑来源与逻辑比特数公式；
6. 比较域、PID 与一般交换环三种情形，知道 $\operatorname{Tor}$、谱序列微分和 extension 分别在什么层面阻止简单直和结论；
7. 沿 $R_2=\mathbb F_2[\varepsilon]\big/\langle\varepsilon^2\rangle$ 的直接计算看出比较映射如何同时失去单射与满射；
8. 判断域上的 HGP 维数公式何时不能无条件用于环系数 LP，并知道安全的替代计算方式。

# 当前真实读者反馈

用户的原始反馈是：`Künneth 分解` 写得不好，需要重新写。

只读诊断进一步发现：

- 主定理和 HGP 回报出现太晚，读者在知道目标前先经历很长的技术展开；
- 初等 complement bookkeeping 与自然性展开过细，一般环部分却突然切换成专家压缩语体；
- 开头是依赖与执行路线说明，不是读者此刻能够理解的真实问题；
- 缺少域上的紧凑成功例子，读者先看到的完整例子反而是失败反例；
- “同调扇区”会和 HGP 的物理比特扇区混淆；
- 域上主线、HGP 应用与一般系数边界没有形成清楚的层次。

不要把这些问题逐项写成正文中的维护说明；应通过整篇重新组织解决它们。

# Reader assumptions

## 可以直接依赖

- 基本线性代数、商空间、kernel、image、cokernel 与向量空间 tensor product；
- `Chain complex 与 cochain complex.md` 中 cycle、boundary 与 homology quotient 的含义；
- `Cochain complex 的 tensor product.md` 中 total degree、直和分量、product differential 与 Koszul sign；本文采用降 degree 的 chain convention，首次使用时只需给足够的转换桥梁；
- `二进制空间性质.md` 中向量子空间可以选择直和补空间，以及补空间一般不唯一。

## 不能直接依赖

- 已经知道 Künneth 定理、比较映射或它的自然性；
- 已经理解 contracting homotopy 为什么杀掉同调；
- 已经掌握 $\operatorname{Tor}$、flat/K-flat、derived tensor product、谱序列、filtration、associated graded 或 extension；
- 已经能区分 HGP 的物理比特扇区、logical-support quotient 与 Künneth 的两个直和项；
- 已经知道域上的 HGP 公式为何不能自动搬到环系数 LP。

仓库存在相关笔记不代表读者已经掌握。允许直接依赖的内容也应在首次承担当前推理作用时给出最短充分桥梁。

# 必须读取

- `Notes/WRITING_GUIDE.md`
- `Notes/OBSIDIAN_MATH.md`
- `Notes/PRO_OUTPUT_PROTOCOL.md`
- `Notes/07-Lifted-Product Code/Künneth 分解.md`
- `CANONICAL_KNOWLEDGE.md`：重点核对 Künneth、HGP 与 LP 的主笔记归属和边界
- `Notes/06-CCZ Distillation/Chain complex 与 cochain complex.md`
- `Notes/06-CCZ Distillation/Cochain complex 的 tensor product.md`
- `Notes/01-量子纠错基础/二进制空间性质.md`
- `Notes/07-Lifted-Product Code/Hypergraph product code.md`：重点核对 chain convention、logical-support quotient、Künneth 选读节和逻辑比特数记号
- `Notes/07-Lifted-Product Code/Lifted product code.md`：重点核对 `PID 与一般系数环` 入链锚点、环系数边界与展开后二进制秩接口
- J. P. May, *A Concise Course in Algebraic Topology* 的 “The Künneth theorem”：核对 PID 短正合列、一般不自然的 splitting 与域上的自然同构
- The Stacks Project, Tag `06XY`（Derived tensor product）：核对 K-flat 与 derived tensor product 的条件
- The Stacks Project, Tag `0H7Z`（Künneth Spectral Sequence）：核对一般环谱序列的假设、指标与收敛目标
- `Translations/S003.full.zh-CN.md` 与 `Papers/S003_2025_Menon_magic_tricycles.pdf`：只用于识别补充材料式 (91) 的来源边界；用户已决定该式不作为一般定理，不得用它覆盖 May/Stacks 的条件

# 来源与数学边界

- 本笔记的 canonical 范围必须保留：比较映射的良定义；域上的自然同构；使用非典范补空间和 contracting homotopy 的证明；二项复形 degree-$1$ 特化；HGP 的两个逻辑来源和 $K$ 公式；PID/一般环边界；$R_2$ 上比较映射失败的直接反例。
- 固定乘积 chain differential 为

  $$
  \partial(c\otimes d)=\partial_Cc\otimes d+(-1)^{|c|}c\otimes\partial_Dd.
  $$

  只有在 $\mathbb F_2$ 上才能无说明地省略符号。product differential 平方为零的完整证明属于上游笔记，本篇不重复。
- 域上结论使用 $k$ 上的有界有限维链复形。比较映射 $\kappa_n$ 是自然的；证明中为 cycles、boundaries 选择的补空间与链级分裂不自然。不要把这两件事混在一起。
- 域上分裂证明必须保留一般域上的 Koszul 符号：收缩位于第一因子时核对交叉项抵消；收缩位于第二因子时使用随第一因子 degree 改变的符号。不得因为最终 HGP 应用位于 $\mathbb F_2$ 就删掉一般域证明中的符号。
- 对二项复形应得到

  $$
  H_1(\mathcal A\otimes_k\mathcal B)
  \cong
  \ker A\otimes_k\operatorname{coker}B
  \oplus
  \operatorname{coker}A\otimes_k\ker B.
  $$

  在 $k=\mathbb F_2$ 的有限维 HGP 中取维数，得到

  $$
  K=k_Ak_B^T+k_A^Tk_B.
  $$

  这里应称为两类逻辑来源或两个 Künneth 直和项，不称为两个物理扇区；HGP blocks、CSS 对易与距离不在本篇重推。
- PID 结论的精确假设必须放在公式附近。May 的标准形式允许一个因子逐项 flat；当前笔记可以保留“两因子有界且逐项自由”作为更强而安全的充分条件，但不得把它说成必要条件。结论是带 $\operatorname{Tor}_1$ 的自然短正合列，splitting 一般不自然，且 Tor 直和指标满足 $p+q=n-1$。不要把循环 LP 常用的 $R_\ell=\mathbb F_2[x]\big/\langle x^\ell-1\rangle$ 默认为 PID。
- 一般交换环应使用 bounded derived Künneth spectral sequence，目标是 $H(C\otimes_R^{\mathbf L}D)$。只有至少一个因子 K-flat 时才能用 ordinary tensor product 代表 derived tensor product；有界逐项自由复形是安全的充分条件。这本身不保证谱序列退化。
- Stacks 来源采用上同调指标；若正文改写成同调指标，必须说明是重编号后的版本并保持 total degree、收敛目标以及微分方向 $d_r:(s,t)\to(s-r,t+r-1)$ 一致。$E^2$ 页的高阶 $\operatorname{Tor}$ 还会经历后续微分，$E^\infty$ 只给出目标同调的 associated graded，重组时还有 extension；不能把 $E^2$ 或 $E^\infty$ 项直接读成额外直和。
- “系数环不是域”只表示域上的直和公式不再自动成立，不表示每个非域实例必有非零 $\operatorname{Tor}$ 或比较映射必失败。
- 循环 LP 的一般系数讨论限于交换环。非交换 group-algebra 的左右模和 commuting actions 属于 `Lifted product code.md`，本篇只给边界提醒，不展开。
- $R_2$ 反例是本文直接计算，应明确这一点。保留其结论：比较映射定义域和目标的二进制维数都为 $2$，但 $\kappa_1$ 的秩为 $1$，既非单射也非满射。
- $R_2$ 有零因子，不是 PID，不能套用 May 的 PID 短正合列。反例中的两个像代表同一个非零同调类，而不是各自都是 boundary；失败也不是源与目标维数不同。
- 用户已决定 S003 补充材料式 (91) 不作为一般定理。该式对有限维域代数给出的无条件直和与 $R_2$ 反例冲突；除非另行证明 semisimple、flat/K-flat 或谱序列退化等额外条件，正文不得采用或暗示这一推广，也不需要在读者正文展开来源争议。
- 一般 LP 未证明相关同调模的平坦性或谱序列退化时，不能套用域上的 $K$ 公式；按展开后的二进制 $H_X,H_Z$ 秩计算逻辑比特数。
- 不新增来源未支持的定理、参数或一般化。若 May/Stacks 与仓库当前 canonical 结论发生实质冲突，返回 `NEEDS_CONTEXT`，不要静默改写。

# 写作权限

## 允许

- 完整替换唯一目标文件；
- 重组标题与论证顺序，删除竞争性、重复或喧宾夺主的解释；
- 在技术证明前先给域上定理、直觉、用途与证明地图；
- 加入一个紧凑的域上 worked example，帮助读者先看到分解成功时怎样工作；
- 把 PID、一般环、谱序列与 $R_2$ 反例组织成明确可跳读的进阶边界层；
- 压缩自然性为交换关系和纯张量核对，但必须保留结论及“自然比较映射／不自然证明选择”的区别。

## 禁止

- 输出或修改其他正式文件、索引、canonical、来源登记、译文或任务外 artifact；
- 删除、移动、拆分、合并或重命名正式文件；
- 删除 canonical 要求保留的上述定理、证明机制、应用或反例；
- 展开重写 HGP blocks、CSS 对易、HGP 距离、LP balanced relation、环值 blocks、二进制展开或 S007 执行；
- 使用“同调扇区”混称 Künneth 直和项与 HGP 物理比特扇区；
- 把任务、审计、allowlist、canonical ownership 或工作流语言写入读者正文；
- 用链接代替比较映射、域上证明、二项特化与一般系数边界所需的关键解释。

必须保留一个标题文字精确为 `PID 与一般系数环` 的 heading，使现有入链 `[[Künneth 分解#PID 与一般系数环]]` 继续解析。涉及删除、移动、拆分、合并或重命名正式文件时，返回 `DECISION_REQUIRED`。

# 写作要求

- 内部自行完成教学规划；直接输出完整、可替换的目标 Markdown，不输出单独的路径表、设计稿、审查表或修改说明；
- 围绕一个真实问题组织全文：什么时候 $H(C\otimes D)$ 能由 $H(C)$ 与 $H(D)$ 直接读出；
- 在全文前 10%–15% 内让读者看到域上的主结论、假设及它对二项复形/HGP 的用途；
- 在长证明前给证明地图，随后保留 complement、可缩部分与 contracting homotopy 的完整逻辑，但压缩初等单射满射和重复 bookkeeping；
- 让正文解释深度从头到尾连续；新术语必须在承担推理前说明其作用，一般环术语可以放入明确可跳过的进阶节；
- 用自然、统一的中文教材语体；英文术语首次必要时括注，后文保持统一；
- 来源、适用条件与指标重编号紧邻相关公式；$R_2$ 反例注明是本文直接计算；
- 正文链接必须有效，不链接 `Notes/WORKING/`；
- 所有数学严格使用 Obsidian 规定的行内与独立块公式定界；不得使用反斜杠括号型定界符、斜杠后直接跟括号的写法、JSON 双重转义或未闭合的数学定界符；
- 输出前从头复读完整文件，严格遵守 `Notes/PRO_OUTPUT_PROTOCOL.md`。

# 完成标准

1. 开头提出真实问题并尽早给出域上定理、条件、直觉与 HGP 用途，读者无需读完证明才知道目标。
2. $\kappa_n$ 的定义、cycle 性与代表元无关性完整，且没有把良定义与可逆性混为一谈。
3. 域上证明有清楚地图；补空间、可缩部分、contracting homotopy 与 tensor summands 的逻辑闭合，但没有被初等 bookkeeping 淹没。
4. 清楚区分：$\kappa_n$ 自然；证明所选补空间和链级分裂不自然。
5. 至少有一个紧凑域上成功例子，服务直觉而不另开竞争性主线。
6. 二项复形公式、HGP logical-$Z$ support quotient 与 $K=k_Ak_B^T+k_A^Tk_B$ 推导正确；两个直和项称为逻辑来源，不与物理扇区混淆。
7. 域、PID、一般交换环形成清楚的三层判断；每层的条件、结论和不能推出的内容准确。
8. flat/K-flat、derived tensor、谱序列、filtration、associated graded 与 extension 在承担推理前得到最短充分说明，或被安置在真正可跳读的进阶层。
9. $R_2$ 反例计算自洽，明确展示 $\kappa_1$ 秩为 $1$、非单射且非满射，并与“非域不等于每例失败”并置。
10. 对 LP 给出可执行的安全判断：未证平坦性或退化时不用域上公式，而按展开后的二进制秩计算。
11. 保留精确 heading `PID 与一般系数环`；不破坏现有正式入链。
12. 不重复相邻 owner 的 HGP/LP/S007 内容，不修改或要求修改 allowlist 外文件。
13. 不把 S003 式 (91) 当作一般定理，也不在正文中静默调和它与 $R_2$ 反例的冲突。
14. 中文、链接与 Obsidian 数学格式通过检查；正文没有任务、审计或维护者语言。
