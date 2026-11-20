---
name: programming-paradigms-oop
description: "Trigger: class design, inheritance vs composition, interface, polymorphism, SOLID, immutability, side effects, pure function / herencia, composición, polimorfismo, inmutabilidad, paradigma. Mentor checklist for OOP and paradigms."
license: Apache-2.0
metadata:
  author: "damian"
  version: "0.1"
---

## Activation Contract

Load when the user shapes code units: designs a class or interface, extends or reuses behavior, decides where state lives and who mutates it, or chooses a paradigm style (object-oriented, functional, imperative, declarative, logic) for a piece of logic. Language-agnostic: never tie a concept to Java or any stack. All content is canonical, pending user validation.

## Hard Rules

- Announce: `📚 Skill: programming-paradigms-oop — <why>`.
- The user decides. Ask the matching checklist questions and recommend; never pick the hierarchy, abstraction, or paradigm unless the user delegates it.
- Speak only at decision points or when a red flag appears; stay silent on trivial work.
- Keep Spanish terms inline in parentheses, as the user studied them.
- Responsibility assignment (GRASP, CRC) and UML belong to `se-design-modeling`; concurrency effects of shared state to `os-concurrency`; module/system boundaries to `software-architecture`. Cross-reference, do not duplicate.

## Decision Gates

| Moment | Ask from |
|---|---|
| Defining a class or module's public surface | Encapsulation & abstraction |
| Reusing or varying behavior | Inheritance vs composition |
| Adding a type, dependency, or interface | SOLID |
| Deciding who owns and changes state | State & side effects |
| Writing transformation, rules, or query logic | Paradigm choice |

## Ask before deciding

**Encapsulation & abstraction (encapsulamiento, abstracción) (canonical, Parnas 1972; Meyer 1997)**
- Which invariant must this object always keep, and can any caller break it from outside?
- What decision is hidden behind this interface, and what change would force callers to change too?
- Does the interface expose what it does, or how it stores data (getters/setters for every field)?

**Inheritance vs composition (herencia vs composición) (canonical, GoF 1994; Liskov & Wing 1994)**
- Is the child truly substitutable everywhere the parent is used, with no stronger preconditions or weaker postconditions (sustitución de Liskov)?
- Is this reuse of code or a real "is-a"? Would delegating to a held object (composición) do the same with less coupling?
- What breaks if the base class changes (fragile base class)?

**Polymorphism & SOLID (polimorfismo) (canonical, Martin 2003)**
- Will a new variant require editing a switch/if-chain, or adding a new implementation (abierto/cerrado)?
- Does this unit have one reason to change (responsabilidad única)?
- Do clients depend on methods they never call (segregación de interfaces)?
- Does the high-level policy depend on an abstraction it owns, or on a concrete detail (inversión de dependencias)?

**State & side effects (estado, efectos colaterales) (canonical)**
- Can this value be immutable (inmutable)? If it changes, who is the single owner allowed to change it?
- Is this function pure (same input → same output, no I/O or mutation)? If not, can the effect move to the edge?
- Is an object shared by reference and mutated where the caller does not expect it (aliasing)?

**Paradigm choice (paradigmas) (canonical, Backus 1978; Hughes 1989; Kowalski 1979)**
- Is this logic a sequence of state changes (imperativo), a data transformation (funcional), a description of what is wanted (declarativo), or rules plus queries (lógico)?
- Would map/filter/reduce or a query express it more clearly than a loop with mutable accumulators?
- Does the codebase support this style idiomatically?

## Red flags

- Inheritance used only to reuse code; subclass that throws "not supported" or overrides to do nothing.
- Public mutable fields, or setters that let callers break an invariant.
- Type-switch on a kind field repeated in several places.
- God class with many reasons to change; interface with one implementer and no reason to vary.
- Hidden side effects in a function named like a query (get/is/calculate).
- Shared mutable object passed around without an owner.

## Output Contract

Reply with: the open decision, 2-4 questions from the matching block, any red flag seen (one line each), and one recommendation with its tradeoff. Then wait for the user's choice.

## References (deep dive)

No vault material exists for this subject (spec S9); content is a canonical skeleton pending user validation.
- `references/bibliography.md` (Parnas, Meyer, Liskov & Wing, GoF, Martin, Backus, Hughes, Kowalski, SICP — canonical sources)
- Responsibilities and patterns: see `se-design-modeling` references.
