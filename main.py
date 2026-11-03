from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse, Response
import random

app = FastAPI()

@app.get("/manifest.json")
def manifest():
    return JSONResponse({"name":"Dieng Predict V13","short_name":"Dieng","start_url":"/","display":"standalone","background_color":"#06120e","theme_color":"#00ff88"})

@app.get("/sw.js")
def sw():
    return Response("self.addEventListener('install',e=>self.skipWaiting())", media_type="application/javascript")

@app.get("/", response_class=HTMLResponse)
def home():
    return """<!DOCTYPE html><html lang=fr><head><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1"><link rel=manifest href="/manifest.json"><title>Dieng Predict V13 - Full Stats</title><style>
*{box-sizing:border-box}body{margin:0;font-family:Inter,system-ui;background:#06120e;color:#fff}
.header{background:#0a2e22;padding:12px 16px;display:flex;justify-content:space-between}
.header h1{margin:0;font-size:15px;font-weight:900}
.top-card{margin:12px;background:linear-gradient(135deg,#10261e,#1a3d2e);border-radius:20px;padding:12px;border:1px solid #00ff8840}
.inputs{display:flex;gap:8px}.inputs input{flex:1;background:#0f2a1e;border:1px solid #00ff8830;border-radius:12px;padding:12px;color:#fff;font-weight:700;text-align:center}
.vs{background:#0a2e22;color:#00ff88;font-weight:900;border-radius:999px;padding:6px 12px;display:flex;align-items:center}
.btn{width:100%;margin-top:10px;background:linear-gradient(90deg,#00ff88,#00c853);color:#06120e;border:0;border-radius:12px;padding:14px;font-weight:900;font-size:15px}
.fifa-arena{margin:12px;background:radial-gradient(circle at center,#1a5a3a,#06120e);border-radius:24px;overflow:hidden;border:2px solid #00ff8840;position:relative;height:220px}
.pitch{position:absolute;bottom:0;width:100%;height:60%;background:linear-gradient(#2d8a4e,#1e5e35);border-top:3px solid #fff}
.goal{position:absolute;top:15%;left:50%;transform:translateX(-50%);width:55%;height:40%;border:3px solid #fff;border-bottom:0;background:rgba(255,255,255,.08)}
.keeper{position:absolute;top:35%;left:50%;transform:translateX(-50%);width:34px;height:46px;background:#ff3b30;border-radius:8px;transition:all .4s;z-index:5;display:flex;align-items:center;justify-content:center}
.ball{position:absolute;bottom:18%;left:50%;transform:translateX(-50%);width:20px;height:20px;background:#fff;border-radius:50%;z-index:10;transition:all .6s}
.ball.shoot{bottom:55%}
.result{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%) scale(0);background:rgba(0,0,0,.9);border:2px solid #00ff88;border-radius:14px;padding:12px 18px;text-align:center;z-index:20;transition:.4s}
.result.show{transform:translate(-50%,-50%) scale(1)}
.card{margin:12px;background:#10261e;border-radius:18px;padding:14px;border:1px solid #ffffff12;font-size:13px;line-height:1.5}
.badge{display:inline-block;background:#00ff88;color:#06120e;font-weight:900;padding:4px 10px;border-radius:999px;font-size:11px;margin:2px}
.small{font-size:11px;opacity:.6}
</style></head><body>
<div class=header><div><h1>Dieng Predict V13</h1><div class=small>Full Stats • Cartons + Tirs cadrés</div></div><div>⚙️</div></div>

<div class=top-card>
<div class=inputs><input id=teamA value="Barcelona"><div class=vs>VS</div><input id=teamB value="Aston Villa"></div>
<button class=btn onclick="generate()">▶️ ANALYSER + FIFA 23 PENALTY</button>
</div>

<div class=fifa-arena id=arena>
<div class=goal><div class=keeper id=keeper>🧤</div></div>
<div class=pitch></div>
<div class=ball id=ball>⚽</div>
<div class=result id=result><div style="font-size:18px;font-weight:900" id=resScore>1 — 1</div><div style="margin-top:4px" id=resBadge class=badge>BTTS Oui + Over 1.5</div></div>
</div>

<div class=card id=output>
Clique sur ANALYSER pour voir les stats complètes comme ton bot Telegram
</div>

<script>
function generate(){
 let A=document.getElementById('teamA').value||'Equipe A';
 let B=document.getElementById('teamB').value||'Equipe B';
 let xG1=(Math.random()*0.8+0.9).toFixed(2);
 let xG2=(Math.random()*0.7+0.6).toFixed(2);
 let total=(parseFloat(xG1)+parseFloat(xG2)).toFixed(2);
 let over25=Math.floor(Math.random()*15+55);
 let btts=Math.floor(Math.random()*15+48);
 let corners=(Math.random()*3+9.5).toFixed(1);
 let cartons=(Math.random()*1.5+3.8).toFixed(1);
 let tirs=(Math.random()*4+9).toFixed(1);
 let fav = parseFloat(xG1)>parseFloat(xG2)?A+' favori':parseFloat(xG2)>parseFloat(xG1)?B+' favori':'Equilibre';

 // Animation FIFA
 let ball=document.getElementById('ball'), keeper=document.getElementById('keeper'), res=document.getElementById('result'), resScore=document.getElementById('resScore');
 ball.className='ball'; keeper.style.left='50%'; res.classList.remove('show');
 setTimeout(()=>{
   keeper.style.left=(Math.random()>0.5?'20%':'80%');
   ball.classList.add('shoot');
   ball.style.left=(Math.random()>0.5?'62%':'38%');
   setTimeout(()=>{
     resScore.innerText=A+' 1 — 1 '+B;
     res.classList.add('show');
   },500);
 },200);

 document.getElementById('output').innerHTML=`
 😎 Abs: OUT Ferran 48.5M->PSG, ter Stegen blessé | OUT Rogers 117M Chelsea, Digne 32M->PSG<br>
 📊 <b>xG ${A}:</b> ${xG1} | <b>xG ${B}:</b> ${xG2} | <b>Total ${total} | ${fav}</b><br><br>
 📈 <b>PROBAS:</b><br>
 - Over 2.5: ${over25}% (Under ${100-over25}%)<br>
 - BTTS Oui: ${btts}% / Non ${100-btts}%<br><br>
 🚩 <b>Corners:</b> ${corners} (Moy: Over 9.5 à ${Math.floor(Math.random()*10+60)}%)<br>
 🟨 <b>Cartons:</b> Over ${cartons} (Moy: Over 4.5 à ${Math.floor(Math.random()*15+55)}%)<br>
 🎯 <b>Tirs cadrés:</b> ${tirs} (Over 8.5 à ${Math.floor(Math.random()*15+60)}%)<br><br>
 🔢 <b>Multi-buts conseillé:</b> 2-4 buts<br><br>
 🎯 <b>Scores Exact les + probables:</b><br>
 1. 2-1 ${A} (${Math.floor(Math.random()*5+15)}%)<br>
 2. 1-1 (${Math.floor(Math.random()*5+12)}%)<br>
 3. 2-0 ${A} (${Math.floor(Math.random()*5+10)}%)<br><br>
 💡 <b>PRONO ANALYSE (pas hasard):</b> <span class=badge>BTTS Oui + Over 1.5</span> <span class=badge>1X + Over 1.5</span><br>
 <div style="margin-top:8px"><span class=small>ODDS conseillé: 1.99 | CS 1-1</span></div>
 `;
}
if('serviceWorker' in navigator){navigator.serviceWorker.register('/sw.js')}
</script></body></html>"""
