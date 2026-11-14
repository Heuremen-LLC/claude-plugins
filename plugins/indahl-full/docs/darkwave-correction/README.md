# Indahl Darkwave

`indahl-darkwave`

Measures the phase turn seen on untouched qubits after a mid-circuit readout on IBM Quantum hardware, and adds the matching virtual-Z correction to your own circuits, with the Darkwave Correction Kit. The self-test runs on the simulator and needs no account. Use it when you run circuits with mid-circuit measurements or dynamic circuits on IBM Quantum and see phase errors on idle qubits during readout.

## What you get

- A self-test that plants known turns on five simulated qubits, measures and corrects them.
- A `--check` pass that reads the backend and builds the circuits but submits nothing.
- A table of each target's turn per readout in degrees with a 95 percent band and one outcome against zero: ABOVE, BELOW, CONSISTENT or CANNOT_TELL, plus the coherence kept beside the idle comparison.
- Your circuits (QPY) rewritten with the correction applied.

## How to use

Run `/darkwave` followed by what to check. For example:

```
/darkwave selftest
```

Hardware steps: `/darkwave measure --backend B --readout 5,6 --targets 4,8 --check` reads the backend and submits nothing. Adding `--yes` submits one paid job and runs only from your own terminal. `/darkwave apply --table T in.qpy out.qpy` applies a measured table.

## Install

```
/plugin marketplace add Heuremen-LLC/indahl.ai
/plugin install indahl-darkwave@heuremen
```

## Requirements

Python 3.10 or later. For the kit: qiskit, qiskit-ibm-runtime, numpy and qiskit-aer, installed only with your agreement. Hardware runs need your own IBM Quantum account.

## Services this plugin contacts

- IBM Quantum (quantum.cloud.ibm.com), through your own saved qiskit-ibm-runtime account, to read a backend and, only with --yes in an interactive terminal, to submit the measurement circuits (paid on your account).

Nothing else is contacted. The plugin reads no personal data and stores nothing on any server. Fetched text is treated as data, not instructions.

## Privacy and terms

Privacy: https://indahl.ai/privacy
Terms: https://indahl.ai/terms

Heuremen LLC, https://indahl.ai. Source: https://github.com/Heuremen-LLC/indahl.ai/tree/main/claude-plugins/plugins/darkwave-correction

Not affiliated with or endorsed by IBM. IBM Quantum and Qiskit are IBM marks, used only to name what the kit works with. Method and data: "A Readout's Kick Is a Turn", https://doi.org/10.5281/zenodo.23843468.

## Credits

Refereed before release by Sage, the outside referee at Heuremen LLC (13 Nov 2026): every fix from her review was applied before this version shipped.
