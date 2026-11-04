from fastapi import FastAPI
from fastapi.responses import HTMLResponse,JSONResponse,Response
import math
app=FastAPI()
@app.get('/manifest.json')
def m():return JSONResponse({'name':'Dieng'})
@app.get('/sw.js')
def s():return Response('a',media_type='application/javascript')
def hc(s):
 h=0
 for c in s:h=ord(c)+((h<<5)-h)
 return abs(h)
def ps(l,k):
 return(l**k*math.exp(-l))/math.factorial(k)
def gt(n):
 h=hc(n)
 return{'av':0.6+(h%20)/10,'fo':0.85+(h%30)/100,'el':1650+(h%100)}
@app.get('/',response_class=HTMLResponse)
def home():
 A=gt('AEK')
 B=gt('Real')
 xa=round(A['av']*A['fo'],2)
 xb=round(B['av']*B['fo'],2)
 t=xa+xb
 d=A['el']-B['el']
 pA=1/(1+10**(-d/400))
 v1=round(pA*84,1)
 v2=round((1-pA)*84,1)
 sc=[]
 for i in range(5):
  for j in range(5):
   sc.append((f"{i}-{j}",ps(xa,i)*ps(xb,j)*100))
 sc=sorted(sc,key=lambda x:x[1],reverse=True)
 s1=sc[0]
 s2=sc[1]
 pT=[ps(t,k) for k in range(8)]
 su=sum(pT)
 tP=[(i,p/su*100) for i,p in enumerate(pT)]
 bY=sum(ps(xa,i)*ps(xb,j)*100 for i in range(1,5) for j in range(1,5))
 bN=100-bY
 def gp(g):
  return next((x[1] for x in tP if x[0]==g),0)
 mu=[]
 mu.append(('1 But',gp(1)))
 mu.append(('2 Buts',gp(2)))
 mu.append(('3 Buts',gp(3)))
 mu.append(('1-2',gp(1)+gp(2)))
 mu.append(('2-3',gp(2)+gp(3)))
 mu.append(('2-4',gp(2)+gp(3)+gp(4)))
 mu.append(('Over 2.5',sum(p for g,p in tP if g>=3)))
 mu.append(('Under 3.5',sum(p for g,p in tP if g<=3)))
 mu.append(('BTTS Oui',bY))
 mu.append(('BTTS Non',bN))
 mu=sorted(mu,key=lambda x:x[1],reverse=True)
 co=round(4.5+t*1.4,1)
 tt=int(8+t*1.8)
 tc=int(2.5+t*0.8)
 fa=11+hc('A')%7
 ca=round(2.2+hc('B')%3*0.5,1)
 h="<html><head><meta charset='utf-8'>"
 h+="<meta name='viewport' content='width=device-width,initial-scale=1'>"
 h+="<style>"
 h+="body{margin:0;background:#06120e;color:#fff;font-family:system-ui;padding:8px}";
 h+="h1{color:#00ff88;font-size:13px;text-align:center}";
 h+=".card{background:#10261e;padding:10px;margin:8px 0;border-radius:12px;border:1px solid #ffffff12}";
 h+=".v1n2{background:linear-gradient(90deg,#00ff88,#00aaff);color:#000;padding:10px;border-radius:10px;text-align:center;font-weight:900;font-size:13px}";
 h+=".sc{background:#123829;border:2px solid #00ff88;border-radius:10px;padding:8px;text-align:center;margin:8px 0}";
 h+=".grid{display:grid;grid-template-columns:1fr 1fr;gap:6px;margin-top:6px}";
 h+=".grid3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:6px;margin-top:6px}";
 h+=".box{background:#0a2e22;border:1px solid #00ff8820;border-radius:8px;padding:8px;text-align:center;font-size:11px}";
 h+=".box.c{border-color:#00ff88;background:#123829;font-weight:900}";
 h+="</style></head><body>"
 h+="<h1>Dieng V26 FOOT COMPLET BEAU</h1>"
 h+=f"<div class=card><div class=v1n2>V1 {v1}% - NUL 16% - V2 {v2}%</div>"
 h+=f"<div style='font-size:10px;background:#0f2a1e;padding:6px;border-radius:6px;margin:6px 0'>xG {xa}+{xb}={t:.2f}</div>"
 h+=f"<div class=sc><b>2 SCORES EXACTS</b><br><b style='font-size:16px'>{s1[0]} {s1[1]:.1f}%</b> - <b style='font-size:16px'>{s2[0]} {s2[1]:.1f}%</b></div>"
 h+="<b>Multi-Buts + Over/Under + BTTS</b><div class=grid>"
 gr=""
 best=mu[0][0]
 for n,p in mu:
  c=" c" if n==best else ""
  gr+=f"<div class='box{c}'><b>{n}</b><br>{p:.1f}%"
  gr+=f"{'<br>CONSEIL' if n==best else ''}</div>"
 h+=gr+"</div>"
 h+=f"<hr><b>Stats Avancees</b><div class=grid3><div class=box>Corners<br><b>~{co}</b></div><div class=box>Cartons<br><b>~{ca}</b></div><div class=box>Fautes<br><b>~{fa}</b></div></div><div class=grid><div class=box>Tirs Totaux<br><b>~{tt}</b></div><div class=box>Tirs Cadres<br><b>~{tc}</b></div></div></div>"
 h+="</body></html>"
 return HTMLResponse(h)
