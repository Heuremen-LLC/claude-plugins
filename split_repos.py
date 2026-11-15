#!/usr/bin/env python3
"""One public repo per plugin (15 Nov 2026, Wayfinder: "can you make a seperate repo for each plugin? ... anytime you commit to the repo where
the plugins live we have to re-publish"). Each plugin's built folder becomes the root of Heuremen-LLC/<plugin name>, with a one-entry
.claude-plugin/marketplace.json so it installs on its own. A repo gets a commit (and so a new directory version) ONLY when that plugin's
own files change; nothing else in the house touches these repos.

  directory copies  plugins/<part>   (no .py, no command hooks; what the Claude directory takes from an unverified org)
  indahl            plugins/indahl   (the directory bundle)
  indahl-full       plugins/indahl-full (our marketplace bundle with scripts and the readcheck hook)

  python3 split_repos.py            dry run: what would change, per repo
  python3 split_repos.py --push     create missing repos (public), commit changed ones, push
Local clones live in ~/bones-forge/plugin_repos/<name>. Never edit them by hand: build_plugins.py / build_bundle.py, then this."""
import json, os, shutil, subprocess, sys, filecmp
H = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(H, 'plugins'); ROOT = os.path.expanduser('~/bones-forge/plugin_repos')
ORG = 'indahl-ai'; PUSH = '--push' in sys.argv
AUTHOR = ['-c', 'user.name=Heuremen LLC', '-c', 'user.email=349448817+indahl-ai@users.noreply.github.com']
market = json.load(open(os.path.join(H, '.claude-plugin', 'marketplace.json')))
def folder(e):
    s = e['source']
    if s.startswith('./plugins/'): return os.path.join(H, s[2:])
    return os.path.join(P, s.split('/src/', 1)[1])          # individual plugin: its directory copy
def run(*a, cwd=None, check=True): return subprocess.run(list(a), cwd=cwd, check=check, capture_output=True, text=True)
def same(a, b):
    c = filecmp.dircmp(a, b, ignore=['.git'])
    def d(c): return bool(c.left_only or c.right_only or c.diff_files or c.funny_files) or any(d(s) for s in c.subdirs.values())
    return not d(c)
os.makedirs(ROOT, exist_ok=True); report = []
for e in market['plugins']:
    name, src = e['name'], folder(e)
    if not os.path.isfile(os.path.join(src, '.claude-plugin', 'plugin.json')): report.append((name, 'SKIP: no plugin.json in %s' % src)); continue
    stage = os.path.join(ROOT, '.stage', name)
    if os.path.exists(stage): shutil.rmtree(stage)
    shutil.copytree(src, stage, ignore=shutil.ignore_patterns('__pycache__', '.DS_Store'))
    pj = json.load(open(os.path.join(stage, '.claude-plugin', 'plugin.json')))
    mk = {'name': name, 'owner': market.get('owner', {'name': 'Heuremen LLC'}),
          'plugins': [{'name': name, 'source': './', 'description': pj.get('description', e.get('description', '')), 'version': pj.get('version', e.get('version', '1.0.0')),
                       **({'category': e['category']} if e.get('category') else {}), 'homepage': e.get('homepage', 'https://indahl.ai/plugins')}]}
    json.dump(mk, open(os.path.join(stage, '.claude-plugin', 'marketplace.json'), 'w'), indent=2); open(os.path.join(stage, '.claude-plugin', 'marketplace.json'), 'a').write('\n')
    repo = os.path.join(ROOT, name); exists_remote = run('gh', 'repo', 'view', '%s/%s' % (ORG, name), check=False).returncode == 0
    if os.path.isdir(os.path.join(repo, '.git')) and same(stage, repo): report.append((name, 'unchanged')); continue
    status = 'new repo' if not exists_remote else 'changed'
    if not PUSH: report.append((name, status + ' (dry run)')); continue
    if not exists_remote:
        run('gh', 'repo', 'create', '%s/%s' % (ORG, name), '--public', '--description', pj.get('description', '')[:340], '--homepage', 'https://indahl.ai/plugins')
    if not os.path.isdir(os.path.join(repo, '.git')):
        os.makedirs(repo, exist_ok=True); run('git', 'init', '-q', '-b', 'main', cwd=repo)
        run('git', 'remote', 'add', 'origin', 'https://github.com/%s/%s.git' % (ORG, name), cwd=repo)
    for f in os.listdir(repo):
        if f != '.git': p = os.path.join(repo, f); shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)
    for f in os.listdir(stage):
        s, d = os.path.join(stage, f), os.path.join(repo, f); shutil.copytree(s, d) if os.path.isdir(s) else shutil.copy2(s, d)
    run('git', 'add', '-A', cwd=repo)
    if run('git', 'diff', '--cached', '--quiet', cwd=repo, check=False).returncode == 0: report.append((name, 'no diff after copy')); continue
    run('git', *AUTHOR, 'commit', '-q', '-m', '%s %s' % (name, pj.get('version', '')), cwd=repo)
    run('git', 'push', '-q', '-u', 'origin', 'main', cwd=repo)
    report.append((name, status + ' -> pushed ' + run('git', 'rev-parse', '--short', 'HEAD', cwd=repo).stdout.strip()))
shutil.rmtree(os.path.join(ROOT, '.stage'), ignore_errors=True)
for n, s in report: print('%-28s %s' % (n, s))
