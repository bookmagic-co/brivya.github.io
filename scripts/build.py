#!/usr/bin/env python3
"""只复制公开站点文件，避免把文档、截图或开发工具部署出去。"""
from pathlib import Path
import shutil
from check import ROOT, check

check()
target = ROOT / '_site'
target.mkdir(exist_ok=True)
for name in ['index.html', 'CNAME', '.nojekyll', 'robots.txt', 'sitemap.xml']:
    shutil.copy2(ROOT / name, target / name)
asset_names = ['style.css', 'docs.css', 'site.js', 'favicon.svg', 'language.css', 'language.js', 'business-animation.css', 'business-animation.js']
for name in asset_names:
    (target / 'assets').mkdir(exist_ok=True)
    shutil.copy2(ROOT / 'assets' / name, target / 'assets' / name)
expected = {'index.html', 'CNAME', '.nojekyll', 'robots.txt', 'sitemap.xml',
            'assets/style.css', 'assets/docs.css', 'assets/site.js', 'assets/favicon.svg'}
expected.update('assets/' + name for name in asset_names)
for source in [*(ROOT / 'docs').rglob('*.html'), *(ROOT / 'en').rglob('*.html'), *(ROOT / 'docs').rglob('*.md'), *(ROOT / 'en').rglob('*.md'), ROOT / 'llms.txt', ROOT / 'llms-full.txt', ROOT / 'en/llms.txt', ROOT / 'en/llms-full.txt', ROOT / 'ai/index.json']:
    relative = source.relative_to(ROOT)
    output = target / relative
    output.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, output)
    expected.add(str(relative))
actual = {str(p.relative_to(target)) for p in target.rglob('*') if p.is_file()}
if actual != expected:
    raise SystemExit(f'构建目录包含预期之外的文件，请先检查: {actual - expected}')
check(target)
print(f'站点产物已生成: {target}')
