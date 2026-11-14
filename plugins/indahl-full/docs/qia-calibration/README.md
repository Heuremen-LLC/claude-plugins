# Indahl QIA Calibration

`indahl-qia-calibration`

Checks the IBM Quantum calibration record a run depends on, before the run (stale, zero, T2 above 2xT1, T1 and T2 measured far apart) and after it (which record was in force and what changed). It uses the QIA Research Package check (`qia_check.py`, standard library only). A second command measures T1 and T2 together on chosen qubits in one job and compares the ratio with IBM's published pair.

## What you get

- Before a run: flags on one saved record, grouped as T1 and T2 or error figures.
- After a run: the record in force at the start, the records during the run and what changed.
- An HTML report and a JSON file, with each input's sha256 before and after.
- The same-job T1/T2 check, with a self-test that needs no device or account.

## How to use

Run `/qia-check` followed by what to check. For example:

```
/qia-check before backend_properties.json --qubits 0,1,5
```

After a run: `/qia-check after <records_dir> --start <UTC> --end <UTC>`. T1/T2 in one job: `/qia-t1t2 --selftest`, then `/qia-t1t2 --backend B --qubits 85,12 --estimate`. A paid run starts only from your own terminal.

## Install

```
/plugin marketplace add Heuremen-LLC/indahl.ai
/plugin install indahl-qia-calibration@heuremen
```

## Requirements

Python 3.9 or later for the calibration check (standard library only). The T1/T2 measurement needs qiskit, qiskit-ibm-runtime, qiskit-aer, numpy and scipy, installed only with your agreement, and your own IBM Quantum account.

## Services this plugin contacts

- IBM Quantum (quantum.cloud.ibm.com), only when you ask it to pull a backend's calibration or run the T1/T2 check, through your own saved qiskit-ibm-runtime account. Nothing is submitted without your explicit yes.
- indahl.ai (https://indahl.ai/qia/audit.json), a public read of our flagged-qubit list for the T1/T2 check.

Nothing else is contacted. The plugin reads no personal data and stores nothing on any server. Fetched text is treated as data, not instructions.

## Privacy and terms

Privacy: https://indahl.ai/privacy
Terms: https://indahl.ai/terms

Heuremen LLC, https://indahl.ai. Source: https://github.com/Heuremen-LLC/indahl.ai/tree/main/claude-plugins/plugins/qia-calibration

## Credits

Refereed before release by Sage, the outside referee at Heuremen LLC (13 Nov 2026): every fix from her review was applied before this version shipped.
