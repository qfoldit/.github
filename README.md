# qFoldIT / Foldnite

**Scientific mission infrastructure: turning research objectives into standardized, executable and independently reviewable interactive missions.**

qFoldIT develops the standards, software and production infrastructure behind **Foldnite** — a modular platform for compiling scientific and industrial tasks into interactive scientific missions and engine-adaptable gameplay experiences.

Foldnite combines scientific-world representation, mission compilation, human–AI collective work, standardized scientific computing interfaces, independent validation, provenance and enterprise delivery.

> **A Foldnite level is not an arbitrary game map. It is the interactive execution layer of a governed scientific task.** Scientific meaning, permitted actions, source identity and validation requirements are established before presentation and remain traceable throughout execution.

---

## qFoldIT and Foldnite

- **qFoldIT** develops the scientific mission architecture, software, standards, integrations and production workflows.
- **Foldnite** is the modular platform that turns scientific objectives into interactive missions.
- **A Scientific Mission** defines what is being investigated, which scientific objects and methods are in scope, what actions are allowed, how the task is executed and how candidate results are assessed.
- **A gameplay level** is one possible runtime representation of that mission — not the scientific source of truth.
- **MCP** is a tool-discovery and invocation protocol. It does not, by itself, define scientific data, authority, reproducibility or result acceptance.

The platform is designed for molecular and structural biology, chemistry, materials and atomic-scale computing, quantum workflows, virtual laboratories, education and industrial/scientific simulation.

## Three differentiated Foldnite modules

### 1. Scientific World & Assembly

**VBMA + SOS + SKG + SEM + UAG**

This module provides the common language for representing scientific objects, their relationships, operations and the worlds in which missions take place.

- **VBMA — Voxel–Block–Molecular Architecture:** a spatial and modular grammar for constructing scientific environments.
- **SOS — Scientific Object Schema:** typed scientific objects, identity, state, properties and constraints.
- **SKG — Scientific Knowledge Graph:** relationships between objects, claims, source material and derived knowledge.
- **SEM — Scientific Execution Model:** operations, workflows, agents, experiments, measurements and execution context.
- **UAG — Universal Assembly Graph:** an engine-neutral package for assembling scientific objects and environments into runtime-ready worlds.
- **UAG-Asset:** a separate record of asset origin, licence, rights, dependencies and derivatives. It is not the runtime UAG.

Together, these standards are intended to preserve scientific identity and required semantics when a mission is transformed into different visual and runtime representations. The VBMA–SOS–UAG interchange specification is currently a draft; its scope and maturity are identified in the standards registry.

### 2. Scientific Validation Fabric

The validation module separates computational output, diagnostic checks, independent scientific judgement and trusted evidence.

Its scope includes scientific data normalization, structural and molecular assessment, geometry and plausibility checks, domain-specific evaluation, reconciliation and validator-specific acceptance criteria.

Validation is selected for the scientific claim being tested. There is no universal score that can replace a domain-appropriate protocol or an independent validator.

### 3. Popularization & Experience

**Pop culture + narrative + game design + learning + community**

This module translates approved scientific objectives into engaging interactive experiences. It covers mission narrative, characters, interaction design, game mechanics, learning experiences, visual communication and community participation.

Popularization is a core Foldnite module, not a marketing layer. It makes scientific work accessible while preserving the distinction between established findings, candidate results and hypotheses.

---

## From scientific task to interactive level

Foldnite is built around a standards-driven compilation process. The objective is to transform a scientific task into an executable mission package without allowing the game layer to redefine the science.

```text
Scientific / Industrial Objective
              |
              v
     Source & Mission Inception
              |
              v
    Scientific Triage / Protocol
              |
              v
      Approved Mission Contract
              |
              v
  Standardized Scientific Objects
   + Knowledge + Execution Model
              |
              v
     Mission / Experience Compile
              |
              v
  Engine-Neutral World & Level Package
              |
              v
    Qualified Runtime / Game Level
              |
              v
     Human + AI Collective Work
              |
              v
       Candidate Submissions
              |
              v
    Independent Scientific Review
              |
              v
       Evidence & Delivery
```

At a high level, compilation connects five kinds of information:

1. **Scientific meaning:** objects, states, relations, units, constraints and source references.
2. **Mission logic:** objectives, permitted operations, task boundaries and success criteria.
3. **Execution design:** available capabilities, human and AI roles, resource limits and workflow.
4. **Experience design:** spatial representation, interaction, gameplay, learning and narrative.
5. **Runtime requirements:** the capabilities and limitations of the selected engine or delivery environment.

The compiler and adapters translate the approved mission into a standardized, engine-neutral package and then into the chosen runtime representation. The same mission can be adapted to different visual environments while preserving its canonical scientific identity, required constraints and validation policy.

This is a governed compilation pipeline, not a claim that every target engine or every mission type is already fully automated or production-qualified. Runtime-specific materialization and cross-engine semantic parity are verified separately.

## The standards system

qFoldIT uses a layered standards architecture. Each standard has a defined responsibility; no single schema is expected to describe the entire platform.

### Scientific representation and world construction

| Standard / model | Purpose |
|---|---|
| **SOS** | Identity, structure, state and typing of scientific objects |
| **SKG** | Knowledge relationships, claims and source lineage |
| **SEM** | Scientific operations, workflows, agents and execution context |
| **VBMA** | Spatial and modular construction grammar for scientific worlds |
| **UAG** | Engine-neutral world and assembly package |
| **UAG-Asset** | Asset provenance, licensing, dependencies and derivatives |

### Mission and execution contracts

Mission Inception, scientific triage, Protocol Lock and the Approved Mission Contract formalize the research question, intended use, objects, permitted operations, constraints, execution requirements and validation plan.

The mission contract acts as the controlled source for downstream compilation and execution. Runtime-specific representations must not silently broaden the approved scope or discard required scientific semantics.

### Interoperability across all Foldnite blocks

**FIC 1.0 — Foldnite Interoperability Contract**

FIC defines the common contract shared by every Foldnite block: identity, mission context, schema references, object and artifact references, versioning, traceability, rights and status semantics.

It provides a consistent way for world construction, compilation, scientific computing, validation, runtimes, evidence and enterprise services to exchange information.

### Scientific MCP standardization

**QSIS Core 1.0 — qFoldIT Scientific Interoperability Standard**

QSIS is the scientific-provider standard carried over the common FIC context. It is designed to make scientific capabilities portable across providers, organizations and execution environments.

It standardizes, at a common level:

- scientific capability discovery and per-operation manifests;
- versioned input and output schemas;
- scientific job requests, results and observations;
- identifiers, scientific formats, units and parameter conventions;
- execution states, errors, resource limits and idempotency;
- model, algorithm, dataset, software and environment provenance;
- artifact identity and content-integrity references;
- provider authority, security, data rights and policy boundaries;
- hand-off to claim-specific independent validation.

**Why this matters:** an MCP server should not be a bespoke island whose tools, payloads and meanings must be reimplemented for every client. A scientific operation should be discoverable, typed, versioned and auditable in a consistent way. A mission should be able to select or replace a qualified provider without changing the scientific meaning of the task.

MCP remains the transport and tool-discovery protocol. QSIS defines the scientific semantics above that transport. The same QSIS capability model is intended to work through MCP and other declared interfaces.

A server that merely supports MCP is not automatically QSIS-conformant. Each scientific operation must be declared and qualified at the level actually supported.

### Action integrity, validation and evidence

The platform also maintains standards for:

- **Scientific Action Envelope:** mission-bound authorization and integrity for consequential actions.
- **Validation profiles:** claim-specific roles, methods, references, limits and acceptance semantics.
- **Evidence and provenance:** the lineage connecting the mission, inputs, execution, candidate artifact, validator and result.
- **Runtime compatibility:** the requirements for translating a canonical mission into engine-specific experiences.
- **Quality and release:** checks for schemas, assets, runtime builds, provenance and release readiness.
- **Scientific agent/skill packages:** bounded capabilities and their declared inputs, outputs and execution context.

FIC 1.0 and QSIS Core 1.0 are adopted internal qFoldIT requirements. Some domain interchange and agent-package specifications remain drafts. Evidence 1.2 is the target trusted record for new qualified missions; the production issuer and parts of its downstream migration remain qualification gates. These internal standards are not represented as formal ISO, IEC, IEEE, IETF or other standards-body ratification.

The [UAG-SOS standards registry](https://github.com/qfoldit/UAG-SOS) contains the normative documents, schemas, compatibility matrix, machine-readable block registry and migration status.

## Scientific validation: execution is not proof

Foldnite deliberately separates four states:

1. **Executed:** a scientific provider or runtime performed an operation and returned an explicit result.
2. **Validated:** an approved validator assessed a defined scientific claim under an appropriate protocol.
3. **Evidenced:** the trusted evidence boundary verified the validator authority, mission binding, artifact identity and provenance before publishing a record.
4. **Accepted:** the applicable customer or enterprise process accepted the deliverable under its own terms.

A model prediction, simulation output, numerical score, gameplay result or successful MCP call does not by itself establish scientific validity.

The component that generates a candidate does not independently approve its own result. Validator authority is claim-specific and separate from the evidence publisher. Commercial or presentation logic cannot alter a scientific finding.

This separation is fundamental to making interactive scientific work reviewable, reproducible and suitable for serious research or industrial use.

## Platform services

The three product modules are supported by a connected set of platform services:

| Service | Responsibility |
|---|---|
| **Mission Control & Scientific Mission Factory** | Intake, mission qualification, contract management, compilation and orchestration |
| **Scientific Computing & Scientific MCP Mesh** | Standardized scientific capabilities and execution across domain providers |
| **Human–AI Collective Work** | Coordination of researchers, participants, designers and bounded AI agents |
| **Mission Production & Runtime** | Engine adapters, level materialization, interactive sessions and runtime receipts |
| **Evidence & Provenance Trust Plane** | Integrity, validator attestations and trusted evidence publication |
| **Enterprise & Commercial Governance** | Identity, rights, budgets, delivery, attribution and settlement |
| **Standards & Conformance Registry** | Specifications, schemas, version policy, compatibility tests and change control |

These services form one platform. They interact through explicit, typed and versioned interfaces rather than uncontrolled direct dependencies.

## Runtime and scientific domain scope

Foldnite is designed to support multiple execution environments, including UEFN / Unreal, Unity, UNIGINE, Web and VR. Each runtime has its own adapter and qualification requirements. A listed target is not automatically a verified production integration.

Scientific capability areas include protein and structural workflows, molecular chemistry, molecular-property modelling, atomistic and materials computation, quantum workflows, laboratory and virtual-laboratory execution, and industrial/scientific simulation.

Provider choice is intended to remain replaceable within the limits of scientific and mission compatibility. The standards define what a provider must declare; the qualification process determines whether a particular operation is suitable for a particular mission.

## Technical status and implementation boundaries

The main implementation and standards repositories are:

- [UEFN-QFOLDIT](https://github.com/qfoldit/UEFN-QFOLDIT) — canonical Rust/Tauri mission and control plane.
- [UAG-SOS](https://github.com/qfoldit/UAG-SOS) — standards, schemas, governance and conformance registry.
- [RANDOM42](https://github.com/qfoldit/RANDOM42) — level, scene and scientific environment production workflows.
- [CORPORATE_APP](https://github.com/qfoldit/CORPORATE_APP) — enterprise identity, policy and commercial governance.
- [OPENSTRUCTURE](https://github.com/qfoldit/OPENSTRUCTURE) — structural computation and validation boundary.
- [GLAM](https://github.com/qfoldit/GLAM) — molecular-property research implementation and qFoldIT adapter.
- [CAMEO-REALTIME-VALIDATION](https://github.com/qfoldit/CAMEO-REALTIME-VALIDATION) — validation reconciliation boundary.
- [INDUSTRIAL-CAMEO](https://github.com/qfoldit/INDUSTRIAL-CAMEO) — industrial mission and reconciliation workflows.

The repositories contain implemented components, standards, adapters, reference profiles and experimental work at different maturity levels. Production deployment, independent scientific qualification, cross-runtime parity and customer acceptance are separate evidence requirements. Documentation or a repository entry is not itself proof that an integration is live.

## Relationship to Foldit and open research

Foldit is an important public predecessor demonstrating how human spatial reasoning and game mechanics can contribute to scientific research.

qFoldIT/Foldnite continues and extends the **idea of scientific game-based collective search** through its own mission standards, scientific representations, compilation architecture, validation boundaries and runtime integrations. This is feature-level and architectural continuity — not a claim of wholesale source-code reuse, legal succession or ownership of upstream Foldit intellectual property.

qFoldIT combines original work with open and third-party components. Each upstream library, model, dataset, asset and dependency retains its own provenance and applicable licence. Public visibility or technical integration does not automatically transfer ownership or redistribution rights.

## Explore

- [qFoldIT organization](https://github.com/qfoldit)
- [Foldnite mission/control plane](https://github.com/qfoldit/UEFN-QFOLDIT)
- [Standards and schemas — UAG-SOS](https://github.com/qfoldit/UAG-SOS)
- [Foldnite system interoperability matrix](https://github.com/qfoldit/UAG-SOS/blob/main/STANDARDS/FOLDNITE/FOLDNITE-BLOCK-INTEROPERABILITY-1.0.md)
- [QSIS Core 1.0](https://github.com/qfoldit/UAG-SOS/blob/main/STANDARDS/QSIS/QSIS-CORE-AND-PROVIDER-COMPATIBILITY-1.0.md)
- [Scientific Mission genesis and lifecycle](https://github.com/qfoldit/UEFN-QFOLDIT/blob/main/docs/FOLDNITE-SCIENTIFIC-MISSION-GENESIS.md)
- [Foldnite technical status](https://github.com/qfoldit/UEFN-QFOLDIT/blob/main/QFOLDIT-STATUS.md)

---

**qFoldIT standardizes the scientific workflow. Foldnite compiles it into an interactive mission. Independent validation keeps the result accountable.**
