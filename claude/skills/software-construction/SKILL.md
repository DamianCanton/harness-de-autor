---
name: software-construction
description: "Trigger: UI component, props vs state, REST API, endpoint, HTTP verb, status code, error handling, naming, code review, CI / componente, estado, API, manejo de errores, revisión de código. Mentor checklist for construction."
license: Apache-2.0
metadata:
  author: "damian"
  version: "0.1"
---

## Activation Contract

Load when the user builds component-based UIs, designs or consumes an HTTP/REST API, or asks about construction practice (defensive code, naming, review, version control, build/CI, refactoring). Language-agnostic: React or Spring are only examples.

## Hard Rules

- Announce: `📚 Skill: software-construction — <why>`.
- The user decides. Ask the matching checklist questions and recommend; never pick the state owner, resource model, or status codes unless the user delegates it.
- Speak only at decision points or when a red flag appears; stay silent on trivial work.
- Keep Spanish terms inline in parentheses, as the user studied them.
- Testing, security, and architecture questions belong to `se-testing-verification`, `security`, `software-architecture`; cross-reference, do not duplicate.

## Decision Gates

| Moment | Ask from |
|---|---|
| Splitting a UI into components | Component tree |
| Adding data that changes | Props vs state |
| Defining endpoints / resources | REST design |
| Wiring UI to an API | Consuming an API |
| Writing, reviewing, or refactoring code | Construction practice (canonical) |

## Ask before deciding

**Component tree (árbol de componentes)**
- Does data flow only parent → child (flujo unidireccional)? How does the child ask the parent to change it (callback)?
- Is rendering declarative (UI = f(state)) and the component pure, or is something mutating the view by hand?

**Props vs state (propiedades vs estado)**
- Who owns this datum? Is it passed in (immutable prop) or changes over time inside the component (state)?
- Which components truly need their own state, and which can take it from the lowest common ancestor (single source of truth / única fuente de verdad)?
- Is it derivable from existing state or props? 
- Are props validated (type, required, default)? What if one is missing?

**REST design (estilo REST)**
- Is each resource a noun with its own URI, and the verb carried by the HTTP method (GET read, POST create, PUT update, DELETE remove)?
- Which methods are safe or idempotent here? What happens if the client retries a POST/DELETE?
- Which status code per outcome (created, not found, invalid input, conflict)? Does the same code mean the same thing everywhere?
- Is the server stateless: does each request carry everything needed (auth, context)?
- Is REST the fit (CRUD over resources) versus SOAP? What is the contract (request, response, errors)?

**Consuming an API (consumo de API)**
- What does the UI show while loading, on empty, and on error? What if the API is down?
- Is the async result handled with failures caught? Is the call in a service layer, not in components?
- Do cross-origin rules (CORS) allow this client? Is the response shape validated?

**Construction practice (canonical, McConnell 2004)**
- Where are inputs validated, and what is the policy for the invalid case (defensive programming / programación defensiva)?
- Does the name say what, not how?
- Is the change small, one purpose per commit, and built and tested by CI?
- Is this a refactor (behavior unchanged, tests green) or a behavior change? Do not mix them.

## Red flags

- Child mutating props, or the same datum stored in two components.
- State copied from props, or state that is derivable.
- Verb in the URI (`/getProduct`), or an endpoint ignoring HTTP method semantics.
- Success code on error, or one catch-all code for every failure.
- Server holding client session state that breaks retries or scaling.
- UI with no loading or error path; API call swallowing errors.
- Refactor mixed with a feature; magic values; unreviewed large diff.

## Output Contract

Reply with: the open decision, 2-4 questions from the matching block, any red flag seen (one line each), and one recommendation with its tradeoff. Then wait.

## References (deep dive)

Read only when the user asks to go deeper or a concept is disputed:
- `~/Documents/Obsidian/INGENIERIA EN SOFT/Taller de Construccion de Software/Resumen - Taller de Construccion de Software - M3 y M4.md` §1-7 (§8 testing → `se-testing-verification`)
- `~/Documents/Obsidian/INGENIERIA EN SOFT/Taller de Construccion de Software/Letra chica - Taller de Construccion de Software - M3 y M4.md` (traps, HTTP codes)
- `~/Documents/Obsidian/INGENIERIA EN SOFT/Taller de Construccion de Software/fuentes-markdown/`
- `references/bibliography.md` (Fielding, McConnell, Fowler — canonical sources)
