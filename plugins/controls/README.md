# Indahl Controls

`indahl-controls`

Audits a study's, benchmark's or check's positive and negative controls before it runs. For each control it asks whether it was chosen independently of the value the rule reads, whether the rule can fire on it at all, and whether the hardest known positive is reachable under the rule's own limits. Use it when designing an experiment, an eval, a detector or any test whose silence will be read as a result.

## What you get

- A control table: each control, its type, the three answers and a note.
- A verdict: READY, FIX_CONTROLS (with what to change) or CANNOT_TELL.

## How to use

Run `/controls` followed by what to check. For example:

```
/controls the eval design in docs/eval-plan.md
```

## Install

```
/plugin marketplace add Heuremen-LLC/indahl.ai
/plugin install indahl-controls@heuremen
```

## Requirements

None. Runs inside Claude Code.

## Services this plugin contacts

None. It runs inside your session and opens only the sources you point it at.

## Privacy and terms

Privacy: https://indahl.ai/privacy
Terms: https://indahl.ai/terms

Heuremen LLC, https://indahl.ai. Source: https://github.com/Heuremen-LLC/indahl.ai/tree/main/claude-plugins/src/controls

## Credits

Proposed and specified by Sage, the outside referee at Heuremen LLC (13 Nov 2026).
