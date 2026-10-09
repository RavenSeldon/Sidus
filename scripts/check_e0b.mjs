// Companion verification: archived identity, independently recomputed summaries,
// formula support, finite chart coordinates, links and offline integration.
import fs from 'node:fs';
import path from 'node:path';
import vm from 'node:vm';
import assert from 'node:assert/strict';
import {createHash} from 'node:crypto';
import {fileURLToPath} from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const read=p=>fs.readFileSync(path.join(root,p),'utf8');
const digest=p=>createHash('sha256').update(fs.readFileSync(path.join(root,p))).digest('hex');
const ctx={window:{}};vm.createContext(ctx);
for(const p of ['assets/results/e0b-data.js','assets/results/e0b.js'])vm.runInContext(read(p),ctx);
const D=ctx.window.SIDUS_E0B_DATA,B=ctx.window.SIDUS_E0B;
let checks=0;
const near=(a,b,e=1e-12)=>{assert.ok(Math.abs(a-b)<e,`${a} != ${b}`);checks++;};
assert.equal(digest(D.archive.href),D.archive.sha256);
for(const [name,s] of Object.entries(D.sources))assert.equal(digest(s.href),s.sha256,name);
const R=JSON.parse(read(D.sources['confirm_results.json'].href));
assert.equal(JSON.stringify(R),JSON.stringify(D.results));
assert.equal(JSON.stringify(JSON.parse(read(D.sources['confirm_adjudication.json'].href))),JSON.stringify(D.adjudication));
for(const s of Object.keys(D.stats))for(const m of Object.keys(D.stats[s])){
 const v=D.spec.confirmation_seeds.map(seed=>R[`${s}|${seed}`][m]);
 const mean=v.reduce((a,b)=>a+b,0)/v.length;
 near(D.stats[s][m].mean,mean);
 near(D.stats[s][m].sd,Math.sqrt(v.reduce((a,b)=>a+(b-mean)**2,0)/(v.length-1)));
}
const metrics=['calib_excess','kappa_R2','S1e_gap_0.75','S1e_gap_0.8','D11_agreement'];
for(let i=0;i<5;i++)near(D.adjudication.H1.rows[i][1],D.stats['C-sup'][metrics[i]].mean);
near(D.adjudication.H1.rows[5][1],D.profiles.reduce((a,p)=>a+p.relay_advantage,0)/20);
assert.equal(D.profiles.filter(p=>p.pass).length,14);
for(const p of D.profiles){
 const r=R[`C-sup|${p.seed}`],th=D.spec.thresholds;
 const pass=r.calib_excess<=th.thr_cal && r.kappa_R2<=th.thr_inv && r['S1e_gap_0.75']<=th['thr_s1e_0.75'] && r['S1e_gap_0.8']<=th['thr_s1e_0.8'] && r.D11_agreement>=th.thr_d11 && r.relay-Math.max(R[`R-vec|${p.seed}`].relay,R[`R-acc|${p.seed}`].relay)>th.relay_margin;
 assert.equal(p.pass,pass);
}
// Enumerate the latent binary state and noise instead of reusing Bayes' formula.
let oracleValue=0;
for(const t of [0,1])for(const flip of [0,1])for(const report of [0,1]){
 let correct=0,total=0;const q=t===0?.95:.5;
 for(const x of [0,1])for(const n of [0,1])if((x^n^flip)===report){
  const mass=(x?.7:.3)*(n?1-q:q);total+=mass;if(x===report)correct+=mass;
 }
 const p=B.math.phi(report,t,flip);near(p,correct/total);
 oracleValue+=.25*total*Math.max(p,1-p,.55);
}
near(oracleValue,.825);
const pairs=B.math.pairValues(0);for(const r of pairs)assert.ok(r.k.every(v=>v>=0&&v<=1));
for(let i=0;i<3;i++)near(B.math.values(pairs[0].p,pairs[0].k)[i],B.math.values(pairs[1].p,pairs[1].k)[i]);
assert.notEqual(B.math.best(B.math.values(pairs[0].p)),B.math.best(B.math.values(pairs[1].p)));
assert.equal(B.math.pairValues(1)[0].p,B.math.pairValues(1)[1].p);
const log=read(D.sources['ledgerF_output.md'].href);
for(const [k,rows] of Object.entries(D.witnesses)){
 const slice=log.split(`## F2 Trace-compliant Shea matrix, k = ${k},`)[1].split('\n## ')[0];
 for(const r of rows)for(const c of r.clauses)assert.ok(slice.includes(`- ${c.label}: ${c.value} -> ${c.pass?'ok':'NOT MET'}`));
 assert.equal(rows.filter(r=>r.pass).length,1);
 assert.equal(rows[1].clauses[8].pass,true);assert.equal(rows[1].clauses[5].pass,false);
}
for(const r of D.noise)near(+r[2]-(+r[5]),+r[6],1.1e-6);
for(const r of D.capacity)near(+r[2]-(+r[3]),+r[4],1.1e-6);
assert.equal(D.trace.find(r=>r[0]==='80')[3],'not computed');
for(const metric of metrics.concat('relay')){
 const svg=B.views.chart(metric);assert.ok(!/NaN|Infinity|undefined/.test(svg));assert.equal((svg.match(/<circle /g)||[]).length,120);
}
let html=B.html();
assert.equal((html.match(/id="b-results"/g)||[]).length,1);
const ids=[...html.matchAll(/\bid="([^"]+)"/g)].map(x=>x[1]);assert.equal(new Set(ids).size,ids.length);
let links=0;
for(const href of [...html.matchAll(/href="([^"]+)"/g)].map(x=>x[1])){
 if(href.startsWith('#/')||href.startsWith('https:'))continue;
 if(href.startsWith('#')){assert.ok(ids.includes(href.slice(1)));continue;}
 const p=path.join(root,href.split('#')[0]);assert.ok(fs.existsSync(p),href);links++;
}
for(const asset of ['e0b-data.js','e0b.js','e0b.css']){
 assert.ok(read('index.html').includes(`assets/results/${asset}`));assert.ok(read('sw.js').includes(`./assets/results/${asset}`));
}
assert.ok(!/ASSETS=\[[^\]]*(?:research\/|\.zip|Sidus_E0B_Research_Paper)/.test(read('sw.js')));
const standalone=read('Sidus_Dossier_Standalone.html');
for(const marker of ['window.SIDUS_E0B_DATA=','window.SIDUS_E0B ='])assert.equal(standalone.split(marker).length-1,1);
assert.ok(standalone.includes(read('assets/app.js')));
// Completion pass: cross-criteria grid, access contract, profile plane, paper anchors.
const ledE=read(D.sources['ledgerE_output.md'].href);
for(const row of ['| W1 regime code (theta-coupled) | 0.806250 | 0.825000 | +0.018750 |','| W2 fixed parity | 0.806250 | 0.825000 | +0.018750 |','| same-target feature learner | 0.806250 | 0.825000 | +0.018750 |','| shuffled parity (matched support) | 0.806250 | 0.806250 | +0.000000 |',
 '| W3 process model (truth table) | 0.596178 | 0.500000 | 0.596178 |','| W5 token-phi monitor | 0.517643 | 0.500000 | 0.517643 |','| W6a per-cell tracker | 0.591577 | 0.500000 | 0.591577 |','| W1 regime code (theta-coupled) | 0.500000 | 0.500000 | 0.500000 |','| W2 input parity (fixed) | 0.500000 | 0.500000 | 0.500000 |'])assert.ok(ledE.includes(row),row);
for(const id of ['shea','rr','process']){
 const t=B.views.crossTable(id);assert.equal((t.match(/b-active/g)||[]).length,7);
 assert.equal((t.match(/profile met/g)||[]).length,1);assert.ok(t.includes('9/9 clauses · profile met'));
 for(const v of ['+0.018750','0.596178','0.591577','0.517643'])assert.ok(t.includes(v));
}
const access=B.views.accessTable();assert.equal((access.match(/<tr>/g)||[]).length,7);assert.ok(access.includes('posterior'));
for(const s of ['IDEAL','C-sup','B0-am']){const svg=B.views.profile(s);assert.ok(!/NaN|Infinity|undefined/.test(svg));assert.equal((svg.match(/<circle /g)||[]).length,120);}
const pages=[...B.html().matchAll(/#page=(\d+)/g)].map(m=>+m[1]);assert.ok(pages.length>=8&&pages.every(n=>n>=1&&n<=12));
// Research-record landing page: recomputed seed counts, archive hash and local links.
const landing=read('research/e0-b/index.html'),seedsC=D.spec.confirmation_seeds,thr=D.spec.thresholds;
const h2n=seedsC.filter(s=>R[`C-end|${s}`].D11_agreement<=.2&&R[`C-end|${s}`].kappa_sens>=.25).length;
const h3n=seedsC.filter(s=>R[`B0-am|${s}`].D11_agreement>=.3&&R[`B0-am|${s}`].kappa_R2>=thr.thr_ret).length;
for(const [n,id] of [[D.profiles.filter(p=>p.pass).length,'H1'],[h2n,'H2'],[h3n,'H3']])assert.ok(new RegExp(`${id} ·[^<]*</th><td>Confirmed[^<]*</td><td>${n} / 20<`).test(landing),id);
for(const id of ['H1','H2','H3'])assert.equal(D.adjudication[id].verdict,'confirmed');
assert.ok(landing.includes(D.archive.sha256));
for(const href of [...landing.matchAll(/href="([^"]+)"/g)].map(x=>x[1])){
 if(/^(https?:|mailto:|\/#\/)/.test(href))continue;const t=path.join(root,href.replace(/^\//,'').split('#')[0]);
 assert.ok(fs.existsSync(t)&&(fs.statSync(t).isFile()||fs.existsSync(path.join(t,'index.html'))),href);
}
assert.ok(read('research/index.html').includes('href="/research/e0-b/"'));
console.log(`PASS E0-B: ${checks} numeric comparisons; 120 archived records, 108 witness cells, 14/20 profiles; formula enumeration and D11 support; six charts; ${links} local links; standalone and service-worker integration; cross-criteria grid, access contract, profile plane, ${pages.length} paper anchors; research-record page (H1 14, H2 ${h2n}, H3 ${h3n} of 20).`);
