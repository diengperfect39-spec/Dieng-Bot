import os
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

print("Demarrage du bot...")
while True:
    print("Bot en attente...")
    time.sleep(60)
