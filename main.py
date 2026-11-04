from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse, Response

app = FastAPI()

HTML_PAGE = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Dieng V18 Multi-Buts Réel</title>
<style>
body{background:#0a0e13;color:#fff;font-family:Arial;padding:10px;padding-bottom:80px}
.header{background:linear-gradient(90deg,#00ff88,#00aaff);padding:14px;border-radius:12px;text-align:center;color:#000;font-weight:bold}
.tab{padding:10px 14px;border-radius:20px;background:#1e222b;color:#888;border:1px solid #333;display:inline-block;margin:3px;cursor:pointer}
.tab.active{background:#00ff88;color:#000;font-weight:bold}
.card{background:#151a22;border:1px solid #2a2e38;border-radius:14px;padding:14px;margin-top:10px}
input{width:100%;padding:11px;border-radius:10px;border:1px solid #333;background:#1e222b;color:#fff;margin:4px 0}
.btn{width:100%;padding:13px;background:#00ff88;color:#000;border:none;border-radius:12px;font-weight:bold;margin-top:8px}
.box{background:#1e222b;border:1px solid #2a2e38;border-radius:10px;padding:10px;text-align:center;margin:4px}
.box b{display:block;color:#00ff88;font-size:15px}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:6px}
.title{color:#00ff88;font-weight:bold;margin:12px 0 5px 0;border-left:3px solid #00ff88;padding-left:8px;font-size:13px}
.form{font-size:11px;color:#aaa;margin:3px 0}
.prob{font-size:12px;background:#00ff8822;padding:4px 8px;border-radius:10px;display:inline-block}
</style>
</head>
<body>
<div class="header">Dieng Predict V18 - MULTI-BUTS 0-2 / 1-3</div>
<div style="margin:10px 0">
<div class="tab active" onclick="show('foot')">Football</div>
<div class="tab" onclick="show('basket')">Basket</div>
<div class="tab" onclick="show('tennis')">Tennis</div>
<div class="tab" onclick="show('hockey')">Hockey</div>
<div class="tab" onclick="show('ping')">Tennis Table</div>
</div>

<div id="foot" class="sec"><div class="card">
<b>Football - 5 derniers matchs + Forme</b>
<input id="fa" value="AEK Athenes">
<input id="fb" value="Real Madrid">
<button class="btn" onclick="foot()">ANALYSER - MULTI-BUTS RÉEL</button>
<div id="rfoot"></div>
</div></div>

<div id="basket" class="sec" style="display:none"><div class="card">
<b>Basket</b><input id="ba" value="Lakers"><input id="bb" value="Warriors">
<button class="btn" onclick="basket()">ANALYSER BASKET</button><div id="rbasket"></div>
</div></div>

<div id="tennis" class="sec" style="display:none"><div class="card">
<b>Tennis</b><input id="ta" value="Alcaraz"><input id="tb" value
