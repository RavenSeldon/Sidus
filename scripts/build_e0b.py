#!/usr/bin/env python3
"""Build the small E0-B browser dataset from the unmodified v4 archive.

No training, scientific adjudication, canonical rebuild, or network access.
Run from any directory: python3 scripts/build_e0b.py
"""
from pathlib import Path
from zipfile import ZipFile
import hashlib
import json
import re
import statistics

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets/results/e0b'
ARCHIVE = ROOT / 'downloads/E0B_MB0-MB2_archive_v4.zip'
PREFIX = 'E0B_MB0-MB2_archive_v4/'


def table(section):
    return [[v.strip() for v in line.strip('|').split('|')]
            for line in section.splitlines() if line.startswith('|')][2:]


def build():
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / 'evidence').mkdir(exist_ok=True)
    with ZipFile(ARCHIVE) as z:
        raw = lambda name: z.read(PREFIX + name)
        read = lambda name: raw(name).decode()
        obj = lambda name: json.loads(read(name))
        manifest = read('MANIFEST.sha256').splitlines()
        for line in manifest:
            digest, name = line.split(maxsplit=1)
            assert hashlib.sha256(raw(name.lstrip('*').removeprefix('./'))).hexdigest() == digest, name
        spec = obj('E0B_Frozen_Confirmation_Spec.json')
        for name, digest in spec['code_sha256'].items():
            assert hashlib.sha256(raw(name)).hexdigest() == digest, name
        # Published source excerpts are byte-for-byte archive members.
        names = [
            'README.md', 'MANIFEST.sha256', 'ENVIRONMENT.txt', 'E0B_Closing_Report.md',
            'E0B_Frozen_Confirmation_Spec.json', 'E0B_Frozen_Confirmation_Spec.md',
            'E0B_Confirmation_Rules.md', 'E0B_Pilot_Protocol_P0.md',
            'E0B_MB0_Contract_Table.md', 'E0B_Final_State_Report.md',
            'freeze_commitment.txt', 'confirmation_rules_commitment.txt',
            'confirm_results.json', 'confirm_adjudication.json', 'confirm_output.md',
            'mb0_output.md', 'ledgerE_output.md', 'ledgerF_output.md',
            'pilot_process_check.md', 'recheck_thresholds.json',
            'e0b_confirm.py', 'e0b_pilot.py', 'e0b_r24.py', 'e0b_ledgerF.py',
        ]
        for name in names:
            (OUT / 'evidence' / name).write_bytes(raw(name))
        sources = {n: {'href': 'assets/results/e0b/evidence/' + n,
                       'sha256': hashlib.sha256(raw(n)).hexdigest()} for n in names}
        mb0, ledger = read('mb0_output.md'), read('ledgerF_output.md')
        trace = table(mb0.split('## M2')[0])
        noise = table(mb0.split('## M2')[1].split('## M3')[0])
        capacity = table(ledger.split('## F2')[0])
        matrices = {}
        for k in (10, 40):
            section = ledger.split(f'## F2 Trace-compliant Shea matrix, k = {k},')[1].split('\n## ')[0]
            witnesses = []
            for block in section.split('\n### ')[1:]:
                header, *lines = block.splitlines()
                title, verdict = header.rsplit(': ', 1)
                clauses = []
                for line in lines:
                    if not line.startswith('- '):
                        continue
                    left, result = line[2:].rsplit(' -> ', 1)
                    label, value = left.split(': ', 1)
                    clauses.append({'label': label, 'value': value, 'pass': result == 'ok'})
                assert len(clauses) == 9
                witnesses.append({'name': title, 'pass': verdict == 'PASS', 'clauses': clauses})
            assert len(witnesses) == 6
            matrices[str(k)] = witnesses
        results, adjudication = obj('confirm_results.json'), obj('confirm_adjudication.json')
        seeds, th = spec['confirmation_seeds'], spec['thresholds']
        systems = ['IDEAL', 'C-sup', 'C-end', 'B0-am', 'R-vec', 'R-acc']
        stats = {}
        for system in systems:
            rows = [results[f'{system}|{seed}'] for seed in seeds]
            stats[system] = {metric: {'mean': statistics.mean(r[metric] for r in rows),
                                    'sd': statistics.stdev(r[metric] for r in rows)} for metric in rows[0]}
        profiles = []
        for seed in seeds:
            r = results[f'C-sup|{seed}']
            advantage = r['relay'] - max(results[f'{s}|{seed}']['relay'] for s in ['R-vec', 'R-acc'])
            checks = [r['calib_excess'] <= th['thr_cal'], r['kappa_R2'] <= th['thr_inv'],
                      r['S1e_gap_0.75'] <= th['thr_s1e_0.75'], r['S1e_gap_0.8'] <= th['thr_s1e_0.8'],
                      r['D11_agreement'] >= th['thr_d11'], advantage > th['relay_margin']]
            profiles.append({'seed': seed, 'pass': all(checks), 'clauses': checks, 'relay_advantage': advantage})
        assert sum(r['pass'] for r in profiles) == 14
        assert len(results) == 120 and len(seeds) == 20
        data = {'spec': spec, 'sources': sources, 'trace': trace, 'noise': noise, 'capacity': capacity,
                'witnesses': matrices, 'results': results, 'stats': stats, 'profiles': profiles,
                'adjudication': adjudication,
                'archive': {'href': str(ARCHIVE.relative_to(ROOT)), 'members_verified': len(manifest),
                            'sha256': hashlib.sha256(ARCHIVE.read_bytes()).hexdigest()}}
        payload = json.dumps(data, ensure_ascii=False, separators=(',', ':'), allow_nan=False)
        (ROOT / 'assets/results/e0b-data.js').write_text('/* Generated by scripts/build_e0b.py; archived values, not new experiment results. */\nwindow.SIDUS_E0B_DATA=' + payload + ';\n')
        print(f'E0-B: {len(manifest)} archive hashes and {len(spec["code_sha256"])} freeze hashes verified; '
              f'{len(results)} system/seed records; 14/20 individual H1 profiles; {len(payload):,} byte dataset.')


if __name__ == '__main__':
    build()
