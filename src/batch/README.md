# Indahl Batch

`indahl-batch`

Runs a check, audit or review over something too big for one context window, such as a whole website, a large repository or a folder of papers. It keeps the instructions short and fixed, gives each batch a fresh worker, writes every result to a file and merges at the end with nothing dropped. Use it when reading the material would fill the context before the work is done.

## What you get

- A one-page brief (`batch/BRIEF.md`) that a worker with no history can follow.
- An item list with a count, and small batches cut from it.
- One results file per batch, with one row per item, including items that could not be read.
- A merged report (`batch/REPORT.md`) with a table per question, the missing-and-rerun list, a spot-check of two items and the date.

## How to use

Run `/batch` followed by what to check. For example:

```
/batch check every page of the docs site against the style guide
```

## Install

```
/plugin marketplace add Heuremen-LLC/indahl.ai
/plugin install indahl-batch@heuremen
```

## Requirements

None. Runs inside Claude Code.

## Services this plugin contacts

None. It runs inside your session.

## Privacy and terms

Privacy: https://indahl.ai/privacy
Terms: https://indahl.ai/terms

Heuremen LLC, https://indahl.ai. Source: https://github.com/Heuremen-LLC/indahl.ai/tree/main/claude-plugins/src/batch
