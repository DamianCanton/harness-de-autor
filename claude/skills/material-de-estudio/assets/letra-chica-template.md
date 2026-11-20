# Letra chica — structure

Purpose: the details that video summaries leave out and that distractors use. Link to the Resumen; do not repeat its general content.

Frontmatter (tags include `letra-chica`, `repaso`) → H1 → one line saying it complements the NotebookLM videos → `> [!info] Criterio usado` → `> [!warning] Dónde mirar primero`.

Sections:
1. **Listas completas, módulo por módulo**: one `> [!example]-` callout per reading. Each list has its exact count in the title, e.g. `**Elementos del modelo ambiental (6):** ...`. Also state which look-alike items are **not** in the list.
2. **Notación: símbolo, significado y trampa**: table per diagram type.
3. **Condiciones y excepciones**: "solo si", "siempre", "nunca" in the text.
4. **Trampas: pares de conceptos parecidos**: table `Par | Diferencia`.
5. **Conceptos secundarios y autores citados**: author (year) → claim or figure.
6. **Rarezas del texto**: inconsistencies in the reading (e.g. a list given with 5 items in one place and 6 in another); answer according to the reading.
7. **Autoevaluación rápida**: about 24 questions; the answers go in a collapsed `> [!tip]- Respuestas` callout.

Verify every count with grep before writing it.
