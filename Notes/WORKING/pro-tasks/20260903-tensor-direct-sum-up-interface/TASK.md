---
task_id: 20260903-tensor-direct-sum-up-interface
route: pro-write-review
status: DONE
target_files:
  - Notes/07-Lifted-Product Code/张量积与直和泛性质的 HGP-Künneth 接口.md
integration_files:
  - Notes/00-index.md
  - CANONICAL_KNOWLEDGE.md

integrity: fast
review_policy: fresh
audit_retention: errors-only

format_handling:
  policy: codex-contextual
  auto_repair: true
  rule_based_fixer: false
  allow_markdown_and_delimiter_repair: true
  allow_unambiguous_latex_syntax_repair: true
  escalate_only_when_meaning_is_ambiguous: true

git:
  remote: main
  branch: codex/tensor-direct-sum-up-interface-20260903
  base_commit: b52ede176daea174f956411f474b2966f7256dea

automation:
  run_to_completion: true
  standing_authorization: true
  auto_commit: true
  auto_push: true
  merge_to_main: false
  max_author_rounds: 2
  max_review_rounds: 1
  preauthorized_browser_rounds:
    - R01
    - R02
  stop_only_on:
    - permission_required
    - account_mismatch
    - needs_context
    - decision_required
    - blocked
    - source_conflict
    - structural_file_change
    - path_outside_allowlist
    - ambiguous_format_or_latex_repair
    - math_content_uncertain
    - format_check_failed_after_codex_repair
    - push_failure
    - merge_to_main
---

# 用户目标

把用户给出的“张量积泛性质与直和泛性质”长篇素材整理成一份连贯、可继续使用的中文笔记，放在 `Notes/07-Lifted-Product Code/`。正文既要建立两种泛性质的数学含义，也要让读者看见它们怎样进入 HGP 的分量组织和 Künneth 比较映射。

# Ownership 冲突与本任务处理

仓库现有 `[[Tensor product 对 direct sum 的分配律]]` 已是普通域上 tensor product 与 direct sum 的 canonical owner，并且已经用两种泛性质证明分配律。若新建一篇不加边界的泛称笔记，会形成第二个 owner。

用户已明确指定新笔记位于 `Notes/07-Lifted-Product Code/`。本任务据此把新稿限定为 HGP–Künneth 的应用接口：允许为自足理解重述两条泛性质和必要构造，但不接管一般定义、分配律、tensor-product complex、完整 Künneth 或 balanced tensor 的既有 ownership，也不重复这些笔记的完整证明。新文只拥有“验证规则—tensor 线性化—direct-sum 拼接”在 HGP/Künneth 中的应用接口。

# 本次授权

- 由 ChatGPT Pro 新写唯一目标文件的完整正文；
- 可以重新组织用户素材，删除超出主线的支线，补足定义、映射方向、良定义性与必要例子；
- 可以在正文中链接现有 canonical notes，并用最短充分桥梁连接 HGP、Künneth 与 LP；
- Codex按上下文处理纯 Obsidian / Markdown / 唯一确定的 LaTeX 格式问题；
- 完成 R01 后由全新 Pro 会话运行 R02 全文审查；
- R02 通过并核对预定集成文字后，Codex只做两处机械插入，不再自行决定措辞或位置；
- 在本任务分支自动 commit/push。

# 预定机械集成文字

在 `Notes/00-index.md` 第 7 节紧接 `[[Hypergraph product code]]` 条目后插入下列完整一行。代码块内保留三个前导空格，使它仍是编号 7 的子项：

```md
   - [[张量积与直和泛性质的 HGP-Künneth 接口]]（可选应用桥梁）：说明如何先验证双线性规则、用张量积泛性质线性化，再用直和泛性质拼接 total-degree 分量；一般分配律仍见 [[Tensor product 对 direct sum 的分配律]]。
```

在 `CANONICAL_KNOWLEDGE.md` 的 `## Tensor product 与 direct sum` 中紧接“主笔记”条目后插入下列完整一行：

```md
- 应用接口：[[张量积与直和泛性质的 HGP-Künneth 接口]]，路径 `Notes/07-Lifted-Product Code/张量积与直和泛性质的 HGP-Künneth 接口.md`；它只整理“验证双线性规则—张量积线性化—直和拼接”在 HGP/Künneth 中的用法，不接管本条目的一般泛性质与分配律 ownership。
```

# 本次不处理

- 不修改 `[[Tensor product 对 direct sum 的分配律]]`、`[[Cochain complex 的 tensor product]]`、`[[Künneth 分解]]`、HGP、LP 或 balanced tensor 正文；
- 不对 `CANONICAL_KNOWLEDGE.md` 或 `Notes/00-index.md` 作上述两条最小链接维护之外的改写；一般泛性质与分配律的 canonical owner 保持不变；
- 不删除、移动、拆分、合并或重命名正式文件；
- 不修改 Papers、Translations 或其它任务产物；
- 不合并主分支。

# 当前阶段

`DONE`：R01 完整正文与全新 Pro 会话的 R02 全文审查均已完成、解析、检查、应用并推送。R02 的两份不合规中间响应按 `errors-only` 保留，同一 R02 最终稿已压缩 quotient-tensor 支线、补足 balanced chain 条件与一般环左右模侧别；两处预定索引/canonical 链接已机械集成。目标笔记与索引的 Obsidian 数学检查、全部任务 diff 检查均通过；canonical 全文件 checker 仅重现未改旧行的已知括号理想警告。任务分支保留，未合并 `main`。
