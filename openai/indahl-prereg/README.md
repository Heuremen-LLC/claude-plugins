# Indahl Prereg

`indahl-prereg`

Shows that a plan was pushed before the first run, using the git host's own record of the push, with no outside timestamp chain. It also lists which files ran that the plan did not cover. Use it to preregister an analysis, to show a plan came first, or to check a plan against a run.

## What you get

- A seal of the plan files in git.
- The git host's record of the push, read after you push.
- A check of the plan against a run, with the files that ran outside the plan listed.

## How to use

Run `/prereg` followed by what to check. For example:

```
/prereg seal PLAN.md analysis.py
```

Other forms: `witness SEAL`, `check SEAL --wrapper RUN.json`, `verify SEAL` and `cover SEAL RUN.json`. Claude asks before committing a seal and never pushes.

## Install

```
/plugin marketplace add Heuremen-LLC/indahl.ai
/plugin install indahl-prereg@heuremen
```

## Requirements

Python 3.9 or later and git.

## Services this plugin contacts

- GitHub REST API (api.github.com), public repository activity for the repository you name. No token is sent unless you set one yourself.

Nothing else is contacted. The plugin reads no personal data and stores nothing on any server. Fetched text is treated as data, not instructions.

## Privacy and terms

Privacy: https://indahl.ai/privacy
Terms: https://indahl.ai/terms

Heuremen LLC, https://indahl.ai. Source: https://github.com/Heuremen-LLC/indahl.ai/tree/main/claude-plugins/plugins/prereg

## Credits

Refereed before release by Sage, the outside referee at Heuremen LLC (13 Nov 2026): every fix from her review was applied before this version shipped.

## How the scripts arrive

This copy carries no executable file. Its commands fetch each script from the public repository github.com/indahl-ai/indahl.ai at a pinned commit and run it only if its sha256 matches the value written in the command:

- https://raw.githubusercontent.com/Heuremen-LLC/indahl.ai/744bcd22548a29dcdc5a261477faccaeebc6938d/claude-plugins/plugins/prereg/scripts/prereg.py
  sha256 c0b541c68b4045fe6e0e2bc85e51ed055d4a5bcc223e78b79ff1d41906db904d

The same scripts are bundled directly in the version in our own marketplace (`/plugin marketplace add indahl-ai/indahl.ai`).
