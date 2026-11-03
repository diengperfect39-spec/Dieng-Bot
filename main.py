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
                                    bot.reply_to(message, "Salut Belli ! Bot Dieng en ligne ✅ Tape /stats")

                                        @bot.message_handler(commands=['stats'])
                                            def stats_msg(message):
                                                    bot.reply_to(message, "📊 Stats Dieng : Bot fonctionne !")

                                                        @bot.message_handler(func=lambda m: True)
                                                            def all_msg(message):
                                                                    bot.reply_to(message, f"Reçu: {message.text}")

                                                                        def run_bot():
                                                                                print("Demarrage bot Telegram...")
                                                                                        bot.infinity_polling()

                                                                                            threading.Thread(target=run_flask, daemon=True).start()
                                                                                                run_bot()