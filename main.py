import os
from flask import Flask
import telebot
from threading import Thread
import unicodedata, hashlib

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

def norm(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s.lower()) if unicodedata.category(c)!='Mn')

def find_team(name):
    n=norm(name)
    # PSG - MAJ ETE 2026 REEL
    if "psg" in n or "paris" in n:
        return (90,82,"Ferran Torres 7b/1p NEW 48.5M (ex-Barca) + Kvara 11b + Dembele 12b + Doue 10b + Akliouche NEW + Godts NEW","Marquinhos, Mendes, Dembele incertain - OUT: Barcola->Liverpool 145M, Mbaye->Villa, Kimpembe->Qatar",90,82,6.1,6.2)
    if "barcel" in n or "barca" in n:
        return (92,78,"Yamal 16b/11p + Raphinha 13b + Lewandowski parti + NEW: Rodri (ex-City 18/08), Gordon 70M Newcastle, Adeyemi, Gabriel Jesus - OUT Ferran->PSG","ter Stegen, Gavi - Rashford retour MU, Araujo pret Liverpool",92,78,6.2,6.4)
    if "aston" in n or "villa" in n:
        return (84,78,"NEW: Jackson 2b + Mbaye 47M ex-PSG + Elliott pret Liverpool 35M + Garnacho pret Chelsea + Manzambi 51M - Watkins 20b + Rogers parti 117M Chelsea","Mings, Kamara - OUT Digne->PSG, Tielemans->MU",84,78,6.0,5.8)
    if "liverpool" in n:
        return (88,79,"Salah PARTI gratuit Trabzonspor - NEW: Barcola 145M ex-PSG + Jacquet 55M Rennes + Ara
