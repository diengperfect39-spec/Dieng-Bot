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
 if "psg" in n or "paris" in n:
  return (90,82,"Ferran Torres NEW 48.5M ex-Barca + Kvara 11b + Dembele 12b","OUT Barcola->Liverpool 145M, Mbaye->Villa, Kimpembe->Qatar",90,82,6.1,6.2)
 if "barcel" in n or "barca" in n:
  return (92,78,"Yamal 16b + Raphinha 13b + NEW Rodri ex-City, Gordon 70M, Adeyemi - OUT Ferran->PSG","Rashford retour MU, Araujo pret Liverpool",92,78,6.2,6.4)
 if "aston" in n or "villa" in n:
  return (84,78,"NEW Jackson + Mbaye 47M ex-PSG + Elliott pret Liverpool + Garnacho pret","OUT Digne->PSG, Rogers 117M Chelsea",84,78,6.0,5.8)
 if "liverpool" in n:
  return (88,79,"Salah PARTI Trabzonspor - NEW Barcola 145M ex-PSG + Jacquet 55M","OUT Konate->Real, Robertson->Tottenham",88,79,5.8,6.0)
 if "real" in n and "madrid" in n:
  return (90,83,"NEW Konate gratuit Liverpool + Bernardo Silva + Dumfries + Cucurella","Carvajal",90,83,5.3,6.0)
 if "city" in n:
  return (91,81,"NEW Ndiaye 76M + Enzo Fernandez 145M - OUT Rodri->Barca + Haaland 28b","De Bruyne",91,81,5.4,6.5)
 if "villarreal" in n:
  return (80,75,"Sorloth 19b + Baena 12p","Moreno",80,75,5.6,5.3)
 if "atletico" in n:
  return (82,88,"NEW Kang-in Lee ex-PSG + Alvarez 15b","Gimenez",82,88,6.1,4.3)
 h=int(hashlib.md5(n.encode()).hexdigest(),16)%10
 return (75+h,75+h//2,f"{name.title()}","Ras",75+h,75+h//2,5.0+h/10,5.0+h/10)
def analyse(e1,e2):
 att1,def1,info1,inj1,a1,d1,t1,c1=find_team(e1)
 att2,def2,info2,inj2,a2,d2,t2,c2=find_team(e2)
 xg1=(att1/90)*(def2/80)*1.5
 xg2=(att2/90)*(def1/80)*1.3
 tot=xg1+xg2
 corners=round(c1+c2,1)
 tirs=round(t1+t2,1)
 over25=78 if tot>3 else 68 if tot>2.6 else 58
 btts=int(min(att1,att2)*0.7)
 diff=(att1-def1)-(att2-def2)
 if diff>8:
  fav=f"{e1} FORT FAVORI";safe=f"1 + Over 1.5";scores=[f"2-0 {e1}",f"3-1 {e1}",f"2-1 {e1}"]
 elif diff>3:
  fav=f"{e1} favori";safe="1X + Over 1.5";scores=[f"2-1 {e1}",f"1-1",f"2-0 {e1}"]
 elif diff<-8:
  fav=f"{e2} FORT FAVORI";safe=f"2 + Over 1.5";scores=[f"0-2 {e2}",f"1-3 {e2}",f"1-2 {e2}"]
 elif diff<-3:
  fav=f"{e2} favori";safe="X2 + Over 1.5";scores=[f"1-2 {e2}",f"1-1",f"0-2 {e2}"]
 else:
  fav="Equilibre";safe="BTTS Oui + Over 1.5";scores=["1-1","2-1","1-2"]
 return f"""🏆 {e1} vs {e2} [V10 MERCATO 2026]
⚽ {e1}: {info1}
⚽ {e2}: {info2}
🤕 {inj1} | {inj2}
📊 xG {xg1:.2f}-{xg2:.2f} Total {tot:.2f} | {fav}
📈 Over 2.5 {over25}% | BTTS {btts}%
🚩 Corners {corners} | 🎯 Tirs {tirs}
🎯 Scores: {scores[0]} / {scores[1]} / {scores[2]}
💡 PRONO: {safe}
"""
@bot.message_handler(func=lambda m: "vs" in m.text.lower())
def vs(m):
 try:
  a,b=m.text.split("vs");e1=a.strip().title();e2=b.strip().title()
  bot.send_message(m.chat.id, analyse(e1,e2))
 except:
  bot.reply_to(m,"Tape: Villarreal vs PSG")
@app.route('/')
def h(): return "Dieng V10"
def run_bot(): bot.infinity_polling()
Thread(target=run_bot).start()
if __name__=="__main__":
 port=int(os.getenv("PORT","10000"))
 app.run(host="0.0.0.0",port=port)
