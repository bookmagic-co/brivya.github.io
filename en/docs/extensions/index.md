# Extension Host

Declare permissions explicitly and extend capabilities through a scoped Host API.

Canonical: https://brivya.com/en/docs/extensions/
Version: 0.1.0-alpha.1
Language: en

## Alpha baseline

The baseline includes Extension Manifest / Package, permission grants, expansion detection, install plans, Registry Client contracts, and worker / remote boundaries.



These framework contracts do not imply an existing hosted Registry or third-party marketplace.

## Effective permissions

```
Requested permissions ∩ Tenant policy ∩ Administrator grant
= Effective permissions
```



Declaring a permission does not grant it. A new version that expands privileges requires approval again. The host grants only the permitted intersection.

## Execution and secrets

```
Extension → Host API
→ Canonical Brivya Runtime / Governed platform service
```



The Host API enforces permissions. Secrets use opaque bindings rather than raw values. There is no raw secret-read Host API.

## Current limits

Phase 1 models worker and remote execution. WASM is deferred and arbitrary third-party in-process execution is outside the baseline. Validate host isolation, authorization and outbound policy before production use.



[Review runtime safety →](https://brivya.com/en/docs/architecture/)
