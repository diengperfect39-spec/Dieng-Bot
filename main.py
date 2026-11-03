from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse, Response

app = FastAPI()

@app.get("/manifest.json")
def manifest():
    return JSONResponse({
        "name": "Dieng Predict FIFA 23 Penalty",
        "short_name": "Dieng FIFA",
        "start_url": "/",
        "display": "standalone",
        "background_color": "#06120e",
        "theme_color": "#00ff88"
    })

@app.get("/sw.js")
def sw():
    return Response("self.addEventListener('install',e=>self.skipWaiting())", media_type="application/javascript")

@app.get("/", response_class=HTMLResponse)
def home():
    return """<!DOCTYPE html>
<html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1">
<link rel="manifest" href="/manifest.json">
<title>Dieng Predict - FIFA 23 Penalty</title>
<style>
*{box-sizing:border-box}body{margin:0;font-family:Inter,sans-serif;background:#06120e;color:#fff;overflow-x:hidden}
.header{background:#0a2e22;padding:12px 16px;display:flex;justify-content:space-between;align-items:center}
.header h1{font-size:16px;margin:0;font-weight:900}.header span{font-size:10px;opacity:.6}
.top-card{margin:12px;background:linear-gradient(135deg,#10261e,#1a3d2e);border-radius:20px;padding:12px;border:1px solid #00ff8840}
.inputs{display:flex;gap:8px;align-items:center}
.inputs input{flex:1;background:#0f2a1e;border:1px solid #00ff8830;border-radius:12px;padding:12px;color:#fff;font-weight:700;text-align:center}
.vs{background:#0a2e22;color:#00ff88;font-weight:900;border-radius:999px;padding:6px 12px}
.btn-green{width:100%;margin-top:10px;background:linear-gradient(90deg,#00ff88,#00c853);color:#06120e;border:0;border-radius:12px;padding:14px;font-weight:900;font-size:15px}
.fifa-arena{margin:12px;background:radial-gradient(circle at center,#1a5a3a,#06120e);border-radius:24px;overflow:hidden;border:2px solid #00ff8840;position:relative;height:380px}
.pitch{position:absolute;bottom:0;width:100%;height:60%;background:linear-gradient(#2d8a4e,#1e5e35);border-top:4px solid #fff}
.goal{position:absolute;top:20%;left:50%;transform:translateX(-50%);width:60%;height:45%;border:4px solid #fff;border-bottom:0;background:rgba(255,255,255,.1);display:flex;justify-content:center}
.keeper{position:absolute;top:35%;left:50%;transform:translateX(-50%);width:36px;height:50px;background:#ff3b30;border-radius:8px;transition:all .4s cubic-bezier(.68,-0.55,.27,1.55);z-index:5}
.keeper.dive-left{left:20% !important;transform:rotate(-30deg)}
.keeper.dive-right{left:80% !important;transform:rotate(30deg)}
.ball{position:absolute;bottom:18%;left:50%;transform:translateX(-50%);width:22px;height:22px;background:#fff;border-radius:50%;box-shadow:0 0 10px #000;z-index:10;transition:all .6s cubic-bezier(.2,.8,.3,1)}
.ball.shoot{bottom:58%;}
.trajectory{position:absolute;bottom:20%;left:50%;width:2px;height:0;background:linear-gradient(to top,rgba(255,255,255,0),rgba(255,255,255,.8));transform:translateX(-50%);transition:height .3s}
.result-banner{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%) scale(0);background:rgba(0,0,0,.85);border:2px solid #00ff88;border-radius:16px;padding:16px 24px;text-align:center;z-index:20;transition:transform .4s cubic-bezier(.68,-0.55,.27,1.55)}
.result-banner.show{transform:translate(-50%,-50%) scale(1)}
.card{margin:12px;background:#10261e;border-radius:20px;padding:14px;border:1px solid #ffffff0f}
.badge{display:inline-block;background:#00ff88;color:#06120e;font-weight:900;padding:6px 12px;border-radius:999px;font-size:12px}
</style></head><body>
<div class=header><div><h1>Dieng Predict V11</h1><span>AI Football • FIFA 23 Penalty Engine</span></div><div style="font-size:20px">⚙️</div></div>

<div class=top-card>
<div class=inputs><input id=teamA value="LASK Linz"><div class=vs>VS</div><input id=teamB value="Slovan Bratislava"></div>
<button class=btn-green onclick="startFifaPenalty()">▶️ LANCER LE PENALTY FIFA 23</button>
</div>

<div class=fifa-arena id=arena>
<div class=goal><div class=keeper id=keeper>🧤</div></div>
<div class=pitch></div>
<div class=trajectory id=traj></div>
<div class=ball id=ball>⚽</div>
<div class=result-banner id=result>
<div style="font-size:28px;font-weight:900" id=resScore>LASK 1 — 1 SLOVAN</div>
<div style="margin-top:6px;font-size:12px;opacity:.8">FIFA 23 Penalty Simulation</div>
<div style="margin-top:8px" class=badge id=resBadge>BTTS Oui + Over 1.5</div>
</div>
</div>

<div class=card>
<div style="display:flex;justify-content:space-between;align-items:center"><span style="font-weight:800">Prediction: BTTS Oui + Over 1.5</span><span style="color:#00ff88">✅</span></div>
<div style="margin-top:8px;font-size:12px;opacity:.7">BTTS 57% • Over 2.5 58% • xG 1.36 - 1.17 • Possession 51% - 49%</div>
<div style="margin-top:10px;display:flex;gap:16px"><div><div style="font-size:11px;opacity:.6">⚽ xG</div><div style="font-weight:800">1.36</div></div><div><div style="font-size:11px;opacity:.6">🚩 Corners</div><div style="font-weight:800">11.6</div></div><div><div style="font-size:11px;opacity:.6">📊 BTTS</div><div style="font-weight:800">57%</div></div></div>
</div>

<script>
function startFifaPenalty(){
 let A=document.getElementById('teamA').value||'LASK';
 let B=document.getElementById('teamB').value||'Slovan';
 let ball=document.getElementById('ball');
 let keeper=document.getElementById('keeper');
 let traj=document.getElementById('traj');
 let res=document.getElementById('result');
 let resScore=document.getElementById('resScore');
 res.classList.remove('show');
 ball.className='ball';
 keeper.className='keeper';
 traj.style.height='0px';
 setTimeout(()=>{
   // keeper choisit aléatoirement
   let dive=Math.random()>0.5?'dive-left':'dive-right';
   keeper.classList.add(dive);
   traj.style.height='180px';
   ball.classList.add('shoot');
   // tir opposé du keeper = BUT
   let isGoal = dive==='dive-left' ? Math.random()>0.3 : Math.random()>0.3;
   if(isGoal){ ball.style.left='65%'; } else { ball.style.left='25%'; }
   setTimeout(()=>{
     resScore.innerText=A+' 1 — 1 '+B;
     res.classList.add('show');
     if(navigator.vibrate) navigator.vibrate(100);
   },600);
 },200);
}
if('serviceWorker' in navigator){navigator.serviceWorker.register('/sw.js')}
</script>
</body></html>"""
