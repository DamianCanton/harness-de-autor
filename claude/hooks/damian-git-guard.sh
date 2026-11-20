#!/usr/bin/env bash
# damian-git-guard — PreToolUse(Bash) hook. User-owned, not managed by gentle-ai.
# exit 2 = block (stderr goes back to Claude as feedback). Any other exit = allow.
# Fail-open by design: if jq is missing or JSON is odd, the command is allowed.

cmd=$(jq -r '.tool_input.command // ""' 2>/dev/null) || exit 0
[[ "$cmd" == *git* ]] || exit 0

# 1) Force-adding ignored files is how the 128-file accident starts.
if [[ "$cmd" == *"git add"* ]] && [[ "$cmd" == *" -f"* || "$cmd" == *"--force"* ]]; then
  echo "Blocked by damian-git-guard: 'git add --force' stages gitignored files. Ask Damián first." >&2
  exit 2
fi

if [[ "$cmd" == *"git"*"commit"* ]]; then
  # 2) The hook sees the index BEFORE the command runs, so add+commit in one call would bypass check 3.
  if [[ "$cmd" == *"git add"* || "$cmd" == *"commit -a"* || "$cmd" == *"commit -am"* || "$cmd" == *"commit --all"* ]]; then
    echo "Blocked by damian-git-guard: run 'git add' and 'git commit' as separate commands so the staged set can be inspected." >&2
    exit 2
  fi
  # 3) Precise check: any staged path that .gitignore excludes? (--no-index: ignore the index, judge by rules only)
  ignored=$(git diff --cached --name-only 2>/dev/null | git check-ignore --no-index --stdin 2>/dev/null)
  if [[ -n "$ignored" ]]; then
    echo "Blocked by damian-git-guard: gitignored files are staged:" >&2
    echo "$ignored" | head -20 >&2
    echo "Unstage them (git restore --staged <path>) or ask Damián." >&2
    exit 2
  fi
fi
exit 0
