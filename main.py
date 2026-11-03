import os
from flask import Flask
import telebot
from threading import Thread

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

def get_real_stats(e1,e2):
    DB = {
        "barcelona": (91, 78, "Lewandowski 24 buts, Yamal 18", "Gavi"),
        "psg": (90, 80, "Mbappe 26 buts, Dembele 15", "Kimpembe"),
        "bayern": (92, 79, "Kane 30 buts, Musiala 14", "Neuer"),
        "real madrid": (89, 82, "Vinicius 22 buts, Bellingham 16", "Carvajal"),
        "man city": (90, 81, "Haaland 28 buts, Foden 12", "De Bruyne"),
        "atletico": (82, 88, "Griezmann 18 buts", "Gimenez"),
        "liverpool": (88, 80, "Salah 23 buts", "Jota"),
        "villarreal": (80, 75, "Sorloth 19 buts", "Moreno"),
        "aston villa": (81, 77, "Watkins 20 buts", "Mings"),
        "dortmund": (84, 76, "Guirassy 22 buts", "Adeyemi"),
    }
    k1 = e1.lower()
    k2 = e2.lower()
    d1 = DB.get(next((k for k in DB if k in k1), "other"), (75,75,f"{e1} forme moyenne", "Ras"))
    d2 = DB.get(next((k for k in DB if k in k2), "other"), (75,75,f"{e2} forme moyenne", "Ras"))
    att1, def1, info1, inj1 = d1
    att2, def2, info2, inj2 = d2
    total = (att1+att2)/2
    return f"🏆 {e1} vs {e2}\n📍 {info1} vs {info2}\n🤕 {inj1} / {inj2}\n📊 Over 2.5: {50+int(total/2)}% - BTTS: {40+int(min(att1,att2)/2)}%\n💡 SAFE: {e1 if att1>att2 else e2} ou Nul"

@bot.message_handler(func=lambda m: "vs" in m.text.lower())
def vs(m):
    try:
        a,b = m.text.split("vs")
        e1=a.strip().title()
        e2=b.strip().title()
        bot.send_message(m.chat.id, get_real_stats(e1,e2))
    except:
        bot.reply_to(m, "Tape: Villarreal vs PSG")

@app.route('/')
def h():
    return "Dieng Live"

def run_bot():
    bot.infinity_polling()

Thread(target=run_bot).start()

if __name__ == "__main__":
    port = int(os.getenv("PORT", "10000"))
    app.run(host="0.0.0.0", port=port)
