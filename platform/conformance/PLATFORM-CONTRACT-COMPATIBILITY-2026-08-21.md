# qFoldIT Platform Contract Compatibility — 2026-08-21

## Purpose

This document freezes the relationship between the organization-level contract family and the currently executable conformance specifications.

## Contract layers

```text
qfoldit.platform/1.0
    |
    +-- mission / submission / evidence / event contracts
    |
    +-- qfoldit.engine-adapter/0.1  (currently executable adapter conformance)
    |
    +-- qfoldit.uag/0.1            (currently executable UAG conformance)
    |
    +-- future major revisions     (compatibility must be explicit)
```

The organization platform contract is the governance family. The engine-adapter and UAG versions identify the executable compatibility level currently enforced by the reusable conformance kit.

## Authority model

```text
Mission Control Plane
    -> Mission Router / Compiler
    -> UAG / Adapter
    -> Runtime Interaction
    -> Submission / Event
    -> CAMEO
    -> Scientific Validator
    -> Evidence / Contribution Record
    -> STATE
```

The following rule is normative:

> Runtime execution may produce submission evidence, but it must never claim scientific authority merely because it can locally validate gameplay or geometry.

## Attention Capture extension

Attention Capture is a presentation/distribution layer, not a new scientific authority layer:

```text
Narrative / original or licensed presentation
    -> Quest object
    -> Mission contract
    -> UAG/MCP task
    -> Runtime interaction
    -> Human spatial search
    -> Submission/event
    -> Scientific validation
```

The extension must preserve the existing contract identifiers and cannot redefine the mission target, protected reference or scientific scoring authority.

## Evidence requirements

Every adapter participating in qFoldIT production should expose:

1. contract identifiers and versions;
2. capability manifest;
3. provenance metadata;
4. conformance result against canonical fixtures;
5. clear `supported` / `partial` / `planned` status;
6. explicit statement that scientific authority remains external to the runtime adapter.

## Versioning rule

Do not silently reinterpret a major contract version. A future `qfoldit.uag/1.0` or `qfoldit.engine-adapter/1.0` must be introduced with an explicit compatibility profile and updated conformance fixtures.
