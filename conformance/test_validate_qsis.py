"""Offline tests for the reusable QSIS 0.1 manifest conformance validator."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("validate_qsis.py")


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
        "input": {
            "schema_uri": "urn:test:input:1",
            "content_types": ["application/json"],
        },
        "output": {
            "schema_uri": "urn:test:output:1",
            "content_types": ["application/json"],
        },
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
        "artifacts": {
            "accepted_formats": ["json"],
            "produced_formats": ["json"],
        },
    }


class QsisManifestValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.capability_dir = self.root / "qsis" / "capabilities"
        self.schema_dir = self.root / "qsis" / "schemas"
        self.input_schema = {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "$id": "urn:test:input:1",
            "type": "object",
        }
        self.output_schema = {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "$id": "urn:test:output:1",
            "type": "object",
        }
        write_json(self.schema_dir / "input.schema.json", self.input_schema)
        write_json(self.schema_dir / "output.schema.json", self.output_schema)

    def run_validator(self, *manifest_names: str) -> subprocess.CompletedProcess:
        return subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--target-root",
                str(self.root),
                *manifest_names,
            ],
            cwd=self.root,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_valid_manifest_passes_and_reports_digest(self) -> None:
        write_json(self.capability_dir / "valid.json", valid_manifest())
        result = self.run_validator("qsis/capabilities/valid.json")
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        self.assertIn("[PASS] QSIS capability test.compute.operation sha256:", result.stdout)
        self.assertIn("Local input/output schema IDs resolved: 2", result.stdout)

    def test_unresolved_input_schema_fails_closed(self) -> None:
        manifest = valid_manifest()
        manifest["input"]["schema_uri"] = "urn:test:missing:1"
        write_json(self.capability_dir / "missing-schema.json", manifest)
        result = self.run_validator("qsis/capabilities/missing-schema.json")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("input.schema_uri is not resolved", result.stderr)

    def test_duplicate_capability_id_fails(self) -> None:
        write_json(self.capability_dir / "one.json", valid_manifest())
        write_json(self.capability_dir / "two.json", valid_manifest())
        result = self.run_validator(
            "qsis/capabilities/one.json",
            "qsis/capabilities/two.json",
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("duplicate capability_id", result.stderr)

    def test_provider_cannot_claim_evidence_authority(self) -> None:
        manifest = valid_manifest()
        manifest["authority"]["can_issue_evidence"] = True
        write_json(self.capability_dir / "evidence-authority.json", manifest)
        result = self.run_validator("qsis/capabilities/evidence-authority.json")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("True was expected", result.stderr)

    def test_duplicate_local_schema_ids_fail(self) -> None:
        write_json(self.schema_dir / "duplicate.schema.json", self.input_schema)
        write_json(self.capability_dir / "valid.json", valid_manifest())
        result = self.run_validator("qsis/capabilities/valid.json")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("duplicate QSIS schema $id", result.stderr)


if __name__ == "__main__":
    unittest.main()
