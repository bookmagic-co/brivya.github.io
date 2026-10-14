# Versions and packages

Understand the public Alpha modules, installation and stability boundaries.

Canonical: https://brivya.com/en/docs/releases/
Version: 0.1.0-alpha.1
Language: en

## v0.1.0-alpha.1

The first public Alpha was released on October 3, 2026. All 14 public npm packages use `0.1.0-alpha.1` under the `next` dist-tag. Pin versions explicitly while APIs remain pre-stable.



```
npm install @brivya/sdk@0.1.0-alpha.1
npm install -g @brivya/cli@0.1.0-alpha.1
```

## Public packages

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

## Capabilities and limits

The baseline includes typed contracts, governed runtime, REST / MCP, reference distribution profiles, CLI / SDK, Restaurant E2E and Extension Host. The root workspace and Restaurant example are not published npm packages.



This version does not promise hosted Runtime, Registry, enterprise identity or automatic production platform publication. npm OIDC migration concerns release governance, not installation or website use.

## Before upgrading

- Review release notes for API and Manifest compatibility.
- Run business contract, permission, approval, idempotency and adapter tests.
- Keep canonical package versions aligned.
- Do not assume Alpha changes are stable compatibility guarantees.
