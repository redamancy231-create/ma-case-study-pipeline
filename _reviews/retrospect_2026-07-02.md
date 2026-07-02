# Retrospect — 2026-07-02 GitHub 发布准备

## 发现

### 1. pre-push hook 覆盖盲区
pre-push hook 只扫描 `git diff` 变更文件，不会全量扫描仓库。Codex 异后端独立扫描发现了 3 处 hook 未拦截的绝对路径残留（位于从未被 git diff 覆盖的旧文件中）。**教训**：发布前须做一次异后端全量扫描，不能仅依赖 hook 的增量检查。

### 2. O7 规则验证
本次发布准备验证了 O7 规则（禁止自扫自夸零残留）的有效性——我用同一套 grep pattern 清理后声称"零残留"，但 Codex 用自己的 pattern 发现了 3 处遗漏。**确认**：O7 规则不仅适用于清理验证，也适用于发布前敏感信息检查。

### 3. 外部模型命令须带输出路径
连续两次给 Codex/Qwen 的命令未带 `> output.txt 2>&1`，导致事后从会话文件提取结果。已写入 memory `feedback_external_model_output_path`。

## 流程复盘

发布准备流程：清理→翻译→审查→修复→就绪，共 7 个检查项。耗时主要在审查环节（#1 异后端扫描 + #6 CLAUDE.md 双后端验证）。

## 未闭合项

- GitHub 正式发布（初始 commit + repo 创建 + docx Release）— ✅ 已完成（2026-07-02 第一会话）
- 发布后：其他三个仓库 README 加交叉链接（双向链接网络）— ✅ 已完成（2026-07-02 第二会话：framework/IRT/PTM 均已 commit+push）
- 发布后：项目复盘归档报告追记 GitHub 发布事实 — 仍待执行（P2，非阻塞）
