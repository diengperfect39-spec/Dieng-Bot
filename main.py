import os
from flask import import os
from flask import Flask
import threading
import time

app = Flask(__name__)
@app.route('/')
def home():
    return "Bot Dieng is alive!"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

threading.Thread(target=run_flask, daemon=True).start()

import asyncio
print("Démarrage du bot...")

# Boucle pour garder le bot actif
alors = True
while alors:
    print("Bot en attente...")
    time.sleep(60)
