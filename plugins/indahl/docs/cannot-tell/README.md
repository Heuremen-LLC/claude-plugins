# Indahl Cannot Tell

`indahl-cannot-tell`

Gives a procedure for answering "I can't tell yet" when the evidence does not settle a question, instead of forcing a guess. The reply states the range of what is still possible, the facts that would decide it and the cheapest way to get them. Use it when a yes or no would be a guess, or when a verdict, number or recommendation is asked for that the material cannot support.

## What you get

- The outcome first: CANNOT_TELL.
- The range of what is still possible, with bounds if it is a number.
- The one or two facts, tests or sources that would decide it, and which way each result would point.
- The cheapest next step, and your lean if you have one, labelled as a lean.

## How to use

Run `/cannot-tell` followed by what to check. For example:

```
/cannot-tell Will the migration finish before the freeze? Here are the last three run logs.
```

## Install

```
/plugin marketplace add Heuremen-LLC/indahl.ai
/plugin install indahl-cannot-tell@heuremen
```

## Requirements

None. Runs inside Claude Code.

## Services this plugin contacts

None. It runs inside your session.

## Privacy and terms

Privacy: https://indahl.ai/privacy
Terms: https://indahl.ai/terms

Heuremen LLC, https://indahl.ai. Source: https://github.com/Heuremen-LLC/indahl.ai/tree/main/claude-plugins/src/cannot-tell
