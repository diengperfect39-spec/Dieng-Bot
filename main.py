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
@app.get('/',response_class=HTMLResponse)
def home():
 h="<html><head><meta charset='utf-8'>"
 h+="<meta name='viewport' content='width=device-width,initial-scale=1'>"
 h+="<style>body{margin:0;background:#06120e;color:#fff;font-family:system-ui;padding:6px}"
 h+="h1{color:#00ff88;font-size:11px;text-align:center}.tabs{display:flex;gap:4px;overflow:auto;padding:6px}"
 h+=".tab{padding:7px 10px;border-radius:20px;background:#10261e;color:#888;border:1px solid #00ff8830;font-size:10px;cursor:pointer;white-space:nowrap}"
 h+=".tab.a{background:#00ff88;color:#000;font-weight:900}.card{background:#10261e;padding:8px;margin:6px 0;border-radius:12px;border:1px solid #ffffff12;font-size:11px}"
 h+=".top{background:#10261e;border:1px solid #00ff8840;border-radius:12px;padding:8px;margin:6px}.inputs{display:flex;gap:4px}"
 h+=".inputs input{flex:1;background:#0f2a1e;border:1px solid #00ff8830;border-radius:7px;padding:8px;color:#fff;text-align:center;font-weight:700}"
 h+=".vs{background:#0a2e22;color:#00ff88;font-weight:900;border-radius:999px;padding:4px 7px}.btn{width:100%;background:#00ff88;color:#06120e;border:0;border-radius:7px;padding:9px;font-weight:900;cursor:pointer}"
 h+=".v1n2{background:linear-gradient(90deg,#00ff88,#00aaff);color:#000;padding:8px;border-radius:8px;text-align:center;font-weight:900}"
 h+=".sc{background:#123829;border:2px solid #00ff88;border-radius:10px;padding:8px;text-align:center;margin:6px 0}"
 h+=".grid{display:grid;grid-template-columns:1fr 1fr;gap:4px;margin-top:4px}.grid3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:4px}"
 h+=".box{background:#0a2e22;border:1px solid #00ff8820;border-radius:7px;padding:6px;text-align:center;font-size:10px}.box.c{border-color:#00ff88;background:#123829;font-weight:900}"
 h+=".sec{display:none}.sec.a{display:block}</style></head><body>"
 h+="<h1>Dieng V26 FOOT + BASKET + HOCKEY + TENNIS + PING</h1>"
 h+="<div class=tabs><div class='tab a' onclick='sh(\"f\",this)'>Foot</div><div class=tab onclick='sh(\"b\",this)'>Basket</div><div class=tab onclick='sh(\"h\",this)'>Hockey</div><div class=tab onclick='sh(\"t\",this)'>Tennis</div><div class=tab onclick='sh(\"p\",this)'>Ping</div></div>"
 h+="<div id=f class='sec a'><div class=top><div class=inputs><input id=fa value='AEK'><div class=vs>VS</div><input id=fb value='Real'></div><button class=btn onclick='gf()'>ANALYSER FOOTBALL</button></div><div class=card id=rf>Clique ANALYSER</div></div>"
 h+="<div id=b class=sec><div class=top><div class=inputs><input id=ba value='Lakers'><div class=vs>VS</div><input id=bb value='Warriors'></div><button class=btn onclick='gb()'>BASKET</button></div><div class=card id=rb></div></div>"
 h+="<div id=h class=sec><div class=top><div class=inputs><input id=ha value='Leafs'><div class=vs>VS</div><input id=hb value='Oilers'></div><button class=btn onclick='gh()'>HOCKEY</button></div><div class=card id=rh></div></div>"
 h+="<div id=t class=sec><div class=top><div class=inputs><input id=ta value='Alcaraz'><div class=vs>VS</div><input id=tb value='Sinner'></div><button class=btn onclick='gt()'>TENNIS</button></div><div class=card id=rt></div></div>"
 h+="<div id=p class=sec><div class=top><div class=inputs><input id=pa value='Fan'><div class=vs>VS</div><input id=pb value='Hari'></div><button class=btn onclick='gp()'>PING</button></div><div class=card id=rp></div></div>"
 h+="<script>"
 h+="function sh(a,b){document.querySelectorAll('.sec').forEach(function(s){s.classList.remove('a')});document.querySelectorAll('.tab').forEach(function(t){t.classList.remove('a')});document.getElementById(a).classList.add('a');b.classList.add('a')}"
 h+="function hc(s){var h=0;for(var i=0;i<s.length;i++){h=s.charCodeAt(i)+((h<<5)-h)}return Math.abs(h)}"
 h+="function fc(n){if(n<=1)return 1;var r=1;for(var i=2;i<=n;i++){r*=i}return r}"
 h+="function ps(l,k){return Math.pow(l,k)*Math.exp(-l)/fc(k)}"
 h+="function gn(n){var h=hc(n);return{av:0.6+(h%20)/10,fo:0.85+(h%30)/100,el:1650+(h%100)}}"
 h+="function gf(){var A=gn(fa.value),B=gn(fb.value),sd=hc(fa.value+fb.value),xgA=Number((A.av*A.fo).toFixed(2)),xgB=Number((B.av*B.fo).toFixed(2)),tot=xgA+xgB,d=(A.el-B.el)+(A.fo-B.fo)*100,pA=1/(1+Math.pow(10,-d/400)),v1=(pA*84).toFixed(1),v2=((1-pA)*84).toFixed(1),sc=[];for(var i=0;i<=4;i++){for(var j=0;j<=4;j++){sc.push({s:i+'-'+j,p:ps(xgA,i)*ps(xgB,j)*100})}}sc.sort(function(a,b){return b.p-a.p});var s1=sc[0],s2=sc[1],pt=[];for(var k=0;k<=7;k++){pt[k]=ps(tot,k)}var sum=0;for(var k=0;k<pt.length;k++){sum+=pt[k]}var tp=[];for(var k=0;k<pt.length;k++){tp[k]=pt[k]/sum*100}var by=0;for(var i=1;i<=4;i++){for(var j=1;j<=4;j++){by+=ps(xgA,i)*ps(xgB,j)*100}}var bn=100-by;var m=[];m.push({n:'1 But',p:tp[1]});m.push({n:'2 Buts',p:tp[2]});m.push({n:'3 Buts',p:tp[3]});m.push({n:'1-2',p:tp[1]+tp[2]});m.push({n:'2-3',p:tp[2]+tp[3]});m.push({n:'2-4',p:tp[2]+tp[3]+tp[4]});var ov=0;for(var k=3;k<tp.length;k++){ov+=tp[k]}var un=0;for(var k=0;k<=3;k++){un+=tp[k]}m.push({n:'Over 2.5',p:ov});m.push({n:'Under 3.5',p:un});m.push({n:'BTTS Oui',p:by});m.push({n:'BTTS Non',p:bn});m.sort(function(a,b){return b.p-a.p});var best=m[0].n,gr='';for(var i=0;i<m.length;i++){var r=m[i];var cl=r.n==best?' c':'';gr+='<div class=\"box'+cl+'\"><b>'+r.n+'</b><br>'+r.p.toFixed(1)+'%'+(cl?' CONSEIL':'')+'</div>'}var co=(4.5+tot*1.4).toFixed(1),tt=(8+tot*1.8).toFixed(0),tc=(2.5+tot*0.8).toFixed(0),faa=(11+sd%7).toFixed(0),ca=(2.2+sd%3*0.5).toFixed(1);var hh='';hh+='<div class=v1n2>V1 '+v1+'% - NUL 16% - V2 '+v2+'%</div>';hh+='<div style=font-size:10px;background:#0f2a1e;padding:5px;border-radius:6px>Equipes '+fa.value+' vs '+fb.value+'<br>xG '+xgA+'+'+xgB+'='+tot.toFixed(2)+'</div>';hh+='<div class=sc><b>2 SCORES</b><br><b>'+s1.s+' '+s1.p.toFixed(1)+'%</b> - <b>'+s2.s+' '+s2.p.toFixed(1)+'%</b></div>';hh+='<b>Multi+Over+BTTS</b><div class=grid>'+gr+'</div><hr><b>Stats</b><div class=grid3><div class=box>Corners<br>~'+co+'</div><div class=box>Cartons<br>~'+ca+'</div><div class=box>Fautes<br>~'+faa+'</div></div><div class=grid><div class=box>Tirs Tot<br>~'+tt+'</div><div class=box>Tirs Cadres<br>~'+tc+'</div></div>';document.getElementById('rf').innerHTML=hh}"
 h+="function gb(){var a=ba.value,b=bb.value,s=hc(a+b),pA=55+s%10,pB=100-pA;var h='';h+='<div class=v1n2>V1 '+pA+'% - V2 '+pB+'%</div><b>Over/Under</b><div class=grid><div class=\"box c\">Over 215.5 58%</div><div class=box>Under 215.5 42%</div></div><b>Handicap</b><div class=grid><div class=box>'+a+' -4.5 '+(pA-5)+'%</div><div class=box>'+b+' +4.5 '+(pB+5)+'%</div></div><b>Total 1&2</b><div class=grid><div class=box>Total '+a+' Over 108.5 56%</div><div class=box>Total '+b+' Over 107.5 53%</div></div>';document.getElementById('rb').innerHTML=h}"
 h+="function gh(){var a=ha.value,b=hb.value;var h='';h+='<div class=v1n2>V1 48% - NUL 18% - V2 34%</div><b>Over/Under</b><div class=grid><div class=\"box c\">Over 5.5 62%</div><div class=box>Under 5.5 38%</div></div><b>Handicap</b><div class=grid><div class=box>'+a+' -1.5 38%</div><div class=box>'+b+' +1.5 61%</div></div><b>Total 1&2</b><div class=grid><div class=box>Total '+a+' Over 2.5 58%</div><div class=box>Total '+b+' Over 2.5 52%</div></div>';document.getElementById('rh').innerHTML=h}"
 h+="function gt(){var a=ta.value,b=tb.value;var h='';h+='<div class=v1n2>V1 57% - V2 43%</div><b>Total Jeux</b><div class=grid><div class=\"box c\">Over 22.5 59%</div><div class=box>Under 22.5 40%</div></div><b>Handicap</b><div class=grid><div class=box>'+a+' -2.5 54%</div><div class=box>'+b+' +2.5 45%</div></div><b>Total 1&2</b><div class=grid><div class=box>Total '+a+' Over 12.5 55%</div><div class=box>Total '+b+' Over 11.5 51%</div></div>';document.getElementById('rt').innerHTML=h}"
 h+="function gp(){var a=pa.value,b=pb.value;var h='';h+='<div class=v1n2>V1 54% - V2 46%</div><b>Total Points</b><div class=grid><div class=\"box c\">Over 75.5 57%</div><div class=box>Under 75.5 42%</div></div><b>Handicap</b><div class=grid><div class=box>'+a+' -2.5 52%</div><div class=box>'+b+' +2.5 47%</div></div><b>Total 1&2</b><div class=grid><div class=box>Total '+a+' Over 38.5 54%</div><div class=box>Total '+b+' Over 35.5 51%</div></div>';document.getElementById('rp').innerHTML=h}"
 h+="</script></body></html>"
 return HTMLResponse(h)
