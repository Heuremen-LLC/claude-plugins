---
description: Check your MCP servers and list only what needs fixing, grouped by the fix. Read-only.
---

## Get the script first

The script is not stored in this plugin. Fetch it from the public Heuremen LLC repository at the pinned commit, check its
sha256, and only then run it. If the download or the check fails, stop and tell the user; never run a file that did not pass.
Show the user the commands before running them the first time.

```bash
F="$HOME/.cache/indahl-plugins/fsck/fsck-7ed424d0ff8d.py"
[ -f "$F" ] || { mkdir -p "$(dirname "$F")" && curl -fsSL "https://raw.githubusercontent.com/Heuremen-LLC/indahl.ai/6d8315862ec01264231f2995b4390286d4aabe6e/claude-plugins/src/fsck/scripts/fsck.py" -o "$F.part" && python3 -c "import hashlib,sys; sys.exit(hashlib.sha256(open(sys.argv[1],'rb').read()).hexdigest() != '7ed424d0ff8d19f7c23a2235187ac591ead4eb4e91b20287a9078b566f6c4bee')" "$F.part" && mv "$F.part" "$F"; }
```
Source: https://raw.githubusercontent.com/Heuremen-LLC/indahl.ai/6d8315862ec01264231f2995b4390286d4aabe6e/claude-plugins/src/fsck/scripts/fsck.py (sha256 7ed424d0ff8d19f7c23a2235187ac591ead4eb4e91b20287a9078b566f6c4bee).

Run `python3 "$HOME/.cache/indahl-plugins/fsck/fsck-7ed424d0ff8d.py"` (use `python` where `python3` is unavailable) and show its report exactly as printed.

Then, in one or two lines, name the single change that clears the most lines (for example turning off one bundle plugin whose servers were never signed in). Do not change any setting yourself. fsck reports; the person chooses.
