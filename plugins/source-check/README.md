# Indahl Source Check

`indahl-source-check`

Checks every citation, reference or link in a paper, report, answer or another skill's output: whether it exists, whether it says what the text claims, and which version was read. Use it on literature reviews, research memos and answers with references, and before citing anything you did not read.

## What you get

- A row for every citation.
- One mark per citation: SUPPORTS, PARTIAL, CONTRADICTS, SILENT, NOT_FOUND or CANNOT_TELL.
- The passage that decides each mark.

## How to use

Run `/source-check` followed by what to check. For example:

```
/source-check literature-review.md
```

## Install

```
/plugin marketplace add Heuremen-LLC/indahl.ai
/plugin install indahl-source-check@heuremen
```

## Requirements

None. Runs inside Claude Code.

## Services this plugin contacts

None. It runs inside your session and opens only the sources you point it at.

## Privacy and terms

Privacy: https://indahl.ai/privacy
Terms: https://indahl.ai/terms

Heuremen LLC, https://indahl.ai. Source: https://github.com/Heuremen-LLC/indahl.ai/tree/main/claude-plugins/src/source-check
