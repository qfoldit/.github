# qFoldIT Chain Conformance v2

The conformance runner validates the canonical identity chain:

```text
Mission
  -> Submission
  -> Evidence
  -> validation.completed Event
```

It also checks that the runtime adapter declares every capability required by the mission fixture.

This is a synthetic interoperability gate. It does not perform a scientific calculation and does not replace OpenStructure or another authoritative validator.
