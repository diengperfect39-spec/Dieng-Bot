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
    return '''<!DOCTYPE html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><link rel="manifest" href="/manifest.json"><title>Dieng V25</title><style>*{box-sizing:border-box}body{margin:0;font-family:system-ui;background:#06120e;color:#fff}.header{background:#0a2e22;padding:12px;text-align:center}.header h1{margin:0;font-size:11px;font-weight:900;color:#00ff88}.tabs{display:flex;gap:5px;padding:8px;overflow:auto}.tab{padding:8px 12px;border-radius:20px;background:#10261e;color:#888;border:1px solid #00ff8830;font-size:11px;cursor:pointer;white-space:nowrap}.tab.active{background:#00ff88;color:#000;font-weight:900}.top-card{margin:8px;background:linear-gradient(135deg,#10261e,#1a3d2e);border-radius:14px;padding:10px;border:1px solid #00ff8840}.inputs{display:flex;gap:5px;align-items:center;margin-bottom:6px}.inputs input{flex:1;background:#0f2a1e;border:1px solid #00ff8830;border-radius:8px;padding:9px;color:#fff;font-weight:700;text-align:center;font-size:12px}.vs{background:#0a2e22;color:#00ff88;font-weight:900;border-radius:999px;padding:5px 8px;font-size:10px}.btn{width:100%;background:linear-gradient(90deg,#00ff88,#00c853);color:#06120e;border:0;border-radius:8px;padding:10px;font-weight:900;font-size:13px;cursor:pointer}.card{margin:8px;background:#10261e;border-radius:14px;padding:10px;border:1px solid #ffffff12;font-size:12px;line-height:1.5}.grid{display:grid;grid-template-columns:1fr 1fr;gap:5px;margin-top:6px}.grid-3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:5px;margin-top:6px}.box{background:#0a2e22;border:1px solid #00ff8820;border-radius:8px;padding:7px;text-align:center}.box.conseil{border-color:#00ff88;background:#123829;box-shadow:0 0 8px #00ff8850}.box-title{font-weight:900;color:#00ff88;font-size:10px}.box-val{font-size:11px;font-weight:700}.badge{background:#00ff88;color:#06120e;font-weight:900;padding:2px 6px;border-radius:999px;font-size:9px}.v1n2{background:linear-gradient(90deg,#00ff88,#00aaff);color:#000;padding:10px;border-radius:10px;text-align:center;font-weight:900;font-size:14px;margin-bottom:8px}.score-box{background:#123829;border:2px solid #00ff88;border-radius:12px;padding:10px;text-align:center;margin:8px 0}hr{border:0;border-top:1px solid #ffffff15;margin:8px 0}.sec{display:none}.sec.active{display:block}</style></head><body>
<div class="header"><h1>Dieng V25 - FOOT INTACT + BASKET/HOCKEY/TENNIS/PING OVER/UNDER + HANDICAP</h1></div>
<div class="tabs"><div class="tab active" onclick="showTab('foot',this)">⚽ Foot</div><div class="tab" onclick="showTab('basket',this)">🏀 Basket</div><div class="tab" onclick="showTab('hockey',this)">🏒 Hockey</div><div class="tab" onclick="showTab('tennis',this)">🎾 Tennis</div><div class="tab" onclick="showTab('ping',this)">🏓 Ping</div></div>

<div id="foot" class="sec active"><div class="top-card"><div class="inputs"><input id="fa" value="AEK Athenes"><div class="vs">VS</div><input id="fb" value="Real Madrid"></div><button class="btn" onclick="genFoot()">ANALYSER FOOTBALL</button></div><div class="card" id="rfoot">Clique ANALYSER</div></div>
<div id="basket" class="sec"><div class="top-card"><div class="inputs"><input id="ba" value="Lakers"><div class="vs">VS</div><input id="bb" value="Warriors"></div><button class="btn" onclick="genBasket()">ANALYSER BASKET</button></div><div class="card" id="rbasket"></div></div>
<div id="hockey" class="sec"><div class="top-card"><div class="inputs"><input id="ha" value="Maple Leafs"><div class="vs">VS</div><input id="hb" value="Oilers"></div><button class="btn" onclick="genHockey()">ANALYSER HOCKEY</button></div><div class="card" id="rhockey"></div></div>
<div id="tennis" class="sec"><div class="top-card"><div class="inputs"><input id="ta" value="Alcaraz"><div class="vs">VS</div><input id="tb" value="Sinner"></div><button class="btn" onclick="genTennis()">ANALYSER TENNIS</button></div><div class="card" id="rtennis"></div></div>
<div id="ping" class="sec"><div class="top-card"><div class="inputs"><input id="pa" value="Fan Zhendong"><div class="vs">VS</div><input id="pb" value="Harimoto"></div><button class="btn" onclick="genPing()">ANALYSER PING</button></div><div class="card" id="rping"></div></div>

<script>
function showTab(id,el){document.querySelectorAll('.sec').forEach(s=>s.classList.remove('active'));document.querySelectorAll('.tab').forEach(t=>t.classList.remove('active'));document.getElementById(id).classList.add('active');el.classList.add('active')}
let DB={"real madrid":{last:[2,3,1,2,4],avg:2.4,fo:1.18,elo:1915},"aek athenes":{last:[0,1,2,0,1],avg:0.8,fo:0.83,elo:1620}};
function hashCode(s){let h=0;for(let i=0;i<s.length;i++)h=s.charCodeAt(i)+((h<<5)-h);return Math.abs(h)}
function fact(n){if(n<=1)return 1;let r=1;for(let i=2;i<=n;i++)r*=i;return r}
function pois(l,k){return (Math.pow(l,k)*Math.exp(-l))/fact(k)}
function getTeam(n){let k=n.toLowerCase();for(let x in DB){if(k.includes(x)||x.includes(k))return DB[x]}let h=hashCode(k);let avg=0.6+(h%20)/10;let la=[];for(let i=0;i<5;i++)la.push((h>>i)%4);return {last:la,avg:avg,fo:0.85+(h%30)/100,elo:1650+(h%100)}}

// ===== FOOTBALL = INTACT V24 =====
function genFoot(){
let tA=document.getElementById('fa').value,tB=document.getElementById('fb').value;
let A=getTeam(tA),B=getTeam(tB),seed=hashCode(tA+tB);
let xgA=Number((A.avg*A.fo).toFixed(2)),xgB=Number((B.avg*B.fo).toFixed(2)),tot=xgA+xgB;
let d=(A.elo-B.elo)+(A.fo-B.fo)*100,pA=1/(1+Math.pow(10,-d/400)),v1=(pA*84).toFixed(1),v2=((1-pA)*84).toFixed(1),vn="16.0";
let scores=[];for(let i=0;i<=4;i++){for(let j=0;j<=4;j++){let p=pois(xgA,i)*pois(xgB,j)*100;scores.push({s:`${i}-${j}`,p:p})}}scores.sort((a,b)=>b.p-a.p);let s1=scores[0],s2=scores[1];
let pTot=[];for(let k=0;k<=7;k++)pTot[k]=pois(tot,k);let sum=pTot.reduce((a,b)=>a+b,0);
let totProbs=pTot.map((p,i)=>({goals:i,prob:(p/sum)*100}));totProbs.sort((a,b)=>b.prob-a.prob);let bestTotal=totProbs[0];
let multiRanges=[{n:"1 But",prob:totProbs.find(x=>x.goals==1)?.prob||0},{n:"2 Buts",prob:totProbs.find(x=>x.goals==2)?.prob||0},{n:"3 Buts",prob:totProbs.find(x=>x.goals==3)?.prob||0},{n:"1-2 Buts",prob:totProbs.filter(x=>x.goals>=1&&x.goals<=2).reduce((a,b)=>a+b.prob,0)},{n:"2-3 Buts",prob:totProbs.filter(x=>x.goals>=2&&x.goals<=3).reduce((a,b)=>a+b.prob,0)},{n:"2-4 Buts",prob:totProbs.filter(x=>x.goals>=2&&x.goals<=4).reduce((a,b)=>a+b.prob,0)},{n:"Over 2.5",prob:totProbs.filter(x=>x.goals>=3).reduce((a,b)=>a+b.prob,0)},{n:"Under 3.5",prob:totProbs.filter(x=>x.goals<=3).reduce((a,b)=>a+b.prob,0)}];
multiRanges.sort((a,b)=>b.prob-a.prob);let bestMulti=multiRanges[0];let grid="";multiRanges.forEach(r=>{let isBest=r.n===bestMulti.n;grid+=`<div class="box ${isBest?'conseil':''}"><div class="box-title">${r.n}</div><div class="box-val">${r.prob.toFixed(1)}% ${isBest?'<br><span class=badge>CONSEIL</span>':''}</div></div>`});
let cor=(4.5+tot*1.4).toFixed(1),tirTot=(8+tot*1.8).toFixed(0),tirCad=(2.5+tot*0.8).toFixed(0),fau=(11+(seed%7)).toFixed(0),car=(2.2+(seed%3)*0.5).toFixed(1);
document.getElementById('rfoot').inner
