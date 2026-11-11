#!/usr/bin/env python3
"""Validate QSIS 0.1 capability manifests in an adapter repository.

The legacy qFoldIT adapter validator remains active. This validator is additive:
a QSIS capability must pass the pinned manifest schema and its input/output
schema URIs must resolve to schema files committed in the target repository.
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
CAPABILITY_SCHEMA = HERE / "qsis" / "0.1" / "scientific-capability-manifest.schema.json"


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"{path}: invalid JSON: {exc}") from exc


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


def validate_manifest(
    manifest_path: Path,
    schema: dict[str, Any],
    schema_index: dict[str, tuple[Path, dict[str, Any]]],
) -> tuple[str, str]:
    manifest = load_json(manifest_path)
    Draft202012Validator(schema, format_checker=FormatChecker()).validate(manifest)
    for direction in ("input", "output"):
        schema_uri = manifest[direction]["schema_uri"]
        if schema_uri not in schema_index:
            raise ValueError(
                f"{manifest_path}: {direction}.schema_uri is not resolved by "
                f"a committed qsis/schemas/*.schema.json $id: {schema_uri}"
            )
    digest = hashlib.sha256(manifest_path.read_bytes()).hexdigest()
    return manifest["capability_id"], digest


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--target-root", type=Path, default=Path("."))
    parser.add_argument("manifests", nargs="+", type=Path)
    args = parser.parse_args()

    schema = load_json(CAPABILITY_SCHEMA)
    Draft202012Validator.check_schema(schema)
    root = args.target_root.resolve()
    index = schema_catalog(root)
    seen: dict[str, Path] = {}

    try:
        for input_path in args.manifests:
            path = input_path if input_path.is_absolute() else root / input_path
            capability_id, digest = validate_manifest(path, schema, index)
            if capability_id in seen:
                raise ValueError(
                    f"duplicate capability_id {capability_id}: {seen[capability_id]} and {path}"
                )
            seen[capability_id] = path
            print(f"[PASS] QSIS capability {capability_id} sha256:{digest}")
    except Exception as exc:
        print(f"[FAIL] {exc}", file=sys.stderr)
        return 1

    print(f"[PASS] QSIS 0.1 manifests validated: {len(args.manifests)}")
    print(f"[PASS] Local input/output schema IDs resolved: {len(index)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
