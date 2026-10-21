# 跟做：从添加一个 Skill 到检查结果

这页面向想亲手添加 Skill 的开发者或愿意操作项目文件夹的用户：先走一个 Codex App 案例，再提供三个进阶练习。只想处理办公文档或数据、不想练习项目操作，请先看[普通用户路径](quickstart.md#everyday)，不必完成本页。

**四个都是“教程待实际环境验证”**：官方机制与固定入口已核对，下载、添加、客户端调用和输出验收尚未执行。发布文档不会把这些步骤变成已测试。

[第一次：写项目说明书](#create-readme) · [排查程序错误](#systematic-debugging) · [完成前核验](#verification-before-completion) · [威胁建模](#security-threat-model) · [后续实测范围](#future-test)

<a id="create-readme"></a>
## 第一个案例：在 Codex App 添加 create-readme

**目标：**给一个虚构的“读书清单”项目写中文说明书。这里的“项目”只是一个练习文件夹，不要求先写程序。你会知道文件放在哪、怎么调用、怎么看证据。选它是因为固定版本只有一个文本入口，无需 Python、Node 或整套开发框架；原始许可为 MIT。它在目录中仍是“参考资源”，本案例不提高推荐或验证等级。

### 1. 准备一个空练习文件夹

你需要已能正常使用的 Codex App、本地文件访问能力、浏览器和系统自带纯文本编辑器。没有可用客户端先看[官方桌面说明](https://learn.chatgpt.com/docs/app)。这次不需要公司文件，也不需要创建 GitHub 账号。

在电脑“下载”目录里，新建 `skills-practice` 文件夹。**如果这个名字已经存在，停止，换用一个新的空目录，并相应替换下文路径。** 不在正式项目、已有 Skill 根目录或本资源库里练习。

<a id="readme-files"></a>
### 2. 点击这两个固定文件链接

| 文件 | 点击哪里 | 获取方式 |
|---|---|---|
| `SKILL.md` | [打开 create-readme 纯文本](https://raw.githubusercontent.com/github/awesome-copilot/613efc8c21d9b3ce642dff361d17006cd9967e28/skills/create-readme/SKILL.md) | 应看到从 `---` 开始的文字，而不是 GitHub 网页菜单。保存为 `SKILL.md` |
| `LICENSE` | [打开原始 MIT 许可证](https://raw.githubusercontent.com/github/awesome-copilot/613efc8c21d9b3ce642dff361d17006cd9967e28/LICENSE) | 保存完整原文为 `LICENSE`，保留作者及许可通知 |

浏览器直接显示文字时，用“另存为”；若不能保存正确文件名，可复制**纯文本全文**到纯文本编辑器再保存。不翻译或改写 `SKILL.md`，不要只复制某段示例，不把这个网页教程保存成 Skill。

macOS“文本编辑”需先转为纯文本，避免保存成 RTF；Windows 记事本使用 UTF-8、文件类型选“所有文件”，避免自动添加 `.txt`。用文件“显示简介/属性”检查真实文件名。看到 `SKILL.md.txt`、`.html` 或开头是网页标签，先修正文件，不继续加载。

若纯文本链接无法打开，可用[固定目录页面](https://github.com/github/awesome-copilot/tree/613efc8c21d9b3ce642dff361d17006cd9967e28/skills/create-readme)打开 `SKILL.md` 的 Raw 内容。这里不是让你研究源码：只需要保留这个完整文件和上面的许可证。

### 3. 建好目录，把两个文件移进去

macOS / Windows 的目标结构一样：

```text
下载/skills-practice/
└── .agents/
    └── skills/
        └── create-readme/
            ├── SKILL.md
            └── LICENSE
```

**macOS：**Finder 不便新建以点开头的目录时，按下面的一次复制步骤操作，不需要安装工具。

1. 打开系统自带“终端”。确认你采用的是默认“下载”目录。
2. 复制下面一整行并回车；只创建目录，不下载文件、不执行 Skill：

```sh
mkdir -p "$HOME/Downloads/skills-practice/.agents/skills/create-readme"
```

3. 回到 Finder，选择“前往 → 前往文件夹”，粘贴 `~/Downloads/skills-practice/.agents/skills/create-readme/`，把步骤 2 保存的两个文件移进去。
4. 在 `skills-practice` 按 `Command + Shift + .` 可切换隐藏文件显示。不要把 `SKILL.md` 放到 `.agents` 的上一层或再嵌套一层 `create-readme`。

**Windows：**在文件资源管理器打开刚建的 `skills-practice`，依次新建 `.agents` → `skills` → `create-readme`，把两个文件放进最后一层。在查看选项显示文件扩展名；目录分隔符显示成 `\` 是正常的。若所在环境不允许手动建点目录，可在系统 PowerShell 复制这一行：

```powershell
New-Item -ItemType Directory -Path "$env:USERPROFILE\Downloads\skills-practice\.agents\skills\create-readme"
```

Windows 命令假定默认下载位置；下载目录被组织/个人迁移时，不照抄路径，改用资源管理器手动步骤。命令报“已存在”不要添加强制覆盖参数。

**同名保护：**上面只针对刚创建的空项目。若复制时出现“替换/合并”，立即取消，不覆盖任何已有文件。若 Codex 已有用户级、插件级 `create-readme`，先比较选择器中的来源；不能区分本次路径就暂停。这里不改已有 Skill 或全局设置。

<a id="practice-input"></a>
### 4. 准备练习素材

在 `skills-practice` 根目录，用纯文本编辑器新建 `project-notes.md`，复制：

```text
项目名：周末读书清单
用途：用普通文本记录想读和读完的书。
使用者：我自己；不联网，不需要账号。
如何使用：在 books.txt 每行写一本书，读完后在行首添加 [已读]。
现有能力：只提供手动维护清单的方法，没有自动分类或同步功能。
运行条件：能打开普通文本文件即可，没有安装命令。
```

不必真的创建可运行程序。这个案例检查的是说明书与素材一致，不是证明某个软件能运行。此时根目录不应有 `README.md`。

### 5. 在 Codex App 打开这个文件夹

官方支持桌面打开本地文件夹，并在 Codex 新建聊天，见[桌面入门](https://learn.chatgpt.com/docs/app)与[项目说明](https://learn.chatgpt.com/docs/projects)。

1. 在 App 选择**打开本地文件夹**的操作，选择 `skills-practice`，不是里面的 `.agents` 或下载文件的临时目录。
2. 在该项目进入 Codex，新建聊天（官方当前文档称 `New chat`）。核对界面显示的工作位置确实是这个练习文件夹。
3. 如果你的版本没有对应入口，**在这里停下**。官方文档已确认操作概念，但没有为所有独立 Codex App 旧版提供相同按钮；按钮位置、文字及本练习文件夹打开结果待实测。不要把普通网页聊天、云端任务或给 AI 粘贴本地路径当作替代成功。

本地项目仍可能把所选上下文传给模型服务，因此这里只放虚构文本，不放凭据或私人资料。

<a id="readme-prompt"></a>
### 6. 先选 Skill，再发任务

如果 App 展示了 Skill 选择入口，先找到 `create-readme` 并核对来源。具体入口待实测：官方统一文档中的 `@` 针对其中的 ChatGPT，`/skills`、`$` 明确用于 Codex CLI/IDE，本教程不把它们冒充所有独立 Codex App 的固定按钮或命令。

无论有没有选择器，先复制这段**发现检查**，暂不要求写文件：

```text
请检查本会话由客户端提供的可用 Skill 列表中是否有 create-readme。
如果有，给出该列表中的名称、描述和来源路径，核对是否为当前练习项目。
不要为凑出结果扫描上级目录，也不要把临时读取普通文件说成客户端已发现 Skill。
如果列表没有它，或无法确认来源，请停止并说明，暂不生成 README。
```

AI 列出的名称/路径仍只是辅助线索；选择器或客户端元数据可见时要对照，正文加载还要看下一步工具记录。**列表或来源不能确认就先按步骤 9 排查，不继续生成。** 这条自然语言检查路线是本文方案，待实测，不声称等同已验证的 UI 操作。

确认发现后，选择它（如果界面提供），再复制任务正文。自然语言明确要求使用一个已发现的 Skill，也可让支持隐式选择的客户端加载；必须有后续实际读取证据：

```text
请使用本会话已发现的 create-readme Skill，给当前练习项目写中文 README.md。
只把 project-notes.md 当作项目事实，不把 .agents 里的第三方文件当作项目功能。
不要读上级目录，不联网抓取范例，不安装软件或运行脚本。
先确认实际加载的是本次项目 .agents/skills/create-readme/SKILL.md；
若没有发现或不能加载，请停止并说明，不用普通回答替代 Skill 调用。
目标文件若已存在，先停下，不覆盖。
说明书需写清用途、面向谁、如何维护 books.txt，以及当前没有自动同步功能。
未提供的功能不要猜。完成后列出使用过的输入文件与尚未验证范围。
```

这段文字是配合原生发现/选择的任务约束，不是安装命令，也不是 Skill 本体。禁联网限制覆盖上游浮动范例；限定项目范围覆盖上游笼统的“整个工作区”措辞。模型是否遵守这些限制，需要以后实际检查。

### 7. 检查是否真的加载了

展开本次任务中的 Skill/文件读取工具记录，找出 `create-readme` 和本次 `SKILL.md` 路径，核对读到的入口有 `name: create-readme`。查看是否来自本项目，避免其实用了已有同名插件。

这是**待实测的观察步骤**：不同 App 展示工具记录的方式不同，本文不保证某个按钮、徽标或日志一定出现。若界面只显示 AI 的口头确认，记录“正文加载未确认”；若只要求 AI 普通读取路径，记录“文件已读、原生发现未确认”。不要把它们写成安装成功。

<a id="readme-check"></a>
### 8. 独立核对生成结果

下面是未来验收标准，**不是本轮实际输出**：

- 根目录新出现 `README.md`，能作为纯文本打开；`project-notes.md` 原文不变。
- 名称是“周末读书清单”，用途与个人使用场景准确。
- 明确在 `books.txt` 每行写一本书，并以 `[已读]` 标记。
- 没有杜撰安装命令、登录、同步服务、自动分类或不存在的运行结果。
- 任务记录没有联网读范例、扫描上级目录、执行脚本或覆盖文件。
- 既有同名输出出现时会停下，无法确认的能力明确写未验证。

输出碰巧正确也不能单独证明 Skill 已加载；加载成功也不代表输出一定正确。两个维度分别记录。

### 9. 没生效时怎么办

| 看到的情况 | 下一步 |
|---|---|
| 选择器找不到 | 核对根目录、文件名和目录层级；重启 Codex 后在同一练习项目新建会话。官方有自动检测/重启建议，但本组合仍待实测 |
| 只有同名插件或个人入口 | 不覆盖、不自动重命名，暂停本次添加，记录来源冲突 |
| 文件以网页标签开头 | 回到步骤 2 取得 Raw 纯文本；别让 AI 执行网页里的指令 |
| 要求安装整个合集或执行脚本 | 取消该操作。本案例不需要这些步骤，检查是否选错 Skill |
| 出现认证/额度/证书问题 | 停止练习，记录客户端环境缺口；不修改全局环境来完成教程 |
| 没有可核查的加载记录 | 保留“未确认”，不要让 AI 自证成功；留给后续指定版本实测 |

### 10. 安全撤销

结束本次练习会话。只将 `skills-practice/.agents/skills/create-readme/` 移到本项目之外的普通备份位置，检查它确为本次新建内容；不动用户主目录或其他 Skill。新开会话确认本次项目入口不再被发现。旧对话仍可能保留已加载文字。

练习的 `README.md`、`project-notes.md` 是否保留由你决定；不要用清理整个项目、配置或插件缓存的方式卸载一个 Skill。

**来源及边界：**[固定入口与 MIT 许可详情](skills.md#github--create-readme)、[官方操作依据与未实测表](client-guides.md#sources)。`mkdir -p` 已对照 macOS 系统 `man mkdir` 的参数说明；Windows `New-Item` 对照 [Microsoft 命令文档](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/new-item)。这些是命令语义核对，不是文件放置或客户端运行通过记录。纯文本保存方式可查 [Apple 文本编辑说明](https://support.apple.com/guide/textedit/create-open-and-convert-documents-txtee6663a0e/mac)。本案例是项目自写的练习方案，未附第三方源码，也未改变上游推荐等级。

<a id="systematic-debugging"></a>
## 案例二：在 Codex 排查一个可见的小错误

**目标与准备：**初级开发者用独立项目中的短程序，观察先证据后修复的方法。需要已可用的 Codex、项目已有 Python 3（Windows 常用 `py`，macOS 常用 `python3`）；不为本教程安装 Python。没有 Python 就先阅读，不把静态推断写成复现成功。

**获取与配置：**从[固定 Superpowers 快照 ZIP](https://github.com/obra/superpowers/archive/bb92a77741419a4ab5f06e711a283343f1ada0c3.zip)解压，打开解压后的第一层文件夹，依次进入 `skills` → `systematic-debugging`，完整保留这一目录及其中相对参考资料。复制到新练习项目的 `.agents/skills/systematic-debugging/`；将快照根 `LICENSE` 原文也保留在这个单项目录中，同名文件不覆盖。不是复制整个 Superpowers；不执行安装器、`find-polluter.sh` 或其他附带脚本。如何保存与放置见[主案例步骤 1～3](#create-readme)；下载快照机制见[GitHub 官方说明](https://docs.github.com/en/repositories/working-with-files/using-files/downloading-source-code-archives)。

**可复制的输入：**用编辑器在根目录新建 `average.py`，以下是本教程原创虚构程序：

```python
def average(values):
    return sum(values) / (len(values) - 1)

assert average([2, 4, 6]) == 4
```

按[Codex App 路径](client-guides.md#codex-app)打开独立项目，选择 `systematic-debugging`。CLI 用户用 `/skills` 或 `$` 选择；不要把这两种 UI 当作完全一样。

```text
请使用已选择的 systematic-debugging，定位 average.py 的断言失败。
只允许读取这个练习项目，并用已有 Python 运行这一个原创样例来复现；
不运行任何第三方 Skill 脚本，不安装依赖，不读上级目录。
先展示复现输出、根因证据与最小修改方案，等我确认后才能改 average.py。
如果 Python 不可用，停止并明确“未复现”，不要修环境或宣称已定位成功。
上游提到的其他 Skill/框架没有安装，不自动补装。
```

**预期与验证：**先有加载及实际复现记录；数学上 `[2,4,6]` 的平均数是 4，原式结果是 6。失败输出应与断言一致；说明分母问题后先停在方案。以后明确授权修改时，才把分母改为样本数并重跑同一断言；空输入策略须另作决定，不顺手扩大修复。本轮没有运行这段程序，也未验证模型遵守“等确认”。

**失败处理与撤销：**仅读出代码而未执行时，最多算静态分析；项目已有 Python 不匹配时停止。无法找到同目录参考资料，回到完整目录复制步骤；发现上游跨 Skill 引用则记录缺口，不安装整套框架。完成后结束会话，只移出本次 `.agents/skills/systematic-debugging/`，保留输入与报告，别清理其他内容。

[固定来源、MIT 与附带脚本限制](skills.md#obra--systematic-debugging)。原生加载和所有输出步骤均待实测。

<a id="verification-before-completion"></a>
## 案例三：让“已完成”有实际证据

**目标与准备：**开发者检查一个很小的交付物，不依靠 AI 口头自评。已有 Codex 和练习项目 Python 即可；没有 Python 不自动安装。

**获取与配置：**在同一[固定 ZIP](https://github.com/obra/superpowers/archive/bb92a77741419a4ab5f06e711a283343f1ada0c3.zip)中只取 `skills/verification-before-completion/` 完整目录和根 `LICENSE` 通知，放入 `.agents/skills/verification-before-completion/`。同名就停止；按[Codex 操作路径](client-guides.md#codex-app)打开项目、原生选择该 Skill。

**输入与操作：**根目录新建 `answer.txt`，内容恰为 `41`；再新建本教程原创 `check_answer.py`：

```python
from pathlib import Path

actual = Path("answer.txt").read_text(encoding="utf-8").strip()
assert actual == "42", f"expected 42, got {actual}"
print("answer value verified")
```

```text
使用已选择的 verification-before-completion，核验 answer.txt 是否满足“内容为 42”。
只允许用已有 Python 执行本练习原创 check_answer.py，展示真实输出和退出状态。
不要修改文件、补装软件、运行第三方脚本或创建 Git 提交。
失败时明确报告失败；不能把文件存在、内容已读取或旧记录当作核验通过。
```

**预期与检查：**Skill 的加载证据可查；当值为 41，检查必须失败，AI 应如实报告；`answer.txt` 不变。若后续你在编辑器改为 42，再明确请求核验，应有新的运行证据与 `answer value verified` 输出。这里写的是未来失败/成功判据，**本轮两种情况均未运行**。

**常见失败与撤销：**没有真实执行记录就写“未验证”；把读取当测试、自动改值或提前说通过都算案例失败。环境缺工具时停止。撤销只移出该单项入口，新开会话，不删除测试输入或其他 Skill。

[固定来源、MIT 与验证命令副作用说明](skills.md#obra--verification-before-completion)。这个规则不会创建不可绕过的程序门禁。

<a id="security-threat-model"></a>
## 案例四：只读分析一个虚构应用的风险

**目标与准备：**开发者为极小的文件读取应用写威胁模型，不运行服务、网络请求或攻击。需要已可用的 Codex 与源码读取/报告写入能力，无需安装 Web 框架。

**获取与配置：**在[固定 OpenAI 快照 ZIP](https://github.com/openai/skills/archive/49f948faa9258a0c61caceaf225e179651397431.zip)中找到 `skills/.curated/security-threat-model/`，保留整个目标目录，尤其 `references/prompt-template.md`、`references/security-controls-and-assets.md` 和目录 `LICENSE.txt`；不安装其他 Skill。放到 `.agents/skills/security-threat-model/`，同名则停。按[Codex 路径](client-guides.md#codex-app)打开项目并选择它。

**输入：**在新练习项目 `notes-demo` 根目录新建 `app.py`（本教程原创、只读分析）：

```python
from pathlib import Path

ROOT = Path("notes")

def read_note(user_supplied_name):
    return (ROOT / user_supplied_name).read_text(encoding="utf-8")
```

```text
请用已选择的 security-threat-model，只读分析当前 notes-demo 项目的 app.py。
假设这是尚未部署的内部原型：将来登录用户可提交文件名，没有管理员权限；
只允许读取 notes 目录中的文本，目录之外不允许访问。当前代码没有展示鉴权层。
不要运行代码、访问 notes 以外真实文件、做漏洞利用或修改源码。
先按 Skill 要求提出需要确认的上下文与假设；收到我确认后再写威胁模型。
输出文件已存在就停止，不覆盖；不要编造已有的鉴权或防护。
```

**后续回复草案：**AI 提出澄清后，用户按实际提问确认“仅此虚构场景；尚未部署；登录层未实现；目录外文件不可读；无其他代码”。不能预先代替真实用户确认；这一步是上游流程的一部分。

**预期与检查：**看到入口与必要参考模板的读取；区分源码事实与假设；识别文件路径越界风险以及缺失的访问控制证据；给出缓解建议和条件，不执行攻击。按上游命名应写 `notes-demo-threat-model.md`，现有文件不覆盖。可手工核对引用是否真的指向 `app.py`，不能用“发现一个风险”推定完整审计。本轮未创建或运行此应用，也未生成真实威胁报告。

**失败与撤销：**不澄清直接编造部署信息、访问真实系统文件、自动修代码或把报告当安全认证都不符合本例。缺模板先补齐同版本资源，不升级；撤销只移出本次单项入口，不删除源码或用户报告。

[固定来源、Apache-2.0 与能力边界](skills.md#openai--security-threat-model)。这里提供的是安全分析工作方法，不是渗透测试授权。

<a id="future-test"></a>
## 后续怎样做最小实测

须另获明确授权后，才在独立练习项目获取并添加所选 Skill。优先只实测主案例：已可用 Codex App、浏览器、纯文本编辑器、固定两个文件、虚构输入；允许范围仅本次项目文件写入与必要客户端模型请求，不改登录/全局配置。

记录操作系统、客户端版本、来源文件、实际目录、发现与加载事件、输入/输出对照、失败和撤销结果。App 菜单与选择器、热刷新、同名区分、日志显示是首要待验证点。主案例通过后，再决定是否测试其他客户端与三个进阶案例；Python 缺失不在本轮自动补装。

[返回入门](quickstart.md) · [32 项用途](usage.md) · [客户端机制与依据](client-guides.md)
