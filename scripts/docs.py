#!/usr/bin/env python3
"""从集中维护的内容生成无依赖的官网文档页。"""
from html import escape
from pathlib import Path
from docs_en import english_pages

ROOT = Path(__file__).resolve().parents[1]
PAGES = [
    ('', '文档中心', '从业务契约到多平台接入，找到构建 Business Agent 的下一步。', [
        ('从这里开始', '<p>Brivya 是开源 Business-to-Agent 基础设施。它将真实业务能力定义为类型化契约，通过同一受治理运行时连接 REST、MCP 与平台分发生态。</p><p>如果第一次使用 Brivya，先完成快速开始，再阅读架构和 Restaurant 示例。已有 TypeScript 项目可以从 SDK 与协议适配器开始。</p>'),
        ('开发路线', '<ol><li><a href="/docs/quickstart/">快速开始</a>：安装 CLI，生成并验证业务 Manifest。</li><li><a href="/docs/architecture/">架构与安全</a>：理解业务契约、运行时和平台投影。</li><li><a href="/docs/sdk/">TypeScript SDK</a>：使用 canonical 类型和运行时。</li><li><a href="/docs/adapters/">协议与平台适配</a>：通过 REST、MCP 和参考分发配置接入生态。</li><li><a href="/docs/restaurant/">Restaurant 示例</a>：运行已有的端到端业务契约测试。</li></ol>'),
        ('当前版本', '<p>当前公开版本为 <code>0.1.0-alpha.1</code>，14 个 npm 包已发布，使用 <code>next</code> dist-tag。公开 API 仍处于预稳定阶段。本文档以当前 Alpha 基线为准，不代表托管服务或第三方平台发布承诺。</p><p><a href="/docs/releases/">查看包列表与版本说明 →</a></p>'),
    ]),
    ('quickstart', '快速开始', '用 CLI 创建第一份业务契约，验证本地开发配置。', [
        ('环境准备', '<p>需要 Node.js 20 或更高版本与 npm。CLI 的本地流程无需云账号、LLM API Key 或数据库。</p><pre><code>node --version\nnpm --version\nnpm install -g @brivya/cli@0.1.0-alpha.1</code></pre>'),
        ('创建业务契约', '<pre><code>mkdir my-business\ncd my-business\nbrivya init\nbrivya validate\nbrivya inspect\nbrivya dev</code></pre><p><code>init</code> 创建 <code>business.agent.yaml</code>；<code>validate</code> 校验 Manifest；<code>inspect</code> 展示解析后的业务定义；<code>dev</code> 验证并展示本地配置。</p><aside class="doc-note">初始化生成的是业务契约骨架，尚未连接实际业务系统。CLI dev 不启动 HTTP 服务，也不代替 BusinessRuntime 执行业务。</aside>'),
        ('编辑与观察', '<p>在生成的 Manifest 中维护业务标识、能力声明、协议和安全要求。先运行 <code>brivya inspect</code> 了解骨架，不要跳过校验。要观察文件变化，使用：</p><pre><code>brivya dev business.agent.yaml --watch</code></pre><p>也可以向 validate、inspect 和 dev 显式传入 Manifest 文件路径。已有文件不会被 init 默默覆盖。</p>'),
        ('连接真实能力', '<p>下一步在应用内使用 SDK 注册能力契约、配置授权与策略、提供 Connector，并接入协议适配器。发现业务能力不等于获得变更权限。</p><p><a href="/docs/sdk/">继续阅读 SDK</a>，或通过 <a href="/docs/restaurant/">Restaurant 示例</a> 理解完整执行路径。</p>'),
    ]),
    ('architecture', '架构与安全', '一份业务真相，多个平台投影；每一次变更都经过同一治理路径。', [
        ('分层模型', '<div class="doc-flow"><div>AI 平台与 Agent Hosts</div><span>↓</span><div>DistributionProfile · REST / MCP</div><span>↓</span><div>Canonical Business Agent · BusinessRuntime</div><span>↓</span><div>Connector · ERP / CRM / POS / Business APIs</div></div><p>Manifest、资源、能力与事件定义 canonical 业务契约。协议适配器负责调用投影，分发配置负责平台发现、交互与打包。业务权威保持在契约和运行时中。</p>'),
        ('变更执行链', '<pre><code>校验 → 授权 → 策略 → 必要的审批\n→ 幂等 → Connector → 事务 / 审计 / 事件</code></pre><p>BusinessRuntime 执行业务安全语义。LLM 不直接修改业务数据库；适配器不能直接调用 Connector 来绕过授权、策略或审批。</p>'),
        ('身份与授权', '<ul><li>Agent Identity 不等于 Authorization：识别调用方不代表允许执行所有能力。</li><li>Discovery 不等于 Authorization：Manifest 描述能力，不能授予变更权限。</li><li>Platform Identity 是身份上下文，仍需经过业务授权。</li><li>UI Confirmation 不等于 ApprovalRecord：前端确认不能替代可信审批证据。</li></ul><p>高风险动作的审批、权限、幂等与审计语义不能被协议或体验投影削弱。</p>'),
        ('核心模块', '<table><thead><tr><th>模块</th><th>职责</th></tr></thead><tbody><tr><td>Core / Manifest</td><td>类型化业务契约、解析与校验</td></tr><tr><td>Policy / Runtime</td><td>策略与受治理执行</td></tr><tr><td>Experience / Distribution</td><td>统一交互语义与平台投影</td></tr><tr><td>SDK / CLI</td><td>开发接口与本地契约工具</td></tr><tr><td>Adapters / Connectors</td><td>协议入口与业务系统边界</td></tr></tbody></table>'),
    ]),
    ('sdk', 'TypeScript SDK', '复用公开业务类型、Manifest 校验器与 canonical 运行时。', [
        ('安装', '<pre><code>npm install @brivya/sdk@0.1.0-alpha.1</code></pre><p>SDK 是 Core、Manifest、Policy 与 Runtime 的公开接口门面，不创建第二套授权或运行时真相。</p>'),
        ('解析和校验 Manifest', '<p>以下示例读取由 CLI init 生成的 Manifest，并运行同一 canonical 解析与校验逻辑：</p><pre><code>import { readFileSync } from "node:fs";\nimport { loadBusinessAgentManifest } from "@brivya/sdk";\n\nconst source = readFileSync("business.agent.yaml", "utf8");\nconst agent = loadBusinessAgentManifest(source);\nconsole.log(agent.metadata.id);</code></pre><p>解析或校验失败时应处理错误，不要将无效 Manifest 继续用于业务执行。</p>'),
        ('运行时与类型', '<pre><code>import {\n  BusinessRuntime,\n  CapabilityRegistry,\n  runtime,\n  type ActionRequest,\n  type CapabilityContract,\n  type Principal,\n  type Delegation,\n} from "@brivya/sdk";</code></pre><p>BusinessRuntime 和 CapabilityRegistry 指向 canonical 实现。实际配置需要能力注册、Connector、授权上下文和相关运行时依赖；仅导入 SDK 不会创建可执行业务服务。</p>'),
        ('应用集成顺序', '<ol><li>定义能力输入、输出与业务安全要求。</li><li>通过 CapabilityRegistry 注册能力契约。</li><li>提供真实业务 Connector 与所需的策略、审批、幂等和审计实现。</li><li>由可信服务端构造身份与委托上下文。</li><li>使用 BusinessRuntime 执行，或通过 REST / MCP 适配器调用同一运行时。</li></ol><p>参考 <a href="/docs/restaurant/">Restaurant 示例</a> 学习注册能力和执行测试；参考 <a href="/docs/adapters/">适配器指南</a> 连接协议入口。</p>'),
    ]),
    ('adapters', '协议与平台适配', 'REST 和 MCP 共享运行时，平台分发配置复用 canonical 业务语义。', [
        ('REST 调用边界', '<p>REST 适配器提供与 HTTP 框架无关的执行投影：</p><pre><code>POST /v0alpha1/capabilities/{capability}/execute\n\n{\n  "input": {},\n  "preconditions": {}\n}</code></pre><p>协议元数据通过 X-Brivya-Capability-Version、X-Request-Id、X-Correlation-Id、X-Causation-Id 与 Idempotency-Key 等头传递。请求体不能声明可信身份或审批状态。</p><p>宿主 HTTP 层验证会话或认证信息，并传入可信 RestSecurityContext；适配器构造 ActionRequest 后调用 BusinessRuntime。</p>'),
        ('MCP 工具投影', '<p>能力 <code>order.create@0.1.0</code> 投影为工具 <code>brivya.order.create.v0.1.0</code>，能力输入输出 JSON Schema 被传递给 MCP SDK。</p><p>宿主 transport/auth 层提供可信 McpContextResolver，映射已验证的会话身份、委托、审批与关联信息。工具参数仅为业务输入；MCP annotations 只是提示，不是授权。</p><aside class="doc-note">默认上下文只包含不可信 Agent actor。缺少可信解析器时，受保护能力在 BusinessRuntime 中拒绝执行。</aside>'),
        ('WorkBuddy 与 WeChat AI', '<table><thead><tr><th>参考投影</th><th>生成内容</th></tr></thead><tbody><tr><td>WorkBuddy</td><td>connector-meta.json、mcp.json、skills/business/SKILL.md</td></tr><tr><td>WeChat AI</td><td>SKILL.md、mcp.json、runtime-bridge.json、components 与注册补丁</td></tr></tbody></table><p>这些是参考打包与一致性基线。生产发布仍需重新核对平台官方要求、资格与审核流程；不保证第三方字段和接口永远稳定。</p>'),
        ('适配前检查', '<ul><li>投影保留输入输出 Schema、风险与权限要求。</li><li>高风险动作保留 canonical 审批语义。</li><li>幂等与审计不会被协议分支削弱。</li><li>客户端身份与 UI 确认不被提升为可信授权证据。</li></ul><p>统一交互语义由 SemanticExperience 描述，再交给平台 renderer 呈现；业务动作仍绑定 canonical Capability ID。</p>'),
    ]),
    ('extensions', 'Extension Host', '明确声明权限，通过受限 Host API 扩展业务能力。', [
        ('Alpha 基线', '<p>Extension Host 包含 Extension Manifest / Package、权限授权、权限扩张检测、安装计划、Registry Client 契约及 worker / remote 执行边界。</p><p>这些是框架层契约与基线能力，不代表已有公开托管 Registry 或第三方扩展市场。</p>'),
        ('有效权限', '<pre><code>请求权限 ∩ 租户策略 ∩ 管理员授权 = 有效权限</code></pre><p>扩展声明权限并不自动获得权限。新版本扩大权限时，需要重新批准；宿主只授予最终交集允许的能力。</p>'),
        ('执行与凭据边界', '<pre><code>Extension → Host API\n→ canonical Brivya Runtime / governed platform service</code></pre><p>Host API 按权限限制访问，凭据通过不透明 secret binding 引用。不存在原始 secret-read Host API，也不应把凭据明文交给扩展。</p>'),
        ('当前限制', '<p>Phase 1 使用 worker 与 remote 执行模型。WASM 延后，任意第三方进程内执行不属于当前基线。上线前需验证宿主隔离、授权和外部网络策略。</p><p><a href="/docs/architecture/">回到运行时安全模型 →</a></p>'),
    ]),
    ('restaurant', 'Restaurant 示例', '通过确定性测试理解发现、预订、订单和支付请求的完整业务链路。', [
        ('示例能力', '<table><thead><tr><th>Capability</th><th>业务步骤</th></tr></thead><tbody><tr><td>menu.search</td><td>搜索菜单</td></tr><tr><td>availability.check</td><td>检查可用性</td></tr><tr><td>reservation.create</td><td>创建预订</td></tr><tr><td>order.create</td><td>创建订单</td></tr><tr><td>payment.request</td><td>请求支付</td></tr></tbody></table><p>REST 与 MCP 执行同一能力契约并共享 BusinessRuntime。示例使用 mock Connector，不依赖特定 LLM 或真实支付 SDK。</p>'),
        ('获取并运行', '<pre><code>git clone https://github.com/brivya/brivya.git\ncd brivya\nnpm install --ignore-scripts --no-audit --no-fund\nnpm run ci</code></pre><p>当前仓库没有提交 lockfile，因此使用与 CI 一致的 npm install。根命令完成构建、类型检查及测试，包含 Restaurant RST-001..RST-024 契约矩阵。</p>'),
        ('只运行示例测试', '<pre><code>npm run build\nnode --test examples/restaurant/dist/test/*.test.js</code></pre><p>先构建所有工作区以准备跨包依赖，再运行已编译的示例测试。测试使用确定性数据，覆盖业务执行、安全拒绝和审计等行为。</p>'),
        ('阅读路径', '<ul><li><code>examples/restaurant/src/manifest.ts</code>：业务身份与能力声明。</li><li><code>examples/restaurant/src/capabilities.ts</code>：业务能力定义。</li><li><code>examples/restaurant/test/</code>：端到端验证证据。</li><li><code>connectors/mock/</code>：模拟业务系统连接。</li></ul><aside class="doc-note">payment.request 表示业务支付请求，不表示示例已经接通真实支付渠道。Manifest 中的 bootstrap URL 是示例业务身份，不是官网提供的在线演示服务。</aside>'),
    ]),
    ('releases', '版本与包', '了解当前 Alpha 的公开模块、安装方式与稳定性边界。', [
        ('v0.1.0-alpha.1', '<p>首个公开 Alpha 于 2026 年 10 月 3 日发布。14 个 npm 包版本统一为 <code>0.1.0-alpha.1</code>，使用 <code>next</code> dist-tag。API 尚未稳定，建议显式固定版本。</p><pre><code>npm install @brivya/sdk@0.1.0-alpha.1\nnpm install -g @brivya/cli@0.1.0-alpha.1</code></pre>'),
        ('公开包列表', '<ul class="package-list">'+''.join('<li><code>@brivya/'+p+'</code></li>' for p in ['core','manifest','policy','runtime','experience','distribution','extensions','sdk','cli','adapter-rest','adapter-mcp','adapter-workbuddy','adapter-wechat-ai','connector-mock'])+'</ul>'),
        ('能力与限制', '<p>当前基线包括类型化契约、受治理运行时、REST / MCP、平台参考投影、CLI / SDK、Restaurant E2E 和 Extension Host。根工作区与 Restaurant 示例未作为公共 npm 包发布。</p><p>托管 Runtime、Registry、企业身份或正式平台自动发布不由此版本承诺。npm OIDC 迁移是发布治理工作，不是使用官网或安装公开包的前置条件。</p>'),
        ('升级前检查', '<ul><li>阅读版本说明，确认 API 与 Manifest 兼容性。</li><li>先运行业务契约、权限、审批、幂等和适配器测试。</li><li>所有 canonical 包保持版本一致。</li><li>不要将 Alpha 变更视为稳定兼容保证。</li></ul>'),
    ]),
    ('contributing', '参与贡献与安全', '帮助完善业务契约、开发工具和多平台一致性。', [
        ('贡献路径', '<p>欢迎通过源码仓的 issue 与 Pull Request 参与。较大的功能先讨论问题、范围与兼容性；实现应保持协议中立、模型中立、类型化能力和明确策略边界。</p><ol><li>创建 feature 分支并聚焦单一改动。</li><li>实现行为变更时补充测试和公开文档。</li><li>运行 npm run ci 与相关发布就绪检查。</li><li>提交 PR，说明问题、行为、验证和兼容性影响。</li></ol>'),
        ('安全报告', '<p>潜在漏洞应按照公开仓 SECURITY.md 的渠道私下报告。不要在公开 issue 中贴出凭据、客户数据或敏感漏洞细节。</p><p><a href="https://github.com/brivya/brivya/blob/main/SECURITY.md">查看安全报告渠道 ↗</a></p>'),
        ('许可证与品牌', '<p>公开框架采用 Apache-2.0 许可证。Brivya 名称与品牌受独立商标政策约束。使用框架不意味着取得第三方平台或 Brivya 品牌的额外授权。</p><p><a href="https://github.com/brivya/brivya/blob/main/LICENSE">查看许可证原文 ↗</a></p>'),
    ]),
]


def generate(root=ROOT):
    urls = ["https://brivya.com/", "https://brivya.com/en/"]
    for language, pages in [("zh", PAGES), ("en", english_pages(PAGES))]:
      for n, (slug, title, summary, sections) in enumerate(pages):
        zh_path = '/docs/' + (slug + '/' if slug else '')
        path = ('/en' if language == 'en' else '') + zh_path
        urls.append('https://brivya.com' + path)
        nav = ''.join(f'<a href="/docs/{s + "/" if s else ""}"'+ (' aria-current="page"' if s == slug else '') + f'>{escape(t)}</a>' for s, t, _, _ in pages)
        toc = ''.join(f'<a href="#section-{i}">{escape(heading)}</a>' for i, (heading, _) in enumerate(sections))
        body = ''.join(f'<section id="section-{i}"><h2>{escape(heading)}</h2>{html}</section>' for i, (heading, html) in enumerate(sections))
        next_slug, next_title, _, _ = pages[(n + 1) % len(pages)]
        html = f'''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)} · Brivya 文档</title><meta name="description" content="{escape(summary, quote=True)}">
<meta name="theme-color" content="#f5f4ef"><meta property="og:title" content="{escape(title)} · Brivya">
<meta property="og:description" content="{escape(summary, quote=True)}"><meta property="og:type" content="website"><meta property="og:url" content="https://brivya.com{path}">
<link rel="canonical" href="https://brivya.com{path}"><link rel="icon" href="/assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="/assets/style.css"><link rel="stylesheet" href="/assets/docs.css"></head>
<body><a class="skip" href="#main">跳转到正文</a><header class="header wrap"><a class="brand" href="/" aria-label="Brivya 首页"><span class="mark" aria-hidden="true">b</span>brivya<span class="brand-dot">.</span></a><nav aria-label="主导航"><a href="/docs/">文档</a><a href="/docs/quickstart/">Quick Start</a><a href="/docs/adapters/">生态</a><a class="github" href="https://github.com/brivya/brivya">源码 ↗</a></nav></header>
<div class="docs-shell wrap"><aside class="docs-sidebar"><p class="eyebrow">DEVELOPER DOCS</p><nav aria-label="文档导航">{nav}</nav><p class="docs-version">v0.1.0-alpha.1<br>预稳定 API</p></aside>
<main id="main" class="doc-main"><p class="breadcrumb"><a href="/">首页</a> / <a href="/docs/">文档</a> / {escape(title)}</p><h1>{escape(title)}</h1><p class="doc-lead">{escape(summary)}</p><nav class="doc-toc" aria-label="本页目录"><span>本页内容</span>{toc}</nav>{body}<a class="doc-next" href="/docs/{next_slug + '/' if next_slug else ''}"><span>下一篇</span><strong>{escape(next_title)} →</strong></a><p class="doc-source">内容依据公开 Alpha 实现 · <a href="https://github.com/brivya/brivya">查看源码 ↗</a></p></main></div>
<footer class="wrap footer"><a class="brand" href="/">brivya<span class="brand-dot">.</span></a><p>Make every business agent-accessible.</p><a href="/docs/contributing/">贡献与许可证 →</a></footer></body></html>'''
        if language == 'en':
            html = html.replace('lang="zh-CN"', 'lang="en"').replace('href="/docs/', 'href="/en/docs/').replace('href="/"', 'href="/en/"')
            labels = {'Brivya 文档': 'Brivya Docs', '跳转到正文': 'Skip to content', 'Brivya 首页': 'Brivya home', '主导航': 'Main navigation', '文档导航': 'Documentation navigation', '本页目录': 'On this page', '预稳定 API': 'Pre-stable APIs', '本页内容': 'On this page', '下一篇': 'Up next', '内容依据公开 Alpha 实现': 'Based on the public Alpha implementation', '查看源码': 'View source', '贡献与许可证': 'Contributing and license', '首页': 'Home', '文档': 'Docs', '生态': 'Platforms', '源码': 'Source'}
            for original, translated in labels.items():
                html = html.replace(original, translated)
        alternatives = f'<link rel="alternate" hreflang="zh-CN" href="https://brivya.com{zh_path}"><link rel="alternate" hreflang="en" href="https://brivya.com/en{zh_path}"><link rel="alternate" hreflang="x-default" href="https://brivya.com{zh_path}">'
        html = html.replace('</head>', alternatives + '<link rel="stylesheet" href="/assets/language.css"><script src="/assets/language.js" defer></script></head>')
        switch = f'<div class="language-switch" role="group" aria-label="Language"><a href="{zh_path}" lang="zh-CN" hreflang="zh-CN" data-language="zh"{' aria-current="true"' if language == "zh" else ""}>中文</a><a href="/en{zh_path}" lang="en" hreflang="en" data-language="en"{' aria-current="true"' if language == "en" else ""}>EN</a></div>'
        html = html.replace('</nav></header>', switch + '</nav></header>', 1)
        ai_prefix = '/en' if language == 'en' else ''
        html = html.replace('</head>', f'<link rel="alternate" type="text/plain" href="{ai_prefix}/llms.txt"><link rel="alternate" type="text/markdown" href="{path}index.md"></head>')
        html = html.replace('</main>', f'<p class="doc-source"><a href="{ai_prefix}/llms.txt">AI docs</a> · <a href="{path}index.md">Markdown</a></p></main>')
        target = root / path.lstrip('/') / 'index.html'
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(html)
    (root / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'  <url><loc>{url}</loc></url>\n' for url in urls) + '</urlset>\n')
    print(f'已生成 {len(PAGES) * 2} 个双语文档内页')


if __name__ == '__main__':
    generate()
