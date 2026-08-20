#!/usr/bin/env python3
"""Validate a compiled qFoldIT UAG package without executing an engine."""
from __future__ import annotations

import json
import pathlib
import sys
from typing import Any

REQUIRED_SCHEMAS = {
    "qfoldit.mission-compiled/1.0",
    "qfoldit.uag/0.1",
    "qfoldit.mission-routing/1.0",
}


def fail(message: str) -> None:
    print(f"[FAIL] {message}")
    raise SystemExit(1)


def load(path: pathlib.Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"Cannot parse {path}: {exc}")
    if not isinstance(value, dict):
        fail("Compiled UAG package must be a JSON object")
    return value


def validate_package(package: dict[str, Any]) -> None:
    if package.get("schema") != "qfoldit.mission-compiled/1.0":
        fail(f"Unsupported compiled package schema: {package.get('schema')}")

    contracts = package.get("contracts")
    mission = package.get("mission")
    routing = package.get("routing")
    world = package.get("world")
    provenance = package.get("provenance")

    if not isinstance(contracts, dict):
        fail("Missing contracts object")
    missing_contracts = sorted(REQUIRED_SCHEMAS - set(contracts.values()))
    if missing_contracts:
        fail(f"Missing canonical contracts: {', '.join(missing_contracts)}")

    if not isinstance(mission, dict):
        fail("Missing mission object")
    for field in ("mission_id", "version"):
        if not isinstance(mission.get(field), str) or not mission[field]:
            fail(f"Mission field '{field}' must be non-empty")

    if not isinstance(routing, dict):
        fail("Missing routing object")
    if routing.get("schema") != "qfoldit.mission-routing/1.0":
        fail("Routing object must use qfoldit.mission-routing/1.0")
    if routing.get("mission_id") != mission["mission_id"]:
        fail("Routing mission_id does not match compiled mission")
    if routing.get("mission_version") != mission["version"]:
        fail("Routing mission_version does not match compiled mission")
    if routing.get("compatible") is not True:
        fail("Compiled package requires a compatible routing decision")
    if not isinstance(routing.get("selected_adapter"), str) or not routing["selected_adapter"]:
        fail("Routing must select an adapter")
    if not isinstance(routing.get("selected_engine"), str) or not routing["selected_engine"]:
        fail("Routing must select an engine")

    if not isinstance(world, dict):
        fail("Missing world object")
    if world.get("schema") != "qfoldit.uag/0.1":
        fail("World must use qfoldit.uag/0.1")
    nodes = world.get("nodes")
    if not isinstance(nodes, list) or not nodes:
        fail("World nodes must be a non-empty array")

    node_ids: set[str] = set()
    for node in nodes:
        if not isinstance(node, dict):
            fail("Every UAG node must be an object")
        node_id = node.get("id")
        node_type = node.get("type")
        if not isinstance(node_id, str) or not node_id:
            fail("Every UAG node requires a non-empty id")
        if node_id in node_ids:
            fail(f"Duplicate UAG node id: {node_id}")
        node_ids.add(node_id)
        if not isinstance(node_type, str) or not node_type:
            fail(f"UAG node {node_id} requires a type")

    if not isinstance(provenance, dict):
        fail("Missing provenance object")
    required_provenance = {"compiler", "mission_id", "routing_policy_ref"}
    missing_provenance = sorted(required_provenance - set(provenance))
    if missing_provenance:
        fail(f"Missing provenance fields: {', '.join(missing_provenance)}")
    if provenance.get("mission_id") != mission["mission_id"]:
        fail("Provenance mission_id does not match compiled mission")

    print(
        "[PASS] UAG package: "
        f"{mission['mission_id']}@{mission['version']} -> "
        f"{routing['selected_engine']}/{routing['selected_adapter']}"
    )
    print(f"[PASS] Nodes: {len(nodes)}")


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate.py <compiled-uag-package.json>")
        return 2
    validate_package(load(pathlib.Path(sys.argv[1])))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
