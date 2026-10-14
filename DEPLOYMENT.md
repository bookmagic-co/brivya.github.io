# 官网开发与自动部署流程

## 已准备

- 独立静态官网，正式域名 `brivya.com`。
- `scripts/check.py` 检查站点资源、锚点、SEO 域名与 XML。
- `scripts/build.py` 生成 `_site`，只包含公开资源，不上传开发文档与截图。
- GitHub Actions：PR 检查，`main` 检查通过后自动发布 Pages；也支持手动重新部署。
- 部署权限只在 deploy job 开启，使用 GitHub 内置短期身份，不需要 npm token。

## 创建与首次上线

1. 使用 GitHub 组织管理员身份确认目标仓库 `bookmagic-co/brivya.github.io` 是否存在。已有仓库应先检查、保留内容，再通过分支与 PR 接入。
2. 若不存在，创建公开仓库 `brivya.github.io`，归属 `bookmagic-co` 组织。
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

## 当前外部阻塞

后续状态：用户已创建公开仓库 `bookmagic-co/brivya.github.io`，当前集成已验证具有管理员与推送权限。仓库为空，正在执行首次推送与 Pages 配置。下述创建权限问题属于原 `brivya` 组织的历史结果。

2026-10-14：最初 GitHub API 被网络策略拦截，已保存 API 与站点域名访问配置。随后 API 已可访问；当前平台 GitHub 身份可管理已选产品仓，但查询官网仓库返回 404，尝试创建组织仓库时返回 `403 Resource not accessible by integration`。因此当前阻塞是 GitHub 集成权限，不能通过更换命令解决。

需由组织管理员创建公开仓库 `bookmagic-co/brivya.github.io`，并将它加入当前 GitHub 集成的授权仓库范围。完成后继续检查权限、推送并启用 Pages。不要在聊天中提供 token。Pages 与正式站点仍未上线；腾讯云 DNS 需要在实际 DNS 管理后台配置。
