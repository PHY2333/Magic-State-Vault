CPTP 映射是量子信息里描述**一般量子过程**的数学对象。它比酉演化更一般，可以描述噪声、退相干、测量后丢弃结果、量子信道等。

CPTP 是两个条件的缩写：

[  
\text{CPTP}=\text{completely positive and trace preserving}.  
]

也就是：

[  
\text{完全正映射}+\text{保迹映射}.  
]

---

# 1. 为什么需要 CPTP 映射？

封闭量子系统的演化是酉演化：

[  
\rho\longmapsto U\rho U^\dagger.  
]

但真实量子系统一般会和环境相互作用，所以仅靠酉演化不够。比如：

[  
\text{系统}+\text{环境}  
]

整体可以酉演化，但只看系统本身时，系统的演化通常不是酉的。

因此我们用更一般的量子信道：

[  
\mathcal E:\rho\mapsto \mathcal E(\rho).  
]

这里 (\rho) 是密度矩阵，要求：

[  
\rho\geq 0,\qquad \operatorname{Tr}\rho=1.  
]

经过物理过程后，输出仍然应该是合法密度矩阵：

[  
\mathcal E(\rho)\geq 0,\qquad \operatorname{Tr}\mathcal E(\rho)=1.  
]

---

# 2. Positive 与 Completely Positive

一个映射 (\mathcal E) 如果满足：

[  
\rho\geq 0  
\quad\Longrightarrow\quad  
\mathcal E(\rho)\geq 0,  
]

就叫 **positive map**，正映射。

但在量子信息里，仅仅 positive 不够。因为系统可能和另一个辅助系统纠缠。即使 (\mathcal E) 只作用在系统 (A) 上，我们也要求：

[  
I_R\otimes \mathcal E_A  
]

作用在联合系统 (RA) 上仍然保持正性。

也就是说，对于任意辅助系统 (R)，都有：

[  
\rho_{RA}\geq 0  
\quad\Longrightarrow\quad  
(I_R\otimes \mathcal E_A)(\rho_{RA})\geq 0.  
]

这叫 **completely positive**，完全正。

所以 complete positivity 的意思是：

> 即使系统和任意外部参考系统纠缠，映射仍然不能把合法态变成非法态。

---

# 3. Trace Preserving 是什么？

密度矩阵的迹表示总概率：

[  
\operatorname{Tr}\rho=1.  
]

如果一个过程是确定发生的物理过程，那么输出态也应该满足：

[  
\operatorname{Tr}\mathcal E(\rho)=1.  
]

更一般地，对于任意输入算符 (\rho)，trace preserving 要求：

[  
\operatorname{Tr}\mathcal E(\rho)=\operatorname{Tr}\rho.  
]

这就是 **保迹**。

---

# 4. Kraus 表示

CPTP 映射最常用的表示方式是 Kraus 表示：

# [  
\mathcal E(\rho)

\sum_a K_a\rho K_a^\dagger.  
]

这里的 (K_a) 称为 Kraus 算符。

每个 (K_a) 可以理解为一种可能的噪声分支或环境分支。比如 Pauli 噪声可以写成：

# [  
\mathcal E(\rho)

p_I\rho  
+  
p_X X\rho X  
+  
p_Y Y\rho Y  
+  
p_Z Z\rho Z.  
]

这对应 Kraus 算符：

[  
K_I=\sqrt{p_I}I,  
]

[  
K_X=\sqrt{p_X}X,  
]

[  
K_Y=\sqrt{p_Y}Y,  
]

[  
K_Z=\sqrt{p_Z}Z.  
]

于是：

# [  
\mathcal E(\rho)

K_I\rho K_I^\dagger  
+  
K_X\rho K_X^\dagger  
+  
K_Y\rho K_Y^\dagger  
+  
K_Z\rho K_Z^\dagger.  
]

---

# 5. Kraus 算符如何表示 trace preserving？

这是最重要的结论。

如果

[  
\mathcal E(\rho)=\sum_a K_a\rho K_a^\dagger,  
]

那么 (\mathcal E) 是 trace preserving，当且仅当：

[  
\boxed{  
\sum_a K_a^\dagger K_a=I  
}  
]

这就是 Kraus 表示下的保迹条件。

---

## 推导

从 Kraus 表示出发：

[  
\mathcal E(\rho)=\sum_a K_a\rho K_a^\dagger.  
]

取迹：

# [  
\operatorname{Tr}\mathcal E(\rho)

\operatorname{Tr}\left(  
\sum_a K_a\rho K_a^\dagger  
\right).  
]

利用迹的线性性：

# [  
\operatorname{Tr}\mathcal E(\rho)

\sum_a  
\operatorname{Tr}  
\left(  
K_a\rho K_a^\dagger  
\right).  
]

再用迹的循环性质：

[  
\operatorname{Tr}(ABC)=\operatorname{Tr}(BCA).  
]

所以：

# [  
\operatorname{Tr}  
\left(  
K_a\rho K_a^\dagger  
\right)

\operatorname{Tr}  
\left(  
K_a^\dagger K_a\rho  
\right).  
]

因此：

# [  
\operatorname{Tr}\mathcal E(\rho)

\sum_a  
\operatorname{Tr}  
\left(  
K_a^\dagger K_a\rho  
\right).  
]

把求和放进去：

# [  
\operatorname{Tr}\mathcal E(\rho)

\operatorname{Tr}  
\left[  
\left(  
\sum_a K_a^\dagger K_a  
\right)  
\rho  
\right].  
]

如果要对任意 (\rho) 都满足：

[  
\operatorname{Tr}\mathcal E(\rho)=\operatorname{Tr}\rho,  
]

就必须有：

[  
\sum_a K_a^\dagger K_a=I.  
]

因为这样：

# [  
\operatorname{Tr}\mathcal E(\rho)

# \operatorname{Tr}(I\rho)

\operatorname{Tr}\rho.  
]

所以保迹条件就是：

[  
\boxed{  
\sum_a K_a^\dagger K_a=I.  
}  
]

---

# 6. 一个酉演化的例子

酉演化是 CPTP 映射的特例：

[  
\mathcal E(\rho)=U\rho U^\dagger.  
]

这时只有一个 Kraus 算符：

[  
K_1=U.  
]

保迹条件变成：

[  
K_1^\dagger K_1=U^\dagger U=I.  
]

这正是酉算符的定义。

所以酉演化当然是 trace preserving。

---

# 7. Pauli channel 的例子

单比特 Pauli channel 为：

# [  
\mathcal E(\rho)

p_I\rho  
+  
p_XX\rho X  
+  
p_YY\rho Y  
+  
p_ZZ\rho Z.  
]

对应 Kraus 算符：

[  
K_I=\sqrt{p_I}I,\quad  
K_X=\sqrt{p_X}X,\quad  
K_Y=\sqrt{p_Y}Y,\quad  
K_Z=\sqrt{p_Z}Z.  
]

检查保迹条件：

# [  
\sum_a K_a^\dagger K_a

p_I I^\dagger I  
+  
p_X X^\dagger X  
+  
p_Y Y^\dagger Y  
+  
p_Z Z^\dagger Z.  
]

因为：

[  
I^\dagger I=X^\dagger X=Y^\dagger Y=Z^\dagger Z=I,  
]

所以：

# [  
\sum_a K_a^\dagger K_a

(p_I+p_X+p_Y+p_Z)I.  
]

如果概率归一化：

[  
p_I+p_X+p_Y+p_Z=1,  
]

那么：

[  
\sum_a K_a^\dagger K_a=I.  
]

因此 Pauli channel 是 trace preserving。

---

# 8. Amplitude damping 的例子

振幅阻尼通道描述激发态 (|1\rangle) 以概率 (\gamma) 衰减到基态 (|0\rangle)。

它的 Kraus 算符可以写成：

[  
K_0=  
\begin{pmatrix}  
1&0\  
0&\sqrt{1-\gamma}  
\end{pmatrix},  
]

[  
K_1=  
\begin{pmatrix}  
0&\sqrt{\gamma}\  
0&0  
\end{pmatrix}.  
]

检查保迹条件。

首先：

# [  
K_0^\dagger K_0

\begin{pmatrix}  
1&0\  
0&1-\gamma  
\end{pmatrix}.  
]

其次：

# [  
K_1^\dagger K_1

\begin{pmatrix}  
0&0\  
0&\gamma  
\end{pmatrix}.  
]

相加：

# [  
K_0^\dagger K_0+K_1^\dagger K_1

# \begin{pmatrix}  
1&0\  
0&1-\gamma  
\end{pmatrix}  
+  
\begin{pmatrix}  
0&0\  
0&\gamma  
\end{pmatrix}

# \begin{pmatrix}  
1&0\  
0&1  
\end{pmatrix}

I.  
]

所以 amplitude damping channel 也是 trace preserving。

---

# 9. Trace non-increasing 的情况

有时候一个量子过程不是确定发生，而是带有 post-selection 的测量分支。

例如只保留某个测量结果，那么输出的迹就是这个结果发生的概率：

[  
\operatorname{Tr}\mathcal E(\rho)\leq \operatorname{Tr}\rho.  
]

这种映射叫 trace non-increasing。

Kraus 条件变成：

[  
\boxed{  
\sum_a K_a^\dagger K_a\leq I.  
}  
]

如果是严格等号：

[  
\sum_a K_a^\dagger K_a=I,  
]

就是 trace preserving。

如果是不等号：

[  
\sum_a K_a^\dagger K_a<I,  
]

就表示只取了某些测量分支，概率可能小于 (1)。

---

# 10. 不要混淆 trace preserving 和 unital

Trace preserving 条件是：

[  
\sum_a K_a^\dagger K_a=I.  
]

而 unital 条件是：

[  
\mathcal E(I)=I.  
]

用 Kraus 算符表示：

# [  
\mathcal E(I)=\sum_a K_aIK_a^\dagger

\sum_a K_aK_a^\dagger.  
]

所以 unital 条件是：

[  
\sum_a K_aK_a^\dagger=I.  
]

注意这和 trace preserving 不一样：

[  
\boxed{  
\text{trace preserving: }  
\sum_a K_a^\dagger K_a=I  
}  
]

[  
\boxed{  
\text{unital: }  
\sum_a K_aK_a^\dagger=I  
}  
]

对酉演化，两者都成立。但对一般噪声不一定都成立。

例如 amplitude damping 是 trace preserving，但不是 unital。

---

# 11. 总结

一个量子信道 (\mathcal E) 是 CPTP，表示它满足：

[  
\text{completely positive}  
]

和

[  
\text{trace preserving}.  
]

Kraus 表示为：

[  
\mathcal E(\rho)=\sum_a K_a\rho K_a^\dagger.  
]

其中 completely positive 由 Kraus 形式自动保证。

trace preserving 则要求：

[  
\boxed{  
\sum_a K_a^\dagger K_a=I.  
}  
]

所以最核心的一句话是：

[  
\boxed{  
\mathcal E(\rho)=\sum_a K_a\rho K_a^\dagger  
\text{ 是 CPTP }  
\Longleftrightarrow  
\sum_a K_a^\dagger K_a=I.  
}  
]

更准确地说，右边的 Kraus 形式保证 CP，而等式

[  
\sum_a K_a^\dagger K_a=I  
]

保证 TP。