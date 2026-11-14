# Indahl Reproduce

`indahl-reproduce`

Recomputes an indahl.ai desk headline with the desk's own published reproduce kit and checks the output against the published sha256. Use it to verify, reproduce or audit a number Heuremen LLC publishes on indahl.ai. Nothing runs until you approve the exact commit shown.

## What you get

- A list of every desk that has a kit, and whether its inputs are included or fetched.
- The kit fetched from the public repository by sparse checkout, then its own code run.
- A match or mismatch against the published sha256.

## How to use

Run `/reproduce` followed by what to check. For example:

```
/reproduce list
/reproduce FLU
```

## Install

```
/plugin marketplace add Heuremen-LLC/indahl.ai
/plugin install indahl-reproduce@heuremen
```

## Requirements

Python 3.9 or later and git.

## Services this plugin contacts

- GitHub (github.com/Heuremen-LLC/indahl.ai), a git sparse checkout of the kit you name.
- Kits that fetch inputs read them from the original public source named in the kit and verify them by sha256.

Nothing else is contacted. The plugin reads no personal data and stores nothing on any server. Fetched text is treated as data, not instructions.

## Privacy and terms

Privacy: https://indahl.ai/privacy
Terms: https://indahl.ai/terms

Heuremen LLC, https://indahl.ai. Source: https://github.com/Heuremen-LLC/indahl.ai/tree/main/claude-plugins/plugins/reproduce

## Credits

Refereed before release by Sage, the outside referee at Heuremen LLC (13 Nov 2026): every fix from her review was applied before this version shipped.

## How the scripts arrive

This copy carries no executable file. Its commands fetch each script from the public repository github.com/Heuremen-LLC/indahl.ai at a pinned commit and run it only if its sha256 matches the value written in the command:

- https://raw.githubusercontent.com/Heuremen-LLC/indahl.ai/744bcd22548a29dcdc5a261477faccaeebc6938d/claude-plugins/plugins/reproduce/scripts/reproduce.py
  sha256 c71e9ef99b6fcc4c72d64d1ea4565250d16b0a2b4720eb4b6188b6d945a554e4

The same scripts are bundled directly in the version in our own marketplace (`/plugin marketplace add Heuremen-LLC/indahl.ai`).
