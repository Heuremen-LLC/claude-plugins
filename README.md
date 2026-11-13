# Heuremen LLC plugins for Claude Code

Three plugins from Heuremen LLC (https://indahl.ai).

```
/plugin marketplace add Heuremen-LLC/claude-plugins
/plugin install standards@heuremen
/plugin install readcheck@heuremen
/plugin install qia-calibration@heuremen
```

## standards

`/standards <arXiv id | DOI | file | claim>` checks a paper or a measured claim against the Standards claim codes F1 to F7
(https://indahl.ai/standard) and returns a recount card. Every code gets one of four statuses: PRESENT, ABSENT, CANNOT_TELL (with a
reason: NOT_RELEASED, UNREADABLE or METHOD_UNSTATED) or NOT_APPLICABLE. Every PRESENT carries a verbatim quote and its location. Any
recompute shows its arithmetic from the paper's printed numbers, with the rounding range. The card says what the paper prints and what
recomputes. It names no cause.

The full Standard, its JSON form and schema ship inside the plugin under `skills/standards-check/references/`.

## readcheck

A gate for research repositories. When Claude Code runs `git commit` and the commit stages a reading (a file named like `*results*`,
`*outcomes*`, `*readings*` or `RESULTS*.md`), the commit is refused unless a complete `CHECK.json` sits in the same folder or above it.
The block has one answer per Standards recount requirement, REQ-01 to REQ-13 (name the ruler, write the baseline first, state the source
and version, four outcomes, intervals with their level, test the instrument first, receipts, dropped material, corrections, CANNOT_TELL
kept apart, what was not tested, counts beside shares).

```
/readcheck new results/run7 "the reading this folder holds"
/readcheck verify results/run7
/readcheck staged
```

Set your own file patterns in `.readcheck.json` at the repository root: `{"globs": ["*_scores.csv", "eval_*.json"]}`.
The script also runs on its own: `python3 plugins/readcheck/scripts/readcheck.py --help`.

## qia-calibration

`/qia-check` runs the QIA calibration checker (the same tool as `pip install qia-check`) on IBM Quantum calibration records saved in
Qiskit's BackendProperties format.

- Before a run: STALE (T1 or T2 measured more than 24 hours before the record's update), ZERO (an error value of exactly 0), T2 above
  2 x T1, and PAIR (T1 and T2 measured more than 24 hours apart), for the qubits you name.
- After a run: the record in force at the start, every record stamped during the run, and each change in T1, T2 and readout error.

Your files are opened read-only and their sha256 is printed before and after. Run on saved files, it sends nothing anywhere.

## Licenses

- `standards`: the Standard text and data, LICENSE-STANDARD.txt (free to use and cite with attribution, including inside prompts and
  tool calls).
- `readcheck`: MIT.
- `qia-calibration`: LICENSE.txt (free to run and cite with attribution).

Heuremen LLC · https://indahl.ai
