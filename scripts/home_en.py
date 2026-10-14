"""Generate the English homepage while preserving markup and local navigation."""
from html.parser import HTMLParser
from html import escape
from pathlib import Path
import re

TEXT = {
    'Brivya · 让业务接入 Agent 世界': 'Brivya · Make every business agent-accessible',
    'Brivya 是开源 Business-to-Agent 基础设施，让业务能力通过安全、类型化的运行时接入 AI 平台与 Agent 生态。': 'Brivya is open Business-to-Agent infrastructure connecting typed business capabilities to AI platforms through a governed runtime.',
    '一次定义业务能力，通过同一受治理运行时连接多个 Agent 生态。': 'Define capabilities once. Connect multiple Agent ecosystems through one governed runtime.',
    '跳转到正文': 'Skip to content', 'Brivya 首页': 'Brivya home', '主导航': 'Main navigation',
    '架构': 'Architecture', '生态': 'Platforms', '让业务成为': 'Make business', 'Agent 世界的': 'agent-accessible.', '原生能力。': 'By design.',
    'Business-to-Agent 基础设施。一次定义业务能力，通过安全、类型化的运行时，连接 AI 平台与 Agent 生态。': 'Business-to-Agent infrastructure. Define capabilities once and connect AI platforms through a secure, typed runtime.',
    '开始构建': 'Start building', '阅读文档': 'Read the docs', '开源 · Apache-2.0 · TypeScript': 'Open source · Apache-2.0 · TypeScript',
    '业务系统经过 Brivya 运行时连接多个 Agent 平台': 'Business systems connect to Agent platforms through Brivya Runtime',
    '公开 npm 包': 'public npm packages', '统一业务运行时': 'canonical runtime', '多平台': 'Many', '协议与分发投影': 'protocols and projections',
    'v0.1.0-alpha.1 发布说明 ↗': 'v0.1.0-alpha.1 release notes →',
    '一份业务真相，': 'One business truth.', '连接多个生态。': 'Many ecosystems.',
    '把业务契约、执行治理与平台投影分开。核心能力保持一致，交互体验适配不同的 Agent 平台。': 'Separate business contracts, execution governance and platform projections. Keep capabilities consistent while adapting experiences to each ecosystem.',
    '业务能力，先于提示词': 'Business before prompts',
    '用 Manifest、资源与类型化 Capability 描述真实业务。发现能力不等于获得执行权限。': 'Describe real business with Manifests, resources and typed capabilities. Discovery never grants execution permission.',
    'Manifest 与契约 →': 'Manifests and contracts →', '每次执行，都有边界': 'Boundaries for every action',
    '变更经过校验、授权、策略、必要的审批、幂等、Connector 与审计。让高风险动作保持可治理。': 'Mutations pass validation, authorization, policy, approval when required, idempotency, Connectors and audit. Keep high-risk actions governable.',
    '原生体验，共享语义': 'Native UI, shared semantics',
    'REST、MCP 与分发适配器共享同一运行时。SemanticExperience 将业务交互映射为平台原生呈现。': 'REST, MCP and distribution adapters share one runtime. SemanticExperience maps business interactions into native platform presentation.',
    '从第一份': 'Start with your', '业务契约开始。': 'first business contract.',
    '安装 CLI，生成 Manifest，再验证你的业务定义。Node.js 20 或更高版本即可开始。': 'Install the CLI, generate a Manifest and validate your business definition. Start with Node.js 20 or newer.',
    '当前为 Alpha：公开 API 仍可能变化。': 'Alpha APIs may change.',
    '验证本地配置；业务执行由 BusinessRuntime 提供。': 'validates local configuration; BusinessRuntime owns execution.',
    '探索 Restaurant 端到端示例 →': 'Explore the Restaurant reference →', '复制': 'Copy', '复制 Quick Start 命令': 'Copy Quick Start commands',
    '# 安装 Alpha CLI': '# Install the Alpha CLI', '# 创建并验证业务契约': '# Create and validate a business contract',
    '组合你的 Agent 基础设施。': 'Compose your Agent infrastructure.',
    '从业务契约到平台接入，按需使用开放模块。平台资格、审核与发布仍遵循各平台规则。': 'Use open modules from business contracts to platform integration. Platform qualification, review and publication still follow each platform’s rules.',
    '使用 Core、Manifest、Policy 与 Runtime 的统一公开契约。': 'Use the shared public contracts of Core, Manifest, Policy and Runtime.',
    '让不同协议复用相同的能力契约与安全语义。': 'Reuse capability contracts and safety semantics across protocols.', '协议适配器': 'Protocol adapters',
    '业务能力与体验的平台分发参考投影。': 'Reference distribution projections for business capabilities and experiences.', '分发配置与一致性校验': 'Distribution profiles and conformance',
    '显式授权、受限 Host API 与隔离执行边界。': 'Explicit grants, scoped Host APIs and isolated execution boundaries.', '扩展与权限契约': 'Extension and permission contracts',
    '从代码开始，': 'Start with the code.', '一起构建开放生态。': 'Build an open ecosystem.',
    '框架文档': 'Framework docs', '参与贡献': 'Contribute', '版本与变更': 'Versions and changes', '安全报告': 'Security reports',
    '让对话进入业务，': 'From intent to action.', '让执行保持可控。': 'Keep business in control.',
    '以预订为例，看看 AI 如何理解业务、提交类型化请求，并通过统一运行时连接已有系统。': 'Follow a reservation journey: AI discovers business capabilities, sends typed input and connects existing systems through one governed runtime.',
    '播放动画': 'Play animation', '用户意图': 'User intent', '业务系统': 'Business systems',
    '发现业务能力': 'Discover a capability',
    'AI 平台从类型化业务契约发现 menu.search 与 availability.check。发现说明能力存在，但不会授予执行权限。': 'An AI host discovers menu.search and availability.check from a typed business contract. Discovery describes what exists; it does not grant permission.',
    '业务价值：一次定义能力，让多个入口理解你的业务。': 'Business value: expose capabilities once, across multiple entry points.',
    '业务流程阶段': 'Business journey stages', '发现能力': 'Discover capabilities', '结构化请求': 'Typed request', '治理检查': 'Business controls', '执行与审计': 'Execution and audit',
    '概念动画，不调用真实业务接口。按需审批与授权由业务策略决定。': 'Concept animation; no live business calls. Authorization and approval requirements are determined by business policy.',
    '了解可运行的 Restaurant 示例 →': 'Explore the runnable Restaurant reference →',
}


def translated(value):
    stripped = value.strip()
    if stripped == '中文' or not re.search('[\u4e00-\u9fff]', value):
        return value
    if stripped not in TEXT:
        raise ValueError(f'Missing English homepage translation: {stripped}')
    return value.replace(stripped, TEXT[stripped])


class EnglishHome(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.output = []
    def handle_decl(self, decl): self.output.append('<!' + decl + '>')
    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if tag == 'html': attrs['lang'] = 'en'
        language_link = attrs.get('data-language')
        for key, value in list(attrs.items()):
            if value is None: continue
            if key in ['aria-label', 'title', 'content']: attrs[key] = translated(value)
            if key in ['href', 'content'] and value == 'https://brivya.com/' and attrs.get('rel') != 'alternate':
                attrs[key] = 'https://brivya.com/en/'
            if key == 'href' and not language_link and attrs.get('rel') != 'alternate':
                if value == '/': attrs[key] = '/en/'
                elif value.startswith('/docs/'): attrs[key] = '/en' + value
                elif value == '/llms.txt': attrs[key] = '/en/llms.txt'
            if key == 'href' and value == '/llms.txt': attrs[key] = '/en/llms.txt'
        if language_link:
            attrs.pop('aria-current', None)
            if language_link == 'en': attrs['aria-current'] = 'true'
        self.output.append('<' + tag + ''.join(' ' + k + (f'="{escape(v, quote=True)}"' if v is not None else '') for k, v in attrs.items()) + '>')
    def handle_endtag(self, tag): self.output.append('</' + tag + '>')
    def handle_data(self, data): self.output.append(escape(translated(data), quote=False))
    def handle_entityref(self, name): self.output.append('&' + name + ';')
    def handle_charref(self, name): self.output.append('&#' + name + ';')
    def handle_comment(self, text): self.output.append('<!--' + text + '-->')


def generate(root):
    parser = EnglishHome()
    parser.feed((root / 'index.html').read_text())
    target = root / 'en/index.html'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(''.join(parser.output))


if __name__ == '__main__':
    generate(Path(__file__).resolve().parents[1])
