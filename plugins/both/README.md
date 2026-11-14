# Indahl Both

`indahl-both`

Holds two competing explanations open instead of settling on one too early. It keeps a separate evidence ledger for each reading and always adds the other two possibilities, so the answer is never forced into one of the first two. Use it when two patterns both fit the evidence, or when a result could come from the thing studied or from the instrument measuring it.

## What you get

- Two readings, A and B, written as plain claims that predict different things.
- Two evidence ledgers, one row per piece of evidence with its bearing on A, B, BOTH and NEITHER.
- The test that would separate the readings, or a statement that none exists yet.
- One state: A, B, BOTH, NEITHER or OPEN, with the row that moved it.

## How to use

Run `/both` followed by what to check. For example:

```
/both Did latency fall because of the new cache, or because the test ran at quieter hours?
```

## Install

```
/plugin marketplace add Heuremen-LLC/indahl.ai
/plugin install indahl-both@heuremen
```

## Requirements

None. Runs inside Claude Code.

## Services this plugin contacts

None. It runs inside your session.

## Privacy and terms

Privacy: https://indahl.ai/privacy
Terms: https://indahl.ai/terms

Heuremen LLC, https://indahl.ai. Source: https://github.com/Heuremen-LLC/indahl.ai/tree/main/claude-plugins/src/both
