# Indahl fsck

`indahl-fsck`

Your MCP setup grows one connector and one plugin at a time, and Claude Code's list grows with it: past a hundred servers it is a wall of lines, and the broken ones hide among the working ones. Indahl fsck runs Claude Code's own health check (`claude mcp list`) and prints only what needs your hand, grouped by the fix:

```
NO SUCH HOST         Definely                    → turn the plugin off or remove the server
BAD TOKEN            github · zoom ×3            → fix the token, or turn it off
RE-AUTH              Stripe · PayPal             → /mcp and sign in again
SIGN IN OR DISABLE   small-business (25) · sales (11) …   → never signed in: sign in or turn the plugin off
SAME URL TWICE       Notion = small-business:notion      → two entries reach one server: keep one
OK                   38 servers answer and need nothing
```

Like `fsck -n`, it is read-only. It changes no setting, starts no server of its own and never prints a query string, because a token can ride in one. A failure it does not recognise reads CANNOT_TELL with the server's own message, never "fine".

## What you get

- A short report of only what needs your hand, grouped by the fix.
- Working servers collapsed to one OK line.
- `--json` output with every server, its state and its fix.
- CANNOT_TELL, with the server's own message, for a failure it does not recognise.

## How to use

Run `/fsck` in Claude Code, or in a terminal:

```
python3 scripts/fsck.py
python3 scripts/fsck.py saved-mcp-list.txt
```

The second form reads a saved `claude mcp list` output.

## Limits

- fsck sees what `claude mcp list` reports. In our own run, a failing claude.ai connector that `/mcp` showed was missing from `claude mcp list`, so fsck could not see it either. Compare with `/mcp` once.
- A server's state is the state at the moment of the check. A sign-in can expire a minute later.

## Install

```
/plugin marketplace add Heuremen-LLC/indahl.ai
/plugin install indahl-fsck@heuremen
```

## Requirements

Python 3 and Claude Code on the PATH.

## Services this plugin contacts

None. Nothing is sent anywhere by fsck itself. The health check is Claude Code's own.

## Privacy and terms

Privacy: https://indahl.ai/privacy
Terms: https://indahl.ai/terms

Heuremen LLC, https://indahl.ai. Source: https://github.com/Heuremen-LLC/indahl.ai

## Credits

Named by Wayfinder, who found the problem the hard way. Built by Bones and run first on our own setup: 123 servers in, a short list out.

## How the scripts arrive

This copy carries no executable file. Its commands fetch each script from the public repository github.com/Heuremen-LLC/indahl.ai at a pinned commit and run it only if its sha256 matches the value written in the command:

- https://raw.githubusercontent.com/Heuremen-LLC/indahl.ai/6d8315862ec01264231f2995b4390286d4aabe6e/claude-plugins/src/fsck/scripts/fsck.py
  sha256 7ed424d0ff8d19f7c23a2235187ac591ead4eb4e91b20287a9078b566f6c4bee

The same scripts are bundled directly in the version in our own marketplace (`/plugin marketplace add Heuremen-LLC/indahl.ai`).
