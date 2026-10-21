# 32 项 Skill：能做什么，怎么开始

这页帮你按实际问题选择，而不是要求先读技术审计。每项给出中文用途、两个场景和可复制的任务正文；固定版本、许可和完整风险留在对应详情里。

**先添加并确认加载，再用示例。** 下方中文只是任务描述，不是 Skill 调用语法。按[客户端教程](client-guides.md)选择或加载对应名称后再发送；受限参考三项只阅读介绍，不参与添加流程。

当前证据有四种：有限本地核心样例、有上游材料但未本地验证、仅静态审阅、受限参考。上游示例/测试源码/评估设计不自动表示已经通过。所有 32 项客户端端到端运行均未验证；本轮不新增运行结论。

- [办公文档](#office)
- [数据与图表](#data)
- [开发工程](#development)
- [自动化](#automation)
- [Agent 通用能力](#agent)
- [信息研究](#research)
- [安全与质量](#security)
- [前端与设计](#design)

<a id="office"></a>
## 办公文档

<a id="k-dense-ai--markitdown"></a>
### markitdown｜把文档转成可读文本

**一句话：**把文档内容提取成 Markdown，便于摘要和检索。 **适合谁：**需批量提取文档内容的技术人员。

**实际问题：**把测试 Word 提取成文本；把多种文档整理到新 Markdown 目录。

**加载后可用的任务正文：**

```text
将授权测试文档提取为新的 Markdown 文件，并列出遗漏的版式信息。
```

另一个场景可以这样问：“先检查所需格式的转换器，不安装 all、不启用云端/OCR/插件分支。”

**额外工具与限制：**需匹配 Python、MarkItDown 和所需转换器；这是 K-Dense 包装指南，不是 Microsoft 官方 Skill。不是保留 Office 版式的编辑器。

**使用状态：**只有本目录范围内静态审阅；此固定 Skill 的功能与客户端运行未验证。

**下一步：**尚未建立该项完整实操教程；先核对下方详情中的依赖与采用门槛，再决定是否采用。

**原始来源与注意事项：**[K-Dense Inc. / markitdown](https://github.com/K-Dense-AI/scientific-agent-skills/tree/593377bb048752abb0152deab9fbb1083a6087df/skills/markitdown) · [MIT](https://github.com/K-Dense-AI/scientific-agent-skills/blob/593377bb048752abb0152deab9fbb1083a6087df/LICENSE.md) · [版本、依赖与完整风险](skills.md#k-dense-ai--markitdown)。

<a id="openai--pdf"></a>
### pdf (OpenAI)｜生成并检查 PDF

**一句话：**组织 PDF 提取、生成、页面渲染和视觉校对。 **适合谁：**需要 PDF 工作流的文档人员或开发者。

**实际问题：**提取测试 PDF 的文字；生成并渲染检查新 PDF。

**加载后可用的任务正文：**

```text
从测试 PDF 提取文字，说明扫描页和布局识别的限制，不修改原件。
```

另一个场景可以这样问：“在新路径生成示例 PDF，并明确页面是否实际渲染、是否检查截断与重叠。”

**额外工具与限制：**按任务准备 PDF 库、Poppler 与字体。此固定 GitHub 版本未运行；文字可提取不证明页面排版正确。

**使用状态：**只有本目录范围内静态审阅；此固定 Skill 的功能与客户端运行未验证。

**下一步：**尚未建立该项完整实操教程；先核对下方详情中的依赖与采用门槛，再决定是否采用。

**原始来源与注意事项：**[OpenAI / pdf](https://github.com/openai/skills/tree/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/pdf) · [Apache-2.0](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/pdf/LICENSE.txt) · [版本、依赖与完整风险](skills.md#openai--pdf)。

<a id="iofficeai--officecli-docx"></a>
### officecli-docx｜用命令工具修改 Word

**一句话：**用 OfficeCLI 定点修改 Word 文本、样式和文档对象。 **适合谁：**愿意核对工具版本和文档结果的办公技术人员。

**实际问题：**修改副本文本样式；调整页眉页脚与表格。

**加载后可用的任务正文：**

```text
先核 OfficeCLI 版本及自动安装/更新控制，再为测试 Word 副本提出修改计划。
```

另一个场景可以这样问：“修改后独立检查字体、分页、字段与输出路径，不声称任意模板无损。”

**额外工具与限制：**需固定 OfficeCLI 平台工具及查看器/字体；必须满足专门采用门槛。源与发行实现不同，未测格式保真，不是即装即用。

**使用状态：**有上游底层 CLI 的限定 DOCX smoke 成功记录，非此格式 Skill 功能通过；本地与客户端未验证。

**下一步：**尚未建立该项完整教程；先读 [OfficeCLI 采用门槛](installation.md#officecli)，不能直接照抄文本 Skill 案例。

**原始来源与注意事项：**[iOfficeAI 原始维护仓库 / officecli-docx](https://github.com/iOfficeAI/OfficeCLI/tree/fb98e593612dee2cec36847666671dba502e60aa/skills/officecli-docx) · [Apache-2.0](https://github.com/iOfficeAI/OfficeCLI/blob/fb98e593612dee2cec36847666671dba502e60aa/LICENSE) · [版本、依赖与完整风险](skills.md#iofficeai--officecli-docx)。

<a id="iofficeai--officecli-xlsx"></a>
### officecli-xlsx｜用命令工具修改 Excel

**一句话：**编辑工作簿中的单元格、公式、样式和原生图表。 **适合谁：**能独立核对公式与数据的办公技术人员。

**实际问题：**更新虚构表格公式；调整图表或透视对象。

**加载后可用的任务正文：**

```text
先满足 OfficeCLI 采用门槛，为测试副本的公式与图表制定操作和核对计划。
```

另一个场景可以这样问：“独立检查公式字符串和关键数值，不把内置计算当完整 Excel 引擎，不覆盖原模板。”

**额外工具与限制：**需固定 OfficeCLI；复杂公式、宏、外链和缓存须另验。尚无零基础完整安装案例，普通 EDA 不能代替它。

**使用状态：**有上游底层 CLI 的限定 DOCX smoke 成功记录，非此格式 Skill 功能通过；本地与客户端未验证。

**下一步：**尚未建立该项完整教程；先读 [OfficeCLI 采用门槛](installation.md#officecli)，不能直接照抄文本 Skill 案例。

**原始来源与注意事项：**[iOfficeAI 原始维护仓库 / officecli-xlsx](https://github.com/iOfficeAI/OfficeCLI/tree/fb98e593612dee2cec36847666671dba502e60aa/skills/officecli-xlsx) · [Apache-2.0](https://github.com/iOfficeAI/OfficeCLI/blob/fb98e593612dee2cec36847666671dba502e60aa/LICENSE) · [版本、依赖与完整风险](skills.md#iofficeai--officecli-xlsx)。

<a id="iofficeai--officecli-pptx"></a>
### officecli-pptx｜用命令工具修改 PPT

**一句话：**对幻灯片、形状、文本和原生图表进行对象级编辑。 **适合谁：**能检查版式与模板的办公技术人员。

**实际问题：**改副本的文字图表；在已有主题中调整对象。

**加载后可用的任务正文：**

```text
先满足 OfficeCLI 采用门槛，给测试演示文稿的定点修改和视觉核对计划。
```

另一个场景可以这样问：“保留主题、母版和字体要求，写新输出；没有渲染就不要声称布局已检查。”

**额外工具与限制：**需固定 OfficeCLI 以及字体/目标查看器。动画、复杂母版和格式保真未实测；不自动安装或更新工具。

**使用状态：**有上游底层 CLI 的限定 DOCX smoke 成功记录，非此格式 Skill 功能通过；本地与客户端未验证。

**下一步：**尚未建立该项完整教程；先读 [OfficeCLI 采用门槛](installation.md#officecli)，不能直接照抄文本 Skill 案例。

**原始来源与注意事项：**[iOfficeAI 原始维护仓库 / officecli-pptx](https://github.com/iOfficeAI/OfficeCLI/tree/fb98e593612dee2cec36847666671dba502e60aa/skills/officecli-pptx) · [Apache-2.0](https://github.com/iOfficeAI/OfficeCLI/blob/fb98e593612dee2cec36847666671dba502e60aa/LICENSE) · [版本、依赖与完整风险](skills.md#iofficeai--officecli-pptx)。

<a id="anthropics--docx"></a>
### docx (Anthropic)｜了解 Anthropic 的 Word 方法（受限参考）

**一句话：**了解 Word 创建、批注和修订流程及其适用边界。 **适合谁：**比较 Office 处理方法的读者。

**实际问题：**了解新建与 OOXML 编辑区别；比较批注与修订流程。

**仅供了解方法的提问（不调用或执行源材料）：**

```text
仅介绍此 Word 方法的用途、批注/修订路径和许可限制，提供原始链接。
```

另一个场景可以这样问：“仅比较其与 OfficeCLI 的任务差异，不下载、复制或执行任何上游材料。”

**额外工具与限制：**仅供受限参考；实际使用取决于适用服务合同，不提供外部安装/执行路线或源码包。

**使用状态：**仅供受限参考；只有静态资料，不提供安装方案，未做功能或客户端运行。

**下一步：**只读原始来源与许可；不提供安装/执行教程。

**原始来源与注意事项：**[anthropics 原始维护仓库 / docx](https://github.com/anthropics/skills/tree/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/docx) · [Proprietary](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/docx/LICENSE.txt) · [版本、依赖与完整风险](skills.md#anthropics--docx)。

<a id="anthropics--xlsx"></a>
### xlsx (Anthropic)｜了解 Anthropic 的 Excel 方法（受限参考）

**一句话：**了解工作簿公式缓存、重算和数据核查的不同环节。 **适合谁：**比较 Excel 技术路线的读者。

**实际问题：**了解重算与结果正确的区别；比较公式与缓存限制。

**仅供了解方法的提问（不调用或执行源材料）：**

```text
仅说明该方法的公式缓存、重算与数值核对边界，提供原始资料链接。
```

另一个场景可以这样问：“仅比较 OfficeCLI 与该方法的外链、宏和保存风险，不提取或运行材料。”

**额外工具与限制：**专有许可与服务合同适用；仅供受限参考，不因收录而获得下载、改编、商业执行或再分发权。

**使用状态：**仅供受限参考；只有静态资料，不提供安装方案，未做功能或客户端运行。

**下一步：**只读原始来源与许可；不提供安装/执行教程。

**原始来源与注意事项：**[anthropics 原始维护仓库 / xlsx](https://github.com/anthropics/skills/tree/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/xlsx) · [Proprietary](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/xlsx/LICENSE.txt) · [版本、依赖与完整风险](skills.md#anthropics--xlsx)。

<a id="anthropics--pptx"></a>
### pptx (Anthropic)｜了解 Anthropic 的 PPT 方法（受限参考）

**一句话：**了解程序化新建与已有模板编辑的不同流程。 **适合谁：**比较演示文稿方法的读者。

**实际问题：**了解新建与模板包编辑区别；了解结构与视觉校验各检查什么。

**仅供了解方法的提问（不调用或执行源材料）：**

```text
只介绍原始 PPT 方法的新建、模板编辑与视觉检查区别，附原始链接。
```

另一个场景可以这样问：“仅比较它与 OfficeCLI 对象编辑的适用场景，不复制脚本、模板或资产。”

**额外工具与限制：**仅供受限参考；不提供跨客户端安装执行路线，服务合同和素材/字体条款须独立确认。

**使用状态：**仅供受限参考；只有静态资料，不提供安装方案，未做功能或客户端运行。

**下一步：**只读原始来源与许可；不提供安装/执行教程。

**原始来源与注意事项：**[anthropics 原始维护仓库 / pptx](https://github.com/anthropics/skills/tree/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/pptx) · [Proprietary](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/pptx/LICENSE.txt) · [版本、依赖与完整风险](skills.md#anthropics--pptx)。

<a id="data"></a>
## 数据与图表

<a id="k-dense-ai--exploratory-data-analysis"></a>
### exploratory-data-analysis｜数据体检

**一句话：**先看清表格的缺失、重复和异常，再决定怎么分析。 **适合谁：**需要检查小型数据表的数据分析人员。

**实际问题：**检查 CSV 的缺失和重复；比较 TSV 数值分布是否受极端值影响。

**加载后可用的任务正文：**

```text
检查 sample.csv 的行列、缺失、重复和数值异常，把报告写到新文件，保留原数据。
```

另一个场景可以这样问：“只检查 sample.json 的结构，严格处理重复键或错误输入，不把它当原生 Excel 统计。”

**额外工具与限制：**需 Python 3.11+；已知小样例仅限标准库核心。不会原生处理任意 XLSX 模板，分组求和不是该核心功能。

**使用状态：**已有有限本地核心合成样例记录（16 次调用、41 项核对）；非完整 Skill/Excel/大文件验证；客户端未验证。

**下一步：**尚未建立该项完整实操教程；先核对下方详情中的依赖与采用门槛，再决定是否采用。

**原始来源与注意事项：**[K-Dense Inc. / exploratory-data-analysis](https://github.com/K-Dense-AI/scientific-agent-skills/tree/593377bb048752abb0152deab9fbb1083a6087df/skills/exploratory-data-analysis) · [MIT](https://github.com/K-Dense-AI/scientific-agent-skills/blob/593377bb048752abb0152deab9fbb1083a6087df/LICENSE.md) · [版本、依赖与完整风险](skills.md#k-dense-ai--exploratory-data-analysis)。

<a id="k-dense-ai--matplotlib"></a>
### matplotlib｜把数据画成图

**一句话：**指导创建静态图表并导出图片或矢量文件。 **适合谁：**有 Python 环境的数据人员。

**实际问题：**给整理好的数据画柱状图；调整图例并导出 SVG。

**加载后可用的任务正文：**

```text
对给定虚构汇总数据画柱状图，先核对数值，再写到新的 PNG 文件。
```

另一个场景可以这样问：“检查图上的字体、单位、图例和坐标，不覆盖已有图片，不声称未做过的视觉检查。”

**额外工具与限制：**需 Python/Matplotlib，部分脚本另需 NumPy/SciPy/cycler。字体、渲染和可选依赖未验证；保存图片可能覆盖旧文件。

**使用状态：**只有本目录范围内静态审阅；此固定 Skill 的功能与客户端运行未验证。

**下一步：**尚未建立该项完整实操教程；先核对下方详情中的依赖与采用门槛，再决定是否采用。

**原始来源与注意事项：**[K-Dense Inc. / matplotlib](https://github.com/K-Dense-AI/scientific-agent-skills/tree/593377bb048752abb0152deab9fbb1083a6087df/skills/matplotlib) · [MIT](https://github.com/K-Dense-AI/scientific-agent-skills/blob/593377bb048752abb0152deab9fbb1083a6087df/LICENSE.md) · [版本、依赖与完整风险](skills.md#k-dense-ai--matplotlib)。

<a id="openai--jupyter-notebook"></a>
### jupyter-notebook｜整理可复现的分析笔记

**一句话：**帮助建立或整理包含说明与代码的 notebook。 **适合谁：**使用 Jupyter 的数据人员与研究者。

**实际问题：**创建实验记录；把演示整理成教学 notebook。

**加载后可用的任务正文：**

```text
先选实验或教程模板，为虚构数据写 notebook 结构；明确输出到新路径。
```

另一个场景可以这样问：“核对 Markdown、代码与内核依赖，未执行的单元不声称运行通过。”

**额外工具与限制：**脚手架需 Python，执行另需内核及项目依赖；上游 CODEX_HOME 路径需适配，不自动 force 或执行不可信单元。

**使用状态：**只有本目录范围内静态审阅；此固定 Skill 的功能与客户端运行未验证。

**下一步：**尚未建立该项完整实操教程；先核对下方详情中的依赖与采用门槛，再决定是否采用。

**原始来源与注意事项：**[openai 原始维护仓库 / jupyter-notebook](https://github.com/openai/skills/tree/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/jupyter-notebook) · [Apache-2.0](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/jupyter-notebook/LICENSE.txt) · [版本、依赖与完整风险](skills.md#openai--jupyter-notebook)。

<a id="development"></a>
## 开发工程

<a id="obra--systematic-debugging"></a>
### systematic-debugging｜有条理地排障

**一句话：**帮助 AI 先找到错误原因，再提出最小修复。 **适合谁：**能读基本代码的开发者。

**实际问题：**复现断言失败；根据日志追踪错误来源。

**加载后可用的任务正文：**

```text
先复现练习代码的错误，给出根因证据和最小方案，等我确认后再修改。
```

另一个场景可以这样问：“对比能正常运行与失败的路径，只检验一个假设，不顺手重构。”

**额外工具与限制：**文本核心无需新包；运行复现要用项目已有工具。不自动执行附带脚本或补装 Superpowers。

**使用状态：**只有本目录范围内静态审阅；此固定 Skill 的功能与客户端运行未验证。

**下一步：**[完整练习草案](hands-on.md#systematic-debugging)（待实测）。

**原始来源与注意事项：**[obra / Superpowers 项目 / systematic-debugging](https://github.com/obra/superpowers/tree/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/systematic-debugging) · [MIT](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/LICENSE) · [版本、依赖与完整风险](skills.md#obra--systematic-debugging)。

<a id="openai--gh-fix-ci"></a>
### gh-fix-ci｜排查 GitHub 自动检查失败

**一句话：**读取 GitHub Actions 的失败日志，提出修复方案。 **适合谁：**已有 GitHub 项目权限的开发者。

**实际问题：**解释 PR 的失败检查；区分外部 CI 与 Actions 故障。

**加载后可用的任务正文：**

```text
只读检查指定 PR 的 GitHub Actions 失败日志，先给证据与修复计划，不改代码。
```

另一个场景可以这样问：“区分脚本查到失败时的非零返回与工具崩溃；外部 CI 只列详情链接。”

**额外工具与限制：**需 Git、已授权 gh、Python 与网络；不自动登录。它不是覆盖所有 CI 的通用修复器，改代码需授权。

**使用状态：**只有本目录范围内静态审阅；此固定 Skill 的功能与客户端运行未验证。

**下一步：**尚未建立该项完整实操教程；先核对下方详情中的依赖与采用门槛，再决定是否采用。

**原始来源与注意事项：**[OpenAI / gh-fix-ci](https://github.com/openai/skills/tree/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/gh-fix-ci) · [Apache-2.0](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/gh-fix-ci/LICENSE.txt) · [版本、依赖与完整风险](skills.md#openai--gh-fix-ci)。

<a id="github--create-readme"></a>
### create-readme｜给项目写说明书

**一句话：**把项目事实整理成别人能照着使用的 README。 **适合谁：**项目作者、初级开发者、开源文档贡献者。

**实际问题：**为小项目写入门说明；补全现有文档的使用路径。

**加载后可用的任务正文：**

```text
只根据 project-notes.md 新建中文 README.md，不联网、不覆盖已有文件。
```

另一个场景可以这样问：“把已有说明中的已知功能与待确认事项分开，不编造安装或运行结果。”

**额外工具与限制：**纯文本核心不需额外软件；只读取授权项目。上游远端范例会变化，本教程禁止默认联网或扫描无关工作区。

**使用状态：**只有本目录范围内静态审阅；此固定 Skill 的功能与客户端运行未验证。

**下一步：**[完整练习草案](hands-on.md#create-readme)（待实测）。

**原始来源与注意事项：**[GitHub awesome-copilot 社区贡献者 / create-readme](https://github.com/github/awesome-copilot/tree/613efc8c21d9b3ce642dff361d17006cd9967e28/skills/create-readme) · [MIT](https://github.com/github/awesome-copilot/blob/613efc8c21d9b3ce642dff361d17006cd9967e28/LICENSE) · [版本、依赖与完整风险](skills.md#github--create-readme)。

<a id="trailofbits--property-based-testing"></a>
### property-based-testing｜用通用性质设计测试

**一句话：**帮助发现只靠少量固定例子容易漏掉的输入问题。 **适合谁：**已有测试环境的开发者。

**实际问题：**检查编码解码可逆；检查排序和归一化的不变量。

**加载后可用的任务正文：**

```text
为这个函数提出性质、生成器与边界用例，避免与实现同义反复的断言。
```

另一个场景可以这样问：“使用项目已有测试框架提出最小方案，不自动修改依赖清单，说明运行预算。”

**额外工具与限制：**按语言使用项目已有框架；不强制新装 Hypothesis 等包。运行测试会执行项目代码，上游评估设计不等于通过记录。

**使用状态：**有上游材料，但未进行本地验证；材料类型与范围见详情，不表示上游或客户端测试通过。

**下一步：**尚未建立该项完整实操教程；先核对下方详情中的依赖与采用门槛，再决定是否采用。

**原始来源与注意事项：**[trailofbits 原始维护仓库 / property-based-testing](https://github.com/trailofbits/skills/tree/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/plugins/property-based-testing/skills/property-based-testing) · [CC-BY-SA-4.0](https://github.com/trailofbits/skills/blob/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/LICENSE) · [版本、依赖与完整风险](skills.md#trailofbits--property-based-testing)。

<a id="automation"></a>
## 自动化

<a id="microsoft--playwright-cli"></a>
### playwright-cli｜让 AI 操作测试网页

**一句话：**通过浏览器命令工具操作页面并收集截图、日志。 **适合谁：**有测试环境的开发者和测试人员。

**实际问题：**测试本地表单；记录点击后的页面与控制台变化。

**加载后可用的任务正文：**

```text
先确认 Skill 与 CLI 版本配套，再对本地虚构表单提出点击、断言和截图计划。
```

另一个场景可以这样问：“只设计临时浏览器会话的验证步骤，不登录生产账号或提交真实订单。”

**额外工具与限制：**需要 Node、配套 CLI 和浏览器。当前固定 Skill 与候选 CLI 尚未形成验证过的配对；本页不提供直接安装路线。

**使用状态：**只有本目录范围内静态审阅；此固定 Skill 的功能与客户端运行未验证。

**下一步：**尚未建立该项完整实操教程；先核对下方详情中的依赖与采用门槛，再决定是否采用。

**原始来源与注意事项：**[Microsoft / Playwright CLI 项目 / playwright-cli](https://github.com/microsoft/playwright-cli/tree/b1a5903c5b633b8c9f843ad7b629c2a78437040c/skills/playwright-cli) · [Apache-2.0](https://github.com/microsoft/playwright-cli/blob/b1a5903c5b633b8c9f843ad7b629c2a78437040c/LICENSE) · [版本、依赖与完整风险](skills.md#microsoft--playwright-cli)。

<a id="agent"></a>
## Agent 通用能力

<a id="anthropics--mcp-builder"></a>
### mcp-builder｜为 AI 设计工具接口

**一句话：**指导开发者把明确的 API 能力设计成 MCP 工具。 **适合谁：**已有 API 需求的开发者。

**实际问题：**设计只读查询工具；为错误返回编写评估方案。

**加载后可用的任务正文：**

```text
基于这个已授权 API 说明设计只读 MCP 工具契约，先给接口与错误处理方案。
```

另一个场景可以这样问：“列出需要固定的 SDK、权限和评估输入，不启动服务或索取真实密钥。”

**额外工具与限制：**阅读无需新包；实现需要所选 SDK 和 API 授权。它不是现成连接器；浮动 SDK 示例不是依赖锁。

**使用状态：**只有本目录范围内静态审阅；此固定 Skill 的功能与客户端运行未验证。

**下一步：**尚未建立该项完整实操教程；先核对下方详情中的依赖与采用门槛，再决定是否采用。

**原始来源与注意事项：**[Anthropic / mcp-builder](https://github.com/anthropics/skills/tree/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/mcp-builder) · [Apache-2.0](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/mcp-builder/LICENSE.txt) · [版本、依赖与完整风险](skills.md#anthropics--mcp-builder)。

<a id="openai--skill-creator"></a>
### skill-creator (OpenAI)｜编写自己的 Skill

**一句话：**把重复工作整理成小而清楚的工作步骤与资源。 **适合谁：**希望维护个人工作方法的技术用户。

**实际问题：**设计 Skill 的调用条件；拆分长规则与按需参考资料。

**加载后可用的任务正文：**

```text
为一个虚构工作流程设计 SKILL.md 的范围、触发条件与资源布局，先给草案。
```

另一个场景可以这样问：“检查指南中的绝对路径与客户端工具名，提出迁移点，不修改已有 Skill。”

**额外工具与限制：**阅读无需新包；辅助脚本可能需 Python/PyYAML。固定验证器会误拒部分合法字段，不是开放标准的唯一判据。

**使用状态：**只有本目录范围内静态审阅；此固定 Skill 的功能与客户端运行未验证。

**下一步：**尚未建立该项完整实操教程；先核对下方详情中的依赖与采用门槛，再决定是否采用。

**原始来源与注意事项：**[OpenAI / skill-creator](https://github.com/openai/skills/tree/49f948faa9258a0c61caceaf225e179651397431/skills/.system/skill-creator) · [Apache-2.0](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.system/skill-creator/LICENSE.txt) · [版本、依赖与完整风险](skills.md#openai--skill-creator)。

<a id="obra--verification-before-completion"></a>
### verification-before-completion｜完成前先看证据

**一句话：**提醒 AI 在说完成前核对真实检查与结果。 **适合谁：**需要明确验收结论的开发者或交付负责人。

**实际问题：**核对测试到底运行没；区分已改代码与问题已解决。

**加载后可用的任务正文：**

```text
先列明交付标准，再用本项目已允许的检查给证据；没执行就写未验证。
```

另一个场景可以这样问：“如果检查失败，请如实报告，不把旧日志或命令退出 0 当作所有目标通过。”

**额外工具与限制：**文本核心无新包；检查工具来自项目。验证命令可能有副作用，它不是不可绕过的自动门禁。

**使用状态：**只有本目录范围内静态审阅；此固定 Skill 的功能与客户端运行未验证。

**下一步：**[完整练习草案](hands-on.md#verification-before-completion)（待实测）。

**原始来源与注意事项：**[obra / Superpowers 项目 / verification-before-completion](https://github.com/obra/superpowers/tree/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/verification-before-completion) · [MIT](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/LICENSE) · [版本、依赖与完整风险](skills.md#obra--verification-before-completion)。

<a id="github--agent-architecture"></a>
### agent-architecture｜设计 AI Agent 的工作结构

**一句话：**先讲清任务、失效代价和控制边界，再选架构。 **适合谁：**准备开发 Agent 的工程人员。

**实际问题：**确定是否需要多 Agent；设计工具权限与验收契约。

**加载后可用的任务正文：**

```text
为虚构客服 Agent 做只含 Markdown 的架构方案，先明确需求、失败代价与验证标准。
```

另一个场景可以这样问：“比较单 Agent 与工作流分工，不部署、不训练，不把评估设计写成实测结果。”

**额外工具与限制：**文本方案无需新服务；默认 PDF/可视化另需工具，可明确要求仅文本。资料多，成本与长期有效性待验证。

**使用状态：**有上游材料，但未进行本地验证；材料类型与范围见详情，不表示上游或客户端测试通过。

**下一步：**尚未建立该项完整实操教程；先核对下方详情中的依赖与采用门槛，再决定是否采用。

**原始来源与注意事项：**[Stanislav Bankovskii；github/awesome-copilot 社区贡献 / agent-architecture](https://github.com/github/awesome-copilot/tree/613efc8c21d9b3ce642dff361d17006cd9967e28/skills/agent-architecture) · [MIT](https://github.com/github/awesome-copilot/blob/613efc8c21d9b3ce642dff361d17006cd9967e28/skills/agent-architecture/LICENSE.txt) · [版本、依赖与完整风险](skills.md#github--agent-architecture)。

<a id="research"></a>
## 信息研究

<a id="huggingface--huggingface-papers"></a>
### huggingface-papers｜读取 AI 论文资料

**一句话：**从论文标识获取论文内容与相关结构信息。 **适合谁：**主要阅读 AI/计算机论文的研究者。

**实际问题：**读取指定论文 Markdown；整理作者和相关模型/数据链接。

**加载后可用的任务正文：**

```text
只读获取指定公开论文的内容，区分论文原文与我的总结，保留来源。
```

另一个场景可以这样问：“列出论文关联信息和未确认项，不调用作者认领、索引或修改链接等写端点。”

**额外工具与限制：**需 HTTP/curl 或等效读取能力；公共读取不先索取令牌。不是综合文献检索或事实核查系统，论文许可独立。

**使用状态：**只有本目录范围内静态审阅；此固定 Skill 的功能与客户端运行未验证。

**下一步：**尚未建立该项完整实操教程；先核对下方详情中的依赖与采用门槛，再决定是否采用。

**原始来源与注意事项：**[huggingface 原始维护仓库 / huggingface-papers](https://github.com/huggingface/skills/tree/c3ff942be3e07116b475253f0a8fc4f54682c1a8/skills/huggingface-papers) · [Apache-2.0](https://github.com/huggingface/skills/blob/c3ff942be3e07116b475253f0a8fc4f54682c1a8/LICENSE) · [版本、依赖与完整风险](skills.md#huggingface--huggingface-papers)。

<a id="security"></a>
## 安全与质量

<a id="openai--security-best-practices"></a>
### security-best-practices｜检查常见代码安全问题

**一句话：**按所支持语言和框架检查常见安全做法。 **适合谁：**维护 Python、JS/TS 或 Go 项目的开发者。

**实际问题：**审查输入处理；检查会话与配置的安全做法。

**加载后可用的任务正文：**

```text
只读审查授权模块的安全问题，按支持语言加载参考资料，给出代码位置和条件。
```

另一个场景可以这样问：“区分已确认问题与一般建议，不自动修复，也不把模型审阅当完整漏洞认证。”

**额外工具与限制：**需源码及框架信息；覆盖语言/框架有限。修改代码、运行扫描或扩大范围另需授权。

**使用状态：**只有本目录范围内静态审阅；此固定 Skill 的功能与客户端运行未验证。

**下一步：**尚未建立该项完整实操教程；先核对下方详情中的依赖与采用门槛，再决定是否采用。

**原始来源与注意事项：**[openai 原始维护仓库 / security-best-practices](https://github.com/openai/skills/tree/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/security-best-practices) · [Apache-2.0](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/security-best-practices/LICENSE.txt) · [版本、依赖与完整风险](skills.md#openai--security-best-practices)。

<a id="openai--security-threat-model"></a>
### security-threat-model｜画清应用面临的安全风险

**一句话：**从源码和架构识别资产、信任边界与攻击路径。 **适合谁：**了解应用基本架构的开发者与安全人员。

**实际问题：**梳理上传接口风险；分析不同用户间的数据隔离。

**加载后可用的任务正文：**

```text
为虚构应用做威胁建模，先核对假设与部署场景，再写有源码依据的报告。
```

另一个场景可以这样问：“只读列出入口、资产和防护缺口，不做攻击、不修代码，不编造已有控制。”

**额外工具与限制：**文本与源码读取即可；需人工澄清上下文并等待确认。它不是漏洞利用工具或无漏洞证明。

**使用状态：**只有本目录范围内静态审阅；此固定 Skill 的功能与客户端运行未验证。

**下一步：**[完整练习草案](hands-on.md#security-threat-model)（待实测）。

**原始来源与注意事项：**[openai 原始维护仓库 / security-threat-model](https://github.com/openai/skills/tree/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/security-threat-model) · [Apache-2.0](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/security-threat-model/LICENSE.txt) · [版本、依赖与完整风险](skills.md#openai--security-threat-model)。

<a id="trailofbits--differential-review"></a>
### differential-review｜重点审查代码变更的安全影响

**一句话：**围绕一次 diff 找出变化引入的风险与影响范围。 **适合谁：**能理解 Git 变更的开发者和安全审查者。

**实际问题：**审查鉴权改动；追踪补丁对调用方的影响。

**加载后可用的任务正文：**

```text
对指定本地 diff 做只读安全审查，给出基线、风险条件和代码证据。
```

另一个场景可以这样问：“区分已知行为和改动影响，不运行被审构建或自动创建 issue、启用可选子代理。”

**额外工具与限制：**需 Git 与历史/源码；要有明确比较基线。插件集成不是独立核心必需条件，安全结论仍需复核。

**使用状态：**只有本目录范围内静态审阅；此固定 Skill 的功能与客户端运行未验证。

**下一步：**尚未建立该项完整实操教程；先核对下方详情中的依赖与采用门槛，再决定是否采用。

**原始来源与注意事项：**[trailofbits 原始维护仓库 / differential-review](https://github.com/trailofbits/skills/tree/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/plugins/differential-review/skills/differential-review) · [CC-BY-SA-4.0](https://github.com/trailofbits/skills/blob/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/LICENSE) · [版本、依赖与完整风险](skills.md#trailofbits--differential-review)。

<a id="trailofbits--codeql"></a>
### codeql｜规划和检查 CodeQL 扫描

**一句话：**指导数据库构建、查询选择及扫描结果质量核对。 **适合谁：**有受控扫描环境的安全工程师。

**实际问题：**为已授权代码选择查询；检查数据库提取不完整的原因。

**加载后可用的任务正文：**

```text
先核查 CodeQL 许可、查询包版本和构建风险，提出隔离扫描方案，不运行构建。
```

另一个场景可以这样问：“说明空结果与数据库缺失的区别，保留无法验证项，不推定没有漏洞。”

**额外工具与限制：**依赖 CodeQL CLI、工具链等；许可独立，私有项目需有效授权。构建会执行项目代码，必须另获批准并隔离。

**使用状态：**有上游材料，但未进行本地验证；材料类型与范围见详情，不表示上游或客户端测试通过。

**下一步：**尚未建立该项完整实操教程；先核对下方详情中的依赖与采用门槛，再决定是否采用。

**原始来源与注意事项：**[trailofbits 原始维护仓库 / codeql](https://github.com/trailofbits/skills/tree/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/plugins/static-analysis/skills/codeql) · [CC-BY-SA-4.0](https://github.com/trailofbits/skills/blob/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/LICENSE) · [版本、依赖与完整风险](skills.md#trailofbits--codeql)。

<a id="trailofbits--supply-chain-risk-auditor"></a>
### supply-chain-risk-auditor｜检查软件依赖的风险信号

**一句话：**从支持的依赖清单查看公告、维护和安装脚本等信号。 **适合谁：**可判断依赖信息披露范围的开发者和安全人员。

**实际问题：**查看公开项目的依赖公告；梳理维护集中与废弃风险。

**加载后可用的任务正文：**

```text
先确认依赖包名和版本允许外发，再规划只读检查，私有包元数据不联网发送。
```

另一个场景可以这样问：“报告公告和数据缺口，不把未找到记录当作安全，也不输出 gh 令牌。”

**额外工具与限制：**需 Python/uv、相应网络源，部分路径用已授权 gh。并非所有锁文件都支持，也不是许可证合规审计。

**使用状态：**有上游材料，但未进行本地验证；材料类型与范围见详情，不表示上游或客户端测试通过。

**下一步：**尚未建立该项完整实操教程；先核对下方详情中的依赖与采用门槛，再决定是否采用。

**原始来源与注意事项：**[trailofbits 原始维护仓库 / supply-chain-risk-auditor](https://github.com/trailofbits/skills/tree/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/plugins/supply-chain-risk-auditor/skills/supply-chain-risk-auditor) · [CC-BY-SA-4.0](https://github.com/trailofbits/skills/blob/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/LICENSE) · [版本、依赖与完整风险](skills.md#trailofbits--supply-chain-risk-auditor)。

<a id="trailofbits--agentic-actions-auditor"></a>
### agentic-actions-auditor｜检查 AI 自动工作流的输入与权限

**一句话：**追踪 GitHub Actions 中不可信内容进入 Agent 的路径。 **适合谁：**维护 AI CI 工作流的开发者与安全人员。

**实际问题：**检查 PR 文本如何进入提示词；追踪工具命令与令牌权限。

**加载后可用的任务正文：**

```text
只读分析指定 Actions 工作流，标出外部输入到 AI 提示词、命令和权限的路径。
```

另一个场景可以这样问：“把攻击示例当检测对象而非执行指令，不运行工作流、不改仓库设置。”

**额外工具与限制：**需 YAML/源码读取，远程模式可需 gh；{baseDir} 等引用在独立客户端可能需适配。不能保证覆盖所有供应商。

**使用状态：**只有本目录范围内静态审阅；此固定 Skill 的功能与客户端运行未验证。

**下一步：**尚未建立该项完整实操教程；先核对下方详情中的依赖与采用门槛，再决定是否采用。

**原始来源与注意事项：**[trailofbits 原始维护仓库 / agentic-actions-auditor](https://github.com/trailofbits/skills/tree/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/plugins/agentic-actions-auditor/skills/agentic-actions-auditor) · [CC-BY-SA-4.0](https://github.com/trailofbits/skills/blob/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/LICENSE) · [版本、依赖与完整风险](skills.md#trailofbits--agentic-actions-auditor)。

<a id="trailofbits--variant-analysis"></a>
### variant-analysis｜寻找同一根因的其他实例

**一句话：**从已经确认的问题出发，搜索类似但易遗漏的位置。 **适合谁：**已掌握明确漏洞根因的安全人员。

**实际问题：**查找类似漏鉴权点；从修复样例扩展搜索模式。

**加载后可用的任务正文：**

```text
基于这个已确认根因，在明确目录范围逐步查找变体，记录误报条件。
```

另一个场景可以这样问：“先用文本搜索，不自动装扫描器或启用并行框架，限制迭代次数与输出。”

**额外工具与限制：**需已确认根因；Git/搜索可做基本流程，可选扫描器需另核。不是首次漏洞发现或补丁正确性验证。

**使用状态：**只有本目录范围内静态审阅；此固定 Skill 的功能与客户端运行未验证。

**下一步：**尚未建立该项完整实操教程；先核对下方详情中的依赖与采用门槛，再决定是否采用。

**原始来源与注意事项：**[trailofbits 原始维护仓库 / variant-analysis](https://github.com/trailofbits/skills/tree/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/plugins/variant-analysis/skills/variant-analysis) · [CC-BY-SA-4.0](https://github.com/trailofbits/skills/blob/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/LICENSE) · [版本、依赖与完整风险](skills.md#trailofbits--variant-analysis)。

<a id="design"></a>
## 前端与设计

<a id="anthropics--frontend-design"></a>
### frontend-design｜设计有明确风格的网页

**一句话：**给网页建立清晰的排版、配色和视觉方向。 **适合谁：**前端开发者与设计协作人员。

**实际问题：**设计活动落地页；改善现有页面的层级和布局。

**加载后可用的任务正文：**

```text
为虚构读书活动页提出视觉方向、配色和字体层级，先说明设计选择。
```

另一个场景可以这样问：“在已授权页面范围改善布局，列出可访问性和响应式仍待检查的事项。”

**额外工具与限制：**需已有前端实现环境；视觉效果依模型和任务。不是已验证的可访问性或性能审计。

**使用状态：**只有本目录范围内静态审阅；此固定 Skill 的功能与客户端运行未验证。

**下一步：**尚未建立该项完整实操教程；先核对下方详情中的依赖与采用门槛，再决定是否采用。

**原始来源与注意事项：**[anthropics 原始维护仓库 / frontend-design](https://github.com/anthropics/skills/tree/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/frontend-design) · [Apache-2.0](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/frontend-design/LICENSE.txt) · [版本、依赖与完整风险](skills.md#anthropics--frontend-design)。

<a id="huggingface--huggingface-gradio"></a>
### huggingface-gradio｜搭建简单交互演示界面

**一句话：**用 Python Gradio 给数据或模型做可操作的演示。 **适合谁：**有 Python 环境的开发者和研究者。

**实际问题：**展示一个模型输入输出；做本地数据查看页面。

**加载后可用的任务正文：**

```text
按已有 Gradio 版本设计本地演示界面，先说明组件与依赖，不公开分享。
```

另一个场景可以这样问：“只使用虚构输入，列明服务监听地址与停止方式，不连接未授权远端模型。”

**额外工具与限制：**需 Python 与相配 Gradio；没有验证过的完整版本组合。启动服务、上传文件、分享公网链接须分别允许。

**使用状态：**只有本目录范围内静态审阅；此固定 Skill 的功能与客户端运行未验证。

**下一步：**尚未建立该项完整实操教程；先核对下方详情中的依赖与采用门槛，再决定是否采用。

**原始来源与注意事项：**[huggingface 原始维护仓库 / huggingface-gradio](https://github.com/huggingface/skills/tree/c3ff942be3e07116b475253f0a8fc4f54682c1a8/skills/huggingface-gradio) · [Apache-2.0](https://github.com/huggingface/skills/blob/c3ff942be3e07116b475253f0a8fc4f54682c1a8/LICENSE) · [版本、依赖与完整风险](skills.md#huggingface--huggingface-gradio)。

<a id="vercel-labs--react-best-practices"></a>
### vercel-react-best-practices｜检查 React 页面性能写法

**一句话：**按规则检查数据等待、打包和渲染等常见性能模式。 **适合谁：**已有 React/Next.js 项目的前端开发者。

**实际问题：**识别请求瀑布；检查不必要的大模块加载。

**加载后可用的任务正文：**

```text
只读审查授权 React 页面的数据请求和包体积问题，标出规则、位置与验证计划。
```

另一个场景可以这样问：“先确认项目 React 版本，没有基准测试就不声称提速，不自动安装建议库。”

**额外工具与限制：**需已有 React/Next.js 环境。源目录名与 Skill 名不同，引用有已知相对链接问题；MIT 与第三方材料边界保留。

**使用状态：**有上游材料，但未进行本地验证；材料类型与范围见详情，不表示上游或客户端测试通过。

**下一步：**尚未建立该项完整实操教程；先核对下方详情中的依赖与采用门槛，再决定是否采用。

**原始来源与注意事项：**[vercel-labs 原始维护仓库 / vercel-react-best-practices](https://github.com/vercel-labs/agent-skills/tree/063bee94c3f4df8453406c830b0a7df0f2860278/skills/react-best-practices) · [MIT](https://github.com/vercel-labs/agent-skills/blob/063bee94c3f4df8453406c830b0a7df0f2860278/skills/react-best-practices/SKILL.md#L4) · [版本、依赖与完整风险](skills.md#vercel-labs--react-best-practices)。

<a id="vercel-labs--composition-patterns"></a>
### vercel-composition-patterns｜整理 React 组件接口

**一句话：**减少布尔参数膨胀，设计更清楚的组件组合与状态归属。 **适合谁：**维护 React 组件库的开发者。

**实际问题：**拆分过多模式开关；明确共享状态放在哪里。

**加载后可用的任务正文：**

```text
为这个布尔参数过多的组件提出组合 API 方案，先解释兼容性再申请修改。
```

另一个场景可以这样问：“比较状态提升与组合方案，核对 React 版本，不把架构改善说成已测性能提升。”

**额外工具与限制：**需已有 React 项目；React 19 规则不直接适用旧版。入口名需适配，第三方内容不自动取得 MIT 许可。

**使用状态：**有上游材料，但未进行本地验证；材料类型与范围见详情，不表示上游或客户端测试通过。

**下一步：**尚未建立该项完整实操教程；先核对下方详情中的依赖与采用门槛，再决定是否采用。

**原始来源与注意事项：**[vercel-labs 原始维护仓库 / vercel-composition-patterns](https://github.com/vercel-labs/agent-skills/tree/063bee94c3f4df8453406c830b0a7df0f2860278/skills/composition-patterns) · [MIT](https://github.com/vercel-labs/agent-skills/blob/063bee94c3f4df8453406c830b0a7df0f2860278/skills/composition-patterns/SKILL.md#L9) · [版本、依赖与完整风险](skills.md#vercel-labs--composition-patterns)。

[返回首页](../README.md) · [不知道怎么选](quickstart.md#choose) · [同类比较](comparisons.md)
