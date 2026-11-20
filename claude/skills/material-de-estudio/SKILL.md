---
name: material-de-estudio
description: "Trigger: material de estudio, resumen de lecturas, letra chica, parcial, examen multiple choice, NotebookLM videos/audios. Build exam study pack from PDF readings."
license: Apache-2.0
metadata:
  author: "damiancanton"
  version: "1.0"
---

## Activation Contract

Load when the user asks to build study material for an exam from PDF readings in an Obsidian subject folder: full summary (resumen), "letra chica" doc, and/or NotebookLM videos, audios, quiz, flashcards. Not for live tutoring or quizzing the user in chat.

## Hard Rules

- Keep the literal terminology of the readings: same terms, definitions, list order, and item counts. No synonyms.
- Every count, figure, author, year, and percentage in any output MUST be grepped from `fuentes-markdown/`, never written from memory (this includes NotebookLM prompts).
- Delegate writing and browser work to **Haiku** subagents; use **Sonnet** only for the coverage audit. Parent orchestrates, verifies, and merges.
- Never accept a subagent claim ("X is not in the source") without grepping the source yourself.
- Follow vault conventions: YAML frontmatter, wikilinks, callouts (`INGENIERIA EN SOFT/AGENTS.md`).
- NotebookLM: drive the user's browser via claude-in-chrome; never install a NotebookLM MCP.
- NotebookLM videos are always generated in the LONG format "Explicación" (the dialog defaults to "Corto"); tell the browser agent explicitly and require it to report the format used.
- Do not commit, and do not delete user files.

## Decision Gates

| Situation | Action |
|---|---|
| Reading > ~40 pages, or writer hits "Output blocked by content filtering" | Split into halves; tell the writer to paraphrase and quote only short literal definitions |
| Page has images (`pdfimages -list`) | Render it with `pdftoppm` and have the writer describe the figure/table |
| Browser session cannot see the user's tab group | Create its own group (`createIfEmpty: true`) and identify the notebook by its source list |
| User asks only for part of the pack | Run only those steps |

## Execution Steps

1. Create `fuentes-markdown/`; per PDF run `pdftotext -layout` with `<!-- página N -->` markers. Run shell loops inside `bash -c` (zsh does not word-split).
2. List pages with images; render them to `scratchpad/<subject>-pages/`.
3. Launch one Haiku writer per reading **in parallel**, each writing `scratchpad/<subject>-secciones/NN.md` per `assets/resumen-template.md`.
4. Concatenate into `Resumen - <Materia> - <Módulos>.md` (frontmatter, warning callout, module map table, sections).
5. Run a Sonnet coverage audit (missing lists, figures, numbers, wrong counts) against the sources; apply the confirmed fixes.
6. Haiku writes `Letra chica - <Materia> - <Módulos>.md` per `assets/letra-chica-template.md`, from the summary plus the sources.
7. Fill `assets/notebooklm-prompts.md` with verified counts and save it to scratchpad; one Haiku browser agent generates each Studio item (see `references/notebooklm-ui.md`).
8. Save to Engram; report.

## Output Contract

Return: the created files (paths), what NotebookLM items are ready or still generating, the audit fixes applied or skipped, and a "No verificado" line. Offer a 2-hour active-recall study plan in one line.

## References

- `assets/resumen-template.md` — section structure and writer prompt.
- `assets/letra-chica-template.md` — letra chica sections.
- `assets/notebooklm-prompts.md` — Studio prompt templates (P1–P7).
- `references/notebooklm-ui.md` — Dia/NotebookLM UI notes and pitfalls.
