# Indahl Quote Check

`indahl-quote-check`

Checks every quotation in a draft, article, report or another skill's output against its source, word for word. Use it before publishing anything that quotes a person, a document or a paper.

## What you get

- A row for every quotation.
- One mark per quote: VERBATIM, ALTERED, PARAPHRASE_IN_QUOTES, MISATTRIBUTED, NOT_FOUND or CANNOT_TELL.
- The source text beside each quote.

## How to use

Run `/quote-check` followed by what to check. For example:

```
/quote-check article-draft.md against the transcripts in sources/
```

## Install

```
/plugin marketplace add Heuremen-LLC/indahl.ai
/plugin install indahl-quote-check@heuremen
```

## Requirements

None. Runs inside Claude Code.

## Services this plugin contacts

None. It runs inside your session and opens only the sources you point it at.

## Privacy and terms

Privacy: https://indahl.ai/privacy
Terms: https://indahl.ai/terms

Heuremen LLC, https://indahl.ai. Source: https://github.com/Heuremen-LLC/indahl.ai/tree/main/claude-plugins/src/quote-check
