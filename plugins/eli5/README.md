# Indahl ELI5

`indahl-eli5`

Takes anything complex or technical, such as a paper, a result, a log, a contract clause, an error message or a plan, and says it again in plain language anyone can follow. It keeps what is true. The key numbers stay in, how sure anyone is stays in, and what is still unknown stays in. Jargon goes out.

## What you get

- The one thing the reader must keep, stated first in plain words.
- A real example, and an analogy only as a bridge, with where it breaks.
- A double check of the result: once as the expert who wrote the source, once as the newcomer reading it.

## How to use

Run `/eli5` followed by what to check. For example:

```
/eli5 the error log in build.txt
```

You can also ask Claude to explain something simply.

## Install

```
/plugin marketplace add Heuremen-LLC/indahl.ai
/plugin install indahl-eli5@heuremen
```

## Requirements

None. Runs inside Claude Code.

## Services this plugin contacts

None. It runs inside your session and opens only what you point it at.

## Privacy and terms

Privacy: https://indahl.ai/privacy
Terms: https://indahl.ai/terms

Heuremen LLC, https://indahl.ai. Source: https://github.com/Heuremen-LLC/indahl.ai/tree/main/claude-plugins/src/eli5

## Credits

Named and shaped by Wayfinder, from the way he has asked for explanations all along.
