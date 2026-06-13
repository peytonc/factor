# Dependency Graph & Reading Order

This document gives an AI agent (or reviewer) an explicit map of the logical
structure so files can be read or validated in a valid order. Edges are taken from
explicit `Theorem N` citations in the source text, plus the foundational dependency
of state-manipulating results on the state representation (T01).

## Clusters

- **Foundations (T01–T04):** the linear state model, existence of trivial /
  non-trivial paths, and monotonic descent.
- **Modular Theory (T05–T10):** projecting the infinite tree into finite rings and
  decomposing orbits via CRT / Hensel lifting.
- **Differential & Swap Theory (T11–T17):** how sibling/branch swaps perturb the
  state, and the exact congruences and lattice formulas they obey. The single-swap
  differential (T15) feeds the multi-swap differential (T17).

## Graph

```mermaid
graph TD
    subgraph Foundations
    T01["T01 · State Transition"]
    T02["T02 · Trivial Path"]
    T03["T03 · Non-Trivial Path"]
    T04["T04 · Monotonic Growth"]
    end
    subgraph Modular_Theory
    T05["T05 · Modular Transition"]
    T06["T06 · Orbit Graph"]
    T07["T07 · Prime Axis Alignment"]
    T08["T08 · Prime Cardinality"]
    T09["T09 · Square-Free Decomp."]
    T10["T10 · Generalized Decomp."]
    end
    subgraph Differential_and_Swap_Theory
    T11["T11 · Sibling Divergence"]
    T12["T12 · Path B/C Congruence"]
    T13["T13 · Path A/B Congruence"]
    T14["T14 · Multi-Swap Congruence"]
    T15["T15 · Suffix Propagation"]
    T16["T16 · Parent Determinism"]
    T17["T17 · Multi-Swap Differential"]
    end

    T01 --> T02
    T01 --> T03
    T01 --> T04
    T01 --> T05
    T05 --> T06
    T06 --> T07
    T06 --> T08
    T07 --> T08
    T06 --> T09
    T08 --> T09
    T09 --> T10
    T01 --> T11
    T11 --> T12
    T11 --> T13
    T12 --> T14
    T13 --> T14
    T11 --> T15
    T01 --> T16
    T11 --> T17
    T15 --> T17
```

## Edge List (machine-readable)

```yaml
edges:
  - from: T01
    to: T02
  - from: T01
    to: T03
  - from: T01
    to: T04
  - from: T01
    to: T05
  - from: T05
    to: T06
  - from: T06
    to: T07
  - from: T06
    to: T08
  - from: T07
    to: T08
  - from: T06
    to: T09
  - from: T08
    to: T09
  - from: T09
    to: T10
  - from: T01
    to: T11
  - from: T11
    to: T12
  - from: T11
    to: T13
  - from: T12
    to: T14
  - from: T13
    to: T14
  - from: T11
    to: T15
  - from: T01
    to: T16
  - from: T11
    to: T17
  - from: T15
    to: T17
```
