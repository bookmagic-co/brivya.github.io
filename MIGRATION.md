# 官网归属迁移到 brivya

目标仓库：`brivya/brivya.github.io`。正式域名：`brivya.com`。

## 已确认

- 原部署仓库为 `bookmagic-co/brivya.github.io`，现已转移为 `brivya/brivya.github.io`。
- 目标仓库已确认存在，公开且当前集成具有读写权限，远端 HEAD 与转移前一致。
- 自动转移 API 原先返回 403；用户已通过 GitHub 完成转移。
- 新仓库 Pages 保留 GitHub Actions 来源、brivya.com 绑定和 Enforce HTTPS。原 CI 成功记录已随仓库保留。

## 管理员操作

1. 打开旧仓库 Settings → General → Danger Zone → Transfer ownership，将新所有者填写为 `brivya`，按 GitHub 页面提示完成确认与必要的接收操作。转移会保留仓库历史与内容。
2. 检查当前 GitHub 集成是否授权访问迁移后的仓库，按需在 `brivya` 组织的 GitHub App 安装设置中加入它。
3. 在新仓库 Settings → Pages 确认 Source 为 GitHub Actions，Custom domain 为 `brivya.com`；检查 github-pages environment 的部署分支规则。
4. 在 `brivya` 组织 Settings → Pages 检查正式域名所有权，若需要验证，将 GitHub 当场生成的 TXT 记录添加到腾讯云。
5. 确认新仓库 Pages 部署已启用后，将腾讯云 `www` 的 CNAME 目标改为 `brivya.github.io`。根域名的四条 GitHub Pages A 记录保持原值。
6. 等待 DNS 和证书就绪，确认 Enforce HTTPS 已开启。

## 接续验证

转移后应更新本地 origin 为 `https://github.com/brivya/brivya.github.io.git`，核对远端 HEAD 与原提交历史，再提交本分支的归属说明修正。重新执行 CI/Pages 部署，验证中英文首页、文档、动画、llms.txt、全文与 JSON 索引，以及 HTTP / www 跳转。

2026-10-14：仓库转移已验证，本地 origin 已更新为新组织地址。证书状态为 dns_changed，GitHub 正在重新签发；当前是否可访问以正式站点检查为准。
