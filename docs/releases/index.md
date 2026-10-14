# 版本与包

了解当前 Alpha 的公开模块、安装方式与稳定性边界。

Canonical: https://brivya.com/docs/releases/
Version: 0.1.0-alpha.1
Language: zh

## v0.1.0-alpha.1

首个公开 Alpha 于 2026 年 10 月 3 日发布。14 个 npm 包版本统一为 `0.1.0-alpha.1`，使用 `next` dist-tag。API 尚未稳定，建议显式固定版本。



```
npm install @brivya/sdk@0.1.0-alpha.1
npm install -g @brivya/cli@0.1.0-alpha.1
```

## 公开包列表

- `@brivya/core`
- `@brivya/manifest`
- `@brivya/policy`
- `@brivya/runtime`
- `@brivya/experience`
- `@brivya/distribution`
- `@brivya/extensions`
- `@brivya/sdk`
- `@brivya/cli`
- `@brivya/adapter-rest`
- `@brivya/adapter-mcp`
- `@brivya/adapter-workbuddy`
- `@brivya/adapter-wechat-ai`
- `@brivya/connector-mock`

## 能力与限制

当前基线包括类型化契约、受治理运行时、REST / MCP、平台参考投影、CLI / SDK、Restaurant E2E 和 Extension Host。根工作区与 Restaurant 示例未作为公共 npm 包发布。



托管 Runtime、Registry、企业身份或正式平台自动发布不由此版本承诺。npm OIDC 迁移是发布治理工作，不是使用官网或安装公开包的前置条件。

## 升级前检查

- 阅读版本说明，确认 API 与 Manifest 兼容性。
- 先运行业务契约、权限、审批、幂等和适配器测试。
- 所有 canonical 包保持版本一致。
- 不要将 Alpha 变更视为稳定兼容保证。

