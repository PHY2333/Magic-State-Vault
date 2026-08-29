# Notes/MODEL_ROUTING.md

本文件把 Notes 角色绑定到实际模型，并规定跨模型提示词和 Git 自动化责任。

## 1. Task route

| route | 适用范围 | Pro gate |
|---|---|---|
| `sol-only` | 错字、链接、路径、frontmatter、纯格式、来源元数据、确定的机械替换 | 无 |
| `hybrid-local` | 一个或少数 conceptual units；用户指出术语、动机、视角、证明或解释问题 | Pro design/author + fresh Pro final review |
| `hybrid-whole-note` | 整篇重写、legacy note、超过两个 changes-required units、whole-note 职责或 optional 路线需重构 | Pro architecture + Pro authoring + Pro whole-note review |
| `hybrid-paper-guide` | 论文导读、source-specific/general 边界、论文记号与教材路线并存 | Pro architecture/author + Pro whole-note review |

只要任务改变读者怎样形成理解，就不能降为 `sol-only`。

## 2. 模型分工

| Role | Model | 主要责任 |
|---|---|---|
| Repository Mapper / Source Verifier | Codex Sol | 仓库、来源、公式、约定、ownership、coverage |
| Lead Didactic Architect | ChatGPT Pro | 整篇主线、unit 边界、模式、depth、optional route |
| Lead Author | ChatGPT Pro | 核心概念正文、复杂推导、关键过渡 |
| Mechanical Editor | Codex Sol | 精确表格、来源表、frontmatter、链接和无语义插槽 |
| Contract Auditor | Codex Sol | 数学、来源、版本、装配和 Obsidian 渲染 |
| Whole-Note Reviewer | 新的 ChatGPT Pro 会话 | 整篇读者体验、行文质量、能力连续性和全局比例 |
| Repository Integrator | Codex Sol | 按 preview 精确写入、commit、push |

## 3. Pro-required 条件

出现任一条件，至少使用 `hybrid-local`：

- 用户反馈“像百科”“视角错误”“知道定义但没有理解”“失去 target”；
- 新复杂对象的首次入口；
- 长证明、复杂推导或多个讲解模式之间的选择；
- whole-first 与 step-by-step 的取舍；
- explanation depth 或 optional placement 未确定；
- 一般理论与论文特例、硬件实现或来源记号混合；
- note type、entry mode、拆分或 ownership 需要判断；
- legacy coverage 出现两个以上 `changes-required`；
- 需要对整篇语言和能力阶梯作结论。

## 4. Reader-visible author mode

`PRO_DESIGN.md` 为每个 unit 指定：

- `pro_full`：Pro 写完整 unit；用于核心概念、复杂推导和曾导致卡点的部分。
- `pro_core_sol_mechanical`：Pro 写主线与过渡；Sol 只插入已验证公式、表格或记号 crosswalk。
- `sol_mechanical`：只用于由数据机械决定的 reader-visible 内容。
- `retain_exact`：保留 exact validated text；仍进入整篇终审。

Hybrid task 中不存在默认 `sol_conceptual`。

## 5. Handoff 责任

- Sol 完成阶段后：验证 → 数学格式检查 → commit → push → 输出精确 Pro prompt。
- Pro 完成阶段后：生成 artifact → 输出精确 `NEXT_SOL_PROMPT`。
- 用户只负责复制提示词，并在 Pro→Sol 时附上 artifact。
- Pro 提示词必须引用 Sol 刚推送的精确 commit。
- Pro artifact 必须记录它依据的 repository、branch、commit 和 request hash。

## 6. 不可替代性

- Sol 不得生成、伪造或自行批准 `PRO_DESIGN.md`、`PRO_DRAFTS/`、`PRO_FINAL_REVIEW.md`。
- Pro 不直接修改本地仓库，不自称 source-validated。
- Sol 保存 Pro 输出时不得改写 prose；若公式分隔符不合格，退回 Pro，不静默转换。
- Pro 暂时不可用时任务停在 `awaiting_pro_*`。

## 7. Git 权限

Git commit/push 只由 Sol执行。默认只推任务分支，不合并主分支。具体规则见 `git-automation.md`。
