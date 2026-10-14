# 官网开发与自动部署流程

## 已准备

- 独立静态官网，正式域名 `brivya.com`。
- `scripts/check.py` 检查站点资源、锚点、SEO 域名与 XML。
- `scripts/build.py` 生成 `_site`，只包含公开资源，不上传开发文档与截图。
- GitHub Actions：PR 检查，`main` 检查通过后自动发布 Pages；也支持手动重新部署。
- 部署权限只在 deploy job 开启，使用 GitHub 内置短期身份，不需要 npm token。

## 创建与首次上线

1. 使用 GitHub 组织管理员身份确认目标仓库 `brivya/brivya.github.io` 是否存在。已有仓库应先检查、保留内容，再通过分支与 PR 接入。
2. 若不存在，创建公开仓库 `brivya.github.io`，归属 `brivya` 组织。
3. 在该仓库 Settings → Pages 选择 **GitHub Actions**。确认组织允许工作流运行 GitHub 官方 Pages actions。
4. 通过组织 Settings → Pages 验证 `brivya.com` 所有权。按 GitHub 生成的 TXT 信息添加到腾讯云 DNSPod。
5. 在仓库 Settings → Pages 将 Custom domain 设为 `brivya.com`。GitHub Actions 部署不依靠产物中的 CNAME 自动创建该配置。
6. 推送已审阅的本站内容到 `main`。工作流应依次通过 Validate and build、Deploy to GitHub Pages；记录实际运行链接。
7. 按 [DOMAIN.md](DOMAIN.md) 配置腾讯云 DNS。证书准备好后开启 Enforce HTTPS。
8. 验证首页、www 跳转、HTTPS、CSS/JS/SVG、robots、sitemap 与手机布局。

## 日常开发

创建 feature 分支 → 修改页面 → 本地检查与浏览器审阅 → PR → CI 通过 → 合并 main → 自动部署 → 正式站点验证。

本地命令：

```bash
python3 scripts/check.py
node --check assets/site.js
python3 scripts/build.py
python3 -m http.server 8080 --bind 127.0.0.1 --directory _site
```

发布状态不能仅由文件存在证明，必须看到 GitHub Actions 实际运行成功及正式站点响应。

## 回滚

对引入问题的提交创建 revert PR，检查通过后合并；main 自动发布恢复后的产物。不要强推覆盖历史。

## 当前执行结果

官网已转移到公开仓库 `brivya/brivya.github.io`，远端 HEAD 与转移前一致。完整提交历史及成功 CI 记录已保留，Pages 仍采用 GitHub Actions，绑定 brivya.com 并开启 Enforce HTTPS。本地 origin 已更新为新地址。

迁移说明见 [MIGRATION.md](MIGRATION.md)。后续开发、PR 和 CI 均使用 brivya 组织；腾讯云 www CNAME 的正确目标为 brivya.github.io。
