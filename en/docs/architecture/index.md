# Architecture and safety

One business truth, many projections. Every mutation follows the same governed execution path.

Canonical: https://brivya.com/en/docs/architecture/
Version: 0.1.0-alpha.1
Language: en

## Layers

AI platforms and Agent Hosts

↓

DistributionProfile · REST / MCP

↓

Canonical Business Agent · BusinessRuntime

↓

Connector · ERP / CRM / POS / Business APIs





Manifests, resources, capabilities and events define the canonical contract. Protocol adapters project invocation; distribution profiles project discovery, experience and packaging. Business authority stays in the contracts and runtime.

## Mutation path

```
Validate → Authorize → Policy → Approval when required
→ Idempotency → Connector → Transaction / Audit / Event
```



BusinessRuntime owns safety semantics. LLMs do not directly mutate business databases. Adapters cannot invoke Connectors to bypass authorization, policy or approval.

## Identity and authorization

- Agent Identity is not Authorization: recognizing a caller does not grant unrestricted execution.
- Discovery is not Authorization: a Manifest describes capabilities, not mutation permission.
- Platform Identity supplies context and still requires business authorization.
- UI Confirmation is not an ApprovalRecord: a client confirmation does not replace trusted evidence.



Protocol and experience projections must preserve risk, approval, permissions, idempotency and audit semantics.

## Core modules

| Module | Responsibility | 
|  --- | --- |
| Core / Manifest | Typed contracts, parsing and validation | 
| Policy / Runtime | Policy and governed execution | 
| Experience / Distribution | Shared interaction semantics and projections | 
| SDK / CLI | Developer APIs and local contract tools | 
| Adapters / Connectors | Protocol entry points and business boundaries |

