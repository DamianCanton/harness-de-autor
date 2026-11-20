<div align="center">

# 🎬 harness-de-autor

### *An auteur's harness for Claude Code.*

**I'm the engineer. The AI is the crew.**
It asks, warns, and reminds me of the stuff I'd forget at 2 a.m. It doesn't get to decide what we build.

[![Claude Code](https://img.shields.io/badge/Claude_Code-harness-D97757?style=flat-square)](https://claude.com/claude-code)
[![gentle-ai](https://img.shields.io/badge/gentle--ai-4.2.0-8A2BE2?style=flat-square)](https://github.com/Gentleman-Programming/gentle-ai)
[![Engram](https://img.shields.io/badge/Engram-3.4.0-2E8B57?style=flat-square)](https://github.com/Gentleman-Programming/engram)
[![herdr](https://img.shields.io/badge/herdr-retro_layout-FF9E3D?style=flat-square)](https://herdr.dev)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue?style=flat-square)](LICENSE)

![herdr retro layout](herdr/retro/preview.png)

</div>

---

## ☕ The idea

Most AI setups try to make the agent do **more**. This one makes it **ask better**.

Think cinéma d'auteur: one person's taste and rules on every frame. These are mine, distilled from my Software Engineering degree and a lot of "why did the AI just rewrite my whole module?" moments.

| You say | The agent does |
|---|---|
| *"renombrá esta función"* | Just does it. Naming isn't a meeting. |
| *"agregá una tabla de historial"* | Stops. Gives the options, the tradeoffs, **one** recommendation. Waits. |
| *"decidilo vos"* | Decides, states what it assumed in one line, keeps going. |
| *"renombrá X y agregá una columna"* | Does the rename now, asks only about the schema. |
| *"¿qué hace esta función?"* | Answers. No lecture. |

The line between "just do it" and "ask me" lives in [`claude/damian-overrides.md`](claude/damian-overrides.md) §7: architecture, data model, security, public contracts, concurrency, testing strategy, and anything irreversible are mine. Everything else is the crew's.

## 🧰 The crew

| Tool | What it does in my setup |
|---|---|
| [**Claude Code**](https://claude.com/claude-code) | The agent. Opus on the main thread, medium effort, fullscreen TUI. |
| [**gentle-ai**](https://github.com/Gentleman-Programming/gentle-ai) | The harness layer by [Gentleman Programming](https://github.com/Gentleman-Programming). One `gentle-ai install` and the persona, orchestrator, agents, and skills are in place. |
| [**Engram**](https://github.com/Gentleman-Programming/engram) | Memory that survives sessions and compactions. |
| [**herdr**](https://herdr.dev) | Where the agents live, side by side, with my pixel-art retro layout. |
| **CodeGraph** | Ships with gentle-ai. A code knowledge graph: one query instead of a grep-and-read loop. |
| [**Codex plugin**](https://github.com/openai/codex-plugin-cc) | A second pair of eyes from another model, for cross-review after big changes. |
| [**Context7**](https://context7.com) | Current library docs, so the agent doesn't code against a two-year-old API. |
| [**Obsidian**](https://obsidian.md) | My uni notes vault. The skills cite it for deep dives. |
| [**Wispr Flow**](https://wisprflow.ai) | I talk, it types. Half my prompts are dictated. 🎙️ *Soon to be replaced by my own version. Stay tuned.* |

### 🎩 What I use from gentle-ai

- **Gentleman persona**: a senior-architect mentor voice. Rioplatense Spanish when I write in Spanish, English in every artifact it produces.
- **ODD (Organic Driven Development)**: small stuff inline; big stuff gets a task doc with my exact words as specs, a log, and commits per work unit. Subagents only when there's a real reason.
- **Skill registry hook**: refreshes on every prompt, so the right skill shows up per project.
- **judgment-day + review lenses**: blind dual review, plus risk, resilience, readability, and reliability reviewers.
- **work-unit-commits / chained-pr / branch-pr**: ~400-line slices, so nobody drowns reviewing.
- **skill-creator**: the style guide every skill in this repo follows.

Turned off on purpose: hyperframes, go-testing, comment-writer, issue-creation, and a few others I don't use.

### 🧠 Why Engram

Claude has the memory of a goldfish between sessions. Engram fixes that.

The agent saves decisions, root causes, and conventions **while it works** (`mem_save`). On a new session or after a compaction, it pulls them back (`mem_context` → `mem_search`). Memories are scoped per project, so my uni notes never leak into client work.

That's what makes *"remember what we decided last week?"* actually work.

## 📚 The skill pack

Fifteen skills written from my degree notes plus canonical sources (each has a `references/bibliography.md`). **Language-agnostic on purpose**: no Java, no framework, just engineering criteria.

Every skill:
- announces itself: `📚 Skill: db-design — vas a agregar una tabla`
- asks sharp questions, only at decision points
- flags red flags in one line each
- gives **one** recommendation with its tradeoff, then waits

| Skill | Wakes up when you say... |
|---|---|
| `se-design-modeling` | domain model, UML, CRC, GRASP, "¿qué patrón uso?" |
| `se-process-requirements` | new feature, scope, use cases, user stories |
| `se-testing-verification` | test cases, boundary values, coverage, ISO 25010 |
| `se-evolution-maintenance` | legacy, "¿lo reescribimos?", technical debt |
| `software-construction` | components, REST, status codes, error handling |
| `software-architecture` | layers, hexagonal, monolith vs services, ADRs |
| `programming-paradigms-oop` | inheritance vs composition, SOLID, pure functions |
| `algorithms-data-structures` | Big-O, graphs, "¿qué estructura uso?" |
| `db-design` | schema, normalization, keys, migrations, indexes |
| `os-concurrency` | race conditions, locks, "anda lento" |
| `networking` | timeouts, retries, DNS, TLS, latency |
| `security` | auth, RLS, secrets, OWASP, personal data (Ley 25.326) |
| `stats-for-engineering` | benchmarks, A/B, confidence intervals, p99 |
| `project-product-management` | estimates, deadlines, scope creep, ethics |
| `material-de-estudio` | turns course PDFs into an exam study pack |

Triggers are bilingual, so *"agregá una tabla"* and *"add a table"* land in the same place.

### 🧪 Tested, not hoped

Three rounds of read-only dry-run agents on a real Next.js + Supabase app:

- **Round 1 (14 prompts):** 14/14 loaded the right skill, announced it, and asked before deciding. Along the way they flagged real bugs the app had.
- **Rounds 2-3 (Haiku; trivial, delegated, and mixed prompts):** 9/12 → 10/12. The remaining misses were patched with sharper rules.

## 🚀 Install

**1. The tools** (macOS + Homebrew)

```bash
brew install gentleman-programming/tap/gentle-ai gentleman-programming/tap/engram herdr
gentle-ai install
```

Inside Claude Code:

```
/plugin marketplace add Gentleman-Programming/engram
/plugin marketplace add openai/codex-plugin-cc
/plugin install engram@engram
/plugin install codex@openai-codex
```

The retro layout runs on the **herdr desktop app** (`Herdr.app`). Get it at [herdr.dev](https://herdr.dev).

**2. This repo**

```bash
git clone https://github.com/DamianCanton/harness-de-autor.git ~/Documents/harness-de-autor
cd ~/Documents/harness-de-autor
./install.sh --dry-run   # preview, touches nothing
./install.sh
```

`install.sh` symlinks everything, so a `git pull` updates the harness and any edit you make lands back in the repo.
- Anything it replaces goes to `~/.claude-harness-backups/<timestamp>/`.
- Running it twice changes nothing.

> ⚠️ `settings.json` is **copied, never linked**. Claude Code writes machine-specific data into it, and a symlink would push that into a public repo. If you already have one, merge [`claude/settings.example.json`](claude/settings.example.json) by hand.

## 🗂️ What's inside

```
harness-de-autor/
├── claude/
│   ├── damian-overrides.md       # my rules on top of gentle-ai (mentor mode = §7)
│   ├── settings.example.json     # model, hooks, plugins, permissions
│   ├── skills/                   # the 15 skills above
│   ├── hooks/damian-git-guard.sh # blocks force-adds and chained add+commit
│   ├── statusline-command.sh     # dir · branch · dirty · ↑↓ · model · context bar · 5h/7d limits
│   └── commands/ scripts/        # /codex-usage + Codex cross-review helper
├── herdr/
│   ├── config.toml
│   └── retro/                    # pixel-art sidebar: Spaces + Agents
└── install.sh
```

## 🍴 Make it yours

- **Fork the rules, not just the files.** `damian-overrides.md` is the soul of this repo. Rename it, rewrite §7 with your own line between "just do it" and "ask me", and point the `@` import in `CLAUDE.md` at it.
- **Dead links are fine.** Some skills point to my Obsidian vault (`~/Documents/Obsidian/...`). Without it those links go nowhere, and the skills still work.
- **Read the recipe first.** Before installing the herdr retro layout, read [`herdr/retro/RECIPE.md`](herdr/retro/RECIPE.md). The sidebar runs `git` in each workspace folder to show the branch and ahead/behind counts.

## 🚫 Not included (on purpose)

- History, sessions, and memories
- Telemetry and caches
- Credentials
- Anything gentle-ai generates (`gentle-ai install` rebuilds it fresh, on the current version)

---

<div align="center">

Made in 🇦🇷 by [Damián Canton](https://github.com/DamianCanton), mate in hand 🧉
Standing on the shoulders of [Gentleman Programming](https://github.com/Gentleman-Programming).

**[Apache-2.0](LICENSE)** · gentle-ai and Engram are MIT · herdr is Apache-2.0

</div>
