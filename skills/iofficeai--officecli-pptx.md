# 按模板修改 PPT 内容与图表

**officecli-pptx** · 专项选择 · 处理 Word、Excel、PPT / 文档

[← 回到选 Skill](../README.md) · [全部客户端入口](../docs/clients.md)

## 适合我吗？

要保留现有主题，定点修改幻灯片对象。

**适合：**能检查模板和排版的用户。

**为什么选它：**提供单一 CLI 对象层、定点修改和视觉 QA；与代码生成/直接 XML 编辑有不同工程成本，适合按对象修订已有演示文稿。

**怎么选同类：**适合已有演示稿对象编辑，不承诺任意模板无损往返。

**先知道：**母版、动画、字体和实际版面仍需核对；先改副本。

## 开始前要有什么？

- 需先单独准备固定 OfficeCLI 工具、字体和查看器。

上游指南含自动安装与更新步骤。缺工具就停止；即使已安装工具，每次调用也须先落实进程级 OFFICECLI_NO_AUTO_INSTALL=1 与 OFFICECLI_SKIP_UPDATE=1，不能只关闭 autoUpdate。固定平台工具、来源校验与写入边界未确认前，不执行 CLI、安装脚本或 Skill 刷新。目前先交付准备计划，实际配置与格式保真仍待实测。

## 1. 获取这一项

**[打开固定版本的单项文件夹](https://github.com/iOfficeAI/OfficeCLI/tree/fb98e593612dee2cec36847666671dba502e60aa/skills/officecli-pptx)** · [查看入口 SKILL.md](https://github.com/iOfficeAI/OfficeCLI/blob/fb98e593612dee2cec36847666671dba502e60aa/skills/officecli-pptx/SKILL.md) · [许可](https://github.com/iOfficeAI/OfficeCLI/blob/fb98e593612dee2cec36847666671dba502e60aa/LICENSE)

复制整个单项文件夹，包含 references、scripts、assets 等实际存在的子目录；不要只取 SKILL.md。

不熟悉 Git？可以把下面的准备任务交给有网络和文件能力的 AI。它只是可复制的准备说明，不是已实测的一键安装器。先打开你的测试项目，再展开所用客户端，直接复制准备任务；同页往下就是调用示例。

**手工替代：**[下载该固定版本 ZIP](https://github.com/iOfficeAI/OfficeCLI/archive/fb98e593612dee2cec36847666671dba502e60aa.zip)，解压后只取 `skills/officecli-pptx/`，放到下方目标目录。ZIP 是上游全仓库快照，不代表推荐安装合集；不执行其中的安装脚本。另保留[原许可](https://github.com/iOfficeAI/OfficeCLI/blob/fb98e593612dee2cec36847666671dba502e60aa/LICENSE)及适用 NOTICE，剩余合集不用放进 AI 工具。

<details>

<summary>macOS / Windows 放文件时怎么操作</summary>



macOS：在 Finder 打开你的项目，按 `Command + Shift + .` 显示隐藏文件；建立下方的 `.agents` 等目录。Windows：资源管理器打开项目，开启“查看 → 显示 → 文件扩展名”，按下方层级建文件夹。

如果系统询问合并/替换，选择取消。不要出现 `技能名/技能名/SKILL.md` 的双层目录。先用临时项目与虚构文件，不搬动你已有的 Skill。



</details>

## 2. 选你的 AI 工具，然后加载

**官方机制已核对，本项未逐客户端实测。** 支持目录不代表工具、权限或脚本已经就绪。下面每个入口包含独立路径，不要同时复制到多个地方。

<details>
<summary>Codex App / CLI · 项目目录</summary>


把整个单项文件夹放到你打开的项目内 `.agents/skills/officecli-pptx/`，入口必须是 `.agents/skills/officecli-pptx/SKILL.md`。这是相对项目的路径，不是系统目录。

在 App 的 Skill 选择器中查找名称；CLI 可用 $officecli-pptx。若版本界面不同，先要求 AI 读取实际入口路径。

App 按项目打开本文件夹，新会话再检查；具体界面未在本项实测。

[官方说明](https://learn.chatgpt.com/docs/build-skills)

**可复制的准备任务：**

```text

请只为当前项目准备 officecli-pptx，先不要执行它。
固定来源：https://github.com/iOfficeAI/OfficeCLI/tree/fb98e593612dee2cec36847666671dba502e60aa/skills/officecli-pptx
入口：https://github.com/iOfficeAI/OfficeCLI/blob/fb98e593612dee2cec36847666671dba502e60aa/skills/officecli-pptx/SKILL.md
保留许可：https://github.com/iOfficeAI/OfficeCLI/blob/fb98e593612dee2cec36847666671dba502e60aa/LICENSE
目标：.agents/skills/officecli-pptx/
先确认当前项目路径正确，且目标目录尚不存在；已有同名项时停止，不覆盖、不合并。只获取此固定提交的目标子目录及其必要相对资源，不下载整个合集，不沿外链获取浮动 main/latest，不执行任何脚本或安装依赖。同时保留适用 LICENSE/NOTICE 与来源记录；资源或许可范围无法确定就停止并报告。不要修改登录、代理、全局配置或其他 Skill。完成后列出实际文件和未满足的条件。如果无法可靠下载完整子目录，请报告，不用猜测内容补齐。

```

</details>

<details>
<summary>OpenCode · 项目目录</summary>


把整个单项文件夹放到你打开的项目内 `.agents/skills/officecli-pptx/`，入口必须是 `.agents/skills/officecli-pptx/SKILL.md`。这是相对项目的路径，不是系统目录。

要求模型通过原生 skill 工具加载 officecli-pptx，再给任务正文；不是终端命令或统一 /officecli-pptx。

也支持 .opencode/skills；本指南只选一个入口，避免重复发现。

[官方说明](https://opencode.ai/docs/skills/)

**可复制的准备任务：**

```text

请只为当前项目准备 officecli-pptx，先不要执行它。
固定来源：https://github.com/iOfficeAI/OfficeCLI/tree/fb98e593612dee2cec36847666671dba502e60aa/skills/officecli-pptx
入口：https://github.com/iOfficeAI/OfficeCLI/blob/fb98e593612dee2cec36847666671dba502e60aa/skills/officecli-pptx/SKILL.md
保留许可：https://github.com/iOfficeAI/OfficeCLI/blob/fb98e593612dee2cec36847666671dba502e60aa/LICENSE
目标：.agents/skills/officecli-pptx/
先确认当前项目路径正确，且目标目录尚不存在；已有同名项时停止，不覆盖、不合并。只获取此固定提交的目标子目录及其必要相对资源，不下载整个合集，不沿外链获取浮动 main/latest，不执行任何脚本或安装依赖。同时保留适用 LICENSE/NOTICE 与来源记录；资源或许可范围无法确定就停止并报告。不要修改登录、代理、全局配置或其他 Skill。完成后列出实际文件和未满足的条件。如果无法可靠下载完整子目录，请报告，不用猜测内容补齐。

```

</details>

<details>
<summary>Claude Code · 项目目录</summary>


把整个单项文件夹放到你打开的项目内 `.claude/skills/officecli-pptx/`，入口必须是 `.claude/skills/officecli-pptx/SKILL.md`。这是相对项目的路径，不是系统目录。

在项目会话输入 /officecli-pptx，再给任务正文。

组织策略、工具权限仍可能限制读取或执行。

[官方说明](https://code.claude.com/docs/en/skills)

**可复制的准备任务：**

```text

请只为当前项目准备 officecli-pptx，先不要执行它。
固定来源：https://github.com/iOfficeAI/OfficeCLI/tree/fb98e593612dee2cec36847666671dba502e60aa/skills/officecli-pptx
入口：https://github.com/iOfficeAI/OfficeCLI/blob/fb98e593612dee2cec36847666671dba502e60aa/skills/officecli-pptx/SKILL.md
保留许可：https://github.com/iOfficeAI/OfficeCLI/blob/fb98e593612dee2cec36847666671dba502e60aa/LICENSE
目标：.claude/skills/officecli-pptx/
先确认当前项目路径正确，且目标目录尚不存在；已有同名项时停止，不覆盖、不合并。只获取此固定提交的目标子目录及其必要相对资源，不下载整个合集，不沿外链获取浮动 main/latest，不执行任何脚本或安装依赖。同时保留适用 LICENSE/NOTICE 与来源记录；资源或许可范围无法确定就停止并报告。不要修改登录、代理、全局配置或其他 Skill。完成后列出实际文件和未满足的条件。如果无法可靠下载完整子目录，请报告，不用猜测内容补齐。

```

</details>

<details>
<summary>Cursor · 项目目录</summary>


把整个单项文件夹放到你打开的项目内 `.agents/skills/officecli-pptx/`，入口必须是 `.agents/skills/officecli-pptx/SKILL.md`。这是相对项目的路径，不是系统目录。

在 Agent 中输入 /，查找并选择 officecli-pptx，再给任务。

本地 Agent 与云端运行可用资源不同；不要据目录支持推断脚本可执行。

[官方说明](https://cursor.com/docs/skills)

**可复制的准备任务：**

```text

请只为当前项目准备 officecli-pptx，先不要执行它。
固定来源：https://github.com/iOfficeAI/OfficeCLI/tree/fb98e593612dee2cec36847666671dba502e60aa/skills/officecli-pptx
入口：https://github.com/iOfficeAI/OfficeCLI/blob/fb98e593612dee2cec36847666671dba502e60aa/skills/officecli-pptx/SKILL.md
保留许可：https://github.com/iOfficeAI/OfficeCLI/blob/fb98e593612dee2cec36847666671dba502e60aa/LICENSE
目标：.agents/skills/officecli-pptx/
先确认当前项目路径正确，且目标目录尚不存在；已有同名项时停止，不覆盖、不合并。只获取此固定提交的目标子目录及其必要相对资源，不下载整个合集，不沿外链获取浮动 main/latest，不执行任何脚本或安装依赖。同时保留适用 LICENSE/NOTICE 与来源记录；资源或许可范围无法确定就停止并报告。不要修改登录、代理、全局配置或其他 Skill。完成后列出实际文件和未满足的条件。如果无法可靠下载完整子目录，请报告，不用猜测内容补齐。

```

</details>

<details>
<summary>Kimi Code · 项目目录</summary>


把整个单项文件夹放到你打开的项目内 `.agents/skills/officecli-pptx/`，入口必须是 `.agents/skills/officecli-pptx/SKILL.md`。这是相对项目的路径，不是系统目录。

在新会话输入 /skill:officecli-pptx，再给任务正文。

面向 Kimi Code CLI/Desktop，不是 Kimi 网页聊天；项目按最近 .git 定位，请先选准项目。

[官方说明](https://www.kimi.com/code/docs/kimi-code-cli/customization/skills.html)

**可复制的准备任务：**

```text

请只为当前项目准备 officecli-pptx，先不要执行它。
固定来源：https://github.com/iOfficeAI/OfficeCLI/tree/fb98e593612dee2cec36847666671dba502e60aa/skills/officecli-pptx
入口：https://github.com/iOfficeAI/OfficeCLI/blob/fb98e593612dee2cec36847666671dba502e60aa/skills/officecli-pptx/SKILL.md
保留许可：https://github.com/iOfficeAI/OfficeCLI/blob/fb98e593612dee2cec36847666671dba502e60aa/LICENSE
目标：.agents/skills/officecli-pptx/
先确认当前项目路径正确，且目标目录尚不存在；已有同名项时停止，不覆盖、不合并。只获取此固定提交的目标子目录及其必要相对资源，不下载整个合集，不沿外链获取浮动 main/latest，不执行任何脚本或安装依赖。同时保留适用 LICENSE/NOTICE 与来源记录；资源或许可范围无法确定就停止并报告。不要修改登录、代理、全局配置或其他 Skill。完成后列出实际文件和未满足的条件。如果无法可靠下载完整子目录，请报告，不用猜测内容补齐。

```

</details>

<details>
<summary>Qoder IDE / CLI · 项目目录</summary>


把整个单项文件夹放到你打开的项目内 `.qoder/skills/officecli-pptx/`，入口必须是 `.qoder/skills/officecli-pptx/SKILL.md`。这是相对项目的路径，不是系统目录。

IDE 重启后输入 / 查找 officecli-pptx；CLI 可 /skills reload 后用 /officecli-pptx。

IDE 与 CLI 的同名优先级文档不同；只保留一个同名入口。CLI 文档：https://docs.qoder.com/cli/Skills

[官方说明](https://docs.qoder.com/extensions/skills)

**可复制的准备任务：**

```text

请只为当前项目准备 officecli-pptx，先不要执行它。
固定来源：https://github.com/iOfficeAI/OfficeCLI/tree/fb98e593612dee2cec36847666671dba502e60aa/skills/officecli-pptx
入口：https://github.com/iOfficeAI/OfficeCLI/blob/fb98e593612dee2cec36847666671dba502e60aa/skills/officecli-pptx/SKILL.md
保留许可：https://github.com/iOfficeAI/OfficeCLI/blob/fb98e593612dee2cec36847666671dba502e60aa/LICENSE
目标：.qoder/skills/officecli-pptx/
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

请只为当前项目准备 officecli-pptx，先不要执行它。
固定来源：https://github.com/iOfficeAI/OfficeCLI/tree/fb98e593612dee2cec36847666671dba502e60aa/skills/officecli-pptx
入口：https://github.com/iOfficeAI/OfficeCLI/blob/fb98e593612dee2cec36847666671dba502e60aa/skills/officecli-pptx/SKILL.md
保留许可：https://github.com/iOfficeAI/OfficeCLI/blob/fb98e593612dee2cec36847666671dba502e60aa/LICENSE
目标：单独的新暂存文件夹/officecli-pptx/
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

请只为当前项目准备 officecli-pptx，先不要执行它。
固定来源：https://github.com/iOfficeAI/OfficeCLI/tree/fb98e593612dee2cec36847666671dba502e60aa/skills/officecli-pptx
入口：https://github.com/iOfficeAI/OfficeCLI/blob/fb98e593612dee2cec36847666671dba502e60aa/skills/officecli-pptx/SKILL.md
保留许可：https://github.com/iOfficeAI/OfficeCLI/blob/fb98e593612dee2cec36847666671dba502e60aa/LICENSE
目标：单独的新暂存文件夹/officecli-pptx/
先确认当前项目路径正确，且目标目录尚不存在；已有同名项时停止，不覆盖、不合并。只获取此固定提交的目标子目录及其必要相对资源，不下载整个合集，不沿外链获取浮动 main/latest，不执行任何脚本或安装依赖。同时保留适用 LICENSE/NOTICE 与来源记录；资源或许可范围无法确定就停止并报告。不要修改登录、代理、全局配置或其他 Skill。完成后列出实际文件和未满足的条件。如果无法可靠下载完整子目录，请报告，不用猜测内容补齐。

```

</details>

## 3. 复制任务，先试一个小样例

先完成上一节的加载，再发送下面的中文任务。示例本身不会自动安装或证明调用成功。

```text

开始前先确认你实际读取了 `officecli-pptx/SKILL.md`。检查 OfficeCLI 是否已安装、版本与来源合规，并确认当前进程可设置 `OFFICECLI_NO_AUTO_INSTALL=1`、`OFFICECLI_SKIP_UPDATE=1`；条件不全就停止，不运行、安装或更新工具。

请在 `[原演示文稿路径]` 的第 `[页码/范围]` 页，将 `[原内容/图表]` 更新为 `[新文案/数据来源]`。目标听众：[人群]；需要保留：[母版、主题、字号、图形、动画、页脚及其他页]。先检查指定页与相关图表数据，只读原文件；结果写入新副本 `[输出目录]/修改稿.pptx`，不得覆盖原件或修改未授权页面。

现在只列出拟修改页、对象、数据映射与可能的版式影响，等待我回复“确认修改副本”。确认后才制作副本并修改；不安装依赖、不联网获取素材。完成后比较指定页与非目标页内容，核对图表数据与标签，并渲染/打开所有受影响页面查看字体、溢出、遮挡和对齐。若无法渲染或查看，明确列为未验证，不能仅凭 PPTX 可打开就宣称模板保真。

```

运行前先让 AI 确认工具是否存在，只处理授权范围与副本；缺工具时先报缺项，不自动安装。

## 4. 怎么知道生效了？

1. 让 AI 说出实际读取的 SKILL.md 路径，并概括这次要执行的步骤。

2. 检查是否读到了需要的参考文件；仅回答“我会用”不能证明加载。

3. 只有准备条件确认后才对副本测试，逐页检查主题、字体、母版、溢出和图表数值。

## 没生效 / 想撤销

先查项目是否打开正确、入口是否为 `技能名/SKILL.md`、是否有同名冲突，然后新建会话重新检查。缺工具不等于 Skill 没加载；看到名字也不等于任务成功。

项目目录方式：只把**本次新加的单项文件夹**移到项目外留作备份，再新建会话。导入方式：只禁用本次导入项并新建任务；删除行为先看客户端确认提示。不要清空整个 skills、缓存或配置目录。

<details>

<summary>来源、固定版本、许可与已知限制</summary>



- 原作者/维护方：iOfficeAI 原始维护仓库；[iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI/tree/fb98e593612dee2cec36847666671dba502e60aa/skills/officecli-pptx)。

- 固定版本：`fb98e593612dee2cec36847666671dba502e60aa`；Skill 以源码 Commit 固定；CLI 项目字段 1.0.157，发行标签对应关系及差异见限制。。

- 许可：[Apache-2.0](https://github.com/iOfficeAI/OfficeCLI/blob/fb98e593612dee2cec36847666671dba502e60aa/LICENSE)。Skill 及同仓原创代码按根 Apache-2.0；NOTICE 须保留；捆绑依赖按 THIRD-PARTY-NOTICES，不能称为零依赖。

- 依赖许可：第三方依赖/资产/服务单独许可。未完成完整传递依赖或所有使用合同的许可审计；原始材料不复制入本项目。

- 运行依据：当前建议依据静态材料。上游示例、测试源码或限定构建记录不等于本项本地运行通过；本项未做客户端端到端测试。

- 原证据：E1：Skill、处理器与安装/更新控制静态证据；E2-success-record（CLI 构建范围）：发行提交的 GitHub Actions 记录 linux-x64、mac-arm64、win-x64 create document 步骤 success，其余平台该步骤 skipped。步骤只创建/添加/读取/关闭 DOCX，未核对版式/公式数值，不证明 XLSX/PPTX 或 Skill 端到端成功。E3/E4 未执行。

- [历史固定版本详细记录](../archive/v1.2/docs/skills.md#iofficeai--officecli-pptx)。



**已知限制（不是要求你执行的步骤）：**



- 模板/母版匹配是 Skill 要求，不是任意复杂模板不变的保证；字体、主题、动画及不同查看器渲染需另验。

- 形状布局坐标由调用者负责，没有通用自动排版保证；高级编辑能力不能由 README 宣传直接认定通过。

- 源提交版本字段为 1.0.157；发行标签 v1.0.157 指向另一提交。三个 SKILL.md、版本文件及 4 个关键控制文件逐项 blob 相同；源提交比标签多 5 个提交、11 个 Word/PPT 实现文件变化，不能说两者完整源码一致或发行二进制已覆盖这些修复。



**采用前提：**仅导航专项，不执行上游默认 setup；未来采用时选择固定发行 v1.0.157 的正确平台资产，先核对来源与已记录 digest/SHA256SUMS，使用自管完整路径；首次及每次调用都用进程级 OFFICECLI_NO_AUTO_INSTALL=1 与 OFFICECLI_SKIP_UPDATE=1，不改全局配置；不调用 install、skills install、MCP 安装或升级入口。仅设置 autoUpdate=false 不足以阻止 Skill 刷新。确认实际用户配置、日志及临时/驻留进程的写入边界，先处理副本。上述是静态采用方案，未实测。



</details>
