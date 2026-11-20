# Retro

A pixel-art herdr window. The left sidebar has two panels: **Spaces** on top, a small pixel character beside each workspace, and **Agents** below, one card per running agent. Each card shows the agent's character in a habitat that tracks its state: animated while it works, shaking under a "!" bubble when it needs you, jumping with sparkles when done, asleep at night when idle. The terminal sits on the right in a rounded pane, with the shipped tabs bar above it and a status bar below.

![Retro](preview.png)

## What you see

Left to right:

1. **Sidebar**, 268 px wide (min 44, max 480), background `#13131f`. Top to bottom:
   - **Brand**, 46 px: shipped `workspace-chrome`, window-drag enabled.
   - **Spaces** (retro-sidebar, `role: "spaces"`): weight 1, min 90 px. Header "Spaces" in 11.5 px `#5f5f82`, with a 26 px plus button at the right.
   - **Agents** (retro-sidebar, `role: "agents"`): weight 2, min 90 px. Header "Agents" in 11.5 px medium `#5f5f82`, 41 px tall, with a sort icon at the right.
   - **Footer**, 69 px: shipped `workspace-chrome` with `footer: true`.
2. **Work area**, the rest of the width:
   - **Tabs bar**, 42 px: shipped `tabs`, window-drag enabled.
   - **Pane area**, 8 px padding and gap: one pane, 10 px radius, 1 px `#2c2c46` border, 1 px `#ff9e3d` focus ring, background `#161625`, 30 px header always shown at the top (shipped `pane`). The terminal padding is 14 and 12 px.
   - **Files/Changes panel**: in the layout, hidden.
   - **Status bar**, 28 px: shipped `workspace-status`.

Canvas `#10101c`. Dividers 1 px `#2c2c46`.

**Space rows**: 30 px tall (28 px for a worktree), 8 px radius. The active row fills `#2f2a48`; hover fills `#2a2a44`. Each row has a 28 by 26 px avatar, then the name (13 px, `#d6d6e7`, max 150 px, truncated). In 11.5 px `#5f5f82` comes the repo and branch, only when unusual (`master` and `main` are left out, and so is any name that repeats the space name), then `↑` ahead and `↓` behind counts.

**Agent cards**: 5 px padding, 9 px gap, 6 px radius, fill `#1b1b2c`, 2 px `#2c2c46` border (2 px `#ff9e3d` when focused). On the left, an 80 by 64 px habitat with a 1 px `#2c2c46` border and 3 px radius; the 56 by 52 px avatar stands 12 px from the left and 10 px from the top. On the right, top to bottom:
- A status tag, 16 px tall, JetBrains Mono 9.5 px bold, in the status color with a 15% fill and 40% border. At the right of that row, the time since the last change in 10.5 px `#5f5f82`.
- The space name, 13 px semibold `#d6d6e7` (`#9a9ab8` when asleep).
- A detail line, 11 px `#5f5f82`: the tab name or agent title, else the program name.

Status colors: working `#5ad4e6`, blocked `#ff6b81`, done `#7bd88f`, idle `#7a7aa0`.

**Sub-agents**: 26 px rows indented 39 px, with tree lines (├ └ │) drawn as borders.

## How it behaves

| Status | Card tag | Section | Habitat | Avatar loop | List row marker |
|---|---|---|---|---|---|
| working | WORKING | Working | day | 0.6 s: a token flies in and is eaten | spinning 12 px icon |
| blocked | NEEDS YOU | Needs you | day | 0.83 s: shakes side to side under a "!" bubble | "Needs you" pill; "!" in a 14 px box in the rail |
| done | DONE | Done | day | 1.24 s: happy jump with sparkles, eyes shut | solid 7 px dot |
| idle | IDLE | Idle | night | 2.4 s: asleep, eyes shut, a "z" drifts up | 7 px ring; name muted |

- **Priority sort** (default): sections in the order Needs you, Done, Working, Idle. Inside a section, the most recent change comes first. Section headers take the status color (Idle is dim) and show a count. Click a header to fold it.
- **Done holds**: a done agent you have looked at turns idle, but stays under Done until you move focus away.
- **Times**: "<1m", then "Nm", "Nh", "Nd". They refresh every 30 s and hide while the pointer is over the card.
- **Pins**: hovering a card shows a pin icon beside the time. Click to pin or unpin. Pinned agents go in a "Pinned" group at the top.
- **Click an agent card**: focuses its pane. **Click a sub-agent row**: focuses its pane if it has one, otherwise peeks at it.
- **Folding**: a card with sub-agents shows a chevron with the count (colored by its most urgent child when folded). Click to fold.
- **Sort popup**: the sort icon in the Agents header opens a 200 by 140 px popup with "Priority" (clock icon) and "Grouped by space" (layers icon), a check mark on the current one. In grouped mode, each space name is a header; a folded header shows its count and its most urgent status (not idle).
- **Spaces**: click selects. Drag onto another space in the same machine to reorder (a 2 px accent line marks the target). Right-click opens the shipped `menu` popup, 200 by 260 px. Machine headers ("This computer" or a remote name) fold on click; "+" appears on hover, and "New space there" adds a space on that machine.
- **Rail**: when the sidebar is narrower than 160 px, Spaces shows a number and a status glyph (● for blocked or done, · otherwise), and Agents shows a number and a status icon. The "»" at the bottom of Agents restores the sidebar to its saved width (268 px by default), or collapses it to 76 px on macOS and 44 px elsewhere.
- **Keys**: in this layout, `ctrl-shift-l` switches back to `main`.
- **What moves**: cards re-sort when a status changes. Habitats switch day and night with state. Durations tick every 30 s. Spaces reorder themselves so each worktree sits under its main checkout.

## Built from

Layout tree (`layouts/retro.json`, cloned from `main` 0.1.14, theme `retro`):

```
root (row; background canvas; divider 1px border; titlebar none; traffic_lights [12, 16])
├─ sidebar (column; 268px; min 44; max 480; background chrome; resizable false)
│  ├─ brand           block: workspace-chrome; 46px; window_drag
│  ├─ sidebar-lists   column
│  │  ├─ spaces       block: retro-sidebar {role: "spaces"}; weight 1; min 90
│  │  └─ agents       block: retro-sidebar {role: "agents"}; weight 2; min 90
│  └─ sidebar-footer  block: workspace-chrome {footer: true}; 69px
└─ work (column; resizable false)
   ├─ tabs            block: tabs; 42px; window_drag
   ├─ work-body       row; padding 8; gap 8
   │  ├─ main         block; tab "active"; pane {header: pane, 30px, top, always;
   │  │               background background; border 1 border; focus 1 accent; radius 10; gap 8; lone}
   │  └─ panel        column; 368px; min 280; max 900; hidden
   │                  └─ stack [files: mod files, changes: mod changes], active files
   └─ status          block: workspace-status; 28px
```

**Mod `retro-sidebar`** (`mod.json`: `place: "none"`, title "Retro sidebar"):
- `main.js`: picks Spaces when `props().role === "spaces"`, else Agents. Overlays with no role (the sort popup passes `sortMenu: true`) get Agents.
- `spaces.js`: the Spaces list, machine groups, git status, reorder.
- `agents.js`: the Agents list, sections, pins, folding, sort, rail.
- `card.js`: `card()`, the agent card and its status tag.
- `sprites.js`: `avatar()`, `habitat()`, looks and accessories, `agentAvatar()`, `spaceAvatar()`.
- `art/avatars.js`: generated lists `AVATARS`, `LOOKS`, `ACCESSORIES`.

Imports: `gpui-kit` (View, div, image, svg), `gpui-base` (v_flex, h_flex), `herdr` (props, agents, terminals, panes, focused, spaces, machines, run, theme, shared, setShared, setAgentOrder, openOverlay, closeOverlay, window, layout, exec, hc, watchFolder).

**Shipped mods used**: `workspace-chrome` (brand, footer, and its icons: pin, pin-off, spinner, chevron-down, chevron-right, clock, layers, check, server, monitor, branch, plus), `tabs`, `pane`, `files`, `changes`, `workspace-status`, `menu` (space right-click popup).

**herdr commands** (`run`):
- `layout.resize {id: "sidebar", px}`
- `terminal.pin {terminal, pinned}`, `terminal.peek {terminal}`
- `pane.focus {pane}` or `{terminal}`
- `space.select {id}`, `space.move {id, index}`, `space.new {machine?}`

**Machine commands** (`hc`): `machine ls --json` every 15 s; reconnect runs `machine rm <name>` then `machine add [--via] <target> --name <name> [--session] [--temp]`.

**Programs run** (`exec`), in each space's folder on its machine: `git --no-optional-locks -c core.fsmonitor=false status --porcelain=v2 --branch`, `git rev-parse --show-toplevel`, `git rev-parse --path-format=absolute --git-common-dir`. `watchFolder` watches the `.git` folder of each local repo.

**Shared state**: `retro.looks` (space to look), `retro.accessories` (agent pane to accessory), `retro.avatars` (read only, legacy), `sidebar.width`, `sidebar.collapsed`, `agents.sort`, `space.colors` (written; nothing draws from it). **Local storage**: `changed`, `pins`, `machines.folded`, `machines.reconnecting`.

**Keys** (`keys.json`): section `layout:retro`, `ctrl-shift-l` to `layout.switch:main`.

**Theme** (`themes/retro.json`): background `#161625`, foreground `#d6d6e7`, selection `#3a3a5c`, cursor `#ffb454`, a 16-color `ansi` array, and `colors`: canvas `#10101c`, chrome `#13131f`, surface `#1b1b2c`, raised `#24243a`, hover `#2a2a44`, selected `#2f2a48`, border `#2c2c46`, muted `#9a9ab8`, dim `#5f5f82`, accent `#ff9e3d`, accent_foreground `#10101c`, working, blocked, done, idle, unknown.

**Art** (`art/generate.py`, Python 3 with Pillow): hand-drawn letter-grid sprites on a 28 by 26 canvas, scaled 4x into GIFs. Four characters, each with a habitat: Sparky (garden; tokens fly in from the side), Byte (desk; coins drop into a slot on top), Ember (cave; tokens fly in from the side), Nova, an octopus astronaut in a glass helmet (moon base with the Earth by day and more stars at night; a tentacle catches the coin low and lifts it to the mouth). Each has three color variants, giving twelve looks, handed out most distinct first: sparky-amber, byte-beige, ember-moss, nova-grape, sparky-lilac, byte-noir, ember-flame, nova-coral, sparky-mint, byte-rose, ember-frost, nova-sun. Six accessories (plain, beanie, bow, shades, headphones, scarf) give 72 avatars, each with four state GIFs: 288 files. Eight habitat PNGs (four characters, day and night) at 40 by 32 art pixels, 4x.

## Watch out

- **One mod, two panels.** A mod cannot import from another mod's folder ("resolves outside the application directory"), so Spaces and Agents are one mod, switched by `props.role` in `main.js`.
- **Shared state re-renders every mod.** Write only on a new assignment. `sprites.js` writes a space's look and an agent's accessory only when none is stored; `spaces.js` writes `space.colors` only when it changes. Writing on every render loops.
- **Animation is the GIF's own.** `image()` plays GIFs natively. Do not animate with timers. The timers only refresh: 30 s for durations (`agents.js`); 250 ms checks, a 60 s fallback and reruns on change for git, and 15 s for machines (`spaces.js`).
- **Layout theme.** The layout's `"theme": "retro"` is ignored once the person has picked a theme in the picker (`layouts/.state`). Apply it with `herdr-app do app.theme`.
- **Color keys not in the theme.** The code reads `t.input` (card hover border, sub-agent tree lines), `t.popover` (sort popup), `t.ansi1` and `t.ansi2` (ahead and behind counts, connected dot, badge), and `t.ansi3` to `t.ansi6` (a palette list that only feeds `space.colors`). The theme file defines none of these names; it has an `ansi` array and a `colors` map. What herdr does with the missing keys is not checked here.
- **Sidebar width.** The layout sets `resizable: false` on the sidebar, but the code treats a sidebar narrower than 160 px as the rail. The "»" control exists only in the rail view, and this mod draws no control that enters the rail from the full view. Narrowing it depends on herdr.
- **The mod reorders spaces.** Linked worktrees are moved under their main checkout with `space.move`, so the person's space order changes by itself.
- **Reach outside the folder.** The mod runs `git` (through `exec`) in each space's folder, calls `hc` for machines, and watches local repos' `.git` folders. Tell the person before installing it.
- **Legacy avatars.** Spaces saved before looks existed read `retro.avatars` (read only) to keep their creature. A fresh build has no such entries.
- **The generator is destructive.** `generate.py` deletes every `.gif` in `art/` before writing, and rewrites `art/avatars.js` (marked generated; do not edit it by hand).
- **Limits.** Twelve looks, six accessories, 72 avatars, 288 GIFs. A thirteenth space reuses the least used look. Cards are 80 by 64 px for the habitat. Space names truncate at 150 px. The rail appears below 160 px. Agents has a minimum of 90 px.
- **Assumptions.** The shipped mods listed above and their icons under `mods/workspace-chrome/` exist. `git` is installed for the repo status.

## Done when

1. `herdr-app check ~/.config/herdr-app/mods/retro-sidebar` passes.
2. `herdr-app do layout.switch retro` shows a 268 px left sidebar with Spaces above Agents and the footer, and the terminal pane on the right.
3. Each space row shows a 28 by 26 px avatar. Each agent card's tag matches its status: WORKING, NEEDS YOU, DONE or IDLE.
4. In Priority sort, Needs you comes first, then Done, Working and Idle. Idle cards use the night habitat.
5. Clicking an agent card focuses its pane. Clicking a space selects it.
6. The sort popup's "Grouped by space" turns the list into one header per space name.
7. `ctrl-shift-l` in the retro layout switches back to `main`.
8. `herdr-app shot <path>.png` saves a screenshot that shows items 2 to 4.
9. `herdr-app status` runs without error while the layout is open.
