#!/usr/bin/env python3
"""Extract only companion evidence. Never rebuild or write the frozen corpus.
Usage: python3 scripts/build_e0a.py --results PATH --freeze PATH
Provenance selectors are executable recipes; wildcard entries cover table cells.
"""
import argparse,csv,io,json,math,re,shutil,statistics,zipfile,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'assets/results'
SOURCES=OUT/'evidence'
P={}; sources={}
def read(z,path):
 b=z.read(path); sources[path]=b
 if path.endswith('.json'): return json.loads(b)
 if path.endswith('.csv'): return list(csv.DictReader(io.StringIO(b.decode())))
 return b.decode()
def get(x,path):
 for k in path: x=x[int(k)] if isinstance(x,list) else x[k]
 return x
def evaluate(r):
 b=sources[r['source_file']];op=r['op']; path=r.get('path',[])
 if op=='csv':
  rows=list(csv.DictReader(io.StringIO(b.decode())))
  rows=[x for x in rows if all(x[k]==v for k,v in r.get('where',{}).items())]
  if r.get('aggregate')=='count': return len(rows)
  if r.get('aggregate')=='endpoint_decline':
   by={(x['seed'],float(x['rho'])):float(x[r['field']]) for x in rows}
   return statistics.mean(by[seed,0]-by[seed,1] for seed in sorted({x['seed'] for x in rows}))
  if 'field' not in r:return rows
  vals=[x[r['field']] for x in rows]
  if r.get('aggregate')=='mean': return 'unavailable' if all(x=='' for x in vals) else statistics.mean(float(x) for x in vals)
  if r.get('aggregate')=='truth_counts': return {v:vals.count(v) for v in sorted(set(vals))}
  return rows
 if op=='markdown_count':
  m=re.search(r'^\| '+re.escape(r['arm'])+r' \| (\d+)/(\d+) \|',b.decode(),re.M);return int(m.group(r['group']))
 x=get(json.loads(b),path)
 if op=='maximum':return max(x.values())
 if op=='length':return len(x)
 if op=='below_full':return len([v for v in x if v<1])
 if op=='minimum_n':
  st=x['statistics'];w=st['a4_ranges']['decline_B_obs'];W=w[1]-w[0]; threshold=x['thresholds']['delta_A4_B_obs'];ideal=json.loads(sources[r['secondary_source']])['A4_population']['decline_B_obs']['mean']
  return math.ceil(W*W*math.log(2/st['a4_alpha_each'])/(2*(ideal-threshold)**2))
 return x
def emit(id,source,path=(),op='json',unit='record',stage='frozen_confirmation',denominator='registered initializations',**kw):
 r={'source_file':source,'path':list(path),'op':op,**kw};v=evaluate(r)
 P[id]={**r,'selector':('/'+'/'.join(map(str,path))) if op=='json' else json.dumps(r,separators=(',',':')),'unit':unit,'population':denominator,'denominator':denominator,'evidence_stage':stage,'aggregation':kw.get('aggregate',op),'artifact_link':'assets/results/evidence/'+source,'exact':v}
 return v

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--results',required=True);ap.add_argument('--freeze',required=True);a=ap.parse_args()
 z=zipfile.ZipFile(a.results);f=zipfile.ZipFile(a.freeze);ex=zipfile.ZipFile(io.BytesIO(f.read('Sidus_E0_Freeze_v0.7_F1/Sidus_E0_Experiment_v0.7.zip')))
 A='Sidus_E0_F1_Execution/'; F='Sidus_E0_Freeze_v0.7_F1/';D='Sidus_E0_Confirmation_v0.7/'
 for n in ['ADJUDICATION.json','DESCRIPTIVE_SUMMARY.json','CONDITION_OUTCOMES.csv','SEED_OUTCOMES.csv','INDEPENDENT_FINITE_AUDIT.json','INDEPENDENT_STATISTICAL_CHECK.json','REPLAY_PROCESS.json','POST_REPLAY_PRESERVATION.json','GENERATION_PROCESS.json'] :read(z,A+n)
 for n in ['FROZEN_CONFIG.json','FREEZE_RECEIPT.json','FREEZE_SHA256.txt']:read(f,F+n)
 for n in ['history/stress_examples/SUMMARY.json','history/STRESS_DESIGN.json','history/previous/development_examples/REPORT.md','history/previous/DESIGN.json','STATISTICAL_PLAN_DRAFT.md']:read(ex,D+n)
 run=[n for n in z.namelist() if n.endswith('.start.json')];marker=[n for n in z.namelist() if '/consumed_freezes/' in n and n.endswith('.json')];assert len(run)==len(marker)==1
 read(z,run[0]);read(z,marker[0])
 adj=json.loads(sources[A+'ADJUDICATION.json']);config=json.loads(sources[F+'FROZEN_CONFIG.json']);rows=list(csv.DictReader(io.StringIO(sources[A+'CONDITION_OUTCOMES.csv'].decode())))
 E=lambda id,path:emit(id,A+'ADJUDICATION.json',path,unit='probability interval; counts of initializations' if path==['reliability'] else 'family error probability' if path==['family_alpha'] else 'adjudication decision',denominator=len(config['seeds']))
 summary={k:E('summary.'+k,[k]) for k in ['gates','reliability','family_alpha','claim_license','E1_license','E0B_license','trust_limit']}
 summary['primary']=emit('summary.primary',A+'DESCRIPTIVE_SUMMARY.json',['primary_metrics'],unit='bits for hiddenness/transmission; expected reward for performance/benefit',denominator=len(config['seeds']))
 summary['attempts']=emit('summary.attempts',A+'DESCRIPTIVE_SUMMARY.json',['execution_counts','evaluated'],unit='attempts')
 summary['diagnostics']=emit('summary.diagnostics',A+'DESCRIPTIVE_SUMMARY.json',['expected_control_outcomes'],unit='control instances')
 summary['config']=emit('summary.config',F+'FROZEN_CONFIG.json');summary['receipt']=emit('summary.receipt',F+'FREEZE_RECEIPT.json');summary['start']=emit('summary.start',run[0]);summary['consumed']=emit('summary.consumed',marker[0])
 for key,name in [('replay','REPLAY_PROCESS.json'),('audit','INDEPENDENT_FINITE_AUDIT.json'),('arithmetic','INDEPENDENT_STATISTICAL_CHECK.json'),('preservation','POST_REPLAY_PRESERVATION.json')]:summary[key]=emit('summary.'+key,A+name)
 summary['audit_discrepancies']=emit('summary.audit_discrepancies',A+'INDEPENDENT_FINITE_AUDIT.json',['discrepancies'],op='length',unit='discrepancies')
 summary['audit_maximum_residual']=emit('summary.audit_maximum_residual',A+'INDEPENDENT_FINITE_AUDIT.json',['maximum_absolute_residual_by_field'],op='maximum',unit='absolute numerical residual across audited fields')
 summary['minimum_n']=emit('summary.minimum_n',F+'FROZEN_CONFIG.json',op='minimum_n',secondary_source=A+'ADJUDICATION.json',secondary_selector='/A4_population/decline_B_obs/mean',unit='initializations')
 summary['declines']={k:emit('summary.declines.'+k,A+'CONDITION_OUTCOMES.csv',op='csv',where={'system':'learned'},field=field,aggregate='endpoint_decline',unit='bits' if k=='decline_m' else 'expected reward',denominator=len(config['seeds'])) for k,field in [('decline_m','m_bits'),('decline_B_class','class_benefit'),('decline_B_obs','observed_benefit')]}
 summary['intervals']={k:emit('summary.intervals.'+k,A+'ADJUDICATION.json',['A4_population',k]) for k in adj['A4_population']}
 for k in summary['intervals']:summary['intervals'][k]={x:v for x,v in summary['intervals'][k].items() if x!='observations'}
 fields=['H_bits','m_bits','consumer_value','comparator_value','class_benefit','observed_benefit','eligible_mass','eligible_reward_drop','no_op_fraction']
 def profile(system,rho,prefix):
  return {k:emit(prefix+'.'+k,A+'CONDITION_OUTCOMES.csv',op='csv',where={'system':system,'rho':str(rho)},field=k,aggregate='mean',unit='bits' if k.endswith('bits') else 'fraction of task population' if k=='eligible_mass' else 'fraction of eligible replacements' if k=='no_op_fraction' else 'expected reward drop within eligible population' if k=='eligible_reward_drop' else 'expected reward',denominator=len(config['seeds'])) for k in fields}
 # Use CSV spelling, avoiding 0 versus 0.0 ambiguity.
 stops=sorted({r['rho'] for r in rows if r['system']=='learned'},key=float)
 summary['sweep']=[profile('learned',rho,'summary.sweep.'+str(i)) for i,rho in enumerate(stops)]
 controls={}
 for system in config['controls']:
  rr=next(r['rho'] for r in rows if r['system']==system);p=profile(system,rr,'controls.'+system)
  for k in ['collapsed','expected_control_diagnostic']:
   p[k]=emit('controls.'+system+'.'+k,A+'CONDITION_OUTCOMES.csv',op='csv',where={'system':system},field=k,aggregate='truth_counts',unit='instances',denominator=len(config['seeds']))
  controls[system]=p
 seeds=emit('seeds',A+'SEED_OUTCOMES.csv',op='csv',unit='one row per initialization',denominator=len(config['seeds']))
 dev={};sd=D+'history/stress_examples/SUMMARY.json';pd=D+'history/previous/DESIGN.json';pr=D+'history/previous/development_examples/REPORT.md'
 dev['seed_count']=emit('development.seed_count',pd,['seeds'],op='length',stage='development_evidence',unit='seeds')
 dev['conditions']=emit('development.conditions',pd,['rhos'],op='below_full',stage='development_evidence',unit='conditions below full reveal')
 dev['selection']=emit('development.selection',pd,['selection'],stage='development_evidence')
 dev['first']={};dev['stress']={}
 for arm in ['baseline','R1','R2','R3']:
  dev['first'][arm]={k:emit('development.first.'+arm+'.'+k,pr,op='markdown_count',arm=arm,group=g,stage='development_evidence',unit='condition-runs') for k,g in [('collapse',1),('runs',2)]}
  dev['stress'][arm]={k:emit('development.stress.'+arm+'.'+k,sd,['summary','arms',arm,k],stage='development_evidence',unit='seed probability' if k=='wilson95' else 'count',denominator=len(json.loads(sources[sd])['design']['fresh_seeds'])) for k in ['collapse_count','seed_denominator','wilson95','panels']}
 dev['paired']=emit('development.paired',sd,['summary','paired_vs_baseline'],stage='development_evidence');dev['grid']=emit('development.grid',sd,['design','grid'],stage='development_evidence')
 # Independent checks against archived data, not brief-transcribed display constants.
 n=len(seeds);assert n==len(config['seeds'])==500
 assert len(rows)==summary['attempts']==6500
 assert sum(r['system']=='learned' for r in rows)==2500
 assert sum(r['system']!='learned' for r in rows)==summary['diagnostics']==4000
 assert sum(r['status']=='pass' for r in seeds)==adj['reliability']['successes']==500
 assert [int(s['seed']) for s in seeds]==config['seeds']
 for s,t in zip(seeds,adj['seed_outcomes']):
  assert s['status']==t['status'] and all(s[g]==t['gates'][g] for g in ['A1','A2','A3','A4']) and s['controls']==t['controls'] and s['reward_application']==t['reward_application']
 by={(r['seed'],float(r['rho'])):r for r in rows if r['system']=='learned'}
 for key,field in [('decline_m','m_bits'),('decline_B_class','class_benefit'),('decline_B_obs','observed_benefit')]:
  ds=[float(by[s['seed'],0][field])-float(by[s['seed'],1][field]) for s in seeds]
  assert abs(statistics.mean(ds)-adj['A4_population'][key]['mean'])<1e-10
  bounds=config['statistics']['a4_ranges'][key];radius=(bounds[1]-bounds[0])*math.sqrt(math.log(2/config['statistics']['a4_alpha_each'])/(2*n))
  assert abs(radius-adj['A4_population'][key]['radius'])<1e-12
 assert summary['family_alpha']==config['statistics']['family_alpha']
 for entry in P.values():assert evaluate(entry)==entry['exact']
 for p in controls.values():assert all(v is not None for v in p.values())
 OUT.mkdir(parents=True,exist_ok=True)
 for path,b in sources.items():
  p=SOURCES/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
 data={'summary':summary,'controls':controls,'seeds':seeds,'development':dev}
 for k,v in data.items():(OUT/('e0a-'+k+'.json')).write_text(json.dumps(v,separators=(',',':')))
 # Subtree provenance covers each child with its exact appended JSON pointer or CSV row/column.
 # Evidence is lazy-loaded per entry; large seed and configuration provenance is not boot payload.
 compact={}
 for i,(k,v) in enumerate(P.items()):
  p=OUT/'provenance'/f'{i}.json';p.parent.mkdir(exist_ok=True);p.write_text(json.dumps(v,separators=(',',':')));compact[k]=f'assets/results/provenance/{i}.json'
 (OUT/'e0a-provenance.json').write_text(json.dumps(compact,separators=(',',':')))
 # Omit bulk config seed inventory and interval observations from browser boot where already represented.
 boot={**data,'provenance':compact};(OUT/'e0a-data.js').write_text('window.SIDUS_E0A='+json.dumps(boot,separators=(',',':'))+';\n')
 downloads=ROOT/'downloads';downloads.mkdir(exist_ok=True)
 for path in [a.results,a.freeze]:shutil.copyfile(path,downloads/Path(path).name)
 (OUT/'source-hashes.json').write_text(json.dumps({p:hashlib.sha256(b).hexdigest() for p,b in sources.items()},indent=2))
 print(f'PASS: {len(rows)} attempts, {n} seeds, {len(P)} executable provenance recipes; all declines and radii match.')
if __name__=='__main__':main()
