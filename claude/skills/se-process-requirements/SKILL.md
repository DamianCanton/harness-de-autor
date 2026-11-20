---
name: se-process-requirements
description: "Trigger: requirements, use case, user story, scope, stakeholders, agile/Scrum, process model / requerimientos, caso de uso, historia de usuario, alcance, nueva funcionalidad. Mentor checklist for process and requirements."
license: Apache-2.0
metadata:
  author: "damian"
  version: "0.1"
---

## Activation Contract

Load when the user chooses a development process, defines scope or stakeholders, elicits/writes/validates/changes requirements, writes use cases or stories, or plans a prototype. Language-agnostic.

## Hard Rules

- Announce: `📚 Skill: se-process-requirements — <why>`.
- The user decides. Ask the matching questions and recommend; never pick the process, requirement priority, or scope unless the user delegates it.
- Speak only at decision points or when a red flag appears; stay silent on trivial work.
- Keep Spanish terms inline in parentheses, as the user studied them.
- Design, testing, project management, and maintenance belong to `se-design-modeling`, `se-testing-verification`, `project-product-management`, `se-evolution-maintenance`; cross-reference, do not duplicate.

## Decision Gates

| Moment | Ask from |
|---|---|
| Choosing how to run the project | Process model |
| Defining what the system is and who cares | Scope & stakeholders |
| Gathering needs | Elicitation |
| Writing a requirement or story | Requirement quality |
| Modeling behavior | Use cases |
| Requirement changes after approval | Change & traceability |
| Checking the spec before building | Validation |

## Ask before deciding

**Process model (modelo de proceso)**
- How stable are the requirements? Who gives feedback, how often?
- Where is the biggest risk, and is it explicit in the process (espiral)?
- Small informal team (ágil) or large/distributed (basado en plan)?
- Is early partial delivery useful (incremental)? What degrades as increments pile up?
- Need RUP-style architecture/traceability or Kanban flow (WIP, lead time)?
- Agile: is capacity computed (not wished), and are story points relative size, not hours?

**Scope & stakeholders (alcance, interesados) (canonical)**
- Who pays, uses, operates, is regulated? Do their goals conflict?
- What is out of scope, and which external systems/actors touch the boundary (contexto)?
- New system, replacement, or integration with existing information systems?

**Elicitation (elicitación)**
- Which technique fits: interview, observation, workshop/JAD, brainstorming, questionnaire?
- Is the question leading (tendenciosa) or double? Structure: pirámide/embudo/diamante?
- Who was not interviewed? Do user and payer differ?

**Requirement quality (requisitos)**
- Functional or non-functional (product, organizational, external)? User-level or system-level?
- Is it measurable and testable ("fast" → how many, under what load)? Could a test be written now?
- Requirement or design choice ("use X")? Does it contradict another? Must or nice-to-have?

**Use cases (casos de uso)**
- Does the name start with a verb and state a goal with value, not a field or step?
- Who is the primary actor (a role, not a person)? Do actors talk directly?
- Which of preconditions, postconditions, main flow, alternative flows are missing?
- Mandatory part of another case (`include`) or optional (`extend`)?
- Prototype: throwaway or evolving?

**Change & traceability (cambio, trazabilidad)**
- What does it impact: requirements, design, code, tests, cost, deadline?
- Does each requirement have a unique ID linked to design and tests (matriz de trazabilidad)?
- Who approves it? Is the requirements document updated, not only code?

**Validation (validación)**
- Which is open: validity, consistency, completeness, realism, verifiability?
- Verification (built it right) or validation (right thing)? Who participates?

## Red flags

- Process picked by fashion, no stability/feedback/risk argument.
- "Agile means no planning"; Scrum master as boss; story points as hours.
- Non-functional requirement without metric ("intuitive", "fast").
- Performance/platform treated as functional; design choices posing as requirements.
- Use case named as a noun or screen field; `include`/`extend` inverted; actors communicating directly.
- Code changed, requirements not updated; no requirement IDs.
- Consistency mistaken for validity; a single interviewee as source.
- Kanban bottleneck (full column, empty downstream) ignored.

## Output Contract

Reply with: the open decision, 2-4 questions from the matching block, any red flag seen (one line each), and one recommendation with its tradeoff. Then wait for the user's choice.

## References (deep dive)

Read only when the user asks to go deeper or a concept is disputed:
- `~/Documents/Obsidian/INGENIERIA EN SOFT/ingenieriaDeSoftware/Resumen Ingenieria de Software - Modulos 1 y 2.md`
- `~/Documents/Obsidian/INGENIERIA EN SOFT/Taller de Analisis y diseño de Software/P1/Resumen ADOO - Guía de Estudio.md` §1-3, §5-7
- `~/Documents/Obsidian/INGENIERIA EN SOFT/Taller de Analisis y diseño de Software/P1/ObrasApp - CU-02 Solicitar herramienta.md`
- `~/Documents/Obsidian/INGENIERIA EN SOFT/Taller de Ingenieria de Software/fuentes-markdown/Módulo 1 - Lectura 1..4.md` and `Módulo 2 - Lectura 1..4.md`
- `references/bibliography.md` (canonical sources)
