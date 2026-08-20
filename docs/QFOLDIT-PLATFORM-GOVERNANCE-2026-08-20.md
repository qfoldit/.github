# qFoldIT Platform Governance — 2026-08-20

## Scope

This document defines the organization-level architecture governance model for the qFoldIT repositories.

## Canonical platform layers

```text
Enterprise Control Plane
    -> Mission Orchestration
    -> Scientific World / UAG
    -> Runtime Adapters
    -> Submission / Event Fabric
    -> Scientific Validation
    -> Evidence / Contribution Records
    -> STATE Projection
    -> Commercial / Governance Policy
```

## Canonical contract family

- `qfoldit.scientific-state/1.0`
- `qfoldit.scientific-object/1.0`
- `qfoldit.mission/1.0`
- `qfoldit.submission/1.0`
- `qfoldit.evidence/1.0`
- `qfoldit.contribution-record/1.0`
- `qfoldit.uag/1.0`
- `qfoldit.engine-adapter/1.0`
- `qfoldit.event/1.0`

The canonical contract registry is maintained with the qFoldIT platform architecture and currently lives in `CORPORATE_APP/contracts/`.

## Authority boundaries

### Enterprise authority

`CORPORATE_APP` owns mission lifecycle, tenant policy, application orchestration and audit references.

### Mission authority

`INDUSTRIAL-CAMEO` owns mission compilation/orchestration and domain routing.

### Scientific authority

`OPENSTRUCTURE` and domain-specific scientific services own scientific evaluation. Runtime code does not redefine scientific truth.

### World authority

Scientific Object Schema and UAG define semantic scientific objects and engine-neutral world representation.

### Runtime authority

UEFN, Unity, UNIGINE, Web and Standalone adapters own runtime realization and local interaction state.

### Public authority

STATE is a derived projection. Public clients do not become the system of record.

### Commercial authority

Reward, eligibility and payout policy remain separate from scientific scoring.

## Repository classes

- `PLATFORM_CORE` — enterprise, mission, validation, contracts and governance.
- `SCIENTIFIC` — solvers, scientific MCPs and research integrations.
- `RUNTIME` — engine and browser adapters.
- `EXPERIENCE` — labs, education and standalone products.
- `INFRASTRUCTURE` — deployment, networking and service infrastructure.
- `PUBLIC` — public website and projections.
- `EVIDENCE` — IP, prior-art, valuation and provenance registry.
- `UPSTREAM` — repositories containing significant third-party source or external technology.

## Required repository metadata

Each production repository should maintain:

1. a current README with platform role;
2. a declared contract version where applicable;
3. a declared license/provenance boundary;
4. a capability declaration for runtime adapters;
5. reproducible verification instructions;
6. an ownership/contribution record for qFoldIT-authored material.

## Development policy

Architecture documentation should follow implementation rather than block implementation. Where a capability is partially integrated, the repository should expose a precise evidence posture and a defined next conformance step.

Scientific claims, commercial claims, retention claims and third-party IP ownership claims must remain separately attributable and evidence-classified.
