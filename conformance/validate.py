#!/usr/bin/env python3
"""Validate qFoldIT adapter manifests and canonical mission fixtures."""
from __future__ import annotations

import json
import pathlib
import sys
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parent
CANONICAL_CAPABILITIES = {
    "scene.graph", "scene.snapshot", "node.create", "node.update", "node.delete",
    "node.group", "node.parent", "geometry.procedural", "materials", "camera",
    "lighting", "physics", "physics.joints", "interaction", "uag.validate",
    "uag.apply", "scientific.visualization",
}
SUPPORTED_ADAPTER_SPECS = {
    "qfoldit.engine-adapter/0.1",
    "qfoldit.scientific-adapter/1.0",
}
SUPPORTED_UAG_SPECS = {"qfoldit.uag/0.1"}


def fail(message: str) -> None:
    print(f"[FAIL] {message}")
    raise SystemExit(1)


def load_json(path: pathlib.Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"Cannot parse {path}: {exc}")


def validate_manifest(manifest: dict[str, Any]) -> set[str]:
    spec = manifest.get("spec")
    if spec not in SUPPORTED_ADAPTER_SPECS:
        fail(f"Unsupported adapter spec: {spec}")

    adapter = manifest.get("adapter")
    capabilities = manifest.get("capabilities")
    if not isinstance(adapter, dict) or not adapter.get("id") or not adapter.get("version"):
        fail("Manifest must declare adapter.id and adapter.version")
    if not isinstance(capabilities, list):
        fail("Manifest capabilities must be an array")

    if spec == "qfoldit.engine-adapter/0.1":
        engine = manifest.get("engine")
        contracts = manifest.get("contracts")
        if not isinstance(engine, dict) or not engine.get("id"):
            fail("Legacy manifest must declare engine.id")
        if not isinstance(contracts, dict) or contracts.get("uag") not in SUPPORTED_UAG_SPECS:
            fail("Legacy manifest must declare a supported qFoldIT UAG contract")
        engine_label = str(engine["id"])
    else:
        scientific_engine = manifest.get("scientific_engine")
        if not isinstance(scientific_engine, str) or not scientific_engine.strip():
            fail("Scientific manifest must declare scientific_engine")
        domain = adapter.get("domain")
        if not isinstance(domain, str) or not domain.strip():
            fail("Scientific manifest must declare adapter.domain")
        provenance = manifest.get("provenance_uri")
        if not isinstance(provenance, str) or not provenance.strip():
            fail("Scientific manifest must declare provenance_uri")
        engine_label = scientific_engine

    seen: set[str] = set()
    for entry in capabilities:
        if not isinstance(entry, dict):
            fail("Each capability entry must be an object")
        capability_id = entry.get("id")
        if not isinstance(capability_id, str) or not capability_id:
            fail("Each capability requires a non-empty id")
        if capability_id in seen:
            fail(f"Duplicate capability: {capability_id}")
        seen.add(capability_id)

        if spec == "qfoldit.engine-adapter/0.1":
            status = entry.get("status")
            level = entry.get("level")
            if status not in {"supported", "partial", "planned"}:
                fail(f"Unsupported capability status for {capability_id}: {status}")
            if level not in {"native", "adapter", "external"}:
                fail(f"Unsupported capability level for {capability_id}: {level}")
        else:
            domain = entry.get("domain")
            description = entry.get("description")
            inputs = entry.get("input_schemas")
            outputs = entry.get("output_schemas")
            validators = entry.get("validator_requirements")
            consequential = entry.get("consequential")
            if not isinstance(domain, str) or not domain.strip():
                fail(f"Scientific capability domain missing: {capability_id}")
            if not isinstance(description, str) or not description.strip():
                fail(f"Scientific capability description missing: {capability_id}")
            if not isinstance(inputs, list) or not inputs:
                fail(f"Scientific capability input_schemas missing: {capability_id}")
            if not isinstance(outputs, list) or not outputs:
                fail(f"Scientific capability output_schemas missing: {capability_id}")
            if not isinstance(validators, list):
                fail(f"Scientific capability validator_requirements missing: {capability_id}")
            if not isinstance(consequential, bool):
                fail(f"Scientific capability consequential flag missing: {capability_id}")
            if consequential and not validators:
                fail(f"Consequential capability must declare validator_requirements: {capability_id}")

    missing = sorted({"scene.graph", "uag.validate", "uag.apply"} - seen)
    if missing:
        fail(f"Required capabilities missing: {', '.join(missing)}")
    unknown = sorted(seen - CANONICAL_CAPABILITIES)
    if unknown:
        print(f"[INFO] Repository-specific capabilities: {', '.join(unknown)}")

    lowered = str(manifest.get("notes", "")).lower()
    for phrase in ("scientific authority", "authoritative scientific score"):
        if phrase in lowered:
            fail("Adapter notes must not claim scientific authority")

    print(f"[PASS] Adapter manifest: {engine_label} / {adapter.get('id')} {adapter.get('version')} [{spec}]")
    return seen


def validate_fixture(name: str) -> dict[str, Any]:
    data = load_json(ROOT / "fixtures" / name)
    expected = {
        "mission.json": ("qfoldit.mission/1.0", {"mission_id", "version", "status"}),
        "submission.json": ("qfoldit.submission/1.0", {"submission_id", "mission_id", "mission_version", "runtime"}),
        "evidence.json": ("qfoldit.evidence/1.0", {"evidence_id", "submission_id", "authority"}),
        "event.json": ("qfoldit.event/1.0", {"event_id", "event_type", "occurred_at", "source", "payload"}),
    }[name]
    schema, required = expected
    if data.get("schema") != schema:
        fail(f"{name}: expected {schema}, got {data.get('schema')}")
    missing = sorted(required - set(data))
    if missing:
        fail(f"{name}: missing {', '.join(missing)}")
    print(f"[PASS] Fixture: {name}")
    return data


def validate_chain(manifest_capabilities: set[str]) -> None:
    mission = validate_fixture("mission.json")
    submission = validate_fixture("submission.json")
    evidence = validate_fixture("evidence.json")
    event = validate_fixture("event.json")
    if submission["mission_id"] != mission["mission_id"]:
        fail("Submission mission_id does not match mission fixture")
    if submission["mission_version"] != mission["version"]:
        fail("Submission mission_version does not match mission version")
    if evidence["submission_id"] != submission["submission_id"]:
        fail("Evidence submission_id does not match submission fixture")
    payload = event.get("payload", {})
    if payload.get("submission_id") != submission["submission_id"]:
        fail("Event payload submission_id does not match submission fixture")
    if payload.get("evidence_id") != evidence["evidence_id"]:
        fail("Event payload evidence_id does not match evidence fixture")
    if event.get("event_type") != "validation.completed":
        fail("Conformance event must represent validation.completed")
    required_capabilities = mission.get("runtime_requirements", {}).get("capabilities", [])
    missing = sorted(set(required_capabilities) - manifest_capabilities)
    if missing:
        fail(f"Mission-required capabilities missing from adapter: {', '.join(missing)}")
    print("[PASS] Mission -> Submission -> Evidence -> Event integrity")


def main() -> int:
    candidate = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path("qfoldit.adapter.json")
    capabilities = validate_manifest(load_json(candidate))
    validate_chain(capabilities)
    print("[PASS] qFoldIT cross-engine conformance baseline")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
