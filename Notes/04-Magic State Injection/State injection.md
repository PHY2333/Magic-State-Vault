State injection 解决的问题是：如何把难以直接容错实现的非 Clifford 资源带入编码计算，并最终把它消耗为数据逻辑比特上的非 Clifford 门。

这个术语在文献中有两种相近但不同的用法：

- 狭义的 **state injection**：把物理层或低编码层制备的有噪声 magic state 转移到目标逻辑编码空间。
- 常被一并称为 injection 的 **gate injection / gate teleportation**：消耗一个逻辑 magic state，在数据逻辑比特上实现对应的非 Clifford 门。

两者在容错流程中的位置不同：

$$
\boxed{
\text{物理 magic state 制备}
\longrightarrow
\text{state injection}
\longrightarrow
\text{distillation}
\longrightarrow
\text{gate injection}
}
$$

本文先说明狭义 state injection 的输入输出和误差含义，再用 $T$ gate injection 给出可完整验证的线路与公式。具体的物理到逻辑注入线路依赖所用量子码和容错架构，不存在与编码无关的唯一电路。

---
### 1. State injection 的最小模型

定义

$$
T=\operatorname{diag}(1,e^{i\pi/4}),
\qquad
\omega=e^{i\pi/4},
$$

以及 T-type magic state

$$
|T\rangle
=T|+\rangle
=\frac{|0\rangle+\omega|1\rangle}{\sqrt{2}}.
$$

狭义 state injection 的目标可抽象写为

$$
\rho_{T,\mathrm{physical}}
\longrightarrow
\rho_{T,L}^{\mathrm{inj}},
$$

其中输出位于目标量子码的逻辑编码空间。理想情况下希望得到

$$
|T_L\rangle
=T_L|+_L\rangle
=\frac{|0_L\rangle+\omega|1_L\rangle}{\sqrt{2}}.
$$

实际注入通常不是“自动获得一个高保真逻辑态”。它只是把非稳定子资源送入编码空间；物理态制备错误、注入线路错误、测量错误和注入阶段较弱的错误保护都会进入有效输入错误率 $p_{\mathrm{in}}$。

在采用简化的逻辑 $Z_L$ 错误模型时，可以写成

$$
\rho_{T,L}^{\mathrm{inj}}
=
(1-p_{\mathrm{in}})
|T_L\rangle\langle T_L|
+
p_{\mathrm{in}}
Z_L|T_L\rangle\langle T_L|Z_L.
$$

这个表达式隐含了两个条件：

1. 已通过适当的随机化或噪声建模，把相关的态误差化为随机逻辑错误；
2. 忽略 coherent error、leakage 和跨多个注入态的 correlated error。

因此，state injection 主要解决“资源如何进入编码空间”，而不是“资源错误率如何下降”。错误率压低通常由后续 distillation 完成。

---
### 2. 从逻辑 magic state 实现逻辑 T 门

设数据态为

$$
|\psi\rangle
=a|0\rangle+b|1\rangle,
\qquad
|a|^2+|b|^2=1.
$$

先在未编码单比特上推导；把所有态和门替换为逻辑版本后，代数完全相同。

采用以下约定：

```text
data:    |ψ⟩ ───●──────────────── output
                │
ancilla: |T⟩ ───X─── M_Z
                       │
                 m=1: apply S
```

也就是：

1. 数据比特是 CNOT 的控制比特；
2. magic-state 辅助比特是 CNOT 的目标比特；
3. 在 $Z$ 基测量辅助比特，结果记为 $m\in\{0,1\}$；
4. 当 $m=1$ 时，对数据比特施加

$$
S=\operatorname{diag}(1,i).
$$

这里的 CNOT 方向、测量基和结果标号共同决定校正规则。若改变其中任何一项，不能直接照搬“$m=1$ 时施加 $S$”。

---
### 3. 测量分支的精确推导

初态为

$$
|\psi\rangle_d|T\rangle_a
=
\frac{1}{\sqrt{2}}
\left(a|0\rangle_d+b|1\rangle_d\right)
\left(|0\rangle_a+\omega|1\rangle_a\right).
$$

CNOT 后得到

$$
\frac{1}{\sqrt{2}}
\left[
a|0\rangle_d
\left(|0\rangle_a+\omega|1\rangle_a\right)
+
b|1\rangle_d
\left(|1\rangle_a+\omega|0\rangle_a\right)
\right].
$$

把辅助比特投影到测量结果 $m$，可得到作用在数据比特上的未归一化分支算符

$$
K_m
=
{}_a\langle m|
\operatorname{CNOT}_{d\rightarrow a}
|T\rangle_a.
$$

两个分支分别为

$$
K_0
=
\frac{1}{\sqrt{2}}
\begin{pmatrix}
1&0\\
0&\omega
\end{pmatrix}
=\frac{1}{\sqrt{2}}T,
$$

以及

$$
\begin{aligned}
K_1
&=
\frac{1}{\sqrt{2}}
\begin{pmatrix}
\omega&0\\
0&1
\end{pmatrix} \\
&=
\frac{\omega}{\sqrt{2}}
\begin{pmatrix}
1&0\\
0&\omega^{-1}
\end{pmatrix}
=\frac{\omega}{\sqrt{2}}T^\dagger.
\end{aligned}
$$

因此，测量后的未归一化数据态是

$$
|\widetilde{\psi}_0\rangle
=K_0|\psi\rangle
=\frac{1}{\sqrt{2}}T|\psi\rangle,
$$

或

$$
|\widetilde{\psi}_1\rangle
=K_1|\psi\rangle
=\frac{\omega}{\sqrt{2}}T^\dagger|\psi\rangle.
$$

分支概率为

$$
\begin{aligned}
P(m)
&=
\langle\psi|K_m^\dagger K_m|\psi\rangle \\
&=\frac{1}{2},
\qquad m\in\{0,1\}.
\end{aligned}
$$

这里 $P(m)=1/2$ 与输入系数 $a,b$ 无关。

对 $m=1$ 分支使用

$$
ST^\dagger
=
\operatorname{diag}(1,i)
\operatorname{diag}(1,e^{-i\pi/4})
=
\operatorname{diag}(1,e^{i\pi/4})
=T.
$$

令条件校正为

$$
C_m=S^m,
$$

则两个分支统一满足

$$
C_mK_m
=
\frac{\omega^m}{\sqrt{2}}T.
$$

归一化并忽略不可观测的整体相位 $\omega^m$ 后，输出恒为

$$
|\psi_{\mathrm{out}}\rangle=T|\psi\rangle.
$$

对应关系为

$$
\begin{array}{c|c|c|c}
m
&
\text{校正前的数据态}
&
\text{条件校正}
&
\text{校正后}
\\
\hline
0
&
T|\psi\rangle
&
I
&
T|\psi\rangle
\\
1
&
T^\dagger|\psi\rangle
&
S
&
T|\psi\rangle
\end{array}
$$

表中省略了归一化因子和整体相位，但没有省略任何相对相位。

---
### 4. 为什么校正仍然是容错友好的

$T$ 是非 Clifford 门，而 $S$ 是 Clifford 门。因此随机测量结果只产生一个 Clifford byproduct，不要求再次消耗 $|T\rangle$。

不过，$S$ byproduct 不是 Pauli byproduct。实现时有三种常见处理方式：

- 立即执行逻辑 $S_L$；
- 在 Clifford frame 中记录它，并相应修改后续门或测量；
- 把校正吸收到后续 Clifford 电路中。

如果控制系统只维护 Pauli frame，就不能把 $S$ 当作普通 Pauli 校正直接忽略；必须升级为 Clifford-frame 追踪或显式实现校正。

---
### 5. Magic-state 错误如何传到数据比特

为了看清 gate injection 不会自动压低错误率，考虑简化的输入态误差模型

$$
\rho_T
=
(1-p)|T\rangle\langle T|
+
pZ|T\rangle\langle T|Z.
$$

若 CNOT、测量和条件 $S$ 校正均视为理想，则：

- 输入 $|T\rangle$ 时，数据上实现 $T$；
- 输入 $Z|T\rangle$ 时，数据上实现 $ZT$，与测量分支无关，至多相差整体相位。

因此输出信道为

$$
\mathcal{E}_{\mathrm{out}}(\rho)
=
(1-p)T\rho T^\dagger
+
pZT\rho T^\dagger Z.
$$

在这个模型下，magic state 的错误概率以一阶直接变成注入门错误概率：

$$
p_{\mathrm{gate}}=p.
$$

这正是需要 distillation 的原因：gate injection 负责消耗资源并实现门，不负责把 $p$ 变成 $O(p^2)$ 或 $O(p^3)$。

如果 Clifford 操作、逻辑测量或 classical feedforward 也有错误，则总门错误率还要加入这些容错操作的逻辑失败概率。上式只描述理想注入线路对 magic-state 错误的传播。

---
### 6. 逻辑编码版本

在编码空间中，把线路中的对象替换为

$$
|\psi\rangle\rightarrow|\psi_L\rangle,
\qquad
|T\rangle\rightarrow|T_L\rangle,
$$

$$
\operatorname{CNOT}\rightarrow\operatorname{CNOT}_L,
\qquad
M_Z\rightarrow M_{Z_L},
\qquad
S\rightarrow S_L.
$$

理想逻辑线路满足

$$
|\psi_L\rangle|T_L\rangle
\longrightarrow
T_L|\psi_L\rangle,
$$

同时消耗辅助逻辑 magic state。实际架构还必须说明：

- 逻辑 CNOT 由 transversal gate、lattice surgery 还是 code deformation 实现；
- $Z_L$ 测量需要多少轮 syndrome extraction；
- $S_L$ 是物理执行还是由 Clifford frame 追踪；
- routing、idle error、decoder failure 和测量延迟是否计入资源开销；
- 注入态错误与数据块逻辑错误是否独立。

这些实现细节决定实际 logical error rate 和 space-time volume，不能只由上面的理想单比特线路给出。

---
### 7. State injection、distillation 与 gate injection 的区别

$$
\begin{array}{c|c|c|c}
\text{阶段}
&
\text{输入}
&
\text{输出}
&
\text{主要作用}
\\
\hline
\text{state injection}
&
\text{物理或低编码 magic state}
&
\text{目标编码空间中的 noisy }|T_L\rangle
&
\text{把资源送入编码空间}
\\
\text{distillation}
&
n\text{ 个 noisy }|T_L\rangle
&
k\text{ 个更低错误率的 }|T_L\rangle
&
\text{压低 magic-state 错误}
\\
\text{gate injection}
&
|\psi_L\rangle\text{ 和高保真 }|T_L\rangle
&
T_L|\psi_L\rangle
&
\text{把资源消耗为逻辑门}
\end{array}
$$

例如，[[Reed-Muller码]] 给出 15-to-1 distillation 所需的编码结构；[[三正交码与横向逻辑T门]] 进一步解释横向 $T$ 与三正交条件的关系。它们处理的是 distillation 所需的码性质，而本笔记处理的是资源进入编码空间以及资源被消耗为逻辑门时的基本接口。

---
### 8. 适用范围与易错点

- 上述精确线路推导假设 magic state、CNOT、测量和条件校正均为理想操作。
- $m=1$ 分支得到的是 $T^\dagger$，通过 $ST^\dagger=T$ 修正；不能误写成 Pauli 校正。
- 测量后未归一化态必须保留 $1/\sqrt{2}$，否则无法正确得到每个分支的概率 $1/2$。
- 整体相位 $\omega$ 可以忽略，相对相位不能忽略。
- 交换 CNOT 控制与目标、改变测量基或采用 $|T^\dagger\rangle$，都会改变 byproduct correction。
- 简化的随机 $Z$ 错误模型不包含 coherent over-rotation、leakage、measurement error 和 correlated fault。
- state injection 的具体容错性取决于编码与架构；不能仅凭抽象映射 $\rho_{T,\mathrm{physical}}\to\rho_{T,L}^{\mathrm{inj}}$ 推断其有效码距或逻辑错误率。

> 核心区分：state injection 把非稳定子资源送入编码空间，distillation 压低该资源的错误率，gate injection 再把资源消耗为数据上的非 Clifford 逻辑门。
