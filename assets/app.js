
const DATA=window.SIDUS_DATA, ATLAS=window.SIDUS_ATLAS;
const app=document.getElementById('app'),rail=document.getElementById('rail'),railNav=document.getElementById('railNav');
const esc=s=>String(s).replace(/[&<>\"']/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','\"':'&quot;',"'":'&#039;'}[m]));
const route=()=>location.hash.replace(/^#\/?/,'').split('/').filter(Boolean);
function primerBody(p){
  const template=document.createElement('template');template.innerHTML=p.html;
  const first=template.content.firstElementChild;
  if(first?.tagName==='H1'&&first.textContent.trim()===p.title.trim())first.remove();
  return template.innerHTML;
}
function searchableText(html){
  const template=document.createElement('template');template.innerHTML=html;
  template.content.querySelectorAll('annotation').forEach(el=>el.remove());
  template.content.querySelectorAll('p,h1,h2,h3,h4,li,tr,th,td,blockquote').forEach(el=>el.append(' '));
  return template.content.textContent.replace(/\s+/g,' ').trim();
}
const topActive=(name)=>document.querySelectorAll('.topnav a,.mobile-tabs a').forEach(a=>a.classList.toggle('active',(a.getAttribute('href')||'').includes('/'+name)||((name==='home')&&a.getAttribute('href')==='#/home')));
function setRail(html){railNav.innerHTML=`<div class="rail-group">Navigate</div><a href="#/results">Results</a>`+html}
function focusApp(){setTimeout(()=>app.focus({preventScroll:true}),0)}
function openMenu(){const on=!rail.classList.contains('open');rail.classList.toggle('open',on);document.getElementById('menuBtn').setAttribute('aria-expanded',on)}
function closeMenu(){rail.classList.remove('open');document.getElementById('menuBtn').setAttribute('aria-expanded','false')}
document.getElementById('menuBtn').onclick=openMenu;
rail.addEventListener('click',e=>{if(e.target.closest('a'))closeMenu()});

function home(){topActive('home');setRail(`<div class="rail-group">Dossier</div><a href="#/home" class="active">Opening</a><a href="#/primer">For Dummies</a><a href="#/atlas">Visual atlas</a><div class="rail-group">Documents</div>${DATA.docs.map((d,i)=>`<a href="#/document/${i}/frontpiece">${d.roman}. ${esc(d.short)}</a>`).join('')}`);
app.innerHTML=`<div class="content-wide"><section class="hero"><div class="hero-copy"><div class="hero-kicker">A research programme in bounded self-monitoring</div><h1 class="display">Sīdus<span style="color:var(--gold)">:</span><br><em>Towards<br><span class="longword">Metarepresentational</span><br>Ecology</em></h1><p class="lede">What happens when a cognitive system cannot inspect all of itself at once?</p><div class="hero-actions"><a class="btn primary" href="#/primer">Begin with the plain-language map</a><a class="btn" href="#/document/0/frontpiece">Read the documents</a><a class="btn" href="#/atlas">Open the atlas</a></div></div></section>
${window.SIDUS_RESULTS.panel()}<div class="route-line"></div><section><div class="eyebrow">The central move</div><div class="question-panel">Do internal monitoring and metarepresentational systems exhibit reproducible relational principles—scarcity, causal topology, recursive control, fidelity constraints, complementarity or substitution—that generalize beyond a single task or architecture?</div><div class="metric-strip"><div class="metric"><b>4</b><span>documents</span></div><div class="metric"><b>E0→E6</b><span>experimental ladder</span></div><div class="metric"><b>r ≠ m</b><span>load-bearing distinction</span></div><div class="metric"><b>local → general</b><span>inference order</span></div></div></section>
<section><div class="eyebrow">The package</div><div class="doc-grid">${DATA.docs.map((d,i)=>`<a class="doc-card" href="#/document/${i}/frontpiece"><div class="roman">${d.roman}</div><h3>${esc(d.short)}</h3><p>${esc(d.title.replace(/^I+V?\.\s*/,''))}</p></a>`).join('')}</div></section></div>`;focusApp()}

function docReader(di,sid){di=Math.max(0,Math.min(DATA.docs.length-1,Number(di)||0));const d=DATA.docs[di];let si=d.sections.findIndex(s=>s.id===sid);if(si<0)si=0;const s=d.sections[si];topActive('document');
let nav=`<div class="rail-group">${d.roman}. ${esc(d.short)}</div>`;let lastPart='';d.sections.forEach((x,i)=>{if(x.part&&x.part!==lastPart){lastPart=x.part;nav+=`<div class="rail-group">${esc(lastPart)}</div>`}nav+=`<a class="${i===si?'active':''}" href="#/document/${di}/${x.id}">${esc(x.title)}</a>`});nav+=`<div class="rail-group">Other documents</div>${DATA.docs.filter((_,i)=>i!==di).map((x,i2)=>{let actual=DATA.docs.indexOf(x);return `<a href="#/document/${actual}/frontpiece">${x.roman}. ${esc(x.short)}</a>`}).join('')}`;setRail(nav);
const prev=si>0?d.sections[si-1]:di>0?DATA.docs[di-1].sections.at(-1):null;const next=si<d.sections.length-1?d.sections[si+1]:di<DATA.docs.length-1?DATA.docs[di+1].sections[0]:null;const prevHref=si>0?`#/document/${di}/${prev.id}`:di>0?`#/document/${di-1}/${prev.id}`:null;const nextHref=si<d.sections.length-1?`#/document/${di}/${next.id}`:di<DATA.docs.length-1?`#/document/${di+1}/${next.id}`:null;
app.innerHTML=`<div class="content-shell"><header class="reader-head"><div class="eyebrow">Document ${d.roman} · ${si+1} / ${d.sections.length}</div><h1>${esc(d.short)}</h1><div class="reader-meta"><span>${esc(s.title)}</span><a href="${d.sourcePdf}" target="_blank" rel="noopener">PDF ↗</a><a href="${d.sourceMd}" target="_blank" rel="noopener">Markdown ↗</a></div>${di===3?`<a class="e-related" href="#/results/e0-a">Related experimental result · 7 September 2026 · E0-A field report →</a>`:''}<div class="progress"><i style="width:${((si+1)/d.sections.length)*100}%"></i></div></header>${s.part?`<div class="part-stamp">${esc(s.part)}</div>`:''}<article class="doc-content">${s.html}</article><nav class="doc-nav">${prevHref?`<a href="${prevHref}">← ${esc(prev.title)}</a>`:'<span></span>'}${nextHref?`<a href="${nextHref}">${esc(next.title)} →</a>`:''}</nav></div>`;window.scrollTo(0,0);focusApp();}

function primer(pid){topActive('primer');let pi=DATA.dummies.findIndex(p=>p.id===pid);if(pi<0)pi=0;let p=DATA.dummies[pi];setRail(`<div class="rail-group">For Dummies</div>${DATA.dummies.map((x,i)=>`<a class="${i===pi?'active':''}" href="#/primer/${x.id}">${esc(x.title)}</a>`).join('')}<div class="rail-group">Go deeper</div><a href="#/atlas">Visual atlas</a><a href="#/document/0/frontpiece">Full documents</a>`);
const numberedAs=p.id==='doc-ii'?'Document II':p.id==='doc-iii'?'Document III':'';
app.innerHTML=`<div class="content-shell"><header class="primer-intro"><div class="translation-tag">Plain-language companion · ${pi+1} / ${DATA.dummies.length}</div><h1>${esc(p.title)}</h1>${numberedAs?`<p class="numbering-note">(Hypotheses numbered as in ${numberedAs}.)</p>`:''}</header><p class="e-related"><a href="#/results/e0-a">Does the message matter? Walk through the first experiment →</a></p><div class="primer-grid"><nav class="primer-menu">${DATA.dummies.map((x,i)=>`<a class="${i===pi?'active':''}" href="#/primer/${x.id}">${esc(x.title)}</a>`).join('')}</nav><div class="primer-page"><article class="doc-content">${primerBody(p)}</article>${p.id==='equations'?instrumentsHTML():''}<nav class="doc-nav">${pi>0?`<a href="#/primer/${DATA.dummies[pi-1].id}">← ${esc(DATA.dummies[pi-1].title)}</a>`:'<span></span>'}${pi<DATA.dummies.length-1?`<a href="#/primer/${DATA.dummies[pi+1].id}">${esc(DATA.dummies[pi+1].title)} →</a>`:''}</nav></div></div></div>`;if(p.id==='equations')bindInstruments();window.scrollTo(0,0);focusApp();}

function atlas(){topActive('atlas');setRail(`<div class="rail-group">Visual atlas</div>${ATLAS.map(x=>`<a href="#${x.id}" onclick="setTimeout(()=>document.getElementById('${x.id}')?.scrollIntoView(),10)">${esc(x.title)}</a>`).join('')}<div class="rail-group">Companion</div><a href="#/primer/equations">Equation lab</a>`);
app.innerHTML=`<div class="content-wide"><header class="primer-intro"><div class="eyebrow">Visual atlas</div><h1>Relational machinery,<br>drawn as an instrument.</h1><p class="lede">Eight plates trace the conceptual spine from local construct to ecology-level claim.</p></header><div class="atlas-grid">${ATLAS.map(x=>`<section class="plate" id="${x.id}" tabindex="0" role="button" aria-label="Expand ${esc(x.title)}"><h3>${esc(x.title)}</h3><p>${esc(x.subtitle)}</p>${x.svg}<span class="plate-expand" aria-hidden="true">↗</span></section>`).join('')}</div>${window.SIDUS_RESULTS.atlas()}</div>`;bindAtlasLightbox();window.scrollTo(0,0);focusApp();}

function ensureAtlasLightbox(){
  let box=document.getElementById('atlasLightbox');
  if(box)return box;
  box=document.createElement('div');
  box.id='atlasLightbox';
  box.className='atlas-lightbox';
  box.setAttribute('aria-hidden','true');
  box.innerHTML=`<div class="atlas-lightbox-card" role="dialog" aria-modal="true" aria-label="Expanded atlas plate"><button class="atlas-lightbox-close" aria-label="Close expanded atlas plate">×</button><div class="atlas-lightbox-content"></div></div>`;
  document.body.appendChild(box);
  box.addEventListener('click',e=>{if(e.target===box)closeAtlasLightbox()});
  box.querySelector('.atlas-lightbox-close').addEventListener('click',closeAtlasLightbox);
  return box;
}
function openAtlasLightbox(plate){
  const box=ensureAtlasLightbox(), content=box.querySelector('.atlas-lightbox-content');
  content.innerHTML=`<div class="atlas-lightbox-heading"><h3>${plate.querySelector('h3').innerHTML}</h3><p>${plate.querySelector('p').innerHTML}</p></div>${plate.querySelector('svg').outerHTML}`;
  box.classList.add('open');box.setAttribute('aria-hidden','false');document.body.classList.add('lightbox-open');
  box.querySelector('.atlas-lightbox-close').focus();
}
function closeAtlasLightbox(){
  const box=document.getElementById('atlasLightbox');if(!box)return;
  box.classList.remove('open');box.setAttribute('aria-hidden','true');document.body.classList.remove('lightbox-open');
}
function bindAtlasLightbox(){
  document.querySelectorAll('.plate').forEach(plate=>{
    plate.addEventListener('click',()=>openAtlasLightbox(plate));
    plate.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();openAtlasLightbox(plate)}});
  });
}

function instrumentsHTML(){return `<div class="instruments"><section class="instrument"><h3>Residual uncertainty</h3><p>Normalize the uncertainty left after public information.</p><label><span>H(C)</span><output id="hTotalOut">2.0 bits</output></label><input id="hTotal" type="range" min="0.5" max="4" step="0.1" value="2"><label><span>H(C | ℐ)</span><output id="hCondOut">1.0 bits</output></label><input id="hCond" type="range" min="0" max="2" step="0.1" value="1"><div class="instrument-output">u = <span id="uOut">0.50</span></div></section>
<section class="instrument"><h3>Rate decomposition</h3><p>Rate spent can exceed target information delivered.</p><label><span>r</span><output id="rOut">1.2 bits</output></label><input id="r" type="range" min="0" max="3" step="0.1" value="1.2"><label><span>m</span><output id="mOut">0.8 bits</output></label><input id="m" type="range" min="0" max="1.2" step="0.1" value="0.8"><div class="instrument-output">Δ = <span id="dOut">0.40</span> bits</div></section>
<section class="instrument"><h3>Shared budget</h3><p>Three channels compete only when their sum approaches the total capacity.</p><label><span>Total capacity C</span><output id="capOut">10</output></label><input id="cap" type="range" min="3" max="18" step="1" value="10"><label><span>r₁</span><output id="r1Out">4</output></label><input id="r1" type="range" min="0" max="10" step="1" value="4"><label><span>r₂</span><output id="r2Out">3</output></label><input id="r2" type="range" min="0" max="10" step="1" value="3"><label><span>r₃</span><output id="r3Out">2</output></label><input id="r3" type="range" min="0" max="10" step="1" value="2"><div class="bars"><div class="bar" id="b1"><span>r₁</span></div><div class="bar" id="b2"><span>r₂</span></div><div class="bar" id="b3"><span>r₃</span></div></div><div class="instrument-output" id="budgetOut">9 / 10</div></section>
<section class="instrument"><h3>Causal relevance</h3><p>How quickly does performance fall under a small valid corruption?</p><label><span>Baseline J</span><output id="baseJOut">100</output></label><input id="baseJ" type="range" min="50" max="120" step="1" value="100"><label><span>Corrupted J</span><output id="corrJOut">96</output></label><input id="corrJ" type="range" min="50" max="120" step="1" value="96"><label><span>δ</span><output id="deltaOut">0.10</output></label><input id="delta" type="range" min="0.05" max="0.5" step="0.05" value="0.1"><div class="instrument-output">c(δ) = <span id="causalOut">40.0</span></div></section></div>`}
function bindInstruments(){const q=id=>document.getElementById(id);function residual(){let h=+q('hTotal').value,c=Math.min(+q('hCond').value,h);q('hCond').max=h;q('hTotalOut').value=h.toFixed(1)+' bits';q('hCondOut').value=c.toFixed(1)+' bits';q('uOut').textContent=h? (c/h).toFixed(2):'—'}q('hTotal').oninput=residual;q('hCond').oninput=residual;residual();function rate(){let r=+q('r').value,m=Math.min(+q('m').value,r);q('m').max=r;q('rOut').value=r.toFixed(1)+' bits';q('mOut').value=m.toFixed(1)+' bits';q('dOut').textContent=(r-m).toFixed(2)}q('r').oninput=rate;q('m').oninput=rate;rate();function budget(){let C=+q('cap').value,vals=[1,2,3].map(i=>+q('r'+i).value),sum=vals.reduce((a,b)=>a+b,0);q('capOut').value=C;vals.forEach((v,i)=>{q('r'+(i+1)+'Out').value=v;q('b'+(i+1)).style.height=Math.max(3,Math.min(100,v/C*100))+'%'});q('budgetOut').textContent=`${sum} / ${C}${sum>C?'  ·  OVER BUDGET':''}`;q('budgetOut').style.color=sum>C?'#df8f76':''}['cap','r1','r2','r3'].forEach(id=>q(id).oninput=budget);budget();function causal(){let a=+q('baseJ').value,b=+q('corrJ').value,d=+q('delta').value;q('baseJOut').value=a;q('corrJOut').value=b;q('deltaOut').value=d.toFixed(2);q('causalOut').textContent=((a-b)/d).toFixed(1)}['baseJ','corrJ','delta'].forEach(id=>q(id).oninput=causal);causal()}

function render(){closeMenu();closeAtlasLightbox();let r=route();if(!r.length||r[0]==='home')return home();if(r[0]==='document')return docReader(r[1]||0,r[2]||'frontpiece');if(r[0]==='primer')return primer(r[1]||'begin-here');if(r[0]==='atlas')return atlas();if(r[0]==='results'){if(!r[1])return window.SIDUS_RESULTS.index();if(r[1]==='e0-a')return window.SIDUS_RESULTS.render(r[2]);return window.SIDUS_RESULTS.index();}home()}
window.addEventListener('hashchange',render);render();

// Search
const panel=document.getElementById('searchPanel'),input=document.getElementById('searchInput'),results=document.getElementById('searchResults');
function openSearch(){panel.classList.add('open');panel.setAttribute('aria-hidden','false');setTimeout(()=>input.focus(),30)}function closeSearch(){panel.classList.remove('open');panel.setAttribute('aria-hidden','true')}
document.getElementById('searchBtn').onclick=openSearch;document.getElementById('searchClose').onclick=closeSearch;panel.onclick=e=>{if(e.target===panel)closeSearch()};
function search(q){q=q.trim().toLowerCase();if(q.length<2){results.innerHTML='<div class="search-empty">Type at least two characters.</div>';return}let hits=[];DATA.docs.forEach((d,di)=>d.sections.forEach(s=>{let text=s.title+' '+searchableText(s.html),pos=text.toLowerCase().indexOf(q);if(pos>=0)hits.push({href:`#/document/${di}/${s.id}`,title:`${d.roman}. ${d.short} — ${s.title}`,snippet:text.slice(Math.max(0,pos-90),pos+170)})}));DATA.dummies.forEach(p=>{let text=p.title+' '+searchableText(p.html),pos=text.toLowerCase().indexOf(q);if(pos>=0)hits.push({href:`#/primer/${p.id}`,title:`For Dummies — ${p.title}`,snippet:text.slice(Math.max(0,pos-90),pos+170)})});window.SIDUS_RESULTS.search.forEach(h=>{if((h.title+' '+h.snippet).toLowerCase().includes(q))hits.unshift(h)});hits=hits.slice(0,30);results.innerHTML=hits.length?hits.map(h=>`<a class="search-result" href="${h.href}" onclick="closeSearch()"><b>${esc(h.title)}</b><span>${esc(h.snippet)}</span></a>`).join(''):'<div class="search-empty">No match in the dossier.</div>'}
input.addEventListener('input',()=>search(input.value));document.addEventListener('keydown',e=>{if(e.key==='/'&&!['INPUT','TEXTAREA'].includes(document.activeElement.tagName)){e.preventDefault();openSearch()}if(e.key==='Escape'){closeAtlasLightbox();closeSearch();closeMenu()}if(e.key==='ArrowRight'&&location.hash.includes('/document/'))document.querySelector('.doc-nav a:last-child')?.click();if(e.key==='ArrowLeft'&&location.hash.includes('/document/'))document.querySelector('.doc-nav a:first-child')?.click()});

// PWA cache
if('serviceWorker' in navigator && location.protocol.startsWith('http')) navigator.serviceWorker.register('sw.js').catch(()=>{});
