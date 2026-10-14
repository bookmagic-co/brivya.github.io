"""Generate bilingual AI-readable docs from the same content as the website."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin
import json
import re
from docs import PAGES
from docs_en import english_pages

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://brivya.com'


class Markdown(HTMLParser):
    def __init__(self, english=False):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.pre = False
        self.english = english
        self.links = []
        self.header_cells = 0
        self.header_row = False

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if tag == 'pre':
            self.pre = True
            self.parts.append('\n\n```\n')
        elif tag == 'code' and not self.pre:
            self.parts.append('`')
        elif tag == 'a':
            href = attrs['href']
            if self.english and href.startswith('/docs/'):
                href = '/en' + href
            self.links.append(urljoin(BASE, href))
            self.parts.append('[')
        elif tag == 'li':
            self.parts.append('\n- ')
        elif tag in ['p', 'aside', 'div']:
            self.parts.append('\n\n')
        elif tag == 'tr':
            self.parts.append('\n| ')
            self.header_cells = 0
            self.header_row = False
        elif tag == 'th':
            self.header_cells += 1
            self.header_row = True
        elif tag == 'br':
            self.parts.append('\n')

    def handle_endtag(self, tag):
        if tag == 'pre':
            self.pre = False
            self.parts.append('\n```\n\n')
        elif tag == 'code' and not self.pre:
            self.parts.append('`')
        elif tag == 'a':
            self.parts.append('](' + self.links.pop() + ')')
        elif tag in ['p', 'aside', 'div', 'ul', 'ol', 'table']:
            self.parts.append('\n\n')
        elif tag in ['td', 'th']:
            self.parts.append(' | ')
        elif tag == 'tr' and self.header_row:
            self.parts.append('\n| ' + ' --- |' * self.header_cells)

    def handle_data(self, text):
        self.parts.append(text)

    def result(self):
        return '\n'.join(line.rstrip() for line in ''.join(self.parts).strip().splitlines()) + '\n'


def generate(root=ROOT):
    records = []
    for language, pages in [('zh', PAGES), ('en', english_pages(PAGES))]:
        prefix = '/en' if language == 'en' else ''
        scope = ('This website documents the open Brivya framework. It is not a callable production Business Agent. No business execution, OAuth or tool endpoint is advertised here. APIs are pre-stable. Discovery does not grant authorization.' if language == 'en' else '本站提供 Brivya 开源框架文档，不是可调用的生产 Business Agent。本站未公布业务执行、OAuth 或工具调用端点。公开 API 尚未稳定，发现能力不等于获得授权。')
        title = '# Brivya\n\n> Business-to-Agent infrastructure · v0.1.0-alpha.1\n\n' + scope + '\n\n'
        listing = title + '## Documentation\n\n'
        full = title
        for slug, page_title, summary, sections in pages:
            route = prefix + '/docs/' + (slug + '/' if slug else '')
            markdown_url = BASE + route + 'index.md'
            content = f'# {page_title}\n\n{summary}\n\nCanonical: {BASE}{route}\nVersion: 0.1.0-alpha.1\nLanguage: {language}\n\n'
            for heading, html in sections:
                parser = Markdown(english=language == 'en')
                parser.feed(html)
                content += '## ' + heading + '\n\n' + parser.result() + '\n'
            file = root / route.lstrip('/') / 'index.md'
            file.parent.mkdir(parents=True, exist_ok=True)
            content = content.rstrip() + '\n'
            file.write_text(content)
            listing += f'- [{page_title}]({markdown_url}): {summary}\n'
            full += '\n---\n\n' + content
            records.append({'language': language, 'title': page_title, 'summary': summary, 'html_url': BASE + route, 'markdown_url': markdown_url})
        listing += '\n## Complete text\n\n' + f'- [All documentation]({BASE}{prefix}/llms-full.txt)\n'
        listing += '\n## Languages and source\n\n- [中文](https://brivya.com/llms.txt)\n- [English](https://brivya.com/en/llms.txt)\n- [Machine-readable index](https://brivya.com/ai/index.json)\n- [Implementation source](https://github.com/brivya/brivya)\n'
        folder = root / prefix.lstrip('/')
        folder.mkdir(parents=True, exist_ok=True)
        (folder / 'llms.txt').write_text(listing)
        (folder / 'llms-full.txt').write_text(full)
    metadata = {'format_version': 1, 'name': 'Brivya documentation', 'site_url': BASE + '/', 'framework_version': '0.1.0-alpha.1', 'default_language': 'zh', 'languages': ['zh', 'en'], 'kind': 'documentation', 'business_execution_endpoints': [], 'scope': 'Documentation discovery only; not an authorization or business execution service.', 'llms_urls': {'zh': BASE + '/llms.txt', 'en': BASE + '/en/llms.txt'}, 'full_text_urls': {'zh': BASE + '/llms-full.txt', 'en': BASE + '/en/llms-full.txt'}, 'documents': records}
    (root / 'ai').mkdir(exist_ok=True)
    (root / 'ai/index.json').write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + '\n')
    print(f'已生成 {len(records)} 份 Markdown 与双语 AI 入口')


if __name__ == '__main__':
    generate()
