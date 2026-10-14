# 协议与平台适配

REST 和 MCP 共享运行时，平台分发配置复用 canonical 业务语义。

Canonical: https://brivya.com/docs/adapters/
Version: 0.1.0-alpha.1
Language: zh

## REST 调用边界

REST 适配器提供与 HTTP 框架无关的执行投影：



```
POST /v0alpha1/capabilities/{capability}/execute

{
  "input": {},
  "preconditions": {}
}
```



协议元数据通过 X-Brivya-Capability-Version、X-Request-Id、X-Correlation-Id、X-Causation-Id 与 Idempotency-Key 等头传递。请求体不能声明可信身份或审批状态。



宿主 HTTP 层验证会话或认证信息，并传入可信 RestSecurityContext；适配器构造 ActionRequest 后调用 BusinessRuntime。

## MCP 工具投影

能力 `order.create@0.1.0` 投影为工具 `brivya.order.create.v0.1.0`，能力输入输出 JSON Schema 被传递给 MCP SDK。



宿主 transport/auth 层提供可信 McpContextResolver，映射已验证的会话身份、委托、审批与关联信息。工具参数仅为业务输入；MCP annotations 只是提示，不是授权。



默认上下文只包含不可信 Agent actor。缺少可信解析器时，受保护能力在 BusinessRuntime 中拒绝执行。

## WorkBuddy 与 WeChat AI

| 参考投影 | 生成内容 |
|  --- | --- |
| WorkBuddy | connector-meta.json、mcp.json、skills/business/SKILL.md |
| WeChat AI | SKILL.md、mcp.json、runtime-bridge.json、components 与注册补丁 |



这些是参考打包与一致性基线。生产发布仍需重新核对平台官方要求、资格与审核流程；不保证第三方字段和接口永远稳定。

## 适配前检查

- 投影保留输入输出 Schema、风险与权限要求。
- 高风险动作保留 canonical 审批语义。
- 幂等与审计不会被协议分支削弱。
- 客户端身份与 UI 确认不被提升为可信授权证据。



统一交互语义由 SemanticExperience 描述，再交给平台 renderer 呈现；业务动作仍绑定 canonical Capability ID。
