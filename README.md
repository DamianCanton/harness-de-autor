<div align="center">

# 🧰 claude-harness

**My Claude Code workbench: a mentor, not a ghostwriter.**

Claude Code + [gentle-ai](https://github.com/Gentleman-Programming/gentle-ai) + [Engram](https://github.com/Gentleman-Programming/engram) + [herdr](https://herdr.dev), with a pack of engineering-criteria skills distilled from a Software Engineering degree.

![herdr retro layout](herdr/retro/preview.png)

</div>

---

## Why this exists

> I'm the engineer. The AI asks, recommends, and reminds me of what I'd forget. It does not decide for me.

Most harnesses push the agent to do more. This one pushes it to **ask better**. Trivial things get done; anything that touches architecture, data, security, contracts, concurrency, or testing strategy stops at a question with options, tradeoffs, and one recommendation. If I say *"decidilo vos"*, it decides, and says what it assumed.

One `git clone` + `./install.sh` and any machine feels like mine.

## What's inside

```
claude-harness/
├── claude/
│   ├── damian-overrides.md      # my rules on top of gentle-ai (mentor mode lives in §7)
│   ├── settings.example.json    # model, hooks, plugins, permissions (machine data stripped)
│   ├── skills/                  # 15 skills I wrote (see below)
│   ├── hooks/damian-git-guard.sh# blocks `git add && git commit` and staged gitignored files
│   ├── statusline-command.sh    # dir · branch · dirty · ↑↓ · model · context bar · 5h/7d limits
│   ├── commands/ scripts/       # /codex-usage and the Codex cross-review helper
├── herdr/
│   ├── config.toml              # herdr base config
│   └── retro/                   # pixel-art layout: Spaces + Agents sidebar with live habitats
└── install.sh                   # symlinks everything into place, backs up what it replaces
```

## The stack

| Piece | Version | What I use it for |
|---|---|---|
| **Claude Code** | latest | The agent. Opus for the main thread, `effortLevel: medium`, fullscreen TUI. |
| **gentle-ai** | 4.2.0 | The harness layer. Installs the persona, the orchestrator and most agents/skills for me. |
| **Engram** | 3.4.0 | Persistent memory across sessions and compactions. |
| **herdr** | latest | Workspace for running agents side by side; the desktop app carries my retro layout. |
| **CodeGraph** | via gentle-ai | Indexed code graph; one query instead of a grep/read loop. |
| **Codex plugin** | `openai/codex-plugin-cc` | Second opinion: cross-review after non-small changes. |
| **Context7** | MCP | Up-to-date library docs instead of stale training data. |

### What I actually use from gentle-ai

- **Gentleman persona / output style**: a senior mentor voice (Rioplatense Spanish when I write in Spanish, English artifacts always).
- **ODD (Organic Driven Development)**: small work inline; large work gets a task doc with verbatim specs, a log, and work-unit commits. Subagents only for a named reason.
- **Skill registry hook**: refreshes `.atl/skill-registry.md` on every prompt so skills route by project.
- **Review lenses + judgment-day**: blind dual review (`jd-judge-a/b`) and risk/resilience/readability/reliability reviewers.
- **work-unit-commits / chained-pr / branch-pr**: reviewable slices of ~400 lines, PRs that don't drown reviewers.
- **skill-creator**: the style guide every skill here follows.

Turned off on purpose (in `skillOverrides`): hyperframes, go-testing, comment-writer, issue-creation, and a few others I don't use.

### Why Engram

Claude forgets everything between sessions. Engram doesn't. The agent saves decisions, bug causes, and conventions **as it works** (`mem_save`), and on a new session or after compaction it pulls them back (`mem_context` → `mem_search`). Memories are scoped per project, so the uni vault never bleeds into client work. It's what makes "remember what we decided last week" actually work.

## The skill pack

Fifteen skills, written from my degree notes and canonical sources (bibliography in each `references/`). Language-agnostic by design: no Java, no framework, just criteria. Every skill announces itself (`📚 Skill: <name> — <why>`), asks 2-4 questions at decision points, flags red flags, and gives **one** recommendation with its tradeoff.

| Skill | Wakes up on |
|---|---|
| `se-design-modeling` | domain model, UML, CRC, GRASP, design patterns |
| `se-process-requirements` | new feature, scope, use cases, user stories |
| `se-testing-verification` | test cases, boundary values, coverage, ISO 25010 |
| `se-evolution-maintenance` | legacy, rewrite vs refactor, technical debt |
| `software-construction` | components, REST, status codes, error handling |
| `software-architecture` | layers, hexagonal, monolith vs services, ADRs |
| `programming-paradigms-oop` | inheritance vs composition, SOLID, purity |
| `algorithms-data-structures` | Big-O, graphs, choosing a structure |
| `db-design` | schema, normalization, keys, migrations, indexes |
| `os-concurrency` | race conditions, locks, deadlocks, "it's slow" |
| `networking` | timeouts, retries, DNS, TLS, latency |
| `security` | auth, RLS, secrets, OWASP, personal data (Ley 25.326) |
| `stats-for-engineering` | benchmarks, A/B, confidence intervals, p99 |
| `project-product-management` | estimates, deadlines, scope creep, ethics |
| `material-de-estudio` | turns course PDFs into an exam study pack |

Triggers are bilingual (English + Spanish), so *"agregá una tabla"* routes to `db-design` just like *"add a table"*.

**Tested, not hoped.** Three rounds of dry-run agents on a real Next.js + Supabase project: 14/14 picked the right skill and asked before deciding; then trivial, delegated, and mixed prompts on Haiku went from 9/12 to 10/12, and the remaining misses were fixed with sharper rules. None of them touched the repo.

## Install

**1. Tools** (macOS / Homebrew)

```bash
brew install gentleman-programming/tap/gentle-ai gentleman-programming/tap/engram herdr
gentle-ai install        # persona, orchestrator, agents, gentle-ai skills, hooks
```

Then, inside Claude Code, add the plugins:

```
/plugin marketplace add Gentleman-Programming/engram
/plugin marketplace add openai/codex-plugin-cc
/plugin install engram@engram
/plugin install codex@openai-codex
```

The retro layout runs on the **herdr desktop app** (`Herdr.app`, which ships `herdr-app`), not only the CLI. Get it from [herdr.dev](https://herdr.dev).

**2. This repo**

```bash
git clone https://github.com/DamianCanton/claude-harness.git ~/claude-harness
cd ~/claude-harness
./install.sh --dry-run   # see what it would do
./install.sh
```

`install.sh` symlinks skills, overrides, hooks, and herdr files, so a `git pull` updates the harness. Anything it replaces is moved to `~/.claude-harness-backups/<timestamp>/`. It is idempotent.

> ⚠️ `settings.json` is **copied, not linked**. Claude Code writes machine-specific data into it, and a symlink would leak that into a public repo. If you already have one, merge `claude/settings.example.json` by hand.

## Make it yours

- **The rules**: `claude/damian-overrides.md`. §7 is mentor mode; rename the file and the `@` import in `CLAUDE.md` if you fork it.
- **Deep-dive links**: some skills point to notes in my Obsidian vault (`~/Documents/Obsidian/...`). Without the vault they're just dead links; the skills still work.
- **herdr retro**: read `herdr/retro/RECIPE.md` first. The sidebar mod runs `git` in each space's folder to show branch and ahead/behind.

## Not included (on purpose)

History, sessions, project memories, telemetry, caches, credentials, and anything gentle-ai generates (`gentle-ai install` recreates it, always on the current version).

## License

[Apache-2.0](LICENSE). gentle-ai and Engram are MIT, herdr is Apache-2.0, each under its own repo.
