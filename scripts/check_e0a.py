#!/usr/bin/env python3
"""Verify every emitted leaf against archive selectors, and frozen payload integrity.
python3 scripts/check_e0a.py [--baseline /path/to/original/Sidus]
"""
from pathlib import Path
import argparse,hashlib,json,re
import build_e0a as build
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'assets/results'
def leaves(x,path=''):
 if isinstance(x,dict):
  for k,v in x.items():yield from leaves(v,path+'.'+k if path else k)
 elif isinstance(x,list):
  for i,v in enumerate(x):yield from leaves(v,path+'.'+str(i))
 else:yield path,x

def resolve(x,path):
 if not path:return x
 if isinstance(x,list):
  head,_,tail=path.partition('.');return resolve(x[int(head)],tail)
 key=max((k for k in x if path==k or path.startswith(k+'.')),key=len)
 return resolve(x[key],path[len(key):].lstrip('.'))

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--baseline');a=ap.parse_args()
 hashes=json.loads((OUT/'source-hashes.json').read_text())
 for name,digest in hashes.items():
  b=(OUT/'evidence'/name).read_bytes();assert hashlib.sha256(b).hexdigest()==digest;build.sources[name]=b
 provenance=json.loads((OUT/'e0a-provenance.json').read_text());records={k:json.loads((ROOT/v).read_text()) for k,v in provenance.items()}
 for k,r in records.items():assert build.evaluate(r)==r['exact'],k
 checked=0
 for group in ['summary','controls','seeds','development']:
  data=json.loads((OUT/f'e0a-{group}.json').read_text())
  for path,v in leaves(data,group):
   matches=[k for k in records if path==k or path.startswith(k+'.')];assert matches,('uncovered',path)
   key=max(matches,key=len);r=records[key];sub=path[len(key):].strip('.')
   expected=resolve(r['exact'],sub)
   assert v==expected,(path,v,expected);assert v is not None,('null',path);checked+=1
 html=(ROOT/'e0a.html').read_text();assert '<script' not in html
 assert len(re.findall('class="e-scene"',html))==6
 assert html.count('class="e-static-mark"')==500
 # All local static reading-edition links resolve, including individual provenance/source artifacts.
 for href in re.findall(r'href="([^"]+)"',html):
  path=href.split('#')[0].split('?')[0]
  if path and not re.match(r'https?:',path):assert (ROOT/path).is_file(),href
 assert 'ATTEMPTS.jsonl' not in (ROOT/'sw.js').read_text() and '.zip' not in (ROOT/'sw.js').read_text()
 frozen={}
 if a.baseline:
  base=Path(a.baseline)
  names=['assets/content.js','assets/atlas.js','SOURCE_SHA256.txt']+[str(p.relative_to(base)) for p in (base/'source').iterdir() if p.is_file()]
  for name in names:
   before=(base/name).read_bytes();after=(ROOT/name).read_bytes();assert before==after,name;frozen[name]=hashlib.sha256(after).hexdigest()
  pattern=r'<script>\s*window.SIDUS_DATA=[\s\S]*?</script>'
  assert re.search(pattern,(base/'Sidus_Dossier_Standalone.html').read_text()).group()==re.search(pattern,(ROOT/'Sidus_Dossier_Standalone.html').read_text()).group(),'standalone frozen payload'
  (ROOT/'E0A_PRESERVATION.json').write_text(json.dumps(frozen,indent=2))
 print(f'PASS: {checked} emitted leaf values; {len(records)} archive recipes; static links and six scenes; {len(frozen)} frozen files plus standalone payload unchanged.')
if __name__=='__main__':main()
