import os
from flask import Flask
import threading
import telebot
import re

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot Dieng is alive!"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

TOKEN = os.environ.get("BOT_TOKEN")

# stockage simple en mémoire {user_id: [scores]}
user_scores = {}

if not TOKEN:
    print("ERREUR BOT_TOKEN manquant")
else:
    bot = telebot.TeleBot(TOKEN)

    @bot.message_handler(commands=['start'])
    def start_msg(message):
        bot.reply_to(message, "Salut Belli ! Envoie un score comme 1-0 et tape /stats pour voir l'historique.")

    @bot.message_handler(commands=['stats'])
    def stats_msg(message):
        uid = message.from_user.id
        scores = user_scores.get(uid, [])
        if not scores:
            bot.reply_to(message, "Historique : aucun score final enregistré pour ce compte.\nEnvoie d'abord 1-0")
        else:
            txt = f"Historique ({len(scores)} scores):\n" + "\n".join(scores[-10:])
            bot.reply_to(message, txt)

    @bot.message_handler(regexp=r'^\d+-\d+$')
    def score_msg(message):
        uid = message.from_user.id
        score = message.text.strip()
        if uid not in user_scores:
            user_scores[uid] = []
        user_scores[uid].append(score)
        bot.reply_to(message, f"Score {score} enregistré ! Tape /stats")

    @bot.message_handler(func=lambda m: True)
    def other_msg(message):
        bot.reply_to(message, "Envoie un score comme 1-0 ou tape /stats")

    threading.Thread(target=run_flask, daemon=True).start()
    print("Bot demarre...")
    bot.infinity_polling()
