"""Controlli sui file HTML generati; non sostituisce una prova visiva nel browser."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json,re,posixpath
root=Path('_build/html').resolve()
config=json.loads(Path('_build/site/config.json').read_text(encoding='utf-8'))
sourcefiles=[]
def collect(entries):
 for x in entries:
  if x.get('file'):sourcefiles.append(Path(x['file']))
  collect(x.get('children',[]))
collect(config['projects'][0]['toc'])
print('Controllo sorgenti',flush=True)
expected_solutions=sum(len(re.findall(r'^:{3,}\{dropdown\} Mostra la soluzione\s*$',p.read_text(encoding='utf-8'),re.M)) for p in sourcefiles)
class Page(HTMLParser):
 def __init__(self):
  super().__init__();self.ids=set();self.links=[];self.images=[];self.details=[];self.stack=[];self.insummary=0;self.scripts=0;self.text=[];self.math_errors=0;self.videos=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if a.get('id'):self.ids.add(a['id'])
  if tag=='a' and a.get('href'):self.links.append(a['href'])
  if tag=='img' and a.get('src'):self.images.append(a['src'])
  if tag=='video':self.videos.append(a)
  if 'katex-error' in a.get('class',''):self.math_errors+=1
  if tag=='details':self.stack.append({'open':'open' in a,'summary':''})
  if tag=='summary':self.insummary+=1
  if tag in ['script','style']:self.scripts+=1
 def handle_endtag(self,tag):
  if tag=='summary':self.insummary=max(0,self.insummary-1)
  if tag=='details' and self.stack:self.details.append(self.stack.pop())
  if tag in ['script','style']:self.scripts=max(0,self.scripts-1)
 def handle_data(self,s):
  if not self.scripts:self.text.append(s)
  if self.insummary and self.stack:self.stack[-1]['summary']+=s
print('Lettura pagine',flush=True)
pages={};errors=[]
allfiles={p.relative_to(root).as_posix():p for p in root.rglob('*') if p.is_file()}
for name,path in allfiles.items():
 if not name.endswith('index.html'):continue
 p=Page();s=path.read_text(encoding='utf-8');p.feed(s);pages[name]=p
 if '</html>' not in s:errors.append(('html incompleto',str(path)))
 if p.math_errors:errors.append(('formule non renderizzate',str(path),p.math_errors))
 if '{figure}' in ''.join(p.text):errors.append(('direttiva figura non convertita',str(path)))
 for d in p.details:
  if d['open'] and any(x in d['summary'].lower() for x in ['soluzion','docente']):errors.append(('soluzione già aperta',str(path),d['summary']))
print('Controllo collegamenti',flush=True)
badlinks=[];svg=set();solutions=0;videos=0
for path,p in pages.items():
 for href in p.links+p.images:
  u=urlsplit(href)
  if u.scheme or u.netloc:continue
  target=path if not u.path else posixpath.normpath(unquote(u.path).lstrip('/') if u.path.startswith('/') else posixpath.join(posixpath.dirname(path),unquote(u.path)))
  if target in ['.','']:target='index.html'
  if target not in allfiles:target=target.rstrip('/')+'/index.html'
  if target not in allfiles:badlinks.append((path,href));continue
  if target.endswith('.svg'):svg.add(target)
  if u.fragment and target in pages and unquote(u.fragment) not in pages[target].ids:
   badlinks.append((path,href,'ancora'))
 solutions+=sum('mostra la soluzione' in d['summary'].lower() for d in p.details);videos+=len(p.videos)
if len(pages)!=len(sourcefiles):errors.append(('numero pagine',len(pages),len(sourcefiles)))
if len(svg)!=len(list(Path('figure').glob('*.svg'))):errors.append(('numero diagrammi',len(svg)))
if solutions!=expected_solutions:errors.append(('soluzioni non convertite',solutions,expected_solutions))
if not videos:errors.append(('video non convertito',videos))
errors.extend(badlinks)
report={'pagine_html':len(pages),'diagrammi_svg':len(svg),'soluzioni_chiuse':solutions,'video':videos,'errori':errors,'limite':'Controlli statici: anteprima browser integrato non disponibile.'}
Path('verifica-sito.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({k:v if k!='errori' else {'numero':len(v),'primi':v[:12]} for k,v in report.items()},ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
