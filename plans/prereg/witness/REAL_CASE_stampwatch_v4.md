# prereg real case: stampwatch PLAN_v4 against the first rule-4 read

Witness: the host's activity record (github_activity_20261113.json): the first push carrying commit 2eb0da1 (PLAN_v4) is at
2026-11-13T18:31:20Z (head 2eb0da1).
Run: the first ibm-read output file (stampwatch_work/read.json on the Mac) was created at 2026-11-13T18:31:28.9Z (file birth time).
Class user_file: a house file, self-held.
Gap: 8.9 s. Tolerance 120 s (default). Outcome: CANNOT_TELL (STRADDLES_EDGE).
PLAN_v2 wrote the expectation as BEFORE. It does not read BEFORE; this is reported, not tuned. The read was started in the command after
the push, which leaves no margin that a host clock compared against a local file clock can resolve.

## Corrections after the referee's pass (beside the first reading, not over it)

- The run time is a first-output time (the result file's birth), not the run's start: the read began before 18:31:28.9Z, so the true
  push-to-start gap is at most 8.9 s and could be negative. A first-output time can never support BEFORE. Reading stands: CANNOT_TELL.
- Witness class: the first reading used a saved activity record (user_file). Re-fetched live through prereg's own paging fetch on
  13 Nov: first push carrying 2eb0da1 at 2026-11-13T18:31:20Z, ref refs/heads/main, public repository, 1 page read, 0 pushes not
  checkable locally, no later force push dropping it. It matches the saved record (github_activity_live_refetch_20261113.json).
- v2's "expected BEFORE" was never computed: push and read ran one after the other, so the gap was always going to be seconds.
