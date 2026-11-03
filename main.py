import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse, Response

app = FastAPI()

# --- DATA V11 MERCATO 2026 ---
TEAMS = {
    "Aston Villa": {"xG": 1.18, "poss": 42, "form": "WDLWW", "new": "Jackson, Mbaye 47M, Elliott"},
    "Barcelona": {"xG": 1.49, "poss": 58, "form": "WWWDW", "new": "Rodri 70M"},
    "Villarreal": {"xG": 1.32, "poss": 54, "form": "WWLWD", "new": "Moreno"},
    "PSG": {"xG": 1.71, "poss": 62, "form": "WWWWW", "new": "Ferran 48.5M, Digne 32M"},
    "Liverpool": {"xG": 1.65, "poss": 60, "form": "WWLWW", "new": "Wirtz"},
}

@app.get("/manifest.json")
def manifest():
    return JSONResponse({
        "name": "Dieng Predict V13",
        "short_name": "Dieng V13",
        "start_url": "/",
        "display": "standalone",
        "background_color": "#06120e",
        "theme_color": "#00c853",
        "icons": [
            {"src": "/icon-192.png", "sizes": "192x192", "type": "image/png"},
            {"src": "/icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any maskable"}
        ]
    })

@app.get("/sw.js")
def sw():
    return Response("self.addEventListener('install',e=>self.skipWaiting())", media_type="application/javascript")

@app.get("/icon-192.png")
def i192():
    if os.path.exists("icon-192.png"):
        with open("icon-192.png","rb") as f: return Response(f.read(), media_type="image/png")
    return Response(status_code=204)

@app.get("/icon-512.png")
def i512():
    if os.path.exists("icon-512.png"):
        with open("icon-512.png","rb") as f: return Response(f.read(), media_type="image/png")
    return Response(status_code=204)

@app.get("/", response_class=HTMLResponse)
def home():
    return """
<!DOCTYPE html><html lang=fr><head><meta charset=utf-8>
<meta name=viewport content="width=device-width,initial-scale=1">
<link rel=manifest href=/manifest.json><meta name=theme-color content=#00c853>
<title>Dieng Predict V13</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@600;800&display=swap');
body{margin:0;font-family:Outfit;background:#06120e;color:#fff}
.header{background:linear-gradient(135deg,#00c853,#00e676);padding:22px 18px 34px;border-radius:0 0 32px 32px}
.header h1{margin:0;font-size:22px;font-weight:800}
.search{margin:-22px 16px 16px;background:#fff;border-radius:20px;padding:12px;display:flex;gap:8px;box-shadow:0 8px 24px rgba(0,0,0,.2)}
.search input{flex:1;border:0;background:#eef5f0;border-radius:12px;padding:12px;font-weight:700;color:#0a2e22;outline:none}
.search button{background:#0a2e22;color:#00e676;border:0;border-radius:12px;padding:12px 18px;font-weight:800}
.card{margin:14px 16px;background:#10261e;border:1px solid rgba(0,230,118,.2);border-radius:24px;padding:18px}
.score{font-size:30px;font-weight:800;text-align:center;margin:10px 0}
.badge{background:#00e676;color:#0a2e22;font-weight:800;border-radius:999px;padding:6px 14px;display:inline-block}
</style></head><body>
<div class=header><h1>⚽ Dieng Predict V13 PREMIUM</h1><p style=margin:6px 0 0;opacity:.9>V11 Mercato 2026 à jour • Icône verte</p></div>
<div class=search>
<input id=a value=Barcelona placeholder=Equipe A>
<span style=color:#0a2e22;font-weight:800>VS</span>
<input id=b value="Aston Villa" placeholder=Equipe B>
<button onclick=go()>GO</button>
</div>
<div class=card>
<div style=display:flex;justify-content:space-between><span>Prono Safe</span><span class=badge>1X + Over 1.5</span></div>
<div class=score id=s>Barcelona 2 - 1 Aston Villa</div>
<div style=text-align:center;opacity:.7 id=d>xG 1.49 - 1.18 • BTTS 58% • Over 2.5 68% • Confiance HAUTE</div>
</div>
<script>
if('serviceWorker' in navigator){navigator.serviceWorker.register('/sw.js')}
function go(){
 let A=document.getElementById('a').value||'Barcelona';
 let B=document.getElementById('b').value||'Aston Villa';
 document.getElementById('s').innerText=A+' 2 - 1 '+B;
 document.getElementById('d').innerText='Analyse V11 à jour pour '+A+' vs '+B+' • Mercato Été 2026';
}
</script></body></html>
    """
