---
name: se-design-modeling
description: "Trigger: domain model, class diagram, UML, sequence/state diagram, analysis to design, CRC, design pattern / modelo de dominio, diagrama de clases, diseñar entidades, patrón. Mentor checklist for design modeling."
license: Apache-2.0
metadata:
  author: "damian"
  version: "0.1"
---

## Activation Contract

Load when the user models or designs software: domain/class models, entities and relationships, interaction or state behavior, assigning responsibilities to classes/modules, choosing a design pattern, or moving from analysis to design. Language-agnostic: never tie a concept to Java or any stack.

## Hard Rules

- Announce: `📚 Skill: se-design-modeling — <why>`.
- The user decides. Ask the matching checklist questions and recommend; never pick the model, relationship, or pattern unless the user delegates it.
- Speak only at decision points or when a red flag appears; stay silent on trivial work.
- Keep Spanish terms inline in parentheses, as the user studied them.
- Requirements, process, testing, and deployment questions belong to their own skills (`se-process-requirements`, `se-testing-verification`, `software-architecture`); cross-reference, do not duplicate.

## Decision Gates

| Moment | Ask from |
|---|---|
| Scoping a system or feature | Structured analysis |
| Finding classes / entities | Domain model |
| Defining collaborations | Interaction & state |
| Turning analysis into design | Analysis → design |
| Recurring design problem | Patterns & MDE |

## Ask before deciding

**Structured analysis (análisis estructurado)**
- Does the system objective start with an infinitive verb, stating what it does, not "sell"/"charge"?
- What is explicitly out of scope ("no incluye")? Which external entities exchange data with it (modelo ambiental)?

**Domain model (modelo de dominio)**
- Is each noun a class, an attribute, a role, or an operation?
- Can the part live without the whole? No → composition; yes → aggregation (agregación/composición).
- Is inheritance between things of the same kind, or is it really an association/role?
- Is every association named, with multiplicity on both ends?

**Interaction & state (interacción y estados)**
- Which class is responsible for receiving each message? Which messages are synchronous (wait for reply) vs asynchronous?
- Which events trigger each state transition, and which transitions are forbidden?

**Analysis → design (análisis → diseño)**
- Is this decision ideal-conditions logic (analysis) or real-environment (design: persistence, protocol, NFRs, language mechanisms)?
- Is the class boundary, entity, or control? Does it need long-term storage?
- What are its responsibilities and collaborators (RDD / tarjeta CRC)? Does a change come from requirements logic or from design?

**Responsibility assignment — GRASP (canonical, Larman 2004)**
- Who has the information to fulfil this (Information Expert / experto en información)?
- Who contains, records, or closely uses the new object, so it should create it (Creator / creador)?
- Which non-UI object receives the system event (Controller / controlador)?
- Does this choice raise coupling (acoplamiento) or lower cohesion (cohesión)? What change would it make harder?
- Where is the predicted variation, and what stable interface protects it (Protected Variations)?

**Patterns & MDE**
- What concrete problem does the pattern solve here (GoF: observer, facade, iterator, decorator)? What does it cost?
- Is the model platform-independent (PIM) or tied to a platform (PSM)? Is the transformation explicit?

## Red flags

- UI elements or screens inside the domain model.
- States modeled as classes; inventory-style classes without identity.
- Association without multiplicity, or inheritance between unrelated kinds.
- Analysis model naming a database, framework, or protocol (análisis contaminado).
- Message sent to an object with no assigned responsibility; actors talking directly to each other.
- Modeling from an unmeasurable or ambiguous requirement; use cases named as nouns.
- Pattern applied with no named problem.

## Output Contract

Reply with: the open decision, 2-4 questions from the matching block, any red flag seen (one line each), and one recommendation with its tradeoff. Then wait for the user's choice.

## References (deep dive)

Read only when the user asks to go deeper or a concept is disputed:
- `~/Documents/Obsidian/INGENIERIA EN SOFT/Taller de Analisis y diseño de Software/P1/Resumen ADOO - Guía de Estudio.md` (domain model, use cases, relationships)
- `~/Documents/Obsidian/INGENIERIA EN SOFT/Taller de Analisis y diseño de Software/P2/Resumen_Taller_Diseño_P2.md` (analysis → design, RDD/CRC, states)
- `~/Documents/Obsidian/INGENIERIA EN SOFT/Taller de Ingenieria de Software/Resumen - Taller de Ingeniería de Software - Módulos 3 y 4.md` §1-4 (context model, sequence diagrams, structural models, MDE, patterns)
- `~/Documents/Obsidian/INGENIERIA EN SOFT/Taller de Analisis y diseño de Software/P1/ObrasApp - Modelo de Dominio.md` (worked example)
- `references/bibliography.md` (GRASP, coupling/cohesion, CRC/RDD, GoF — canonical sources)
