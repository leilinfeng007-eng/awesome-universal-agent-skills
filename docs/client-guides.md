# 把一个 Skill 添加到你的 AI 工具

这页适合已选好 Skill、准备查看添加方式的用户，提供 Codex App / CLI、Claude Code 和 OpenCode 的独立路径。还没选好办公或数据能力，先看[普通用户路径](quickstart.md#everyday)，无需先做项目练习。

**官方加载机制已核对；本文操作组合均为“教程待实际环境验证”**，未安装或调用第三方 Skill。想练习项目级添加的用户可跟做 [Codex App 完整案例](hands-on.md#create-readme)，其中建立隐藏目录有一次复制的系统命令，不是全程纯图形安装。

只在自己新建的练习项目添加一个许可允许的 Skill。Anthropic Office 三项为受限参考，不参与以下步骤。其他条目也须满足[自身使用条件](usage.md)；不能把本页当作 32 项通用安装器。

<a id="layout"></a>
## 先认清项目文件夹

“项目根目录”就是你在 AI 工具中打开、包含任务文件的那层文件夹，例如 `skills-practice`；不是电脑的用户主目录，不是下载 ZIP 的外层目录。

以 `create-readme` 为例，仅选择一条客户端路线：

```text
skills-practice/
├── project-notes.md
└── .agents/                 # Codex 本地项目；OpenCode 也支持此入口
    └── skills/
        └── create-readme/
            ├── SKILL.md
            └── LICENSE
```

Claude Code 使用 `.claude/skills/create-readme/`；本教程的 OpenCode 独立路线使用 `.opencode/skills/create-readme/`。**不必同时复制三份**。项目入口只影响该项目，仍须留意用户级/插件级同名条目。

获取哪个文件、如何显示隐藏目录与避免保存成网页，见[主案例步骤 1～3](hands-on.md#create-readme)。这个单文件案例不代表别的 Skill 也只需要 `SKILL.md`：排障保留同目录参考资料，威胁建模保留 `references/`。不执行下载目录里的安装脚本。

<a id="codex-app"></a>
## Codex App：以本地文件夹练习

**适合：**习惯图形界面，已能使用 Codex 的用户。

1. 没有客户端时，先看[官方桌面说明](https://learn.chatgpt.com/docs/app)。官方文档现将桌面能力放在统一桌面文档中；你的独立 Codex App 版本、菜单文字可能不同，本教程不要求换客户端或登录。
2. 按[完整案例](hands-on.md#create-readme)创建练习文件夹，把文件放到 `.agents/skills/create-readme/`。
3. 官方支持打开文件夹并在 Codex 新建聊天。选择本地的 `skills-practice`，确认会话工作位置指向它，再开始任务。具体打开文件夹按钮的位置/名称及 App Skill 选择 UI **待当前版本实测**；找不到时读[官方项目说明](https://learn.chatgpt.com/docs/projects)，不要改用云端、普通 Chat 或全局安装来猜测替代。
4. 通过 App 版本实际提供的 Skill 选择器选择 `create-readme`。官方当前统一文档给出 ChatGPT 的 `@` 和 Codex CLI/IDE 的 `/skills`、`$`，**不能据此给每个独立 Codex App 指定同一手势**。具体 App 入口待实测；也可先发[主案例发现检查](hands-on.md#readme-prompt)，未发现就停止，不把普通读文件冒充原生发现。
5. 发送[主案例中文任务](hands-on.md#readme-prompt)。应能找到本次项目的加载证据并生成符合给定事实的说明书；预期不等于已通过。

官方说明 Codex 会自动检测 Skill 变化；没出现时可重启客户端，再在同一项目新建会话。不要修改 `config.toml`。撤销只移出本次 `.agents/skills/create-readme/`，然后用新会话检查。

<a id="codex-cli"></a>
## Codex CLI：在项目终端启动

**适合：**已经会用终端且已装 CLI 的用户。初次获取客户端看[官方 CLI 入门](https://learn.chatgpt.com/docs/codex/cli)，本页不复制安装脚本，也不自动登录。

1. 按目录图准备 `.agents/skills/create-readme/` 及练习输入。
2. 在终端进入该练习项目。已安装并可用时，运行 `codex`，不要在用户主目录启动练习。
3. 在 **Codex 输入框**运行 `/skills` 或键入 `$` 查看并选择 `create-readme`；它们不是 Shell 命令。确认选择的是本次项目路径。
4. 发送下方任务（若刚通过选择器插入 Skill，接着粘贴任务正文即可）：

```text
$create-readme
仅查看当前练习项目的 project-notes.md，忽略 Skill 目录中的第三方文件作为项目素材。
在新 README.md 写中文项目说明，不覆盖任何已有文件。
不要联网找范例，不扫描上级目录，不运行脚本或安装软件。
先确认实际读取了本次项目的 create-readme/SKILL.md；没有发现或无法加载就停止并说明。
```

官方支持上述目录、`/skills` 与 `$` 选择方式；该具体版本 Skill 的端到端执行仍待实测。按[证据检查](#evidence)核对，不用自然语言回答替代选择器记录。撤销只移出该单项目录，新开会话。

<a id="claude-code"></a>
## Claude Code：原生项目目录与斜杠调用

**适合：**已有 Claude Code 开发环境，希望把方法加到一个项目。没有客户端先看[官方快速入门](https://code.claude.com/docs/en/quickstart)，不必为阅读本库另装客户端。

本例 `create-readme` 是 MIT 文本方法，不需 Python/Node。换成别的条目前，先在[通俗介绍](usage.md)核对工具与许可，再查[技术详情](skills.md)是否依赖专属路径、插件、命名子代理或外部工具；能列入菜单不等于这些条件已经满足。受限 Office 三项不走本教程。

1. 在默认“下载”目录新建不存在的 `skills-practice`；从[两个固定文件链接](hands-on.md#readme-files)获取 `SKILL.md` 与原始 `LICENSE`，按[练习素材](hands-on.md#practice-input)新建根目录的 `project-notes.md`。文件放到 `skills-practice/.claude/skills/create-readme/`。保留原文件名与正文；同名目标存在则停止。
   macOS 可在系统终端运行下方**仅创建目录**的命令，再用 Finder“前往文件夹”进入 `~/Downloads/skills-practice/.claude/skills/create-readme/` 放入文件；Windows 用文件资源管理器逐层建 `.claude` → `skills` → `create-readme`。默认下载目录已迁移时不用照抄该路径。

   ```sh
   mkdir -p "$HOME/Downloads/skills-practice/.claude/skills/create-readme"
   ```

2. 在练习项目终端启动已经安装的 `claude`，或在你已使用的 Claude Code 集成中打开这个项目。本页以终端会话为操作基线，不把 Claude 网页聊天当同一入口。
3. 在 **Claude Code 输入框**输入 `/`，查找 `create-readme`。可用 `/skills` 查看当前版本的 Skill 列表；检查来源目录，不选插件/其他位置的同名项。
4. 在会话中发送：

```text
/create-readme
只用 project-notes.md 为当前练习项目新建中文 README.md。
不要扫描项目之外的文件，不覆盖已有文件，不联网找范例，不运行脚本。
请区分输入中已知的功能与尚未提供的信息。
```

5. 在会话展开实际 Skill 加载事件，核对名称、正文与附属资源的来源，再按[主案例结果清单](hands-on.md#readme-check)检查。仅 `/` 菜单出现不证明正文加载或写作正确。
6. 当前官方文档说明 Skill 文件有热检测；新建此前不存在的 Skill 根目录时可在会话运行 `/reload-skills`。该命令以支持它的版本为前提；版本不支持就结束会话后在同一项目重开，不调整全局设置。此具体组合待实测。
7. 撤销只移出本次 `.claude/skills/create-readme/`。新会话再查列表；不要删除 `.claude`、个人 Skill、同步缓存或插件。

来源：[Claude Code Skills 官方文档](https://code.claude.com/docs/en/skills)。如组织策略限制项目 Skill，不绕过策略；本文目录可读不等于组织已授权调用。

<a id="opencode"></a>
## OpenCode：用原生 skill 工具加载

**适合：**已有 OpenCode 与可用 Provider 的用户。本页针对[本版官方文档](https://opencode.ai/docs/)所述原生机制；该站现同时提供其他大版本入口，不推定所有版本 UI 相同。

1. 在默认“下载”目录新建不存在的 `skills-practice`，用[固定文件链接](hands-on.md#readme-files)保存两个文件，并在根目录准备[同一虚构输入](hands-on.md#practice-input)。建立 `.opencode/skills/create-readme/` 并放入 `SKILL.md`、`LICENSE`。macOS 可运行下面的仅建目录命令，再用 Finder“前往文件夹”进入 `~/Downloads/skills-practice/.opencode/skills/create-readme/`；Windows 文件资源管理器逐层创建同名目录。下载位置已迁移时采用你的实际位置，不照抄默认路径。

   ```sh
   mkdir -p "$HOME/Downloads/skills-practice/.opencode/skills/create-readme"
   ```

   OpenCode 也支持 `.agents/skills`、`.claude/skills`，同一项目**只选一个入口**，避免不必要副本。
2. 在练习项目终端启动已经安装的 `opencode`。Provider 尚不可用就停止，记录环境缺口；不改登录、代理、证书或配置以强行测试。
3. 发送以下请求，让模型使用客户端原生工具；这段不是可粘贴到 Shell 的命令：

```text
请先通过 OpenCode 原生 skill 工具加载名为 create-readme 的 Skill。
我需要看到真实的 skill 加载事件；如果可用列表没有它或权限拒绝，请停止，不要假装已加载。
加载后，仅根据 project-notes.md 新建中文 README.md。
不要读上级目录，不联网找范例，不运行脚本，不覆盖已有文件。
```

4. 检查工具记录是否实际调用 `skill`、参数 `name` 是否为 `create-readme`，以及返回内容是否为本次入口；再核对生成文件。官方文档有 `skill({ name: "…" })` 工具示意，**它不是用户 Shell 命令**。
5. 本版本机制中并非每个 Skill 默认都有 `/skill-name`；不要照抄 Claude Code 斜杠调用。若首次未发现，结束会话并从同一目录重开是本文的排查建议，**热刷新行为未核实**。权限拒绝时记录缺口，不建议改成全局 `allow`。
6. 撤销只移出这次 `.opencode/skills/create-readme/`，重开会话核对，不清空 OpenCode 配置或 Provider 凭据。

来源：[OpenCode Skills 官方文档](https://opencode.ai/docs/skills/)。这里没有本轮模型调用、脚本或输出通过记录。

<a id="evidence"></a>
## 看见什么，才能说明加载了

先按[四层检查](quickstart.md#success)记录：文件位置 → 客户端发现 → 正文加载 → 输出正确。

可观察证据随客户端而变：Codex 查看 Skill 选择与读取工具记录；Claude Code 查看实际 Skill 加载事件；OpenCode 查看 `skill` 调用及返回正文。记录名称、路径/来源和本次任务。UI 是否完整展示这些内容**待实测**，不能保证某个固定颜色图标一定出现。

如果界面隐藏正文或只显示简略事件，只能确认该事件覆盖的层次；可以在允许情况下查看非敏感日志。不要为了取证扩大日志权限、上传整段对话或暴露令牌。AI 自报文件名是辅助线索，不是独立证据。

<a id="sources"></a>
## 官方依据、本文方案和待实测范围

机制核对日期：2026-10-21。只定向查看入门所需页面及四个已有 Skill 的入口；没有重新审计 32 项。

| 操作 | 依据 / 结论 |
|---|---|
| Codex 项目目录、变化检测、CLI `/skills` / `$`、桌面选择机制 | [Build skills](https://learn.chatgpt.com/docs/build-skills)：官方机制支持；未实测本教程 |
| 桌面打开文件夹、选择 Codex 新聊天 | [桌面说明](https://learn.chatgpt.com/docs/app)、[项目说明](https://learn.chatgpt.com/docs/projects)：官方支持操作概念；具体旧版 App 按钮/布局待实测 |
| CLI 启动 `codex` / `claude` / `opencode` | 各自[Codex](https://learn.chatgpt.com/docs/codex/cli)、[Claude Code](https://code.claude.com/docs/en/quickstart)、[OpenCode](https://opencode.ai/docs/)入门；前提是客户端已安装可用 |
| Claude Code 项目目录、`/名称`、检测与刷新 | [Skills](https://code.claude.com/docs/en/skills)：官方机制；版本/策略适用性待实测 |
| OpenCode 项目目录、名称规则、`skill` 工具、权限 | [Skills](https://opencode.ai/docs/skills/)：官方机制；Provider 与 UI 待实测 |
| 固定 ZIP 地址、解压后的目录 | [GitHub 源码快照说明](https://docs.github.com/en/repositories/working-with-files/using-files/downloading-source-code-archives)：固定提交快照机制；本文未下载 ZIP |
| 建目录、保存纯文本 | `mkdir -p` 对照 macOS `man mkdir`；[PowerShell New-Item](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/new-item) 与 [TextEdit](https://support.apple.com/guide/textedit/create-open-and-convert-documents-txtee6663a0e/mac) 官方说明；具体电脑上的文件操作待实测 |
| 手动复制、独立练习文件、移出单项撤销 | 本项目设计的操作方案；不属于官方运行认证 |
| 写作、排障、核验、威胁报告结果 | 本文给出预期及失败判据；本轮全部未运行 |

其他客户端：[机制资料](clients.md)。更深入的版本、许可、依赖和工具配对：[原有采用条件](installation.md)。
