# 第一次使用 Agent Skills

这页帮你选对一个 Skill，再走到获取、添加、使用和检查。第一次只选一个，优先用独立练习文件夹。

**先选路线：**处理办公文档或数据，看[普通用户路径](#everyday)；想亲手添加 Skill 的开发者，看[Codex App 跟做案例](hands-on.md#create-readme)。不要求所有人先做编程练习。教程有官方机制依据，但仍待实际环境验证。

## 1. 先理解它能帮什么忙

你可以把 Skill 理解为交给 AI 的一份“专业工作手册”。它通常有固定步骤、判断规则，有时还有参考资料、模板或脚本。例如，排障 Skill 要求先复现问题、找证据，再改代码。

Skill 不是独立 App，也不会在添加后自动完成所有工作。你仍需要一个支持它的 AI 工具、一项明确任务，以及任务需要的文件和权限。

普通提问告诉 AI“这次要做什么”；Skill 把可复用的工作方法带进任务。两者一起使用。**只把本文的中文示例粘贴给 AI，并不代表它已加载对应 Skill。** 不是所有聊天产品都能读取电脑上的 `SKILL.md`；本教程不把本地目录方案套到普通 ChatGPT 网页聊天。

<a id="everyday"></a>
## 普通用户：先从自己的工作开始

你可以先完成选择，不需要先建项目、学终端或下载源码。

1. **说清要交付什么。** “看表格有没有缺值”和“修改 Excel 的公式/格式”需要不同能力；“把 Word 提取成文字”和“保留 Word 排版修改”也不同。
2. **点开匹配项，看使用条件。** 下表给出下一步；如果工具尚未准备好，停在这里即可，不照抄开发者的安装案例。
3. **只用你已有且获准使用的 AI 工具。** 已有能力满足任务时无需重复添加。确需新增 Skill，才转到[客户端教程](client-guides.md)；文本案例的复制方法不替代 OfficeCLI 等条目的额外工具门槛。
4. **开始时只用虚构输入或非敏感副本。** 加载所选 Skill 后使用[该项中文示例](usage.md)，要求新输出、不覆盖原件，再独立核对结果。不能确认加载时就保留“未确认”，不要把普通聊天当 Skill 成功调用。

| 你要交付什么 | 先选谁 | 接下来点击哪里 |
|---|---|---|
| 检查表格的缺失、重复和异常 | exploratory-data-analysis | [数据体检介绍](usage.md#k-dense-ai--exploratory-data-analysis)，再看[Excel 与 CSV 的区别](#excel) |
| 修改 Excel 的公式、格式或图表 | officecli-xlsx | [用途与示例](usage.md#iofficeai--officecli-xlsx) → [额外工具与版本门槛](installation.md#officecli) |
| 修改 Word 的文字、样式或页眉 | officecli-docx | [用途与示例](usage.md#iofficeai--officecli-docx)；需要固定 OfficeCLI，尚非零基础即用教程 |
| 修改 PPT 的文字、对象或图表 | officecli-pptx | [用途与示例](usage.md#iofficeai--officecli-pptx)；模板、字体和视觉结果仍须检查 |
| 把文档内容提取成文字供整理 | markitdown | [转换用途与限制](usage.md#k-dense-ai--markitdown)，不能当作原格式编辑 |
| 把已整理的数据做成静态图 | matplotlib | [绘图用途与条件](usage.md#k-dense-ai--matplotlib)，需要相应 Python 环境与字体 |

**一个不需要编程的选择例子：**你拿到一份 Excel，只想检查空值和重复，先选 EDA；它的已知核心输入是 CSV/TSV，不直接保证处理 `.xlsx`。如果还要保留公式与样式修改原生工作簿，改看 OfficeCLI XLSX 的条件；没准备好工具就先停止新增，不自行试装。如果只想了解某种专有 Office 方法，则只读[受限参考介绍](usage.md#anthropics--xlsx)。

准备好匹配工具后，可用一份手工可核对的虚构副本：两列“项目、金额”，三条记录为“甲、10”“乙、20”“乙、20”。未来验收时应能核对三条记录、一个额外完全重复记录；若你的任务包括金额汇总，手算核对值是 50。**这些是示例预期，不是本轮实测结果，也不把金额分组求和算作 EDA 原生功能。** 原生 Excel 编辑还要检查公式与格式，不能只检查数值。

你不必为了使用本库走完后面的程序排障案例。当前 Office 原生编辑尚无本项目已验证的零基础完整安装教程；这里明确给出选择与停止条件，不承诺一键添加后就能工作。

## 2. 选你已经在用的工具

| 你的工具 | 需要先具备什么 | 下一步 |
|---|---|---|
| Codex App | 可正常使用的桌面客户端、能打开本地文件夹的 Codex 会话 | [按客户端了解添加方式](client-guides.md#codex-app)；开发者可选[跟做案例](hands-on.md#create-readme) |
| Codex CLI | 已能在终端启动的 CLI、可用账号与项目文件访问权限 | [Codex CLI 操作路径](client-guides.md#codex-cli) |
| Claude Code | 已可用的客户端与账号/模型服务、一个练习项目 | [Claude Code 独立教程](client-guides.md#claude-code) |
| OpenCode | 已可用的客户端和 Provider、允许读取 Skill 的会话 | [OpenCode 独立教程](client-guides.md#opencode) |
| 其他工具 | 先确认是否支持本地 Skill、导入或插件 | [现有机制资料](clients.md) |

没有客户端？先到上述教程中的官方入口了解获取方式。不必为了一个 Skill 同时安装三个客户端；本项目也不代为安装、登录或改设置。客户端、模型调用、工具或第三方服务可能单独收费。

<a id="choose"></a>
## 3. 从需求选一个 Skill

**开发者例子：**“程序报错，我希望 AI 先找原因，不要一上来乱改。”办公与数据任务不必走此例，使用上面的[普通用户路径](#everyday)。

1. 从[首页的修复代码入口](../README.md#tasks)进入。
2. 选择 [systematic-debugging：有条理地排障](usage.md#obra--systematic-debugging)。它是工作方法，不是自动修复器。
3. 如果已会添加 Skill，进入[排障案例](hands-on.md#systematic-debugging)；第一次接触文件放置，先做[写说明书案例](hands-on.md#create-readme)，再换成排障 Skill 的完整目录。
4. 加载后发送案例中的中文任务，核对读取记录和根因证据。

<a id="excel"></a>
### 我只想处理 Excel，选哪个？

先分清“分析表格里的数据”和“编辑原生 Excel 文件”：

| 你现在的任务 | 先了解谁 | 现在可以继续到哪里 |
|---|---|---|
| 检查数据有多少行、哪里缺值、是否重复 | [exploratory-data-analysis](usage.md#k-dense-ai--exploratory-data-analysis) | 核心范围是 CSV/TSV；Excel 可先对**副本**使用“另存为 CSV UTF-8”，仅保留所选工作表的值，可能丢公式/格式。确认日期、编码和精度后再采用。需要 Python 3.11+，尚无本轮完整安装案例 |
| 修改 `.xlsx` 的公式、样式、图表或透视表 | [officecli-xlsx](usage.md#iofficeai--officecli-xlsx) | 先读[采用门槛](installation.md#officecli)；需固定工具和禁用自动安装/更新，尚无适合零基础照抄的安装教程。缺少工具或无法确认版本时先停下，不套用 EDA 教程 |
| 把已整理好的数据画成图 | [matplotlib](usage.md#k-dense-ai--matplotlib) | 需相应 Python 绘图库和字体；不自动读取任意 Excel 模板 |
| 了解 Anthropic 的 Excel 工作方法 | [xlsx（仅受限参考）](usage.md#anthropics--xlsx) | 只阅读原创介绍与上游链接，不提供外部安装或执行路线 |

如果你不懂开发，只想立即处理一个正式工作簿，这里目前提供的是**选择依据，不是一套已经验证过的 Excel 安装捷径**。可以先用自己已有的、明确支持该文件的工具；不要为试教程上传公司数据，也不要把 CSV 导出当作原文件格式保留。后续文档中的“待实测”不是你操作失败。

<a id="success"></a>
## 4. 四步确认，才算真正用上

| 检查层次 | 你要看到什么 | 单靠什么还不够 |
|---|---|---|
| 文件放对了 | 指定项目下有 `Skill名称/SKILL.md`，文件不是网页或 `.txt` | 下载过 ZIP |
| 客户端发现了 | 选择器、可用列表或工具描述中出现正确名称；来源是本次项目 | 文件夹存在 |
| 正文加载了 | 实际 Skill 调用记录，或读取本次 `SKILL.md` 的工具记录；必要资料也被读取 | AI 自称“我用了这个 Skill” |
| 结果对了 | 用案例的独立标准检查输出，原输入和已有文件受保护 | AI 给出了回答，或命令退出码为 0 |

**手动要求 AI 读一个文件只能证明文件被读，不自动证明原生 Skill 发现/选择成功。** 若客户端不展示可核查的加载过程，记录“正文加载未能确认”，不要补写成功。不同版本的 UI/日志展示待实测，详见[客户端检查方法](client-guides.md#evidence)。

<a id="faq"></a>
## 5. 遇到问题，从这里排查

| 问题 | 先做什么 |
|---|---|
| 找不到 Skill | 对照[项目目录图](client-guides.md#layout)，检查大小写、`.md.txt`、多嵌套一层、是否打开了同一个项目。不要改全局路径试运气 |
| 文件正确，AI 没调用 | 用客户端自己的选择/调用方式；Codex、Claude Code、OpenCode 的入口不同，见[独立教程](client-guides.md)。只有在实际加载后再判断效果 |
| 需要额外软件 | 查[该条目的使用条件](usage.md)；缺少依赖就记录缺口，不让 AI 默认安装全套环境 |
| 添加后效果没变化 | 分别检查发现、正文加载和任务结果。方法类 Skill 不会多出一个独立 App 或自动工具按钮 |
| 同名 Skill 已存在 | 取消复制，不点“替换”或“合并”。检查客户端显示的来源；本教程不重命名上游入口来规避冲突。无法区分就暂停 |
| 提示认证、额度、证书或代理错误 | 属于客户端/服务环境问题，先停止本次练习；本教程不要求更改登录、代理或证书来强行完成 |
| 想卸载 | 结束练习会话，只把**本次新建的单项文件夹**移出发现目录，保留到确认无误再删除；不要清空根目录。新开会话检查，不把旧对话中已加载的内容当作卸载失败 |
| Skill 要付费吗 | 原创导览的许可、上游 Skill 许可和客户端/模型费用是三件事；免费公开源码不代表所有服务或用途免费。看[许可说明](../LICENSE-NOTICE.md) |
| Windows/macOS 都能用吗 | 文本方法通常更容易迁移；路径、Shell、Python、字体和二进制支持仍需分别确认。这里没有跨系统运行通过结论 |

下一步：[普通用户选任务](#everyday) · [开发者跟做 Codex App 案例](hands-on.md#create-readme) · [浏览 32 项通俗介绍](usage.md) · [返回首页](../README.md)
