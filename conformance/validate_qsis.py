#!/usr/bin/env python3
"""Validate QSIS capabilities and cross-contract execution lineage.

The legacy qFoldIT adapter validator remains a separate compatibility gate.
This validator performs static contract checks; it does not authenticate
publishers, verify asymmetric signatures, or qualify a live scientific service.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

HERE = Path(__file__).resolve().parent
QSIS_SCHEMA_ROOT = HERE / "qsis" / "0.1"
CAPABILITY_SCHEMA = QSIS_SCHEMA_ROOT / "scientific-capability-manifest.schema.json"
JOB_REQUEST_SCHEMA = QSIS_SCHEMA_ROOT / "scientific-job-request.schema.json"
JOB_RESULT_SCHEMA = QSIS_SCHEMA_ROOT / "scientific-job-result.schema.json"
ACTION_SCHEMA = QSIS_SCHEMA_ROOT / "scientific-action-envelope-v1.1.schema.json"
EVIDENCE_SCHEMA = QSIS_SCHEMA_ROOT / "qfoldit-evidence-record-v1.2.schema.json"
FORMAT_CHECKER = FormatChecker()


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"{path}: invalid JSON: {exc}") from exc


def validate_document(value: Any, schema_path: Path, label: str) -> None:
    schema = load_json(schema_path)
    Draft202012Validator.check_schema(schema)
    Draft202012Validator(schema, format_checker=FORMAT_CHECKER).validate(value)


def schema_catalog(target_root: Path) -> dict[str, tuple[Path, dict[str, Any]]]:
    catalog: dict[str, tuple[Path, dict[str, Any]]] = {}
    schema_root = target_root / "qsis" / "schemas"
    if not schema_root.exists():
        return catalog
    for path in sorted(schema_root.rglob("*.schema.json")):
        value = load_json(path)
        if not isinstance(value, dict) or not isinstance(value.get("$id"), str):
            raise ValueError(f"{path}: each QSIS schema must declare a string $id")
        schema_id = value["$id"]
        if schema_id in catalog:
            raise ValueError(f"duplicate QSIS schema $id: {schema_id}")
        Draft202012Validator.check_schema(value)
        catalog[schema_id] = (path, value)
    return catalog


def manifest_digest(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def validate_manifest(
    manifest_path: Path,
    schema: dict[str, Any],
    schema_index: dict[str, tuple[Path, dict[str, Any]]],
) -> tuple[str, str, dict[str, Any]]:
    manifest = load_json(manifest_path)
    Draft202012Validator(schema, format_checker=FORMAT_CHECKER).validate(manifest)
    for direction in ("input", "output"):
        schema_uri = manifest[direction]["schema_uri"]
        if schema_uri not in schema_index:
            raise ValueError(
                f"{manifest_path}: {direction}.schema_uri is not resolved by "
                f"a committed qsis/schemas/*.schema.json $id: {schema_uri}"
            )
    digest = manifest_digest(manifest_path)
    return manifest["capability_id"], digest, manifest


def validate_execution_chain(
    manifest_path: Path,
    manifest: dict[str, Any],
    request_path: Path,
    result_path: Path,
    schema_index: dict[str, tuple[Path, dict[str, Any]]],
    action_path: Path | None,
    evidence_path: Path | None,
) -> None:
    if action_path is None and evidence_path is not None:
        raise ValueError("--evidence-record requires --action-envelope")

    request = load_json(request_path)
    result = load_json(result_path)
    validate_document(request, JOB_REQUEST_SCHEMA, "QSIS Job Request")
    validate_document(result, JOB_RESULT_SCHEMA, "QSIS Job Result")

    expected_manifest_digest = manifest_digest(manifest_path)
    if request["capability"]["capability_id"] != manifest["capability_id"]:
        raise ValueError("Job Request capability_id does not match selected manifest")
    if request["capability"]["manifest_sha256"] != expected_manifest_digest:
        raise ValueError("Job Request manifest_sha256 does not match selected manifest digest")
    if request["authorization"]["status"] != "approved":
        raise ValueError("executed Job Request must have authorization.status=approved")
    if request["execution"]["mode"] not in manifest["execution"]["modes"]:
        raise ValueError("Job Request execution.mode is not declared by capability manifest")

    input_schema_uri = manifest["input"]["schema_uri"]
    output_schema_uri = manifest["output"]["schema_uri"]
    input_schema = schema_index[input_schema_uri][1]
    output_schema = schema_index[output_schema_uri][1]
    Draft202012Validator(input_schema, format_checker=FORMAT_CHECKER).validate(
        request["parameters"]
    )

    request_mission = request["mission"]
    result_mission = result["mission"]
    for key in ("mission_id", "mission_inception_sha256"):
        if result_mission[key] != request_mission[key]:
            raise ValueError(f"Job Result mission.{key} does not match Job Request")
    if request["job_id"] != result["job_id"]:
        raise ValueError("Job Result job_id does not match Job Request")
    if request["capability"] != result["capability"]:
        raise ValueError("Job Result capability binding does not match Job Request")
    if result_mission.get("action_envelope_sha256") != request_mission.get("action_envelope_sha256"):
        raise ValueError("Job Result action envelope hash does not match Job Request")

    provider = manifest["provider"]
    result_provider = result["provider"]
    for key in ("provider_id", "implementation_id", "provider_version"):
        if result_provider[key] != provider[key]:
            raise ValueError(f"Job Result provider.{key} does not match capability manifest")
    if "metrics" in result:
        Draft202012Validator(output_schema, format_checker=FORMAT_CHECKER).validate(
            result["metrics"]
        )
    if result["scientific_validation_status"] != "NOT_PERFORMED":
        raise ValueError("provider Job Result must not claim scientific validation")
    if result["evidence_status"] != "NOT_CREATED":
        raise ValueError("provider Job Result must not claim qFoldIT Evidence creation")

    if action_path is not None:
        action = load_json(action_path)
        validate_document(action, ACTION_SCHEMA, "Scientific Action Envelope 1.1")
        if request_mission.get("action_envelope_sha256") != action["contentHash"]:
            raise ValueError("Job Request action_envelope_sha256 does not match Action Envelope contentHash")
        if action["missionId"] != request_mission["mission_id"]:
            raise ValueError("Action Envelope missionId does not match Job Request")
        if action["missionInceptionSha256"] != request_mission["mission_inception_sha256"]:
            raise ValueError("Action Envelope mission inception hash does not match Job Request")
        if request_mission.get("submission_id") is not None:
            if result_mission.get("submission_id") != request_mission["submission_id"]:
                raise ValueError("Job Result submission_id does not match Job Request")

        if evidence_path is not None:
            evidence = load_json(evidence_path)
            validate_document(evidence, EVIDENCE_SCHEMA, "Evidence Record 1.2")
            if evidence["missionId"] != action["missionId"]:
                raise ValueError("Evidence missionId does not match Action Envelope")
            if evidence["missionInceptionSha256"] != action["missionInceptionSha256"]:
                raise ValueError("Evidence mission inception hash does not match Action Envelope")
            if evidence["actionEnvelopeHash"] != action["contentHash"]:
                raise ValueError("Evidence actionEnvelopeHash does not match Action Envelope contentHash")
            if evidence["submissionId"] != request_mission.get("submission_id"):
                raise ValueError("Evidence submissionId does not match Job Request submission_id")

    print(
        f"[PASS] QSIS Job Request/Result lineage: {request['job_id']} "
        f"({result['status']})"
    )
    if action_path is not None:
        print("[PASS] Action Envelope 1.1 mission/hash binding")
    if evidence_path is not None:
        print("[PASS] Evidence 1.2 schema and mission/action/submission lineage")
        print("[INFO] This is structural lineage validation, not signature or publisher authentication.")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--target-root", type=Path, default=Path("."))
    parser.add_argument("--job-request", type=Path)
    parser.add_argument("--job-result", type=Path)
    parser.add_argument("--action-envelope", type=Path)
    parser.add_argument("--evidence-record", type=Path)
    parser.add_argument("manifests", nargs="+", type=Path)
    args = parser.parse_args()

    if (args.job_request is None) != (args.job_result is None):
        parser.error("--job-request and --job-result must be supplied together")
    if args.evidence_record is not None and args.action_envelope is None:
        parser.error("--evidence-record requires --action-envelope")
    if args.job_request is not None and len(args.manifests) != 1:
        parser.error("cross-contract execution validation requires exactly one manifest")

    schema = load_json(CAPABILITY_SCHEMA)
    Draft202012Validator.check_schema(schema)
    root = args.target_root.resolve()
    index = schema_catalog(root)
    seen: dict[str, Path] = {}
    manifest_values: list[tuple[Path, dict[str, Any]]] = []

    try:
        for input_path in args.manifests:
            path = input_path if input_path.is_absolute() else root / input_path
            capability_id, digest, manifest = validate_manifest(path, schema, index)
            if capability_id in seen:
                raise ValueError(
                    f"duplicate capability_id {capability_id}: {seen[capability_id]} and {path}"
                )
            seen[capability_id] = path
            manifest_values.append((path, manifest))
            print(f"[PASS] QSIS capability {capability_id} {digest}")

        if args.job_request is not None and args.job_result is not None:
            manifest_path, manifest = manifest_values[0]
            def rooted(path: Path) -> Path:
                return path if path.is_absolute() else root / path
            validate_execution_chain(
                manifest_path,
                manifest,
                rooted(args.job_request),
                rooted(args.job_result),
                index,
                rooted(args.action_envelope) if args.action_envelope else None,
                rooted(args.evidence_record) if args.evidence_record else None,
            )
    except Exception as exc:
        print(f"[FAIL] {exc}", file=sys.stderr)
        return 1

    print(f"[PASS] QSIS 0.1 manifests validated: {len(args.manifests)}")
    print(f"[PASS] Local input/output schema IDs resolved: {len(index)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
