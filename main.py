import os
from flask import Flask
import threading
import telebot
import re
import math
from collections import defaultdict

app = Flask(__name__)

@app.route('/')
def home():
    return "Dieng Predict Pro is alive"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

TOKEN = os.environ.get("BOT_TOKEN")
user_history = defaultdict(list)

if not TOKEN:
    print("ERREUR BOT_TOKEN")
else:
    bot = telebot.TeleBot(TOKEN)

    @bot.message_handler(commands=['start'])
    def start(m):
        bot.reply_to(m, "DIENG PREDICT PRO\nEnvoie: Al Hilal vs Al Nassr\nJe donne: 1X2 / Double Chance / Over Under / BTTS / Scores / Corners / Cartons / Tirs / Multi buts")

    @bot.message_handler(commands=['stats'])
    def stats(m):
        hist = user_history[m.from_user.id]
        if not hist:
            bot.reply_to(m, "Historique vide")
        else:
            txt = "Historique:\n" + "\n".join(hist[-10:])
            bot.reply_to(m, txt)

    @bot.message_handler(func=lambda msg: "vs" in msg.text.lower())
    def predict(msg):
        try:
            parts = re.split(" vs ", msg.text, flags=re.IGNORECASE)
            if len(parts) != 2:
                raise ValueError
            team1 = parts[0].strip()
            team2 = parts[1].strip()
            
            avg1 = 1.55
            avg2 = 1.15
            
            scores = {}
            for i in range(4):
                for j in range(4):
                    prob1 = math.exp(-avg1) * (avg1 ** i) / math.factorial(i)
                    prob2 = math.exp(-avg2) * (avg2 ** j) / math.factorial(j)
                    scores[str(i) + "-" + str(j)] = prob1 * prob2
            
            p_home = 0
            p_draw = 0
            p_away = 0
            p_over = 0
            p_btts = 0
            
            for k,v in scores.items():
                a = int(k.split("-")[0])
                b = int(k.split("-")[1])
                if a > b:
                    p_home += v
                elif a == b:
                    p_draw += v
                else:
                    p_away += v
                if a + b > 2:
                    p_over += v
                if a > 0 and b > 0:
                    p_btts += v
            
            top = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:2]
            
            txt = "ANALYSE: " + team1 + " vs " + team2 + "\n\n"
            txt += "1X2:\n"
            txt += "1: " + str(round(p_home*100,1)) + "% | Nul: " + str(round(p_draw*100,1)) + "% | 2: " + str(round(p_away*100,1)) + "%\n\n"
            txt += "DOUBLE CHANCE:\n"
            txt += "1X: " + str(round((p_home+p_draw)*100,1)) + "% | 12: " + str(round((p_home+p_away)*100,1)) + "% | X2: " + str(round((p_draw+p_away)*100,1)) + "%\n\n"
            txt += "OVER 2.5:\nOver: " + str(round(p_over*100,1)) + "% | Under: " + str(round((1-p_over)*100,1)) + "%\n\n"
            txt += "BTTS:\nOui: " + str(round(p_btts*100,1)) + "% | Non: " + str(round((1-p_btts)*100,1)) + "%\n\n"
            txt += "SCORES:\n" + top[0][0] + " " + str(round(top[0][1]*100,1)) + "%\n" + top[1][0] + " " + str(round(top[1][1]*100,1)) + "%\n\n"
            txt += "CORNERS: Moy 10.4 Over 9.5 60% | 1MT 4.5 58% | 2MT 5.5 56%\n"
            txt += "CARTONS: Over 3.5 60% | FAUTES Over 22.5 57%\n"
            txt += "TIRS: Over 8.5 62% | MULTI 2-4 buts " + str(round(p_over*80,0)) + "%\n\n"
            txt += "18+ Info seulement"
            
            user_history[msg.from_user.id].append(team1 + " vs " + team2)
            bot.reply_to(msg, txt)
        except Exception as e:
            bot.reply_to(msg, "Erreur: envoie comme Al Hilal vs Al Nassr")

    threading.Thread(target=run_flask, daemon=True).start()
    bot.infinity_polling()
