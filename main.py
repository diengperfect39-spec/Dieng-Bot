from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse, Response
app = FastAPI()

@app.get('/manifest.json')
def manifest():
    return JSONResponse({'name':'Dieng V25','short_name':'Dieng','start_url':'/','display':'standalone','background_color':'#06120e','theme_color':'#00ff88'})

@app.get('/sw.js')
def sw():
    return Response("self.addEventListener('install', e=>self.skipWaiting());", media_type='application/javascript')

@app.get('/', response_class=HTMLResponse)
def home():
    parts = [
    "<!DOCTYPE html><html><head><meta charset='utf-8'>",
    "<meta name='viewport' content='width=device-width,initial-scale=1'>",
    "<title>Dieng V25 OK</title><style>",
    "*{box-sizing:border-box}body{margin:0;font-family:system-ui;background:#06120e;color:#fff}",
    ".header{background:#0a2e22;padding:12px;text-align:center}.header h1{margin:0;font-size:11px;color:#00ff88;font-weight:900}",
    ".tabs{display:flex;gap:5px;padding:8px;overflow:auto}.tab{padding:8px 12px;border-radius:20px;background:#10261e;color:#888;border:1px solid #00ff8830;font-size:11px;cursor:pointer;white-space:nowrap}.tab.active{background:#00ff88;color:#000;font-weight:900}",
    ".top-card{margin:8px;background:#10261e;border-radius:14px;padding:10px;border:1px solid #00ff8840}.inputs{display:flex;gap:5px}.inputs input{flex:1;background:#0f2a1e;border:1px solid #00ff8830;border-radius:8px;padding:9px;color:#fff;font-weight:700;text-align:center}",
    ".vs{background:#0a2e22;color:#00ff88;font-weight:900;border-radius:999px;padding:5px 8px}.btn{width:100%;background:linear-gradient(90deg,#00ff88,#00c853);color:#06120e;border:0;border-radius:8px;padding:10px;font-weight:900;cursor:pointer}",
    ".card{margin:8px;background:#10261e;border-radius:14px;padding:10px;border:1px solid #ffffff12;font-size:12px}.grid{display:grid;grid-template-columns:1fr 1fr;gap:5px;margin-top:6px}.box{background:#0a2e22;border:1px solid #00ff8820;border-radius:8px;padding:7px;text-align:center}.box.conseil{border-color:#00ff88;background:#123829}.box-title{font-weight:900;color:#00ff88;font-size:10px}.box-val{font-size:11px;font-weight:700}",
    ".v1n2{background:linear-gradient(90deg,#00ff88,#00aaff);color:#000;padding:10px;border-radius:10px;text-align:center;font-weight:900;font-size:14px;margin-bottom:8px}.score-box{background:#123829;border:2px solid #00ff88;border-radius:12px;padding:10px;text-align:center;margin:8px 0}hr{border:0;border-top:1px solid #ffffff15;margin:8px 0}.sec{display:none}.sec.active{display:block}</style></head><body>",
    "<div class='header'><h1>Dieng V25 OK - FOOT INTACT + AUTRES SPORTS</h1></div>",
    "<div class='tabs'><div class='tab active' onclick=\"showTab('foot',this)\">Foot</div><div class='tab' onclick=\"showTab('basket',this)\">Basket</div><div class='tab' onclick=\"showTab('hockey',this)\">Hockey</div><div class='tab' onclick=\"showTab('tennis',this)\">Tennis</div><div class='tab' onclick=\"showTab('ping',this)\">Ping</div></div>",
    "<div id='foot' class='sec active'><div class='top-card'><div class='inputs'><input id='fa' value='AEK Athenes'><div class='vs'>VS</div><input id='fb' value='Real Madrid'></div><button class='btn' onclick='genFoot()'>ANALYSER FOOTBALL</button></div><div class='card' id='rfoot'></div></div>",
    "<div id='basket' class='sec'><div class='top-card'><div class='inputs'><input id='ba' value='Lakers'><div class='vs'>VS</div><input id='bb' value='Warriors'></div><button class='btn' onclick='genBasket()'>ANALYSER BASKET</button></div><div class='card' id='rbasket'></div></div>",
    "<div id='hockey' class='sec'><div class='top-card'><div class='inputs'><input id='ha' value='Maple Leafs'><div class='vs'>VS</div><input id='hb' value='Oilers'></div><button class='btn' onclick='genHockey()'>ANALYSER HOCKEY</button></div><div class='card' id='rhockey'></div></div>",
    "<div id='tennis' class='sec'><div class='top-card'><div class='inputs'><input id='ta' value='Alcaraz'><div class='vs'>VS</div><input id='tb' value='Sinner'></div><button class='btn' onclick='genTennis()'>ANALYSER TENNIS</button></div><div class='card' id='rtennis'></div></div>",
    "<div id='ping' class='sec'><div class='top-card'><div class='inputs'><input id='pa' value='Fan Zhendong'><div class='vs'>VS</div><input id='pb' value='Harimoto'></div><button class='btn' onclick='genPing()'>ANALYSER PING</button></div><div class='card' id='rping'></div></div>",
    "<script>function showTab(id,el){document.querySelectorAll('.sec').forEach(s=>s.classList.remove('active'));document.querySelectorAll('.tab').forEach(t=>t.classList.remove('active'));document.getElementById(id).classList.add('active');el.classList.add('active')}",
    "function hashCode(s){let h=0;for(let i=0;i<s.length;i++)h=s.charCodeAt(i)+((h<<5)-h);return Math.abs(h)}function fact(n){if(n<=1)return 1;let r=1;for(let i=2;i<=n;i++)r*=i;return r}function pois(l,k){return (Math.pow(l,k)*Math.exp(-l))/fact(k)}",
    "function getTeam(n){let h=hashCode(n);let avg=0.6+(h%20)/10;let la=[];for(let i=0;i<5;i++)la.push((h>>i)%4);return {last:la,avg:avg,fo:0.85+(h%30)/100,elo:1650+(h%100)}}",
    "function genFoot(){let tA=document.getElementById('fa').value,tB=document.getElementById('fb').value;let A=getTeam(tA),B=getTeam(tB),seed=hashCode(tA+tB);let xgA=Number((A.avg*A.fo).toFixed(2)),xgB=Number((B.avg*B.fo).toFixed(2)),tot=xgA+xgB;let d=(A.elo-B.elo)+(A.fo-B.fo)*100,pA=1/(1+Math.pow(10,-d/400)),v1=(pA*84).toFixed(1),v2=((1-pA)*84).toFixed(1);let scores=[];for(let i=0;i<=4;i++){for(let j=0;j<=4;j++){let p=pois(xgA,i)*pois(xgB,j)*100;scores.push({s:i+'-'+j,p:p})}}scores.sort((a,b)=>b.p-a.p);let s1=scores[0],s2=scores[1];let cor=(4.5+tot*1.4).toFixed(1),tirTot=(8+tot*1.8).toFixed(0),tirCad=(2.5+tot*0.8).toFixed(0),fau=(11+(seed%7)).toFixed(0),car=(2.2+(seed%3)*0.5).toFixed(1);document.getElementById('rfoot').innerHTML='<div class=v1n2>V1 '+v1+'% - NUL 16% - V2 '+v2+'%</div><div class=score-box><b>2 SCORES EXACTS</b><br><b style=font-size:20px>'+s1.s+' ('+s1.p.toFixed(1)+'%)</b> - <b style=font-size:20px>'+s2.s+' ('+s2.p.toFixed(1)+'%)</b><br>xG '+xgA+' + '+xgB+' = '+tot.toFixed(2)+'</div><hr>Corners ~'+cor+' | Cartons ~'+car+' | Fautes ~'+fau+'<br>Tirs Totaux ~'+tirTot+' | Tirs Cadres ~'+tirCad;}",
    "function genBasket(){let a=document.getElementById('ba').value,b=document.getElementById('bb').value,seed=hashCode(a+b),pA=55+(seed%10),pB=100-pA;document.getElementById('rbasket').innerHTML='<div class=v1n2>V1 '+pA+'% - V2 '+pB+'%</div><hr><b>TOTAL OVER/UNDER</b><div class=grid><div class=box conseil><div class=box-title>Over 215.5</div><div class=box-val>58.2% CONSEIL</div></div><div class=box><div class=box-title>Under 215.5</div><div class=box-val>41.8%</div></div></div><hr><b>HANDICAP</b><div class=grid><div class=box><div class=box-title>'+a+' -4.5</div><div class=box-val>'+(pA-5)+' %</div></div><div class=box><div class=box-title>'+b+' +4.5</div><div class=box-val>'+(pB+5)+' %</div></div></div><hr><b>TOTAL 1 & 2</b><div class=grid><div class=box><div class=box-title>Total '+a+' Over 108.5</div><div class=box-val>56.3%</div></div><div class=box><div class=box-title>Total '+b+' Over 107.5</div><div class=box-val>53.8%</div></div></div>';}",
    "function genHockey(){let a=document.getElementById('ha').
