# **Gamified Quantum Molecular Drug Design for Global Science**

```python
"""
Minimal, tested proof-of-concept for the Object -> Operation -> Result
pattern from Scientific World Schema, grounded in THREE real, already-
working qFoldIT functions (not hypothetical "planet"/"robot" objects).

Goal: find out empirically whether the abstract pattern actually holds
as a useful data contract across genuinely different domains (bio-
oxidation kinetics, quantum protein folding, scene export) -- not just
assert that it does.
"""

from dataclasses import dataclass, field, asdict
from typing import Any
import time


@dataclass
class ScientificObject:
    """The 'Object' node -- what the operation acts on or produces."""
    object_type: str          # e.g. "ore_sample", "peptide_sequence", "scene_plan"
    object_id: str
    state: dict[str, Any] = field(default_factory=dict)


@dataclass
class Operation:
    """The 'Operation' node -- what was actually run, and with what."""
    operation_name: str       # must match a real, callable function name
    mcp_source: str           # which real skill/MCP this came from
    inputs: dict[str, Any]
    started_at: float = field(default_factory=time.time)


@dataclass
class Result:
    """The 'Measurement/Knowledge' node -- what came back."""
    operation: Operation
    output_object: ScientificObject
    raw_output: dict[str, Any]
    completed_at: float = field(default_factory=time.time)

    def to_dict(self) -> dict:
        return {
            "operation": {**asdict(self.operation)},
            "output_object": asdict(self.output_object),
            "raw_output": self.raw_output,
            "duration_s": round(self.completed_at - self.operation.started_at, 6),
        }


def wrap_bioox(temperature_c: float, ph: float) -> Result:
    """Wraps qfoldit-mining's real effective_rate_constant() as a Scientific World Schema Result."""
    import sys
    sys.path.insert(0, "/mnt/skills/user/qfoldit-mining/scripts")
    import bioox_kinetics as bx

    op = Operation(
        operation_name="effective_rate_constant",
        mcp_source="qfoldit-mining",
        inputs={"temperature_c": temperature_c, "ph": ph},
    )
    k = bx.effective_rate_constant(temperature_c, ph)
    out_obj = ScientificObject(
        object_type="bioleaching_reaction_rate",
        object_id=f"bioox_{temperature_c}C_pH{ph}",
        state={"k_eff_per_day": k},
    )
    return Result(operation=op, output_object=out_obj, raw_output={"k_eff": k})


def wrap_qfold(sequence: str) -> Result:
    """Wraps qfoldit-qfold's real brute_force_best_fold() as a Scientific World Schema Result."""
    import sys
    sys.path.insert(0, "/mnt/skills/user/qfoldit-qfold/scripts")
    import hp_lattice_folder as hp

    op = Operation(
        operation_name="brute_force_best_fold",
        mcp_source="qfoldit-qfold",
        inputs={"sequence": sequence},
    )
    fold = hp.brute_force_best_fold(sequence)
    out_obj = ScientificObject(
        object_type="hp_lattice_fold",
        object_id=f"fold_{sequence}",
        state={"contacts": fold["best_fold"]["contacts"], "bitstring": fold["best_fold"]["bitstring"]},
    )
    return Result(operation=op, output_object=out_obj, raw_output=fold)


def wrap_scene_export(result: Result) -> Result:
    """
    Takes a PREVIOUS Result's output_object and feeds it into
    qfoldit-scene-export -- this is the actual cross-MCP interoperability
    test: does one domain's Object cleanly become another domain's input?
    """
    import sys
    sys.path.insert(0, "/mnt/skills/user/qfoldit-scene-export/scripts")
    from scene_plan import ScenePlan, Node, Material
    from export_usd import export_usd

    # Turn the HP-lattice fold's 2D coordinates into a trivial 3D scene
    coords = result.raw_output["best_fold"]["coordinates"]
    nodes = [
        Node(id=f"res_{i}", primitive="sphere", position=(x * 2.0, y * 2.0, 0.0),
             scale=(0.3, 0.3, 0.3), material=Material(color_rgba=(0.3, 0.5, 0.9, 1.0)))
        for i, (x, y) in enumerate(coords)
    ]
    plan = ScenePlan(name="hp_fold_visualization", nodes=nodes)
    plan.validate()

    op = Operation(
        operation_name="export_usd",
        mcp_source="qfoldit-scene-export",
        inputs={"source_object_id": result.output_object.object_id},
    )
    export_result = export_usd(plan, "/tmp/schema_test_fold.usda")
    out_obj = ScientificObject(
        object_type="usd_scene_file",
        object_id=export_result["path"],
        state={"backend": export_result["backend"], "num_nodes": len(nodes)},
    )
    return Result(operation=op, output_object=out_obj, raw_output=export_result)

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

David Baker - [Protein Folding Code: Won a Nobel Prize](https://youtu.be/cx7l9ZGFZkw)

Kelly Chibale - [Beyond the Code: AI 2050](https://youtu.be/7KmUzG1hltI)

Dr. Neil Voss - [CryoEM & Protein Geometry](https://youtube.com/playlist?list=PL5LJPD9b2pRY3HCA-zq60vjCmwoWU6Zxv&si=O8er-pfzGQgxyU_m)

Silvia Holler - [Future of folding: Cotraslational folding simulation](https://youtu.be/C_QIO--OUf4)

Alexei Lapkin - [iDMT: Innovation Centre in Digital Molecular Technologies](https://youtu.be/Dd7ZwpgT4nw)

Scientific Publications - [Playing Dice with the Universe: Programming Quantum Computers to Play Traditional Games](https://arxiv.org/abs/2604.23819)

Realtime Statistics - [CAMEO: automated benchmarking of structure prediction servers, complementing CASP](https://robetta.bakerlab.org/)


<a href="https://blogs.nvidia.com/blog/claude-science-bionemo-agent-toolkit/">
 <img src="https://qfoldit.github.io/video/anthropic-nvidia.png"/>
</a>

![](https://qfoldit.github.io/img/1/logo/Dell_Nvidia_Factory.png)

<a href="https://www.youtube.com/watch?v=idtMsa_1yNk">
 <img src="https://qfoldit.github.io/video/claude_qfoldit.jpg"/>
</a>

![](https://qfoldit.github.io/video/CGS_LOGO.png)

![](https://qfoldit.github.io/video/CGS_CENTER_WHITE.png)

![](https://qfoldit.github.io/video/GSRC.png)

![](https://qfoldit.github.io/video/RF3_hero_image.png)

<a href="https://www.bakerlab.org/">
 <img src="https://qfoldit.github.io/img/posters/David_Baker_AT_FoldIT_LAB_OFFICE.png"/>
</a>

![](https://qfoldit.github.io/video/Nvidia_evo2.jpg)

![](https://qfoldit.github.io/assets/evo2.jpg)

![](https://qfoldit.github.io/video/NVidia_ISING.png)

![](https://qfoldit.github.io/video/ISS_CAL_MR.png)

![](https://qfoldit.github.io/video/Artemis_VR.png)

![](https://qfoldit.github.io/video/space_qfold.png)

![](https://qfoldit.github.io/video/qfolditdna.png)

![](https://qfoldit.github.io/video/Drew_Berry.png)

![](https://qfoldit.github.io/img/posters/iDMT_Molecular.png)

![](https://qfoldit.github.io/img/Westminster_Labster.png)

![](https://joyenergy.github.io/img/Professor_Chibale.png)

![](https://qfoldit.github.io/img/1/logo/syntech.png)

![](https://qfoldit.github.io/img/1/logo/idmt.png)

![](https://qfoldit.github.io/img/1/logo/idmt_partners.png)


*An open-science partner of the [Ersilia Open Source Initiative](https://github.com/ersilia-os/) and [Visualizing biological data](https://vizbi.org/)*


[![License](https://img.shields.io/badge/License-Proprietary%20with%20Open%20Components-blue)](#)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)

[![Kubernetes](https://img.shields.io/badge/Kubernetes-1.28%2B-blue)](https://kubernetes.io/)

[![Ersilia](https://img.shields.io/badge/Ersilia-Integrated-purple)](https://ersilia.io)


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

# Organization Members


| GitHub | Organization |
|-|-|
| Jianmin Wang | AspirinCode |
| George Kwa | CEPBEP |
| e-CEDI | DIGITALCEDI |
| Kelly Chibale | h3dchibale |
| Mao Jiashun | shunsunsun |
| Silvia Holler | SilviaHoller |
| Dr. Neil Voss | vosslab |


---

# Mission


qFoldIT connects:

**Science + AI Agents + Digital Twins + Game Design + Simulation**

into one universal assembly framework.


Our mission:

> Build an open ecosystem where humans and AI agents can design, simulate and deploy complex digital systems across scientific, industrial, gaming and spatial computing platforms.

---

# Contact

GitHub Organization:

qFoldIT@gmail.com <br>
https://github.com/qfoldit
