#!/usr/bin/env python3
"""Validate qFoldIT adapter manifests and canonical mission fixtures."""
from __future__ import annotations
import json, pathlib, sys
from typing import Any
ROOT = pathlib.Path(__file__).resolve().parent
CAPS={"scene.graph","scene.snapshot","node.create","node.update","node.delete","node.group","node.parent","geometry.procedural","materials","camera","lighting","physics","physics.joints","interaction","uag.validate","uag.apply","scientific.visualization"}
def fail(msg:str)->None: print(f"[FAIL] {msg}"); raise SystemExit(1)
def load(p:pathlib.Path)->Any:
    try:return json.loads(p.read_text(encoding="utf-8"))
    except Exception as exc:fail(f"Cannot parse {p}: {exc}")
def manifest(m:dict[str,Any])->set[str]:
    if m.get("spec")!="qfoldit.engine-adapter/0.1":fail("Unsupported adapter spec")
    if not isinstance(m.get("engine"),dict) or not m["engine"].get("id"):fail("Missing engine.id")
    if not isinstance(m.get("adapter"),dict) or not m["adapter"].get("id"):fail("Missing adapter metadata")
    if not isinstance(m.get("contracts"),dict) or m["contracts"].get("uag")!="qfoldit.uag/0.1":fail("Unsupported UAG contract")
    seen=set()
    for e in m.get("capabilities",[]):
        cid=e.get("id"); status=e.get("status"); level=e.get("level")
        if not cid or cid in seen:fail("Invalid or duplicate capability")
        if status not in {"supported","partial","planned"} or level not in {"native","adapter","external"}:fail(f"Invalid capability declaration: {cid}")
        seen.add(cid)
    missing={"scene.graph","uag.validate","uag.apply"}-seen
    if missing:fail(f"Required capabilities missing: {', '.join(sorted(missing))}")
    for phrase in ("scientific authority","authoritative scientific score"):
        if phrase in str(m.get("notes","")).lower():fail("Runtime adapter cannot claim scientific authority")
    print(f"[PASS] Manifest: {m['engine']['id']} / {m['adapter']['id']}")
    return seen
def fixture(name:str)->dict[str,Any]:
    p=ROOT/"fixtures"/name; d=load(p)
    expected={"mission.json":"qfoldit.mission/1.0","submission.json":"qfoldit.submission/1.0","evidence.json":"qfoldit.evidence/1.0","event.json":"qfoldit.event/1.0"}[name]
    if d.get("schema")!=expected:fail(f"{name}: wrong schema")
    print(f"[PASS] Fixture: {name}");return d
def main()->int:
    caps=manifest(load(pathlib.Path(sys.argv[1])))
    mission=fixture("mission.json"); sub=fixture("submission.json"); ev=fixture("evidence.json"); event=fixture("event.json")
    if sub["mission_id"]!=mission["mission_id"] or sub["mission_version"]!=mission["version"]:fail("Submission is not linked to mission")
    if ev["submission_id"]!=sub["submission_id"]:fail("Evidence is not linked to submission")
    payload=event.get("payload",{})
    if payload.get("submission_id")!=sub["submission_id"] or payload.get("evidence_id")!=ev["evidence_id"]:fail("Event is not linked to submission/evidence")
    if event.get("event_type")!="validation.completed":fail("Unexpected conformance event type")
    req=set(mission.get("runtime_requirements",{}).get("capabilities",[])); missing=req-caps
    if missing:fail(f"Mission-required capabilities missing: {', '.join(sorted(missing))}")
    print("[PASS] Mission -> Submission -> Evidence -> Event integrity"); print("[PASS] qFoldIT cross-engine conformance baseline"); return 0
if __name__=="__main__": raise SystemExit(main())
