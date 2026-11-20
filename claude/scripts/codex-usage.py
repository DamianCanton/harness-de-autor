#!/usr/bin/env python3
"""Print Codex usage (5h and weekly windows) from the newest rate_limits event in ~/.codex/sessions."""
import glob
import json
import os
import re
import sys
import time
from datetime import datetime, timezone

SESSIONS = os.path.expanduser("~/.codex/sessions")
CONFIG = os.path.expanduser("~/.claude/codex-review-home/config.toml")
MAX_FILES = 25


def newest_rate_limits():
    files = sorted(glob.glob(f"{SESSIONS}/*/*/*/*.jsonl"), key=os.path.getmtime, reverse=True)
    for path in files[:MAX_FILES]:
        found = None
        with open(path, encoding="utf-8", errors="replace") as fh:
            for line in fh:
                if '"rate_limits"' not in line:
                    continue
                try:
                    payload = json.loads(line).get("payload", {})
                except json.JSONDecodeError:
                    continue
                if payload.get("rate_limits"):
                    found = (json.loads(line).get("timestamp"), payload["rate_limits"])
        if found:
            return found
    return None


def configured_model():
    try:
        with open(CONFIG, encoding="utf-8") as fh:
            text = fh.read()
    except OSError:
        return "unknown"
    model = re.search(r'^model\s*=\s*"([^"]+)"', text, re.M)
    effort = re.search(r'^model_reasoning_effort\s*=\s*"([^"]+)"', text, re.M)
    return f"{model.group(1) if model else 'unknown'} · effort {effort.group(1) if effort else 'default'}"


def window(label, data, now):
    if not data:
        return f"{label}: n/a"
    reset = data["resets_at"]
    if reset <= now:
        return f"{label}: 0% (window already reset; last reading is stale)"
    left = int(reset - now)
    hours, rem = divmod(left, 3600)
    reset_local = datetime.fromtimestamp(reset).strftime("%a %H:%M")
    return f"{label}: {data['used_percent']:.0f}% used · resets in {hours}h{rem // 60:02d}m ({reset_local})"


def main():
    result = newest_rate_limits()
    if not result:
        print("No Codex rate_limits found. Run a Codex task first (e.g. /codex:review).")
        return 1
    stamp, limits = result
    now = time.time()
    seen = datetime.fromisoformat(stamp.replace("Z", "+00:00"))
    age_min = int((datetime.now(timezone.utc) - seen).total_seconds() // 60)
    print(f"Codex review : {configured_model()} (plan: {limits.get('plan_type')})")
    print(window("5h window ", limits.get("primary"), now))
    print(window("Weekly    ", limits.get("secondary"), now))
    print(f"Last reading: {age_min} min ago (only updates after a Codex turn)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
