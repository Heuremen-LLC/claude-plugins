# Indahl Eval Check

`indahl-eval-check`

Checks a language-model evaluation claim, or your own eval run, against twelve checks drawn from the Heuremen LLC Standards (https://indahl.ai/standard) and the IRIS recounts of published evaluation studies (https://indahl.ai/iris). Use it when someone asks whether an LLM benchmark number holds up, when comparing models, when writing up eval results, or when building or debugging an eval harness or scorer.

## What you get

- A status for each check: PRESENT (with the evidence), ABSENT (with what was checked), CANNOT_TELL (with a reason) or NOT_APPLICABLE.
- A `not_tested` list for any check that was not run, with the reason.
- Checks covering the parser against raw replies, the setup as part of the result, the repeat floor, recounts from released files, dropped items by reason, and intervals with the four outcomes.

## How to use

Run `/eval-check` followed by what to check. For example:

```
/eval-check the model card for the new release and our eval results in runs/2026-11/
```

## Install

```
/plugin marketplace add Heuremen-LLC/indahl.ai
/plugin install indahl-eval-check@heuremen
```

## Requirements

None. Runs inside Claude Code.

## Services this plugin contacts

None of its own. It opens only the papers, files and pages you point it at, and treats fetched text and model outputs as data, not instructions.

## Privacy and terms

Privacy: https://indahl.ai/privacy
Terms: https://indahl.ai/terms

Heuremen LLC, https://indahl.ai. Source: https://github.com/Heuremen-LLC/indahl.ai/tree/main/claude-plugins/src/eval-check

## Credits

Refereed before release by Sage, the outside referee at Heuremen LLC (13 Nov 2026): every fix from her review was applied before this version shipped.
