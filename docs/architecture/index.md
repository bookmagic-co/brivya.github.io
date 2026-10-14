# 架构与安全

一份业务真相，多个平台投影；每一次变更都经过同一治理路径。

Canonical: https://brivya.com/docs/architecture/
Version: 0.1.0-alpha.1
Language: zh

## 分层模型

AI 平台与 Agent Hosts

↓

DistributionProfile · REST / MCP

↓

Canonical Business Agent · BusinessRuntime

↓

Connector · ERP / CRM / POS / Business APIs





Manifest、资源、能力与事件定义 canonical 业务契约。协议适配器负责调用投影，分发配置负责平台发现、交互与打包。业务权威保持在契约和运行时中。

## 变更执行链

```
校验 → 授权 → 策略 → 必要的审批
→ 幂等 → Connector → 事务 / 审计 / 事件
```



BusinessRuntime 执行业务安全语义。LLM 不直接修改业务数据库；适配器不能直接调用 Connector 来绕过授权、策略或审批。

## 身份与授权

- Agent Identity 不等于 Authorization：识别调用方不代表允许执行所有能力。
- Discovery 不等于 Authorization：Manifest 描述能力，不能授予变更权限。
- Platform Identity 是身份上下文，仍需经过业务授权。
- UI Confirmation 不等于 ApprovalRecord：前端确认不能替代可信审批证据。



高风险动作的审批、权限、幂等与审计语义不能被协议或体验投影削弱。

## 核心模块

| 模块 | 职责 | 
|  --- | --- |
| Core / Manifest | 类型化业务契约、解析与校验 | 
| Policy / Runtime | 策略与受治理执行 | 
| Experience / Distribution | 统一交互语义与平台投影 | 
| SDK / CLI | 开发接口与本地契约工具 | 
| Adapters / Connectors | 协议入口与业务系统边界 |

