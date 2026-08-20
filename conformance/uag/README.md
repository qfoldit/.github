# qFoldIT UAG Package Conformance

This module validates engine-neutral UAG packages produced by the qFoldIT Mission Compiler.

## Contract boundary

The validator operates on the compiled package contract and verifies:

- package schema identity;
- mission and routing identity;
- selected engine and adapter provenance;
- UAG contract version;
- node identity uniqueness;
- required node fields;
- capability declarations;
- deterministic package metadata.

It does not perform scientific validation and does not execute engine-specific code.

## Canonical pipeline

```text
Mission
  -> Mission Router
  -> Mission Compiler
  -> Compiled UAG Package
  -> UAG Conformance
  -> Engine Adapter
  -> Runtime Submission
```

## Required package identity

A compiled package must expose:

```text
qfoldit.mission-compiled/1.0
qfoldit.uag/0.1
qfoldit.mission-routing/1.0
```

The package must preserve the source mission ID/version and the routing decision selected adapter/engine.
