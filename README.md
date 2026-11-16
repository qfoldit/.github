# qFoldIT / Foldnite

**Scientific mission infrastructure: from a research objective to an interactive, independently reviewable mission and evidence-backed deliverable.**

qFoldIT develops the technical and scientific infrastructure behind **Foldnite** — a modular platform for producing, executing, validating and communicating interactive scientific missions.

The platform combines scientific object and world assembly, independent validation workflows, science popularization and game design, human–AI collaboration, scientific computing, cross-engine runtime adapters, provenance and enterprise governance.

> **Product principle:** a scientific mission is not just a game level. It is a governed workflow connecting a real objective, typed scientific state, authorized execution, candidate submissions, independent review and evidence.

---

## What qFoldIT and Foldnite are

- **qFoldIT** is the organization and technology programme responsible for the scientific mission architecture, software, standards, integrations and research/production workflows.
- **Foldnite** is the modular scientific mission platform built on that infrastructure.
- **Scientific Missions** are the units of work: each has a defined objective, scientific objects, permitted methods, execution environment, acceptance criteria, validator requirements and provenance.
- **MCP** is one supported transport for exposing tools. It is not the scientific data model, mission authority or validation standard.

Foldnite is designed to serve scientific and industrial workflows across molecular and structural biology, chemistry, materials science, virtual laboratories, education and other domains where interactive collective work can contribute useful candidate solutions or observations.

## The three differentiated Foldnite modules

### 1. Scientific World & Assembly

**VBMA + SOS + SKG + SEM + UAG**

A shared representation layer for scientific objects, knowledge relationships, operations, spatial worlds and engine-neutral assembly.

- **VBMA** — Voxel–Block–Molecular Architecture: spatial and modular world-authoring grammar.
- **SOS** — Scientific Object Schema: typed scientific objects, identity and state.
- **SKG** — Scientific Knowledge Graph: relationships, claims, sources and derived knowledge.
- **SEM** — Scientific Execution Model: operations, workflows, agents, constraints and execution traces.
- **UAG** — Universal Assembly Graph: versioned, engine-neutral runtime assembly package.
- **UAG-Asset** — separate asset-origin, licensing, dependency and derivative graph; not the runtime UAG.

The same scientific meaning should survive translation between qualified runtimes. Visual simplification must not silently discard the scientific identity or relationships required by a mission.

### 2. Scientific Validation Fabric

A qFoldIT-adapted validation and reconciliation module that keeps computational output, diagnostics, independent scientific judgement and trusted evidence separate.

Its documented integration surfaces include RDKit, PoseBusters, OpenStructure and CAMEO-oriented reconciliation, with mission-specific independent validators and laboratory evidence where required.

A solver result, model score, docking score, game score or successful tool call is **not** scientific acceptance. The validator and protocol must be appropriate to the claim being assessed.

### 3. Popularization & Experience

**Pop culture + narrative + game design + learning + community**

The experience module translates approved scientific objectives into understandable and engaging interactive missions.

It covers narrative, characters, interaction design, learning experiences, visual communication, community participation and science popularization. It is a core Foldnite product module — not a decorative marketing layer.

It may explain or visualize provisional findings, but it cannot modify source scientific data, validator outcomes or evidence status.

---

## The platform services around those modules

| Block | Responsibility |
|---|---|
| **F-04 — Mission Control & Scientific Mission Factory** | Mission Inception, scientific triage, Protocol Lock, Mission Contract, AGDM, Gameplay IR, compilation, routing and mission orchestration |
| **F-05 — Scientific Computing & Scientific MCP Mesh** | Versioned scientific capabilities and bounded computation through MCP or other declared provider interfaces |
| **F-06 — Human–AI Collective Work & Agent Runtime** | Coordination of scientists, players, designers, operators and bounded AI agents |
| **F-07 — Mission Production, Runtime & Toolbelts** | Materialization and execution through engine-specific adapters and creator tools |
| **F-08 — Evidence & Provenance Trust Plane** | Verification of mission lineage, validator attestations and integrity before trusted Evidence publication |
| **F-09 — Enterprise & Commercial Governance** | Partner/tenant policy, identity, rights, budgets, disclosure, delivery, attribution and settlement |
| **F-10 — Standards, Schemas & Conformance Registry** | Normative standards, machine-readable schemas, compatibility rules, migrations and conformance tests |

The ten blocks are governed as one interoperable platform. They are not ten independent products and they are not required to connect through uncontrolled all-to-all calls. Mission Control and explicit typed adapters govern the hand-offs.

## Interoperability standards

Two internal qFoldIT standards define the current compatibility baseline:

- **Foldnite Interoperability Contract (FIC) 1.0** — common identity, mission, schema, object, artifact, event, rights, trace and version context for every Foldnite block.
- **QSIS Core 1.0** — scientific-provider profile for capabilities, scientific jobs, observations, formats, provenance, authority and validation hand-off.

**MCP remains transport and tool discovery. FIC defines cross-block context. QSIS defines scientific interoperability semantics.**

The normative documents and executable registry are maintained in [qfoldit/UAG-SOS](https://github.com/qfoldit/UAG-SOS):

- [Foldnite Block Interoperability Contract 1.0](https://github.com/qfoldit/UAG-SOS/blob/main/STANDARDS/FOLDNITE/FOLDNITE-BLOCK-INTEROPERABILITY-1.0.md)
- [QSIS Core 1.0](https://github.com/qfoldit/UAG-SOS/blob/main/STANDARDS/QSIS/QSIS-CORE-AND-PROVIDER-COMPATIBILITY-1.0.md)
- [Machine-readable block registry](https://github.com/qfoldit/UAG-SOS/blob/main/SCHEMAS/FOLDNITE/foldnite-block-interface-registry-1.0.json)
- [Individual F-01…F-10 interface manifests](https://github.com/qfoldit/UAG-SOS/tree/main/SCHEMAS/FOLDNITE/BLOCKS)

These are adopted **internal qFoldIT requirements**, not claims of formal ISO, IEC, IEEE, IETF or other standards-body ratification.

### Compatibility is an evidence-based status

The standard makes full compatibility mandatory as a target. It does not mean every existing provider or runtime has already passed.

| Level | Meaning |
|---|---|
| F0 | Declared |
| F1 | Schema aligned |
| F2 | Contract tested |
| F3 | Integrated producer/consumer compatibility — required before calling a block fully compatible |
| F4 | Operationally qualified — production release gate |

The current registry records all ten blocks at **F0 for FIC conformance** while the new cross-block schemas, fixtures and integration receipts are completed. This does not erase existing working subsystems; it means the new platform-wide compatibility claim has not yet been proven.

Scientific providers have their own QSIS qualification gates. A catalogue entry or MCP endpoint is not automatically a qualified provider.

---

## The Scientific Mission lifecycle

The intended end-to-end workflow is:

```text
Customer / Research / Industrial Objective
                  |
                  v
          Mission Inception
                  |
                  v
       Scientific Triage / Protocol Lock
                  |
                  v
         Approved Mission Contract
                  |
                  v
        SOS / SKG / SEM + AGDM / IR
                  |
                  v
         UAG + Experience Packages
                  |
                  v
       Qualified Runtime / Mission Room
                  |
                  v
       Human + AI Collective Work
                  |
                  v
         Candidate Submission
                  |
                  v
      Claim-specific Independent Review
                  |
                  v
       Evidence & Provenance Boundary
                  |
                  v
       Enterprise Delivery / Settlement
```

Not every deployment currently implements every stage end to end. The mission contract, qualification state and evidence record must say what is implemented, what was actually executed and what remains open.

## Runtime and scientific provider strategy

Foldnite is designed to be runtime- and provider-neutral.

**Runtime targets:** UEFN / Unreal, Unity, UNIGINE, Web and VR. Each engine and target profile requires its own adapter and qualification evidence. A documented target is not automatically a production integration.

**Scientific capability providers:** protein and structure workflows, GLAM, atomistic/materials computing, quantum backends, chemistry tooling, laboratory/virtual-laboratory systems and other domain-specific providers.

Provider integration is staged and operation-specific. For example, the GLAM adapter documents a bounded adaptive molecular-property training/model-selection workflow and its MCP wrapper remains experimental. Atomic-MCP, nested Protein MCP tools and quantum backends retain their own open qualification gates. NVIDIA BioNeMo/NIM and Dell AI Factory/NVIDIA AI-Q are considered provider/infrastructure reference patterns, not proof of live qFoldIT production connections.

## Validation, evidence and commercial authority

The architecture deliberately separates four outcomes:

1. **Execution:** a provider or runtime ran and returned an explicit job outcome.
2. **Scientific validation:** an approved validator assessed a defined claim under a defined protocol.
3. **Evidence publication:** the trusted evidence boundary verified authority and integrity and published the evidence record.
4. **Commercial acceptance:** the enterprise/customer policy determined delivery, attribution or settlement.

A provider cannot issue its own trusted Evidence record. A validator returns an attestation to the separate trust boundary. Commercial logic cannot change a scientific finding.

Evidence 1.2 is the target trust-plane record for new qualified missions. Its production publisher, signed validator-attestation verification, durable append-only storage and key lifecycle remain explicit qualification gates.

## Relationship to Foldit and open research

Foldit (publicly introduced in 2008) is an important predecessor demonstrating how human spatial reasoning and game mechanics can contribute to scientific research.

qFoldIT/Foldnite continues and extends the **idea of scientific game-based collective search** through its own mission contracts, object models, validation boundaries, world-assembly system and runtime integrations. This is feature-level and architectural continuity — not a claim of wholesale source-code reuse, legal succession or ownership of upstream Foldit intellectual property.

qFoldIT combines proprietary and open components. Every repository, upstream model, dataset, asset and dependency retains its applicable licence and provenance. Public visibility of a repository or internal permission to integrate a component does not automatically grant third-party ownership or redistribution rights.

## Current engineering status

The principal implementation repositories are:

- [UEFN-QFOLDIT](https://github.com/qfoldit/UEFN-QFOLDIT) — canonical Rust/Tauri mission and control plane.
- [UAG-SOS](https://github.com/qfoldit/UAG-SOS) — normative standards, schemas, governance and runbooks.
- [RANDOM42](https://github.com/qfoldit/RANDOM42) — level, scene, laboratory asset and production workflow.
- [CORPORATE_APP](https://github.com/qfoldit/CORPORATE_APP) — enterprise, tenant, rights and commercial governance.
- [OPENSTRUCTURE](https://github.com/qfoldit/OPENSTRUCTURE) — structural computation/validation boundary and upstream integration.
- [GLAM](https://github.com/qfoldit/GLAM) — GLAM research implementation and qFoldIT adapter.
- [CAMEO-REALTIME-VALIDATION](https://github.com/qfoldit/CAMEO-REALTIME-VALIDATION) — realtime reconciliation boundary.
- [INDUSTRIAL-CAMEO](https://github.com/qfoldit/INDUSTRIAL-CAMEO) — industrial mission routing and reconciliation.
- [Atomic-MCP](https://github.com/qfoldit/Atomic-MCP) — atomistic/materials provider, currently qualification-gated.
- [Protein-Design-MCP](https://github.com/qfoldit/Protein-Design-MCP) — upstream-derived MCP distribution and separately licensed qFoldIT skill bundle; not currently qualified as a qFoldIT QSIS provider.
- [Foldnite–Sirius Partnership](https://github.com/qfoldit/Foldnite-Sirius-Partnership) — partnership and Snezhinka/Yamal programme records.

The canonical Foldnite 0.7.0 repository is build-capable for local development, but release-verified status is not claimed. Native Lore integration, governed UEFN materialization, reproducible dependency locks, production signing and verified target builds remain gates. GitHub Actions workflows and code-level tests must be distinguished from successful runner-executed results.

## How to explore and collaborate

Start with the [qFoldIT organization repositories](https://github.com/qfoldit) and the [UAG-SOS standards registry](https://github.com/qfoldit/UAG-SOS).

Useful entry points:

- [Foldnite technical mission lifecycle](https://github.com/qfoldit/UEFN-QFOLDIT/blob/main/docs/FOLDNITE-SCIENTIFIC-MISSION-GENESIS.md)
- [Foldnite platform status](https://github.com/qfoldit/UEFN-QFOLDIT/blob/main/QFOLDIT-STATUS.md)
- [Foldnite block interoperability matrix](https://github.com/qfoldit/UAG-SOS/blob/main/STANDARDS/FOLDNITE/FOLDNITE-BLOCK-INTEROPERABILITY-1.0.md)
- [QSIS Core 1.0](https://github.com/qfoldit/UAG-SOS/blob/main/STANDARDS/QSIS/QSIS-CORE-AND-PROVIDER-COMPATIBILITY-1.0.md)
- [Implementation and standards readiness audit](https://github.com/qfoldit/UAG-SOS/blob/main/GOVERNANCE/STANDARDS-READINESS-AUDIT-2026-11-11.md)

Scientific, engineering, runtime, design and enterprise collaborators should begin with the relevant repository's current interface, licence and qualification status. Please use repository Issues and Discussions for technical proposals; no partnership, endorsement, data access or production entitlement should be inferred from a documented integration target.

---

**qFoldIT builds the infrastructure. Foldnite turns scientific objectives into governed, interactive missions — and keeps execution, validation, evidence and commercial outcomes distinct.**
