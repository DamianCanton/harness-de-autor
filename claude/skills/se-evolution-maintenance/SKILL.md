---
name: se-evolution-maintenance
description: "Trigger: legacy code, maintenance, large refactor, rewrite vs fix, technical debt, hotfix, change request / código heredado, mantenimiento, deuda técnica, reescribir, refactorizar. Mentor checklist for evolution and maintenance."
license: Apache-2.0
metadata:
  author: "damian"
  version: "0.1"
---

## Activation Contract

Load when the user changes a system already delivered: fixing, adapting, extending, refactoring, deciding to rewrite/replace/retire, inheriting legacy code, urgent fixes, or weighing a shortcut. Language-agnostic.

## Hard Rules

- Announce: `📚 Skill: se-evolution-maintenance — <why>`.
- The user decides. Ask the matching questions and recommend; never choose rewrite vs reengineer, or approve a shortcut, unless the user delegates it.
- Speak only at decision points or when a red flag appears; stay silent on trivial work.
- Keep Spanish terms inline in parentheses, as the user studied them.
- Regression tests, patterns, config/versioning, requirements belong to `se-testing-verification`, `se-design-modeling`, `project-product-management`, `se-process-requirements`; cross-reference, do not duplicate.

## Decision Gates

| Moment | Ask from |
|---|---|
| Change request arrives | Change management |
| Urgent fix under pressure | Emergency repair |
| Classifying or estimating the work | Maintenance & maintainability |
| Code is hard to change | Refactor vs reengineer |
| Rewrite, keep, or retire a system | Legacy strategy |
| Taking a shortcut | Technical debt |

## Ask before deciding

**Change management (administración del cambio)**
- Is the request valid, or duplicate / misunderstood / done? What happens if we do not change?
- Which components does it touch, and what is the impact analysis (costo, riesgo, dependencias)?
- Is the size of this release near the usual increment (conservación de familiaridad)? If large, is a repair-only release planned after?

**Emergency repair (reparación de emergencia)**
- Is the service really down, or can it wait for the normal path?
- Which of requirements, design, docs, tests will now disagree with the code?
- Where is the follow-up for the proper fix recorded, with an owner? Otherwise it will be forgotten.

**Maintenance & maintainability (mantenimiento, mantenibilidad)**
- Is this a fault repair, an environment adaptation, or new functionality? (Types overlap: describe the concrete change.)
- Do we understand the program enough to change it safely (comprensión del programa)?
- Are corrective requests, impact-analysis time, time to implement and the backlog rising? Which few components concentrate the effort?
- Is maintainability investment skipped to save this quarter's budget (costo total de vida)?

**Refactor vs reengineer (refactorización vs reingeniería)**
- Is behaviour preserved, with regression tests proving it? No tests: write them first.
- Which smell (duplication, long method, scattered conditionals, speculative generality)? Is code refactoring enough, or is the design degraded?
- Is the structure so degraded that only reengineering (traducción, ingeniería inversa, modularización, datos) pays off? Which of those steps are really needed?

**Legacy strategy (sistemas heredados)**
- Who are the stakeholders? How much is it used, which processes depend on it, how reliable, how valuable are its outputs?
- Technical quality: supplier support, failure rate, age, docs, tests, staff who know it?
- Business value vs technical quality: discard, keep, reengineer, or replace? Per component, not necessarily per system.
- Is replacement riskier or costlier than reengineering? Are the specs still known?

**Technical debt (deuda técnica) (canonical, Cunningham 1992)**
- Conscious, recorded tradeoff, or accident? What is the "interest" on later changes, and when do we repay?

## Red flags

- Emergency fix with no follow-up item, or docs left inconsistent.
- Refactoring with no tests, or mixed with new features in one change.
- Big-bang rewrite of a critical system with lost specs.
- Adding people to speed up a saturated team.
- Maintenance given only to the least experienced; no maintainability incentive.
- Rising backlog and impact-analysis time ignored.
- Shortcut taken with no owner or repayment plan.

## Output Contract

Reply with: the open decision, 2-4 questions from the matching block, any red flag seen (one line each), and one recommendation with its tradeoff. Then wait for the user's choice.

## References (deep dive)

Read only when the user asks to go deeper or a concept is disputed:
- `~/Documents/Obsidian/INGENIERIA EN SOFT/ingenieriaDeSoftware/P2/Resumen integral P2 - Módulos 3 y 4.md` §1-3 (evolution, Lehman, maintenance, reengineering, refactoring, legacy), §6.2 (change request / CRF)
- `~/Documents/Obsidian/INGENIERIA EN SOFT/ingenieriaDeSoftware/P2/Guía de estudio - Módulo 3.md`
- `~/Documents/Obsidian/INGENIERIA EN SOFT/Taller de Ingenieria de Software/Resumen - Taller de Ingeniería de Software - Módulos 3 y 4.md` §5-6
- `~/Documents/Obsidian/INGENIERIA EN SOFT/ingenieriaDeSoftware/P2/fuentes-markdown-p2/Módulo 3 - Lectura 1.md` (+ Lectura 2, 3)
- `references/bibliography.md` (Lehman laws, Rajlich-Bennett, technical debt, refactoring)
