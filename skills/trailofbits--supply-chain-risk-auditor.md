# 看看项目依赖有没有风险信号

**supply-chain-risk-auditor** · 专项选择 · 查代码与依赖风险

[← 回到选 Skill](../README.md) · [全部客户端入口](../docs/clients.md)

## 适合我吗？

想了解依赖的公告、维护状态和发布异常。

**适合：**公开项目维护者。

**为什么选它：**Python 标准库收集器区分 assessed/unassessable，按锁定版本核对公告，支持结果缓存。 补齐依赖供应链，与源码安全、凭据扫描及现有 CI 修复不同，不能互替。

**怎么选同类：**关注依赖生态，不等于源码安全或许可证合规结论。

**先知道：**会向公开服务查询包名与版本；私有依赖先确认是否可外发。

## 开始前要有什么？

- Python 3.11+、uv，可选 gh；需要外网查询。

可以先准备单项文件；真正运行前仍须满足上面的工具条件。准备任务和客户端步骤均按文档编写，本轮没有执行安装。

## 1. 获取这一项

**[打开固定版本的单项文件夹](https://github.com/trailofbits/skills/tree/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/plugins/supply-chain-risk-auditor/skills/supply-chain-risk-auditor)** · [查看入口 SKILL.md](https://github.com/trailofbits/skills/blob/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/plugins/supply-chain-risk-auditor/skills/supply-chain-risk-auditor/SKILL.md) · [许可](https://github.com/trailofbits/skills/blob/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/LICENSE)

复制整个单项文件夹，包含 references、scripts、assets 等实际存在的子目录；不要只取 SKILL.md。

不熟悉 Git？可以把下面的准备任务交给有网络和文件能力的 AI。它只是可复制的准备说明，不是已实测的一键安装器。先打开你的测试项目，再展开所用客户端，直接复制准备任务；同页往下就是调用示例。

**手工替代：**[下载该固定版本 ZIP](https://github.com/trailofbits/skills/archive/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0.zip)，解压后只取 `plugins/supply-chain-risk-auditor/skills/supply-chain-risk-auditor/`，放到下方目标目录。ZIP 是上游全仓库快照，不代表推荐安装合集；不执行其中的安装脚本。另保留[原许可](https://github.com/trailofbits/skills/blob/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/LICENSE)及适用 NOTICE，剩余合集不用放进 AI 工具。

<details>

<summary>macOS / Windows 放文件时怎么操作</summary>



macOS：在 Finder 打开你的项目，按 `Command + Shift + .` 显示隐藏文件；建立下方的 `.agents` 等目录。Windows：资源管理器打开项目，开启“查看 → 显示 → 文件扩展名”，按下方层级建文件夹。

如果系统询问合并/替换，选择取消。不要出现 `技能名/技能名/SKILL.md` 的双层目录。先用临时项目与虚构文件，不搬动你已有的 Skill。



</details>

## 2. 选你的 AI 工具，然后加载

**官方机制已核对，本项未逐客户端实测。** 支持目录不代表工具、权限或脚本已经就绪。下面每个入口包含独立路径，不要同时复制到多个地方。

<details>
<summary>Codex App / CLI · 项目目录</summary>


把整个单项文件夹放到你打开的项目内 `.agents/skills/supply-chain-risk-auditor/`，入口必须是 `.agents/skills/supply-chain-risk-auditor/SKILL.md`。这是相对项目的路径，不是系统目录。

在 App 的 Skill 选择器中查找名称；CLI 可用 $supply-chain-risk-auditor。若版本界面不同，先要求 AI 读取实际入口路径。

App 按项目打开本文件夹，新会话再检查；具体界面未在本项实测。

[官方说明](https://learn.chatgpt.com/docs/build-skills)

**可复制的准备任务：**

```text

请只为当前项目准备 supply-chain-risk-auditor，先不要执行它。
固定来源：https://github.com/trailofbits/skills/tree/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/plugins/supply-chain-risk-auditor/skills/supply-chain-risk-auditor
入口：https://github.com/trailofbits/skills/blob/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/plugins/supply-chain-risk-auditor/skills/supply-chain-risk-auditor/SKILL.md
保留许可：https://github.com/trailofbits/skills/blob/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/LICENSE
目标：.agents/skills/supply-chain-risk-auditor/
先确认当前项目路径正确，且目标目录尚不存在；已有同名项时停止，不覆盖、不合并。只获取此固定提交的目标子目录及其必要相对资源，不下载整个合集，不沿外链获取浮动 main/latest，不执行任何脚本或安装依赖。同时保留适用 LICENSE/NOTICE 与来源记录；资源或许可范围无法确定就停止并报告。不要修改登录、代理、全局配置或其他 Skill。完成后列出实际文件和未满足的条件。如果无法可靠下载完整子目录，请报告，不用猜测内容补齐。

```

</details>

<details>
<summary>OpenCode · 项目目录</summary>


把整个单项文件夹放到你打开的项目内 `.agents/skills/supply-chain-risk-auditor/`，入口必须是 `.agents/skills/supply-chain-risk-auditor/SKILL.md`。这是相对项目的路径，不是系统目录。

要求模型通过原生 skill 工具加载 supply-chain-risk-auditor，再给任务正文；不是终端命令或统一 /supply-chain-risk-auditor。

也支持 .opencode/skills；本指南只选一个入口，避免重复发现。

[官方说明](https://opencode.ai/docs/skills/)

**可复制的准备任务：**

```text

请只为当前项目准备 supply-chain-risk-auditor，先不要执行它。
固定来源：https://github.com/trailofbits/skills/tree/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/plugins/supply-chain-risk-auditor/skills/supply-chain-risk-auditor
入口：https://github.com/trailofbits/skills/blob/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/plugins/supply-chain-risk-auditor/skills/supply-chain-risk-auditor/SKILL.md
保留许可：https://github.com/trailofbits/skills/blob/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/LICENSE
目标：.agents/skills/supply-chain-risk-auditor/
先确认当前项目路径正确，且目标目录尚不存在；已有同名项时停止，不覆盖、不合并。只获取此固定提交的目标子目录及其必要相对资源，不下载整个合集，不沿外链获取浮动 main/latest，不执行任何脚本或安装依赖。同时保留适用 LICENSE/NOTICE 与来源记录；资源或许可范围无法确定就停止并报告。不要修改登录、代理、全局配置或其他 Skill。完成后列出实际文件和未满足的条件。如果无法可靠下载完整子目录，请报告，不用猜测内容补齐。

```

</details>

<details>
<summary>Claude Code · 项目目录</summary>


把整个单项文件夹放到你打开的项目内 `.claude/skills/supply-chain-risk-auditor/`，入口必须是 `.claude/skills/supply-chain-risk-auditor/SKILL.md`。这是相对项目的路径，不是系统目录。

在项目会话输入 /supply-chain-risk-auditor，再给任务正文。

组织策略、工具权限仍可能限制读取或执行。

[官方说明](https://code.claude.com/docs/en/skills)

**可复制的准备任务：**

```text

请只为当前项目准备 supply-chain-risk-auditor，先不要执行它。
固定来源：https://github.com/trailofbits/skills/tree/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/plugins/supply-chain-risk-auditor/skills/supply-chain-risk-auditor
入口：https://github.com/trailofbits/skills/blob/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/plugins/supply-chain-risk-auditor/skills/supply-chain-risk-auditor/SKILL.md
保留许可：https://github.com/trailofbits/skills/blob/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/LICENSE
目标：.claude/skills/supply-chain-risk-auditor/
先确认当前项目路径正确，且目标目录尚不存在；已有同名项时停止，不覆盖、不合并。只获取此固定提交的目标子目录及其必要相对资源，不下载整个合集，不沿外链获取浮动 main/latest，不执行任何脚本或安装依赖。同时保留适用 LICENSE/NOTICE 与来源记录；资源或许可范围无法确定就停止并报告。不要修改登录、代理、全局配置或其他 Skill。完成后列出实际文件和未满足的条件。如果无法可靠下载完整子目录，请报告，不用猜测内容补齐。

```

</details>

<details>
<summary>Cursor · 项目目录</summary>


把整个单项文件夹放到你打开的项目内 `.agents/skills/supply-chain-risk-auditor/`，入口必须是 `.agents/skills/supply-chain-risk-auditor/SKILL.md`。这是相对项目的路径，不是系统目录。

在 Agent 中输入 /，查找并选择 supply-chain-risk-auditor，再给任务。

本地 Agent 与云端运行可用资源不同；不要据目录支持推断脚本可执行。

[官方说明](https://cursor.com/docs/skills)

**可复制的准备任务：**

```text

请只为当前项目准备 supply-chain-risk-auditor，先不要执行它。
固定来源：https://github.com/trailofbits/skills/tree/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/plugins/supply-chain-risk-auditor/skills/supply-chain-risk-auditor
入口：https://github.com/trailofbits/skills/blob/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/plugins/supply-chain-risk-auditor/skills/supply-chain-risk-auditor/SKILL.md
保留许可：https://github.com/trailofbits/skills/blob/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/LICENSE
目标：.agents/skills/supply-chain-risk-auditor/
先确认当前项目路径正确，且目标目录尚不存在；已有同名项时停止，不覆盖、不合并。只获取此固定提交的目标子目录及其必要相对资源，不下载整个合集，不沿外链获取浮动 main/latest，不执行任何脚本或安装依赖。同时保留适用 LICENSE/NOTICE 与来源记录；资源或许可范围无法确定就停止并报告。不要修改登录、代理、全局配置或其他 Skill。完成后列出实际文件和未满足的条件。如果无法可靠下载完整子目录，请报告，不用猜测内容补齐。

```

</details>

<details>
<summary>Kimi Code · 项目目录</summary>


把整个单项文件夹放到你打开的项目内 `.agents/skills/supply-chain-risk-auditor/`，入口必须是 `.agents/skills/supply-chain-risk-auditor/SKILL.md`。这是相对项目的路径，不是系统目录。

在新会话输入 /skill:supply-chain-risk-auditor，再给任务正文。

面向 Kimi Code CLI/Desktop，不是 Kimi 网页聊天；项目按最近 .git 定位，请先选准项目。

[官方说明](https://www.kimi.com/code/docs/kimi-code-cli/customization/skills.html)

**可复制的准备任务：**

```text

请只为当前项目准备 supply-chain-risk-auditor，先不要执行它。
固定来源：https://github.com/trailofbits/skills/tree/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/plugins/supply-chain-risk-auditor/skills/supply-chain-risk-auditor
入口：https://github.com/trailofbits/skills/blob/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/plugins/supply-chain-risk-auditor/skills/supply-chain-risk-auditor/SKILL.md
保留许可：https://github.com/trailofbits/skills/blob/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/LICENSE
目标：.agents/skills/supply-chain-risk-auditor/
先确认当前项目路径正确，且目标目录尚不存在；已有同名项时停止，不覆盖、不合并。只获取此固定提交的目标子目录及其必要相对资源，不下载整个合集，不沿外链获取浮动 main/latest，不执行任何脚本或安装依赖。同时保留适用 LICENSE/NOTICE 与来源记录；资源或许可范围无法确定就停止并报告。不要修改登录、代理、全局配置或其他 Skill。完成后列出实际文件和未满足的条件。如果无法可靠下载完整子目录，请报告，不用猜测内容补齐。

```

</details>

<details>
<summary>Qoder IDE / CLI · 项目目录</summary>


把整个单项文件夹放到你打开的项目内 `.qoder/skills/supply-chain-risk-auditor/`，入口必须是 `.qoder/skills/supply-chain-risk-auditor/SKILL.md`。这是相对项目的路径，不是系统目录。

IDE 重启后输入 / 查找 supply-chain-risk-auditor；CLI 可 /skills reload 后用 /supply-chain-risk-auditor。

IDE 与 CLI 的同名优先级文档不同；只保留一个同名入口。CLI 文档：https://docs.qoder.com/cli/Skills

[官方说明](https://docs.qoder.com/extensions/skills)

**可复制的准备任务：**

```text

请只为当前项目准备 supply-chain-risk-auditor，先不要执行它。
固定来源：https://github.com/trailofbits/skills/tree/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/plugins/supply-chain-risk-auditor/skills/supply-chain-risk-auditor
入口：https://github.com/trailofbits/skills/blob/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/plugins/supply-chain-risk-auditor/skills/supply-chain-risk-auditor/SKILL.md
保留许可：https://github.com/trailofbits/skills/blob/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/LICENSE
目标：.qoder/skills/supply-chain-risk-auditor/
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

请只为当前项目准备 supply-chain-risk-auditor，先不要执行它。
固定来源：https://github.com/trailofbits/skills/tree/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/plugins/supply-chain-risk-auditor/skills/supply-chain-risk-auditor
入口：https://github.com/trailofbits/skills/blob/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/plugins/supply-chain-risk-auditor/skills/supply-chain-risk-auditor/SKILL.md
保留许可：https://github.com/trailofbits/skills/blob/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/LICENSE
目标：单独的新暂存文件夹/supply-chain-risk-auditor/
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

请只为当前项目准备 supply-chain-risk-auditor，先不要执行它。
固定来源：https://github.com/trailofbits/skills/tree/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/plugins/supply-chain-risk-auditor/skills/supply-chain-risk-auditor
入口：https://github.com/trailofbits/skills/blob/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/plugins/supply-chain-risk-auditor/skills/supply-chain-risk-auditor/SKILL.md
保留许可：https://github.com/trailofbits/skills/blob/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/LICENSE
目标：单独的新暂存文件夹/supply-chain-risk-auditor/
先确认当前项目路径正确，且目标目录尚不存在；已有同名项时停止，不覆盖、不合并。只获取此固定提交的目标子目录及其必要相对资源，不下载整个合集，不沿外链获取浮动 main/latest，不执行任何脚本或安装依赖。同时保留适用 LICENSE/NOTICE 与来源记录；资源或许可范围无法确定就停止并报告。不要修改登录、代理、全局配置或其他 Skill。完成后列出实际文件和未满足的条件。如果无法可靠下载完整子目录，请报告，不用猜测内容补齐。

```

</details>

## 3. 复制任务，先试一个小样例

先完成上一节的加载，再发送下面的中文任务。示例本身不会自动安装或证明调用成功。

```text

开始前先确认你实际读取了 `supply-chain-risk-auditor/SKILL.md`；若不能读取就停止说明。

请只对我明确提供的公开项目依赖清单 `[package.json/lockfile 路径]` 做静态风险收集，不安装或解析依赖、不改文件、不执行项目代码。项目是否包含私有包：[是/否/不确定]；允许查询的公开服务与可能外发的包名/版本：[由我确认后填写]。在任何网络查询前，先只读解析清单，列出拟查询的每个包名、版本、数据字段、目标服务及查询目的，等我明确回复“允许查询这些公开依赖”后再联网。

私有、内部、未公开或归属不明的包一律不外发；未确认前只做本地静态盘点。获准查询后，保留来源与查询时间，分类报告已知漏洞/维护信号/无法评估项；服务不可达或包未识别都不能写成“安全”。输出新报告 `[输出目录]/dependency-review.md`，附范围、版本清单、证据链接、风险等级、误报可能和未完成检查。不要自动升级依赖或修改锁文件。

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



- 原作者/维护方：trailofbits 原始维护仓库；[trailofbits/skills](https://github.com/trailofbits/skills/tree/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/plugins/supply-chain-risk-auditor/skills/supply-chain-risk-auditor)。

- 固定版本：`5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0`；未核实 Skill 语义版本；以完整 Commit 固定。。

- 许可：[CC-BY-SA-4.0](https://github.com/trailofbits/skills/blob/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/LICENSE)。Skill 许可不覆盖依赖、服务、字体、数据或模型。未审计完整传递依赖许可；使用时按所选工具版本和用途另核。

- 依赖许可：第三方依赖/资产/服务单独许可。未完成完整传递依赖或所有使用合同的许可审计；原始材料不复制入本项目。

- 运行依据：当前建议依据静态材料。上游示例、测试源码或限定构建记录不等于本项本地运行通过；本项未做客户端端到端测试。

- 原证据：E1 静态审阅；E2 材料类型：upstream_test_source；核对精确 pin/范围、锁文件闭包、无法验证数据、缓存与渲染等测试断言；测试使用模拟数据，不代表在线数据源端到端已验证。 E3/E4 未执行；推荐建议不代表运行验证。

- [历史固定版本详细记录](../archive/v1.2/docs/skills.md#trailofbits--supply-chain-risk-auditor)。



**已知限制（不是要求你执行的步骤）：**



- 不读 pnpm/yarn/poetry 锁文件；无测量不表示安全；不是许可证合规审计，也不检验包能否安装。

- 仅对已批准公开的依赖元数据使用；私有包名同样可能保密，必须先确认可外发。脚本通过既有 gh 获取 GitHub 凭据，不应把令牌输出、缓存或传给非 GitHub 端点。



**采用前提：**仅对已批准公开的依赖元数据使用；私有包名同样可能保密，必须先确认可外发。脚本通过既有 gh 获取 GitHub 凭据，不应把令牌输出、缓存或传给非 GitHub 端点。 不读 pnpm/yarn/poetry 锁文件；无测量不表示安全；不是许可证合规审计，也不检验包能否安装。



</details>
