# Witness Receipt Protocol (WRP)
## Canonical Protocol Specification

---

## Purpose

The Witness Receipt Protocol (WRP) defines a deterministic, offline-verifiable
receipt format for sealing decisions, evaluations, or attestations.

WRP is a protocol primitive, not an AI system.

---

## Core Properties

WRP guarantees:

- Deterministic evaluation
- Canonical serialization
- Stable hashing
- Offline verification
- Forward-compatible evolution

---

## Determinism

Given identical input:

- Canonical bytes MUST be identical
- Hash MUST be identical
- Verification result MUST be identical

Non-determinism is forbidden.

---

## Canonicalization Rules

All receipts MUST:

- Use UTF-8 encoding
- Use normalized Unicode (NFC)
- Use sorted object keys
- Contain no insignificant whitespace
- Contain no floats unless explicitly defined
- Declare `schema_version`

Canonicalization rules are immutable per schema version.

---

## Receipt Immutability

Once issued, a receipt:

- MUST NOT be modified
- MUST NOT be reinterpreted
- MUST remain verifiable forever

Receipts are self-contained and do not depend on external state.

---

## Verification

Verification:

- Is offline
- Is stateless
- Requires only the receipt and protocol rules
- Does not depend on the issuing system

---

## Evolution Rules

WRP evolves ONLY via:

- New schema versions
- New receipt types
- New endpoints

Existing receipts and schemas remain valid indefinitely.

Silent changes are forbidden.

---

## Authority Boundary

WRP does not decide truth.

WRP proves that a specific decision occurred under declared rules.

Meaning is assigned by the consuming system, not the protocol.
