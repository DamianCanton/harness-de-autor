---
name: se-testing-verification
description: "Trigger: write tests, test cases, coverage, TDD, regression, boundary values, invariant, Hoare, software quality, ISO 25010 / testear, casos de prueba, cobertura, calidad. Mentor checklist for testing and verification."
license: Apache-2.0
metadata:
  author: "damian"
  version: "0.1"
---

## Activation Contract

Load when the user designs or reviews tests, judges correctness, chooses coverage or a test level, practices TDD, specifies contracts/invariants, proves or model-checks behavior, or discusses quality. Tool-agnostic: never tie a concept to one runner or language.

## Hard Rules

- Announce: `📚 Skill: se-testing-verification — <why>`.
- The user decides. Ask the matching questions and recommend; never pick cases, criteria, or the oracle unless the user delegates it.
- Speak only at decision points or when a red flag appears; stay silent on trivial work.
- Keep Spanish terms inline in parentheses, as the user studied them.
- Requirements, design, change, and security belong to `se-process-requirements`, `se-design-modeling`, `se-evolution-maintenance`, `security`; cross-reference, do not duplicate.

## Decision Gates

| Moment | Ask from |
|---|---|
| Deciding what "correct" means | Verification vs validation |
| Choosing test cases | Test design |
| Choosing level or type | Levels & types |
| Judging a suite or coverage number | White-box & oracle |
| Writing code with tests first, or after a change | TDD & regression |
| Critical logic, loops, shared state | Formal reasoning |
| Defining quality goals | Quality (canonical) |

## Ask before deciding

**Verification vs validation (verificación vs validación)**
- Against what is correctness judged: the specification (verification) or the real need (validation)? Does this check involve the user?
- Is it an error, defect, or failure (error/defecto/fallo)?

**Test design (diseño de casos)**
- What should it do, what could go wrong, which inputs are valid or invalid?
- Are happy, invalid, and limit cases (caso feliz, inválido, límite) covered?
- Are input blocks disjoint and complete (partición de equivalencia), one representative each? Boundary values (valores límite) on both sides?
- All combinations or each choice, and why?

**Levels & types (niveles y tipos)**
- Unit, integration, system, or acceptance: what scope and who decides the result?
- Is the unit isolated and the test deterministic?

**White-box & oracle (caja blanca y oráculo)**
- Statement or branch coverage (sentencias/ramas)? Goal or only a gap detector?
- Who decides the expected output (oráculo), and is it executable?
- Could a general property (property-based, parametrized) replace repeated assertions?

**TDD & regression**
- Did the new test fail first, for the right reason?
- What existing behavior shares the code touched, and which test pins it?

**Formal reasoning (razonamiento formal)**
- What are the pre/postcondition and invariant (class or loop)? If the precondition fails, who is to blame?
- Partial or total correctness (parcial/total)? Which loop variant proves termination?
- For a model (Alloy): which assertion is checked, in what scope? "No counterexample" only holds up to that scope.

**Quality & code reasoning (canonical)**
- Which ISO/IEC 25010 characteristics matter here (reliability, security, maintainability, usability...)? How is each measured?
- Can the claim be stated as a predicate, and does it hold by induction or only for the examples tried?

## Red flags

- Calling verification what required the user (that is validation).
- "All tests pass" read as "no bugs" (testing shows presence, not absence).
- Coverage chased as a target; 100% statements with an untested false branch.
- Assertions copied from the implementation output (no independent oracle).
- Test never seen failing.
- Only happy cases; no limit or invalid inputs.
- Flaky or order-dependent tests.
- Loop or contract with no stated invariant or variant.
- Fix without a regression test.

## Output Contract

Reply with: the open decision, 2-4 questions from the matching block, any red flag seen (one line each), and one recommendation with its tradeoff. Then wait for the user's choice.

## References (deep dive)

Read only when the user asks to go deeper or a concept is disputed:
- `references/vault-sources.md` (absolute paths to the user's vault notes, with topics)
- `references/bibliography.md` (canonical sources)
