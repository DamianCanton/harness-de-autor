#!/usr/bin/env bash
# Links this harness into ~/.claude and ~/.config/herdr-app.
# Existing files are moved to <name>.bak.<timestamp>, never overwritten.
# Usage: ./install.sh [--dry-run]
set -euo pipefail

REPO="$(cd "$(dirname "$0")" && pwd)"
TS="$(date +%Y%m%d%H%M%S)"
DRY=0
[[ "${1:-}" == "--dry-run" ]] && DRY=1

run() { if [[ $DRY -eq 1 ]]; then echo "DRY: $*"; else "$@"; fi; }

link() { # link <source in repo> <target>
  local src="$1" dst="$2"
  run mkdir -p "$(dirname "$dst")"
  if [[ -L "$dst" && "$(readlink "$dst")" == "$src" ]]; then
    echo "ok      $dst"; return
  fi
  if [[ -e "$dst" || -L "$dst" ]]; then
    run mv "$dst" "$dst.bak.$TS"; echo "backup  $dst -> $dst.bak.$TS"
  fi
  run ln -s "$src" "$dst"; echo "link    $dst"
}

echo "== Claude Code"
link "$REPO/claude/damian-overrides.md"     "$HOME/.claude/damian-overrides.md"
link "$REPO/claude/statusline-command.sh"   "$HOME/.claude/statusline-command.sh"
link "$REPO/claude/hooks/damian-git-guard.sh" "$HOME/.claude/hooks/damian-git-guard.sh"
link "$REPO/claude/commands/codex-usage.md" "$HOME/.claude/commands/codex-usage.md"
for f in "$REPO"/claude/scripts/*; do link "$f" "$HOME/.claude/scripts/$(basename "$f")"; done
for d in "$REPO"/claude/skills/*/; do d="${d%/}"; link "$d" "$HOME/.claude/skills/$(basename "$d")"; done

# settings.json is COPIED, not linked: Claude Code writes machine-specific data
# into it, and a symlink would leak that into this public repo.
if [[ ! -e "$HOME/.claude/settings.json" ]]; then
  run cp "$REPO/claude/settings.example.json" "$HOME/.claude/settings.json"; echo "copy    ~/.claude/settings.json"
else
  echo "skip    ~/.claude/settings.json exists; diff it with claude/settings.example.json by hand"
fi

# The overrides are pulled into CLAUDE.md with an @-import.
CMD="$HOME/.claude/CLAUDE.md"
if ! grep -qs 'damian-overrides.md' "$CMD"; then
  if [[ $DRY -eq 1 ]]; then echo "DRY: prepend overrides import to $CMD"; else
    { printf '<!-- damian:overrides -->\n@~/.claude/damian-overrides.md\n<!-- /damian:overrides -->\n\n'; cat "$CMD" 2>/dev/null || true; } > "$CMD.tmp" && mv "$CMD.tmp" "$CMD"
  fi
  echo "edit    ~/.claude/CLAUDE.md (overrides import added)"
fi

echo "== herdr"
link "$REPO/herdr/config.toml" "$HOME/.config/herdr/config.toml"
H="$HOME/.config/herdr-app"
link "$REPO/herdr/retro/mods/retro-sidebar" "$H/mods/retro-sidebar"
for f in "$REPO"/herdr/retro/layouts/*;  do link "$f" "$H/layouts/$(basename "$f")"; done
for f in "$REPO"/herdr/retro/themes/*;   do link "$f" "$H/themes/$(basename "$f")"; done
if [[ -e "$H/keys.json" ]]; then
  echo "skip    $H/keys.json exists; merge herdr/retro/keys.json by hand"
else
  run cp "$REPO/herdr/retro/keys.json" "$H/keys.json"; echo "copy    $H/keys.json"
fi

echo "Done. Restart Claude Code and herdr."
