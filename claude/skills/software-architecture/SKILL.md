---
name: software-architecture
description: "Trigger: architecture, layered, hexagonal, clean architecture, microservices vs monolith, event-driven, quality attributes, ADR, deployment / arquitectura, capas, módulos, despliegue, acoplamiento. Mentor checklist for architecture."
license: Apache-2.0
metadata:
  author: "damian"
  version: "0.1"
---

## Activation Contract

Load when the user decides a system's structure: module or service boundaries, dependency direction, architectural style, how components communicate, where code is deployed, which quality attribute wins a tradeoff, or how to record that decision. Language-agnostic: frameworks and clouds are examples only. Content is canonical except the views block, pending user validation.

## Hard Rules

- Announce: `📚 Skill: software-architecture — <why>`.
- The user decides. Ask the matching checklist questions and recommend; never pick the style, boundary, or tradeoff unless the user delegates it.
- Speak only at decision points or when a red flag appears; stay silent on trivial work.
- Keep Spanish terms inline in parentheses, as the user studied them.
- Class-level design and GRASP belong to `se-design-modeling`; eliciting NFRs to `se-process-requirements`; quality evaluation and testing to `se-testing-verification`; migrating or refactoring an existing system to `se-evolution-maintenance`; data ownership and schema to `db-design`; network concerns to `networking`; threats to `security`. Cross-reference, do not duplicate.

## Decision Gates

| Moment | Ask from |
|---|---|
| Starting a system or major feature | Drivers & quality attributes |
| Choosing structure or dependency direction | Styles |
| Splitting into services or deployables | Distribution |
| Documenting structure or deployment | Views |
| Any decision costly to reverse | ADR |

## Ask before deciding

**Drivers & quality attributes (atributos de calidad) (canonical, ISO/IEC 25010:2023; Bass et al. 2021)**
- Which two or three quality attributes drive this system (performance, availability, security, maintainability, scalability)? Are they measurable scenarios, not adjectives?
- Which attribute do we sacrifice for which, and who agreed to that tradeoff?
- What is the expected change: which parts will vary most in the next year?

**Styles (estilos arquitectónicos) (canonical, Garlan & Shaw 1993; Cockburn 2005; Martin 2017)**
- Do dependencies point inward, toward the domain, with infrastructure as replaceable adapters (puertos y adaptadores)?
- Can the core use cases run and be tested without the database, UI, or framework?
- Does the top-level structure reveal the domain (screaming) or the framework (controllers/, services/)?
- Layered: may a layer skip the one below? Event-driven: who owns the event contract, and how are ordering and duplicates handled?

**Distribution (monolito vs microservicios) (canonical, Lewis & Fowler 2014; Conway 1968)**
- Do we need independent deployment and scaling per part, or would a modular monolith with enforced boundaries suffice?
- Do team boundaries match service boundaries?
- Is each service's data owned by it alone? What happens when a call between services fails?

**Views (vistas de componentes y despliegue) (vault: Taller de Análisis y Diseño P2 §5)**
- Which interfaces does each component provide and require (interfaz proporcionada/requerida)?
- Which artifact (artefacto) runs on which node and execution environment (nodo, entorno de ejecución)? Which protocol connects nodes?
- Which view does this audience need (logical, development, process, physical + scenarios; Kruchten 1995)?

**ADR (registro de decisiones) (canonical, Nygard 2011)**
- Is this decision expensive to reverse? If so, is it recorded with context, decision, status, and consequences?
- Which alternatives were rejected, and why?

## Red flags

- Domain logic importing framework, database, or HTTP types.
- Microservices sharing a database, or chosen for a small team with no independent deploy need (distributed monolith).
- "Scalable"/"maintainable" stated without a measurable scenario.
- Layers bypassed ad hoc; circular dependencies between modules.
- Architecture diagram with no protocols, nodes, or interface direction.
- Irreversible decision with no recorded rationale or rejected alternatives.

## Output Contract

Reply with: the open decision, 2-4 questions from the matching block, any red flag seen (one line each), and one recommendation with its tradeoff (named quality attributes). Then wait for the user's choice.

## References (deep dive)

Read only when the user asks to go deeper or a concept is disputed:
- `~/Documents/Obsidian/INGENIERIA EN SOFT/Taller de Analisis y diseño de Software/P2/Resumen_Taller_Diseño_P2.md` §5 "El Modelo de Implementación y Despliegue" (component and deployment diagrams, worked example)
- `references/bibliography.md` (Perry & Wolf, Garlan & Shaw, Kruchten, Bass et al., ISO/IEC 25010, Cockburn, Martin, Lewis & Fowler, Conway, Nygard — canonical sources)
