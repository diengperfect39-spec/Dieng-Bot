from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse, Response
import math
app = FastAPI()
@app.get('/manifest.json')
def m(): return JSONResponse({'name':'Dieng'})
@app.get('/sw.js')
def s(): return Response('a', media_type='application/javascript')
def ps(l,k): return (l**k * math.exp(-l)) / math.factorial(k)
def club(s):
 s=s.lower()
 if 'real' in s: return 2.1
 if 'barca' in s or 'city' in s or 'bayern' in s: return 1.95
 if 'aek' in s: return 1.15
 return 1.3
@app.get('/', response_class=HTMLResponse)
def home():
 h="<html><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>"
 h+="<style>body{margin:0;background:#06120e;color:#fff;font-family:system-ui;padding:6px}h1{color:#00ff88;font-size:11px;text-align:center}.tabs{display:flex;gap:4px;overflow:auto;padding:6px}.tab{padding:7px 10px;border-radius:20px;background:#10261e;color:#888;border:1px solid #00ff8830;font-size:10px;cursor:pointer;white-space:nowrap}.tab.a{background:#00ff88;color:#000;font-weight:900}.card{background:#10261e;padding:8px;margin:6px 0;border-radius:12px;border:1px solid #ffffff12;font-size:11px}.top{background:#10261e;border:1px solid #00ff8840;border-radius:12px;padding:8px;margin:6px}.inputs{display:flex;gap:4px}.inputs input{flex:1;background:#0f2a1e;border:1px solid #00ff8830;border-radius:7px;padding:8px;color:#fff;text-align:center;font-weight:700}.small{display:flex;gap:4px;margin-top:4px}.small input{flex:1;background:#0a1f18;border:1px solid #00ff8820;border-radius:6px;padding:6px;color:#9effd0;text-align:center;font-size:10px}.vs{background:#0a2e22;color:#00ff88;font-weight:900;border-radius:999px;padding:4px 7px}.btn{width:100%;background:#00ff88;color:#06120e;border:0;border-radius:7px;padding:9px;font-weight:900;cursor:pointer;margin-top:4px}.v1n2{background:linear-gradient(90deg,#00ff88,#00aaff);color:#000;padding:8px;border-radius:8px;text-align:center;font-weight:900}.sc{background:#123829;border:2px solid #00ff88;border-radius:14px;padding:14px;text-align:center;margin:6px 0}.grid{display:grid;grid-template-columns:1fr 1fr;gap:4px;margin-top:4px}.grid3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:4px}.box{background:#0a2e22;border:1px solid #00ff8820;border-radius:7px;padding:6px;text-align:center;font-size:10px}.box.c{border-color:#00ff88;background:#123829;font-weight:900}.sec{display:none}.sec.a{display:block}label{font-size:9px;color:#00ff88}</style></head><body>"
 h+="<h1>Dieng V39 FULL COMPLET - TOUS SPORTS</h1><div class=tabs><div class='tab a' onclick='sh(\"f\",this)'>Foot PRO</div><div class=tab onclick='sh(\"b\",this)'>Basket PRO</div><div class=tab onclick='sh(\"h\",this)'>Hockey PRO</div><div class=tab onclick='sh(\"t\",this)'>Tennis PRO</div><div class=tab onclick='sh(\"p\",this)'>Ping PRO</div></div>"
 h+="<div id=f class='sec a'><div class=top><div class=inputs><input id=fa value='AEK'><div class=vs>VS</div><input id=fb value='Real Madrid'></div><div class=small><div style=flex:1><label>AEK Marques 5m</label><input id=fam type=number value=7></div><div style=flex:1><label>AEK Encaisses 5m</label><input id=fac type=number value=4></div></div><div class=small><div style=flex:1><label>Real Marques 5m</label><input id=fbm type=number
