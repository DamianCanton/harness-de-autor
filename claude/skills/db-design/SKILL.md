---
name: db-design
description: "Trigger: database schema, table, ER diagram, normalization, key, SQL, migration, transaction, index, trigger / base de datos, tabla, esquema, migración, normalizar, consulta. Mentor checklist for relational design and SQL."
license: Apache-2.0
metadata:
  author: "damian"
  version: "0.1"
---

## Activation Contract

Load when the user designs a relational model or writes SQL: keys, normalization, ERD, DDL/DML/DCL/TCL, routines/triggers, transactions, indexes. Engine-agnostic.

## Hard Rules

- Announce: `📚 Skill: db-design — <why>`.
- The user decides. Ask and recommend; never pick keys, normal form, isolation level, or index unless the user delegates.
- Speak only at decision points or red flags; silent on trivial work.
- Keep Spanish terms inline in parentheses, as the user studied them.
- Class modeling, requirements, access control, locks belong to `se-design-modeling`, `se-process-requirements`, `security`, `os-concurrency`; cross-reference, do not duplicate.

## Decision Gates

| Moment | Ask from |
|---|---|
| Starting from a problem | Problem → model |
| Choosing keys, domains, constraints | Keys & constraints |
| Repeated or derived facts | Dependencies & normalization |
| Drawing ERD / mapping to tables | ERD → relational |
| Writing a query | Query |
| DML/DDL, migration, deploy | Statements & migrations |
| Logic inside the database | Routines & triggers |
| Concurrent writers, slow query | Transactions & performance |

## Ask before deciding

**Problem → model (del problema al modelo)**
- Which questions must the data answer (análisis antes que diseño)?
- Entity, attribute, or relationship?

**Keys & constraints (claves, dominios, restricciones)**
- Which candidate key is minimal and stable (clave candidata)? Natural or surrogate?
- What does NULL mean here: not applicable or unknown? Must it be allowed?
- Does the type match the domain (length, collation in comparisons)?
- Which rules become constraints (unique, check, FK actions)?

**Dependencies & normalization (dependencias funcionales, normalización)**
- What determines what? Does every non-key attribute depend on the key, the whole key, and nothing but the key (1FN/2FN/3FN/BCFN)?
- Repeated groups (`phone1, phone2`)? Which anomaly (inserción, actualización, borrado)?
- If denormalizing: which measured read cost justifies it, and who keeps copies consistent?

**ERD → relational (DER → modelo relacional)**
- Cardinality min..max on both ends; total or partial participation?
- 1:M → FK on the many side; M:N → associative table; weak entity → owner key + discriminator; multivalued → own table.
- Specialization (especialización): one table or one per subtype? State the tradeoff; the sources give no single rule.

**Query (consulta)**
- Filtering rows (WHERE) or groups (HAVING)?
- Join, scalar subquery, or IN/ANY/ALL: how many rows per side? Inner or outer?
- How do NULLs behave in comparisons, counts, `NOT IN`?

**Statements & migrations (DML/DDL/DCL/TCL)**
- WHERE tested as a SELECT first?
- DDL reversible, or implicit commit (DELETE/TRUNCATE/DROP vary by engine)?
- Where is the commit boundary? Minimum privileges (GRANT/REVOKE) per role?
- Is the migration rehearsed on a copy?

**Routines & triggers (rutinas, cursores, triggers)**
- Server (reuse, less traffic) or application (portability, server load)? Can a set statement replace the cursor?
- Trigger BEFORE or AFTER? What happens to the statement when it errors?

**Transactions & performance (canonical)**
- Which invariants must hold together (ACID)? Which isolation level; which anomaly (dirty, non-repeatable, phantom, lost update) is acceptable?
- Optimistic or pessimistic; deadlock and retry handling?
- Query plan read before adding an index? What do writes pay?

## Red flags

- Multi-valued cell or numbered columns; partial or transitive dependency.
- No primary key or a volatile one.
- UPDATE/DELETE with no WHERE; DROP/TRUNCATE assumed rollbackable.
- Commit mid-unit; rule only in app code.
- Cursor where a set statement works; hidden trigger writes.
- Migration pushed to a shared/remote database, or written without checking others' migrations for collisions; see the user's migration rules in `~/.claude/damian-overrides.md`.
- Index without reading the plan; unmeasured denormalization.

## Output Contract

Reply with: the open decision, 2-4 questions from the matching block, red flags seen (one line each), one recommendation with its tradeoff. Then wait.

## References (deep dive)

Read only when the user asks or a concept is disputed:
- `~/Documents/Obsidian/INGENIERIA EN SOFT/Base de datos 1/P1/Resumen Base de Datos 1 - Modulos 1 y 2.md` (keys, algebra, FDs, normalization, ERD, mapping; readings `Modulo 1|2 - Lectura 1-4.md` in the same folder)
- `~/Documents/Obsidian/INGENIERIA EN SOFT/Base de datos 1/P2/Resumen Base de Datos P2.md` (SQL, DML/DDL/TCL, types, routines, cursors, triggers)
- `~/Documents/Obsidian/INGENIERIA EN SOFT/Base de datos 1/P2/Atlas visual Base de Datos P2.md` (query pipeline, transactions, trigger lifecycle)
- `references/bibliography.md` (transactions, isolation, concurrency, indexing, denormalization: canonical)
