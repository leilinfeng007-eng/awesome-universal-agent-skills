# 整理越来越复杂的 React 组件

**vercel-composition-patterns** · 优先了解 · 做网页与交互界面

[← 回到选 Skill](../README.md) · [全部客户端入口](../docs/clients.md)

## 适合我吗？

一个组件塞满布尔开关，调用和维护越来越难。

**适合：**React 组件维护者。

**为什么选它：**解决组件架构与可维护性，区别于性能规则；8 份具体规则、前后示例与编译指南全部在固定目录，可独立阅读。

**怎么选同类：**解决结构与复用；性能分析是另一项 React Best Practices。

**先知道：**用组合设计组件边界，不为简单组件强加架构。

## 开始前要有什么？

- 现有 React 项目；React 19 规则不适用于旧版本。

可以先准备单项文件；真正运行前仍须满足上面的工具条件。准备任务和客户端步骤均按文档编写，本轮没有执行安装。

## 1. 获取这一项

**[打开固定版本的单项文件夹](https://github.com/vercel-labs/agent-skills/tree/063bee94c3f4df8453406c830b0a7df0f2860278/skills/composition-patterns)** · [查看入口 SKILL.md](https://github.com/vercel-labs/agent-skills/blob/063bee94c3f4df8453406c830b0a7df0f2860278/skills/composition-patterns/SKILL.md) · [许可](https://github.com/vercel-labs/agent-skills/blob/063bee94c3f4df8453406c830b0a7df0f2860278/skills/composition-patterns/SKILL.md#L9)

源文件夹名称与 name 不同：目标目录必须使用 vercel-composition-patterns。保留 MIT 声明和来源，第三方引用权利另核。

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


把整个单项文件夹放到你打开的项目内 `.agents/skills/vercel-composition-patterns/`，入口必须是 `.agents/skills/vercel-composition-patterns/SKILL.md`。这是相对项目的路径，不是系统目录。

在 App 的 Skill 选择器中查找名称；CLI 可用 $vercel-composition-patterns。若版本界面不同，先要求 AI 读取实际入口路径。

App 按项目打开本文件夹，新会话再检查；具体界面未在本项实测。

[官方说明](https://learn.chatgpt.com/docs/build-skills)

**可复制的准备任务：**

```text

请只为当前项目准备 vercel-composition-patterns，先不要执行它。
固定来源：https://github.com/vercel-labs/agent-skills/tree/063bee94c3f4df8453406c830b0a7df0f2860278/skills/composition-patterns
入口：https://github.com/vercel-labs/agent-skills/blob/063bee94c3f4df8453406c830b0a7df0f2860278/skills/composition-patterns/SKILL.md
保留许可：https://github.com/vercel-labs/agent-skills/blob/063bee94c3f4df8453406c830b0a7df0f2860278/skills/composition-patterns/SKILL.md#L9
目标：.agents/skills/vercel-composition-patterns/
先确认当前项目路径正确，且目标目录尚不存在；已有同名项时停止，不覆盖、不合并。只获取此固定提交的目标子目录及其必要相对资源，不下载整个合集，不沿外链获取浮动 main/latest，不执行任何脚本或安装依赖。同时保留适用 LICENSE/NOTICE 与来源记录；资源或许可范围无法确定就停止并报告。不要修改登录、代理、全局配置或其他 Skill。完成后列出实际文件和未满足的条件。如果无法可靠下载完整子目录，请报告，不用猜测内容补齐。

```

</details>

<details>
<summary>OpenCode · 项目目录</summary>


把整个单项文件夹放到你打开的项目内 `.agents/skills/vercel-composition-patterns/`，入口必须是 `.agents/skills/vercel-composition-patterns/SKILL.md`。这是相对项目的路径，不是系统目录。

要求模型通过原生 skill 工具加载 vercel-composition-patterns，再给任务正文；不是终端命令或统一 /vercel-composition-patterns。

也支持 .opencode/skills；本指南只选一个入口，避免重复发现。

[官方说明](https://opencode.ai/docs/skills/)

**可复制的准备任务：**

```text

请只为当前项目准备 vercel-composition-patterns，先不要执行它。
固定来源：https://github.com/vercel-labs/agent-skills/tree/063bee94c3f4df8453406c830b0a7df0f2860278/skills/composition-patterns
入口：https://github.com/vercel-labs/agent-skills/blob/063bee94c3f4df8453406c830b0a7df0f2860278/skills/composition-patterns/SKILL.md
保留许可：https://github.com/vercel-labs/agent-skills/blob/063bee94c3f4df8453406c830b0a7df0f2860278/skills/composition-patterns/SKILL.md#L9
目标：.agents/skills/vercel-composition-patterns/
先确认当前项目路径正确，且目标目录尚不存在；已有同名项时停止，不覆盖、不合并。只获取此固定提交的目标子目录及其必要相对资源，不下载整个合集，不沿外链获取浮动 main/latest，不执行任何脚本或安装依赖。同时保留适用 LICENSE/NOTICE 与来源记录；资源或许可范围无法确定就停止并报告。不要修改登录、代理、全局配置或其他 Skill。完成后列出实际文件和未满足的条件。如果无法可靠下载完整子目录，请报告，不用猜测内容补齐。

```

</details>

<details>
<summary>Claude Code · 项目目录</summary>


把整个单项文件夹放到你打开的项目内 `.claude/skills/vercel-composition-patterns/`，入口必须是 `.claude/skills/vercel-composition-patterns/SKILL.md`。这是相对项目的路径，不是系统目录。

在项目会话输入 /vercel-composition-patterns，再给任务正文。

组织策略、工具权限仍可能限制读取或执行。

[官方说明](https://code.claude.com/docs/en/skills)

**可复制的准备任务：**

```text

请只为当前项目准备 vercel-composition-patterns，先不要执行它。
固定来源：https://github.com/vercel-labs/agent-skills/tree/063bee94c3f4df8453406c830b0a7df0f2860278/skills/composition-patterns
入口：https://github.com/vercel-labs/agent-skills/blob/063bee94c3f4df8453406c830b0a7df0f2860278/skills/composition-patterns/SKILL.md
保留许可：https://github.com/vercel-labs/agent-skills/blob/063bee94c3f4df8453406c830b0a7df0f2860278/skills/composition-patterns/SKILL.md#L9
目标：.claude/skills/vercel-composition-patterns/
先确认当前项目路径正确，且目标目录尚不存在；已有同名项时停止，不覆盖、不合并。只获取此固定提交的目标子目录及其必要相对资源，不下载整个合集，不沿外链获取浮动 main/latest，不执行任何脚本或安装依赖。同时保留适用 LICENSE/NOTICE 与来源记录；资源或许可范围无法确定就停止并报告。不要修改登录、代理、全局配置或其他 Skill。完成后列出实际文件和未满足的条件。如果无法可靠下载完整子目录，请报告，不用猜测内容补齐。

```

</details>

<details>
<summary>Cursor · 项目目录</summary>


把整个单项文件夹放到你打开的项目内 `.agents/skills/vercel-composition-patterns/`，入口必须是 `.agents/skills/vercel-composition-patterns/SKILL.md`。这是相对项目的路径，不是系统目录。

在 Agent 中输入 /，查找并选择 vercel-composition-patterns，再给任务。

本地 Agent 与云端运行可用资源不同；不要据目录支持推断脚本可执行。

[官方说明](https://cursor.com/docs/skills)

**可复制的准备任务：**

```text

请只为当前项目准备 vercel-composition-patterns，先不要执行它。
固定来源：https://github.com/vercel-labs/agent-skills/tree/063bee94c3f4df8453406c830b0a7df0f2860278/skills/composition-patterns
入口：https://github.com/vercel-labs/agent-skills/blob/063bee94c3f4df8453406c830b0a7df0f2860278/skills/composition-patterns/SKILL.md
保留许可：https://github.com/vercel-labs/agent-skills/blob/063bee94c3f4df8453406c830b0a7df0f2860278/skills/composition-patterns/SKILL.md#L9
目标：.agents/skills/vercel-composition-patterns/
先确认当前项目路径正确，且目标目录尚不存在；已有同名项时停止，不覆盖、不合并。只获取此固定提交的目标子目录及其必要相对资源，不下载整个合集，不沿外链获取浮动 main/latest，不执行任何脚本或安装依赖。同时保留适用 LICENSE/NOTICE 与来源记录；资源或许可范围无法确定就停止并报告。不要修改登录、代理、全局配置或其他 Skill。完成后列出实际文件和未满足的条件。如果无法可靠下载完整子目录，请报告，不用猜测内容补齐。

```

</details>

<details>
<summary>Kimi Code · 项目目录</summary>


把整个单项文件夹放到你打开的项目内 `.agents/skills/vercel-composition-patterns/`，入口必须是 `.agents/skills/vercel-composition-patterns/SKILL.md`。这是相对项目的路径，不是系统目录。

在新会话输入 /skill:vercel-composition-patterns，再给任务正文。

面向 Kimi Code CLI/Desktop，不是 Kimi 网页聊天；项目按最近 .git 定位，请先选准项目。

[官方说明](https://www.kimi.com/code/docs/kimi-code-cli/customization/skills.html)

**可复制的准备任务：**

```text

请只为当前项目准备 vercel-composition-patterns，先不要执行它。
固定来源：https://github.com/vercel-labs/agent-skills/tree/063bee94c3f4df8453406c830b0a7df0f2860278/skills/composition-patterns
入口：https://github.com/vercel-labs/agent-skills/blob/063bee94c3f4df8453406c830b0a7df0f2860278/skills/composition-patterns/SKILL.md
保留许可：https://github.com/vercel-labs/agent-skills/blob/063bee94c3f4df8453406c830b0a7df0f2860278/skills/composition-patterns/SKILL.md#L9
目标：.agents/skills/vercel-composition-patterns/
先确认当前项目路径正确，且目标目录尚不存在；已有同名项时停止，不覆盖、不合并。只获取此固定提交的目标子目录及其必要相对资源，不下载整个合集，不沿外链获取浮动 main/latest，不执行任何脚本或安装依赖。同时保留适用 LICENSE/NOTICE 与来源记录；资源或许可范围无法确定就停止并报告。不要修改登录、代理、全局配置或其他 Skill。完成后列出实际文件和未满足的条件。如果无法可靠下载完整子目录，请报告，不用猜测内容补齐。

```

</details>

<details>
<summary>Qoder IDE / CLI · 项目目录</summary>


把整个单项文件夹放到你打开的项目内 `.qoder/skills/vercel-composition-patterns/`，入口必须是 `.qoder/skills/vercel-composition-patterns/SKILL.md`。这是相对项目的路径，不是系统目录。

IDE 重启后输入 / 查找 vercel-composition-patterns；CLI 可 /skills reload 后用 /vercel-composition-patterns。

IDE 与 CLI 的同名优先级文档不同；只保留一个同名入口。CLI 文档：https://docs.qoder.com/cli/Skills

[官方说明](https://docs.qoder.com/extensions/skills)

**可复制的准备任务：**

```text

请只为当前项目准备 vercel-composition-patterns，先不要执行它。
固定来源：https://github.com/vercel-labs/agent-skills/tree/063bee94c3f4df8453406c830b0a7df0f2860278/skills/composition-patterns
入口：https://github.com/vercel-labs/agent-skills/blob/063bee94c3f4df8453406c830b0a7df0f2860278/skills/composition-patterns/SKILL.md
保留许可：https://github.com/vercel-labs/agent-skills/blob/063bee94c3f4df8453406c830b0a7df0f2860278/skills/composition-patterns/SKILL.md#L9
目标：.qoder/skills/vercel-composition-patterns/
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

请只为当前项目准备 vercel-composition-patterns，先不要执行它。
固定来源：https://github.com/vercel-labs/agent-skills/tree/063bee94c3f4df8453406c830b0a7df0f2860278/skills/composition-patterns
入口：https://github.com/vercel-labs/agent-skills/blob/063bee94c3f4df8453406c830b0a7df0f2860278/skills/composition-patterns/SKILL.md
保留许可：https://github.com/vercel-labs/agent-skills/blob/063bee94c3f4df8453406c830b0a7df0f2860278/skills/composition-patterns/SKILL.md#L9
目标：单独的新暂存文件夹/vercel-composition-patterns/
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

请只为当前项目准备 vercel-composition-patterns，先不要执行它。
固定来源：https://github.com/vercel-labs/agent-skills/tree/063bee94c3f4df8453406c830b0a7df0f2860278/skills/composition-patterns
入口：https://github.com/vercel-labs/agent-skills/blob/063bee94c3f4df8453406c830b0a7df0f2860278/skills/composition-patterns/SKILL.md
保留许可：https://github.com/vercel-labs/agent-skills/blob/063bee94c3f4df8453406c830b0a7df0f2860278/skills/composition-patterns/SKILL.md#L9
目标：单独的新暂存文件夹/vercel-composition-patterns/
先确认当前项目路径正确，且目标目录尚不存在；已有同名项时停止，不覆盖、不合并。只获取此固定提交的目标子目录及其必要相对资源，不下载整个合集，不沿外链获取浮动 main/latest，不执行任何脚本或安装依赖。同时保留适用 LICENSE/NOTICE 与来源记录；资源或许可范围无法确定就停止并报告。不要修改登录、代理、全局配置或其他 Skill。完成后列出实际文件和未满足的条件。如果无法可靠下载完整子目录，请报告，不用猜测内容补齐。

```

</details>

## 3. 复制任务，先试一个小样例

先完成上一节的加载，再发送下面的中文任务。示例本身不会自动安装或证明调用成功。

```text

开始前先确认你实际读取了 `composition-patterns/SKILL.md`，并核对项目 React 版本；不能读取规则或项目不是适用版本时停止说明。

请评估 `[组件文件/路径]`：它目前有这些开关/布尔属性 `[列出]`，调用位置 `[列出或由你只读搜索]`，希望改善的问题是 `[调用复杂/选项互斥/难扩展等]`。先只读检查组件实现、调用点和使用者可见 API，列出当前行为和兼容要求；不要凭空认定组件需要重构。

根据实际问题比较维持现状、组合式子组件、children/slot 或共享上下文等方案，解释取舍。不得为简单组件强加架构，不新增依赖。先给最小迁移计划与受影响调用点，等我确认后才修改。确认后保持现有用户行为，按项目版本使用其支持的模式（涉及 React 19 专属能力时明确指出）；检查所有重要属性组合并运行相关现有测试。报告改动范围、验证输出及未覆盖的组合。

```

运行前先让 AI 确认工具是否存在，只处理授权范围与副本；缺工具时先报缺项，不自动安装。

## 4. 怎么知道生效了？

1. 让 AI 说出实际读取的 SKILL.md 路径，并概括这次要执行的步骤。

2. 检查是否读到了需要的参考文件；仅回答“我会用”不能证明加载。

3. 检查重构前后组件行为与调用兼容；不要为采用模式改变原需求。

## 没生效 / 想撤销

先查项目是否打开正确、入口是否为 `技能名/SKILL.md`、是否有同名冲突，然后新建会话重新检查。缺工具不等于 Skill 没加载；看到名字也不等于任务成功。

项目目录方式：只把**本次新加的单项文件夹**移到项目外留作备份，再新建会话。导入方式：只禁用本次导入项并新建任务；删除行为先看客户端确认提示。不要清空整个 skills、缓存或配置目录。

<details>

<summary>来源、固定版本、许可与已知限制</summary>



- 原作者/维护方：vercel-labs 原始维护仓库；[vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills/tree/063bee94c3f4df8453406c830b0a7df0f2860278/skills/composition-patterns)。

- 固定版本：`063bee94c3f4df8453406c830b0a7df0f2860278`；Skill metadata 1.0.0；完整 Commit 固定实际规则。。

- 许可：[MIT](https://github.com/vercel-labs/agent-skills/blob/063bee94c3f4df8453406c830b0a7df0f2860278/skills/composition-patterns/SKILL.md#L9)。SKILL 本体明示 MIT，根 README 为仓库级 MIT 声明；未见两目录的冲突许可标记，但不推定第三方片段或外链内容获相同授权。未随附完整许可正文。

- 依赖许可：第三方依赖/资产/服务单独许可。未完成完整传递依赖或所有使用合同的许可审计；原始材料不复制入本项目。

- 运行依据：当前建议依据静态材料。上游示例、测试源码或限定构建记录不等于本项本地运行通过；本项未做客户端端到端测试。

- 原证据：E1：固定资源与名称/引用检查；E2-upstream_usage_example：前后对照代码可核对；没有测得性能提升或组件回归通过记录。E3/E4 未执行。

- [历史固定版本详细记录](../archive/v1.2/docs/skills.md#vercel-labs--composition-patterns)。



**已知限制（不是要求你执行的步骤）：**



- 源目录 composition-patterns 与 name=vercel-composition-patterns 不一致；需在目标客户端适配落地名称，未实测。

- 14 个目录文件、8 份 SKILL 所列具体规则均存在，未发现相对文件链接缺失；不是组件运行正确的测试结果。

- React 19 特定规则不适用于 React 18 或更早版本；不要把组合模式当自动性能提升。



**采用前提：**仅导航与原创评述；Skill frontmatter 明示 MIT，根 README 同样声明 MIT，固定目录未随附完整许可正文。不据此断言未授权第三方片段/外链内容都是 MIT，也不宣称取得逐文件权利确认。若未来获取，固定整个目标目录及必要 rules/AGENTS/metadata，按 name 值设置客户端落地目录、保留上游来源与许可声明；分发/改编前核对覆盖范围和必要版权/许可通知。无需运行贡献者构建流程。



</details>
