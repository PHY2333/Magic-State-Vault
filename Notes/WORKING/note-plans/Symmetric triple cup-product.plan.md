# Symmetric triple cup-product 写作蓝图

## 2026-07-05 学习路径重排

### 阅读包

#### 当前笔记
- 文件：`Notes/06-CCZ Distillation/Symmetric triple cup-product.md`。
- 当前问题：`### Integrated Leibniz condition` 先引用 preorientation parity constraints，但 Definition 5 的 local cup-product rule 尚未出现；`### Symmetric triple cup-product` 里使用 Proposition 5 的 in/out pieces，但 Proposition 5 仍在后面。读者在这些章节中必须理解尚未建立的概念。
- 本次目标：重排整篇笔记，使 `Definition 5` 的 classical cup-product 规则和 Menon Proposition 5 的 physical $CCZ$ 基向量判据都出现在第一次需要它们之前。

#### 上游笔记
- 文件：`Notes/06-CCZ Distillation/Tricycle complex 的 balanced-product 构造.md`
  - 继承内容：$C^0=R$、$C^1=R^3$、$C^2=R^3$、$C^3=R$，以及三个 seed elements $a,b,c$。
  - 本文承接方式：先用这些对象建立 sector / coordinate / top-degree integral，再进入 cup-product 读数。
  - 不重复展开：balanced product quotient、$H_X,H_Z,H_{\mathrm{meta}}$ 的矩阵推导。
- 文件：`Notes/06-CCZ Distillation/Cup product 与 Leibniz rule.md`
  - 继承内容：三重 cup product 先得到 $C^3$ cochain，数值读数必须杀掉 representative 改变产生的 coboundaries。
  - 本文承接方式：先定义 Menon 的具体数值读数 $f_{\mathrm{CCZ}}$，再解释 integrated Leibniz 为什么保证 coboundary invariance。
  - 不重复展开：一般 Leibniz rule 和 cohomology 乘法推导。

#### 下游笔记
- 文件：`Notes/06-CCZ Distillation/Menon 2025 Magic Tricycles.md`
  - 下游调用内容：STCP、free=0 constraints、Proposition 5 判据、logical connectivity tensor。
  - 本文边界：当前笔记提供可复用的学习路径；下游只引用结果。

#### 缺失素材
- 缺少的例子：不需要新增数值例子；需要把 $\eta\cup h$、$h\cup\eta$ 和 $p_i,q_j,r_k$ 的三条 top-degree 路径写成正文。
- 缺少的来源：已核对 `.tmp/S003_2025_Menon_magic_tricycles.txt` Appendix D。
- 待核对约定：无。

### 资料研究
- 是否启动：是。
- 理由：用户指出 Definition 5 / Proposition 5 出现太晚，属于学习路径问题；需要按论文 Appendix D 核对原始依赖顺序。
- 来源：
  1. Menon Appendix D：
     - 采用内容：先定义 four-term cochain complex 和 $f_\cup$；再给 Definition 5 的 classical preorientation cup-product；再给 Definition 6 的 symmetric triple cup-product；再给 Proposition 3/4 的 integrated Leibniz 条件；最后给 Proposition 5 的 tricycle physical $CCZ$ 判据。
     - 用途：重排当前笔记顺序。
     - 待核对：无。
- 对主线的影响：不新增前置笔记，只重排当前笔记。

### 学习路径草案

#### 第 1 步：physical $CCZ$ selection 与 logical quotient
- 读者已有知识：CSS/cochain 中 $C^1$ 是 physical support，$H^1(C)$ 是 logical $X$ quotient。
- 本步新增内容：$A_{pqr}$、$f_{\mathrm{CCZ}}$、coboundary invariance 的目标条件。
- 解决的理解障碍：先知道最终要构造什么函数，以及为什么要对 coboundaries 消失。
- 删除本步会导致：后面 integrated Leibniz 不知道要服务哪个 logical gate 条件。
- 下一步如何使用：后面所有 cup-product 构造都为了产生这样的 $f_{\mathrm{CCZ}}$。

#### 第 2 步：tricycle coordinates 与 $\int_R$
- 读者已有知识：balanced product 给出 $R\to R^3\to R^3\to R$。
- 本步新增内容：sector labels $\mathrm I,\mathrm{II},\mathrm{III}$、qubit label $p_i$、$C^3=R$ 上的 $\int_R$。
- 解决的理解障碍：Definition 5 和 Proposition 5 中的 group coordinates、sector labels 和 top-degree coordinate。
- 删除本步会导致：Proposition 5 的集合公式没有坐标落点。
- 下一步如何使用：classical seed cup-product 和 physical 判据都使用这些 labels。

#### 第 3 步：classical preorientation 与 Definition 5
- 读者已有知识：每个 sector 来自 seed complex $R\xrightarrow{\alpha_i}R$。
- 本步新增内容：$\alpha_i=\alpha_i^{\mathrm{in}}+\alpha_i^{\mathrm{out}}+\alpha_i^{\mathrm{free}}$；$\eta\cup h$ 看 out，$h\cup\eta$ 看 in，free 在这两条二元读数里给 $0$。
- 解决的理解障碍：in/out/free 的数学来源。
- 删除本步会导致：Integrated Leibniz condition 和 STCP 中的 in/out/free 都是未定义概念。
- 下一步如何使用：Definition 6 与 Proposition 5 都建立在 Definition 5 的二元读数上。

#### 第 4 步：symmetric triple cup-product
- 读者已有知识：Definition 5 的二元 local cup-product 已建立。
- 本步新增内容：固定括号会导致过强条件；Menon 按 degree-$1$ 变量位置混合括号。
- 解决的理解障碍：symmetric 不是交换律，而是替换固定括号的三线性读数。
- 删除本步会导致：integrated Leibniz 的 symmetric 版本来源不清。
- 下一步如何使用：Proposition 5 的三条路径来自这个 mixed bracketing。

#### 第 5 步：physical $CCZ$ criterion
- 读者已有知识：sector / coordinate / in-out pieces / symmetric triple product。
- 本步新增内容：Proposition 5 的三条 subsets $S_r,S_q,S_p$ 和 $f_{\mathrm{CCZ}}(p_i,q_j,r_k)$。
- 解决的理解障碍：先得到具体 physical 判据，再讨论它是否合法。
- 删除本步会导致：后面说 integrated Leibniz 保证 $f_{\mathrm{CCZ}}$ 合法时，$f_{\mathrm{CCZ}}$ 仍不存在。
- 下一步如何使用：Integrated Leibniz condition 检查这个函数能否下降到 quotient。

#### 第 6 步：integrated Leibniz 与 preorientation constraints
- 读者已有知识：已有 $f_{\mathrm{CCZ}}$ 和 classical preorientation。
- 本步新增内容：integrated Leibniz 杀掉 representative 替换产生的 $C^3$ coboundaries；free=0 constraints 是可检查版本。
- 解决的理解障碍：constraints 是合法性检查，不是 Proposition 5 公式的一部分。
- 删除本步会导致：physical 选择函数和 logical action 无法连接。
- 下一步如何使用：logical connectivity tensor。

### 验收
- 理解验收：旧顺序不通过；新顺序通过，因为每一节只使用前文已定义对象。
- 例子验收：不新增完整例子；Definition 5 的 $\eta,h$ 局部规则和 Proposition 5 的三路径解释足够承担本次障碍。
- 推导验收：通过，条件是正文中明确写出 `Definition 5 -> symmetric triple product -> Proposition 5 -> integrated Leibniz -> quotient`。

### 修订后的学习路径

1. `Physical CCZ 选择数组`
2. `Coboundary invariance`
3. `Tricycle coordinates 与 top-degree integral`
4. `Classical preorientation`
5. `Symmetric triple cup-product`
6. `Physical CCZ criterion`
7. `Integrated Leibniz condition`
8. `Preorientation constraints`
9. `Logical connectivity tensor`
10. `边界`
11. `来源`

### 写作蓝图

正文先说明要构造的是 physical $CCZ$ 的三线性选择函数，并说明它必须对 coboundary 方向消失才能成为 logical gate。随后引入 Menon tricycle complex 的 sector labels 和 $C^3=R$ 上的 $\int_R$，给后面的 top-degree 读数提供坐标。接着前置 Definition 5：preorientation 把 seed coboundary support 分成 in/out/free，并由此定义二元 cup-product 的局部读数。再定义 symmetric triple cup-product 和 Proposition 5 的 physical $CCZ$ 基向量判据。最后回到 integrated Leibniz：它检查 Proposition 5 给出的 $f_{\mathrm{CCZ}}$ 是否满足 coboundary invariance，并由 free=0 parity constraints 给出可计算条件。

### Subagent 检查摘要

- 路径检查：不通过；证据：旧稿 `Integrated Leibniz condition` 在 Definition 5 / Definition 6 / preorientation 建立前引用这些对象。
- 理解检查：不通过；证据：读者读“相应括号和 cup-product 约定”时还不知道 Definition 5/6。
- 推导检查：不通过；证据：旧稿只展示固定左括号情形，尚未铺垫 symmetric triple cup-product 的 mixed bracketing。
- 素材检查：通过；证据：Appendix D 已提供 Definition 5 -> Definition 6 -> Proposition 3 -> Proposition 4 -> Proposition 5 的原始依赖顺序。
- 文体检查：部分通过；证据：正文语言基本像正式笔记，但标题顺序像论文结果堆叠。
- 清稿检查：不通过；证据：需要重排章节，不是局部润色能解决。
- 必须修改：重排为 physical $CCZ$ 目标、quotient 条件、tricycle coordinates / $\int_R$、Definition 5、Definition 6、Proposition 5、integrated Leibniz、constraints、logical tensor。

### 本次写作范围
- 写入当前笔记：整篇 STCP 的章节重排与正文重写。
- 拆出或补充前置：不新增。
- 只建立链接：balanced product、一般 Leibniz、CSS quotient。
- 不在本文展开：Appendix D 的完整逐项 proof、NLR、scheduled depth、single-shot。
- 待核对：无。

### 语言清稿

- 需要修改：
  1. 原顺序：`Integrated Leibniz condition` 在 `Classical preorientation` 前。
     - 问题：使用了尚未出现的 preorientation、bracketing 和 parity constraints。
     - 修改后：移动到 `Proposition 5 criterion` 之后，并改名为 `Symmetric integrated Leibniz condition`。
  2. 原顺序：`Proposition 5 criterion` 在 preorientation constraints 之后，且 integrated Leibniz 之前没有具体 $f_{\mathrm{CCZ}}$ 判据。
     - 问题：读者不知道 integrated Leibniz 正在检查哪个 physical 选择函数。
     - 修改后：在 Definition 5/6 之后先给 Proposition 5 的 physical hyperedge formula，再说明合法性由 integrated Leibniz 检查。
  3. 原标题：`Symmetric triple cup-product` 承担 sector、preorientation、Definition 5、Definition 6 等多层前置。
     - 问题：标题下堆入太多未铺垫对象。
     - 修改后：拆出 `Tricycle coordinates 与 top-degree integral` 和 `Classical preorientation`。
- 可以保留：
  - 句子：`Coboundary invariance 是 physical $CCZ$ 选择函数能否下降到 $H^1(C)$ 的判据。`
    - 理由：它是全篇逻辑目标。
- 通过 / 不通过：通过。

## 2026-07-05 Definition 5 前置清稿

- 触发问题：`Classical preorientation` 一开头就说 “Menon Definition 5”，读者还没有见过该定义，因此后面的解释仍然依赖未建立概念。
- 修改原则：先从 seed map $R\xrightarrow{\alpha_i}R$ 只能给出 coboundary support 讲起，再说明 preorientation 是额外的局部 cup-product 数据；等 $\eta\cup h$、$h\cup\eta$ 和 degree-$0$ 自乘规则都写完后，最后才说明这套规则就是 Appendix D 的 Definition 5。
- 正文处理：去掉导言、`Classical preorientation` 和 `Symmetric triple cup-product` 开头对 Definition 5/6 编号的提前依赖，改成“classical preorientation 给出的二元 cup-product 规则”“上一节定义的二元 cup product”，并在规则写完后再标注 Appendix D 的 Definition 5/6。
- 结果：读到 `Classical preorientation` 时不需要预先知道 Definition 5；编号只作为来源标签出现，不再作为推导前提。

## 阅读包

### 当前笔记
- 文件：`Notes/06-CCZ Distillation/Symmetric triple cup-product.md`。
- 当前问题：`### Symmetric triple cup-product`、`### Proposition 5 criterion`、`### Preorientation constraints` 三节有定义堆叠感；in/out/free 的来源、用途和与 Proposition 5 的关系不够清楚；Proposition 5 的三重交集公式缺中间路径。
- 本次目标：只重写这三节，使主线从 classical preorientation、symmetric triple cup-product、integrated Leibniz、Proposition 5 三元组判据连续推进。

### 上游笔记
- 文件：`Notes/06-CCZ Distillation/Tricycle complex 的 balanced-product 构造.md`
  - 继承内容：Menon tricycle complex 为 $R\to R^3\to R^3\to R$，其中 $C^1=R^3$ 是三个 data sectors，$C^3=R$ 是 top-degree/metacheck coordinate。
  - 本文承接方式：只使用 $C^1=R^3$ 的 sector label 和 $C^3=R$ 的 group coordinate，不重推 balanced product quotient 和矩阵。
  - 不重复展开：$H_X,H_Z,H_{\mathrm{meta}}$ 的矩阵来源、$R\otimes_RR\otimes_RR\cong R$ 的证明。
- 文件：`Notes/06-CCZ Distillation/Cup product 与 Leibniz rule.md`
  - 继承内容：cup product 要下降到 cohomology，representative 改变产生的 coboundary 必须被读数泛函杀掉；三重 cup product 先落在 $C^3$。
  - 本文承接方式：直接使用 integrated Leibniz/coboundary invariance 关系，说明 preorientation 是为了让这些积分后的 coboundary 项消失。
  - 不重复展开：一般 Leibniz rule 推导、Koszul sign、simplicial cup product 例子。
- 文件：`Notes/06-CCZ Distillation/Cochain complex 的 tensor product.md`
  - 继承内容：三个二项 complex 乘成四项 complex，degree $1$ sector 有三种来源。
  - 本文承接方式：只保留 sector label 的含义，不重讲 tensor-product total degree。

### 下游笔记
- 文件：`Notes/06-CCZ Distillation/Menon 2025 Magic Tricycles.md`
  - 下游调用内容：使用 STCP、free=0 parity constraints、Proposition 5 的 $f_{\mathrm{CCZ}}$，再连接到 logical hypergraph magic state。
  - 本文边界：当前笔记提供可复用的 STCP 判据；下游不应重新证明 Proposition 5，也不在当前笔记展开 single-shot、scheduled depth 或 subrank。
- 文件：`Notes/00-index.md`
  - 下游调用内容：只作为路线图提及 STCP。
  - 本文边界：本次不改变主线结构，不更新 index。

### 缺失素材
- 缺少的例子：不需要新增完整数值例子；需要补的是 Proposition 5 三个集合作为三条到 $C^3=R$ 的路径。
- 缺少的来源：已核对 Menon 论文 Appendix D 的 Definition 5、Definition 6、Proposition 3、Proposition 4、Theorem D.1 和 Proposition 5。
- 待核对约定：无。需避免把 free=0 parity constraints 写成 free 非空情形的完整判据。

## 资料研究

- 是否启动：是。
- 理由：用户明确指出“为什么要拆成 in/out/free 三部分，拆成这样有什么意义”不清楚；该问题需要核对论文 Appendix D 中 preorientation 与 integrated Leibniz 的原始关系。
- 来源：
  1. 来源：`Papers/S003_2025_Menon_magic_tricycles.pdf`，Appendix D。
     - 采用内容：Definition 5 把 classical two-term complex 中的 coboundary support 分成 $\delta_{\mathrm{in}}$、$\delta_{\mathrm{out}}$、$\delta_{\mathrm{free}}$，并由此定义 classical cup product；Definition 6 用 mixed parentheses 定义 symmetric triple cup-product；Proposition 3 说明 symmetric integrated Leibniz 足以推出 coboundary invariance；Proposition 4 给出 in/out/free 的 parity subconditions；free=0 时式 (52)-(54) 给出 group-algebra 元素的简化条件；Proposition 5 给出 physical $CCZ$ 判据。
     - 用途：补足 in/out/free 的动机、合法性条件和 Proposition 5 交集公式的来源。
     - 待核对：无。
  2. 来源：`Notes/06-CCZ Distillation/Menon 2025 Magic Tricycles.md`。
     - 采用内容：下游如何引用 STCP、parity constraints、Proposition 5 和 logical hypergraph state。
     - 用途：确认当前笔记应提供的可复用结论。
     - 待核对：无。
- 对主线的影响：本次不新增前置笔记；三节内部增加推导和动机，保留 STCP 主笔记边界。

## 学习路径草案

### 第 1 步：从 $C^1=R^3$ 的 sector labels 进入
- 读者已有知识：balanced product 笔记已经给出 $C^1=R^3$、$C^3=R$。
- 本步新增内容：每个 physical qubit label 写成 $p_i$，其中 $p\in G$，$i\in\{\mathrm I,\mathrm {II},\mathrm {III}\}$。
- 解决的理解障碍：Proposition 5 中 $p_i,q_j,r_k$ 的 sector label 和 group coordinate 分别是什么。
- 删除本步会导致：后面的 $\mathbf 1_{\{i,j,k\}\text{ pairwise distinct}}$ 和 $\alpha_i$ 记号突然出现。
- 下一步如何使用：sector label 决定使用哪一个 seed element $\alpha_i$ 和哪种 local support piece。
- 是否需要素材：不需要外部素材。

### 第 2 步：preorientation 来自 classical two-term complex 的 cup product
- 读者已有知识：cup product 是额外乘法，Leibniz rule 控制 representative 改变。
- 本步新增内容：在 classical seed $R\xrightarrow{\alpha_i}R$ 中，$\alpha_i\gamma$ 是 basis coboundary；preorientation 把这个 coboundary support 分成 in/out/free 三份。
- 解决的理解障碍：in/out/free 不是任意装饰，而是 cup product 读 coboundary support 时的方向数据。
- 删除本步会导致：读者无法理解为什么要拆三份，以及为什么拆分不改变 code maps。
- 下一步如何使用：in/out pieces 进入 Proposition 5 的三条到 $C^3$ 的路径；free part 进入完整 integrated Leibniz 条件。
- 是否需要素材：已由 Appendix D Definition 5 支持。

### 第 3 步：symmetric triple cup-product 的括号意义
- 读者已有知识：固定括号的三重 cup product 能给出 $C^3$ cochain。
- 本步新增内容：Menon 不固定使用 $(x\cup y)\cup z$，而是按三元组中 degree-$1$ 变量的位置选择括号，从而轮换处理三条 representative 替换路径。
- 解决的理解障碍：symmetric 不是交换律，而是避免固定括号偏向某一条路径。
- 删除本步会导致：Proposition 5 的三个集合看起来像外加公式。
- 下一步如何使用：解释 $S_r,S_q,S_p$ 是三个候选 qubits 通过另两个 sector 的 pieces 到达同一 top coordinate 的路径。
- 是否需要素材：Appendix D Definition 6。

### 第 4 步：Proposition 5 三重交集
- 读者已有知识：每个 sector 的 seed element 分为 $\alpha_i^{\mathrm{in}}+\alpha_i^{\mathrm{out}}+\alpha_i^{\mathrm{free}}$。
- 本步新增内容：给定 $p_i,q_j,r_k$，三条到 $C^3=R$ 的路径分别是 $r\alpha_i^{\mathrm{in}}\alpha_j^{\mathrm{in}}$、$q\alpha_i^{\mathrm{in}}\alpha_k^{\mathrm{out}}$、$p\alpha_j^{\mathrm{out}}\alpha_k^{\mathrm{out}}$；交集奇偶就是积分读数。
- 解决的理解障碍：为什么集合从 $r,q,p$ 出发、为什么使用这些 sector indices、为什么要取交集。
- 删除本步会导致：Proposition 5 判据仍然跳步。
- 下一步如何使用：交集奇偶定义 physical $CCZ$ 选择函数。
- 是否需要素材：Appendix D Proposition 5。

### 第 5 步：preorientation constraints 先于 Proposition 5 的逻辑合法性
- 读者已有知识：$f_{\mathrm{CCZ}}$ 必须对 coboundary 方向消失才能下降到 $H^1$。
- 本步新增内容：free=0 时，Appendix D 的 conditions 压成三类 parity constraints；这些条件检查 integrated Leibniz，而 Proposition 5 负责在合法 preorientation 上读出 physical gates。
- 解决的理解障碍：Proposition 5 与 constraints 的先后关系。
- 删除本步会导致：读者误以为交集公式自动保证任意分割合法。
- 下一步如何使用：进入 logical connectivity tensor。
- 是否需要素材：Appendix D Proposition 4 和式 (52)-(54)。

## 理解验收

### 卡点
1. 卡点：in/out/free 的动机。
   - 读者缺少什么：classical seed coboundary support 与 cup product 规则之间的连接。
   - 后文哪里会断：Proposition 5 中的 in/out pieces 和 free part 的边界。
   - 处理方式：重写。
2. 卡点：三重交集公式。
   - 读者缺少什么：三个候选 qubits 到同一个 $C^3=R$ coordinate 的路径解释。
   - 后文哪里会断：$|S_1\cap S_2\cap S_3|$ 为什么等于 integrated triple product。
   - 处理方式：补推导。
3. 卡点：constraints 与 Proposition 5 的关系。
   - 读者缺少什么：先检查 integrated Leibniz，再用交集公式选门。
   - 后文哪里会断：logical connectivity tensor 的良定义性。
   - 处理方式：重写。

### 结论
- 通过 / 不通过：通过，条件是正文必须补上述三处。
- 必须修改：目标三节全部重写，不新增前置笔记。

## 例子验收

- 是否需要例子：不需要完整数值例子。
- 具体对象：用一般候选 qubits $p_i,q_j,r_k$ 的三条路径作为“局部操作过程”。
- 操作过程：列出 $S_r,S_q,S_p$，说明它们都位于 $C^3=R$ 的 group coordinate；交集非空表示三条路径命中同一 coordinate。
- 解决的困难：说明 Proposition 5 的集合公式不是纯记号，而是 integrated triple product 的 coordinate-level 读数。
- 如何回到正式定义：将交集奇偶写成 $f_{\mathrm{CCZ}}(p_i,q_j,r_k)$。
- 不承担什么：不证明 Appendix D 的完整 inherited cup-product 计算，也不枚举具体 code。
- 通过 / 不通过：通过。

## 推导验收

- 上游公式或定义：
  - $H^1(C)=\ker\delta^1/\operatorname{im}\delta^0$。
  - $f_{\mathrm{CCZ}}(\delta^0u,y,z)=0$ 是下降到 quotient 的条件。
  - $C^3=R$ 和 $\int_R$ 把 $C^3$ cochain 读成 $\mathbb F_2$ 数。
  - Appendix D Definition 5、Definition 6、Proposition 3、Proposition 4、Proposition 5。
- 本文目标：解释 Menon 的 STCP 如何从 preorientation 产生 physical $CCZ$ 判据，并说明 free=0 parity constraints 如何保证 coboundary invariance。
- 中间步骤：
  1. $C^1=R^3$ 给 sector label；sector $i$ 的 seed map 是乘以 $\alpha_i$。
  2. 对 basis element $\gamma$，$\alpha_i\gamma$ 的 support 被分成 in/out/free 三份。
  3. symmetric triple cup-product 按 degree-$1$ 变量位置选择括号，控制三条 representative 替换路径。
  4. 对 $p_i,q_j,r_k$，三条路径 $S_r,S_q,S_p$ 同时命中某个 $C^3$ coordinate 时贡献一次。
  5. free=0 parity constraints 检查 integrated Leibniz；合法后 $f_{\mathrm{CCZ}}$ 满足 coboundary invariance。
- 关键条件的作用：
  - pairwise distinct sector 条件保证三条路径覆盖三个不同 seed directions。
  - in/out pieces 决定 Proposition 5 中到 top coordinate 的方向选择。
  - free part 不进入简化 Proposition 5 公式，但进入完整 integrated Leibniz 条件；free=0 时可用三类 parity constraints。
- 待核对点：无。
- 通过 / 不通过：通过。

## Subagent 检查摘要

- 路径检查：不通过；证据：原文先用“合法 preorientation”再在下一节解释合法性，容易误读为任意分割可用。
- 理解检查：不通过；证据：in/out/free 只被说成 support partition，没有说明服务于 integrated Leibniz。
- 推导检查：不通过；证据：Proposition 5 三个集合直接出现，缺少到 $C^3=R$ 的三条路径。
- 素材检查：部分通过；证据：本地上下游一致，但 subagent 未核对 PDF。主 agent 已核对 Appendix D，消解待核对。
- 文体检查：部分通过；证据：标题可用，但定义堆叠感来自推导缺口。
- 清稿检查：不通过；证据：$\delta_{i\ne j\ne k}$ 链式不等号容易歧义。
- 必须修改：补 preorientation 动机、补三条路径、明确 constraints 与 Proposition 5 先后关系，替换歧义 indicator。

## 修订后的学习路径

### 第 1 步：sector 与 seed labels
- 读者已有知识：$C^1=R^3$、$C^3=R$。
- 本步新增内容：$p_i$ 表示 sector $i$ 中 group coordinate $p$ 的 qubit，$\alpha_{\mathrm I}=a$、$\alpha_{\mathrm {II}}=b$、$\alpha_{\mathrm {III}}=c$。
- 解决的理解障碍：Proposition 5 的变量和 sector indicator。
- 下一步如何使用：sector 决定使用哪些 $\alpha_i$ pieces。

### 第 2 步：preorientation 的来源与意义
- 读者已有知识：representative 改变会产生 coboundary。
- 本步新增内容：preorientation 是对每个 seed coboundary support 的 in/out/free 分割，用来定义 classical cup product 的局部读取规则。
- 解决的理解障碍：拆分不是改变 code，而是添加 cup-product 数据。
- 下一步如何使用：in/out pieces 进入 physical $CCZ$ 交集公式；free part 进入完整合法性条件。

### 第 3 步：symmetric triple cup-product
- 读者已有知识：固定括号可得 $C^3$ cochain。
- 本步新增内容：Menon 依据 degree-$1$ 变量位置混合括号顺序，避免固定括号只偏向某两条 representative 替换路径。
- 解决的理解障碍：symmetric 的含义和它为何改动旧条件。
- 下一步如何使用：为三条到 $C^3$ 的路径铺垫。

### 第 4 步：Proposition 5 判据
- 读者已有知识：每个 $\alpha_i$ 已分为 in/out/free。
- 本步新增内容：三个候选 qubits 分别通过另两个 sector 的 in/out pieces 到 $C^3=R$；同一 coordinate 的命中奇偶给出 $f_{\mathrm{CCZ}}$。
- 解决的理解障碍：交集公式的来源。
- 下一步如何使用：定义 physical $CCZ$ 选择数组。

### 第 5 步：free=0 constraints 与合法性
- 读者已有知识：coboundary invariance 是 logical gate 的必要条件。
- 本步新增内容：free=0 时的 parity constraints 是 integrated Leibniz 的可计算版本；通过后 Proposition 5 的 $f_{\mathrm{CCZ}}$ 才下降到 $H^1$。
- 解决的理解障碍：constraints 与 Proposition 5 不是并列定义，而是合法性与读数的关系。
- 下一步如何使用：进入 logical connectivity tensor。

## 本次写作范围

- 写入当前笔记：目标三节的重写；补 preorientation 动机、symmetric bracket 的最小说明、Proposition 5 三条路径、free=0 constraints 的适用范围。
- 拆出或补充前置：不新增前置笔记。
- 只建立链接：继续引用 balanced product、cup product 与 Leibniz rule、Menon 论文。
- 不在本文展开：balanced product 矩阵推导、一般 cup product 教程、Appendix D inherited cup-product 的完整逐项证明、scheduled depth、NLR、single-shot。
- 待核对：无。

## 写作蓝图

### 正文主线
正文从 $C^1=R^3$ 的 sector label 和 seed element $\alpha_i$ 开始。随后说明 preorientation 是在 classical seed coboundary support 上添加的 cup-product 方向数据，它把每个 $\alpha_i\gamma$ 分成 in/out/free 三份。接着引入 symmetric triple cup-product：Menon 混合括号顺序，使三条 representative 替换路径都能由 integrated Leibniz 控制。然后用 Proposition 5 把三个候选 qubits 到同一个 $C^3=R$ coordinate 的三条路径写成交集判据。最后说明 free=0 parity constraints 是 integrated Leibniz 的可计算条件，合法后 Proposition 5 的 $f_{\mathrm{CCZ}}$ 才能下降到 $H^1(C)$。

### 章节安排

#### 标题：Symmetric triple cup-product
- 本节处理的具体数学对象：$C^1=R^3$ sectors、qubit label $p_i$、seed elements $\alpha_i$、preorientation partition、symmetric triple cup-product 的括号规则。
- 从上一节如何过渡：上一节说明 integrated Leibniz 杀掉 $C^3$ coboundaries；本节说明 Menon 为实现这一点给 seed coboundaries 加 preorientation。
- 本节需要铺垫什么：preorientation 不改变 $\delta$ maps；它只决定 cup product 在 coboundary support 上如何读 in/out/free。
- 本节结束时读者应得到什么：in/out/free 服务于 cup-product 读数与 integrated Leibniz，free part 不进入简化 Proposition 5 公式但不能从合法性中消失。
- 不应直接写入的验收语言：不要写“解决理解障碍”“本节需要说明”。

#### 标题：Proposition 5 criterion
- 本节处理的具体数学对象：候选 qubits $p_i,q_j,r_k$，三条 subsets $S_r,S_q,S_p\subseteq G$，pairwise-distinct sector indicator。
- 从上一节如何过渡：preorientation 给出了 $\alpha_i^{\mathrm{in}}$、$\alpha_i^{\mathrm{out}}$；现在把它们代入三条到 $C^3=R$ 的路径。
- 本节需要铺垫什么：当 $i,j,k$ 两两不同时，三条路径才覆盖三个不同 seed directions；若任意两个 sector 相同，STCP 读数为零。
- 本节结束时读者应得到什么：交集奇偶即 physical $CCZ$ 选择函数的基向量值。
- 不应直接写入的验收语言：不要写“这一步解释为什么”。

#### 标题：Preorientation constraints
- 本节处理的具体数学对象：free=0 条件下的 parity constraints、完整 Appendix D integrated Leibniz 条件、coboundary invariance。
- 从上一节如何过渡：Proposition 5 给出读数；本节给出什么时候这个读数合法。
- 本节需要铺垫什么：constraints 检查 representative 替换产生的 integrated coboundaries 是否消失。
- 本节结束时读者应得到什么：先验证 preorientation constraints，再使用 Proposition 5；free 非空时不能套用三行简化 constraints。
- 不应直接写入的验收语言：不要写“必须修改”“通过验收”。

### 例子安排
- 例子出现位置：不放独立例子；在 Proposition 5 中用 $S_r,S_q,S_p$ 的路径解释替代。
- 例子前需要铺垫：先定义 $p_i,q_j,r_k$ 和 pairwise distinct sectors。
- 例子只说明：三条路径为何取交集。
- 例子不承担：不证明 Proposition 5 的全部 inherited cup-product 计算。

### 推导安排
- 必须完整写：
  - $\alpha_i=\alpha_i^{\mathrm{in}}+\alpha_i^{\mathrm{out}}+\alpha_i^{\mathrm{free}}$ 的 partition 如何诱导 $\alpha_i\gamma$ 的 partition。
  - $S_r,S_q,S_p$ 如何都落在 $C^3=R$ 的 group coordinate。
  - free=0 parity constraints 的三行公式和适用范围。
- 只说明理由：
  - symmetric triple cup-product 的 mixed parentheses 来自 Definition 6，不逐项列出所有 classical cases。
  - Proposition 5 的完整 proof 是 Appendix D 的 inherited cup-product 计算。
- 只外链：
  - balanced product、一般 Leibniz rule、tensor-product signs、single-shot/NLR/depth。

### 标题检查
- 标题是否为主题短语：是。
- 是否有完整判断句标题：无。

### 验收语言过滤
- 是否残留“本文只处理”“本文不”“为了看清”“解决的理解障碍”“输入/输出”等验收语言：无。
- 替换方案：正式正文直接写对象、公式和用途。

## 语言清稿

- 需要修改：
  1. 原句：`$\delta_{i\ne j\ne k}$ 等于 $1$ 当且仅当 $i,j,k$ 两两不同。`
     - 问题：链式不等号容易歧义，subagent 已指出该符号不稳。
     - 修改后：改为先定义 $\mathbf 1_{\mathrm{pd}}(i,j,k)$，再在 Proposition 5 公式中使用该 indicator。
  2. 原句：`例如对 $G$ 的子集 $S,T\subseteq G$，$pST=\{pst:s\in S,\ t\in T\}$。`
     - 问题：Proposition 5 中实际使用的是 $\mathbb F_2[G]$ 的乘法；如果多个乘积项给出同一 group element，可能发生 mod 2 抵消。
     - 修改后：先说明 $p\beta\gamma$ 在 $\mathbb F_2[G]$ 中计算后取 support，再给无抵消时的集合乘法读法。
  3. 原句：`若 degree-$0$ basis element 与 degree-$1$ basis element 相乘，$\mathrm{out}$ piece 决定它从左侧作用时能读到哪些 coboundary coordinates，$\mathrm{in}$ piece 决定它从右侧作用时能读到哪些 coboundary coordinates。`
     - 问题：只给方向描述，读者仍看不到 Definition 5 的局部判定规则。
     - 修改后：补出 $\eta\cup h$ 与 $h\cup\eta$ 的两个分段公式，分别说明 out 和 in pieces 如何保留 $C^1$ coordinate。
- 可以保留：
  - 句子：`preorientation 不改变 seed map $\gamma\mapsto\alpha_i\gamma$，而是在同一个 coboundary support 上指定 cup product 可以沿哪些 local pieces 读数。`
    - 理由：它直接说明 in/out/free 的数学作用，不是验收语言。
  - 句子：`Proposition 5 只给出 physical 三元组的读数公式；preorientation 的合法性来自 integrated Leibniz 条件。`
    - 理由：它明确读数与合法性的先后关系。
- 通过 / 不通过：通过。
