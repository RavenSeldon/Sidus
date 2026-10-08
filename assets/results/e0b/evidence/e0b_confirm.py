#!/usr/bin/env python3
"""E0-B confirmation pipeline (rules: E0B_Confirmation_Rules.md, hash-committed before the pilot recheck).
Usage:
  python3 e0b_confirm.py recheck   # pilot seeds 1-10: repaired measures + ideal-pipeline floors -> thresholds
  python3 e0b_confirm.py confirm   # seeds 1001-1020 under E0B_Frozen_Confirmation_Spec.json (must exist)
Pure numpy, float64. Training is identical to e0b_pilot.py (deterministic by seed)."""
import sys, json, time
import numpy as np
import e0b_pilot as P

SYSTEMS = ('C-sup', 'C-end', 'B0-am', 'R-vec', 'R-acc')
DPS = (0.75, 0.80)

def kappa_retention(Mf, fit, Mt, test, rng):
    """R^2 for recovering (ka, ki, kd) from (M, phi_post, R): MLP fit on fit split, scored on test split."""
    Xf = np.c_[Mf, fit['phip'], fit['r']]; Xt = np.c_[Mt, test['phip'], test['r']]
    mu, sd = Xf.mean(0), Xf.std(0) + 1e-9; Yf = np.c_[fit['ka'], fit['ki'], fit['kd']]; Yt = np.c_[test['ka'], test['ki'], test['kd']]
    net = P.MLP(Xf.shape[1], 3, rng)
    for t in range(2000):
        ix = rng.integers(0, len(Yf), 1024); pred = net.fwd((Xf[ix] - mu) / sd)
        net.bwd(2 * (pred - Yf[ix]) / 1024); net.step()
    pred = net.fwd((Xt - mu) / sd); mse = ((pred - Yt) ** 2).mean(0); var = Yt.var(0)
    return float((1 - mse / var).mean())

def measures(code, eval_seed, n=100000):
    rng = np.random.default_rng(eval_seed)
    fit, test = P.sample_shea(n, rng), P.sample_shea(n, rng)
    Mf = code(fit).reshape(n, -1); Mt = code(test).reshape(n, -1); out = {}
    pol = P.fit_policy(Mf, fit['r'], P.relay_pay(fit), rng)
    out['relay'] = float(P.relay_pay(test)[np.arange(n), pol(Mt, test['r'])].mean())
    reg = P.fit_regressor(Mf, fit['r'], fit['L'], rng)
    out['calib_excess'] = float(((reg(Mt, test['r']) - test['phip']) ** 2).mean())
    Mk = code(test, ka=rng.random(n), ki=rng.random(n), kd=rng.random(n)).reshape(n, -1)
    out['kappa_sens'] = float(np.linalg.norm(Mk - Mt, axis=1).mean() / (Mt.std(0).mean() + 1e-12))
    out['kappa_R2'] = kappa_retention(Mf, fit, Mt, test, rng)
    # D11 with the FULL action-value vector matched (shared kd; interior ka, ki)
    act = lambda ph: np.argmax(np.stack([ph, 1 - ph, np.full_like(ph, P.D)], 1), 1)
    aopt = act(test['phip']); perm = rng.permutation(n)
    elig = (test['r'] == test['r'][perm]) & (aopt != aopt[perm]); i1 = np.where(elig)[0][:20000]; i2 = perm[i1]
    f1, f2 = test['phip'][i1], test['phip'][i2]; m = len(i1)
    lo_a, hi_a = np.maximum(0, f2 - f1), np.minimum(1, 1 + f2 - f1); ka1 = lo_a + rng.random(m) * (hi_a - lo_a); ka2 = ka1 + f1 - f2
    lo_i, hi_i = np.maximum(0, f1 - f2), np.minimum(1, 1 + f1 - f2); ki1 = lo_i + rng.random(m) * (hi_i - lo_i); ki2 = ki1 + f2 - f1
    kd = rng.random(m)
    assert np.allclose(f1 + ka1, f2 + ka2) and np.allclose(1 - f1 + ki1, 1 - f2 + ki2)           # full vector matched
    assert (ka2 >= -1e-12).all() and (ka2 <= 1 + 1e-12).all() and (ki2 >= -1e-12).all() and (ki2 <= 1 + 1e-12).all()
    sub = lambda idx: {k_: v[idx] for k_, v in test.items()}
    M1 = code(sub(i1), ka=ka1, ki=ki1, kd=kd).reshape(m, -1); M2 = code(sub(i2), ka=ka2, ki=ki2, kd=kd).reshape(m, -1)
    out['D11_agreement'] = float(((pol(M1, test['r'][i1]) == aopt[i1]) & (pol(M2, test['r'][i2]) == aopt[i2])).mean())
    for dp in DPS:
        polp = P.fit_policy(Mf, fit['r'], P.relay_pay(fit, dp), rng)
        v = P.relay_pay(test, dp)[np.arange(n), polp(Mt, test['r'])].mean()
        ideal = P.relay_pay(test, dp)[np.arange(n), np.argmax(np.stack([test['phip'], 1 - test['phip'], np.full(n, dp)], 1), 1)].mean()
        out[f'S1e_gap_{dp}'] = float(ideal - v)
    return out

def ideal_code(b, ka=None, ki=None, kd=None):
    return b['phip'][:, None]

def run(seeds, tag):
    res = {}
    for s in seeds:
        for kind in SYSTEMS:
            t0 = time.time(); code = P.train_system(kind, s); res[f'{kind}|{s}'] = measures(code, 9000 + s)
            print(tag, kind, s, {k: round(v, 6) for k, v in res[f'{kind}|{s}'].items()}, f'{time.time() - t0:.0f}s', flush=True)
        res[f'IDEAL|{s}'] = measures(ideal_code, 9000 + s)
        print(tag, 'IDEAL', s, {k: round(v, 6) for k, v in res[f'IDEAL|{s}'].items()}, flush=True)
    return res

def bounds(v, alpha=0.05):
    """seed-level mean and one-sided (1 - alpha) t-bounds (lower, upper)."""
    from scipy.stats import t as tdist
    v = np.asarray(v); n = len(v); mu = v.mean(); se = v.std(ddof=1) / np.sqrt(n); tq = tdist.ppf(1 - alpha, n - 1)
    return mu, mu - tq * se, mu + tq * se

def adjudicate(res, spec, seeds):
    th = spec['thresholds']; get = lambda sysn, k: np.array([res[f'{sysn}|{s}'][k] for s in seeds])
    best_rival = np.maximum(get('R-vec', 'relay'), get('R-acc', 'relay'))
    out = {}
    # H1: C-sup passes all six clauses (IUT for pass at alpha; Holm over six for declaring a clause fail)
    clauses = [('S1a calibration', get('C-sup', 'calib_excess'), th['thr_cal'], 'le'),
               ('S1b kappa-retention R2', get('C-sup', 'kappa_R2'), th['thr_inv'], 'le'),
               ('S1e gap 0.75', get('C-sup', 'S1e_gap_0.75'), th['thr_s1e_0.75'], 'le'),
               ('S1e gap 0.80', get('C-sup', 'S1e_gap_0.8'), th['thr_s1e_0.8'], 'le'),
               ('D11 agreement', get('C-sup', 'D11_agreement'), th['thr_d11'], 'ge'),
               ('relay advantage over best rival', get('C-sup', 'relay') - best_rival, th['relay_margin'], 'gt')]
    rows = []; pvals_fail = []
    for name, v, thr, side in clauses:
        mu, lo, hi = bounds(v)
        passed = (hi <= thr) if side == 'le' else (lo >= thr if side == 'ge' else lo > thr)
        rows.append([name, float(mu), float(lo), float(hi), thr, side, passed])
    # Holm for failure declarations: a clause is declared FAILED if its passing-side bound at Holm-adjusted alpha excludes passing
    for i, (name, v, thr, side) in enumerate(clauses):
        mu, lo, hi = bounds(v, 0.05 / len(clauses))      # Bonferroni over the six clauses: at least as conservative as Holm for declaring failure
        failed = (lo > thr) if side == 'le' else (hi < thr)
        rows[i].append(failed)
    out['H1'] = dict(rows=rows, verdict='confirmed' if all(r[6] for r in rows) else ('disconfirmed' if any(r[7] for r in rows) else 'inconclusive'))
    # H2: C-end D11 upper <= 0.20 AND kappa_sens lower >= 0.25, each at alpha/2
    d11 = get('C-end', 'D11_agreement'); ks = get('C-end', 'kappa_sens')
    m1, l1, h1 = bounds(d11, 0.025); m2, l2, h2 = bounds(ks, 0.025)
    conf = (h1 <= 0.20) and (l2 >= 0.25); dis = (l1 > 0.20) or (h2 < 0.25)
    out['H2'] = dict(rows=[['D11 agreement <= 0.20', float(m1), float(l1), float(h1)], ['kappa-sensitivity >= 0.25', float(m2), float(l2), float(h2)],
                           ['(descriptive) kappa R2', float(get('C-end', 'kappa_R2').mean()), None, None]],
                     verdict='confirmed' if conf else ('disconfirmed' if dis else 'inconclusive'))
    # H3: B0-am D11 lower >= 0.30 AND kappa R2 lower >= thr_ret, each at alpha/2
    d11 = get('B0-am', 'D11_agreement'); r2 = get('B0-am', 'kappa_R2')
    m1, l1, h1 = bounds(d11, 0.025); m2, l2, h2 = bounds(r2, 0.025)
    conf = (l1 >= 0.30) and (l2 >= th['thr_ret']); dis = (h1 < 0.30) or (h2 < th['thr_ret'])
    out['H3'] = dict(rows=[['D11 agreement >= 0.30', float(m1), float(l1), float(h1)], [f"kappa R2 >= {th['thr_ret']:.4f}", float(m2), float(l2), float(h2)]],
                     verdict='confirmed' if conf else ('disconfirmed' if dis else 'inconclusive'))
    return out

if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'recheck':
        seeds = list(range(1, 11)); res = run(seeds, 'RECHECK'); json.dump(res, open('recheck_results.json', 'w'), indent=1)
        fl = lambda k, q: float(np.quantile([res[f'IDEAL|{s}'][k] for s in seeds], q))
        th = {'thr_cal': fl('calib_excess', 0.95) + 0.002,
              'thr_s1e_0.75': fl('S1e_gap_0.75', 0.95) + 0.002, 'thr_s1e_0.8': fl('S1e_gap_0.8', 0.95) + 0.002,
              'thr_inv': fl('kappa_R2', 0.95) + 0.02, 'thr_ret': fl('kappa_R2', 0.95) + 0.10,
              'thr_d11': fl('D11_agreement', 0.05) - 0.10, 'relay_margin': 0.01299}
        json.dump({'thresholds': th, 'floors': {k: [res[f'IDEAL|{s}'][k] for s in seeds] for k in res['IDEAL|1']}}, open('recheck_thresholds.json', 'w'), indent=1)
        print('THRESHOLDS', json.dumps(th, indent=1))
        # exploratory: apply the decision algebra to the pilot seeds (n=10) for information only
        print('EXPLORATORY pilot-seed adjudication (n=10, not confirmatory):')
        for h, v in adjudicate(res, {'thresholds': th}, seeds).items(): print(' ', h, v['verdict'])
    elif mode == 'confirm':
        spec = json.load(open('E0B_Frozen_Confirmation_Spec.json'))
        seeds = list(range(1001, 1021)); res = run(seeds, 'CONFIRM'); json.dump(res, open('confirm_results.json', 'w'), indent=1)
        adj = adjudicate(res, spec, seeds); json.dump(adj, open('confirm_adjudication.json', 'w'), indent=1, default=str)
        for h, v in adj.items():
            print(h, v['verdict'])
            for r in v['rows']: print('   ', r)
