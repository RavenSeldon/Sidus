#!/usr/bin/env python3
"""E0-B Ledger D-II checks (exact rational arithmetic; imports e0b_contracts.py).

E1  B1-invert-value under R2.3: M = 1 - phi is an invertible relabel of phi -> identical relay value.
E2  R2.3 acceptance references: full-information optimum and public-only optimum (consumer sees kappa).
E3  R2.4 candidate: independent hidden payoff contexts on EVERY action
      accept pays L + ka, invert pays (1-L) + ki, defer pays d + kd;  ka, ki, kd ~ U[0,1] independent,
      visible to encoders and the acceptance consumer, hidden from the relay (which observes M and R).
    Rivals: scalar Q_accept = phi + ka; scalar Q_invert = 1 - phi + ki; the vector (Q_accept, Q_invert).
    Q_defer = d + kd carries no phi information and is omitted. Piecewise-exact (1-D and 2-D) integration.
"""
from fractions import Fraction as F
from collections import defaultdict
import e0b_contracts as C
D = C.D
def atoms(k):
    S = [(pr, s) for pr, s in C.states(F(0), k=k) if s['kappa'] == 0]
    ph = C.encode(S, 'L', C.ENC_BASE if k is None else C.ENC_TRACE); A = defaultdict(lambda: [F(0), F(0)])
    for pr, s in S: a = A[(s['r'], ph(s))]; a[0] += 2 * pr; a[1] += 2 * pr * s['L']
    return dict(A)
pay = lambda m, c: (c, m - c, D * m)
def phi_relay(A):
    return sum(max(pay(m, c)) for (r, f), (m, c) in A.items())
def inv_relay(A):                       # code 1 - phi: group by the code value instead of phi
    g = defaultdict(lambda: [F(0), F(0)])
    for (r, f), (m, c) in A.items(): a = g[(r, 1 - f)]; a[0] += m; a[1] += c
    return sum(max(pay(m, c)) for m, c in g.values())
def relay_1d(A, shift):                 # M = shift(phi) + U[0,1]
    items = [(r, shift(f), m, c) for (r, f), (m, c) in A.items()]
    bps = sorted({s for _, s, _, _ in items} | {s + 1 for _, s, _, _ in items}); v = F(0)
    for lo, hi in zip(bps, bps[1:]):
        mid = (lo + hi) / 2
        for r in (0, 1):
            live = [(m, c) for rr, s, m, c in items if rr == r and s <= mid <= s + 1]
            if live: v += (hi - lo) * max(sum(pay(m, c)[j] for m, c in live) for j in range(3))
    return v
def relay_2d(A):                        # M = (phi + ka, 1 - phi + ki)
    items = [(r, f, 1 - f, m, c) for (r, f), (m, c) in A.items()]
    bx = sorted({a for _, a, _, _, _ in items} | {a + 1 for _, a, _, _, _ in items})
    by = sorted({b for _, _, b, _, _ in items} | {b + 1 for _, _, b, _, _ in items}); v = F(0)
    for x0, x1 in zip(bx, bx[1:]):
        mx = (x0 + x1) / 2
        for y0, y1 in zip(by, by[1:]):
            my = (y0 + y1) / 2
            for r in (0, 1):
                live = [(m, c) for rr, a, b, m, c in items if rr == r and a <= mx <= a + 1 and b <= my <= b + 1]
                if live: v += (x1 - x0) * (y1 - y0) * max(sum(pay(m, c)[j] for m, c in live) for j in range(3))
    return v
def acc_ref(A):                         # E_kappa max(phi + kappa, 1 - phi, d), consumer knows phi and kappa
    v = F(0)
    for (r, f), (m, c) in A.items():
        phi = c / m; t = max(1 - phi, D)          # accept iff phi + kappa >= t
        cut = min(max(t - phi, F(0)), F(1))
        v += m * (t * cut + ((1 - cut) * phi + (1 - cut * cut) / 2))
    return v

def emax(shifts):
    """E[max_i (U_i + s_i)] for iid U_i ~ U[0,1], exact piecewise-polynomial integration."""
    L = max(shifts); pts = sorted({L, L + 1} | {s + 1 for s in shifts if L < s + 1 < L + 1}); total = F(0)
    for a, b in zip(pts, pts[1:]):
        poly = [F(1)]; mid = (a + b) / 2
        for s in shifts:
            if mid >= s + 1: continue
            poly = [(poly[i-1] if i > 0 else 0) + (poly[i] * (-s) if i < len(poly) else 0) for i in range(len(poly) + 1)]
        integ = lambda t: sum(c * t**(i + 1) / (i + 1) for i, c in enumerate(poly))
        total += (b - a) - (integ(b) - integ(a))
    return L + total
def acc_ref_r24(A):   # E4: R2.4 acceptance optimum E[max(phi+ka, 1-phi+ki, d+kd)]
    return sum(m * emax([c / m, 1 - c / m, D]) for (r, f), (m, c) in A.items())

if __name__ == '__main__':
    for tag, k in (('mapping oracle', None), ('k=40 traces (marginal MAP)', 40)):
        A = atoms(k)
        print(f"\n[{tag}]")
        print(f"  E1 relay (M,R): phi {float(phi_relay(A)):.6f}   B1-invert-value 1-phi {float(inv_relay(A)):.6f}")
        print(f"  E2 R2.3 acceptance optimum (full info incl. kappa) {acc_ref(A)} = {float(acc_ref(A)):.6f}")
        print(f"  E3 R2.4 relay (M,R): phi {float(phi_relay(A)):.6f} | scalar Q_accept {float(relay_1d(A, lambda f: f)):.6f}"
              f" | scalar Q_invert {float(relay_1d(A, lambda f: 1 - f)):.6f} | vector (Q_accept,Q_invert) {float(relay_2d(A)):.6f}")
    # public-only acceptance reference (consumer sees o, R, kappa; mapping unknown)
    S = [(pr, s) for pr, s in C.states(F(0)) if s['kappa'] == 0]
    P = defaultdict(lambda: [F(0), F(0)])
    for pr, s in S: a = P[(s['o'], s['r'])]; a[0] += 2 * pr; a[1] += 2 * pr * s['L']
    print(f"\n  E2 public-only acceptance optimum (o, R, kappa) {float(acc_ref({k_: v for k_, v in P.items()})):.6f}")
    print("\n  E4 R2.4 acceptance optimum E[max(phi+ka, 1-phi+ki, d+kd)]:")
    print(f"     public (o,R) {float(acc_ref_r24(dict(P))):.6f} | k=40 {float(acc_ref_r24(atoms(40))):.6f} | oracle {acc_ref_r24(atoms(None))} = {float(acc_ref_r24(atoms(None))):.6f}")
