// Companion-only assembly: never invoke canonical document/PDF regeneration.
import fs from 'node:fs';
import {createHash} from 'node:crypto';
import vm from 'node:vm';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const read=p=>fs.readFileSync(path.join(root,p),'utf8');
const ctx={window:{}};vm.createContext(ctx);
for(const p of ['assets/results/e0a-data.js','assets/results/e0a.js'])vm.runInContext(read(p),ctx);
let body=ctx.window.SIDUS_RESULTS.html();
const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
// A real static reading surface, including every evidence source and seed row.
body=body.replace(/<div class="e-buttons"[\s\S]*?<\/div>/g,'');
body=body.replace(/<button[^>]*data-seed[^>]*>([\s\S]*?)<\/button>/g,'<span class="e-static-mark">$1</span>');
body=body.replace(/<button[^>]*data-copy-hash[^>]*>[\s\S]*?<\/button>/g,'');
body=body.replace(/href="#\/results\/e0-a\/scene-(\d)"/g,'href="#scene-$1"').replace(/href="#\//g,'href="index.html#/');
body=body.replace(/<details class="e-evidence" data-evidence="([^"]+)">[\s\S]*?<div class="e-evidence-body" aria-live="polite"><\/div><\/details>/g,(_,p)=>{
 const keys=ctx.window.SIDUS_E0A.provenance,key=Object.keys(keys).filter(k=>p===k||p.startsWith(k+'.')).sort((a,b)=>b.length-a.length)[0],v=JSON.parse(read(keys[key]));
 return `<details class="e-evidence"><summary>Inspect the evidence</summary><dl><dt>Displayed field</dt><dd>${esc(p)}</dd><dt>Archived source</dt><dd><a href="${esc(v.artifact_link)}">${esc(v.source_file)}</a></dd><dt>Exact selector and aggregation</dt><dd><code>${esc(v.selector)}${p===key?'':' → '+esc(p.slice(key.length+1))}</code></dd><dt>Unit</dt><dd>${esc(v.unit)}</dd><dt>Population / denominator</dt><dd>${esc(v.population)}</dd><dt>Evidence stage</dt><dd>${esc(v.evidence_stage)}</dd></dl><a href="${keys[key]}">Complete transformation record</a></details>`;
});
fs.writeFileSync(path.join(root,'e0a.html'),`<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="dark"><title>Does the message matter? — Sīdus E0-A field report</title><link rel="stylesheet" href="assets/styles.css"><link rel="stylesheet" href="assets/results/e0a.css"><style>body:before{inset:0}main{margin:0 auto!important;max-width:1200px;padding:25px!important}.e-static-mark{height:26px;border:1px solid #858a80;text-align:center}.e-report .e-static-mark span{line-height:1}</style></head><body><main><p class="e-print-note"><a href="index.html#/results/e0-a">Open the interactive report</a> · Static reading edition · no scripts required</p>${body}</main></body></html>`);
let standalone=read('Sidus_Dossier_Standalone.html');
// Replace the live app only; retain original frozen document and Atlas scripts byte-for-byte.
standalone=standalone.replace(/<script>\s*const DATA=[\s\S]*?<\/script>/,()=>'<script>\n'+read('assets/app.js')+'\n</script>');
standalone=standalone.replace(/<!-- E0A COMPANION STYLE -->[\s\S]*?<!-- END E0A COMPANION STYLE -->\n?/g,'');
standalone=standalone.replace('</head>','<!-- E0A COMPANION STYLE --><style>'+read('assets/results/e0a.css')+'</style><!-- END E0A COMPANION STYLE -->\n</head>');
standalone=standalone.replace(/<!-- E0A COMPANION SCRIPTS -->[\s\S]*?<!-- END E0A COMPANION SCRIPTS -->\n?/g,'');
standalone=standalone.replace(/<script>\s*const DATA=/,()=>`<!-- E0A COMPANION SCRIPTS --><script>${read('assets/results/e0a-data.js')}</script><script>${read('assets/results/e0a.js')}</script><!-- END E0A COMPANION SCRIPTS -->\n<script>\nconst DATA=`);
fs.writeFileSync(path.join(root,'Sidus_Dossier_Standalone.html'),standalone);
console.log('Built static field report and synchronized standalone companion; canonical payload unchanged.');

const version=createHash('sha256').update(['index.html','assets/app.js','assets/results/e0a.css','assets/results/e0a.js','assets/results/e0a-data.js','e0a.html'].map(read).join('')).digest('hex').slice(0,12);
fs.writeFileSync(path.join(root,'sw.js'),read('sw.js').replace(/const CACHE='[^']+'/,`const CACHE='sidus-dossier-v6-e0a-${version}'`));
