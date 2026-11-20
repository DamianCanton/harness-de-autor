# NotebookLM in Dia via claude-in-chrome — notes

- Load the claude-in-chrome tools in one ToolSearch call, then call `tabs_context_mcp` with `createIfEmpty: true`. A session cannot see tab groups created by other sessions.
- Find the right notebook by matching its source list against the PDF names.
- Studio panel: clicking a tile (Resumen en audio, Resumen en video, Cuestionario, Tarjetas didácticas) opens its customize dialog: "Tema personalizado" text box, format, language, and the **Generar ahora** button. There is no pencil icon to look for.
- NotebookLM may redirect from notebooklm.google.com to notebook.google.com; that is the same app.
- **Video format (MANDATORY): always pick the LONG format.** The dialog defaults to **"Corto"**, which is too short to cover a whole module. Before clicking Generar, select **"Explicación"** (the dialog offers only "Corto" and "Explicación") and confirm the selection in a screenshot. The Studio item then reads "Generando resumen en video explicativo...". Switching format changes the focus-chip grid: make sure no pre-checked chip (e.g. a single subtopic) narrows the video. Click inside the "Tema personalizado" box before typing. Report the chosen format for each video.
- Audio length has only **Predeterminada** and **Corta**. For a long audio, pick the **"Análisis detallado"** format (formerly "Análisis profundo").
- Several items can generate at the same time. Launching a new item does not duplicate one that is already generating.
- Videos take about 10 to 20 minutes. Report the item as "generando" and do not wait in a loop.
- The browser agent must return: each item's title, its state (listo or generando), and its duration when shown.
- Do not click delete or share. Do not accept dialogs.
