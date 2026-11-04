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
def ps(l,k):return(l**k*math.exp(-l))/math.factorial(k)
def gt(n):h=hc(n);return{'av':0.6+(h%20)/10,'fo':0.85+(h%30)/100,'el':1650+(h%100)}
@app.get('/',response_class=HTMLResponse)
def home():
 A=gt('AEK');B=gt('Real');xa=round(A['av']*A['fo'],2);xb=round(B['av']*B['fo'],2);t=xa+xb;d=A['el']-B['el'];pA=1/(1+10**(-d/400));v1=round(pA*84,1);v2=round((1-pA)*84,1);sc=[]
 for i in range(5):
  for j in range(5):sc.append((f"{i}-{j}",ps(xa,i)*ps(xb,j)*100))
 sc=sorted(sc,key=lambda x:x[1],reverse=True);s1,s2=sc[0],sc[1];pT=[ps(t,k) for k in range(8)];su=sum(pT);tP=[(i,p/su*100) for i,p in enumerate(pT)];bY=sum(ps(xa,i)*ps(xb,j)*100 for i in range(1,5) for j in range(1,5));bN=100-bY
 def gp(g):return next((x[1] for x in tP if x[0]==g),0)
 mu=[('1 But',gp(1)),('2 Buts',gp(2)),('3 Buts',gp(3)),('1-2',gp(1)+gp(2)),('2-3',gp(2)+gp(3)),('2-4',gp(2)+gp(3)+gp(4)),('Over 2.5',sum(p for g,p in tP if g>=3)),('Under 3.5',sum(p for g,p in tP if g<=3)),('BTTS Oui',bY),('BTTS Non',bN)];mu=sorted(mu,key=lambda x:x[1],reverse=True);co=round(4.5+t*1.4,1);tt=int(8+t*1.8);tc=int(2.5+t*0.8);fa=11+hc('A')%7;ca=round(2.2+hc('B')%3*0.5,1)
 h=f"<body style='background:#06120e;color:#fff;font-family:system-ui;padding:10px'><h1 style='color:#00ff88;font-size:14px'>Dieng V26 FOOT COMPLET OK</h1><div style='background:#10261e;padding:10px
