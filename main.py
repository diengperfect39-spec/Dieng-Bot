from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse, Response
app = FastAPI()

@app.get("/manifest.json")
def manifest():
    return JSONResponse({"name":"Dieng V25","short_name":"Dieng","start_url":"/","display":"standalone","background_color":"#06120e","theme_color":"#00ff88"})

@app.get("/sw.js")
def sw():
    return Response("self.addEventListener('install', e=>self.skipWaiting());", media_type="application/javascript")

@app.get("/", response_class=HTMLResponse)
def home():
    html_code = """
<!DOCTYPE html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><link rel="manifest" href="/manifest.json"><title>Dieng V25</title><style>*{box-sizing:border-box}body{margin:0;font-family:system-ui;background:#06120e;color:#fff}.header{background:#0a2e22;padding:12px;text-align:center}.header h1{margin:0;font-size:11px;font-weight:900;color:#00ff88}.tabs{display:flex;gap:5px;padding:8px;overflow:auto}.tab{padding:8px 12px;border-radius:20px;background:#10261e;color:#888;border:1px solid #00ff8830;font-size:11px;cursor:pointer;white-space:nowrap}.tab.active{background:#00ff88;color:#000;font-weight:900}.top-card{margin:8px;background:linear-gradient(135deg,#10261e,#1a3d2e);border-radius:14px;padding:10px;border:1px solid #00ff8840}.inputs{display:flex;gap:5px;align-items:center;margin-bottom:6px}.inputs input{flex:1;background:#0f2a1e;border:1px solid #00ff8830;border-radius:8px;padding:9px;color:#fff;font-weight:700;text-align:center;font-size:12px}.vs{background:#0a2e22;color:#00ff88;font-weight:900;border-radius:999px;padding:5px 8px;font-size:10px}.btn{width:100%;background:linear-gradient(90deg,#00ff88,#00c853);color:#06120e;border:0;border-radius:8px;padding:10px;font-weight:900;font-size:13px;cursor:pointer}.card{margin:8px;background:#10261e;border-radius:14px;padding:10px;border:1px solid #ffffff12;font-size:12px;line-height:1.5}.grid{display:grid;grid-template-columns:1fr 1fr;gap:5px;margin-top:6px}.grid-3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:5px;margin-top:6px}.box{background:#0a2e22;border:1px solid #00ff8820;border-radius:8px;padding:7px;text-align:center}.box.conseil{border-color:#00ff88;background:#123829;box-shadow:0 0 8px #00ff8850}.box-title{font-weight:900;color:#00ff88;font-size:10px}.box-val{font-size:11px;font-weight:700}.badge{background:#00ff88;color:#06120e;font-weight:900;padding:2px 6px;border-radius:999px;font-size:9px}.v1n2{background:linear-gradient(90deg,#00ff88,#00aaff);color:#000;padding:10px;border-radius:10px;text-align:center;font-weight:900;font-size:14px;margin-bottom:8px}.score-box{background:#123829;border:2px solid #00ff88;border-radius:12px;padding:10px;text-align:center;margin:8px 0}hr{border:0;border-top:1px solid #ffffff15;margin:8px 0}.sec{display:none}.sec.active{display:block}</style></head><body>
<div class="header"><h1>Dieng V25 - FOOT INTACT + AUTRES SPORTS OVER UNDER HANDICAP</h1></div>
<div class="tabs"><div class="tab active" onclick="showTab('foot',this)">Foot</div><div class="tab" onclick="showTab('basket',this)">Basket</div><div class="tab" onclick="showTab('hockey',this)">Hockey</div><div class="tab" onclick="showTab('tennis',this)">Tennis</div><div class="tab" onclick="showTab('ping',this)">Ping</div></div>
<div id="foot" class="sec active"><div class="top-card"><div class="inputs"><input id="fa" value="AEK Athenes"><div class="vs">VS</div><input id="fb" value="Real Madrid"></div><button class="btn" onclick="genFoot()">ANALYSER FOOTBALL</button></div><div class="card" id="rfoot">Clique ANALYSER</div></div>
<div id="basket" class="sec"><div class="top-card"><div class="inputs"><input id="ba" value="Lakers"><div
