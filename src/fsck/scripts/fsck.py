#!/usr/bin/env python3
"""Indahl fsck: check your MCP tables. Read-only, like fsck -n: it reports what is broken and the fix, and changes nothing.

  fsck.py            runs `claude mcp list` (Claude Code's own health check) and prints only what needs your hand
  fsck.py FILE       reads a saved `claude mcp list` output instead
  fsck.py --json     the same, as JSON
  fsck.py selftest

Query strings in URLs are never printed, because a token can ride in one."""
import json, re, subprocess, sys
from collections import defaultdict, OrderedDict

LINE = re.compile(r'^(?P<name>.+?): (?P<target>.+?) - (?P<mark>[✔!✘]) (?P<status>.*)$')

def redact(u):
    return re.sub(r'\?.*$', '?…', u.split(' (HTTP)')[0].strip())

def classify(name, target, mark, status):
    plugin = name.startswith('plugin:')
    if mark == '✔': return 'OK', ''
    if mark == '!':
        return ('SIGN IN OR DISABLE', 'installed plugin that was never signed in: /mcp to sign in, or turn the plugin off in /plugins') if plugin else ('RE-AUTH', 'run /mcp and sign in again')
    s = status
    if 'not-setup' in target or 'not-setup' in s: return 'NOT CONFIGURED', 'the plugin ships a placeholder address: set it up from the plugin\'s own docs, or turn the plugin off'
    if 'ENOTFOUND' in s: return 'NO SUCH HOST', 'the address does not exist: turn the plugin off in /plugins or remove the server'
    if 'endpoint not found' in s.lower() or 'HTTP 404' in s: return 'WRONG ADDRESS', 'the host answers but the MCP path is gone: update or turn off the plugin'
    if 'Authorization' in s or 'HTTP 401' in s or 'HTTP 403' in s or 'Invalid access token' in s: return 'BAD TOKEN', 'the server refused the token the config sends: fix the header or token for this server, or turn it off'
    if 'CONNECTION_CLOSED' in s or 'ECONNREFUSED' in s: return 'LOCAL SERVER EXITS', 'the local command starts and dies: run it in a terminal to see why, or remove it'
    if '-32602' in s or '-32600' in s: return 'HANDSHAKE REFUSED', 'the server rejects the MCP handshake: update its command or remove it'
    if 'HTTP 5' in s or '502' in s or '503' in s: return 'SERVER DOWN', 'the server errors: remove it if it is retired, or retry later'
    return 'CANNOT_TELL', 'failed for a reason fsck does not recognise: ' + s[:120]

ORDER = ['NOT CONFIGURED', 'NO SUCH HOST', 'WRONG ADDRESS', 'BAD TOKEN', 'LOCAL SERVER EXITS', 'HANDSHAKE REFUSED', 'SERVER DOWN', 'CANNOT_TELL', 'RE-AUTH', 'SIGN IN OR DISABLE']

def check(text):
    rows = []
    for ln in text.splitlines():
        m = LINE.match(ln.strip())
        if not m: continue
        d = m.groupdict(); cat, fix = classify(d['name'], d['target'], d['mark'], d['status'])
        rows.append(dict(name=d['name'], target=redact(d['target']), state=cat, fix=fix))
    byurl = defaultdict(list)
    for r in rows:
        if r['target'].startswith('http'): byurl[r['target'].rstrip('/?…')].append(r['name'])
    dups = {u: n for u, n in byurl.items() if len(n) > 1}
    return rows, dups

def report(rows, dups):
    groups = OrderedDict((k, []) for k in ORDER)
    for r in rows:
        if r['state'] != 'OK': groups[r['state']].append(r)
    out = ['Indahl fsck: %d servers checked' % len(rows), '']
    for k, rs in groups.items():
        if not rs: continue
        if k == 'SIGN IN OR DISABLE':   # bundle plugins ship many sign-ins: one entry per plugin, with its count
            per = OrderedDict()
            for x in rs: per.setdefault(x['name'].split(':')[1] if x['name'].startswith('plugin:') else x['name'], []).append(x)
            out.append('%-20s %s' % (k, ' · '.join(p + (' (%d)' % len(v) if len(v) > 1 else '') for p, v in sorted(per.items(), key=lambda kv: -len(kv[1])))))
        else:
            out.append('%-20s %s' % (k, ' · '.join(x['name'].replace('plugin:', '').replace('claude.ai ', '') for x in rs)))
        out.append('%-20s → %s' % ('', rs[0]['fix'] if k != 'CANNOT_TELL' else 'see --json for each reason'))
    if dups:
        out.append('%-20s %s' % ('SAME URL TWICE', ' · '.join(' = '.join(n) for n in dups.values())))
        out.append('%-20s → %s' % ('', 'two entries reach one server: keep one, turn the other off'))
    ok = sum(1 for r in rows if r['state'] == 'OK')
    out += ['', 'OK: %d servers answer and need nothing' % ok]
    if not rows: out = ['Indahl fsck: no servers found in the input, so nothing was checked (CANNOT_TELL)']
    return '\n'.join(out)

def selftest():
    t = '\n'.join(['a: https://x.example/mcp - ✔ Connected', 'b: https://y.example/mcp?key=SECRET - ! Needs authentication',
        'plugin:p:q: https://not-setup/v1/mcp?k=1 (HTTP) - ✘ Failed to connect — ENOTFOUND: x', 'plugin:p:r: https://gone.example/mcp (HTTP) - ✘ Failed to connect — ENOTFOUND: getaddrinfo',
        'plugin:p:s: https://z.example/mcp (HTTP) - ✘ Failed to connect — HTTP 400: Authorization header is badly formatted',
        'plugin:p:t: npx thing - ✘ Failed to connect — CONNECTION_CLOSED: Connection closed', 'plugin:p:u: https://x.example/mcp (HTTP) - ! Needs authentication',
        'c: https://w.example - ✘ Failed to connect — something new'])
    rows, dups = check(t); st = {r['name']: r['state'] for r in rows}; rep = report(rows, dups); bad = 0
    for name, want in [('a', 'OK'), ('b', 'RE-AUTH'), ('plugin:p:q', 'NOT CONFIGURED'), ('plugin:p:r', 'NO SUCH HOST'), ('plugin:p:s', 'BAD TOKEN'), ('plugin:p:t', 'LOCAL SERVER EXITS'), ('plugin:p:u', 'SIGN IN OR DISABLE'), ('c', 'CANNOT_TELL')]:
        ok = st.get(name) == want; bad += not ok; print(('PASS ' if ok else 'FAIL ') + '%s reads %s' % (name, want) + ('' if ok else ' (got %s)' % st.get(name)))
    for n, c in [('a query-string token is never printed', 'SECRET' not in rep), ('one server reached twice is reported', any('a' in v and 'plugin:p:u' in v for v in dups.values())),
                 ('empty input reads CANNOT_TELL, not all clear', 'CANNOT_TELL' in report([], {})), ('working servers collapse to one line', rep.count('\na ') == 0 and 'OK: 1' in rep)]:
        bad += not c; print(('PASS ' if c else 'FAIL ') + n)
    print('selftest: %s' % ('all pass' if not bad else '%d FAILED' % bad)); return 1 if bad else 0

if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] == ['selftest']: sys.exit(selftest())
    js = '--json' in a; a = [x for x in a if x != '--json']
    text = open(a[0]).read() if a else subprocess.run(['claude', 'mcp', 'list'], capture_output=True, text=True, timeout=300).stdout
    rows, dups = check(text)
    print(json.dumps(dict(servers=rows, same_url=dups), indent=1) if js else report(rows, dups))
