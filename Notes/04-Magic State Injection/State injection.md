State injection 的核心思想是：不直接对数据比特执行难以容错实现的非 Clifford 门，而是预先准备一个携带该非 Clifford 资源的辅助态，再用 Clifford 门、测量和条件修正，把这个门的作用传送到数据比特上。

本文先沿用常见的宽泛说法，把 $T$ 门的注入线路也称为 state injection；更严格地说，下面的线路属于 $T$-gate injection 或 gate teleportation，而“state injection”还常特指把物理魔态注入到逻辑编码空间中。

对 $T$ 门来说，非 Clifford 资源集中在魔态
$$
|A\rangle = T|+\rangle
    = \frac{|0\rangle + e^{i\pi/4}|1\rangle}{\sqrt{2}}
$$
中；注入线路本身只需要 [[Clifford group]] 操作、Pauli 测量和经典前馈。

---
### 最小模型

定义
$$
T =
\begin{pmatrix}
1 & 0 \\
0 & e^{i\pi/4}
\end{pmatrix},
\qquad
\omega = e^{i\pi/4}.
$$

因此
$$
|A\rangle = T|+\rangle
    = \frac{|0\rangle + \omega |1\rangle}{\sqrt{2}}.
$$

这个态也常记作 $|T\rangle$；本文使用 $|A\rangle$ 是为了贴近 magic-state injection 文献中的 ancilla 记号。

可以把 $|A\rangle$ 理解为：$T$ 门的非 Clifford 相位已经被预先写进了辅助量子态。后续注入电路不再实时实现 $T$ 门，而是把这个相位资源转移到数据比特上。

设数据态为
$$
|\psi\rangle = a|0\rangle + b|1\rangle.
$$

使用如下电路：

```text
data:    |ψ⟩ ───●────────────── output
                │
ancilla: |A⟩ ───X─── M_Z
                       │
              if m = 1, apply S on data
```

也就是：

1. 数据比特作为 CNOT 的控制比特。
2. 魔态辅助比特作为 CNOT 的目标比特。
3. 在 $Z$ 基测量辅助比特，测量结果记为 $m \in \{0,1\}$。
4. 若 $m=1$，对数据比特施加 Clifford 修正 $S$。

这里
$$
S =
\begin{pmatrix}
1 & 0 \\
0 & i
\end{pmatrix}.
$$

---
### 关键推导

初态为
$$
|\psi\rangle |A\rangle
=
\frac{1}{\sqrt{2}}
(a|0\rangle + b|1\rangle)
(|0\rangle + \omega |1\rangle).
$$

CNOT 之后，数据比特不变，辅助比特在数据为 $|1\rangle$ 时翻转：
$$
\frac{1}{\sqrt{2}}
\left[
a|0\rangle (|0\rangle + \omega |1\rangle)
+ b|1\rangle (|1\rangle + \omega |0\rangle)
\right].
$$

现在测量辅助比特。

#### 测量结果 $m=0$

取辅助比特为 $|0\rangle$ 的分量，未归一化的数据态为
$$
a|0\rangle + \omega b|1\rangle.
$$

这正是
$$
T|\psi\rangle
=
T(a|0\rangle + b|1\rangle)
=
a|0\rangle + \omega b|1\rangle.
$$

所以当 $m=0$ 时，不需要任何修正。

#### 测量结果 $m=1$

取辅助比特为 $|1\rangle$ 的分量，未归一化的数据态为
$$
\omega a|0\rangle + b|1\rangle.
$$

忽略整体相位 $\omega$，它等价于
$$
a|0\rangle + \omega^{-1} b|1\rangle
=
T^\dagger |\psi\rangle.
$$

这次得到的是 $T^\dagger$，不是 $T$。但是只需要施加 Clifford 门 $S$，因为
$$
S T^\dagger
=
\begin{pmatrix}
1 & 0 \\
0 & i
\end{pmatrix}
\begin{pmatrix}
1 & 0 \\
0 & e^{-i\pi/4}
\end{pmatrix}
=
\begin{pmatrix}
1 & 0 \\
0 & e^{i\pi/4}
\end{pmatrix}
= T.
$$

因此
$$
S T^\dagger |\psi\rangle = T|\psi\rangle.
$$

---
### 测量分支

两个测量结果的概率都是 $1/2$，与 $a,b$ 无关。经过条件修正后，最终确定性得到 $T|\psi\rangle$：

$$
\begin{array}{c|c|c}
\text{测量结果} & \text{数据上得到的门} & \text{修正} \\
\hline
m=0 & T & I \\
m=1 & T^\dagger & S
\end{array}
$$

这里的“确定性”指逻辑效果确定：测量结果本身仍然随机，但随机的 Pauli/Clifford byproduct 可以由经典前馈或 frame update 追踪并修正。

---
### 物理图像

[[Gottesman-Knill theorem]] 说明 Clifford 操作、Pauli 测量和稳定子态可以被高效经典模拟；只靠这些操作不能提供通用量子计算所需的非 Clifford 资源。$T$ 门的作用是引入 Clifford 层级之外的相位。

State injection 把这个困难拆成两部分：

1. 难的部分：制备非稳定子态 $|A\rangle$。
2. 容错友好的部分：用 Clifford 操作、测量和前馈把 $|A\rangle$ 中的相位资源转移到数据比特。

> $T$ 门并不是在注入电路中实时执行的；它已经在魔态 $|A\rangle=T|+\rangle$ 中被预先编码。注入电路只负责把这个非 Clifford 资源消耗掉，并在数据比特上实现等效的 $T$ 门。

---
### 为什么对容错量子计算重要

许多量子纠错码可以较自然地容错实现 Clifford 操作，例如
$$
H,\quad S,\quad \mathrm{CNOT},\quad \text{Pauli measurement}.
$$

但根据 Eastin-Knill 定理，不能依靠一套横向逻辑门直接实现所有通用逻辑门。特别是 $T$ 门通常不能像某些 Clifford 门那样简单横向实现。

因此常见路线是
$$
\boxed{
\text{Clifford 操作}
+
\text{魔态}
+
\text{测量}
+
\text{经典前馈}
}
$$
来间接实现逻辑 $T$ 门。

在这个框架中，真正的非 Clifford 资源是 $|A\rangle$。CNOT、$Z$ 基测量和 $S$ 修正都是 Clifford 操作。

---
### State injection、distillation 与 gate injection

这些术语经常一起出现，但功能不同。

**State injection** 通常指把一个物理层或低编码层的魔态注入到逻辑编码空间中：
$$
|A\rangle_{\mathrm{physical}}
\longrightarrow
|A_L\rangle.
$$

注入本身通常不能保证魔态已经有很高保真度。它解决的是“如何把非稳定子资源带入编码空间”，不是“如何把错误率压低到算法可用水平”。

**Magic-state distillation** 消耗多个有噪声的逻辑魔态，得到数量更少但错误率显著降低的逻辑魔态：
$$
\left(|A_L\rangle_{\mathrm{noisy}}\right)^{\otimes n}
\longrightarrow
|A_L\rangle_{\mathrm{high\,fidelity}}^{\otimes k}.
$$

详见 [[Magic State Distillation]]。

**Gate injection** 或 **gate teleportation** 消耗一个高保真逻辑魔态，通过测量线路在数据逻辑比特上实现逻辑 $T$ 门：
$$
|\psi_L\rangle
\longrightarrow
T_L|\psi_L\rangle.
$$

因此完整流程通常是
$$
\boxed{
\text{物理魔态制备}
\rightarrow
\text{state injection}
\rightarrow
\text{magic-state distillation}
\rightarrow
\text{逻辑 }T\text{ 门注入}
}
$$

---
### 适用范围与易错点

- 上面的推导假设 $|A\rangle$ 是理想魔态，CNOT、测量和 $S$ 修正也是理想操作。
- 在容错语境中，应把数据态、辅助态和修正都替换成逻辑版本：$|\psi_L\rangle$、$|A_L\rangle$、$T_L$、$S_L$。
- 如果魔态有错误，注入电路会把魔态错误转化为数据比特上的逻辑门错误，所以高保真 $T$ 门依赖后续的 [[Magic State Distillation]]。
- $m=1$ 分支中的 $T^\dagger$ 与 $T$ 只差一个 Clifford 修正 $S$，这是这个注入方案能确定性工作的关键。
- 不同文献可能使用不同方向的 CNOT、不同测量基或不同魔态定义；比较线路时必须一起核对 byproduct correction。

---
### 与其它笔记的连接

- [[T state]]：解释 $|A\rangle=T|+\rangle$ 为什么是非稳定子资源。
- [[Clifford group]]：说明注入电路中哪些操作仍在 Clifford 集合内。
- [[Magic State Distillation]]：解释如何把有噪声的逻辑魔态提纯到可用于容错计算。
- [[T gate injection]]：专门讨论消耗 $|A_L\rangle$ 实现逻辑 $T_L$ 的线路和 frame update。
