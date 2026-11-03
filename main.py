import os
from flask import Flask
import telebot
from threading import Thread
import unicodedata, hashlib

TOKEN=os.getenv("BOT_TOKEN")
bot=telebot.TeleBot(TOKEN)
app=Flask(__name__)

def norm(s):
 return ''.join(c for c in unicodedata.normalize('NFD', s.lower()) if unicodedata.category(c)!='Mn')

def find_team(name):
 n=norm(name)
 if "villarreal" in n:
  return (81,76,"Perez 18b + Barry 14b + Pepe + Baena 12p + Moleiro NEW 70M","Moreno incertain",81,76,5.8,5.1)
 if "aston" in n or n=="villa" or " villa" in n:
  return (84,78,"Jackson NEW pret Chelsea + Mbaye 47M ex-PSG + Elliott pret","OUT Rogers 117M Chelsea, Digne 32M->PSG",84,78,6.0,5.8)
 if "psg" in n or "paris" in n:
  return (90,83,"Ferran Torres NEW 48.5M + Kvara 11b + Dembele 12b + Digne 32M","OUT Barcola 145M->LIV, Mbaye 47M->Villa",90,83,6.1,6.2)
 if "barcel" in n:
  return (92,78,"Yamal 16b + Raphinha 13b + Rodri NEW 70M + Gordon NEW","OUT Ferran 48.5M->PSG",92,78,6.2,6.4)
 if "liverpool" in n:
  return (88,79,"Barcola NEW 145M ex-PSG + Jacquet 55M + Ekitike + Wirtz","OUT Salah, Konate->Real",88,79,5.8,6.0)
 h=int(hashlib.md5(n.encode()).hexdigest(),16)%10
 return (75+h,75+h//2,f"{name.title()}","Ras",75+h,75+h//2,5.0+h/10,5.0+h/10)

def analyse(e1,e2):
 att1,def1,info1,inj1,a1,d1,t1,c1=find_team(e1)
 att2,def2,info2,inj2,a2,d2,t2,c2=find_team(e2)
 xg1=round((att1/90)*(def2/80)*1.5,2)
 xg2=round((att2/90)*(def1/80)*1.3,2)
 tot=round(xg1+xg2,2)
 corners=round(c1+c2,1)
 tirs=round(t1+t2,1)
 over25=78 if tot>3 else 68 if tot>2.6 else 58
 btts=int(min(att1,att2)*0.7)
 over95=62 if corners>10 else 54
 diff=(att1-def1)-(att2-def2)
 if diff>8:
  fav=f"{e1} FORT FAVORI";prono=f"1 + Over 1.5";score=f"{e1} 2 — 0 {e2}"
 elif diff>3:
  fav=f"{e1} favori";prono=f"1X + Over 1.5";score=f"{e1} 2 — 1 {e2}"
 elif diff<-8:
  fav=f"{e2} FORT FAVORI";prono=f"2 + Over 1.5";score=f"{e1} 0 — 2 {e2}"
 elif diff<-3:
  fav=f"{e2} favori";prono=f"X2 + Over 1.5";score=f"{e1} 1 — 2 {e2}"
 else:
  fav="Equilibre";prono="BTTS Oui + Over 1.5";score=f"{e1} 1 — 1 {e2}"
 return f"🏆 {e1} vs {e2} [V12 APP]\n⚽ {e1}: {info1}\n⚽ {e2}: {info2}\n🤕 {inj1} | {inj2}\n📊 xG {xg1}-{xg2} Total {tot} {fav}\n📈 Over2.5 {over25}% BTTS {btts}%\n🚩 Corners {corners} 🎯 Tirs {tirs}\n💡 {prono}\n🎯 {score}"

APP_HTML = """
<!DOCTYPE html><html lang="fr"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Dieng Predict V11</title><meta name="theme-color" content="#0b3d20">
<style>*{margin:0;padding:0;box-sizing:border-box;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica,Arial,sans-serif}
body{background:#0a2e18;color:white;min-height:100vh;padding-bottom:80px}
.header{background:#123f26;padding:14px 16px;display:flex;justify-content:space-between;position:sticky;top:0}
.header h1{font-size:20px;font-weight:900}.header small{color:#8ee8b0;font-size:11px;display:block}
.card{background:#164d2e;margin:12px;border-radius:16px;padding:16px;box-shadow:0 8px 20px rgba(0,0,0,0.3)}
.input-row{display:flex;gap:8px;align-items:center;margin:12px}
.input-row input{flex:1;background:#0e3320;border:1px solid #2a6b45;color:white;border-radius:12px;padding:14px 12px;font-size:15px;font-weight:700;text-align:center}
.vs{background:#1f5c36;border-radius:20px;padding:6px 14px;font-weight:900}
.btn{background:#2ee57a;color:#05210f;border:none;width:calc(100% - 24px);margin:12px;padding:16px;border-radius:14px;font-weight:900;font-size:16px;cursor:pointer}
.score{font-size:22px;font-weight:900;text-align:center;margin:14px 0}
.pred-box{background:#1d6a3a;border-radius:12px;padding:12px;display:flex;gap:10px;align-items:center}
.dot{width:32px;height:32px;background:#2ee57a;border-radius:50%;display:grid;place-items:center;color:#05210f;font-weight:900}
.kpi{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;margin-top:14px;text-align:center}
.kpi span{font-size:11px;opacity:0.8;display:block}.kpi strong{font-size:22px}
.bar{height:8px;background:#0e3320;border-radius:10px;overflow:hidden;margin-top:6px}.bar i{display:block;height:100%;background:#2ee57a}
.list{margin-top:12px;font-size:13px;line-height:1.6;color:#c8f0d6}.list li{margin-left:16px}
.footer-nav{position:fixed;bottom:0;left:0;right:0;background:#0f3a22;display:flex;justify-content:space-around;padding:12px 0;border-top:1px solid #1e5a35}
.footer-nav b{font-size:11px;opacity:0.7}.footer-nav b.active{opacity:1;color:#2ee57a}
</style></head><body>
<div class="header"><div><h1>Dieng Predict V11</h1><small>AI Football Prediction • v11</small></div><div>⚙️</div></div>
<div class="card"><div class="input-row"><input id="t1" value="Barcelona"><div class="vs">VS</div><input id="t2" value="Aston Villa"></div>
<button class="btn" onclick="predict()">See Full Analysis</button></div>
<div id="out"></div>
<div class="footer-nav"><b class="active">⚽ Predict</b><b>📊 Stats</b><b>📰 News</b><b>👤 Profile</b></div>
<script>
function norm(s){return s.toLowerCase().normalize('NFD').replace(/[\\u0300-\\u036f]/g,'');}
function getTeam(name){let n=norm(name);
if(n.includes('villarreal'))return{att:81,def:76,info:'Perez 18b + Barry 14b + Pepe + Moleiro NEW 70M',inj:'Moreno incertain',corn:5.8,tirs:5.1};
if(n.includes('aston')||n==='villa'||n.includes(' villa'))return{att:84,def:78,info:'Jackson NEW pret Chelsea + Mbaye 47M ex-PSG + Elliott pret',inj:'OUT Rogers 117M Chelsea, Digne 32M->PSG',corn:6.0,tirs:5.8};
if(n.includes('psg')||n.includes('paris'))return{att:90,def:83,info:'Ferran Torres NEW 48.5M + Kvara 11b + Dembele 12b + Digne 32M',inj:'OUT Barcola 145M->LIV, Mbaye 47M->Villa',corn:6.1,tirs:6.2};
if(n.includes('barcel'))return{att:92,def:78,info:'Yamal 16b + Raphinha 13b + Rodri NEW 70M',inj:'OUT Ferran 48.5M->PSG',corn:6.2,tirs:6.4};
if(n.includes('liverpool'))return{att:88,def:79,info:'Barcola NEW 145M ex-PSG + Jacquet 55M',inj:'OUT Salah',corn:5.8,tirs:6.0};
let h=name.length%10;return{att:75+h,def:75+Math.floor(h/2),info:name,inj:'Ras',corn:5.0+h/10,tirs:5.0+h/10};}
function predict(){let e1=document.getElementById('t1').value||'Barcelona';let e2=document.getElementById('t2').value||'Aston Villa';
let t1=getTeam(e1),t2=getTeam(e2);let xg1=((t1.att/90)*(t2.def/80)*1.5).toFixed(2);let xg2=((t2.att/90)*(t1.def/80)*1.3).toFixed(2);
let tot=(parseFloat(xg1)+parseFloat(xg2)).toFixed(2);let diff=(t1.att-t1.def)-(t2.att-t2.def);let fav,prono,score;
if(diff>8){fav=e1+' FORT FAVORI';prono=e1+' gagne & Over 1.5';score=e1+' 2 — 0 '+e2;}
else if(diff>3){fav=e1+' favori';prono='1X + Over 1.5';score=e1+' 2 — 1 '+e2;}
else if(diff<-8){fav=e2+' FORT FAVORI';prono=e2+' gagne & Over 1.5';score=e1+' 0 — 2 '+e2;}
else if(diff<-3){fav=e2+' favori';prono='X2 + Over 1.5';score=e1+' 1 — 2 '+e2;}
else{fav='Equilibre';prono='BTTS Oui + Over 1.5';score=e1+' 1 — 1 '+e2;}
let corners=(t1.corn+t2.corn).toFixed(1);let btts=Math.min(t1.att,t2.att)*0.7|0;let over25=tot>3?78:tot>2.6?68:58;
let poss1=Math.max(38,Math.min(68,Math.round(50+diff)));let poss2=100-poss1;
document.getElementById('out').innerHTML=`<div class="card"><div style="display:flex;justify-content:space-between;align-items:center">
<div style="text-align:center"><div style="font-size:36px">🔵🔴</div><b>${e1.substring(0,3).toUpperCase()}</b></div>
<div style="text-align:center"><div class="vs">VS</div><div style="font-size:10px;opacity:0.7;margin-top:6px">UEFA Champions League • Today • 21:00 CET</div></div>
<div style="text-align:center"><div style="font-size:36px">🦁</div><b>${e2.substring(0,3).toUpperCase()}</b></div></div>
<div class="score">${score}</div><div style="text-align:center;font-size:11px;color:#8ee8b0">Predicted Score • xG ${xg1} - ${xg2} • Total ${tot} • ${fav}</div>
<div class="pred-box" style="margin-top:12px"><div class="dot">✓</div><div><b>Prediction: ${prono}</b><br><small style="opacity:0.8">BTTS ${btts}% • Over 2.5 ${over25}%</small></div></div>
<div class="kpi"><div><span>⚽ xG</span><strong>${xg1}</strong><span>${e1}</span></div><div><span>🚩 Corners</span><strong>${corners}</strong></div><div><span>👥 BTTS</span><strong>${btts}%</strong></div></div>
<div style="margin-top:14px"><div style="display:flex;justify-content:space-between;font-size:13px"><b>Possession</b><b>${poss1}% — ${poss2}%</b></div><div class="bar"><i style="width:${poss1}%"></i></div></div>
<div class="list"><b>Match Analysis</b><li>${e1}: ${t1.info}</li><li>${e2}: ${t2.info}</li><li>Abs: ${t1.inj} | ${t2.inj}</li><li>Over 2.5 ${over25}% • Corners ${corners} • Multi-buts 2-4</li><li>PRONO: ${prono}</li></div></div>`;}
predict();
</script></body></html>
"""

@app.route('/')
def h():
 return APP_HTML

@bot.message_handler(func=lambda m: "vs" in m.text.lower())
def vs(m):
 try:
  a,b=m.text.lower().split("vs")
  e1=a.strip().title();e2=b.strip().title()
  bot.send_message(m.chat.id, analyse(e1,e2))
 except:
  bot.reply_to(m,"Tape: Villarreal vs PSG")

def run_bot(): bot.infinity_polling()
Thread(target=run_bot).start()
if __name__=="__main__":
 port=int(os.getenv("PORT","10000"))
 app.run(host="0.0.0.0",port=port)
