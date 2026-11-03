import os
from flask import Flask
import threading
import telebot
import re
import math
from collections import defaultdict

app = Flask(__name__)
@app.route('/')
def home(): return "Dieng Predict Pro is alive!"
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
        bot.reply_to(m, "⚽ DIENG PREDICT PRO ⚽\n\nEnvoie un match comme ça:\nAl Hilal vs Al Nassr\n\nJe vais analyser tout seul:\n🏆 1X2 / Double Chance\n⚽ Over/Under 2.5 / BTTS\n🎯 2 Scores Exacts\n🚩 Corners (1MT/2MT/90min)\n🟨 Cartons / Fautes\n🥅 Tirs cadrés / Multi buts\n\nTape /stats pour historique")

    @bot.message_handler(commands=['stats'])
    def stats(m):
        hist = user_history[m.from_user.id]
        if not hist:
            bot.reply_to(m, "Historique vide. Envoie un match: Ex: Real vs Barca")
        else:
            txt = f"📊 Historique ({len(hist)} analyses):\n\n" + "\n".join(hist[-10:])
            bot.reply_to(m, txt)

    @bot.message_handler(func=lambda msg: "vs" in msg.text.lower() and not msg.text.startswith('/'))
    def predict_match(msg):
        try:
            text = msg.text
            parts = re.split(r'\s+vs\s+', text, flags=re.IGNORECASE)
            if len(parts) != 2: raise ValueError
            team1, team2 = parts[0].strip(), parts[1].strip()
            
            avg_home = 1.55
            avg_away = 1.15
            
            scores = {}
            for i in range(0, 4):
                for j in range(0, 4):
                    p = (math.exp(-avg_home) * avg_home**i / math.factorial(i)) * (math.exp(-avg_away) * avg_away**j / math.factorial(j))
                    scores[f"{i}-{j}"] = p

            p_home = sum(v for k,v in scores.items() if int(k.split('-')[0]) > int(k.split('-')[1]))
            p_draw = sum(v for k,v in scores.items() if int(k.split('-')[0]) == int(k.split('-')[1]))
            p_away = sum(v for k,v in scores.items() if int(k.split('-')[0])
