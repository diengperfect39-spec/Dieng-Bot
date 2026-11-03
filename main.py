import os
from flask import Flask
import threading
import telebot

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot Dieng is alive!"

    def run_flask():
        port = int(os.environ.get("PORT", 10000))
            app.run(host='0.0.0.0', port=port)

            TOKEN = os.environ.get("BOT_TOKEN")

            if not TOKEN:
                print("ERREUR BOT_TOKEN manquant")
                else:
                    bot = telebot.TeleBot(TOKEN)

                        @bot.message_handler(commands=['start'])
                            def start_msg(message):
                                    bot.reply_to(message, "Salut Belli ! Ton bot est en ligne ✅")

                                        threading.Thread(target=run_flask).start()
                                            print("Bot lancé...")
                                                bot.infinity_polling()