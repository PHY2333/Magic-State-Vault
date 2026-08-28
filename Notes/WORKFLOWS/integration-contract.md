# Notes/WORKFLOWS/integration-contract.md

Repository Integrator 只在 `MANUSCRIPT_VERDICT: pass` 且 `INTEGRATION_PREVIEW: ready` 后写正式仓库。

## 1. 输入

通过的 drafts、ready preview、目标文件、NOTE_TYPES、LANGUAGE_PROFILE、index/canonical 与相关链接。

## 2. 权限

可以按 preview 替换／插入正文、删除旧竞争文本、补 frontmatter、在独立成立的句子后加自然链接、必要时最小更新 index/canonical 和修路径格式。

不得改变教学顺序、claims、explanation depth、optional placement 或数学主张。任何偏离 preview 都返回相应阶段。

## 3. 最终检查

- 正式文件无 WORKING 链接；
- note type/entry mode 一致；
- 旧新开头不并存；
- optional/upstream detail 与 owner 一致；
- links/anchors 有效；
- 中文术语一致；
- 无无关 diff；
- `git diff --check` 通过。

## 4. 输出

生成 `INTEGRATION_REPORT.md`，记录修改、replacement range、links、frontmatter、index/canonical、preview 一致性与未解决事项。
