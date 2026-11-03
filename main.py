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
  return (81,76,"Perez 18b + Barry 14b + Pepe + Baena 12p + Moleiro NEW 70M Las Palmas","Moreno incertain",81,76,5.8,5.1)
 if "aston" in n or n=="villa" or " villa" in n:
  return (84,78,"Jackson NEW pret Chelsea + Mbaye 47M ex-PSG + Elliott pret LFC + Buendia","OUT Rogers 117M Chelsea, Digne 32M->PSG",84,78,6.0,5.8)
 if "psg" in n or "paris" in n:
  return (90,83,"Ferran Torres NEW 48.5M ex-Barca + Kvara 11b + Dembele 12b + Digne 32M ex-Villa","OUT Barcola 145M->Liverpool, Mbaye 47M->Villa, Kimpembe->Qatar",90,83,6.1,6.2)
 if "barcel" in n:
  return (92,78,"Yamal 16b + Raphinha 13b + Rodri NEW ex-City 70M + Gordon NEW + Adeyemi","OUT Ferran 48.5M->PSG, ter Stegen blesse",92,78,6.2,6.4)
 if "liverpool" in n:
  return (88,79,"Barcola NEW 145M ex-PSG + Jacquet 55M Rennes + Ekitike + Wirtz","OUT Salah Trabzonspor, Konate->Real",88,79,5.8,6.0)
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
  fav=f"{e1} FORT FAVORI";prono=f"1 + Over 1.5 ({e1} gagne & +1.5 buts)";scores=[(f"2-0 {e1}",21),(f"3-1 {e1}",17),(f"2-1 {e1}",14)]
 elif diff>3:
  fav=f"{e1} favori";prono=f"1X + Over 1.5";scores=[(f"2-1 {e1}",18),(f"1-1",15),(f"2-0 {e1}",13)]
 elif diff<-8:
  fav=f"{e2} FORT FAVORI";prono=f"2 + Over 1.5 ({e2} gagne & +1.5 buts)";scores=[(f"0-2 {e2}",21),(f"1-3 {e2}",17),(f"1-2 {e2}",14)]
 elif diff<-3:
  fav=f"{e2} favori";prono=f"X2 + Over 1.5";scores=[(f"1-2 {e2}",18),(f"1-1",15),(f"0-2 {e2}",13)]
 else:
  fav="Equilibre";prono="BTTS Oui + Over 1.5";scores=[("1-1",16),("2-1",14),("1-2",12)]
 return f"""🏆 {e1} vs {e2} [V11 MERCATO 2026]
⚽ {e1}: {info1}
⚽ {e2}: {info2}
🤕 Abs: {inj1} | {inj2}
📊 xG {e1}: {xg1} | xG {e2}: {xg2} | Total {tot} | {fav}

📈 PROBAS:
- Over 2.5: {over25}% (Under {100-over25}%)
- BTTS Oui: {btts}% / Non {100-btts}%

🚩 Corners: {corners} (Moy: Over 9.5 a {over95}%)
🟨 Cartons: Over {round((c1+c2)/2.5,1)}
🎯 Tirs cadres: {tirs} (Over 8.5 a {58+btts//5}%)

🔢 Multi-buts conseille: 2-4 buts

🎯 Scores Exact les + probables:
1. {scores[0][0]} ({scores[0][1]}%)
2. {scores[1][0]} ({scores[1][1]}%)
3. {scores[2][0]} ({scores[2][1]}%)

💡 PRONO ANALYSE (pas hasard): {prono}
"""

@bot.message_handler(func=lambda m: "vs" in m.text.lower())
def vs(m):
 try:
  a,b=m.text.lower().split("vs")
  e1=a.strip().title();e2=b.strip().title()
  bot.send_message(m.chat.id, analyse(e1,e2))
 except:
  bot.reply_to(m,"Tape: Villarreal vs PSG")

@app.route('/')
def h(): return "Dieng V11"
def run_bot(): bot.infinity_polling()
Thread(target=run_bot).start()
if __name__=="__main__":
 port=int(os.getenv("PORT","10000"))
 app.run(host="0.0.0.0",port=port)
