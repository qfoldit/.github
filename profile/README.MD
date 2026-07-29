<!-- # **qFoldIT** is a ‭«***Universal Builder & Gamifier of Scientific***». -->  <!-- **Gamified Quantum Molecular Drug Design for Global Science** -->

<!-- ****qFoldIT**** is a ‭«***Universal Builder & Gamifier of Scientific Problems***». -->

a scientific problem describes once → the system turns it into a game of any genre →
players solve it → results flow back into the scientific graph.

[LEGO® Fortnite Cinematic Trailer](https://www.youtube.com/watch?v=GeKTrjGdJ2E)

<a href="https://www.cell.com/trends/biotechnology/abstract/S0167-7799(22)00034-8">
 <img src="https://qfoldit.github.io/assets/lego_biotech.png"/>
</a>

<a href="https://create.fortnite.com/join/2f8d8693-4fbf-4a21-ac3d-9a97efd6ed97/2b51a870-d7ef-40f8-8e57-73273fa578b3">
 <img src="https://qfoldit.github.io/assets/lego_qfoldit_hero.png"/>
</a>

<a href="https://www.bakerlab.org/">
 <img src="https://qfoldit.github.io/assets/lego_baker_lab.png"/>
</a>
<!-- # qFoldIT -- Multiplayer Gamification of Science -->
<!-- **github.com/qfoldit** -->
<br> <br>
qFoldIT builds the connective tissue between real scientific computation and shared, playable, multiplayer worlds. Its mission is straightforward: take genuine science -- protein folding, quantum simulation, drug screening, industrial process modeling -- and give it a form people can walk through, compete over, and build together, starting with Fortnite and extending across the major game and simulation engines used in research and industry today.

This document covers the full qFoldIT ecosystem: its architecture, its shipped capabilities, and the vision it's built toward.

---

<!--![](https://qfoldit.github.io/assets/lego-standarts_1.png)
![](https://qfoldit.github.io/assets/lego-standarts_2.png)
![](https://qfoldit.github.io/assets/lego-standarts_3.png)-->

# Standards

**Minimalist Presentation of Scientific Content**  
*Synced with UEFN-TOOLBELT*

---

## 1. Mission and Definition

**MPNC** — a system of rules for visualization, sound design, and interactive presentation of scientific objects inside qFoldIT.

> **Minimalist Presentation of Scientific Content (MPNC)** is a set of guidelines for visualization, sound, and interaction of scientific assets within qFoldIT, where every element serves a functional purpose, and the *absence* of an element is as meaningful as its presence.

MPNC applies to all qFoldIT output artifacts:  
`UEFN islands` · `LEGO visualizations` · `MCP agent scenarios` · `SKG infographics` · `Atomic Gameplay Engine`

---

## 2. MPNC Principles

Six axioms defining visual minimalism in qFoldIT's scientific communication.

### 01. One object – one function
Every LEGO brick, Niagara particle, or UI element fulfills exactly one semantic role. Combining functions into a single visual object is prohibited.

### 02. Color as data, not decoration
Color palette is strictly tied to physicochemical properties (CPK/LEGO hybrid). Changing hue without changing the object's property is not allowed.

### 03. Emptiness as a focusing tool
Absence of objects in the visual field is an active element of presentation. Scene "silence" is equivalent to "accent".

### 04. Animation only for operations
Any motion of particles, bricks, or camera must reflect a specific atomic operation (Construct, Connect, Transform, etc.). Decorative animation is prohibited.

### 05. Text as a last resort
Text annotations are allowed only as 3D‑labels when meaning cannot be conveyed through form, color, or sound. Limit: 3 words per element.

### 06. Unified scale law
All objects within one UAG scene obey a single scale ratio: 1 Å = N UEFN units. Scaling for "clarity" is prohibited.

---

## 3. LEGO‑CPK: Visual Alphabet

The basic unit of visualization is the LEGO brick, parameterized according to the CPK model. Brick geometry encodes chemical type; UEFN physical properties encode atomic mass.

| Element | Color | Brick type | Mass |
|---------|-------|------------|------|
| Carbon (C) | Black | 2×2 | 12.01 |
| Oxygen (O) | Red | Round | 16.00 |
| Nitrogen (N) | Blue | 2×2 | 14.01 |
| Hydrogen (H) | White | 1×1 | 1.008 |
| Sulfur (S) | Yellow | 2×2 | 32.06 |
| Phosphorus (P) | Green | 2×2 | 30.97 |
| Iron (Fe) | Purple | 2×2 | 55.85 |
| Error / Clash | Orange pulse | – | Collision |

---

## 4. UEFN Visualization Rules

Runtime constraints and requirements for Fortnite (UEFN) under MPNC.

- **R‑01. HUD Zero:** In an ideal scene, there are no 2D panels. All information is conveyed through brick glow, LEGO snap sounds, and Niagara particle physics.

- **R‑02. LOD as a scientific tool:** Distant atoms are grouped into "clouds" (aggregate particles); close‑up atoms reveal full LEGO geometry. LOD transition should match the shift in focus scale.

- **R‑03. Niagara only for emphasis:** Particles are used exclusively to mark energy transitions (formation glow, clash spark, minimization trail). Limit: at most one emitter per 10 atoms.

- **R‑04. Camera as MCP director:** Camera movement is initiated only by the MCP agent or player. Automatic cutscenes are allowed only when switching Atomic Cycles.

- **R‑05. Sound as tactile feedback:** Every LEGO snap on bond formation, every "hum" during simulation is a semantic signal. The audio layer must be recognisable without visuals.

- **R‑06. Decals as annotations:** Text labels are allowed only as Decal projections onto surfaces. Font: Inter/Segoe UI, white, outline #181818.

- **R‑07. Physics not decorative:** Ragdoll and impulses are applied only upon bond breakage or collision. "Pretty chaos" without scientific justification is prohibited.

---

## 5. MCP Protocol for Minimalist Presentation

The MCP agent acts as the director of visual storytelling. Instructions are decomposed into a UAG scene through a strict protocol.

| MCP Intent | Visual Scenario | UEFN Execution | MPNC Constraint |
|------------|-----------------|----------------|-----------------|
| `spawn_atom` | Atom appears in the scene | SpawnEmitter + brick fade‑in in 0.3s | opacity ramp only |
| `form_bond` | Chemical bond creation | MoveTo + snap sound + glow Decal | glow ≤ 0.5s |
| `mutate` | Side‑chain replacement | Disassemble (ragdoll out) → assemble (snap in) | static context |
| `minimize` | Energy optimization | Smooth drift to new coordinates + trail | trail opacity ≤ 30% |
| `validate` | Result verification | Split‑screen: target vs candidate; RMSD as 3D‑text | 2 objects max |
| `annotate` | Add metadata | Decal projection or agent voice (TTS) | text ≤ 3 words |

---

## 6. Atomic Cycles — Visual Signatures

Each of the 10 base cycles has a fixed combination of color, sound, and camera behavior.

| Cycle | Visual Signature | Sound | Camera |
|-------|------------------|-------|--------|
| **Construct** | Fade‑in white/gray brick from void | Low “thud” | Static; focus on spawn |
| **Connect** | Snap + beam between bricks; glow 0.3s | LEGO click | Micro‑zoom on bond |
| **Transform** | Rotation of brick around axis; dim trail | Mechanical “click” | Orbit 15° |
| **Optimize** | Drift to target position; plate turns green | Hum, descending pitch | Smooth pull‑back |
| **Simulate** | Vibrate all bricks; Niagara “sand” | White noise, fading out | Free fly‑around |
| **Validate** | Checkmark (green) / Cross (orange) | Positive chime / Negative buzz | Split‑screen or freeze |
| **Discover** | Burst of gold particles; brick pulses | Exalted “ding” | Slow‑motion zoom |
| **Persist** | Compress into SKG icon; fade to void | Digital “shutter” | Zoom‑out to orbital view |
| **Share** | Ghost copy flies toward player avatar | Whistle + echo | Pan across participants |
| **Iterate** | Rewind → new branch; old branch fades | Reverse whoosh + reset click | Pull‑back → reset → zoom‑in |

---

## 7. Integration with qFoldIT Architecture

MPNC intersects with all layers of qFoldIT architecture. Each component imposes constraints that become rules of presentation.

### qFoldIT Components — Runtime Mapping

| Layer | Component | Role in MPNC | Constraint |
|-------|-----------|--------------|------------|
| Science | SOS | Defines LEGO geometry and CPK color of each scientific object | `1 object = 1 brick` |
| Science | SKG | Stores visual artifacts as graph nodes; ensures 1:1 fidelity | `SKGF = 1.0` |
| Science | SEM | Decomposes scientific operations into sequences of Atomic Cycles | `only 10 cycles` |
| World | UAG | Assembles the scene from LEGO nodes with unified scale | `1 Å = N UU` |
| Interface | UWI | Translates MCP commands into UEFN calls without loss of semantics | `no magic bridge` |
| AI | MCP | Director: chooses camera, sound, presentation tempo | `text ≤ 3 words` |
| Runtime | UEFN-TOOLBELT | Generates Verse code and checks MPNC lint rules before publishing | `lint pre‑commit` |

---

## 8. Genre Adapters and Minimalism

Genre Adapters interpret Atomic Cycles into genre rules, but are not allowed to add elements outside MPNC.

| Adapter | Minimalist Interpretation | Prohibited |
|---------|---------------------------|------------|
| **Tetris** | Amino acids = tetrominoes; folding = layer stacking. Only CPK colors. | combo flashes, score pop‑ups |
| **Tower Defense** | Ligands = “enemies”, protein = “tower”. Bonds = damage zones. | health bars, damage numbers |
| **Roguelike** | Each run = a new polypeptide chain. Permadeath = unstable conformation. | skeletal animations, loot items |
| **Factory** | Metabolic pathway = conveyor. Substrates = resources, enzymes = assemblers. | smoke, sparks, extra UI icons |
| **Sandbox** | Pure LEGO playground with a limited set of bricks (SOS objects). | custom textures, free scaling |

---

## 9. Presentation Quality Metrics

Quantitative criteria for automated compliance checking against MPNC.

| Metric | Name | Description | Target |
|--------|------|-------------|--------|
| D1 | VNR (Visual Noise Ratio) | Ratio of pixels changed without scientific reason to total pixels | < 5% |
| D2 | SPD (Semantic Pixel Density) | Number of scientific parameters encoded by one visual element | ≥ 3 |
| D3 | TDI (Text Dependency Index) | % of players completing a cycle without reading a text prompt | > 85% |
| D4 | FRT (Focus Retention Time) | Continuous focus time on target object before switch | > 12 s |
| D5 | SKGF (SKG Fidelity) | Correspondence of UEFN artifact to record in Scientific Knowledge Graph | 1:1 (zero loss) |
| D6 | LAU (LEGO Authenticity) | Conformance to LEGO System standards. Reviewer: Dr. Voss. | 100% |

---

## 10. Appendices

### Appendix A. UEFN-TOOLBELT Integration

All MPNC rules are implemented as UEFN-TOOLBELT modules:  
`qfoldit.particles.minimal` · `qfoldit.camera.focus` · `qfoldit.audio.semantic`  

Each module contains lint rules that check the scene for compliance before publishing.

The MPNC color system is synchronised with `theme.py` (Ocean Bennett, UEFN-TOOLBELT). Active theme: `toolbelt_dark` — the base palette for all qFoldIT UI elements.

### Appendix B. MCP Prompt Template

Standard prompt for MCP agent:

```
Generate visual scenario for [operation] following MPNC‑v1.1.
Theme: toolbelt_dark · Max particles: [N/10] · Text: none
Sound: semantic · Camera: operation‑linked · HUD: zero
```

### Appendix C. LEGO Ideas Compliance

All LEGO visualisations published on ideas.lego.com on behalf of qFoldIT undergo review for MPNC and LEGO Authenticity before upload. Reviewer profile: **Vosslab** (Dr. Neil Voss) — official LEGO Artist, creator of Tetrisphere.

![](https://raw.githubusercontent.com/qfoldit/UEFN-TOOLBELT/main/docs/dashboard_hero.png)
<!--
## The Architecture

qFoldIT organizes its whole stack into six named layers, each with a clear job:

| Layer | Purpose |
|---|---|
| **Scientific Object Schema (SOS)** | The canonical data model for scientific objects -- proteins, molecules, materials, reactors, quantum circuits, and more -- shared across every qFoldIT tool and skill. |
| **Scientific Knowledge Graph (SKG)** | Captures the relationships between objects, experiments, and the knowledge they produce -- the living map of what's been discovered and how it connects. |
| **Scientific Execution Model (SEM)** | Describes protocols, workflows, constraints, and experiment telemetry -- the executable side of the science, covering who does what and how a run unfolds. |
| **Universal Assembly Graph (UAG)** | A real, working, engine-neutral scene-graph format already used to describe 3D worlds -- nodes, connections, constraints, and interactions that any supported engine can render. |
| **Universal World Interface (UWI)** | A translation layer connecting the abstract SOS/SKG/SEM/UAG model to the concrete tool calls of each real game engine's own live bridge -- with working implementations shipping today for Unity, Unreal, UNIGINE, and all three UEFN backends. |
| **Model Context Protocol (MCP)** | The transport layer, built on Anthropic's open MCP standard, that lets AI agents drive every tool in the stack. |

Alongside these six, **UEFN-TOOLBELT** (undergroundrap/UEFN-TOOLBELT, AGPL-3.0) is a powerful external toolkit qFoldIT integrates directly for Fortnite: 358 tools for autonomous level assembly, full world-state export, and -- uniquely -- real Verse gameplay-code generation, complementing qFoldIT's own MCP servers.

><!-- <a href="https://create.fortnite.com/join/2f8d8693-4fbf-4a21-ac3d-9a97efd6ed97/2b51a870-d7ef-40f8-8e57-73273fa578b3">
 <img src="https://qfoldit.github.io/assets/lego_l-protein.png"/>
</a> -->

<a href="https://create.fortnite.com/join/2f8d8693-4fbf-4a21-ac3d-9a97efd6ed97/2b51a870-d7ef-40f8-8e57-73273fa578b3">
 <img src="https://qfoldit.github.io/assets/lego_fortnite_Genesis_Garden.jpg"/>
</a>

<a href="https://create.fortnite.com/join/2f8d8693-4fbf-4a21-ac3d-9a97efd6ed97/2b51a870-d7ef-40f8-8e57-73273fa578b3">
 <img src="https://qfoldit.github.io/assets/lego_qfoldit.png"/>
</a>

<!-- <a href="https://www.youtube.com/watch?v=idtMsa_1yNk">
 <img src="https://qfoldit.github.io/video/claude_qfoldit.jpg"/>
</a>

<a href="https://blogs.nvidia.com/blog/claude-science-bionemo-agent-toolkit/">
 <img src="https://qfoldit.github.io/video/anthropic-nvidia.png"/>
</a> -->

![](https://qfoldit.github.io/img/1/logo/Dell_Nvidia_Factory.png)

<a href="https://blogs.nvidia.com/blog/claude-science-bionemo-agent-toolkit/">
 <img src="https://qfoldit.github.io/video/anthropic-nvidia.png"/>
</a>

*qFoldIT — Universal Builder & Gamifier of Scientific*  
*MPNC synced with UEFN-TOOLBELT*  
*© qFoldIT Core Team, 2026*

<!--

This layered design is what lets a single scientific result -- a folded protein, a converged quantum simulation, a cleared drug-safety screen -- flow all the way from raw computation to a shared, walkable, competitive experience, on whichever engine a community wants to build in.

---

## What's Shipping Today

### 30 MCP tools, spanning the full scientific pipeline

qFoldIT's `Protein-Design-MCP` server puts real computational biology, chemistry, and physics directly in the hands of an AI agent:

- **Generative protein design**: binder design, fold generation, sequence design and optimization, backbone generation, structure and complex prediction, interface analysis, energy minimization, stability scoring, hotspot suggestion -- built on RFdiffusion, ProteinMPNN, ESMFold, and AlphaFold2.
- **Physics-grade refinement**: PyRosetta scoring, relaxation, interface scoring, and design, plus Boltz-2 structure and affinity prediction.
- **Bioactivity and drug screening**: ZairaChem-powered QSAR training and bioactivity prediction, plus a multi-endpoint ADMET profiler covering solubility, toxicity, and the H3D Centre's malaria/tuberculosis screening cascades.
- **Quantum-computing-assisted folding**: a CVaR-optimized Variational Quantum Eigensolver (via QuPepFold) for peptide ground-state energies, and a quantum-walk-inspired Metropolis simulation (inspired by the QFold algorithm) that produces full 3D backbone trajectories -- runnable with zero extra dependencies.
- **Spatial digital twins**: direct export of any structure to OpenUSD, ready for NVIDIA Omniverse, NanoVer VR, Unreal, Unity, UNIGINE, or UEFN.
- **Gamification tools**: `generate_game_design` turns any scientific result into a deterministic set of levels, par scores, and achievements; `generate_multiplayer_challenge` turns one into a round-based competitive structure with a real-metric objective and team roles -- ready to drop into a live arena.
- **Digital twins of real facilities**: `generate_facility_twin` builds walkable, instrumented digital twins of a biomining reactor, a MEOR oil-recovery reservoir, a pipeline corrosion-monitoring rig, a quantum lab station, or an ADMET screening lab -- with every gauge and indicator light driven by the actual computed output of the corresponding science tool.
- **UWI translation**: `uwi_spawn_object` and `uwi_apply_graph` translate a scene description into the exact tool calls needed on Unity, Unreal, UNIGINE, or any of the three UEFN backends.

### 23 Claude Skills, covering the full breadth of scientific gamification

The `claude-skills` plugin packages qFoldIT's domain expertise as modular, reusable Agent Skills:

- **Scientific simulation**: quantum molecular folding, NVIDIA BioNeMo-powered structure prediction, a validated VQE simulator, bio-mining and ore-prospecting kinetics, microbial enhanced oil recovery, pipeline corrosion modeling, plant growth and L-system procedural botany, and plastic pyrolysis characterization.
- **VR science**: a NanoVer bridge for collaborative, interactive molecular dynamics in virtual reality.
- **Digital twin and engine skills**: a shared UAG pipeline feeding dedicated adapters for Unreal Engine, Unity, UNIGINE, OpenUSD/NVIDIA Omniverse, Apple RealityKit/visionOS, Three.js/WebXR, and -- the flagship multiplayer connector -- **UEFN/Fortnite**, with a facility-twin builder purpose-built for turning labs and industrial sites into playable spaces.
- **Molecular Tetris**: a genuinely playable, browser-based science game already shipping today.

### Three real, independently-integrated UEFN backends for Fortnite

qFoldIT connects to Fortnite through three distinct, community-built MCP bridges, each opening different capabilities:

- **KirChuvakov/uefn-mcp-server** (MIT) -- a lightweight 28-tool bridge for fast, permissively-licensed scene control.
- **undergroundrap/UEFN-TOOLBELT** (AGPL-3.0) -- 358 tools across 55 categories, complete with its own native MCP bridge, a scan of the full 4,698-device Fortnite Creative palette, and the ecosystem's most powerful capability: generating and deploying real Verse gameplay code directly from a placed scene.
- **quangdang46/uefn-verse-mcp** (AGPL-3.0, building on both of the above) -- an MCP-first architecture with a broad registered-action surface.

Fortnite's own official **Industrial Galleries** and **Industrial Prefabs** content categories -- Factory, Power Plant, The Rig, Junk Junction, Steel Bridge, and more -- give qFoldIT's facility twins real, ready-to-use architectural building blocks, and Verse's own `creative_prop`/`creative_device` classes give every generated instrument a real, confirmed mechanism for coming alive in a live session.

### A canonical, shared schema

`scientific-world-schema` is qFoldIT's standalone specification repository -- the single source of truth for SOS, SKG, SEM, UAG, and UWI, so every domain-specific MCP and every engine skill in the ecosystem speaks the same language.

---

## The Vision Ahead

qFoldIT's roadmap is built directly on top of what's already working:

- **A fully realized UWI**, extending today's translation layer into deep, native integrations across every major engine and lab-hardware platform -- Blender, LabVIEW, ROS2, NI DAQ, and physical sensor networks -- so any scientific object can be spawned, measured, and streamed live, anywhere.
- **Persistent, community-driven seasons**: since every qFoldIT game-design document carries a deterministic seed tied to its source result, a growing Scientific Knowledge Graph of community-contributed discoveries can unlock new zones, challenges, and content over time -- turning ongoing scientific work into an ongoing, shared world.
- **Boss fights as real optimization problems**: live quantum simulations and folding trajectories driving actual in-game encounters, where beating the boss means genuinely converging the computation.
- **AI Scientist NPCs**: agents that hand out quest chains mirroring the real scientific method -- hypothesis, experiment, measurement, knowledge -- turning good research practice into core gameplay.
- **Secondary-structure-driven procedural architecture**: real protein secondary-structure classifications (alpha helices, beta sheets, turns) generating level geometry directly, so a folded protein's own shape becomes a piece of playable space.
- **A complete, end-to-end multiplayer proof point**: taking a live scientific result all the way from computation to a published, multiplayer-tested Fortnite experience -- the natural next milestone for a platform built on the idea that science is better, and reaches further, when it's shared.

qFoldIT's layered architecture -- SOS, SKG, SEM, UAG, UWI, and MCP, now joined by a direct UEFN-TOOLBELT integration -- means every one of these next steps builds on infrastructure that already exists and already works. The foundation is real; the destination is a genuinely multiplayer, genuinely scientific, genuinely playable universe.

---

## Already Inside UEFN

qFoldIT's presence in UEFN isn't only architectural -- the organization holds a live **UEFN Team account**, "qFoldIT," tagged with its own mission statement, "Scientific Gamification," ready to develop and publish island projects, share them via Unreal Revision Control, and grow its contributor roster (up to 30 team members) as the ecosystem's Fortnite work moves from integration to publication.

<!-- ## Explore the Ecosystem

- **[qfoldit/Protein-Design-MCP](https://github.com/qfoldit)** -- the MCP server: 30 tools spanning generative design, physics-grade scoring, quantum folding, gamification, digital twins, and engine control.
- **[qfoldit/skills](https://github.com/qfoldit)** -- 23 Claude Skills covering scientific simulation, VR science, and digital-twin engine adapters for every major platform.
- **[qfoldit/scientific-world-schema](https://github.com/qfoldit)** -- the canonical SOS/SKG/SEM/UAG/UWI specification tying the whole ecosystem together. -->

<!--
# Components

| Component | Purpose | Status |
| :--- | :--- | :--- |
| **Scientific Object Schema (SOS)** | Canonical model of scientific objects | Data Specification |
| **Scientific Knowledge Graph (SKG)** | Relations between objects, experiments, and knowledge | Semantic Graph |
| **Scientific Execution Model (SEM)** | Protocols, workflows, constraints, and experiment telemetry | Executable Model |
| **Universal Assembly Graph (UAG)** | Graph for assembling digital scenes and worlds (existing format) | Runtime DSL |
| **Universal World Interface (UWI)** | Unified abstract API for interaction with game engines, simulators, and labs | Target Specification |
| **Model Context Protocol (MCP)** | Protocol for AI interaction with tools | Existing Anthropic Standard |

---

# Runtime Mapping

| Runtime | SOS | SKG | SEM | UAG | UWI | MCP |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Unity** | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| **Unreal Engine** | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| **UNIGINE** | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| **NVIDIA Omniverse** | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| **Blender** | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| **Labster** | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| **Fortnite (UEFN)** | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| **LabVIEW** | ✔ | ✔ | ✔ | — | ✔ | ✔ |
| **ROS2** | ✔ | ✔ | ✔ | — | ✔ | ✔ |
| **NI DAQ** | ✔ | ✔ | ✔ | — | ✔ | ✔ |
| **Physical Sensors** | ✔ | ✔ | ✔ | — | ✔ | ✔ |

``` text
                                   Humans
                                      │
                           Citizen Scientists
                                      │
                               AI Scientists
                                      │
                     qFoldIT Reality Interface
          Scientific Object Schema (SOS) • Universal World Interface (UWI)
          Universal Assembly Graph (UAG) • Model Context Protocol (MCP)
                                      │
 ─────────────────────────────────────────────────────────────────────────────
 Virtual Worlds      Digital Twins      Physical Laboratories
 Unreal Engine       NVIDIA Omniverse   LabVIEW
 Unity               OpenUSD            NI DAQ
 UNIGINE             CAD                Robotics
 Blender             Simulation         Sensors
 Labster             Synthetic Data     Scientific Instruments
 ─────────────────────────────────────────────────────────────────────────────
                         Knowledge • Continuous Learning
```

```
Overall Technology Readiness Level (TRL): 6/9

Current State:

AI Agent Layer             █████████░ 90%

Scientific Skills           ████████░░ 85%

MCP Infrastructure          ███████░░░ 70%

Scientific Models            ████████░░ 78%

Quantum Computing            ██████░░░░ 60%

Digital Twin                ███████░░░ 75%

Spatial Computing            ██████░░░░ 65%

Game Engine Integration      ███████░░░ 70%

Citizen Science Layer        █████░░░░░ 50%


TOTAL PLATFORM              ███████░░░ 73%  
```

---


Anthropic - [qFoldIT is "Claude Science" Ready](https://claude.com/product/claude-science)

Ericsson - [Immersive Future of Gaming](https://www.ericsson.com/en/about-us/new-world-of-possibilities/imagine-possible-perspectives/future-of-gaming)

David Baker - [Protein Folding Code: Won a Nobel Prize](https://youtu.be/cx7l9ZGFZkw)

Kelly Chibale - [Beyond the Code: AI 2050](https://youtu.be/7KmUzG1hltI)

Dr. Neil Voss - [CryoEM & Protein Geometry](https://youtube.com/playlist?list=PL5LJPD9b2pRY3HCA-zq60vjCmwoWU6Zxv&si=O8er-pfzGQgxyU_m)

Silvia Holler - [Future of folding: Cotraslational folding simulation](https://youtu.be/C_QIO--OUf4)

Alexei Lapkin - [iDMT: Innovation Centre in Digital Molecular Technologies](https://youtu.be/Dd7ZwpgT4nw)

Scientific Publications - [Playing Dice with the Universe: Programming Quantum Computers to Play Traditional Games](https://arxiv.org/abs/2604.23819)

Realtime Statistics - [CAMEO: automated benchmarking of structure prediction servers, complementing CASP](https://robetta.bakerlab.org/)
-->

<!--
![](https://qfoldit.github.io/video/CGS_LOGO.png)
![](https://qfoldit.github.io/video/CGS_CENTER_WHITE.png)
![](https://qfoldit.github.io/video/GSRC.png)
![](https://qfoldit.github.io/video/RF3_hero_image.png)
![](https://qfoldit.github.io/video/Nvidia_evo2.jpg)
![](https://qfoldit.github.io/assets/evo2.jpg)
![](https://qfoldit.github.io/video/NVidia_ISING.png)
![](https://qfoldit.github.io/video/ISS_CAL_MR.png)
![](https://qfoldit.github.io/video/Artemis_VR.png)
![](https://qfoldit.github.io/video/space_qfold.png)
![](https://qfoldit.github.io/video/qfolditdna.png)
![](https://qfoldit.github.io/video/Drew_Berry.png)
![](https://qfoldit.github.io/img/posters/iDMT_Molecular.png)
![](https://qfoldit.github.io/img/labster-virtual-labs.png)
![](https://qfoldit.github.io/img/Westminster_Labster.png)
![](https://joyenergy.github.io/img/Professor_Chibale.png)
![](https://qfoldit.github.io/img/1/logo/syntech.png)
![](https://qfoldit.github.io/img/1/logo/idmt.png)
![](https://qfoldit.github.io/img/1/logo/idmt_partners.png)
-->

*An open-science partner of the [Ersilia Open Source Initiative](https://github.com/ersilia-os/) and [Visualizing biological data](https://vizbi.org/)*


[![License](https://img.shields.io/badge/License-Proprietary%20with%20Open%20Components-blue)](#)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)

[![Kubernetes](https://img.shields.io/badge/Kubernetes-1.28%2B-blue)](https://kubernetes.io/)

[![Ersilia](https://img.shields.io/badge/Ersilia-Integrated-purple)](https://ersilia.io)
<!--
---

# qFoldIT

## From Molecular Folding to Universal Digital Twin Assembly


qFoldIT was originally created as a **gamified quantum molecular drug design platform** for global scientific collaboration.

The fundamental idea:

> Complex systems can be represented as connected structures of nodes, relationships, constraints and instructions.


This principle evolved into:

# Universal Assembly Graph (UAG)


A universal representation layer for AI agents and digital twins.

qFoldIT can describe:

- molecular structures;
- biological systems;
- robotics;
- industrial equipment;
- architecture;
- game worlds;
- simulation environments;
- spatial computing experiences.


---

# Universal Assembly Graph Architecture


```
             qFoldIT Core

      Universal Assembly Graph

                |

      Digital Twin Compiler

                |
```

```
================================================

Science        Games        Simulation

Molecules      Unreal       UNIGINE

Biology        Unity        UNIGINE 2 Sim

Industry       Spatial      Web

Omniverse      Apple        Three.js

OpenUSD        visionOS     React Three Fiber

================================================

```


---

# AI Agent Infrastructure


qFoldIT follows a modern agent architecture:


```

AI Agent
   |
Agent Skills
   |
Model Context Protocol (MCP)
   |
qFoldIT Core
   |
Engine Adapters

```


## MCP Layer

Provides:

- external tool connectivity;
- engine integration;
- automation;
- project generation;
- simulation control.


## Agent Skills Layer

Provides:

- domain expertise;
- workflows;
- reusable design patterns;
- specialized AI capabilities.


---

# Compatible Platforms


## Game Engines


## Unreal Engine

Supports:

- AAA game worlds;
- cinematic environments;
- gameplay systems;
- Blueprint workflows.


## Unity Engine

Supports:

- interactive applications;
- XR experiences;
- mobile deployment;
- simulations.


---

# Digital Twin Platforms


## NVIDIA Omniverse + OpenUSD

Supports:

- industrial digital twins;
- USD pipelines;
- AI simulation environments;
- collaborative 3D workflows.


---

# Simulation Platforms


## UNIGINE 2

Supports:

- real-time visualization;
- professional simulations;
- high-fidelity environments.


## UNIGINE 2 Sim

Supports:

- physics simulation;
- synthetic environments;
- AI training scenarios.


---

# Apple Spatial Computing


## Xcode

Supports:

- native Apple applications;
- project generation;
- build workflows.


## Swift / SwiftUI

Supports:

- application interfaces;
- spatial UI.


## RealityKit

Supports:

- AR;
- spatial computing;
- visionOS applications.


## visionOS

Supports:

- Apple spatial experiences.


## USDZ

Supports:

- Apple 3D asset pipeline.


## Metal

Supports:

- GPU acceleration;
- high-performance computation.


---

# Web 3D Platform


## Three.js

Supports:

- browser digital twins;
- WebGL/WebGPU visualization;
- online experiences.


## React Three Fiber

Supports:

- React-based 3D editors;
- component-driven worlds;
- Game Designer workflows.


## WebXR

Supports:

- browser XR experiences.


---

# Repository Architecture


```

qFoldIT/

├── core/

│   └── Universal Assembly Graph Engine

├── standards/

│   ├── MCP

│   ├── Agent Skills

│   └── OpenUSD

├── engines/

│   ├── Unreal

│   ├── Unity

│   ├── NVIDIA Omniverse

│   ├── UNIGINE

│   ├── Apple

│   └── Web

├── mcp-servers/

├── skills/

└── examples/

```

---

# Mission


qFoldIT connects:

**Science + AI Agents + Digital Twins + Game Design + Simulation**

into one universal assembly framework.


Our mission:

> Build an open ecosystem where humans and AI agents can design, simulate and deploy complex digital systems across scientific, industrial, gaming and spatial computing platforms.
-->
---

# Contact

GitHub Organization:

qFoldIT@gmail.com <br>
https://github.com/qfoldit
