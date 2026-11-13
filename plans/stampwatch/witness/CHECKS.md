
## 2026-11-13 13:35 stampwatch IBM controls: rule 4 and FROZEN counts on saved IBM records outside the floor window, 13 Nov 2026
packs: Q,P,O
(answer each line: holds:/fixed:/caught:/n/a:/cannot tell: followed by what was checked)
- I: holds: floor learned only from pairs inside 2026-05-04..09-14, test pairs all outside it; negative and positive classes chosen by stamp gap and dates moved, not by values; dropped: none (0 refused of 9,331 records, 0 duplicate stamps)
- II: holds: per pair k identical restamps counted item by item before any rate; 0 events in every class, so there is nothing to net; repeat floor here is the floor window itself (0 of 172,993)
- III: n/a: counts of identical values, no signed readings
- V: holds: rulers named in PLAN_v3/v4 before reading: exact binomial P(X>=k|n,u) with BH q=0.05, and the exact 95% upper bound of k/n against u+0.05; both printed per reading
- VI: holds: ABOVE/CONSISTENT/CANNOT_TELL per reading with reasons; 0 ABOVE, 496 CONSISTENT, 5,068 CANNOT_TELL (5,056 unclassed + 12 positive NO_INTERVAL_FORMABLE); positives cannot be read by rule 4 by construction (stated in v4)
- R: holds: counts from read.json produced by stampwatch.py sha in this commit; record files named by filename; nothing post hoc: expected outcomes written in PLAN_v4 (2eb0da1) before this run
- QA: holds: the quantity is IBM's own per-field date and value in its published record, read as published; no vendor figure is reinterpreted; rebuttal 'the stamp attests gates too' tested: FROZEN_RECORD now hashes every field and reads 0
- QB: n/a: no idle arm; this reads published records only
- QC: holds: planted set 13 of 13 passed before reading (selftest); known-good negatives 12 of 12 CONSISTENT; floor measured (0 of 172,993); rule 4 has no real-data positive (stated)
- QD: holds: four outcomes kept; backends are the units; no pooling across backends for readings
- QE: holds: no mechanism named; Q6 described as per-field dates unchanged, never as 'IBM did not remeasure'
- QF: holds: plan v1-v4 pushed before any test pair read (activity record in witness/); record times from file names and last_update_date
- QG: holds: referee (Sage) gets the raw result file and the code; her v3 fixes acted on in v4; nothing published on a site yet
- P1: n/a: the result quotes no source text; it is counts and file names only
- P2: holds: every number points to witness/ibm_controls_result_20261113.json, counts and floors files, code sha
- P3: holds: field names as IBM publishes them (T1, T2, readout_error, prob_meas*)
- P4: holds: no cause stated anywhere in the result
- P5: holds: intervals are exact 95% Clopper-Pearson, stated in the plan
- P6: holds: summary says 0 flags and FROZEN_RECORD 0; Q6 is FROZEN_QUBITS_ONLY/FROZEN_DATE, not a whole-record freeze
- P7: n/a: nothing goes to the ledger or site from this run
- P8: n/a: nothing rendered; this result is a JSON file in the repository, no site page
- P9: holds: plain sentences, no counts in headings
- P10: holds: the FROZEN_RECORD definition was corrected during this run (gates added) after the first output showed 1,768; labelled as a correction in the commit message
- O1: holds: blind-feed collectors registered on the tick bus (snap_hf, snap_ckan, push_manifests); this run is a one-off
- O2: holds: no failures; 0 refused records
- O3: n/a: the run is CPU only (python stdlib), no GPU touched
- O4: holds: liveness = read.json written with 5,564 readings
- O5: holds: absolute paths in riders and scripts
- O6: n/a: the run is CPU only, so no GPU job on any machine
