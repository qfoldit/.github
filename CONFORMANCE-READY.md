# qFoldIT Conformance Readiness

The reusable qFoldIT conformance workflow is available under `.github/workflows/reusable-qfoldit-conformance.yml`.

Runtime repositories should call the reusable workflow from their own CI and pass the path to their `qfoldit.adapter.json` manifest when using the legacy compatibility contract.

## Two conformance lanes

1. **Legacy compatibility lane:** `conformance/validate.py` continues to validate existing engine/scientific-adapter manifests and the historical 1.0 fixture chain. This lane is not QSIS 0.1 qualification.
2. **QSIS 0.1 lane:** `conformance/validate_qsis.py` validates per-operation capability manifests and can validate the linked Job Request 0.1 / Job Result 0.1, Action Envelope 1.1 and Evidence 1.2 schema and cross-reference chain. The reusable workflow enables the capability lane when the target repository contains `qsis/capabilities/*.json`.

The reusable workflow also runs the QSIS validator's synthetic offline regression suite. Source schemas are mirrored from UAG-SOS and pinned by blob SHA in `conformance/qsis/0.1/`.

## Important qualification boundary

A missing QSIS manifest means the QSIS lane is not applicable to that repository revision; it is never reported as QSIS PASS. A static manifest or cross-reference PASS does not establish a live provider, canonical Rust content-hash verification, cryptographic publisher authentication, independent scientific validation or production Evidence 1.2 issuance.

## Runner status

As of 2026-11-11, selected UAG-SOS and UEFN-QFOLDIT workflow jobs were observed with `runner_id=0`, empty runner name and no steps. The repository workflows and validator code have been committed, but CI execution remains unverified until organization/repository Actions runner availability is restored. See [UAG-SOS issue #1](https://github.com/qfoldit/UAG-SOS/issues/1) and the [runner recovery runbook](https://github.com/qfoldit/UAG-SOS/blob/main/STANDARDS/OPERATIONS/GITHUB-ACTIONS-RUNNER-READINESS-AND-CI-RECOVERY-2026-11-11.md).
