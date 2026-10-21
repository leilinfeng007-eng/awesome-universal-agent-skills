# 把一个 Skill 添加到你的 AI 工具

这页帮你把已经选好的 Skill 接入实际工具：Codex、OpenCode、Kimi Code、Qoder、QoderWork、WorkBuddy，以及 Claude Code。先选**具体产品和形态**，不要只看模型品牌。还没选好能力，先看[普通用户路径](quickstart.md#everyday)。

**官方加载机制已核对；本文操作组合均为“教程待实际环境验证”**，未安装或调用第三方 Skill。想练习项目级添加的用户可跟做 [Codex App 完整案例](hands-on.md#create-readme)，其中建立隐藏目录有一次复制的系统命令，不是全程纯图形安装。

目录型入口优先使用独立练习项目；导入型客户端可能持久保存安装和启用状态，须自己明确选择单项，不接管已有资源。Anthropic Office 三项为受限参考，不参与以下步骤。其他条目也须满足[自身使用条件](usage.md)；本页不替代 Python、浏览器、OfficeCLI 等工具的准备。

<a id="platform-picker"></a>
## 你正在用哪个工具？

| 工具 | 添加方式 | 调用入口 | 点这里继续 |
|---|---|---|---|
| Codex App / CLI | 项目 `.agents/skills/` | App 入口依版本；CLI `/skills`、`$` | [App](#codex-app) / [CLI](#codex-cli) |
| OpenCode | 项目 `.opencode/skills/`，也支持 `.agents/skills/` | 原生 `skill` 工具 | [OpenCode 步骤](#opencode) |
| Kimi Code CLI / Desktop | Git 项目 `.agents/skills/` 或 `.kimi-code/skills/` | `/skill:名称` | [Kimi Code 步骤](#kimi-code) |
| Qoder IDE / CLI | 项目 `.qoder/skills/` | `/名称`；CLI 可 `/skills` | [Qoder 步骤](#qoder) |
| QoderWork | “扩展 → 技能”导入 | `/` 选择或任务指名 | [QoderWork 步骤](#qoderwork) |
| WorkBuddy 桌面版 | 技能面板上传单项技能包 | 新会话中指名 | [WorkBuddy 步骤](#workbuddy) |
| Claude Code | 项目 `.claude/skills/` | `/名称` | [Claude Code 步骤](#claude-code) |

**Kimi 网页、Kimi Code、Qoder IDE、新 Qoder 桌面和 QoderWork 不是同一入口。** 支持技能面板，不等于能读取电脑的 `.agents/skills`。本表仅是已核实的官方机制；本库没有因此完成任一条目的客户端运行验证。

手里还没有 Skill 文件？先到[逐项获取入口](installation.md#get-files)，只取所选目标及必要资源，再回来选择客户端。首次可用[两个文件的练习](hands-on.md#readme-files)理解放置方法，但不需要为了正式工作安装这个练习项。

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

<a id="kimi-code"></a>
## Kimi Code CLI / Desktop

**适合：**已经使用现行 Kimi Code 的用户。此处依据现行 `kimi-code` 文档，不套用旧 `kimi-cli` 的默认目录，也不要求升级现有客户端。

1. 获取固定版本完整单项目录和许可。已有 Git 项目可选 `项目/.agents/skills/<name>/SKILL.md` 或 `项目/.kimi-code/skills/<name>/SKILL.md`，只选一处；项目根是工作目录向上最近包含 `.git` 的目录。不是在任何普通下载文件夹都保证得到相同项目发现结果。
2. `<name>` 使用入口中的真实 `name`，保留相对资源。检查项目和用户入口有无同名项；存在就停止，不覆盖。
3. CLI 用户在该项目重开已经可用的 `kimi` 会话；Desktop 用户打开同一项目。官方明确桌面版沿用目录机制；具体版本界面和本库条目运行待实测。
4. 输入 `/` 查看，再用实际名称调用，例如：

   ```text
   /skill:systematic-debugging 只分析当前练习项目。先复现并给根因证据，不修改文件或安装软件；没有所需工具就说明未复现。
   ```

5. 分别核对可用列表、加载/读取记录、相对资源和结果。保留默认交互审批，不使用自动批准模式来完成教程。
6. 撤销只移出本次添加的单项目录，再重开会话；不删除用户根目录，不改其他 Skill。

**没有 Git 项目？** 官方有启动参数 `kimi --skills-dir ./local-skills`，但它会在本次启动**替换**默认项目及用户发现目录，不是追加。它属于进阶、待实测路线，不能不加说明地让新手使用。

依据：[CLI Skill 文档](https://www.kimi.com/code/docs/kimi-code-cli/customization/skills.html)、[Desktop 扩展](https://www.kimi.com/code/docs/kimi-code-desktop/settings-and-extensions.html)、[启动参数](https://www.kimi.com/code/docs/en/kimi-code-cli/reference/kimi-command)、[权限与工具](https://www.kimi.com/code/docs/kimi-code-cli/reference/tools.html)。[旧版迁移说明](https://www.kimi.com/code/docs/kimi-code-cli/guides/migration.html)只用于辨别版本，不是本教程的升级要求。

Kimi 网页 Agent 模式另有[技能面板](https://www.kimi.com/help/plugins-and-skills/use-skills-in-agent)，但本轮未确认本库任意 GitHub Skill 的完整网页导入路径。不要套用 CLI 目录；标记“本库导入未确认”。

<a id="qoder"></a>
## Qoder IDE / CLI

**适合：**已经使用 Qoder 开发工具的用户。这里不是 QoderWork，也不是另一个新版 Qoder 桌面入口。

1. 将合法获取的完整单项放入 `项目/.qoder/skills/<name>/`，保留 `SKILL.md`、资源与许可；先检查 `.qoder/skills/` 和用户 `~/.qoder/skills/` 是否同名，存在就停止复制。
2. **IDE：**按官方文档重启 IDE，再在对话输入 `/` 查找；使用 `/skill-name` 或明确描述相符任务。
3. **CLI：**在对应项目新开会话；现有会话可 `/skills reload`，用 `/skills` 查看，再 `/skill-name`。这些是 Qoder 输入框中的命令，不是 Shell 命令。
4. 指名任务后核对实际加载记录及资源；脚本仍需本机对应运行环境与权限。条目出现不代表任务完成。
5. 撤销只移出本次项目的单项，再按客户端刷新/重启；不删用户入口、插件或配置。

**同名优先级不能混写。** 官方 IDE 页写项目优先，CLI 页写用户优先；本教程不依赖覆盖顺序，始终先查同名冲突。依据：[IDE Skills](https://docs.qoder.com/extensions/skills)、[CLI Skills](https://docs.qoder.com/cli/Skills)、[CLI 加载排查](https://docs.qoder.com/cli/troubleshoot-loading)。具体 Skill 与版本组合未运行。

<a id="qoderwork"></a>
## QoderWork：独立导入

1. 先获得许可允许的完整单项材料。选择左侧“扩展 → 技能 → 安装技能”，按该页面要求上传 `SKILL.md` **以及所需辅助文件**，不要只上传入口漏掉资源。
2. 导入前检查已安装列表是否重名，重名先停。QoderWork 使用独立 `~/.qoderwork/skills/` 入口，不能从 IDE 的 `.qoder/skills` 或 Codex 的 `.agents/skills` 推断它会直接共享。
3. 确认列表中出现正确项，再输入 `/` 选择或在新任务中指名，随后检查实际加载、资源与结果。
4. 持久导入、同名处理、是否改写内容和符号链接共享行为尚未验证。撤销只操作本次导入项；本轮没有核实所有版本删除按钮，不编造清理命令，不手工清空根目录。

依据：[QoderWork 官方教程](https://docs.qoder.com/zh/qoderwork/skills)。其内置办公能力不代表本目录三项 Anthropic Office 材料因此获得服务外使用许可。

如果你用的是**新版 Qoder 桌面**，另看[该产品的 Skills 文档](https://docs.qoder.com/qoder/skills)：入口为 Extensions → Skills → Add Skills → Upload Skill，可用 ZIP 或 `SKILL.md`。不要直接混用 IDE/Work 的按钮、目录和覆盖规则；本库组合仍待实测。

<a id="workbuddy"></a>
## WorkBuddy：技能包导入

此处为腾讯 `workbuddy.cn` 的桌面产品，不套用 CodeBuddy CLI、其他同名工具或管理器中的目录映射。

1. 在客户端打开“专家·技能·连接器 → 技能 → 添加技能 → 上传技能”，选择许可允许的**单项本地技能包**。该动作会持久安装，不是临时读文件。
2. 先查已安装列表，重名不覆盖。官方用户页没有明确手工发现目录、压缩包层级或同名处理规则；本项目不能保证把任意 GitHub 文件夹随手压缩就能导入。没有可靠包格式依据时停在“打包适配待确认”，不改上游文件碰运气。
3. 导入后在“已安装”确认启用，另开会话，明确指名，例如“请使用 systematic-debugging 分析当前工作空间的这个错误，先给证据，不修改文件”。这是自然语言调用请求；尚未确认该产品通用 `/skill-name` 语法。
4. 看实际加载及结果；保持默认权限，先用工作空间副本。上传成功不证明脚本能运行，Python、Bash 等环境仍需另具备。
5. 暂停时只关闭本次导入项并新开会话。官方说明旧会话可能仍保留已加载内容；不要删除其他技能、全局配置或同步数据。

依据：[技能面板官方说明](https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market)、[权限模式](https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Permission-Modes)。[开放平台 Skill 规范](https://open.workbuddy.cn/docs/skill)的中英文描述、版本和作者要求针对市场发布，不能未经确认就强加给本地导入或据此改写原始 Skill。

**以上新增产品说明均为 2026-10-21 官方机制核对，不是客户端运行验收。** 想查看具体 Skill 的适用范围、依赖与适配点，返回[逐项介绍](usage.md)；其他产品见[机制总表](clients.md)。
