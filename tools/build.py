#!/usr/bin/env python3
"""Build the original directory UI and Markdown cards; never downloads or runs Skills."""
import argparse
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = 'https://github.com/leilinfeng007-eng/awesome-universal-agent-skills'
H = html.escape


def load_catalog():
    return json.loads((ROOT / 'catalog.json').read_text())


def check_catalog(data):
    ids, names = set(), set()
    assert data['schema_version'] == '2.0.0'
    for s in data['skills']:
        assert s['id'] not in ids, 'duplicate id'
        assert s['name'] not in names, 'ambiguous installed name'
        ids.add(s['id']); names.add(s['name'])
        assert re.fullmatch(r'[a-z0-9-]+', s['slug'])
        assert s['category'] in data['categories']
        assert s['level'] in data['levels']
        assert re.fullmatch(r'[0-9a-f]{40}', s['upstream']['commit'])
        assert s['upstream']['commit'] in s['upstream']['directory_url']
        assert s['upstream']['commit'] in s['upstream']['skill_url']
        assert s['license']['skill_expression'] != 'Proprietary'
        assert s['validation']['cross_client_runtime'] == 'not_verified'
        assert s['detail_url'] == 'skills/' + s['slug'] + '.md'
        assert s['fetch_mode'] in {'guided', 'single_file', 'prepare_first'}
        assert s['clients'] == [c['id'] for c in data['clients']]
        assert s['prompt'] and s['prerequisites'] and s['comparison']
    assert not ids.intersection(x['id'] for x in data['archived'])


def acquisition_prompt(s, client):
    u = s['upstream']
    destination = client['directory'] + '/' + s['name'] if client['mode'] == 'folder' else '单独的新暂存文件夹/' + s['name']
    return (f'请只为当前项目准备 {s["name"]}，先不要执行它。\n'
            f'固定来源：{u["directory_url"]}\n'
            f'入口：{u["skill_url"]}\n'
            f'保留许可：{s["license"]["skill_license_url"]}\n'
            f'目标：{destination}/\n'
            '先确认当前项目路径正确，且目标目录尚不存在；已有同名项时停止，不覆盖、不合并。'
            '只获取此固定提交的目标子目录及其必要相对资源，不下载整个合集，'
            '不沿外链获取浮动 main/latest，不执行任何脚本或安装依赖。'
            '同时保留适用 LICENSE/NOTICE 与来源记录；资源或许可范围无法确定就停止并报告。'
            '不要修改登录、代理、全局配置或其他 Skill。完成后列出实际文件和未满足的条件。'
            '如果无法可靠下载完整子目录，请报告，不用猜测内容补齐。')


def source_hint(s):
    if s['id'].startswith('anthropics--'):
        return '不要下载整个 Anthropic 合集（包含其他受限材料）。只获取本项和本项许可。'
    if s['id'].startswith('vercel-labs--'):
        return '源文件夹名称与 name 不同：目标目录必须使用 ' + s['name'] + '。保留 MIT 声明和来源，第三方引用权利另核。'
    return '复制整个单项文件夹，包含 references、scripts、assets 等实际存在的子目录；不要只取 SKILL.md。'


def evidence(s):
    if s['validation']['function'] == 'local_core_sample_passed':
        return '已有有限本地核心样例记录：16 次调用、41 项数值和保护核对，仅小型合成 CSV/TSV/严格 JSON；不是全部功能或客户端测试。'
    return '当前建议依据静态材料。上游示例、测试源码或限定构建记录不等于本项本地运行通过；本项未做客户端端到端测试。'


def preflight(s):
    if s['id'].startswith('iofficeai--'):
        return ('上游指南含自动安装与更新步骤。缺工具就停止；即使已安装工具，每次调用也须先落实进程级 '
                'OFFICECLI_NO_AUTO_INSTALL=1 与 OFFICECLI_SKIP_UPDATE=1，不能只关闭 autoUpdate。'
                '固定平台工具、来源校验与写入边界未确认前，不执行 CLI、安装脚本或 Skill 刷新。'
                '目前先交付准备计划，实际配置与格式保真仍待实测。')
    if s['fetch_mode'] == 'prepare_first':
        return ('先准备工具，再考虑添加。' + s['start_note'] + ' 本页不提供自动安装或远程脚本执行指令。')
    return '可以先准备单项文件；真正运行前仍须满足上面的工具条件。准备任务和客户端步骤均按文档编写，本轮没有执行安装。'


def client_body(s,c):
    invoke=c['invoke'].replace('NAME',s['name'])
    if c['mode']=='import':
        return (f'{invoke}\n\n{c["note"]} 先把固定单项和许可放入暂存目录，在界面确认格式和资源都被保留；'
                '没有确认前不导入，也不要上传整仓库 ZIP。导入会改变客户端持久状态，由你决定是否继续。')
    target=c['directory']+'/'+s['name']
    return (f'把整个单项文件夹放到你打开的项目内 `{target}/`，入口必须是 `{target}/SKILL.md`。'
            '这是相对项目的路径，不是系统目录。\n\n'+invoke+'\n\n'+c['note'])


def card_md(s,data):
    u=s['upstream']; lic=s['license']
    out=[f'# {s["title"]}',f'**{s["name"]}** · {data["levels"][s["level"]]} · {data["categories"][s["category"]]}',
         '[← 回到选 Skill](../README.md) · [全部客户端入口](../docs/clients.md)',
         '## 适合我吗？',s['problem'],f'**适合：**{s["audience"]}。',f'**为什么选它：**{s["recommendation_reason"]}',
         f'**怎么选同类：**{s["comparison"]}',f'**先知道：**{s["start_note"]}',
         '## 开始前要有什么？']
    out += ['- '+p for p in s['prerequisites']]
    out += [preflight(s),'## 1. 获取这一项',
            f'**[打开固定版本的单项文件夹]({u["directory_url"]})** · [查看入口 SKILL.md]({u["skill_url"]}) · [许可]({lic["skill_license_url"]})',
            source_hint(s),
            '不熟悉 Git？可以把下面的准备任务交给有网络和文件能力的 AI。它只是可复制的准备说明，不是已实测的一键安装器。先打开你的测试项目，再展开所用客户端，直接复制准备任务；同页往下就是调用示例。']
    if s['fetch_mode']=='single_file':
        raw=f'https://raw.githubusercontent.com/{u["repository"]}/{u["commit"]}/{u["directory"]}/SKILL.md'
        out += [f'本项是轻量文本入口，也可右键[固定版本原始文件]({raw})，选择“链接另存为”，保存为 `SKILL.md`，并保留上方 Apache 许可。保存后检查不是 HTML 或 `.md.txt`。这只适用于本项，不能套用到带资源的其他 Skill。']
    elif not s['id'].startswith(('anthropics--','vercel-labs--')):
        archive=f'https://github.com/{u["repository"]}/archive/{u["commit"]}.zip'
        out += [f'**手工替代：**[下载该固定版本 ZIP]({archive})，解压后只取 `{u["directory"]}/`，放到下方目标目录。ZIP 是上游全仓库快照，不代表推荐安装合集；不执行其中的安装脚本。另保留[原许可]({lic["skill_license_url"]})及适用 NOTICE，剩余合集不用放进 AI 工具。']
    out += ['<details>','<summary>macOS / Windows 放文件时怎么操作</summary>','',
            'macOS：在 Finder 打开你的项目，按 `Command + Shift + .` 显示隐藏文件；建立下方的 `.agents` 等目录。Windows：资源管理器打开项目，开启“查看 → 显示 → 文件扩展名”，按下方层级建文件夹。',
            '如果系统询问合并/替换，选择取消。不要出现 `技能名/技能名/SKILL.md` 的双层目录。先用临时项目与虚构文件，不搬动你已有的 Skill。','', '</details>',
            '## 2. 选你的 AI 工具，然后加载',
            '**官方机制已核对，本项未逐客户端实测。** 支持目录不代表工具、权限或脚本已经就绪。下面每个入口包含独立路径，不要同时复制到多个地方。']
    for c in data['clients']:
        out += [f'<details>\n<summary>{c["label"]} · {"项目目录" if c["mode"]=="folder" else "需界面导入，待验证"}</summary>\n',
                client_body(s,c),f'[官方说明]({c["source"]})',
                '**可复制的准备任务：**','```text',acquisition_prompt(s,c),'```','</details>']
    out += ['## 3. 复制任务，先试一个小样例',
            '先完成上一节的加载，再发送下面的中文任务。示例本身不会自动安装或证明调用成功。','```text',s['prompt'],'```',
            '运行前先让 AI 确认工具是否存在，只处理授权范围与副本；缺工具时先报缺项，不自动安装。',
            ]
    if 'exercise' in s:
        ex=s['exercise']
        out += ['### 手头没有项目？用这个小练习',
                f'在新的空文件夹中建立 `{ex["filename"]}`，复制下面的代码。只对这个临时文件练习，不读其他项目。已有 Python 即可；没有则先停，不为本教程安装。',
                '```python', ex['code'], '```', ex['expected_note'],
                '加载 Skill 后可发送：', '```text', ex['prompt'], '```',
                '用真实执行输出对照预期，而不是让 AI 自己宣布练习通过。']
    out += ['## 4. 怎么知道生效了？']
    out += [f'{i}. {v}' for i,v in enumerate(s['ready_checks'],1)]
    out += ['## 没生效 / 想撤销',
            f'先查项目是否打开正确、入口是否为 `技能名/SKILL.md`、是否有同名冲突，然后新建会话重新检查。缺工具不等于 Skill 没加载；看到名字也不等于任务成功。',
            '项目目录方式：只把**本次新加的单项文件夹**移到项目外留作备份，再新建会话。导入方式：只禁用本次导入项并新建任务；删除行为先看客户端确认提示。不要清空整个 skills、缓存或配置目录。',
            '<details>','<summary>来源、固定版本、许可与已知限制</summary>','',
            f'- 原作者/维护方：{u["maintainer"]}；[{u["repository"]}]({u["directory_url"]})。',
            f'- 固定版本：`{u["commit"]}`；{u.get("version_label","以 Commit 为准")}。',
            f'- 许可：[{lic["skill_expression"]}]({lic["skill_license_url"]})。{lic.get("scope_note","")}',
            f'- 依赖许可：{lic.get("dependencies_review","依赖单独核实。")}',f'- 运行依据：{evidence(s)}',
            f'- 原证据：{s["validation"]["evidence_summary"]}',
            f'- [历史固定版本详细记录](../archive/v1.2/docs/skills.md#{s["id"]})。',
            '','**已知限制（不是要求你执行的步骤）：**','']
    out += ['- '+v for v in s['limitations']]
    out += ['',f'**采用前提：**{s["adoption_gate"]}','', '</details>']
    return '\n\n'.join(out)+'\n'


def card_html(s,data):
    u=s['upstream'];lic=s['license']
    a=lambda label,url:f'<a href="{H(url,quote=True)}" target="_blank" rel="noopener noreferrer">{H(label)}</a>'
    p=lambda text:f'<p>{H(text)}</p>'
    out=f'<h2>{H(s["title"])}</h2><p class="eyebrow">{H(s["name"])}</p>'
    out+=p(s['problem'])+p('适合：'+s['audience'])+p('怎么选：'+s['comparison'])+p('先知道：'+s['start_note'])
    out+='<h3>开始前准备</h3>'+''.join(p(x) for x in s['prerequisites'])+p(preflight(s))
    out+='<h3>1 · 获取固定单项</h3>'+p(source_hint(s))+a('打开固定文件夹',u['directory_url'])+' · '+a('许可',lic['skill_license_url'])
    out+=p('下面的准备任务可交给有网络与文件能力的 AI。按官方机制编写，未执行安装；遇同名项必须停止。不要下载整个合集。')
    for c in data['clients']:
        out+=f'<details><summary>{H(c["label"])} · {"项目目录" if c["mode"]=="folder" else "导入待验证"}</summary>'
        out+=p(client_body(s,c).replace('`',''))+a('官方说明',c['source'])
        out+='<pre>'+H(acquisition_prompt(s,c))+'</pre><button class="copy-pre" type="button">复制准备任务</button></details>'
    out+='<h3>2 · 加载后试一个小样例</h3><pre>'+H(s['prompt'])+'</pre><button class="copy-pre" type="button">复制任务</button>'
    if 'exercise' in s:
        ex=s['exercise']
        out+='<h3>手头没有项目？试一个小练习</h3>'+p('在新的空文件夹建立 '+ex['filename']+'。只用已有 Python，不装包，不读其他项目。')
        out+='<pre>'+H(ex['code'])+'</pre><button class="copy-pre" type="button">复制练习代码</button>'+p(ex['expected_note'])
        out+='<pre>'+H(ex['prompt'])+'</pre><button class="copy-pre" type="button">复制练习任务</button>'
    out+='<h3>3 · 检查有没有生效</h3><ol>'+''.join('<li>'+H(x)+'</li>' for x in s['ready_checks'])+'</ol>'
    out+=p('没生效：核对项目、单层文件夹、同名入口，再开新会话。撤销：只移出本次新增单项，或禁用本次导入项。不要清空 skills 或客户端配置。')
    out+='<details><summary>固定版本、许可与证据</summary>'+p(u['commit'])+a(lic['skill_expression'],lic['skill_license_url'])+p(evidence(s))
    out+=''.join(p(x) for x in s['limitations'])+p('采用前提：'+s['adoption_gate'])+'</details>'
    out+=p('手工获取、Windows/macOS 文件操作、完整许可和历史依据：')+a('打开完整 GitHub 卡片',REPO+'/blob/redesign/skill-library/'+s['detail_url'])
    return out


def readme(data):
    ss=data['skills']
    get=lambda id:next(s for s in ss if s['id']==id)
    link=lambda s:f'[{s["title"]}]({s["detail_url"]})'
    out=['# 真正用得上的 Agent Skills',
         '> 为 AI 加一份专门的做事指南：先找到要解决的事，再选适合你工具的那一项。',
         '**20 项认真选择的 Skill，8 项优先了解，12 项专项选择。** 不堆数量，不要求先学 Git，也不把“能添加”写成“已运行成功”。',
         '**[按任务找 ↓](#find) · [按 AI 工具找 ↓](#clients) · [第一次使用 ↓](#start) · [可搜索目录](#search)**',
         '想让 AI 改 Excel、排查错误、画图或做网页？这里帮你判断选谁、先准备什么，并在**一张卡片内**给出固定来源、添加路径、中文示例和撤销方法。下载的是原作者材料，本仓库不打包第三方 Skill。',
         '<a id="find"></a>','## 你想让 AI 帮什么忙？',
         '| 我想…… | 从这里开始 | 开始前知道 |','| --- | --- | --- |',
         f'| 看懂 CSV / TSV 数据 | {link(get("k-dense-ai--exploratory-data-analysis"))} | 需要 Python；先体检，不改原表 |',
         f'| 把数据画成图 | {link(get("k-dense-ai--matplotlib"))} | 需要绘图环境；检查字体和数据 |',
         f'| 读一批文档、提取文字 | {link(get("k-dense-ai--markitdown"))} | 提取内容，不保留原版式 |',
         f'| 修改 Word、Excel、PPT | [Word](skills/iofficeai--officecli-docx.md) · [Excel](skills/iofficeai--officecli-xlsx.md) · [PPT](skills/iofficeai--officecli-pptx.md) | 专项：先准备 OfficeCLI，尚非即装即用 |',
         f'| 让 AI 修复代码错误 | {link(get("obra--systematic-debugging"))} | 沿用项目日志和测试工具 |',
         f'| 让网页更好看、更好维护 | {link(get("anthropics--frontend-design"))} · [React 性能](skills/vercel-labs--react-best-practices.md) · [组件结构](skills/vercel-labs--composition-patterns.md) | 后两项面向 React；无需 Vercel 账号 |',
         f'| 查代码或依赖的安全风险 | [变更安全审查](skills/trailofbits--differential-review.md) · [依赖风险](skills/trailofbits--supply-chain-risk-auditor.md) | 不能代替专业验收；外发数据先确认 |',
         f'| 创建 Agent 或工具接口 | [Agent 设计](skills/github--agent-architecture.md) · [MCP 接口](skills/anthropics--mcp-builder.md) | 面向开发者，不是现成服务 |',
         f'| 读 AI 论文 | [论文与关联资料](skills/huggingface--huggingface-papers.md) | 需要联网，只读公开资料 |',
         '**想自动操作网页？** 目前没有给新手推荐可复现的固定组合；[原 Playwright CLI 记录](archive/README.md)保留供参考，不用其他能力冒充浏览器自动化。',
         '<a id="start"></a>','## 第一次用，从这里开始',
         'Skill 通常是一个带 `SKILL.md` 的文件夹，告诉 AI 如何完成特定任务；它不会自动给电脑装好 Python、Office 或其他工具。',
         '1. **先看卡片的“适合我吗”和“开始前要有什么”。** 普通办公用户可以先看上面的文档/数据入口；开发者可从[系统排障](skills/obra--systematic-debugging.md)开始。缺工具就先停，不必照抄命令。',
         '2. **在同一张卡片展开你使用的 AI 工具。** 直接复制准备任务，让 AI 只获取固定单项；也可按卡片手工下载。已有同名项时停止。',
         '3. **按该工具的方式加载，再复制中文任务试一个副本。** 请 AI 说出实际读取的文件路径，核对真正生成的结果。能说出名字不等于已经生效。',
         '不会操作也没关系：把卡片的准备任务交给当前 AI。若它没有网络/文件权限，卡片会提供原文件入口；不要让它凭空补出资源。所有添加说明均待各客户端实际验收。',
         '<a id="clients"></a>','## 我使用的是哪个 AI 工具？',
         '来源公司不是使用限制。下面按**官方发现或导入机制**分组；每项仍要满足自己的工具条件，不代表我们已逐项实测。',
         '| 工具 | 这份目录怎么用 |','| --- | --- |']
    for c in data['clients']:
        text=f'项目内 `{c["directory"]}/技能名/`' if c['mode']=='folder' else '独立技能面板导入；包格式/资源保留待验证'
        out.append(f'| [{c["label"]}](docs/clients.md#{c["id"]}) | {text}；卡片内有专属步骤 |')
    out += ['<a id="search"></a>','## 查找与筛选',
            '- **直接在 GitHub 用：** 下方按任务浏览；电脑按 `Ctrl + F`（Mac：`Command + F`）搜索中文任务或英文名称。',
            '- **想搜索、按任务与门槛筛选，并选择 AI 配置路径：** [打开在线 Skill 目录](https://leilinfeng007-eng.github.io/awesome-universal-agent-skills/)，无需下载文件。搜索词只在本机浏览器内处理，无后端或追踪。',
            '<a id="all"></a>','## 全部当前推荐',
            '“优先了解”表示用途常见、入口相对清楚；“专项选择”表示需要更多工具或有特定场景。它们不是测试成绩。']
    for key,label in data['categories'].items():
        out += [f'### {label}','| Skill / 用途 | 选择条件 |','| --- | --- |']
        for s in ss:
            if s['category']==key:
                out.append(f'| {link(s)}<br><sub>{s["name"]} · {data["levels"][s["level"]]}</sub> | {s["start_note"]} |')
    out += ['## 我们怎样做选择',
            '看独立实用价值、原始维护方、资源是否完整、必要工具与长期获取条件；不按 Stars 排名。能清楚说明适用场景和限制，才放进当前目录。相似但用途不同的项可以并列；暂停推荐的内容保留在[历史参考区](archive/README.md)。',
            '**验证说清楚：** 只有 EDA 的受限核心有历史本地合成样例记录；本轮没有安装或运行第三方 Skill，所有条目的跨客户端运行仍未验证。每张卡片可展开原始证据，不把推荐当成功保证。',
            '## 维护与来源',
            '[怎么贡献和更新](CONTRIBUTING.md) · [数据与构建方式](docs/maintenance.md) · [结构化目录](catalog.json) · [许可证边界](LICENSE-NOTICE.md) · [历史参考](archive/README.md)',
            '原创导览采用 CC BY 4.0；原创构建代码采用 MIT。第三方 Skill 和依赖保留各自许可，仓库不镜像它们的代码。',
            '---',
            '**English:** A carefully curated, Chinese-first guide to practical Agent Skills. Find a task, understand the prerequisites, and get a pinned-source setup and usage card for your AI tool. Optional online search; no backend, tracking, or bundled third-party Skills.']
    return re.sub(r'(?m)^(\|[^\n]*\|)\n\n(?=\|)', r'\1\n', '\n\n'.join(out))+'\n'


def outputs(data):
    result={ROOT/'README.md':readme(data)}
    for s in data['skills']:result[ROOT/s['detail_url']]=card_md(s,data)
    page_data={k:data[k] for k in ['categories','clients','compatibility_note']}
    page_data['skills']=[dict(s,detail_html=card_html(s,data)) for s in data['skills']]
    # Prevent script termination by content, even when a future source contains </script>.
    embedded=json.dumps(page_data,ensure_ascii=False).replace('<','\\u003c').replace('\u2028','\\u2028').replace('\u2029','\\u2029')
    template=(ROOT/'tools/directory.html').read_text()
    assert template.count('__CATALOG_JSON__')==1
    result[ROOT/'index.html']=template.replace('__CATALOG_JSON__',embedded)
    return result


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true');args=parser.parse_args()
    data=load_catalog();check_catalog(data);result=outputs(data)
    stale=[]
    for path,text in result.items():
        if args.check:
            if not path.exists() or path.read_text()!=text:stale.append(str(path.relative_to(ROOT)))
        else:path.parent.mkdir(parents=True,exist_ok=True);path.write_text(text)
    if stale:raise SystemExit('Generated files differ: '+', '.join(stale))
    print(('Checked' if args.check else 'Built')+f' {len(result)} outputs; {len(data["skills"])} current Skills.')

if __name__=='__main__':main()
