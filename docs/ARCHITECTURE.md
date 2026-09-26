# NEXA Infinity Architecture

## Architectural rule

NEXA is case- and evidence-centric. Modules exchange normalized events and references rather than silently modifying source evidence.

## Core architectural principles

### 1. Evidence is not an AI opinion

Evidence remains distinct from interpretation.

- Original evidence is immutable from analytical workflows.
- Derived artifacts retain provenance, timestamps, hashes, and references to their source.
- AI output is analysis, hypothesis, correlation, or recommendation; it is never evidence by itself.
- An AI assessment must not retrospectively alter the evidence that produced it.

### 2. AI assists. Human verifies. Human decides.

NEXA implements a **Human-in-the-Loop (HITL)** model. AI may detect patterns, correlate events, challenge an analyst's hypothesis, identify evidentiary gaps, and recommend next steps, but the human analyst remains the decision authority.

A central NEXA capability is evidentiary challenge:

> **"You are missing this evidence to support that conclusion."**

The AI should not merely agree with the analyst. It should expose missing support, alternative explanations, contradictions, uncertainty, and recommended evidence to acquire or review.

## Bidirectional human–AI reasoning

```text
HUMAN ─────────────────────► AI
       hypothesis / question
       investigative context
       analyst reasoning

AI ────────────────────────► HUMAN
       correlates
       challenges
       identifies missing evidence
       exposes uncertainty
       recommends next investigative step

HUMAN ─────────────────────► SYSTEM
       verifies
       decides
       authorizes
```

The final transition from analysis to validated finding or consequential action belongs to the human.

## Human Gate

AI-generated findings must preserve their review state explicitly.

```text
AI_GENERATED
      ↓
PENDING_HUMAN_REVIEW
      ↓
 ┌────┼───────────────┐
 ↓    ↓               ↓
APPROVED           REJECTED
 ↓                    ↓
VALIDATED          DISMISSED
      \              /
       \            /
        INCONCLUSIVE
```

A reviewer may determine that available evidence is insufficient. NEXA must preserve **INCONCLUSIVE** as a legitimate analytical outcome rather than forcing confirmation or rejection.

A validated finding should retain at minimum:

- supporting evidence references;
- AI assessment and stated uncertainty;
- human reviewer identity;
- human decision;
- review timestamp;
- analyst rationale where required;
- complete audit trail.

AI/human disagreement is preserved rather than overwritten.

## Evidence-to-decision chain

```text
EVIDENCE
   ↓
OBSERVATION
   ↓
AI ASSESSMENT
   ↓
HUMAN REVIEW
   ↓
VALIDATED FINDING / REJECTED / INCONCLUSIVE
   ↓
AUDIT LOG
```

This separation allows NEXA to distinguish a fact observed in evidence from a machine inference and from a human analytical conclusion.

## Human authorization for defensive actions

For consequential defensive actions, recommendation and execution are separate operations.

```text
Event / Incident
      ↓
AI analysis
      ↓
Evidence + rationale + uncertainty
      ↓
Recommended action
      ↓
HUMAN AUTHORIZATION GATE
      ↓
Policy Engine
      ↓
Defender
      ↓
Audit + Evidence
```

The architecture must support policies that require explicit human authorization before high-impact actions. The audit record must preserve what the AI recommended, what evidence was available, what the human decided, and what the system ultimately executed.

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
AI Router / Analytical Challenge
        ↓
Human Review
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
- Human review is mandatory where policy requires validation or authorization.
- Defensive actions pass through policy and audit controls.
- AI recommendations and human decisions remain separately attributable.
- Lab/training data is separated from real-case data.
