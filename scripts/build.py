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
for name in ['style.css', 'site.js', 'favicon.svg']:
    (target / 'assets').mkdir(exist_ok=True)
    shutil.copy2(ROOT / 'assets' / name, target / 'assets' / name)
expected = {'index.html', 'CNAME', '.nojekyll', 'robots.txt', 'sitemap.xml',
            'assets/style.css', 'assets/site.js', 'assets/favicon.svg'}
actual = {str(p.relative_to(target)) for p in target.rglob('*') if p.is_file()}
if actual != expected:
    raise SystemExit(f'构建目录包含预期之外的文件，请先检查: {actual - expected}')
check(target)
print(f'站点产物已生成: {target}')
