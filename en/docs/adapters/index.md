# Protocols and platforms

REST and MCP share the runtime. Distribution profiles reuse canonical business semantics.

Canonical: https://brivya.com/en/docs/adapters/
Version: 0.1.0-alpha.1
Language: en

## REST boundary

The REST adapter is an HTTP-framework-neutral execution projection:



```
POST /v0alpha1/capabilities/{capability}/execute

{
  "input": {},
  "preconditions": {}
}
```



Protocol metadata uses X-Brivya-Capability-Version, X-Request-Id, X-Correlation-Id, X-Causation-Id and Idempotency-Key headers. The body cannot assert trusted identity or approval state.



The hosting HTTP layer verifies authentication or session state and supplies a trusted RestSecurityContext. The adapter constructs an ActionRequest and calls BusinessRuntime.

## MCP projection

The capability `order.create@0.1.0` becomes the tool `brivya.order.create.v0.1.0`. Input and output JSON Schemas pass through to the MCP SDK.



The hosting transport/auth layer supplies a trusted McpContextResolver for verified identity, delegation, approvals and correlation metadata. Tool arguments are business input only. MCP annotations are hints, not authorization.



The default context contains only an untrusted Agent actor. Protected capabilities fail closed without a trusted resolver.

## WorkBuddy and WeChat AI

| Reference projection | Output | 
|  --- | --- |
| WorkBuddy | connector-meta.json, mcp.json, skills/business/SKILL.md | 
| WeChat AI | SKILL.md, mcp.json, runtime-bridge.json, components and registration patch | 



These are reference generators and conformance baselines. Production publication still requires current official platform requirements, qualification and review. Third-party fields and APIs are not guaranteed stable.

## Before integration

- Preserve schemas, risk and permission requirements.
- Keep canonical approval requirements for high-risk actions.
- Preserve idempotency and audit across protocols.
- Never elevate client identity or UI confirmation into trusted authorization evidence.



SemanticExperience describes shared interactions; platform renderers provide native presentation while actions remain bound to canonical Capability IDs.

