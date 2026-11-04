from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse, Response
app=FastAPI()

@app.get('/manifest.json')
def manifest():
    return JSONResponse({'name':'Dieng Predict V18 Multi Sports Pro','short_name':'Dieng V18','start_url':'/','display':'standalone','background_color':'#0a0e13','theme_color':'#00ff88'})

@app.get('/sw.js')
def sw():
    return Response("self.addEventListener('fetch',e=>{});", media_type="application/javascript")

@app.get('/', response_class=HTMLResponse)
def home():
    return '''<!DOCTYPE html><html lang="fr"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Dieng Predict V18 - Multi Sports Pro</title><style>body{background:#0a0e13;color:#fff;font-family:Arial;margin:0;padding:10px}.header{background:linear-gradient(90deg,#00ff88,#00aaff);padding:14px;border-radius:12px;text-align:center;color:#000;font-weight:bold}.tabs{display:flex;gap:6px;margin:12px 0;overflow-x:auto}.tab{padding:10px 14px;border-radius:20px;background:#1e222b;color:#888;border:1px solid #333;cursor:pointer;white-space:nowrap;font-size:13px}.tab.active{background:#00ff88;color:#000;font-weight:bold;border-color:#00ff88}.card{background:#151a22;border:1px solid #2a2e38;border-radius:14px;padding:14px;margin-top:12px}input,select{width:100%;padding:12px;border-radius:10px;border:1px solid #333;background:#1e222b;color:#fff;margin:5px 0}.btn{width:100%;padding:14px;background:#00ff88;color:#000;border:none;border-radius:12px;font-weight:bold;font-size:16px;margin-top:10px;cursor:pointer}.badge{display:inline-block;padding:4px 10px;border-radius:15px;font-size:11px;margin:3px;font-weight:bold}.bg-green{background:#00ff8833;color:#00ff88;border:1px solid #00ff88}.bg-blue{background:#00aaff33;color:#00aaff;border:1px solid #00aaff}.bg-yellow{background:#ffcc0033;color:#ffcc00;border:1px solid #ffcc00}.stat{font-size:13px;color:#ccc;margin:4px 0}.stat b{
