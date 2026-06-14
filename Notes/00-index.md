这个库围绕 magic state、非 Clifford 资源、容错量子计算和资源估算展开。主线目标是理解为什么 Clifford 操作本身不够通用，magic state 如何提供非 Clifford 资源，以及这些资源在容错架构中如何被注入、蒸馏和消耗。

---
### 主线入口

- [[State injection]]：用魔态、Clifford 操作、测量和经典前馈，把非 Clifford 的 $T$ 门作用传送到数据比特上。

---
### 容错与稳定子前置

- [[二进制空间性质]]：整理 $\mathbb{F}_2^n$、线性子空间、商空间和正交补等记号，是 CSS 码和稳定子推导的线性代数基础。
- [[逻辑基态的表示]]：从只有 $X$ 型稳定子的简单情形、CSS 码，到一般稳定子码，推导逻辑计算基态的陪集态、投影算符和仿射子空间表示。
- [[逻辑基态的二次相位]]：说明稳定子态在计算基展开中为什么只能出现一次相位和 $CZ$ 型二次相位。

---
### 后续应补主题

- [[Clifford group]]
- [[Gottesman-Knill theorem]]
- [[T state]]
- [[Magic State Distillation]]
- [[T gate injection]]
- [[Surface-code factory]]
