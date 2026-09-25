# NEXA Infinity Architecture

## Architectural rule

NEXA is case- and evidence-centric. Modules exchange normalized events and references rather than silently modifying source evidence.

## Initial flow

```text
Source / Acquisition
        ↓
Normalization
        ↓
NEXA Event
        ↓
Correlation
        ↓
Entity / Relationship / Incident
        ↓
Policy
        ↓
Defender Simulator
        ↓
Audit + Evidence + Report
```

## Trust boundaries

- Original evidence is immutable from analytical workflows.
- Derived artifacts retain provenance.
- AI output is analysis, never evidence by itself.
- Defensive actions pass through policy and audit controls.
- Lab/training data is separated from real-case data.
