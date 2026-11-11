"""Offline tests for the reusable QSIS cross-contract conformance validator."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("validate_qsis.py")
ACTION_HASH = "sha256:" + "a" * 64
INCEPTION_HASH = "sha256:" + "b" * 64
CONTRACT_HASH = "sha256:" + "c" * 64
SUBMISSION_ID = "22222222-2222-4222-8222-222222222222"
JOB_ID = "33333333-3333-4333-8333-333333333333"


def write_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def valid_manifest() -> dict:
    return {
        "contract": "qfoldit.qsis.capability-manifest/0.1",
        "capability_id": "test.compute.operation",
        "semantic_version": "1.0.0",
        "title": "Test capability",
        "description": "Synthetic test capability for offline conformance.",
        "domain": "test",
        "operation": "compute",
        "provider": {
            "provider_id": "test-provider",
            "implementation_id": "test-impl",
            "provider_version": "1.0.0",
        },
        "input": {"schema_uri": "urn:test:input:1", "content_types": ["application/json"]},
        "output": {"schema_uri": "urn:test:output:1", "content_types": ["application/json"]},
        "execution": {
            "modes": ["sync"],
            "idempotent": True,
            "cancellable": False,
            "async_job_status": False,
        },
        "authority": {
            "role": "compute_only",
            "can_issue_evidence": False,
            "independent_validation_required": True,
        },
        "provenance": {
            "required_fields": [
                "mission_id",
                "mission_inception_sha256",
                "input_artifact_sha256",
                "provider_version",
            ],
            "output_digest_algorithm": "sha256",
        },
        "data_handling": {
            "deployment_modes": ["local_device"],
            "data_residency": ["test-only"],
            "sensitive_data_supported": False,
            "egress_policy": "no_external_egress",
        },
        "artifacts": {"accepted_formats": ["json"], "produced_formats": ["json"]},
    }


def valid_action() -> dict:
    return {
        "contract": "qfoldit.scientific-action-envelope/1.1",
        "envelopeId": "11111111-1111-4111-8111-111111111111",
        "missionId": "mission-test",
        "missionInceptionSha256": INCEPTION_HASH,
        "sessionId": "session-test",
        "actorType": "HUMAN",
        "actorId": "tester",
        "scientificObjectId": "object-test",
        "schemaVersion": "sos/1.1",
        "stateId": "state-1",
        "parentStateId": None,
        "actionType": "atomic.energy.single_point",
        "actionPayload": {"test": True},
        "runtimeId": "foldnite-test",
        "adapterVersion": "1.0.0",
        "timestamp": "2026-11-11T10:00:00Z",
        "contentHash": ACTION_HASH,
    }


def valid_evidence() -> dict:
    return {
        "evidenceId": "44444444-4444-4444-8444-444444444444",
        "evidenceContract": "qfoldit.evidence/1.2",
        "missionId": "mission-test",
        "missionVersion": "1.0.0",
        "missionInceptionSha256": INCEPTION_HASH,
        "submissionId": SUBMISSION_ID,
        "actionEnvelopeHash": ACTION_HASH,
        "runtimeId": "foldnite-test",
        "runtimeAdapterVersion": "1.0.0",
        "validatorId": "test-validator",
        "validatorVersion": "1.0.0",
        "engine": "test-engine",
        "engineVersion": "1.0.0",
        "jobId": "validation-job-1",
        "referenceId": "test-reference",
        "referenceSha256": "d" * 64,
        "modelSha256": "e" * 64,
        "artifactReferences": ["artifact://candidate/1"],
        "validationStatus": "accepted",
        "score": 0.9,
        "validationVersion": "profile/1.0",
        "createdAt": "2026-11-11T10:01:00Z",
        "completedAt": "2026-11-11T10:02:00Z",
        "contentHash": "sha256:" + "f" * 64,
    }


class QsisManifestValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.capability_dir = self.root / "qsis" / "capabilities"
        self.schema_dir = self.root / "qsis" / "schemas"
        self.schema_dir.mkdir(parents=True)
        self.input_schema = {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "$id": "urn:test:input:1",
            "type": "object",
            "required": ["temperature"],
            "properties": {"temperature": {"type": "number", "minimum": 0}},
            "additionalProperties": False,
        }
        self.output_schema = {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "$id": "urn:test:output:1",
            "type": "object",
            "required": ["result"],
            "properties": {"result": {"type": "number"}},
            "additionalProperties": False,
        }
        write_json(self.schema_dir / "input.schema.json", self.input_schema)
        write_json(self.schema_dir / "output.schema.json", self.output_schema)
        self.manifest = valid_manifest()
        write_json(self.capability_dir / "test.json", self.manifest)
        self.manifest_path = self.root / "qsis" / "capabilities" / "test.json"
        self.manifest_digest = "sha256:" + hashlib.sha256(self.manifest_path.read_bytes()).hexdigest()

    def write_execution_chain(self) -> tuple[Path, Path, Path, Path]:
        action_path = self.root / "action.json"
        write_json(action_path, valid_action())
        request = {
            "contract": "qfoldit.qsis.scientific-job-request/0.1",
            "job_id": JOB_ID,
            "mission": {
                "mission_id": "mission-test",
                "mission_version": "1.0.0",
                "mission_inception_sha256": INCEPTION_HASH,
                "mission_contract_sha256": CONTRACT_HASH,
                "submission_id": SUBMISSION_ID,
                "action_envelope_sha256": ACTION_HASH,
            },
            "subject": {
                "scientific_object_id": "object-test",
                "schema_id": "qfoldit.atomic-structure",
                "schema_version": "1.0",
            },
            "capability": {
                "capability_id": self.manifest["capability_id"],
                "manifest_sha256": self.manifest_digest,
                "provider_constraint": "test-provider",
            },
            "inputs": [{
                "artifact_id": "input-1",
                "uri": "artifact://input/1",
                "media_type": "application/json",
                "format": "json",
                "sha256": "sha256:" + "1" * 64,
                "size_bytes": 128,
                "license_ref": "MIT",
                "rights_ref": "test-rights",
            }],
            "parameters": {"temperature": 298.15},
            "execution": {
                "mode": "sync",
                "idempotency_key": "test-idempotency-key-0001",
                "deadline": "2026-11-11T10:10:00Z",
                "resource_budget": {"max_runtime_seconds": 60},
                "random_seed": 17,
            },
            "authorization": {
                "status": "approved",
                "approval_ref": "approval-test-1",
                "approved_by": "mission-owner",
                "approved_at": "2026-11-11T09:59:00Z",
                "required_scopes": ["test.compute"],
                "data_residency_policy": "local",
            },
        }
        request_path = self.root / "request.json"
        write_json(request_path, request)
        result = {
            "contract": "qfoldit.qsis.scientific-job-result/0.1",
            "job_id": JOB_ID,
            "status": "succeeded",
            "mission": {
                "mission_id": "mission-test",
                "mission_inception_sha256": INCEPTION_HASH,
                "submission_id": SUBMISSION_ID,
                "action_envelope_sha256": ACTION_HASH,
            },
            "capability": {
                "capability_id": self.manifest["capability_id"],
                "manifest_sha256": self.manifest_digest,
            },
            "provider": {
                "provider_id": "test-provider",
                "implementation_id": "test-impl",
                "provider_version": "1.0.0",
            },
            "timing": {
                "started_at": "2026-11-11T10:00:01Z",
                "finished_at": "2026-11-11T10:00:02Z",
                "elapsed_seconds": 1.0,
            },
            "outputs": [{
                "artifact_id": "output-1",
                "uri": "artifact://output/1",
                "media_type": "application/json",
                "format": "json",
                "sha256": "sha256:" + "2" * 64,
                "size_bytes": 128,
            }],
            "execution_provenance": {
                "parameters_sha256": "sha256:" + "3" * 64,
                "environment": {"test": True},
            },
            "metrics": {"result": 1.0},
            "warnings": [],
            "limitations": ["Synthetic test only."],
            "error": None,
            "scientific_validation_status": "NOT_PERFORMED",
            "evidence_status": "NOT_CREATED",
        }
        result_path = self.root / "result.json"
        write_json(result_path, result)
        evidence_path = self.root / "evidence.json"
        write_json(evidence_path, valid_evidence())
        return request_path, result_path, action_path, evidence_path

    def run_validator(self, *extra_args: str) -> subprocess.CompletedProcess:
        return subprocess.run(
            [sys.executable, str(SCRIPT), "--target-root", str(self.root), *extra_args,
             "qsis/capabilities/test.json"],
            cwd=self.root,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_valid_manifest_passes_and_reports_digest(self) -> None:
        result = self.run_validator()
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        self.assertIn("[PASS] QSIS capability test.compute.operation", result.stdout)

    def test_unresolved_input_schema_fails_closed(self) -> None:
        self.manifest["input"]["schema_uri"] = "urn:test:missing:1"
        write_json(self.manifest_path, self.manifest)
        result = self.run_validator()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("input.schema_uri is not resolved", result.stderr)

    def test_duplicate_capability_id_fails(self) -> None:
        write_json(self.capability_dir / "two.json", self.manifest)
        result = self.run_validator("qsis/capabilities/two.json")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("duplicate capability_id", result.stderr)

    def test_provider_cannot_claim_evidence_authority(self) -> None:
        self.manifest["authority"]["can_issue_evidence"] = True
        write_json(self.manifest_path, self.manifest)
        result = self.run_validator()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("False was expected", result.stderr)

    def test_duplicate_local_schema_ids_fail(self) -> None:
        write_json(self.schema_dir / "duplicate.schema.json", self.input_schema)
        result = self.run_validator()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("duplicate QSIS schema $id", result.stderr)

    def test_full_job_action_and_evidence_lineage_passes(self) -> None:
        request, result_file, action, evidence = self.write_execution_chain()
        outcome = self.run_validator(
            "--job-request", str(request),
            "--job-result", str(result_file),
            "--action-envelope", str(action),
            "--evidence-record", str(evidence),
        )
        self.assertEqual(outcome.returncode, 0, outcome.stderr + outcome.stdout)
        self.assertIn("QSIS Job Request/Result lineage", outcome.stdout)
        self.assertIn("Action Envelope 1.1 mission/hash binding", outcome.stdout)
        self.assertIn("Evidence 1.2 schema and mission/action/submission lineage", outcome.stdout)

    def test_job_request_requires_approved_authorization(self) -> None:
        request, result_file, _, _ = self.write_execution_chain()
        data = json.loads(request.read_text(encoding="utf-8"))
        data["authorization"]["status"] = "pending"
        write_json(request, data)
        outcome = self.run_validator("--job-request", str(request), "--job-result", str(result_file))
        self.assertNotEqual(outcome.returncode, 0)
        self.assertIn("authorization.status=approved", outcome.stderr)

    def test_result_cannot_claim_evidence_was_created_by_provider(self) -> None:
        request, result_file, _, _ = self.write_execution_chain()
        data = json.loads(result_file.read_text(encoding="utf-8"))
        data["evidence_status"] = "CREATED"
        write_json(result_file, data)
        outcome = self.run_validator("--job-request", str(request), "--job-result", str(result_file))
        self.assertNotEqual(outcome.returncode, 0)
        self.assertIn("NOT_CREATED", outcome.stderr)

    def test_result_must_match_manifest_provider_version(self) -> None:
        request, result_file, _, _ = self.write_execution_chain()
        data = json.loads(result_file.read_text(encoding="utf-8"))
        data["provider"]["provider_version"] = "9.9.9"
        write_json(result_file, data)
        outcome = self.run_validator("--job-request", str(request), "--job-result", str(result_file))
        self.assertNotEqual(outcome.returncode, 0)
        self.assertIn("provider.provider_version", outcome.stderr)


if __name__ == "__main__":
    unittest.main()
