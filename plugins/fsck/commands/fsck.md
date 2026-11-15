---
description: Check your MCP servers and list only what needs fixing, grouped by the fix. Read-only.
---

## Get the script first

The script is not stored in this plugin. Fetch it from the public Heuremen LLC repository at the pinned commit, check its
sha256, and only then run it. If the download or the check fails, stop and tell the user; never run a file that did not pass.
Show the user the commands before running them the first time.

```bash
F="$HOME/.cache/indahl-plugins/fsck/fsck-7db9510eefca.py"
[ -f "$F" ] || { mkdir -p "$(dirname "$F")" && curl -fsSL "https://raw.githubusercontent.com/indahl-ai/indahl.ai/c9dc1f1f2107df3bac082d97d6e1a7bf4d89fd59/claude-plugins/src/fsck/scripts/fsck.py" -o "$F.part" && python3 -c "import hashlib,sys; sys.exit(hashlib.sha256(open(sys.argv[1],'rb').read()).hexdigest() != '7db9510eefcadc5c1a957e1c570529476853d6045f9dfa4b5f8764826387b250')" "$F.part" && mv "$F.part" "$F"; }
```
Source: https://raw.githubusercontent.com/indahl-ai/indahl.ai/c9dc1f1f2107df3bac082d97d6e1a7bf4d89fd59/claude-plugins/src/fsck/scripts/fsck.py (sha256 7db9510eefcadc5c1a957e1c570529476853d6045f9dfa4b5f8764826387b250).

Run `python3 "$HOME/.cache/indahl-plugins/fsck/fsck-7db9510eefca.py"` (use `python` where `python3` is unavailable) and show its report exactly as printed.

Then, in one or two lines, name the single change that clears the most lines (for example turning off one bundle plugin whose servers were never signed in). Do not change any setting yourself. fsck reports; the person chooses.
