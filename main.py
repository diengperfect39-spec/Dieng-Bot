import os
from flask import Flask
import telebot
from threading import Thread
import hashlib

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

def find_team(name):
    DB = {
        "barcelona": (91, 78, "Lewandowski 24b Yamal 18p", "Gavi", 5.8, 6.2),
        "barcelone": (91, 78, "Lewandowski 24b Yamal 18p", "Gavi", 5.8, 6.2),
        "psg": (90, 80, "Dembele 15p Barcola 18b", "Kimpembe", 5.9, 6.0),
        "bayern": (92, 79, "Kane 30b Musiala 14p", "Neuer", 5.6, 6.3),
        "real madrid": (89, 82, "Vinicius 22b Bellingham 16p", "Carvajal", 5.2, 5.9),
        "man city": (90, 81, "Haaland 28b Foden 12p", "De Bruyne", 5.4, 6.5),
        "atletico": (82, 88, "Griezmann 18b Alvarez 15b", "Gimenez", 6.1, 4.3),
        "liverpool": (88, 80, "Salah 23b Nunez 14b", "Jota", 5.5, 6.1),
        "villarreal": (80, 75, "Sorloth 19b Baena 12p", "Moreno", 5.6, 5.3),
        "aston villa": (81, 77, "Watkins 20b Rogers 10b", "Mings", 5.7, 5.1),
        "dortmund": (84, 76, "Guirassy 22b Brandt 11p", "Adeyemi", 5.8, 5.5),
    }
    n = name.lower()
    for k in DB:
        if k in n:
            return DB[k]
    h = int(hashlib.md5(n.encode()).hexdigest(), 16) % 20
    return (70+h, 70+(h%10), f"{name.title()} forme moyenne", "Ras", 5.0+h/10, 4.5+h/10)

def get_full(e1,e2):
    att1, def1, info1, inj1, tirs1, corn1 = find_team(e1)
    att2, def2, info2, inj2, tirs2, corn2 = find_team(e2)
    total = (att1+att2)/2
    corners = round(corn1+corn2,1)
    tirs = round(tirs1+tirs2,1)
    cartons = round(3.5 + (def1+def2-150)/28, 1)
    over25 = int(42 + total/2.1)
    btts = int(35 + min(att1,att2)/2.2)
    if total > 88:
        multi = "3-5 buts (72%) / 4-6 buts (48%)"
    elif total > 82:
        multi = "2-4 buts (72%) / 3-5 buts (58%)"
    else:
        multi = "1-3 buts (68%) / 2-4 buts (55%)"
    if att1 > att2 + 6:
        scores = [f"2-1 {e1}", f"1-1", f"2-0 {e1}"]
    elif att2 > att1 + 6:
        scores = [f"1-2 {e2}", f"1-1", f"0-2 {e2}"]
    else:
        scores = [f"2-1", f"1-1", f"2-0"]
    safe = f"1X + Over 1.5" if att1>att2 else f"X2 + Over 1.5"
    return f"""🏆 {e1} vs {e2}
⚽ {info1} vs {info2}
🤕 Abs: {inj1} / {inj2}
📊 Over/Under:
- Over 2.5: {over25}% / Under: {100-over25}%
📖 BTTS: Oui {btts}% / Non {100-btts}%
🚩 Corners: {corners} (Over 8.5 - 65%)
🟨 Cartons: Over {cartons} (70%)
🎯 Tirs cadrees: {tirs} (Over 8.5 - 68%)
🔢 Multi-buts: {multi}
🎯 Scores Exact:
1. {scores[0]} (22%)
2. {scores[1]} (18%)
3. {scores[2]} (15%)
💡 PRONO SAFE: {safe}
"""

@bot.message_handler(func=lambda m: "vs" in m.text.lower())
def vs(m):
    try:
        a,b = m.text.split("vs")
        e1=a.strip().title()
        e2=b.strip().title()
        bot.send_message(m.chat.id, get_full(e1,e2))
    except:
        bot.reply_to(m, "Tape: Villarreal vs PSG")

@app.route('/')
def h():
    return "Dieng V6 Full Live"

def run_bot():
    bot.infinity_polling()

Thread(target=run_bot).start()
if __name__ == "__main__":
    port = int(os.getenv("PORT", "10000"))
    app.run(host="0.0.0.0", port=port)
