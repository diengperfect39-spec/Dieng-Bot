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
    html = '''<!DOCTYPE html><html lang=fr><head><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1"><title>Dieng Predict V13 - Full Stats</title><style>*{box-sizing:border-box}body{margin:0;font-family:Inter,sans-serif;background:#06120e;color:#fff}.header{background:#0a2e22;padding:12px}.top-card{margin:12px;background:#10261e;border-radius:20px;padding:12px;border:1px solid #00ff8840}.inputs{display:flex;gap:8px}.inputs input{flex:1;background:#0f2a1e;border:1px solid #00ff8830;border-radius:12px;padding:12px;color:#fff;font-weight:700;text-align:center}.btn{width:100%;margin-top:10px;background:#00ff88;color:#06120e;border:0;border-radius:12px;padding:14px;font-weight:900}.card{margin:12px;background:#10261e;border-radius:18px;padding:14px;font-size:13px;line-height:1.6}.badge{background:#00ff88;color:#06120e;font-weight:900;padding:4px 10px;border-radius:999px;font-size:11px}</style></head><body><div class=header><h1>Dieng Predict V13 - Cartons + Tirs cadres OK</h1></div><div class=top-card><div class=inputs><input id=teamA value=Barcelona><div>VS</div><input id=teamB value=Aston Villa></div><button class=btn onclick=generate()>ANALYSER + FIFA 23 PENALTY</button></div><div class=card id=output>Clique ANALYSER - Version avec Cartons et Tirs cadres</div><script>function generate(){let A=document.getElementById("teamA").value||"Equipe A";let B=document.getElementById("teamB").value||"Equipe B";let xG1=(Math.random()*0.8+0.9).toFixed(2);let xG2=(Math.random()*0.7+0.6).toFixed(2);let corners=(Math.random()*3+9.5).toFixed(1);let cartons=(Math.random()*1.5+3.8).toFixed(1);let tirs=(Math.random()*4+9).toFixed(1);let over25=Math.floor(Math.random()*15+55);let btts=Math.floor(Math.random()*15+48);document.getElementById("output").innerHTML="<b>xG "+A+":</b> "+xG1+" | <b>xG "+B+":</b> "+xG2+"<br><br>Over 2.5: "+over25+"%<br>BTTS: "+btts+"%<br><br>🚩 Corners: "+corners+"<br>🟨 Cartons: Over "+cartons+"<br>🎯 Tirs cadres: "+tirs+" (Over 8.5)<br><br>💡 PRONO: BTTS Oui + Over 1.5";}</script></body></html>'''
    return html
