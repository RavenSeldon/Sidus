#!/usr/bin/env python3
"""Rebuild web readers, PDF bodies and hashes from the four canonical Markdown files.

Requires Pandoc 3.x, XeLaTeX, and Python packages pymupdf and pypdf.
The companion/atlas editorial content remains in assets/content.js and atlas.js.
Run from any directory: python scripts/rebuild.py [--web-only]
"""
from pathlib import Path
import argparse, hashlib, html, json, re, subprocess, tempfile, unicodedata

ROOT=Path(__file__).resolve().parents[1]
FORMAT='markdown+tex_math_single_backslash'

def pandoc(text, target, *args):
    fmt=FORMAT+('+autolink_bare_uris' if target=='latex' else '')
    p=subprocess.run(['pandoc','-f',fmt,'-t',target,'--wrap=none',*args],input=text,text=True,capture_output=True,check=True)
    if target!='plain' and p.stderr.strip(): print(p.stderr.strip())
    return p.stdout

def slug(text):
    text=unicodedata.normalize('NFKD',text).encode('ascii','ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+','-',text).strip('-')

def chunks(text, separate_refs):
    out=[]; current=[]; title='Opening'; part=None; next_part=None
    def flush():
        nonlocal current
        if current: out.append((title,part,''.join(current)))
        current=[]
    for line in text.splitlines(keepends=True):
        if line.startswith('# PART '):
            flush(); next_part=line[2:].strip(); continue
        is_section=line.startswith('## ') and not re.match(r'## [IV]+\.',line)
        if is_section or (separate_refs and line.startswith('# References')):
            if next_part is None: flush()
            title=line.lstrip('#').strip();part=next_part;next_part=None
        current.append(line)
    flush()
    return out

def build_web():
    p=ROOT/'assets/content.js'
    data=json.loads(p.read_text().split('=',1)[1].rstrip(';\n '))
    for doc in data['docs']:
        text=(ROOT/doc['sourceMd']).read_text()
        doc['title']=re.search(r'^## ([IV]+\..+)$',text,re.M).group(1)
        ids={s['title']:s['id'] for s in doc['sections']}
        sections=[]
        for title,part,source in chunks(text,doc['roman']=='IV'):
            sid='frontpiece' if title=='Opening' else ids.get(title,slug(title))
            sections.append(dict(id=sid,title=title,part=part,html=pandoc(source,'html5','--mathml'),plain=pandoc(source,'plain')))
        doc['sections']=sections
    p.write_text('window.SIDUS_DATA='+json.dumps(data,ensure_ascii=False)+';\n')
    # Reuse the exact standalone shell/style/artwork, replacing only its scripts.
    p=ROOT/'Sidus_Dossier_Standalone.html'; standalone=p.read_text()
    for marker,asset in [('window.SIDUS_DATA=','content.js'),('window.SIDUS_ATLAS=','atlas.js'),('const DATA=','app.js')]:
        pattern=r'<script>\s*'+re.escape(marker)+r'.*?</script>'
        assert len(re.findall(pattern,standalone,re.S))==1,marker
        standalone=re.sub(pattern,lambda _: '<script>\n'+(ROOT/'assets'/asset).read_text()+'\n</script>',standalone,flags=re.S)
    p.write_text(standalone)

def build_pdfs():
    import fitz
    from pypdf import PdfReader, PdfWriter
    for source in sorted((ROOT/'source').glob('*.md')):
        number=source.name[:2]
        with tempfile.TemporaryDirectory() as tmp:
            tmp=Path(tmp)
            tex=pandoc(source.read_text(),'latex','--standalone','--top-level-division=section',
                '-V','documentclass=article','-V','fontsize=10pt','-V','papersize=a4',
                '-V','geometry:margin=22mm','-V','mainfont=DejaVu Serif',
                '-V','sansfont=DejaVu Sans','-V','monofont=DejaVu Sans Mono',
                '-V','mathfont=Latin Modern Math','-V','colorlinks=true',
                '-V','linkcolor=gold','-V','urlcolor=gold',
                '-H',str(ROOT/'scripts/pdf-style.tex'))
            # Permit a line break at this compound table label without changing its text.
            tex=tex.replace('complementarity/substitution',r'complementarity/\allowbreak substitution')
            (tmp/'body.tex').write_text(tex)
            for _ in range(2):
                result=subprocess.run(['xelatex','-interaction=nonstopmode','-halt-on-error','body.tex'],cwd=tmp,text=True,capture_output=True)
                if result.returncode: raise RuntimeError(result.stdout[-7000:])
            log=(tmp/'body.log').read_text()
            warnings=[line for line in log.splitlines() if 'Missing character' in line or 'Overfull' in line]
            if warnings: print(source.name,*warnings,sep='\n')
            writer=PdfWriter(); cover=PdfReader(ROOT/'scripts/covers'/f'{number}.pdf')
            writer.add_page(cover.pages[0])
            for page in PdfReader(tmp/'body.pdf').pages:writer.add_page(page)
            title=re.search(r'^## (.+)$',source.read_text(),re.M).group(1)
            writer.add_metadata({'/Title':'Sīdus: '+title,'/Subject':'September 2026 implementation-validity and university-agnostic revision'})
            with source.with_suffix('.pdf').open('wb') as f:writer.write(f)
            check=fitz.open(source.with_suffix('.pdf'))
            text=''.join(page.get_text() for page in check)
            if re.search(r'Radboud|MLNC|HCIS|Donders|ru\.nl|Nijmegen',text,re.I):raise RuntimeError('Institutional text in '+source.name)
            print(source.with_suffix('.pdf').name, len(check),'pages')

def hashes():
    paths=sorted((ROOT/'source').glob('*'))
    (ROOT/'SOURCE_SHA256.txt').write_text(''.join(f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}\n' for p in paths if p.suffix in ('.md','.pdf')))

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--web-only',action='store_true');args=ap.parse_args()
    build_web()
    if not args.web_only:build_pdfs()
    hashes()
