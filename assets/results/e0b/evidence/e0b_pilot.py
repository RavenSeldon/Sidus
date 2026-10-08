#!/usr/bin/env python3
"""E0-B learned pilot P0 (protocol: E0B_Pilot_Protocol_P0.md, committed by SHA-256 before running).
Pure numpy; float64. Usage: python3 e0b_pilot.py [shea|process|all] [n_seeds]"""
import sys, json, time
import numpy as np

P_X, QH, QL, D = 0.7, 0.95, 0.5, 0.55
OS = [(0, 0), (0, 1), (1, 0), (1, 1)]
FAM = [((0, 1), 0), ((0, 1), 1), ((1, 0), 0), ((1, 0), 1), ((1, 1), 0), ((1, 1), 1)]
TAB = np.array([[((w[0] * o[0] + w[1] * o[1]) + b) % 2 for o in OS] for (w, b) in FAM])
pS = P_X * (QH + QL) / 2 + (1 - P_X) * (1 - (QH + QL) / 2)
TRAIN_IDS = [1, 2, 3, 5]; HELDOUT_IDS = [4, 0]            # FAM indices: held-out ((1,1),0) and ((0,1),0)

# ------------------------------------------------------------------ tiny MLP with Adam (manual backprop)
class MLP:
    def __init__(self, nin, nout, rng, h=32):
        self.W1 = rng.normal(0, 1 / np.sqrt(nin), (nin, h)); self.b1 = np.zeros(h)
        self.W2 = rng.normal(0, 1 / np.sqrt(h), (h, nout)); self.b2 = np.zeros(nout)
        self.p = ['W1', 'b1', 'W2', 'b2']; self.m = {k: 0 for k in self.p}; self.v = {k: 0 for k in self.p}; self.t = 0
    def fwd(self, X):
        self.X = X; self.H = np.tanh(X @ self.W1 + self.b1); return self.H @ self.W2 + self.b2
    def bwd(self, G):
        self.g = {'W2': self.H.T @ G, 'b2': G.sum(0)}
        GH = (G @ self.W2.T) * (1 - self.H ** 2)
        self.g['W1'] = self.X.T @ GH; self.g['b1'] = GH.sum(0); return GH @ self.W1.T
    def step(self, lr=3e-3, b1=0.9, b2=0.999):
        self.t += 1
        for k in self.p:
            self.m[k] = b1 * self.m[k] + (1 - b1) * self.g[k]; self.v[k] = b2 * self.v[k] + (1 - b2) * self.g[k] ** 2
            mh = self.m[k] / (1 - b1 ** self.t); vh = self.v[k] / (1 - b2 ** self.t)
            setattr(self, k, getattr(self, k) - lr * mh / (np.sqrt(vh) + 1e-8))

def phi_cf(r, f, T, p=P_X):
    q = np.where(T == 0, QH, QL); s = r ^ f
    px_s = np.where(s == 1, p, 1 - p); pn0 = px_s * q / (px_s * q + (1 - px_s) * (1 - q))
    return np.where(f == 0, pn0, 1 - pn0)

# ------------------------------------------------------------------ Shea-arm sampler (k traces per input, balanced)
def sample_shea(n, rng, k=40):
    wb = rng.integers(0, 6, n); f_all = TAB[wb]
    cnt = rng.binomial(k, np.where(f_all == 0, pS, 1 - pS))
    ll = np.stack([np.where(TAB[v] == 0, cnt * np.log(pS) + (k - cnt) * np.log(1 - pS),
                            cnt * np.log(1 - pS) + (k - cnt) * np.log(pS)).sum(1) for v in range(6)], 1)
    post = np.exp(ll - ll.max(1, keepdims=True)); post /= post.sum(1, keepdims=True)
    m1_all = post @ TAB
    x = (rng.random(n) < P_X).astype(int); z1 = rng.integers(0, 2, n); z2 = rng.integers(0, 2, n); T = z1 ^ z2
    q = np.where(T == 0, QH, QL); nn = (rng.random(n) >= q).astype(int); o = rng.integers(0, 4, n)
    f = f_all[np.arange(n), o]; r = x ^ nn ^ f; L = (r == x).astype(float); m1 = m1_all[np.arange(n), o]
    s1 = P_X * q + (1 - P_X) * (1 - q)                          # P(R=1 | f=0, T)
    l1 = np.where(r == 1, 1 - s1, s1); l0 = np.where(r == 1, s1, 1 - s1)
    w = m1 * l1 / (m1 * l1 + (1 - m1) * l0)                     # P(f(o)=1 | counts, R, T)
    phip = (1 - w) * phi_cf(r, np.zeros(n, int), T) + w * phi_cf(r, np.ones(n, int), T)
    ka, ki, kd = rng.random(n), rng.random(n), rng.random(n)
    return dict(o=o, r=r, T=T, m1=m1, L=L, phip=phip, ka=ka, ki=ki, kd=kd)

def enc_in(b, ka=None, ki=None, kd=None):
    ka = b['ka'] if ka is None else ka; ki = b['ki'] if ki is None else ki; kd = b['kd'] if kd is None else kd
    return np.c_[np.eye(4)[b['o']], b['r'], b['T'], b['m1'], ka, ki, kd]

def acc_pay(b): return np.stack([b['L'] + b['ka'], 1 - b['L'] + b['ki'], D + b['kd']], 1)
def relay_pay(b, d=D): return np.stack([b['L'], 1 - b['L'], np.full_like(b['L'], d)], 1)

def softmax(Z): Z = Z - Z.max(1, keepdims=True); E = np.exp(Z); return E / E.sum(1, keepdims=True)

def train_system(kind, seed, steps=4000, bs=1024):
    rng = np.random.default_rng(seed); dout = {'C-end': 1, 'C-sup': 1, 'R-vec': 2, 'R-acc': 1, 'B0-am': 4}[kind]
    E = MLP(10, dout, rng); Cn = MLP(dout + 4, 3, rng) if kind in ('C-end', 'B0-am') else None
    for t in range(steps):
        b = sample_shea(bs, rng); M = E.fwd(enc_in(b))
        if kind in ('C-end', 'B0-am'):
            Z = Cn.fwd(np.c_[M, b['r'], b['ka'], b['ki'], b['kd']]); Pi = softmax(Z); Pay = acc_pay(b)
            G = -Pi * (Pay - (Pi * Pay).sum(1, keepdims=True)) / bs
            GM = Cn.bwd(G)[:, :dout]; E.bwd(GM); Cn.step(); E.step()
        elif kind == 'C-sup':
            p = 1 / (1 + np.exp(-M[:, 0])); E.bwd(((p - b['L']) / bs)[:, None]); E.step()
        elif kind == 'R-vec':
            Y = np.c_[b['L'] + b['ka'], 1 - b['L'] + b['ki']]; E.bwd(2 * (M - Y) / bs); E.step()
        else:
            Y = (b['L'] + b['ka'])[:, None]; E.bwd(2 * (M - Y) / bs); E.step()
    def code(b, ka=None, ki=None, kd=None):
        M = E.fwd(enc_in(b, ka, ki, kd))
        return (1 / (1 + np.exp(-M))) if kind == 'C-sup' else M
    return code

# ------------------------------------------------------------------ relay fitting and measures
def fit_policy(M, r, pay, rng, nbins=40):
    """returns a policy function (M, r) -> action, fit on (M, r, pay)."""
    d = M.shape[1]
    if d <= 2:
        nb = nbins if d == 1 else 20
        edges = [np.quantile(M[:, j], np.linspace(0, 1, nb + 1)[1:-1]) for j in range(d)]
        def key(Mx, rx):
            idx = np.zeros(len(rx), int)
            for j in range(d): idx = idx * nb + np.searchsorted(edges[j], Mx[:, j])
            return idx * 2 + rx
        K = key(M, r); nk = (nb ** d) * 2
        S = np.zeros((nk, 3)); np.add.at(S, K, pay)
        best = S.argmax(1); fallback = pay.sum(0).argmax(); best[(S == 0).all(1)] = fallback
        return lambda Mx, rx: best[key(Mx, rx)]
    # MLP relay with 3 restarts for d > 2
    bestf, bestv = None, -1
    X = np.c_[M, r]; mu, sd = X.mean(0), X.std(0) + 1e-9
    for rs in range(3):
        net = MLP(d + 1, 3, np.random.default_rng(rng.integers(1 << 30)))
        for t in range(1500):
            ix = rng.integers(0, len(r), 1024); Pi = softmax(net.fwd((X[ix] - mu) / sd)); P = pay[ix]
            net.bwd(-Pi * (P - (Pi * P).sum(1, keepdims=True)) / 1024); net.step()
        pol = lambda Mx, rx, net=net: net.fwd((np.c_[Mx, rx] - mu) / sd).argmax(1)
        v = pay[np.arange(len(r)), pol(M, r)].mean()
        if v > bestv: bestv, bestf = v, pol
    return bestf

def fit_regressor(M, r, L, rng, nbins=40):
    d = M.shape[1]
    if d <= 2:
        nb = nbins if d == 1 else 20
        edges = [np.quantile(M[:, j], np.linspace(0, 1, nb + 1)[1:-1]) for j in range(d)]
        def key(Mx, rx):
            idx = np.zeros(len(rx), int)
            for j in range(d): idx = idx * nb + np.searchsorted(edges[j], Mx[:, j])
            return idx * 2 + rx
        K = key(M, r); nk = (nb ** d) * 2; s = np.bincount(K, L, nk); c = np.bincount(K, None, nk)
        mean = np.where(c > 0, s / np.maximum(c, 1), L.mean())
        return lambda Mx, rx: mean[key(Mx, rx)]
    X = np.c_[M, r]; mu, sd = X.mean(0), X.std(0) + 1e-9; net = MLP(d + 1, 1, rng)
    for t in range(2000):
        ix = rng.integers(0, len(r), 1024); p = 1 / (1 + np.exp(-net.fwd((X[ix] - mu) / sd)[:, 0]))
        net.bwd(((p - L[ix]) / 1024)[:, None]); net.step()
    return lambda Mx, rx: 1 / (1 + np.exp(-net.fwd((np.c_[Mx, rx] - mu) / sd)[:, 0]))

def evaluate(code, seed, n=100000):
    rng = np.random.default_rng(9000 + seed)
    fit, test = sample_shea(n, rng), sample_shea(n, rng)
    Mf, Mt = code(fit), code(test)
    Mf = Mf.reshape(len(fit['r']), -1); Mt = Mt.reshape(len(test['r']), -1)
    out = {}
    pol = fit_policy(Mf, fit['r'], relay_pay(fit), rng)
    a = pol(Mt, test['r']); out['E1_relay'] = float(relay_pay(test)[np.arange(n), a].mean())
    out['E1_relay_per_trial'] = relay_pay(test)[np.arange(n), a]
    reg = fit_regressor(Mf, fit['r'], fit['L'], rng); out['E2_calib_excess'] = float(((reg(Mt, test['r']) - test['phip']) ** 2).mean())
    Mk = code(test, ka=rng.random(n), ki=rng.random(n), kd=rng.random(n)).reshape(n, -1)
    out['E3_kappa_sens'] = float(np.linalg.norm(Mk - Mt, axis=1).mean() / (Mt.std(0).mean() + 1e-12))
    # E4 designed D11 pairs: partner = random test trial with same R and different phi_post-optimal action
    act = lambda ph: np.argmax(np.stack([ph, 1 - ph, np.full_like(ph, D)], 1), 1)
    aopt = act(test['phip']); perm = rng.permutation(n)
    elig = (test['r'] == test['r'][perm]) & (aopt != aopt[perm]); i1 = np.where(elig)[0][:20000]; i2 = perm[i1]
    f1, f2 = test['phip'][i1], test['phip'][i2]
    a1 = np.maximum(0, f2 - f1); c1 = np.maximum(0, f1 - f2)
    sub = lambda idx: {k_: v[idx] for k_, v in test.items()}
    M1 = code(sub(i1), ka=a1, ki=c1).reshape(len(i1), -1); M2 = code(sub(i2), ka=a1 + f1 - f2, ki=c1 + f2 - f1).reshape(len(i1), -1)
    ok = (pol(M1, test['r'][i1]) == aopt[i1]) & (pol(M2, test['r'][i2]) == aopt[i2])
    out['E4_D11_agreement'] = float(ok.mean())
    for dp in (0.75, 0.80):
        polp = fit_policy(Mf, fit['r'], relay_pay(fit, dp), rng)
        v = relay_pay(test, dp)[np.arange(n), polp(Mt, test['r'])].mean()
        ideal = np.maximum(np.maximum(test['phip'], 1 - test['phip']), dp)
        realized_ideal = relay_pay(test, dp)[np.arange(n), np.argmax(np.stack([test['phip'], 1 - test['phip'], np.full(n, dp)], 1), 1)].mean()
        out[f'E5_S1e_gap_{dp}'] = float(realized_ideal - v)
    ideal_a = act(test['phip']); out['ideal_relay'] = float(relay_pay(test)[np.arange(n), ideal_a].mean())
    out['ideal_per_trial'] = relay_pay(test)[np.arange(n), ideal_a]
    return out

# ------------------------------------------------------------------ Process arm
def sample_proc(n, rng, ids, kp=20):
    wb = rng.choice(ids, n); f = TAB[wb]; cnt = rng.binomial(kp, np.where(f[:, :3] == 0, pS, 1 - pS))
    ll = np.stack([np.where(TAB[v, :3] == 0, cnt * np.log(pS) + (kp - cnt) * np.log(1 - pS),
                            cnt * np.log(1 - pS) + (kp - cnt) * np.log(pS)).sum(1) for v in range(6)], 1)
    post = np.exp(ll - ll.max(1, keepdims=True)); post /= post.sum(1, keepdims=True)
    bayes = post @ TAB[:, 3]
    bits = np.where(2 * cnt > kp, 0, np.where(2 * cnt < kp, 1, 0.5))
    return dict(cnt=cnt / kp, bits=bits, y=f[:, 3].astype(float), bayes=bayes)

def train_proc(kind, seed, steps=3000, bs=512):
    rng = np.random.default_rng(seed)
    net = MLP(3, 1, rng, h=32) if kind != 'P-cell-lin' else None
    W = np.zeros(4) if kind == 'P-cell-lin' else None
    m = v = 0; t_ = 0
    for t in range(steps):
        b = sample_proc(bs, rng, TRAIN_IDS); X = b['cnt'] if kind == 'P-struct' else b['bits']
        if kind == 'P-cell-lin':
            Xa = np.c_[X, np.ones(bs)]; p = 1 / (1 + np.exp(-(Xa @ W))); g = Xa.T @ (p - b['y']) / bs
            t_ += 1; m = 0.9 * m + 0.1 * g; v = 0.999 * v + 0.001 * g ** 2
            W -= 3e-3 * (m / (1 - 0.9 ** t_)) / (np.sqrt(v / (1 - 0.999 ** t_)) + 1e-8)
        else:
            p = 1 / (1 + np.exp(-net.fwd(X)[:, 0])); net.bwd(((p - b['y']) / bs)[:, None]); net.step()
    if kind == 'P-cell-lin': return lambda b: (np.c_[b['bits'], np.ones(len(b['y']))] @ W) > 0
    return lambda b: net.fwd(b['cnt'] if kind == 'P-struct' else b['bits'])[:, 0] > 0

if __name__ == '__main__':
    which = sys.argv[1] if len(sys.argv) > 1 else 'all'; nseeds = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    seeds = list(range(1, nseeds + 1)); res = {}
    if which in ('shea', 'all'):
        for kind in ('C-end', 'C-sup', 'R-vec', 'R-acc', 'B0-am'):
            for s in seeds:
                t0 = time.time(); code = train_system(kind, s); ev = evaluate(code, s)
                pt = ev.pop('E1_relay_per_trial'); it = ev.pop('ideal_per_trial')
                np.save(f'pilot_trials_{kind}_{s}.npy', np.stack([pt, it]))
                res[f'{kind}|{s}'] = ev
                print(kind, s, {k_: round(v_, 6) for k_, v_ in ev.items()}, f'{time.time() - t0:.0f}s', flush=True)
        json.dump(res, open('pilot_shea_results.json', 'w'), indent=1)
    if which in ('process', 'all'):
        pres = {}
        rng = np.random.default_rng(424242); ho = sample_proc(400000, rng, HELDOUT_IDS)
        pres['bayes_identity_blind_heldout'] = float(np.where(ho['bayes'] == 0.5, 0.5, ((ho['bayes'] > 0.5) == (ho['y'] == 1))).mean())
        for kind in ('P-struct', 'P-cell-lin', 'P-cell-mlp'):
            for s in seeds:
                pred = train_proc(kind, s); acc = float((pred(ho) == (ho['y'] == 1)).mean())
                pres[f'{kind}|{s}'] = acc; print(kind, s, round(acc, 6), flush=True)
        print('identity-blind Bayes (held-out, MC):', round(pres['bayes_identity_blind_heldout'], 6))
        json.dump(pres, open('pilot_process_results.json', 'w'), indent=1)
