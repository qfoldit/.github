#!/usr/bin/env python3
"""Validate a qFoldIT adapter manifest and canonical platform fixtures."""
from __future__ import annotations

import json
import pathlib
import sys
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parent

CANONICAL_CAPABILITIES = {
    "scene.graph",
    "scene.snapshot",
    "node.create",
    "node.update",
    "node.delete",
    "node.group",
    "node.parent",
    "geometry.procedural",
    "materials",
    "camera",
    "lighting",
    "physics",
    "physics.joints",
    "interaction",
    "uag.validate",
    "uag.apply",
    "scientific.visualization",
}

SUPPORTED_ADAPTER_SPECS = {"qfoldit.engine-adapter/0.1"}
SUPPORTED_UAG_SPECS = {"qfoldit.uag/0.1"}


def fail(message: str) -> None:
    print(f"[FAIL] {message}")
    raise SystemExit(1)


def load_json(path: pathlib.Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # pragma: no cover
        fail(f"Cannot parse {path}: {exc}")


def validate_manifest(manifest: dict[str, Any]) -> None:
    if manifest.get("spec") not in SUPPORTED_ADAPTER_SPECS:
        fail(f"Unsupported adapter spec: {manifest.get('spec')}")

    engine = manifest.get("engine")
    adapter = manifest.get("adapter")
    contracts = manifest.get("contracts")
    capabilities = manifest.get("capabilities")

    if not isinstance(engine, dict) or not engine.get("id"):
        fail("Manifest must declare engine.id")
    if not isinstance(adapter, dict) or not adapter.get("id") or not adapter.get("version"):
        fail("Manifest must declare adapter.id and adapter.version")
    if not isinstance(contracts, dict) or contracts.get("uag") not in SUPPORTED_UAG_SPECS:
        fail("Manifest must declare a supported qFoldIT UAG contract")
    if not isinstance(capabilities, list):
        fail("Manifest capabilities must be an array")

    seen: set[str] = set()
    for entry in capabilities:
        if not isinstance(entry, dict):
            fail("Each capability entry must be an object")
        capability_id = entry.get("id")
        status = entry.get("status")
        level = entry.get("level")
        if not isinstance(capability_id, str) or not capability_id:
            fail("Each capability requires a non-empty id")
        if capability_id in seen:
            fail(f"Duplicate capability: {capability_id}")
        seen.add(capability_id)
        if status not in {"supported", "partial", "planned"}:
            fail(f"Unsupported capability status for {capability_id}: {status}")
        if level not in {"native", "adapter", "external"}:
            fail(f"Unsupported capability level for {capability_id}: {level}")

    missing = sorted({"scene.graph", "uag.validate", "uag.apply"} - seen)
    if missing:
        fail(f"Required capabilities missing: {', '.join(missing)}")

    unknown = sorted(seen - CANONICAL_CAPABILITIES)
    if unknown:
        print(f"[INFO] Repository-specific capabilities: {', '.join(unknown)}")

    notes = str(manifest.get("notes", ""))
    forbidden_claims = ("scientific authority", "authoritative scientific score")
    lowered = notes.lower()
    for phrase in forbidden_claims:
        if phrase in lowered:
            fail("Adapter notes must not claim scientific authority")

    print(f"[PASS] Adapter manifest: {engine.get('id')} / {adapter.get('id')} {adapter.get('version')}")


def validate_fixture(name: str) -> None:
    path = ROOT / "fixtures" / name
    data = load_json(path)
    required = {
        "mission.json": {"schema": "qfoldit.mission/1.0", "required": {"mission_id", "version", "status"}},
        "submission.json": {"schema": "qfoldit.submission/1.0", "required": {"submission_id", "mission_id", "runtime"}},
        "evidence.json": {"schema": "qfoldit.evidence/1.0", "required": {"evidence_id", "submission_id", "authority"}},
        "event.json": {"schema": "qfoldit.event/1.0", "required": {"event_id", "event_type", "occurred_at", "source", "payload"}},
    }[name]
    if data.get("schema") != required["schema"]:
        fail(f"{name}: expected {required['schema']}, got {data.get('schema')}")
    missing = sorted(required["required"] - set(data))
    if missing:
        fail(f"{name}: missing {', '.join(missing)}")
    print(f"[PASS] Fixture: {name}")


def main() -> int:
    candidate = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path("qfoldit.adapter.json")
    validate_manifest(load_json(candidate))
    for fixture in ("mission.json", "submission.json", "evidence.json", "event.json"):
        validate_fixture(fixture)
    print("[PASS] qFoldIT cross-engine conformance baseline")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
