#!/usr/bin/env python3
"""Offline static checks for the public n8n demonstration package."""
import pathlib, json, re, sys
base = pathlib.Path(__file__).resolve().parents[1]
paths = [p for p in base.rglob('*') if p.is_file() and '.git' not in p.parts]
assert not (base/'.git').exists(), 'Refuse inherited Git history'
for p in paths:
    if p.suffix.lower() not in ('.json', '.md', '.csv') and p.name!='.gitignore':
        continue
    s=p.read_text(encoding='utf-8')
    assert 'REPLACE_WITH_TEST_SHEET_ID' in s or not p.name.endswith('safe-demo.json') or p.name=='recruitment-routing-manual-demo.json', p
    assert not re.search(r'https://docs\.google\.com/spreadsheets/d/[a-zA-Z0-9_-]+',s,re.I), p
    assert not re.search(r'(?i)@[a-z0-9.-]+\.[a-z]{2,}',s) or all(x.lower().endswith('@example.com') for x in re.findall(r'[a-z0-9_.+-]+@[a-z0-9.-]+\.[a-z]{2,}',s,re.I)), p
for p in (base/'workflows').glob('*.json'):
    j=json.loads(p.read_text(encoding='utf-8'))
    assert j.get('active') is False, p
    names={n['name'] for n in j['nodes']}
    assert len(names)==len(j['nodes']), p
    assert all(n['type']!='n8n-nodes-base.googleSheetsTrigger' for n in j['nodes']), p
    for n in j['nodes']:
        assert 'credentials' not in n, p
        if n['type']=='n8n-nodes-base.gmail':
            assert n.get('disabled') is True, p
            assert n['parameters']['sendTo']=='YOUR_TEST_INBOX@example.com', p
        if n['type']=='n8n-nodes-base.googleSheets':
            assert n['parameters']['documentId']['value']=='REPLACE_WITH_TEST_SHEET_ID', p
    for output in j['connections'].values():
        for branch in output.get('main',[]):
            for edge in branch: assert edge['node'] in names, (p,edge)
print('PASS: public demo package static safety checks')
