---
task_id: 20260831-kunneth-pro-rerun
request_id: R01
request_type: rewrite
route: pro-write-review
output_mode: full-file
review_policy: fresh
binding_id: cbe2147fcfa945b0a85ba2855693413c
target_files:
  - Notes/07-Lifted-Product Code/Künneth 分解.md
---

# 用户目标

依据当前 checkpoint 中更新后的 Writing Guide，从头连续复读并整篇重写 Künneth 分解笔记。完成后，读者应能够：

1. 说清楚问题“何时可以先分别求 $C,D$ 的同调，再由 tensor product 读出 $C\otimes D$ 的同调”；
2. 定义比较映射 $\kappa_n$，解释 cycle 性、代表元无关性、单射、满射与自然性分别在说什么；
3. 跟随域上证明的完整机制：把每个复形拆成同调代表元部分与可缩部分，tensor 后所有含可缩因子的分量不贡献同调；
4. 区分自然的比较同构与证明中非典范、一般不自然的补空间和链级分裂；
5. 对两个二项复形推出 degree-$1$ 的两个 Künneth 直和项，并把它们准确翻译成 HGP 的两类逻辑来源和逻辑比特数公式；
6. 比较域、PID 与一般交换环三种情形，知道 $\operatorname{Tor}$、谱序列微分和 extension 在哪一步阻止简单直和结论；
7. 沿 $R_2=\mathbb F_2[\varepsilon]/\langle\varepsilon^2\rangle$ 的直接计算看出 $\kappa_1$ 怎样同时失去单射与满射；
8. 判断域上的 HGP 维数公式何时不能无条件用于环系数 LP，并选择展开后的二进制秩作为安全计算接口。

# 当前真实读者反馈

用户原始反馈是整篇笔记“写得不好，需要重新写”；在上一轮完成后，用户又更新了 Writing Guide 与 Review Request 模板，要求完整重跑流程，而不是对旧会话作形式追认。

当前基线数学主干基本正确，但按新版指南仍有以下全文问题：

- 开头示意中的系数对象、$H(C)$ 的分次含义和后续 $\otimes_k$ 记号之间需要更连续的引入；
- “自然同构”首次出现时，读者尚不知道“自然”要求哪一个交换关系；后文又直接使用 $H_p(f)$ 与 $f\otimes g$，需要在承担推理前给最短充分说明；
- “非常干净、隐藏的额外类、意外识别”等话不能独立承担数学结论，应还原为 $\kappa_n$ 的满射与单射分别允许什么具体判断；
- HGP 公式若在早段预告，必须明确它是后文应用并给出所需的最短记号桥梁；正式应用处应说明 $C_2\xrightarrow{H_Z^{\mathsf T}}C_1\xrightarrow{H_X}C_0$ 中两个映射的角色，不能让链接承担主解释；
- 一般环谱序列需要让读者知道 $E^{r+1}$ 由 $(E^r,d_r)$ 的同调得到，才能追踪某项怎样存活、被杀或成为边界；
- 全文 876 行，需重新判断每节是否推进主线、证明细节与进阶边界是否处于最短充分深度。不要机械追求缩短；删除或压缩必须服从理解闭合。

不要把这些诊断逐项改写成读者正文中的维护说明。通过整篇重新组织、重写过渡和补足承重桥梁来解决。

# Reader assumptions

## 可以直接依赖

- 基本线性代数、商空间、kernel、image、cokernel 与向量空间 tensor product；
- `Chain complex 与 cochain complex.md` 中 cycle、boundary 与 homology quotient；
- `Cochain complex 的 tensor product.md` 中 total degree、直和分量、product differential 与 Koszul sign；本文采用降 degree 的 chain convention，首次使用时给出最短转换桥梁；
- `二进制空间性质.md` 中向量子空间可选直和补空间且选择一般不唯一。

## 不能直接依赖

- 已经知道 Künneth 定理、比较映射、自然变换或“自然同构”的交换关系；
- 已经理解 contracting homotopy 为什么使每个 cycle 成为 boundary；
- 已经掌握 $\operatorname{Tor}$、flat/K-flat、derived tensor product、谱序列、filtration、associated graded 或 extension；
- 已经能区分 HGP 的物理比特扇区、logical-support quotient 与 Künneth 直和项；
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
- `Notes/07-Lifted-Product Code/Hypergraph product code.md`：只核对 chain convention、logical-support quotient、两类逻辑来源和逻辑比特数记号
- `Notes/07-Lifted-Product Code/Lifted product code.md`：只核对精确入链、环系数边界和展开后二进制秩接口
- J. P. May, *A Concise Course in Algebraic Topology*, Chapter 17 “The Künneth theorem”：核对 PID 短正合列、一般不自然 splitting 与域上自然同构
- The Stacks Project, Tag `06XY`（Derived tensor product）：核对 K-flat 与 ordinary / derived tensor product 的条件
- The Stacks Project, Tag `0H7Z`（Künneth Spectral Sequence）：核对一般环谱序列的假设、指标、页间关系与收敛目标
- `Translations/S003.full.zh-CN.md` 与 `Papers/S003_2025_Menon_magic_tricycles.pdf`：只用于识别补充材料式 (91) 的来源边界；该式不作为一般定理

# 来源与数学边界

- canonical 范围必须保留：比较映射的良定义；域上的自然同构；使用非典范补空间和 contracting homotopy 的证明；二项复形 degree-$1$ 特化；HGP 的两类逻辑来源和 $K$ 公式；PID / 一般环边界；$R_2$ 上比较映射失败的直接反例。
- 固定乘积 chain differential 为

  $$
  \partial(c\otimes d)=\partial_Cc\otimes d+(-1)^{|c|}c\otimes\partial_Dd.
  $$

  只有在 $\mathbb F_2$ 上才能无说明地省略符号。$\partial^2=0$ 的完整证明属于上游笔记，本篇不重复。
- 域上结论使用 $k$ 上的有界有限维链复形。$\kappa_n$ 是自然的；证明中选择的 cycles / boundaries 补空间、收缩与链级分裂一般不自然。
- 域上分裂证明保留一般域的 Koszul 符号：收缩在第一因子时核对交叉项抵消；收缩在第二因子时使用随第一因子 degree 改变的符号。
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
  K=k_Ak_B^{\mathsf T}+k_A^{\mathsf T}k_B.
  $$

  两项称为逻辑来源或 Künneth 直和项，不称为物理扇区；不重推 HGP blocks、CSS 对易或距离。
- PID 结论把精确假设放在公式附近。May 的标准形式允许一个因子逐项 flat；两因子有界逐项自由只是更强而安全的充分条件。结论是带 $\operatorname{Tor}_1$ 的自然短正合列，splitting 一般不自然，Tor 指标满足 $p+q=n-1$。循环 LP 常用的 $R_\ell=\mathbb F_2[x]/\langle x^\ell-1\rangle$ 不能默认为 PID。
- 一般交换环使用 bounded derived Künneth spectral sequence，目标是 $H(C\otimes_R^{\mathbf L}D)$。至少一个因子 K-flat 时 ordinary tensor product 才代表 derived tensor product；有界逐项自由是安全充分条件，但不保证谱序列在 $E^2$ 退化。
- Stacks 使用上同调指标。若改写为同调指标，说明重编号并保持 total degree、收敛目标与微分方向 $d_r:(s,t)\to(s-r,t+r-1)$ 一致。$E^2$ 的高阶 $\operatorname{Tor}$ 还会经历后续微分；$E^\infty$ 只给 associated graded，重组目标同调还有 extension。
- “系数环不是域”只表示域上直和公式不再自动成立，不表示每个非域实例必有非零 $\operatorname{Tor}$、非平凡微分或失败的比较映射。
- $R_2$ 反例是本文直接计算。保留：定义域与目标的二进制维数均为 $2$，但 $\kappa_1$ 的秩为 $1$，既非单射也非满射；两个像代表同一个非零同调类。$R_2$ 有零因子且不是 PID。
- S003 补充材料式 (91) 不作为一般定理。除非另行证明 semisimple、flat/K-flat 或谱序列退化等额外条件，不得用该式支持无条件的一般环直和；读者正文无需展开来源争议。
- 一般 LP 未证明相关平坦性或谱序列退化时，不套用域上的 $K$ 公式；按展开后的二进制 $H_X,H_Z$ 秩计算。非交换左右模与 commuting actions 只作边界提醒并交回 `Lifted product code.md`。
- 不新增来源未支持的定理、参数或一般化。若 May / Stacks 与 canonical 发生实质冲突，返回 `NEEDS_CONTEXT`，不要静默改写。

# 写作权限

## 允许

- 完整替换唯一目标文件；
- 重组内部标题、顺序、例子与证明展开，删除重复解释和不能还原的抽象压缩；
- 根据新版 Writing Guide 自行选择问题驱动、整体先行、worked example 与证明地图的组合；
- 在不牺牲证明闭合的前提下压缩 bookkeeping，并把一般环内容组织成真正可跳读的进阶层。

## 禁止

- 输出或修改其他正式文件、索引、canonical、来源登记、译文或任务外 artifact；
- 删除、移动、拆分、合并或重命名正式文件；
- 删除 canonical 要求保留的定理、证明机制、应用或反例；
- 重复 HGP blocks、CSS 对易、距离、LP balanced relation、环值 blocks、二进制展开或 S007 执行内容；
- 使用“同调扇区”混称 Künneth 直和项与 HGP 物理比特扇区；
- 把任务、审查、allowlist、canonical ownership 或工作流语言写入读者正文；
- 用链接代替比较映射、域上证明、二项特化、HGP chain 角色或一般系数边界所需的关键解释。

必须保留 H1 `# Künneth 分解`，并保留一个标题文字精确为 `PID 与一般系数环` 的二级 heading，使现有入链 `[[Künneth 分解#PID 与一般系数环]]` 继续解析。若只能通过删除、移动、拆分、合并或重命名正式文件解决问题，返回 `DECISION_REQUIRED`。

# 写作要求

- 内部完成教学规划，直接输出完整、可替换的目标 Markdown；不输出设计稿、审查表、修改说明或 patch；
- 让正文围绕一个真实问题持续推进：什么时候 $H(C\otimes D)$ 能由 $H(C)$ 与 $H(D)$ 读出；
- 在读者承担长证明前给出域上的结论、条件、具体含义与后续用途，但所有记号和术语先获得最短充分落点；
- 长证明先说明目标、困难与步骤，随后保留 complement、可缩部分、contracting homotopy 和 tensor summands 的完整逻辑；
- 每条关键公式附近说明对象、映射方向、条件与用途；每条抽象总结都能回到前文的具体对象、关系和后果；
- 首次使用缩写与角色记号时闭合当前含义：HGP / LP 给出中文称呼与英文全称，$K$ 说明为逻辑比特数，第二因子收缩中的 $X$ 说明为任意链复形，PID 除全称外说明“每个理想均为主理想的整环”；
- 例子必须说明展示什么、不能推广什么，并返回一般主线；一般环进阶层跳过后，域上主线与 HGP 回报仍完整；
- 来源、适用条件和指标重编号紧邻相关结论；$R_2$ 反例注明为本文直接计算；
- 使用自然统一的中文教材语体；正文链接有效且不链接 `Notes/WORKING/`；
- 数学严格遵守 `Notes/OBSIDIAN_MATH.md` 的行内与独立块公式规范，不得使用其它定界、JSON 双重转义或未闭合定界符；
- 输出前从头连续复读全文并严格遵守 `Notes/PRO_OUTPUT_PROTOCOL.md`。

# 完成标准

1. 开头建立真实对象和问题；第一次出现 $k$、$H(C)$、HGP、LP、$K$、任意链复形 $X$ 与 PID 时，当前所需含义已经闭合，不靠读者猜测。
2. 域上定理在长证明前出现，并把 $\kappa_n$ 的单射、满射与自然性翻译成可操作的具体判断，而不是由抽象形容词代替。
3. $\kappa_n$ 的 cycle 性、代表元无关性、可逆性和自然性分别有可追踪理由；$H_p(f)$、$f\otimes g$ 等对象在使用前得到说明。
4. 域上证明有清楚地图；补空间、可缩复形、收缩同伦与所有含可缩因子的 tensor summands 的逻辑闭合，Koszul 符号正确。
5. 紧凑成功例子说明它展示的 degree、该例的维数结论不能推广、以及它如何预告一般证明；例子不替代正式定义或证明。
6. 二项复形、HGP chain-complex 角色、logical-$Z$ quotient 与 $K=k_Ak_B^{\mathsf T}+k_A^{\mathsf T}k_B$ 的桥梁连续；两项不与物理扇区混淆。
7. 域、PID、一般交换环形成三层判断；PID 短正合列说明第一箭头单射、第二箭头满射且像等于核；flat/K-flat、derived tensor、页间同调、filtration、associated graded 与 extension 均在承重前得到最短充分说明。
8. $R_2$ 反例计算自洽并展示 $\kappa_1$ 秩为 $1$、非单射且非满射；同时明确非域不等于每例失败。
9. 对 LP 给出可执行的安全判断，不越界重写 LP/HGP/S007 的 owner 内容。
10. 保留精确标题与入链；不采用 S003 式 (91) 作为一般定理；不修改 allowlist 外文件。
11. 每节推进主线或被明确安置为可跳读补充；前后读者能力连续，没有维护者语言、重复定义、竞争性解释或不可还原的总结。
12. 中文、链接与 Obsidian 数学格式通过检查；无 `待核对`、`TODO：补引用` 或 `待补推导`。
