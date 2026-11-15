# Indahl fsck

`indahl-fsck`

Your MCP setup grows one connector and one plugin at a time, and Claude Code's list grows with it: past a hundred servers it is a wall of lines, and the broken ones hide among the working ones. Indahl fsck runs Claude Code's own health check (`claude mcp list`) and prints only what needs your hand, grouped by the fix. It also catches the claude.ai connectors that list leaves out:

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

- `claude mcp list` leaves out a claude.ai connector that is failing ([anthropics/claude-code#109864](https://github.com/anthropics/claude-code/issues/109864)). fsck therefore also reads the claude.ai connectors Claude Code has connected before (`claudeAiMcpEverConnected` in `~/.claude.json`) and reports any that the list leaves out as NOT LISTED. That covers a failing connector and one you removed on claude.ai alike; `/mcp` tells them apart. If `~/.claude.json` can't be read, fsck says so instead of reading clean.
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
