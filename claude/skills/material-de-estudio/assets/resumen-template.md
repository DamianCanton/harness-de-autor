# Resumen — writer prompt and structure

## Writer prompt (one Haiku agent per reading)

Read `fuentes-markdown/<Lectura>.md` from top to bottom and the page renders listed below. Write `scratchpad/<subject>-secciones/NN.md` in Spanish (neutral and professional).

Rules:
- Use the reading's exact terms and definitions. Keep every list complete, in its original order and with the same number of items.
- Describe every figure and table: its number, title, and contents.
- Mark answers to the review activities ("repaso") as deduced. Add **(a verificar)** when the text does not state them explicitly.
- Quote only short literal definitions and paraphrase the rest, so long verbatim passages do not trip the content filter.
- End the section with the callout `> [!important] Claves para el multiple choice`, listing counts, look-alike concepts, authors, years and percentages.
- Report: the commands you ran, the lines written, and any page you could not cover.

## Section skeleton

```markdown
## N. <Título literal de la lectura>
### N.1 <Subtema>
...
**Figura X: <título>.** <contenido>
> [!important] Claves para el multiple choice
> - ...
```

## Final document

Frontmatter (title, date, tags, aliases, fuentes) → H1 → one-paragraph scope → `> [!warning] Respuestas de repaso` → `## Mapa de los módulos` table with wikilinks to the PDFs → `# MÓDULO X` → sections.
