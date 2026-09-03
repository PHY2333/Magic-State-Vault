---
task_id: 20260903-tensor-direct-sum-up-interface
request_id: R01
request_type: new-note
route: pro-write-review
output_mode: full-file
review_policy: fresh
binding_id: dbee088eca964ef9b0bd70b575751c75
target_files:
  - Notes/07-Lifted-Product Code/张量积与直和泛性质的 HGP-Künneth 接口.md
---

# 用户目标

内部自行完成教学规划，把下述用户素材整理成一篇完整的新笔记。它应帮助已经学过基础线性代数、但尚未真正理解 universal property 的读者回答两个问题：

1. tensor product 为什么能把双线性规则唯一地变成线性映射；
2. direct sum 为什么能把分别定义在不同 summands 上的线性映射唯一地拼起来。

读完后，读者还应能在 HGP 与 Künneth 中识别这两步各自承担的工作，而不会把 ordinary tensor product、direct sum、product-complex totalization、homology quotient 或 balanced tensor 混成同一个构造。

# 用户提供素材中必须吸收的内容

用户原稿不是必须照抄的结构，而是待整理的数学素材。请吸收其中与本篇主线相符的内容，并按教学需要重排、压缩或补足：

- 泛性质不是 tensor product 附加的一条性质，而是刻画 tensor product 及其典范双线性映射的方式；具体 quotient construction 负责证明这样的对象存在；
- 区分三个层次：空间 $V\otimes_kW$、纯张量 $v\otimes w$、由线性映射 $f,g$ 诱导的 $f\otimes g$；一般张量只是有限个纯张量之和，不必是单个纯张量；
- tensor product 的泛性质

  $$
  \operatorname{Hom}_k(V\otimes_kW,X)
  \cong
  \operatorname{Bilin}_k(V\times W,X)
  $$

  以及由自由向量空间商去双线性关系得到的一个具体实现；必须区分“存在一个实现”和“泛性质把所有实现唯一到唯一同构地刻画”；
- direct sum 的 mapping-out 泛性质：由 $f:V\to X$、$g:W\to X$ 唯一得到 $[f,g]:V\oplus W\to X$，并写清包含映射与唯一性；
- 有限 direct sum 还具有 mapping-in 的 product 泛性质，因而是 biproduct；无限族时 direct sum 是 coproduct，direct product 才是 product，不能把有限结论无条件推广；
- 对比 tensor product 与 direct sum 解决的映射问题：一个编码双线性交互，一个保存独立来源并拼接分量映射；
- 精确区分

  $$
  (v,w),
  \qquad
  v\otimes w,
  \qquad
  [v]\otimes[w],
  \qquad
  [v\otimes w].
  $$

  它们的 ambient spaces 不同，不能因符号相似而认作同一个对象；
- 在域 $k$ 上可用一个紧凑段落说明

  $$
  (V/U)\otimes_k(W/S)
  \cong
  \frac{V\otimes_kW}{U\otimes_kW+V\otimes_kS},
  $$

  并解释为何 $[v]\otimes[w]\mapsto[v\otimes w]$ 的目标必须是右侧 quotient。这里的 $U\otimes W$、$V\otimes S$ 通过域上 inclusion 的诱导映射视为子空间；不要把这套写法无条件推广到一般 modules；
- 作为 Künneth 接口，说明先在 cycle representatives 上验证

  $$
  ([c],[d])\longmapsto[c\otimes d]
  $$

  对代表元良定义且双线性，才能由 tensor universal property 得到 $H_p(C)\otimes H_q(D)$ 上的线性比较映射；泛性质本身不替代代表元无关性的证明，也不自动保证该映射是同构；
- 作为 HGP 接口，解释

  $$
  C_1=(A_1\otimes B_0)\oplus(A_0\otimes B_1)
  $$

  中内层 tensor product 与外层 direct sum 的分工：内层配对两个因子的坐标，外层保留两种 total-degree 来源；物理直和分量不能与 Künneth 的逻辑直和项混称；
- 可以保留一个真正服务主线的 worked example，例如双线性型怎样诱导 $V\otimes W\to k$，或 coordinate functionals 怎样检验 $e_i\otimes f_j$ 的线性无关性；例子不能替代定义，也不应发展成第二条主线。

# Reader assumptions

## 可以直接依赖

- 域 $k$ 上的向量空间、线性映射、基、子空间与 quotient space；
- 二元 direct sum 的元素写成 $(v,w)$，并知道线性映射由基上的取值确定；
- kernel、image 与“代表元改变”的基本含义；
- 基础链复形术语只在最后的 Künneth 接口段使用，且该段可以链接上游笔记。

## 不能直接依赖

- 已经理解 universal property、自然同构、coproduct、product 或 biproduct；
- 已经知道 tensor product 的 quotient construction 或一般元素为何是有限纯张量和；
- 已经能从双线性公式无条件写出 tensor product 上的线性映射；
- 已经理解无限 direct sum 与 direct product 的泛性质差别；
- 已经能区分 ordinary tensor、Kronecker matrix blocks、product complex 的 totalization 与 balanced tensor；
- 已经知道 Künneth 比较映射为什么良定义，或它在什么条件下是同构。

# 必须读取

- `Notes/WRITING_GUIDE.md`
- `Notes/OBSIDIAN_MATH.md`
- `Notes/PRO_OUTPUT_PROTOCOL.md`
- `CANONICAL_KNOWLEDGE.md` 中 `Tensor product 与 direct sum`、`Cochain complex 的 tensor product`、`Künneth 分解`、`Balanced tensor product 与 coinvariant quotient` 与 HGP/LP 的 ownership 边界
- `Notes/06-CCZ Distillation/Tensor product 对 direct sum 的分配律.md`
- `Notes/06-CCZ Distillation/Cochain complex 的 tensor product.md`
- `Notes/06-CCZ Distillation/Balanced tensor product 与 coinvariant quotient.md`：只核对 ordinary 与 balanced universal property 的边界，不展开后者
- `Notes/07-Lifted-Product Code/Hypergraph product code.md`：重点核对 $C_1$ 两个物理分量、total degree 与 Künneth 两类逻辑来源的区别
- `Notes/07-Lifted-Product Code/Künneth 分解.md`：重点核对比较映射的良定义、direct-sum 拼接与域／一般系数边界
- `Notes/07-Lifted-Product Code/Lifted product code.md`：重点核对 ordinary、balanced、环值块与二进制展开的边界

# Ownership 与文件职责

仓库已有主笔记 `[[Tensor product 对 direct sum 的分配律]]`。它继续拥有 ordinary tensor product 对 direct sum 分配的自然同构及其 $\Phi,\Psi$ 证明。新笔记位于 `Notes/07-Lifted-Product Code/`，职责是让 HGP/Künneth 读者掌握“验证规则—tensor 线性化—direct-sum 拼接”的映射构造模式。

因此：

- 可以在本篇自足地陈述并解释两条泛性质，也可以用 compact quotient realization 解释 tensor product 的存在；
- 不重写完整 distributivity proof，不重新展开 product differential 的 $\partial^2=0$ 证明，不重写完整 Künneth 证明，不重写 HGP blocks，不定义完整 balanced tensor theory；
- 第一次需要这些下游结果时，以最短充分桥梁说明本篇结论怎样被使用，再链接对应主笔记；
- 正文开头不能用 ownership、仓库路径、任务或维护语言作教材入口；ownership 只通过自然的“延伸阅读”链接体现。

# 数学边界

- 除专门的边界提醒外，正文固定共同系数域 $k$，所有 tensor products 都是 $\otimes_k$；不要把 ordinary tensor product 的结论无条件搬到 $\otimes_R$；
- tensor product 对象应和典范双线性映射 $\tau:V\times W\to V\otimes_kW$ 一起陈述。泛性质的唯一性是因子化映射的唯一性；进一步应说明满足同一泛性质的两个实现之间存在唯一的典范同构；
- quotient construction 若出现，必须列全向量加法与两个变量的标量相容关系，并闭合“关系子空间落入 kernel，所以映射下降到 quotient”的存在性论证；不要把具体构造误写成本质上唯一的底层集合；
- $V\times W$ 是双线性映射的两变量输入集合，$V\oplus W$ 是向量空间；在二元有限维情形它们的底层 pair 表示相似，也不能混淆其线性结构与泛性质；
- 一般 tensor 是有限个 pure tensors 的和，这种分解通常不唯一。若用基展开，则唯一性来自所选 bases 对应的 tensor-product basis；
- 任意指标族的 direct sum 满足

  $$
  \operatorname{Hom}_k\!\left(\bigoplus_iV_i,X\right)
  \cong
  \prod_i\operatorname{Hom}_k(V_i,X).
  $$

  有限族的 direct sum 同时是 product；无限族的 mapping-in 目标一般应为 $\prod_iV_i$。不要因每个 direct sum 都有 coordinate projections 就声称无限 direct sum 满足完整 product universal property；
- quotient-tensor 公式只在向量空间范围内使用。若提一般 modules，必须把相关子对象写成诱导映射的 images 或补充 flatness 条件；本篇宜只作边界提醒；
- Künneth 接口必须保留 Koszul sign 所需的代表元检查，并明确“比较映射存在”与“比较映射是同构”是两件事。域上同构条件与一般环边界交给 `[[Künneth 分解]]`；
- HGP 中 $C_1$ 的两个 summands 是取 kernel/quotient 前的物理坐标来源；Künneth 的两个 summands 是同调层的逻辑来源，不能混用“两个扇区”；
- 不把矩阵 Kronecker product、ordinary tensor product、tensor-product complex 或 balanced tensor product 当成完全相同的对象。只说明必要接口并链接对应 owner；
- 不新增来源未支持的定理或把有限情形静默推广到无限情形。

# 建议的教学主线

这只是组织约束，不要求照抄标题：

1. 从一个真实问题进入：只给出纯张量上的规则或各 summand 上的规则，怎样知道它唯一延伸成整个空间上的线性映射？
2. 用 tensor universal property 解决“双线性规则怎样线性化”，并用 quotient realization 解释存在性；
3. 用 direct-sum universal property 解决“分量映射怎样拼接”，再解释有限 biproduct 与无限族的分叉；
4. 把两种模式并排比较，明确对象、映射方向、输入数据与输出映射；
5. 解释四种相似符号及 quotient representatives；
6. 用一个 worked example 检验读者是否真的能构造映射；
7. 回到 Notes/07：先构造 $\kappa_{p,q}$，再由 direct sum 拼成 $\kappa_n$；解释 HGP 中内层 tensor 与外层 direct sum 的分工；最后标出 balanced tensor 与完整 Künneth 的边界。

主线应由问题、构造、验证和回报串起来，不要写成“概念百科”或把用户素材原顺序逐段搬运。

# 写作权限

## 允许

- 新写唯一目标文件；
- 调整章节结构、删去与主线无关的素材、增加必要的交换关系或逐元素验证；
- 使用一个紧凑例子和一个简洁对照表；表中只放短行内公式；
- 使用 Obsidian wikilinks 连接本任务列出的正式笔记。

## 禁止

- 输出或修改 allowlist 外任何文件；
- 把任务、请求、review、allowlist、canonical ownership 或 Git 语言写入读者正文；
- 重复 `[[Tensor product 对 direct sum 的分配律]]` 中完整 $\Phi/\Psi$ 分配律证明；
- 重复 tensor-product complex、Künneth、HGP 或 balanced tensor 的完整构造与证明；
- 把用户原稿中的 `\(...\)` 或其它不兼容数学定界符带入成稿；
- 以抽象口号、类比或表格代替定义、条件、良定义性和唯一性论证。

# 写作要求

- 标题使用 `# 张量积与直和泛性质的 HGP–Künneth 接口`；
- 用自然、统一的中文教材语体。英文术语首次必要时括注，后文保持一种主称呼；
- 在每条 Hom 对应附近写清映射方向、输入数据、典范映射和唯一性；
- 公式服务于正文推进，不连续堆放 boxed slogans；
- 复杂步骤先说明目的，再给验证，最后回到它解答的问题；
- 链接不能承担主线所需的唯一解释，正文也不得链接 `Notes/WORKING/`；
- 行内公式用 `$...$`，块公式的两个 `$$` 各自单独成行；不得使用 `\(...\)`、`\[...\]`、JSON 双重转义或未闭合的数学定界符；
- 输出前从头连续复读完整文件，并严格遵守 `Notes/PRO_OUTPUT_PROTOCOL.md`。

# 完成标准

1. 开头提出“怎样把局部规则变成唯一整体线性映射”的真实问题，且两种泛性质围绕同一主线出现。
2. tensor product 对象、典范双线性映射、存在唯一因子化与唯一到唯一同构的含义准确。
3. quotient realization 的存在性论证闭合，但没有接管分配律主笔记。
4. pure tensor、一般 tensor 与 $f\otimes g$ 三个层次清楚，至少一个具体例子能实际展示 universal property 的用法。
5. direct sum 的 mapping-out 泛性质及唯一性完整；有限 biproduct 与无限 direct sum/product 的分叉准确。
6. 两种泛性质的比较明确到对象、数据、映射方向和用途，而不只是“独立并列／相互作用”的口号。
7. $(v,w)$、$v\otimes w$、$[v]\otimes[w]$、$[v\otimes w]$ 的 ambient spaces 与相互关系写清楚；quotient-tensor 公式范围准确。
8. Künneth 接口先证明代表元无关并得到 bilinear rule，再使用 tensor universal property；没有把映射存在误写成同构。
9. HGP 的物理 direct-sum 分量与 Künneth 的逻辑 direct-sum 项保持区分。
10. ordinary tensor、product-complex totalization、Kronecker blocks 与 balanced tensor 的边界清楚但不喧宾夺主。
11. 没有重复相邻 owner 的完整证明，没有任务语言或维护者语言。
12. 中文、链接、Markdown 和 Obsidian 数学格式通过检查，输出是唯一目标文件的完整 replace block。
