#!/usr/bin/env python3
"""readcheck.py -- Heuremen LLC (https://indahl.ai/standard). Standard library only. MIT license.

A reading (a results, outcomes or readings file) is committed together with a check block, CHECK.json, in the same folder or a folder
above it. The block has one line per Standards recount requirement, REQ-01 to REQ-13. Every line is filled: "holds: <what you checked>",
"not applicable: <why>", or what you found and fixed. A blank line, or one still reading TODO, fails.

  python3 readcheck.py new <folder> --what "<the reading>"   write a blank CHECK.json to fill
  python3 readcheck.py verify <folder>                       check one block
  python3 readcheck.py staged                                check every reading staged in git
  python3 readcheck.py hook                                  Claude Code PreToolUse hook (reads the tool call on stdin)

Which files count as readings: names matching READING_GLOBS below, or the "globs" list in a .readcheck.json at the repository root."""
import json, sys, os, fnmatch, subprocess, datetime as dt, argparse, re

REQS = {
 "REQ-01": "Name the ruler before the number: the instrument and the question it answers, chosen before the quantity was computed.",
 "REQ-02": "Write the baseline down first: counts, windows, averaging and places examined, for every arm, before the measurement arm.",
 "REQ-03": "State the data source: where each input came from; raw copies kept with SHA-256 hashes.",
 "REQ-04": "State the version read: version, edition or retrieval date of every source, with the date and time of the read.",
 "REQ-05": "Use reading outcomes: ABOVE / BELOW / CONSISTENT / CANNOT_TELL against a figure named in advance; CANNOT_TELL carries a reason.",
 "REQ-06": "Give each reading its interval and level: interval, method, level, n, and the n it was selected from; every rate names its denominator.",
 "REQ-07": "Test the instrument first: a case it must pass and a case it must fail, both recorded.",
 "REQ-08": "Publish receipts: every number links to the file, row or run it came from.",
 "REQ-09": "Name dropped material: every discarded run, row or arm, with the reason and what replaced it.",
 "REQ-10": "Publish corrections beside the first reading: a corrected reading stays in the record beside the correction.",
 "REQ-11": "Keep CANNOT_TELL as its own result: never folded into pass or fail, never counted as agreement or disagreement.",
 "REQ-12": "State what was not tested: every code, fault and guard not tested, and why.",
 "REQ-13": "Print the counts beside every headline share: NOTHING_RETURNED count and CANNOT_TELL share by reason.",
}
READING_GLOBS = ["*results*.json", "*results*.jsonl", "*results*.csv", "*outcomes*.json", "*outcomes*.jsonl", "*outcomes*.csv",
                 "*readings*.json", "*readings*.jsonl", "*readings*.csv", "RESULTS*.md", "*_RESULT.md"]
BLOCK = "CHECK.json"
MIN_ANSWER = 8

def new(folder, what):
    os.makedirs(folder, exist_ok=True); p = os.path.join(folder, BLOCK)
    if os.path.exists(p): sys.exit(f"{p} exists; edit it")
    blk = {"standard": "Standards 2.0.0 recount requirements", "what": what,
           "written": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
           "requirements": {k: {"asks": v, "answer": "TODO"} for k, v in REQS.items()}}
    json.dump(blk, open(p, "w"), indent=2); print(f"wrote {p}: fill every answer, then commit it with the reading")

def problems(path):
    try: blk = json.load(open(path))
    except Exception as e: return [f"{path}: not readable JSON ({e})"]
    out = []
    if not str(blk.get("what", "")).strip(): out.append(f"{path}: 'what' is empty")
    reqs = blk.get("requirements", {})
    for k in REQS:
        a = str((reqs.get(k) or {}).get("answer", "")).strip()
        if not a: out.append(f"{path}: {k} has no answer")
        elif re.fullmatch(r"(?i)todo\.?|tbd|-|n/?a|none|ok|yes|holds:?", a): out.append(f"{path}: {k} answer '{a}' says nothing; write what you checked")
        elif len(a) < MIN_ANSWER: out.append(f"{path}: {k} answer too short to say what was checked")
    return out

def find_block(f, root):
    d = os.path.dirname(os.path.abspath(f)); root = os.path.abspath(root)
    while True:
        p = os.path.join(d, BLOCK)
        if os.path.exists(p): return p
        if d == root or os.path.dirname(d) == d: return None
        d = os.path.dirname(d)

def git(*a, cwd=None):
    return subprocess.run(["git", *a], cwd=cwd, capture_output=True, text=True)

def staged(cwd=None, with_tracked=False):
    r = git("rev-parse", "--show-toplevel", cwd=cwd)
    if r.returncode: return []
    root = r.stdout.strip(); globs = READING_GLOBS
    cfg = os.path.join(root, ".readcheck.json")
    if os.path.exists(cfg):
        try: globs = json.load(open(cfg)).get("globs", globs)
        except Exception: pass
    names = git("diff", "--cached", "--name-only", "--diff-filter=AM", cwd=root).stdout.split()
    if with_tracked: names += git("diff", "--name-only", "--diff-filter=AM", cwd=root).stdout.split()  # what commit -a adds
    out = []
    for n in names:
        if not any(fnmatch.fnmatch(os.path.basename(n), g) for g in globs): continue
        blk = find_block(os.path.join(root, n), root)
        if not blk: out.append(f"{n}: a reading with no {BLOCK} in its folder or above. Run: python3 readcheck.py new {os.path.dirname(n) or '.'} --what \"...\"")
        else: out += [x.replace(blk, os.path.relpath(blk, root)) for x in problems(blk)]
    return sorted(set(out))

def hook():
    try: ev = json.load(sys.stdin)
    except Exception: return 0
    cmd = (ev.get("tool_input") or {}).get("command", "")
    if not re.search(r"(^|[;&|]\s*|\s)git\s+(-C\s+\S+\s+)?commit\b", cmd): return 0
    m = re.search(r"git\s+-C\s+(\S+)", cmd); cwd = m.group(1) if m else ev.get("cwd")
    bad = staged(cwd, with_tracked=bool(re.search(r"\s-[a-zA-Z]*a[a-zA-Z]*\b|\s--all\b", cmd)))
    if not bad: return 0
    print("readcheck: this commit adds a reading without a complete check block.\n" + "\n".join(bad) +
          "\nFill every REQ line in CHECK.json (see https://indahl.ai/standard) and commit it with the reading.", file=sys.stderr)
    return 2

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    n = sp.add_parser("new"); n.add_argument("folder"); n.add_argument("--what", required=True)
    v = sp.add_parser("verify"); v.add_argument("folder")
    sp.add_parser("staged"); sp.add_parser("hook")
    a = ap.parse_args()
    if a.cmd == "new": new(a.folder, a.what)
    elif a.cmd == "verify":
        p = a.folder if a.folder.endswith(".json") else os.path.join(a.folder, BLOCK); bad = problems(p)
        print("\n".join(bad) if bad else f"{p}: complete"); sys.exit(1 if bad else 0)
    elif a.cmd == "staged":
        bad = staged(); print("\n".join(bad) if bad else "every staged reading has a complete check block"); sys.exit(1 if bad else 0)
    elif a.cmd == "hook": sys.exit(hook())

if __name__ == "__main__": main()
