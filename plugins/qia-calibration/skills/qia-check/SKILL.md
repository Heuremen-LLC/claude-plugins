---
name: qia-check
description: Check an IBM Quantum backend calibration record (Qiskit BackendProperties JSON) before a run, or find which record was in force during a run and what changed. Use when someone is about to run on IBM Quantum hardware, is writing up results that cite T1, T2, readout error or gate error, asks whether a calibration record is stale or consistent, or mentions QIA or the QIA Calibration Pack.
---

# QIA calibration check

The checker is `${CLAUDE_PLUGIN_ROOT}/scripts/qia_check.py` (Python 3.9 or later, standard library only; the same tool as
`pip install qia-check`). It opens the user's files read-only, prints their sha256 before and after, and writes its report to a separate
folder (default `./heuremen_report/`). Run on saved files, it sends nothing anywhere. Only `--pull` contacts IBM, with the user's own saved
account, and only when the user asks for it.

The console prints only the paths of two reports: an HTML page for people and a JSON file. Read the JSON file (keys `meta`, `inputs`,
`flags` before a run; `meta`, `record_at_start`, `records_during`, `changes`, `skipped` after one) and report from it. Confirm that each
input's `sha256_before` equals its `sha256_after`.

## Before a run

1. Get the record. If the user has none, show them how to save one:
   `json.dump(backend.properties().to_dict(), open('record.json', 'w'), default=str)`
2. Run `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/qia_check.py" before record.json --qubits <the qubits the circuit uses>`.
3. Report each entry in `flags` (STALE, ZERO, T2>2T1 as ABOVE or CANNOT_TELL, PAIR) for the qubits used, and suggest moving the
   layout off flagged qubits where the circuit allows it. If no flags, say the record's own figures passed these checks, nothing more.

## After a run

1. Collect the records saved around the run into one folder (one saved right before submitting is the one that matters).
2. Run `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/qia_check.py" after <folder> --start <run start, UTC> --end <run end, UTC> --qubits <...>`.
   Times come from the job record (`job.metrics()` or the job's timestamps), never from memory.
3. Report the record in force at the start, every recalibration inside the window, and each change in T1, T2 and readout error on the
   run's qubits. If the folder has no record at or before the start, say the record in force is not in the folder.

## How to talk about the result

- The checks read IBM's published figures only. They say nothing about the user's results. Do not turn a flag into a claim about the
  device or the experiment.
- IBM's gate_error is a randomized-benchmarking average infidelity, not a per-gate probability, and T1 is IBM's own fit over IBM's window.
  Say so if the user compares their own numbers against these figures.
- A figure inside the stated value is not a deviation, however large it looks in other units.

Free to run and cite with attribution to Heuremen LLC, https://indahl.ai/qia. See LICENSE.txt.
