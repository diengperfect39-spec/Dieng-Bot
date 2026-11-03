
import os
import telebot
from flask import Flask
from datetime import datetime
import threading

TOKEN = os.environ.get("BOT_TOKEN", "8501720752:AAEoGaC5aX6YpH7n5f2sX1k9vJ8qLm0nOpQ")
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# --- CALENDRIER ---
TODAY = "Mardi 3 Novembre 2026"
TODAY_MATCHES = [
    ("Barcelona", "Aston Villa", "LDC 20h00 GMT"),
    ("Atletico Madrid", "Bayern Munich", "LDC 20h00 GMT"),
    ("Manchester United", "Roma", "LDC 20h00 GMT"),
    ("Feyenoord", "Inter", "LDC 20h00 GMT"),
    ("Villarreal", "PSG", "LDC 20h00 GMT"),
    ("Galatasaray", "Stuttgart", "LDC 17h45 GMT"),
    ("Al Hilal", "Shabab Al Ahli", "AFC Elite 18h15 GMT"),
    ("Al Hilal", "Al Nassr", "Saudi Pro League"),
]

FUTUR_MATCHES = {
    "4 Nov": ["Real Madrid vs Liverpool (LDC)", "Man City vs Dortmund (LDC)"],
    "5 Nov": ["Arsenal vs Inter (LDC)", "Napoli vs Chelsea (LDC)"],
    "8 Nov": ["Barca vs Real Madrid (Liga)", "PSG vs Marseille (L1)"]
}

def find_match_info(team1, team2):
    t1, t2 = team1.lower(), team2.lower()
    for a,b,comp in TODAY_MATCHES:
        if (t1 in a.lower() or a.lower() in t1) and (t2 in b.lower() or b.lower() in t2):
            return f"🔴 MATCH DU JOUR - {comp} - {TODAY}"
        if (t2 in a.lower() or a.lower() in t2) and (t1 in b.lower() or b.lower() in t1):
            return f"🔴 MATCH DU JOUR - {comp} - {TODAY}"
    return None

def prediction_text(t1, t2, info):
    header = info if info else f"📅 ANALYSE - {t1} vs {t2} (Match à venir)"
    return f"""{header}

🏆 {t1} vs {t2}

📊 1X2:
• {t1}: 45% (1.95)
• Nul: 25% (3.40)
• {t2}: 30% (3.80)

🎯 Double Chance:
• 1X: 68%
• 12: 75%
• X2: 58%

⚽ Over/Under 2.5:
• Over 2.5: 62% ✅
• Under 2.5: 38%

🥅 BTTS:
• Oui: 58%
• Non: 42%

🎯 Score Exact:
• 2-1 (22%) | 1-1 (18%) | 2-0 (15%)

🚩 Corners: Over 8.5 - 65%
🟨 Cartons: Over 3.5 - 70%
🎯 Tirs cadrés: Over 8.5 - 68%
🔢 Multi-buts: 2-4 buts - 72%

💡 PRONO SAFE: 1X + Over 1.5
💎 RISQUE: {t1} gagne & BTTS
"""

@bot.message_handler(func=lambda m: True)
def handle(m):
    text = m.text.strip()
    low = text.lower()
    
    # Commande calendrier
    if low in ["calendrier", "programme", "aujourd'hui", "today", "matchs"]:
        msg = f"📅 PROGRAMME - {TODAY}\n\n"
        for a,b,comp in TODAY_MATCHES:
            msg += f"• {a} vs {b} - {comp}\n"
        msg += "\n🔜 À VENIR:\n"
        for date, matchs in FUTUR_MATCHES.items():
            msg += f"{date}: {', '.join(matchs)}\n"
        msg += "\nTape: Team A vs Team B pour analyse"
        bot.reply_to(m, msg)
        return

    if "vs" not in low:
        bot.reply_to(m, "Tape: Barcelona vs Aston Villa\nOu tape: calendrier")
        return

    parts = text.split("vs") if "vs" in text else text.split("VS")
    if len(parts) < 2:
        return
    t1 = parts[0].strip().title()
    t2 = parts[1].strip().title()
    
    info = find_match_info(t1, t2)
    resp = prediction_text(t1, t2, info)
    bot.reply_to(m, resp)

@app.route('/')
def home():
    return "Bot Live - Dieng Predict"

def run_bot():
    bot.infinity_polling()

threading.Thread(target=run_bot, daemon=True).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
