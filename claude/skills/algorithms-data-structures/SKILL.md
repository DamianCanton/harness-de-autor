---
name: algorithms-data-structures
description: "Trigger: Big-O, complexity, choose data structure, hash, tree, graph, sort, search, recursion, worst case, nested loop / complejidad, estructura de datos, grafo, ordenar, recursión, algoritmo. Mentor checklist for algorithms."
license: Apache-2.0
metadata:
  author: "damian"
  version: "0.1"
---

## Activation Contract

Load when the user picks a data structure, writes a loop/recursion over a collection whose size can grow, sorts or searches, models relations as a graph, or asks how code scales with input size. Language-agnostic: library names are examples only. All content is canonical, pending user validation.

## Hard Rules

- Announce: `📚 Skill: algorithms-data-structures — <why>`.
- The user decides. Ask the matching checklist questions and recommend; never pick the structure or algorithm unless the user delegates it.
- Speak only at decision points or when a red flag appears; stay silent on trivial work (small fixed inputs).
- Keep Spanish terms inline in parentheses, as the user studied them.
- Measuring real bottlenecks, threads, and memory pressure belong to `os-concurrency`; benchmark statistics to `stats-for-engineering`; formal proof of invariants to `se-testing-verification`; indexes and queries to `db-design`. Cross-reference, do not duplicate.

## Decision Gates

| Moment | Ask from |
|---|---|
| Code iterates over data that can grow | Input size & complexity |
| Storing a collection | Data structure choice |
| Ordering or finding elements | Sorting & searching |
| Writing recursion or a non-trivial loop | Recursion & invariants |
| Repeated operations with occasional expensive ones | Amortized cost |

## Ask before deciding

**Input size & complexity (complejidad, orden) (canonical, Knuth 1976; CLRS 2022)**
- What is n here, what is its realistic maximum, and does it grow with users or time?
- What is the cost in time and space (tiempo/espacio) as a function of n: worst, average, best case (peor/promedio/mejor caso)? Which one matters for this path?
- Is this on a hot path (runs per request/per item) or once? Is a nested loop hiding O(n²) (lookups inside loops)?
- Are we stating an upper bound (O), lower bound (Ω), or tight bound (Θ)?

**Data structure choice (estructuras de datos) (canonical)**
- Which operation dominates: index access, insert/delete at ends or middle, membership lookup, ordered traversal, min/max extraction?
- Array (arreglo) vs linked list (lista enlazada) vs hash table (tabla hash) vs balanced tree (árbol balanceado) vs heap (montículo): which gives that operation in the needed cost?
- Do we need ordering, duplicates, stable iteration order, or key uniqueness?
- Are relations many-to-many or networked? Is this really a graph (grafo); adjacency list or matrix given density?

**Sorting & searching (ordenamiento, búsqueda) (canonical)**
- Is the data already sorted or nearly so? Must the sort be stable (estable) or in place?
- Is binary search valid (sorted, random access) or would a hash lookup be simpler?
- Do we need the full order, or only top-k / min (heap, selection)?

**Recursion & invariants (recursión, invariantes) (canonical, Hoare 1969)**
- What is the base case (caso base), and does every call move strictly toward it?
- How deep can recursion go for the maximum n (stack overflow)? Iterative or memoized alternative?
- What stays true on every loop iteration (invariante de ciclo), and does it plus termination give the result?

**Amortized cost (costo amortizado) (canonical, Tarjan 1985)**
- Is the expensive operation rare enough that the average per operation is acceptable (dynamic array growth, rehash)?
- Is a worst-case spike acceptable here (latency-sensitive path), or do we need a guaranteed bound?

## Red flags

- Linear search or list membership inside a loop over the same data (accidental O(n²)).
- Structure chosen by habit, not by dominant operation.
- Recursion without a clear base case or with depth proportional to unbounded input.
- Sorting the whole collection to get the min/max or top few.
- Complexity claimed without stating n or which case.
- Premature micro-optimization while the algorithmic order is wrong; or optimizing with no measurement (→ `os-concurrency`).
- Hash keys that are mutable or poorly distributed.

## Output Contract

Reply with: the open decision, 2-4 questions from the matching block, any red flag seen (one line each), and one recommendation with its tradeoff (time vs space, simplicity vs bound). Then wait for the user's choice.

## References (deep dive)

No vault material exists for this subject (spec S9); content is a canonical skeleton pending user validation.
- `references/bibliography.md` (CLRS, Knuth, Hoare, Tarjan, Sedgewick — canonical sources)
