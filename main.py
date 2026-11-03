from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse, Response
app = FastAPI()
@app.get("/manifest.json")
def manifest():
    return JSONResponse({"name":"Dieng Predict V13","short_name":"Dieng V13","start_url":"/","display":"standalone","background_color":"#06120e","theme_color":"#00c853","icons":[{"src":"/icon-512.png","sizes":"512x512","type":"image/png"}]})
@app.get("/sw.js")
def sw():
    return Response("self.addEventListener('install',e=>self.skipWaiting())", media_type="application/javascript")
@app.get("/", response_class=HTMLResponse)
def home():
    return '''<html><head><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1"><link rel=manifest href=/manifest.json><title>Dieng V13</title><style>body{margin:0;font-family:sans-serif;background:#06120e;color:#fff}.top{background:linear-gradient(135deg,#00c853,#00e676);padding:24px 18px 40px;border-radius:0 0 32px 32px}.box{margin:-24px 16px 16px;background:#fff;border-radius:20px;padding:12px;display:flex;gap:8px}.box input{flex:1;border:0;background:#eef5f0;border-radius:12px;padding:12px;font-weight:700;color:#0a2e22}.box button{background:#0a2e22;color:#00e676;border:0;border-radius:12px;padding:12px 18px;font-weight:800}.card{margin:14px 16px;background:#10261e;border-radius:24px;padding:18px}.score{font-size:28px;font-weight:800;text-align:center}</style></head><body><div class=top><h1>Dieng Predict V13 PREMIUM</h1></div><div class=box><input id=a value=Barcelona><span style=color:#0a2e22;font-weight:800>VS</span><input id=b value="Aston Villa"><button onclick="go()">GO</button></div><div class=card><div class=score id=s>Barcelona 2 - 1 Aston Villa</div></div><script>function go(){let A=document.getElementById('a').value;let B=document.getElementById('b').value;document.getElementById('s').innerText=A+' 2 - 1 '+B;}</script></body></html>'''
