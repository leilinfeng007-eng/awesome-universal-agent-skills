# 给 AI 做一个能用的工具接口

**mcp-builder** · 专项选择 · 创建 Agent 与工具接口

[← 回到选 Skill](../README.md) · [全部客户端入口](../docs/clients.md)

## 适合我吗？

已有 API，想通过 MCP 让 AI 有边界地使用它。

**适合：**接口开发者。

**为什么选它：**官方指南覆盖工具设计、结构化返回和评估；可按真实集成需求独立选用。

**怎么选同类：**先定 Agent 边界看 Agent Architecture，再按本项实现工具。

**先知道：**先设计输入、错误处理与评估，再实现；不默认部署。

## 开始前要有什么？

- 选定 MCP SDK、目标 API 与授权；不是现成连接器。

可以先准备单项文件；真正运行前仍须满足上面的工具条件。准备任务和客户端步骤均按文档编写，本轮没有执行安装。

## 1. 获取这一项

**[打开固定版本的单项文件夹](https://github.com/anthropics/skills/tree/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/mcp-builder)** · [查看入口 SKILL.md](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/mcp-builder/SKILL.md) · [许可](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/mcp-builder/LICENSE.txt)

不要下载整个 Anthropic 合集（包含其他受限材料）。只获取本项和本项许可。

不熟悉 Git？可以把下面的准备任务交给有网络和文件能力的 AI。它只是可复制的准备说明，不是已实测的一键安装器。先打开你的测试项目，再展开所用客户端，直接复制准备任务；同页往下就是调用示例。

<details>

<summary>macOS / Windows 放文件时怎么操作</summary>



macOS：在 Finder 打开你的项目，按 `Command + Shift + .` 显示隐藏文件；建立下方的 `.agents` 等目录。Windows：资源管理器打开项目，开启“查看 → 显示 → 文件扩展名”，按下方层级建文件夹。

如果系统询问合并/替换，选择取消。不要出现 `技能名/技能名/SKILL.md` 的双层目录。先用临时项目与虚构文件，不搬动你已有的 Skill。



</details>

## 2. 选你的 AI 工具，然后加载

**官方机制已核对，本项未逐客户端实测。** 支持目录不代表工具、权限或脚本已经就绪。下面每个入口包含独立路径，不要同时复制到多个地方。

<details>
<summary>Codex App / CLI · 项目目录</summary>


把整个单项文件夹放到你打开的项目内 `.agents/skills/mcp-builder/`，入口必须是 `.agents/skills/mcp-builder/SKILL.md`。这是相对项目的路径，不是系统目录。

在 App 的 Skill 选择器中查找名称；CLI 可用 $mcp-builder。若版本界面不同，先要求 AI 读取实际入口路径。

App 按项目打开本文件夹，新会话再检查；具体界面未在本项实测。

[官方说明](https://learn.chatgpt.com/docs/build-skills)

**可复制的准备任务：**

```text

请只为当前项目准备 mcp-builder，先不要执行它。
固定来源：https://github.com/anthropics/skills/tree/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/mcp-builder
入口：https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/mcp-builder/SKILL.md
保留许可：https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/mcp-builder/LICENSE.txt
目标：.agents/skills/mcp-builder/
先确认当前项目路径正确，且目标目录尚不存在；已有同名项时停止，不覆盖、不合并。只获取此固定提交的目标子目录及其必要相对资源，不下载整个合集，不沿外链获取浮动 main/latest，不执行任何脚本或安装依赖。同时保留适用 LICENSE/NOTICE 与来源记录；资源或许可范围无法确定就停止并报告。不要修改登录、代理、全局配置或其他 Skill。完成后列出实际文件和未满足的条件。如果无法可靠下载完整子目录，请报告，不用猜测内容补齐。

```

</details>

<details>
<summary>OpenCode · 项目目录</summary>


把整个单项文件夹放到你打开的项目内 `.agents/skills/mcp-builder/`，入口必须是 `.agents/skills/mcp-builder/SKILL.md`。这是相对项目的路径，不是系统目录。

要求模型通过原生 skill 工具加载 mcp-builder，再给任务正文；不是终端命令或统一 /mcp-builder。

也支持 .opencode/skills；本指南只选一个入口，避免重复发现。

[官方说明](https://opencode.ai/docs/skills/)

**可复制的准备任务：**

```text

请只为当前项目准备 mcp-builder，先不要执行它。
固定来源：https://github.com/anthropics/skills/tree/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/mcp-builder
入口：https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/mcp-builder/SKILL.md
保留许可：https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/mcp-builder/LICENSE.txt
目标：.agents/skills/mcp-builder/
先确认当前项目路径正确，且目标目录尚不存在；已有同名项时停止，不覆盖、不合并。只获取此固定提交的目标子目录及其必要相对资源，不下载整个合集，不沿外链获取浮动 main/latest，不执行任何脚本或安装依赖。同时保留适用 LICENSE/NOTICE 与来源记录；资源或许可范围无法确定就停止并报告。不要修改登录、代理、全局配置或其他 Skill。完成后列出实际文件和未满足的条件。如果无法可靠下载完整子目录，请报告，不用猜测内容补齐。

```

</details>

<details>
<summary>Claude Code · 项目目录</summary>


把整个单项文件夹放到你打开的项目内 `.claude/skills/mcp-builder/`，入口必须是 `.claude/skills/mcp-builder/SKILL.md`。这是相对项目的路径，不是系统目录。

在项目会话输入 /mcp-builder，再给任务正文。

组织策略、工具权限仍可能限制读取或执行。

[官方说明](https://code.claude.com/docs/en/skills)

**可复制的准备任务：**

```text

请只为当前项目准备 mcp-builder，先不要执行它。
固定来源：https://github.com/anthropics/skills/tree/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/mcp-builder
入口：https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/mcp-builder/SKILL.md
保留许可：https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/mcp-builder/LICENSE.txt
目标：.claude/skills/mcp-builder/
先确认当前项目路径正确，且目标目录尚不存在；已有同名项时停止，不覆盖、不合并。只获取此固定提交的目标子目录及其必要相对资源，不下载整个合集，不沿外链获取浮动 main/latest，不执行任何脚本或安装依赖。同时保留适用 LICENSE/NOTICE 与来源记录；资源或许可范围无法确定就停止并报告。不要修改登录、代理、全局配置或其他 Skill。完成后列出实际文件和未满足的条件。如果无法可靠下载完整子目录，请报告，不用猜测内容补齐。

```

</details>

<details>
<summary>Cursor · 项目目录</summary>


把整个单项文件夹放到你打开的项目内 `.agents/skills/mcp-builder/`，入口必须是 `.agents/skills/mcp-builder/SKILL.md`。这是相对项目的路径，不是系统目录。

在 Agent 中输入 /，查找并选择 mcp-builder，再给任务。

本地 Agent 与云端运行可用资源不同；不要据目录支持推断脚本可执行。

[官方说明](https://cursor.com/docs/skills)

**可复制的准备任务：**

```text

请只为当前项目准备 mcp-builder，先不要执行它。
固定来源：https://github.com/anthropics/skills/tree/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/mcp-builder
入口：https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/mcp-builder/SKILL.md
保留许可：https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/mcp-builder/LICENSE.txt
目标：.agents/skills/mcp-builder/
先确认当前项目路径正确，且目标目录尚不存在；已有同名项时停止，不覆盖、不合并。只获取此固定提交的目标子目录及其必要相对资源，不下载整个合集，不沿外链获取浮动 main/latest，不执行任何脚本或安装依赖。同时保留适用 LICENSE/NOTICE 与来源记录；资源或许可范围无法确定就停止并报告。不要修改登录、代理、全局配置或其他 Skill。完成后列出实际文件和未满足的条件。如果无法可靠下载完整子目录，请报告，不用猜测内容补齐。

```

</details>

<details>
<summary>Kimi Code · 项目目录</summary>


把整个单项文件夹放到你打开的项目内 `.agents/skills/mcp-builder/`，入口必须是 `.agents/skills/mcp-builder/SKILL.md`。这是相对项目的路径，不是系统目录。

在新会话输入 /skill:mcp-builder，再给任务正文。

面向 Kimi Code CLI/Desktop，不是 Kimi 网页聊天；项目按最近 .git 定位，请先选准项目。

[官方说明](https://www.kimi.com/code/docs/kimi-code-cli/customization/skills.html)

**可复制的准备任务：**

```text

请只为当前项目准备 mcp-builder，先不要执行它。
固定来源：https://github.com/anthropics/skills/tree/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/mcp-builder
入口：https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/mcp-builder/SKILL.md
保留许可：https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/mcp-builder/LICENSE.txt
目标：.agents/skills/mcp-builder/
先确认当前项目路径正确，且目标目录尚不存在；已有同名项时停止，不覆盖、不合并。只获取此固定提交的目标子目录及其必要相对资源，不下载整个合集，不沿外链获取浮动 main/latest，不执行任何脚本或安装依赖。同时保留适用 LICENSE/NOTICE 与来源记录；资源或许可范围无法确定就停止并报告。不要修改登录、代理、全局配置或其他 Skill。完成后列出实际文件和未满足的条件。如果无法可靠下载完整子目录，请报告，不用猜测内容补齐。

```

</details>

<details>
<summary>Qoder IDE / CLI · 项目目录</summary>


把整个单项文件夹放到你打开的项目内 `.qoder/skills/mcp-builder/`，入口必须是 `.qoder/skills/mcp-builder/SKILL.md`。这是相对项目的路径，不是系统目录。

IDE 重启后输入 / 查找 mcp-builder；CLI 可 /skills reload 后用 /mcp-builder。

IDE 与 CLI 的同名优先级文档不同；只保留一个同名入口。CLI 文档：https://docs.qoder.com/cli/Skills

[官方说明](https://docs.qoder.com/extensions/skills)

**可复制的准备任务：**

```text

请只为当前项目准备 mcp-builder，先不要执行它。
固定来源：https://github.com/anthropics/skills/tree/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/mcp-builder
入口：https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/mcp-builder/SKILL.md
保留许可：https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/mcp-builder/LICENSE.txt
目标：.qoder/skills/mcp-builder/
先确认当前项目路径正确，且目标目录尚不存在；已有同名项时停止，不覆盖、不合并。只获取此固定提交的目标子目录及其必要相对资源，不下载整个合集，不沿外链获取浮动 main/latest，不执行任何脚本或安装依赖。同时保留适用 LICENSE/NOTICE 与来源记录；资源或许可范围无法确定就停止并报告。不要修改登录、代理、全局配置或其他 Skill。完成后列出实际文件和未满足的条件。如果无法可靠下载完整子目录，请报告，不用猜测内容补齐。

```

</details>

<details>
<summary>QoderWork · 需界面导入，待验证</summary>


在 Extensions → Skills → Install Skills 中上传单项与辅助资源，随后通过 / 或明确名称选择。

独立导入入口；固定版本、同名处理及导入后文件是否改写仍待实测。不要改写全局配置。 先把固定单项和许可放入暂存目录，在界面确认格式和资源都被保留；没有确认前不导入，也不要上传整仓库 ZIP。导入会改变客户端持久状态，由你决定是否继续。

[官方说明](https://docs.qoder.com/zh/qoderwork/skills)

**可复制的准备任务：**

```text

请只为当前项目准备 mcp-builder，先不要执行它。
固定来源：https://github.com/anthropics/skills/tree/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/mcp-builder
入口：https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/mcp-builder/SKILL.md
保留许可：https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/mcp-builder/LICENSE.txt
目标：单独的新暂存文件夹/mcp-builder/
先确认当前项目路径正确，且目标目录尚不存在；已有同名项时停止，不覆盖、不合并。只获取此固定提交的目标子目录及其必要相对资源，不下载整个合集，不沿外链获取浮动 main/latest，不执行任何脚本或安装依赖。同时保留适用 LICENSE/NOTICE 与来源记录；资源或许可范围无法确定就停止并报告。不要修改登录、代理、全局配置或其他 Skill。完成后列出实际文件和未满足的条件。如果无法可靠下载完整子目录，请报告，不用猜测内容补齐。

```

</details>

<details>
<summary>WorkBuddy · 需界面导入，待验证</summary>


专家·技能·连接器 → 技能 → 添加技能 → 上传技能；新任务中明确指名。

只确认本地技能包导入机制，包层级和资源保留未确认。先在界面核对要求；不保证任意 ZIP 可导入，不使用 CodeBuddy 路径。 先把固定单项和许可放入暂存目录，在界面确认格式和资源都被保留；没有确认前不导入，也不要上传整仓库 ZIP。导入会改变客户端持久状态，由你决定是否继续。

[官方说明](https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market)

**可复制的准备任务：**

```text

请只为当前项目准备 mcp-builder，先不要执行它。
固定来源：https://github.com/anthropics/skills/tree/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/mcp-builder
入口：https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/mcp-builder/SKILL.md
保留许可：https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/mcp-builder/LICENSE.txt
目标：单独的新暂存文件夹/mcp-builder/
先确认当前项目路径正确，且目标目录尚不存在；已有同名项时停止，不覆盖、不合并。只获取此固定提交的目标子目录及其必要相对资源，不下载整个合集，不沿外链获取浮动 main/latest，不执行任何脚本或安装依赖。同时保留适用 LICENSE/NOTICE 与来源记录；资源或许可范围无法确定就停止并报告。不要修改登录、代理、全局配置或其他 Skill。完成后列出实际文件和未满足的条件。如果无法可靠下载完整子目录，请报告，不用猜测内容补齐。

```

</details>

## 3. 复制任务，先试一个小样例

先完成上一节的加载，再发送下面的中文任务。示例本身不会自动安装或证明调用成功。

```text

基于这个已授权 API 说明设计只读 MCP 工具契约，先给接口与错误处理方案。

```

运行前先让 AI 确认工具是否存在，只处理授权范围与副本；缺工具时先报缺项，不自动安装。

## 4. 怎么知道生效了？

1. 让 AI 说出实际读取的 SKILL.md 路径，并概括这次要执行的步骤。

2. 检查是否读到了需要的参考文件；仅回答“我会用”不能证明加载。

3. 用一份可丢弃的小样例核对输出内容；查看日志中真实执行的步骤和未验证范围。

## 没生效 / 想撤销

先查项目是否打开正确、入口是否为 `技能名/SKILL.md`、是否有同名冲突，然后新建会话重新检查。缺工具不等于 Skill 没加载；看到名字也不等于任务成功。

项目目录方式：只把**本次新加的单项文件夹**移到项目外留作备份，再新建会话。导入方式：只禁用本次导入项并新建任务；删除行为先看客户端确认提示。不要清空整个 skills、缓存或配置目录。

<details>

<summary>来源、固定版本、许可与已知限制</summary>



- 原作者/维护方：Anthropic；[anthropics/skills](https://github.com/anthropics/skills/tree/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/mcp-builder)。

- 固定版本：`dbd4588f9e1033efb41dad4bef2f7947c8993d44`；无单项稳定发行版核实；按Commit固定。

- 许可：[Apache-2.0](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/mcp-builder/LICENSE.txt)。仅指已审 Skill/仓库许可；依赖、资产及服务另行核对。

- 依赖许可：未完成所选分发版本全部传递依赖/资产的许可审计。

- 运行依据：当前建议依据静态材料。上游示例、测试源码或限定构建记录不等于本项本地运行通过；本项未做客户端端到端测试。

- 原证据：入口和目录许可证已审；完整评估资源、SDK 和服务运行未验证。

- [历史固定版本详细记录](../archive/v1.2/docs/skills.md#anthropics--mcp-builder)。



**已知限制（不是要求你执行的步骤）：**



- 它是开发指南，不是现成连接器、MCP 服务或通用 API 执行器。

- 指南中的 main、最新 SDK 和 Inspector 示例不是固定依赖锁。

- SDK、API 权限、资产及具体服务依赖需另核。



**采用前提：**固定所选 SDK/服务版本，独立核对许可与鉴权；不得把示例视为部署授权。



</details>
