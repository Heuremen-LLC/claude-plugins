# Indahl Standards

`indahl-standards`

Checks a published paper, preprint or claim against the Heuremen LLC Standards claim codes F1 to F7 (https://indahl.ai/standard) and returns a recount card. Use it to check, audit or recount a paper or a measured claim for internal consistency, selected headlines, missing intervals, unreleased readings or numbers that do not recompute.

## What you get

- A recount card: a status (PRESENT, ABSENT, CANNOT_TELL or NOT_APPLICABLE) for each code F1 to F7.
- Verbatim quotes with their locations, and the scope searched.
- Arithmetic for any number that was recomputed.
- A `not_tested` entry for anything the card did not check, and why.

## How to use

Run `/standards` followed by what to check. For example:

```
/standards ./paper.pdf
```

The skill itself is `standards-check`. The Standard's full text and machine-readable form are bundled in the plugin.

## Install

```
/plugin marketplace add Heuremen-LLC/indahl.ai
/plugin install indahl-standards@heuremen
```

## Requirements

None. Runs inside Claude Code.

## Services this plugin contacts

None of its own. When you give an arXiv id or DOI, Claude fetches that paper with its own tools and treats the text as data, not instructions.

## Privacy and terms

Privacy: https://indahl.ai/privacy
Terms: https://indahl.ai/terms

Heuremen LLC, https://indahl.ai. Source: https://github.com/Heuremen-LLC/indahl.ai/tree/main/claude-plugins/src/standards

## Credits

Refereed before release by Sage, the outside referee at Heuremen LLC (13 Nov 2026): every fix from her review was applied before this version shipped.
