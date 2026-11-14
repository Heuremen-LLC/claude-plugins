# Indahl Number Check

`indahl-number-check`

Checks every number in a report, memo, deck or dashboard against its source. Each figure is traced and marked HELD, MOVED, NO_SOURCE or CANNOT_TELL, with the source line beside it. Use it after any research, finance, analytics or business-report skill, or before sending anything with numbers in it.

## What you get

- A row for every figure in the document.
- One mark per figure: HELD, MOVED, NO_SOURCE or CANNOT_TELL.
- The source line beside each figure.

## How to use

Run `/number-check` followed by what to check. For example:

```
/number-check Q3-summary.md against the spreadsheets in data/
```

## Install

```
/plugin marketplace add Heuremen-LLC/indahl.ai
/plugin install indahl-number-check@heuremen
```

## Requirements

None. Runs inside Claude Code.

## Services this plugin contacts

None. It runs inside your session and opens only the sources you point it at.

## Privacy and terms

Privacy: https://indahl.ai/privacy
Terms: https://indahl.ai/terms

Heuremen LLC, https://indahl.ai. Source: https://github.com/Heuremen-LLC/indahl.ai/tree/main/claude-plugins/src/number-check
