#!/usr/bin/env python3
"""E0-B Ledger F — implementation corrections after the review of Ledger E (archive v2 preserved).

F1  S1e binding-payoff grid: phi code vs policy-bit W10 at d' in {0.70 .. 0.90}; oracle, k=10, k=40 traces.
    Ledger E's proposed {0.75, 0.90} fails to discriminate at k=10 (d'=0.90); {0.75, 0.80} discriminates everywhere.
F2  Trace-compliant Shea matrix re-run with S1e at the binding pair {0.75, 0.80}, with W10 added as a full witness.
F3  Process P1c, specificity arm (v2.1 wording: 'for matched anchor output and matched reliability, M supports
    different predictions where mappings differ'), joined to the relabelling-invariance arm executed in Ledger E.
Exact arithmetic (trace distributions float-derived for k > 10). Imports e0b_contracts, e0b_mb0, e0b_mb12, e0b_ledgerE.
"""
from fractions import Fraction as F
from collections import defaultdict
from itertools import product, combinations
import e0b_contracts as C
import e0b_mb0 as M0
import e0b_mb12 as M
import e0b_ledgerE as E

D = C.D; act = M.act
S1E_BINDING = (F(75, 100), F(80, 100))

def grouped_value(S, code, dp):
    g = defaultdict(lambda: [F(0), F(0)])
    for pr, s in S: a = g[(code(s), s['r'])]; a[0] += pr; a[1] += pr * s['L']
    return sum(max(c, m - c, dp * m) for m, c in g.values())

def contexts():
    So = M.world(); oracle = lambda s: M.phi_cf(s['r'], s['o'], s['T'], s['f'], C.P_X)
    out = [('oracle', So, oracle)]
    for k in (10, 40):
        S = E.trace_world(k); enc = C.encode(S, 'L', ['o', 'r', 'T', 'fhat']); out.append((f'k={k} trace', S, (lambda s, enc=enc: enc(s))))
    return out

def f1():
    rows = []
    for tag, S, target in contexts():
        for dp in (F(70, 100), F(75, 100), F(80, 100), F(85, 100), F(90, 100)):
            a = grouped_value(S, target, dp); b = grouped_value(S, lambda s: act(target(s)), dp)
            rows.append((tag, dp, a, b))
    return rows

def f2(k, dps=S1E_BINDING):
    """trace-compliant Shea clauses (as Ledger E E4) with S1e at binding payoffs and W10 as an additional witness."""
    S = E.trace_world(k); phit = C.encode(S, 'L', ['o', 'r', 'T', 'fhat']); PH = lambda s: phit(s)
    atoms = M0.atoms_from(S); bound = M0.relay_rival(atoms, 'vector')
    it = [(r, f, m, c) for (r, f), (m, c) in atoms.items()]
    def rival_dec(kind):
        def dec(mv, r):
            if kind == 'accept': L = [x for x in it if x[0] == r and x[1] <= mv <= x[1] + 1]
            elif kind == 'invert': L = [x for x in it if x[0] == r and 1 - x[1] <= mv <= 2 - x[1]]
            else: L = [x for x in it if x[0] == r and x[1] <= mv[0] <= x[1] + 1 and 1 - x[1] <= mv[1] <= 2 - x[1]]
            m = sum(x[2] for x in L); return (sum(x[3] for x in L) / m) if m else None
        return dec
    def rival_integrals(kind, dlist):
        if kind == 'vector':
            bx = sorted({f for _, f, _, _ in it} | {f + 1 for _, f, _, _ in it}); by = sorted({1 - f for _, f, _, _ in it} | {2 - f for _, f, _, _ in it})
            cells = [((a + b) / 2, (c_ + d_) / 2, (b - a) * (d_ - c_)) for a, b in zip(bx, bx[1:]) for c_, d_ in zip(by, by[1:])]
            livef = lambda cl, r: [x for x in it if x[0] == r and x[1] <= cl[0] <= x[1] + 1 and 1 - x[1] <= cl[1] <= 2 - x[1]]
        else:
            sh = (lambda f: f) if kind == 'accept' else (lambda f: 1 - f)
            bp = sorted({sh(f) for _, f, _, _ in it} | {sh(f) + 1 for _, f, _, _ in it})
            cells = [((a + b) / 2, None, b - a) for a, b in zip(bp, bp[1:])]
            livef = lambda cl, r: [x for x in it if x[0] == r and sh(x[1]) <= cl[0] <= sh(x[1]) + 1]
        val = F(0); exc = F(0); vd = [F(0)] * len(dlist)
        for cl in cells:
            for r in (0, 1):
                L = livef(cl, r)
                if not L: continue
                m = sum(x[2] for x in L); c = sum(x[3] for x in L); pb = c / m
                val += cl[2] * max(c, m - c, D * m); exc += cl[2] * sum(x[2] * (pb - x[1]) ** 2 for x in L)
                for i, dp in enumerate(dlist): vd[i] += cl[2] * max(c, m - c, dp * m)
        return val, exc, vd
    WT = {
        'W5t token-phi (trace-compliant)': ('free', lambda s, c: PH(s)),
        'W10 policy bit act(phi) at d=0.55': ('free', lambda s, c: act(PH(s))),
        'W1 regime code': ('free', lambda s, c: s['T']),
        'B1t-accept-value': ('accept', lambda s, c: PH(s) + c['ka']),
        'B1t-invert-value': ('invert', lambda s, c: 1 - PH(s) + c['ki']),
        'B1t-action-vector': ('vector', lambda s, c: (PH(s) + c['ka'], 1 - PH(s) + c['ki'])),
    }
    C0 = dict(ka=F(0), ki=F(0)); out = {}
    idx = {(s['x'], s['z1'], s['z2'], s['n'], s['o'], s['wb'], s['fhat']): s for _, s in S}
    oracle_phi = lambda s: M.phi_cf(s['r'], s['o'], s['T'], s['f'], C.P_X)
    part = {}
    for _, t in S: part.setdefault((t['o'], t['T'], t['fhat'], t['r']), t)
    for name, (kind, code) in WT.items():
        res, ok = {}, {}
        if kind == 'free':
            g = defaultdict(lambda: [F(0), F(0)])
            for pr, s in S: a = g[(code(s, C0), s['r'])]; a[0] += pr; a[1] += pr * s['L']
            dec = lambda m, r, g=g: (g[(m, r)][1] / g[(m, r)][0]) if g[(m, r)][0] else None
            exc = sum(pr * (dec(code(s, C0), s['r']) - PH(s)) ** 2 for pr, s in S)
            val = sum(max(c, m - c, D * m) for m, c in g.values())
            vd = [sum(max(c, m - c, dp * m) for m, c in g.values()) for dp in dps]
        else:
            dec = rival_dec(kind); val, exc, vd = rival_integrals(kind, dps)
        res['S1a calibration excess (contract target)'] = exc; ok['S1a calibration excess (contract target)'] = exc == 0
        elig = trk = F(0); kg = [(F(0), F(0)), (F(1, 2), F(1, 2))] if kind != 'free' else [(F(0), F(0))]
        for pr, s in S:
            s2 = idx[(s['x'], 1 - s['z1'], s['z2'], s['n'], s['o'], s['wb'], s['fhat'])]; dphi = PH(s2) - PH(s)
            if dphi == 0: continue
            for ka, ki in kg:
                cc = dict(ka=ka, ki=ki); a, b = dec(code(s, cc), s['r']), dec(code(s2, cc), s2['r'])
                elig += pr; trk += pr * (a is not None and b is not None and (b - a) * dphi > 0)
        res['S1b tracking rate'] = trk / elig; ok['S1b tracking rate'] = trk == elig
        nu = sum(pr for pr, s in S if code(s, C0) != code(s, dict(ka=F(1, 2), ki=F(1, 2))))
        res['S1b nuisance change mass'] = nu; ok['S1b nuisance change mass'] = nu == 0
        tot = hit = F(0)
        for (p1, s1), (p2, s2) in product(S, S):
            if s1['r'] != s2['r'] or act(PH(s1)) == act(PH(s2)): continue
            ph = dec(code(s2, C0), s1['r']); tot += p1 * p2; hit += p1 * p2 * (ph is not None and act(ph) == act(PH(s2)))
        res['S1c directional substitution rate'] = hit / tot; ok['S1c directional substitution rate'] = hit == tot
        gM = defaultdict(lambda: [F(0), F(0)])
        for pr, s in S: a = gM[code(s, C0)]; a[0] += pr; a[1] += pr * s['L']
        decM = lambda m: gM[m][1] / gM[m][0]
        tx = sum(pr for pr, s in S if (s['o'], s['T'], s['fhat'], 1 - s['r']) in part
                 and act(decM(code(s, C0))) != act(decM(code(part[(s['o'], s['T'], s['fhat'], 1 - s['r'])], C0))))
        res['S1d transplant action-change mass'] = tx; ok['S1d transplant action-change mass'] = tx > 0
        opts = [sum(pr * max(PH(s), 1 - PH(s), dp) for pr, s in S) for dp in dps]
        res["S1e binding d' (value, contract optimum)"] = [(float(dp), float(v), float(o)) for dp, v, o in zip(dps, vd, opts)]
        ok["S1e binding d' (value, contract optimum)"] = all(v == o for v, o in zip(vd, opts))
        mis = sum(pr for pr, s in S if dec(code(s, C0), s['r']) is not None and act(dec(code(s, C0), s['r'])) != act(oracle_phi(s)))
        res['S1f endogenous misrepresentation mass'] = mis; ok['S1f endogenous misrepresentation mass'] = mis > 0
        res['S1h relay value vs trace bound'] = (float(val), float(bound)); ok['S1h relay value vs trace bound'] = val > bound
        pairs = sep = 0
        for (_, s1), (_, s2) in combinations(S, 2):
            if s1['r'] != s2['r']: continue
            f1_, f2_ = PH(s1), PH(s2)
            if act(f1_) == act(f2_): continue
            a1, i1 = max(F(0), f2_ - f1_), max(F(0), f1_ - f2_); pairs += 1
            sep += code(s1, dict(ka=a1, ki=i1)) != code(s2, dict(ka=a1 + f1_ - f2_, ki=i1 + f2_ - f1_))
        res['S1h D11 separation'] = f"{sep}/{pairs}"; ok['S1h D11 separation'] = sep == pairs
        out[name] = (res, ok)
    return out

def f3(k=5):
    """P1c specificity: pairs of identities with the same anchor output f(00), matched (equal) reliability by design,
    and different f(11). Specificity = P(decoder predicts the pair member's own f(11) | that member) minus
    P(decoder predicts it | the other member), averaged over ordered pairs. > 0 means M supports different
    predictions where the mappings differ."""
    St = M.proc_states(k); res = {}
    for name, (lvl, code) in M.PROC.items():
        _, rule = M.linear_acc(St, code)
        p1 = defaultdict(lambda: [F(0), F(0)])        # wb -> [mass, mass predicting 1]
        for pr, blk, tr in St: a = p1[blk['wb']]; a[0] += pr; a[1] += pr * rule(M.enc(code(blk, tr)))
        P = {wb: v[1] / v[0] for wb, v in p1.items()}
        pairs = [(a, b) for a in M.FAM for b in M.FAM if a != b and M.fval(a, (0, 0)) == M.fval(b, (0, 0)) and M.fval(a, (1, 1)) != M.fval(b, (1, 1))]
        spec = sum(((P[a] if M.fval(a, (1, 1)) else 1 - P[a]) - (P[b] if M.fval(a, (1, 1)) else 1 - P[b])) for a, b in pairs) / len(pairs)
        res[name] = (len(pairs), spec)
    return res

if __name__ == '__main__':
    print("# E0-B Ledger F execution log\n\n## F1 S1e binding-payoff grid (relay value: phi code vs policy-bit W10)\n")
    print("| context | d' | phi code | W10 policy bit | phi advantage |")
    print("|---|---|---|---|---|")
    for tag, dp, a, b in f1(): print(f"| {tag} | {float(dp):.2f} | {float(a):.6f} | {float(b):.6f} | {float(a - b):+.6f} |")
    for k in (10, 40):
        print(f"\n## F2 Trace-compliant Shea matrix, k = {k}, S1e at d' = 0.75 / 0.80\n")
        for nm, (rs, oks) in f2(k).items():
            print(f"### {nm}: {'PASS' if all(oks.values()) else 'fail'}")
            for kk, v in rs.items(): print(f"- {kk}: {v if isinstance(v, (str, list, tuple)) else float(v)} -> {'ok' if oks[kk] else 'NOT MET'}")
            print()
    print("## F3 Process P1c specificity arm (k = 5; matched anchor f(00), matched reliability, different f(11))\n")
    print("| witness | eligible ordered pairs | specificity |")
    print("|---|---|---|")
    for nm, (n, sp) in f3().items(): print(f"| {nm} | {n} | {float(sp):+.6f} |")
