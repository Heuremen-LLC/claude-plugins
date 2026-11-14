# Indahl Correct

`indahl-correct`

Records a correction beside the original, never over it. It captures what was wrong, who caught it, when, the evidence, the corrected text and whether every place that cited the original was reached. Use it when an error is found in anything already published or sent, such as a paper, a page, a report, a dataset or a message.

## What you get

- An appended entry in `CORRECTIONS.md`: date, item, original, corrected text, evidence, who caught it and scope.
- A visible note at the corrected spot, with the original kept retrievable.
- A downstream list of every place the original reached, each marked UPDATED, NOTIFIED, CANNOT_REACH or NOT_NEEDED.

## How to use

Run `/correct` followed by what to check. For example:

```
/correct The Q3 report page says 14 percent. The source table says 11 percent.
```

## Install

```
/plugin marketplace add Heuremen-LLC/indahl.ai
/plugin install indahl-correct@heuremen
```

## Requirements

None. Runs inside Claude Code.

## Services this plugin contacts

None. It runs inside your session and opens only the sources you point it at.

## Privacy and terms

Privacy: https://indahl.ai/privacy
Terms: https://indahl.ai/terms

Heuremen LLC, https://indahl.ai. Source: https://github.com/Heuremen-LLC/indahl.ai/tree/main/claude-plugins/src/correct

## Credits

Proposed and specified by Sage, the outside referee at Heuremen LLC (13 Nov 2026).
