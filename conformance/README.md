# qFoldIT Cross-Engine Conformance Kit

This directory defines the reusable conformance layer for qFoldIT runtime adapters and scientific mission integration.

## Purpose

The kit verifies that a repository participating in the qFoldIT platform:

1. declares a valid engine adapter manifest;
2. exposes the required qFoldIT contract identifiers;
3. declares canonical capability identifiers consistently;
4. preserves the separation between runtime validation and scientific authority;
5. can validate canonical Mission, Submission, Evidence and Event fixtures;
6. records provenance and adapter metadata in a machine-readable form.

## Required adapter contract

The current adapter manifest namespace remains:

```text
qfoldit.engine-adapter/0.1
```

The platform contract family is:

```text
qfoldit.platform/1.0
```

The UAG contract remains explicitly versioned and is currently accepted at:

```text
qfoldit.uag/0.1
```

A future UAG major version can be added without changing the conformance runner.

## Runtime roles

The following separation is normative:

```text
Runtime Adapter -> produces interaction/submission data
CAMEO -> orchestrates mission validation
Scientific Validator -> produces authoritative scientific evidence
STATE -> publishes derived, safe-to-share state
```

An engine adapter must not claim scientific authority merely because it performs a local runtime validation.

## Capability vocabulary

Canonical capabilities currently include:

- `scene.graph`
- `scene.snapshot`
- `node.create`
- `node.update`
- `node.delete`
- `node.group`
- `node.parent`
- `geometry.procedural`
- `materials`
- `camera`
- `lighting`
- `physics`
- `physics.joints`
- `interaction`
- `uag.validate`
- `uag.apply`
- `scientific.visualization`

Repositories may expose additional capabilities, but canonical identifiers must remain stable.
