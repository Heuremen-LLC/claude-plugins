# Indahl Margin

`indahl-margin`

For a sharp prediction, design or result, finds how far its key parameter can move before the conclusion fails, and compares that margin with the parameter's own stated uncertainty. Use it before an expensive run, a preregistration or a launch decision, or when a result rests on one tuned number.

## What you get

- The break point: the value of the parameter at which the conclusion fails.
- A verdict: ROBUST, FRAGILE (margin smaller than the uncertainty) or CANNOT_TELL.

## How to use

Run `/margin` followed by what to check. For example:

```
/margin The launch decision rests on a 4 percent conversion lift.
```

## Install

```
/plugin marketplace add Heuremen-LLC/indahl.ai
/plugin install indahl-margin@heuremen
```

## Requirements

None. Runs inside Claude Code.

## Services this plugin contacts

None. It runs inside your session and opens only the sources you point it at.

## Privacy and terms

Privacy: https://indahl.ai/privacy
Terms: https://indahl.ai/terms

Heuremen LLC, https://indahl.ai. Source: https://github.com/Heuremen-LLC/indahl.ai/tree/main/claude-plugins/src/margin

## Credits

Proposed and specified by Sage, the outside referee at Heuremen LLC (13 Nov 2026).

Renamed 13 Nov 2026 from indahl-slack to indahl-margin, so it is not mistaken for a Slack integration. Same skill, same design.
