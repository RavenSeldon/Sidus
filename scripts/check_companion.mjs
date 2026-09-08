import fs from 'node:fs';import vm from 'node:vm';import path from 'node:path';import {fileURLToPath} from 'node:url';import assert from 'node:assert/strict';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..'),read=p=>fs.readFileSync(path.join(root,p),'utf8'),ctx={window:{}};vm.createContext(ctx);
for(const p of ['assets/results/e0a-data.js','assets/results/e0a.js'])vm.runInContext(read(p),ctx);
const escape=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
let count=0;
for(const m of read('e0a.html').matchAll(/<span data-value="([^"]+)" data-format="([^"]+)">([^<]*)<\/span>/g)){
 const x=m[1].split('.').reduce((x,k)=>x[k],ctx.window.SIDUS_E0A), f=m[2];
 const expected=typeof x!=='number'?escape(x):f==='exact'?String(x):f==='percent'?new Intl.NumberFormat('en',{maximumFractionDigits:1}).format(x*100)+'%':new Intl.NumberFormat('en',{maximumFractionDigits:4}).format(Math.abs(x)<.00005?0:x);
 assert.equal(m[3],expected,m[1]);count++;
}
assert.equal(count>4000,true);
const standalone=read('Sidus_Dossier_Standalone.html');for(const marker of ['window.SIDUS_E0A=','window.SIDUS_RESULTS=','const DATA='])assert.equal(standalone.split(marker).length-1,1,marker);
const app=read('assets/app.js');assert(app.includes("if(r[0]==='results')"));assert(app.includes('SIDUS_RESULTS.search'));assert(app.includes('di===3?'));
console.log(`PASS: ${count} rendered values match emitted data and formatting; routes, search, reader hook and standalone scripts present.`);
