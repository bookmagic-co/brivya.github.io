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
    page = Page()
    page.feed((root / 'index.html').read_text())
    if page.lang != 'zh-CN' or page.h1 != 1:
        raise ValueError('页面语言或主标题数量不正确')
    if page.canonical != [DOMAIN] or page.og_urls != [DOMAIN]:
        raise ValueError('canonical 或 Open Graph 域名不一致')
    for ref in page.references:
        url = urlsplit(ref)
        if url.scheme or url.netloc:
            if url.scheme != 'https' or not url.netloc:
                raise ValueError(f'不支持的外部链接: {ref}')
            continue
        if url.path:
            local = (root / unquote(url.path).lstrip('/')).resolve()
            if not local.is_relative_to(root.resolve()) or not local.is_file():
                raise ValueError(f'资源缺失或越界: {ref}')
        elif url.fragment and unquote(url.fragment) not in page.ids:
            raise ValueError(f'锚点缺失: {ref}')
    if (root / 'CNAME').read_text().strip() != 'brivya.com':
        raise ValueError('CNAME 域名不正确')
    if f'Sitemap: {DOMAIN}sitemap.xml' not in (root / 'robots.txt').read_text():
        raise ValueError('robots sitemap 地址不正确')
    urls = ET.parse(root / 'sitemap.xml').findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
    if [url.text for url in urls] != [DOMAIN]:
        raise ValueError('sitemap URL 不正确')
    ET.parse(root / 'assets/favicon.svg')
    print('PASS: 部署文件、资源、锚点、标题、正式域名与 XML')


if __name__ == '__main__':
    try:
        check(Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else ROOT)
    except (ValueError, OSError, ET.ParseError) as error:
        print(f'FAIL: {error}', file=sys.stderr)
        sys.exit(1)
