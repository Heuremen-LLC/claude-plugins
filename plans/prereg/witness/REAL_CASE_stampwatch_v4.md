# prereg real case: stampwatch PLAN_v4 against the first rule-4 read

Witness: the host's activity record (github_activity_20261113.json): the first push carrying commit 2eb0da1 (PLAN_v4) is at
2026-11-13T18:31:20Z (head 2eb0da1).
Run: the first ibm-read output file (stampwatch_work/read.json on the Mac) was created at 2026-11-13T18:31:28.9Z (file birth time).
Class user_file: a house file, self-held.
Gap: 8.9 s. Tolerance 120 s (default). Outcome: CANNOT_TELL (STRADDLES_EDGE).
PLAN_v2 wrote the expectation as BEFORE. It does not read BEFORE; this is reported, not tuned. The read was started in the command after
the push, which leaves no margin that a host clock compared against a local file clock can resolve.
