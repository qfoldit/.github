# qFoldIT Repository Map — Coverage Overlay

The main architecture map covers the organization-wide public and private repository inventory available to the audit connector. Two intentionally non-product/internal surfaces are treated separately here so the graph remains readable.

| Repository | Decision | Canonical role | Relationship |
|---|---|---|---|
| `qfoldit/uefn-mcp` | **CONSOLIDATE** | Private/legacy UEFN MCP implementation lineage | migrate unique behavior into `UEFN-QFOLDIT` runtime UEFN-MCP boundary; do not retain as a second MCP authority |
| `qfoldit/.github-private` | **KEEP** | Private governance/operational artifacts | remains isolated from public governance; referenced by private deployment and operational workflows |

## Coverage rule

The organization inventory is authoritative for repository existence. The public architecture map classifies each repository by lifecycle and dependency role. Private repositories that should never become public dependencies are represented through this overlay rather than duplicated as public implementation references.

## Decision

`uefn-mcp` is not a competing runtime architecture. It is migration lineage for the canonical UEFN MCP boundary already defined by `UEFN-QFOLDIT`.
