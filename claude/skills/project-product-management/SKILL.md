---
name: project-product-management
description: "Trigger: estimate, scope creep, project risk, deadline, team, vendor, MVP, business model, ethics / estimar, plazos, riesgo del proyecto, equipo, cliente, idea de negocio, ética. Mentor checklist for project and product."
license: Apache-2.0
metadata:
  author: "damian"
  version: "0.1"
---

## Activation Contract

Load when the user plans, estimates, or leads a project, manages a team or stakeholders, assesses risks, buys or subcontracts, decides whether an idea is worth building, designs a business model or pitch, or hits an ethical doubt. Language-agnostic.

## Hard Rules

- Announce: `📚 Skill: project-product-management — <why>`.
- The user decides. Ask the matching questions and recommend; never set scope, estimate, priority, or contract terms unless the user delegates it.
- Speak only at decision points or when a red flag appears.
- Keep Spanish terms inline in parentheses, as the user studied them.
- Requirements, testing, and architecture belong to `se-process-requirements`, `se-testing-verification`, `software-architecture`; security/privacy depth to `security`; cross-reference, do not duplicate.

## Decision Gates

| Moment | Ask from |
|---|---|
| Sizing or committing to a date | Scope, schedule, cost (canonical) |
| Forming or leading a team | Team & leadership |
| Reporting, meetings, stakeholders | Communication |
| Starting, or a new threat appears | Risk |
| Buying, outsourcing, signing | Procurement |
| "Should we build this?" | Product & business model |
| Data, licenses, status honesty | Ethics (canonical) |

## Ask before deciding

**Scope, schedule, cost (canonical)**
- What is explicitly in and out (alcance)? Who approves a change, and who pays for it?
- Is this estimate a range with assumptions, or one number? Who made it, and who will do the work?
- What is forgotten: testing, integration, deployment, review?

**Team & leadership (equipo y liderazgo)**
- Which stage is the team in (formación, tormenta, normalización, desempeño)? Who is missing for the next one?
- Does everyone know the goal and their role? Did the team take part in the plan?
- Conflict source: scarce resources, schedule priorities, or work styles? Is feedback private, specific, about behavior (canonical)?

**Communication (comunicaciones)**
- Who needs what, how often, through which channel, and who escalates? Is a reply confirmed understood?
- Does the status report compare against the baseline (variación), not just say "on track"?

**Risk (riesgos)**
- Which events could hit scope, time, cost, quality? Is there a risk register?
- Probability and impact for each: severity from the matrix? Exposure (EMV) = probability x impact in money?
- Which top risks (Pareto line) get a response? Mitigation (reduce) vs contingency (if it happens)?
- Who owns it, what indicator triggers it, when is it re-reviewed?

**Procurement (abastecimiento)**
- Buy or build, and why? Which contract type shifts cost risk to whom (fixed price, time & materials, cost-reimbursable)?
- Clauses: change control, penalties, confidentiality, IP ownership, termination? Selection beyond price?

**Product & business model (modelo de negocio)**
- Which real problem, for whom, and what evidence (not opinion)? Problem hypothesis (does the pain exist?) or solution hypothesis (is it seen as useful)?
- What is the riskiest hypothesis, and the cheapest test (prototipo/MVP, disposable, built to learn)? Which indicator (KPI) and test card (tarjeta de pruebas) decide it?
- Who are the early adopters (adoptantes tempranos)? After the test: iterate or pivot (pivotear), on validated learning (aprendizaje validado), not downloads or followers?
- Who pays, why, how much (WTP, precio primero)? Does the revenue model fit the segment?
- Pitch: who is the audience? Impact measured by outcomes, not outputs (KPI)?

**Decision economics (canonical)**
- What is the opportunity cost? Does the benefit exceed the cost, and over what horizon (ROI)?

## Red flags

- A single-number estimate with no assumptions; commitment before scope is agreed.
- Scope change absorbed silently; no change owner.
- Risks known but unspoken; no register; no one owns a risk.
- Status "all green" with no baseline comparison.
- Building before any validation; features chosen before knowing who pays.
- Ethics (canonical): personal data collected without purpose or consent; unchecked licenses or copied code; claiming competence or status you lack; hiding estimate slips.

## Output Contract

Reply with: the open decision, 2-4 questions from the matching block, any red flag seen (one line each), and one recommendation with its tradeoff. Then wait for the user's choice.

## References (deep dive)

Read only when the user asks to go deeper or a concept is disputed:
- `references/vault-sources.md` (the user's vault notes and converted PDFs)
- `references/bibliography.md` (PMBOK, estimation, team dynamics, ethics, economics: canonical sources)
