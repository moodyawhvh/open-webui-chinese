> 🌐 本文档由 [open-webui/open-webui](https://github.com/open-webui/open-webui) 翻译,英文原版见原项目。

<!--
贡献者必读检查项:
1. 请将 PR 目标分支设为 `dev` 分支。指向 `main` 的 PR 将被直接关闭。
2. 代码类 Pull Request 不是默认的贡献途径。
3. 不要一上来就提代码 PR。请先从一份写得清楚的 Issue 或 Discussion 开始,除非有维护者明确要求提交 PR,或者改动仅涉及 i18n/本地化。
4. 不要删除底部的贡献者许可协议(CLA)部分,CLA 机器人需要它。
-->

# Pull Request(拉取请求)

感谢你想要改进 Open WebUI。最有价值的贡献通常是一份清晰、表述完善的 Issue,而不是未经沟通的代码 Pull Request。

只有在维护者明确提出要求时,或者改动仅涉及 i18n/本地化时,才提交代码 Pull Request。对于真实、可复现的 Bug,请先提交一份描述完善的 [Issue](https://github.com/open-webui/open-webui/issues)。对于功能请求、UI/UX 改动、行为变更、架构调整、疑似修复方案或尚未验证的思路,请从活跃的 [Discussion](https://github.com/open-webui/open-webui/discussions) 开始。

在继续之前,请确保所关联的 Issue 或 Discussion 已说明面向用户的问题、预期结果、受影响的工作流程,以及维护者评估所需的全部示例、日志、截图、约束条件或复现细节。

如果你有实现思路,请将其作为参考补充到 Issue 或 Discussion 中。如果想分享代码作参考,请以本地 diff、补丁或分支说明的形式放在那里,不要为参考代码单独开 Pull Request。

未经沟通的 PR 可能不经过评审即被关闭,尤其是那些引入了未经讨论的产品、架构、兼容性、依赖或维护决策的 PR。

## 检查清单

- [ ] 本 PR 的目标分支是 `dev` 分支。
- [ ] 本 PR 关联了一份描述完善、已确认的 Issue 或活跃的 Discussion:`Closes #___` / `Relates to #___`。
- [ ] 有维护者明确要求我提交此 PR,或本 PR 仅更新 i18n/本地化内容。
- [ ] 本次改动是一个逻辑单元,不包含无关提交。
- [ ] 我遵循了周边代码的既有模式,避免引入不必要的新配置项、抽象或依赖。
- [ ] 我手动测试了改动的功能,以及可能受影响的周边行为。
- [ ] 我在必要时更新了相关文档,包括 [Open WebUI 文档仓库](https://github.com/open-webui/docs)。
- [ ] UI 改动已附上截图,涉及动画或交互时附上了录屏。
- [ ] 我在提交前审阅了所有 AI 生成的代码。
- [ ] PR 标题使用了下方列出的前缀之一。

## 标题前缀

请使用以下前缀之一:

- **BREAKING CHANGE**:影响向后兼容性的变更
- **build**:构建系统或依赖变更
- **ci**:CI/CD 工作流变更
- **chore**:重构、清理或非功能性变更
- **docs**:文档新增或更新
- **feat**:新功能或功能增强
- **fix**:Bug 修复或勘误
- **i18n**:国际化或本地化变更
- **perf**:性能优化
- **refactor**:代码重构

## 摘要

描述本次变更、它解决的问题,以及对用户的影响。

## 测试

列出你实际执行过的手动检查项。必要时附上命令、环境细节、截图或录屏。

## 变更日志条目

### 新增(Added)

-

### 变更(Changed)

-

### 修复(Fixed)

-

### 移除(Removed)

-

### 安全(Security)

-

### 破坏性变更(Breaking Changes)

-

## 补充说明

填写维护者在评审前需要了解的其他信息。

## 贡献者许可协议(CLA)

<!--
请勿删除本节。
在你勾选下方复选框、确认已阅读并同意 CLA 之前,PR 不会被评审或合并。
-->

- [ ] 提交此 Pull Request 即表示我确认已阅读并完全同意[贡献者许可协议(CLA)](https://github.com/open-webui/open-webui/blob/main/CONTRIBUTOR_LICENSE_AGREEMENT),并按照其条款提供我的贡献。
