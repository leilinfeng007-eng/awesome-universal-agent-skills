# 选择你使用的 AI 工具

[← 先选一个 Skill](../README.md#find)

**不必先读完这页。** 每张 Skill 卡片都包含该工具的项目路径、准备任务、调用方法和撤销说明。这页只帮助你判断客户端机制，不是安装成功记录。官方支持发现，不等于这一项的脚本、工具或权限已可用。

<a id="codex"></a>
## Codex App / CLI

在 App 打开你的测试项目。项目入口为 `.agents/skills/技能名/SKILL.md`，不是把整仓库添加到全局。准备好后新开会话，在 Skill 选择器查找名称；CLI 可用 `$技能名`。App 具体界面可能随版本变化，本轮未实际操作；找不到时先要求 AI 读取卡片写明的实际入口，不能假装菜单已经出现。

[官方机制](https://learn.chatgpt.com/docs/build-skills)

<a id="opencode"></a>
## OpenCode

项目支持 `.agents/skills/技能名/`，也有 `.opencode/skills/`。只选一个入口。在会话要求模型通过原生 `skill` 工具加载名称，再给任务正文；不要把 `skill({name: ...})` 当终端命令，也不要假定统一 `/技能名`。

[官方说明](https://opencode.ai/docs/skills/)

<a id="claude"></a>
## Claude Code

项目入口 `.claude/skills/技能名/`，会话输入 `/技能名`。加载后再给具体任务；组织策略和工具权限仍可能限制执行。只配置单项，不需要为阅读一个指南装整套插件。

[官方说明](https://code.claude.com/docs/en/skills)

<a id="cursor"></a>
## Cursor

项目可用 `.agents/skills/技能名/`（也支持 `.cursor/skills/`）。在 Agent 中输入 `/` 查找 Skill。不要同时重复放置；本地 Agent 与云端可用文件、工具和权限不一定相同。

[官方说明](https://cursor.com/docs/skills)

<a id="kimi"></a>
## Kimi Code

Kimi Code CLI/Desktop 可复用 `.agents/skills/技能名/`；新会话用 `/skill:技能名`。当前文档按最近的 `.git` 定位项目；先确认项目根，不为添加 Skill 随意改动已有 Git 配置。本说明不泛指 Kimi 网页聊天，也不沿用旧版 kimi-cli 的用户目录。

[CLI 官方说明](https://www.kimi.com/code/docs/kimi-code-cli/customization/skills.html) · [Desktop 扩展说明](https://www.kimi.com/code/docs/kimi-code-desktop/settings-and-extensions.html)

<a id="qoder"></a>
## Qoder IDE / CLI

使用项目 `.qoder/skills/技能名/`。IDE 重启后通过 `/` 查找；CLI 可 `/skills reload` 后 `/技能名`。IDE 与 CLI 对同名优先级的文档存在差异，因此本指南要求只保留一个同名入口，不靠优先级覆盖。

[IDE 官方说明](https://docs.qoder.com/extensions/skills) · [CLI 官方说明](https://docs.qoder.com/cli/Skills)

<a id="qoderwork"></a>
## QoderWork

这是独立入口，不套用 Qoder IDE 的目录。官方路径是 Extensions → Skills → Install Skills；上传单项及辅助文件后，通过 `/` 或明确名称选择。

导入会写入客户端持久状态。固定版本是否保留、同名处理、导入后是否改写文件均待实测；先核对界面，不承诺一键导入。撤销优先只禁用本次导入项，再新建任务。

[官方说明](https://docs.qoder.com/zh/qoderwork/skills)

<a id="workbuddy"></a>
## WorkBuddy

腾讯 WorkBuddy 官方路径：专家·技能·连接器 → 技能 → 添加技能 → 上传技能。添加并启用后，在新任务中指名 Skill。

只确认支持本地技能包，包层级与辅助文件保留仍待确认；不要把任意 ZIP 宣称可直接导入，不使用 CodeBuddy 的目录。界面不清楚时先停止；本库不要求你为验证改动配置。导入后只禁用本次项即可停止使用，删除前看确认提示。

[官方说明](https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market)

## 原则：共享一份，不强行共享所有

Codex、OpenCode、Cursor、Kimi Code 有共同的 `.agents/skills` 项目入口，可以先在一个测试项目保留一份单项核心。Claude Code、Qoder 使用各自明确的项目目录；可以选择受控副本，但不要同时放同名冲突项。QoderWork、WorkBuddy 走独立导入。符号链接在这些组合中的真实表现没有逐客户端验证，不作为新手默认步骤。

目录发现只是第一步。OfficeCLI、CodeQL 等需要额外工具；Trail of Bits 部分条目的 `{baseDir}`、可选子代理或 frontmatter 扩展需要适配；这些条件写在卡片里。不能把所有标签理解为“直接可运行”。

## 已有 GitHub CLI 的开发者：可选快捷路线

不是前置条件，不为本库升级或安装管理器。官方 `gh skill` 自 2.90.0 提供，仍属预览。若你现有版本的 `gh skill install --help` 确实列出以下参数，可在测试项目使用单项命令，例如：

```sh
gh skill install obra/superpowers skills/systematic-debugging --pin bb92a77741419a4ab5f06e711a283343f1ada0c3 --agent codex --scope project
```

参数仅按官方文档核对，本轮未执行。不要加 `--force`、`--all` 或更新命令。同名提示应拒绝覆盖。它会注入来源元数据，并写用户级 `~/.agents/.skill-lock.json`，所以不是只写项目或原样复制；它只取 Skill 子树，根 LICENSE/NOTICE 需要另保留。

[官方手册](https://cli.github.com/manual/gh_skill_install) · [预览发布说明](https://github.blog/changelog/2026-04-16-manage-agent-skills-with-github-cli/) · [安装实现](https://github.com/cli/cli/blob/trunk/internal/skills/installer/installer.go) · [锁记录实现](https://github.com/cli/cli/blob/trunk/internal/skills/lockfile/lockfile.go)

本页客户端机制定向核对日期：2026-10-21。没有安装、登录、启动或修复这些客户端，也没有获得新的 Skill 端到端运行证据。
