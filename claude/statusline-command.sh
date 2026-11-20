#!/bin/sh
input=$(cat)
dir=$(echo "$input" | jq -r '.workspace.current_dir // .cwd // ""')
model=$(echo "$input" | jq -r '.model.display_name // ""')
used=$(echo "$input" | jq -r '.context_window.used_percentage // empty')
short=$(basename "$dir")
branch=""
if [ -n "$dir" ] && git -C "$dir" rev-parse --git-dir >/dev/null 2>&1; then
  branch=$(GIT_OPTIONAL_LOCKS=0 git -C "$dir" symbolic-ref --short HEAD 2>/dev/null || GIT_OPTIONAL_LOCKS=0 git -C "$dir" rev-parse --short HEAD 2>/dev/null)
fi
dirty=""
ab=""
if [ -n "$branch" ]; then
  dirty=$(GIT_OPTIONAL_LOCKS=0 git -C "$dir" status --porcelain 2>/dev/null | wc -l | tr -d ' ')
  [ "$dirty" = "0" ] && dirty=""
  counts=$(GIT_OPTIONAL_LOCKS=0 git -C "$dir" rev-list --left-right --count '@{u}...HEAD' 2>/dev/null)
  if [ -n "$counts" ]; then
    set -- $counts
    [ "$2" -gt 0 ] 2>/dev/null && ab="↑$2"
    [ "$1" -gt 0 ] 2>/dev/null && ab="$ab↓$1"
  fi
fi
printf '\033[34m%s\033[0m' "$short"
[ -n "$branch" ] && printf ' \033[32m\xee\x82\xa0 %s\033[0m' "$branch"
[ -n "$dirty" ] && printf ' \033[33m●%s\033[0m' "$dirty"
[ -n "$ab" ] && printf ' \033[36m%s\033[0m' "$ab"
[ -n "$model" ] && printf ' \033[35m%s\033[0m' "$model"
tok=$(echo "$input" | jq -r '.context_window.total_input_tokens // empty')
size=$(echo "$input" | jq -r '.context_window.context_window_size // empty')
five=$(echo "$input" | jq -r '.rate_limits.five_hour.used_percentage // empty')
week=$(echo "$input" | jq -r '.rate_limits.seven_day.used_percentage // empty')
fmt() { awk -v n="$1" 'BEGIN{ if (n>=1000000) printf "%.1fM", n/1000000; else if (n>=1000) { s=sprintf("%.1f", n/1000); sub(/\.0$/,"",s); printf "%sk", s } else printf "%d", n }'; }
bar() { awk -v p="$1" -v w=10 'BEGIN{ if (p>100) p=100; if (p<0) p=0; f=int(p*w/100+0.5); c=(p>=85)?31:(p>=60)?33:32; printf "\033[%dm", c; for(i=0;i<f;i++) printf "\342\226\210"; printf "\033[90m"; for(i=f;i<w;i++) printf "\342\226\221"; printf "\033[0m" }'; }
col() { awk -v p="$1" 'BEGIN{ printf "%d", (p>=85)?31:(p>=60)?33:32 }'; }
seg() { printf ' \033[90m%s\033[0m %s \033[%sm%.0f%%\033[0m' "$1" "$(bar "$2")" "$(col "$2")" "$2"; }
if [ -n "$tok" ] && [ -n "$size" ]; then
  seg ctx "${used:-0}"
  printf ' \033[90m%s/%s\033[0m' "$(fmt "$tok")" "$(fmt "$size")"
elif [ -n "$used" ]; then
  seg ctx "$used"
fi
[ -n "$five" ] && seg 5h "$five"
[ -n "$week" ] && seg 7d "$week"
printf '\n'
