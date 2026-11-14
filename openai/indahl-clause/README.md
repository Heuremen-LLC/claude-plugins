# Indahl Clause

`indahl-clause`

Checks the sentences that report a result for wording that claims more than the comparison showed. It catches an item that is wrong on its own described as if the paired comparison moved, a CONSISTENT result reported as "the same", a non-significant difference reported as "no difference", and a cause named where only an association was measured. Use it on results sections, eval write-ups, clinical and product summaries and press releases.

## What you get

- Every result sentence pulled out and numbered.
- KEEP or REWORD for each sentence, with the reason.
- For each REWORD, the exact replacement sentence, naming the comparison, the interval and the scope.

## How to use

Run `/clause` followed by what to check. For example:

```
/clause the results section of draft-v3.md
```

## Install

```
/plugin marketplace add Heuremen-LLC/indahl.ai
/plugin install indahl-clause@heuremen
```

## Requirements

None. Runs inside Claude Code.

## Services this plugin contacts

None. It runs inside your session and opens only the sources you point it at.

## Privacy and terms

Privacy: https://indahl.ai/privacy
Terms: https://indahl.ai/terms

Heuremen LLC, https://indahl.ai. Source: https://github.com/Heuremen-LLC/indahl.ai/tree/main/claude-plugins/src/clause

## Credits

Proposed and specified by Sage, the outside referee at Heuremen LLC (13 Nov 2026).
