from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()
HTML="""<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width"><title>Dieng V18</title><style>body{background:#0a0e13;color:#fff;font-family:Arial;padding:10px} .h{background:linear-gradient(90deg,#00ff88,#00aaff);padding:12px;border-radius:10px;text-align:center;color:#000;font-weight:bold} .c{background:#151a22;border:1px solid #333;border-radius:10px;padding:12px;margin-top:10px} input{width:100%;padding:10px;border-radius:8px;border:1px solid #333;background:#1e222b;color:#fff;margin:4px 0} .btn{width:100%;padding:12px;background:#00ff88;border:none;border-radius:10px;font-weight:bold} .b{background:#1e222b;border:1px solid #333;border-radius:8px;padding:8px;text-align:center;margin:3px} .b b{color:#00ff88;display:block} .g{display:grid;grid-template-columns:1fr 1fr;gap:5px} .t{color:#00ff88;font-weight:bold;margin:10px 0 4px 0;font-size:13px} .f{font-size:11px;color:#aaa}</style></head><body><div class=h>Dieng V18 - MULTI-BUTS REEL 0-2 / 1-3</div><div class=c><b>Football - 5 derniers matchs</b><input id=a value="AEK Athenes"><input id=b value="Real Madrid"><button class=btn onclick=go()>ANALYSER</button><div id=r></div></div><script>
let DB={"real madrid":{fo:1.18,elo:1915,avg:2.4,last:[2,3,1,2,4],co:6.2,ca:1.8,ti:5.8,fa:11.5},"aek athenes":{fo:0.83,elo:1620,avg:0.8,last:[0,1,2,0,1],co:4.1,ca:2.6,ti:3.2,fa:14.2}};
function getF(n){let k=n.toLowerCase();for(let x in DB){if(k.includes(x)||x.includes(k))return DB[x]}return{fo:0.95,elo:1650,avg:1.2,last:[1,1,2,1,0],co:4.5,ca:2.2,ti:4,fa:12.5}}
function po(k,l){let p=Math.exp(-l);for(let i=1;i<=k;i++)p*=l/i;return p}
function pr(xg,mn,mx){let t=0;for(let k=mn;k<=mx;k++)t+=po(k,xg);return (t*100).toFixed(1)}
function go(){
let av=document.getElementById('a').value,bv=document.getElementById('b').value;
let A=getF(av),B=getF(bv);
let xA=(A.avg*A.fo).toFixed(2),xB=(B.avg*B.fo).toFixed(2),xT=parseFloat(xA)+parseFloat(xB);
let d=(A.elo-B.elo)+(A.fo-B.fo)*100,pA=1/(1+Math.pow(10,-d/400)),v1=(pA*84).toFixed(1),v2=((1-pA)*84).toFixed(1);
let h=`<div style=margin-top:10px><b>V1 ${v1}% - NUL 16% - V2 ${v2}%</b>
<div class=f><b>5 derniers ${av}:</b> ${A.last.join('-')} Moy ${A.avg} buts Forme ${A.fo}</div>
<div class=f><b>5 derniers ${bv}:</b> ${B.last.join('-')} Moy ${B.avg} buts Forme ${B.fo}</div>
<div class=f><b>xG basé sur forme + 5 matchs:</b> ${xA} + ${xB} = ${xT.toFixed(2)}</div>
<div class=t>MULTI-BUTS REEL - Calculé sur 5 matchs + forme</div>
<div class=g>
<div class=b><b>0-1</b>${pr(xT,0,1)}%</div><div class=b><b>0-2</b>${pr(xT,0,2)}%</div>
<div class=b><b>0-3</b>${pr(xT,0,3)}%</div><div class=b><b>1-2</b>${pr(xT,1,2)}%</div>
<div class=b><b>1-3</b><span style=color:#000;background:#00ff88;padding:2px 6px;border-radius:6px>${pr(xT,1,3)}% CONSEIL</span></div>
<div class=b><b>1-4</b>${pr(xT,1,4)}%</div><div class=b><b>2-3</b>${pr(xT,2,3)}%</div>
<div class=b><b>2-4</b>${pr(xT,2,4)}%</div><div class=b><b>2-5</b>${pr(xT,2,5)}%</div><div class=b><b>2-6</b>${pr(xT,2,6)}%</div>
</div>
<div class=t>CORNERS / CARTONS / TIRS / FAUTES</div>
<div class=g><div class=b><b>${(A.co*A.fo+B.co*B.fo).toFixed(1)}</b>Corners</div><div class=b><b>${(A.ca+B.ca).toFixed(1)}</b>Cartons</div><div class=b><b>${(A.ti*A.fo+B.ti*B.fo).toFixed(1)}</b>Tirs</div><div class=b><b>${(A.fa+B.fa).toFixed(0)}</b>Fautes</div></div></div>`;
document.getElementById('r').innerHTML=h}
</script></body></html>"""
@app.get("/")
def home(): return HTMLResponse(HTML)
