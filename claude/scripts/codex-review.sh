#!/bin/sh
# Run the Codex plugin's native review against the current repo, whatever plugin version is installed.
# Model and effort come from an isolated CODEX_HOME so ~/.codex/config.toml stays untouched.
# Usage: codex-review.sh [--base <ref>] [--scope auto|working-tree|branch]
set -eu
plugin_dir=$(ls -d "$HOME"/.claude/plugins/cache/openai-codex/codex/*/ 2>/dev/null | sort -V | tail -1)
if [ -z "$plugin_dir" ]; then
  echo "codex plugin not installed" >&2
  exit 2
fi
export CODEX_HOME="$HOME/.claude/codex-review-home"
exec node "${plugin_dir}scripts/codex-companion.mjs" review "$@"
