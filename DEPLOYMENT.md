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

## 当前执行结果与剩余步骤

2026-10-14：官网源码与工作流已成功推送。首次运行 [38524750819](https://github.com/bookmagic-co/brivya.github.io/actions/runs/38524750819) 的 Validate and build 全部通过，部署在 Check Pages configuration 失败，Deploy 步骤未执行。

实际开启 Pages 的 API 请求返回 `403 Resource not accessible by integration`。管理员权限查询不代表 GitHub 集成具有 Pages API 写权限。官方 configure-pages 的自动启用参数也要求非 GITHUB_TOKEN 的额外权限，因此不通过添加未提供的 token 绕过此步骤。

管理员需在仓库 Settings → Pages 将 Source 选择为 GitHub Actions。然后重跑失败的部署 job 或手动触发工作流。先验证默认站点 `https://bookmagic-co.github.io/brivya.github.io/`；自定义域名验证完成后，在同一页面设置 `brivya.com`，按 DOMAIN.md 配置腾讯云 DNS 与 HTTPS。

源码与 CI 已完成；Pages 首次上线、正式域名和 HTTPS 验证仍待完成。不要在聊天中提供 token。
