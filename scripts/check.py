#!/usr/bin/env python3
"""检查可部署官网的资源引用、锚点和正式域名配置。"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
DOMAIN = 'https://brivya.com/'


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.references = []
        self.canonical = []
        self.og_urls = []
        self.h1 = 0
        self.lang = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'html':
            self.lang = attrs.get('lang')
        if tag == 'h1':
            self.h1 += 1
        if 'id' in attrs:
            if attrs['id'] in self.ids:
                raise ValueError(f"重复 id: {attrs['id']}")
            self.ids.add(attrs['id'])
        for key in ('href', 'src'):
            if key in attrs:
                self.references.append(attrs[key])
        if tag == 'link' and attrs.get('rel') == 'canonical':
            self.canonical.append(attrs.get('href'))
        if tag == 'meta' and attrs.get('property') == 'og:url':
            self.og_urls.append(attrs.get('content'))


def check(root=ROOT):
    required = ['index.html', 'CNAME', '.nojekyll', 'robots.txt', 'sitemap.xml',
                'assets/style.css', 'assets/site.js', 'assets/favicon.svg']
    for name in required:
        if not (root / name).is_file():
            raise ValueError(f'缺少部署文件: {name}')
    pages = {}
    for file in [root / 'index.html', *sorted((root / 'docs').rglob('*.html'))]:
        page = Page()
        page.feed(file.read_text())
        expected = DOMAIN + str(file.parent.relative_to(root)).replace('.', '').strip('/')
        if expected != DOMAIN:
            expected += '/'
        if page.lang != 'zh-CN' or page.h1 != 1:
            raise ValueError(f'{file}: 页面语言或主标题数量不正确')
        if page.canonical != [expected] or page.og_urls != [expected]:
            raise ValueError(f'{file}: canonical 或 Open Graph URL 不一致')
        pages[file.resolve()] = page
    for file, page in pages.items():
        for ref in page.references:
            url = urlsplit(ref)
            if url.scheme or url.netloc:
                if url.scheme != 'https' or not url.netloc:
                    raise ValueError(f'不支持的外部链接: {ref}')
                continue
            base = root if url.path.startswith('/') else file.parent
            local = (base / unquote(url.path).lstrip('/')).resolve() if url.path else file
            if local.is_dir():
                local /= 'index.html'
            if not local.is_relative_to(root.resolve()) or not local.is_file():
                raise ValueError(f'{file}: 资源缺失或越界: {ref}')
            if url.fragment and (local not in pages or unquote(url.fragment) not in pages[local].ids):
                raise ValueError(f'{file}: 页面锚点缺失: {ref}')
    if (root / 'CNAME').read_text().strip() != 'brivya.com':
        raise ValueError('CNAME 域名不正确')
    if f'Sitemap: {DOMAIN}sitemap.xml' not in (root / 'robots.txt').read_text():
        raise ValueError('robots sitemap 地址不正确')
    urls = ET.parse(root / 'sitemap.xml').findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
    if {url.text for url in urls} != {page.canonical[0] for page in pages.values()} or len(urls) != len(pages):
        raise ValueError('sitemap 与全部页面 URL 不一致')
    ET.parse(root / 'assets/favicon.svg')
    print(f'PASS: {len(pages)} 个页面、跨页资源与锚点、标题、正式 URL 和 sitemap')


if __name__ == '__main__':
    try:
        check(Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else ROOT)
    except (ValueError, OSError, ET.ParseError) as error:
        print(f'FAIL: {error}', file=sys.stderr)
        sys.exit(1)
