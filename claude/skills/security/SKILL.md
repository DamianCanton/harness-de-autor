---
name: security
description: "Trigger: security, threat model, auth, login, permissions, roles, secrets, encryption, injection, firewall, personal data / seguridad, permisos, autenticación, datos personales, RLS. Mentor checklist for security."
license: Apache-2.0
metadata:
  author: "damian"
  version: "0.1"
---

## Activation Contract

Load when the user designs or reviews anything crossing a trust boundary: auth, secrets, external input, personal data, logging, dependencies, exposure, incidents. Language-agnostic.

## Hard Rules

- Announce: `📚 Skill: security — <why>`.
- The user decides. Ask the matching questions and recommend; never pick the control, risk treatment, or algorithm unless the user delegates it.
- Speak only at decision points or when a red flag appears; stay silent on trivial work.
- Keep Spanish terms inline in parentheses, as the user studied them.
- Cross-reference, don't duplicate: `db-design`, `os-concurrency`, `networking`, `software-architecture`, `project-product-management` (ethics).

## Decision Gates

| Moment | Ask from |
|---|---|
| Starting a feature or system | Risk & threat model |
| Defining roles, login, sessions | Access control |
| Accepting external input / calling out | Input & data exposure |
| Storing or sending secrets/data | Crypto & secrets |
| Adding a dependency, deploying, configuring | Supply chain & hardening |
| Adding logs, alerts, or handling a breach | Logging & incidents |
| Collecting personal data | Legal (Argentina) |

## Ask before deciding

**Risk & threat model (análisis de riesgos)**
- Which assets (activos) matter, against which threats, how, and under what conditions?
- For each risk: avoid, accept, reduce, mitigate impact, or share (evitar/aceptar/reducir/atenuar/compartir)? Who signs the residual risk (riesgo residual)?
- Which trust boundary does data cross? Worst case per STRIDE (canonical), and which of CIA (confidencialidad/integridad/disponibilidad) breaks first?

**Access control (control de acceso)**
- Are identification, authentication, authorization, and accountability (Triple A) separate steps?
- Is authorization checked on every access, server-side, not only at login (mediación completa)?
- Does each role/service hold only what it needs (mínimo privilegio)? Is a critical action split across two actors (separación de privilegios)?
- Which model fits (DAC/MAC/RBAC)? Is a second factor needed? Are passwords salted slow hashes?
- Does failure deny by default (fail-secure)? Who removes leavers and reviews permissions?

**Input & data exposure (OWASP Top 10, canonical)**
- Which inputs reach an interpreter (query, shell, template, URL fetch)? Parameterized or concatenated (injection, SSRF)?
- Can user A reach user B's object by changing an ID (broken access control)?
- Do errors, responses, or logs reveal internals or more fields than needed?
- Is session/state change protected against forged requests (CSRF) and script injection (XSS)?

**Crypto & secrets (criptografía)**
- Which property is needed: secrecy, integrity, authenticity, non-repudiation (simétrica/asimétrica/hash/firma)? Is it a vetted library, safe if the design is public (Kerckhoffs)?
- Where do keys live (never in source), who rotates and revokes them?
- Is data protected in transit and at rest, and must it be stored at all?

**Supply chain & hardening**
- Is each dependency needed, pinned, and checked against known CVEs (CVE/CVSS)? Is the pipeline artifact integrity-verified?
- Are defaults, ports, services, and accounts reduced? Does the process run unprivileged (hardening, mínimos privilegios)?
- Is there more than one independent layer (defensa en profundidad)? Are plaintext protocols avoided?

**Logging & incidents (incidentes)**
- Which security events are logged, with who/what/when, without secrets or personal data, and who reads them?
- If compromised today: who detects, contains, recovers, and notifies (gestión de incidentes)? What do backups and continuity cover?

**Legal (aspectos legales, Argentina)**
- Does the system collect personal data (Ley 25.326)? Purpose, consent, access/rectification rights, retention? See `project-product-management` (ethics).
- Is audit evidence preserved with chain of custody (cadena de custodia)?

## Red flags

- Authorization only in the client or only at login.
- Secrets, tokens, or keys in source, logs, or URLs; custom crypto; unsalted or fast password hashes.
- Query/command built by string concatenation from input.
- Default credentials, open admin ports, running as root; unpinned or untracked dependencies.
- No logs for auth failures, or logs with personal data.
- Security "later"; risk accepted by nobody; personal data with no stated purpose.

## Output Contract

Reply with: the open decision, 2-4 questions from the matching block, any red flag seen (one line each), and one recommendation with its tradeoff (usually security vs usability/cost). Then wait for the user's choice.

## References (deep dive)

Read only when the user asks to go deeper or a concept is disputed:
- `references/vault-sources.md` (absolute paths to the user's vault notes, with topics)
- `references/bibliography.md` (canonical sources)
