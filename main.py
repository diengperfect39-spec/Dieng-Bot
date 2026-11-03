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
        return (88,79,"Salah PARTI gratuit Trabzonspor - NEW: Barcola 145M ex-PSG + Jacquet 55M Rennes + Araujo pret Barca + Munoz - OUT Konate->Real, Robertson->Tottenham","Jota, Elliott->Villa",88,79,5.8,6.0)
    if "real" in n and "madrid" in n:
        return (90,83,"NEW: Konate gratuit Liverpool + Bernardo Silva + Dumfries + Cucurella + Diomande - Vinicius 22b + Bellingham 16p","Carvajal",90,83,5.3,6.0)
    if "man city" in n or "city" in n:
        return (91,81,"NEW: Ndiaye 76M Everton + Enzo Fernandez 145M Chelsea + Bouaddi 100M Lille - OUT Rodri->Barca, Savinho->Tottenham + Haaland 28b","De Bruyne",91,81,5.4,6.5)
    if "villarreal" in n:
        return (80,75,"Sorloth 19b + Baena 12p + Gerard Moreno","Moreno incertain",80,75,5.6,5.3)
    if "atletico" in n:
        return (82,88,"NEW: Kang-in Lee ex-PSG + Alvarez 15b + Griezmann 18b","Gimenez",82,88,6.1,4.3)
    h=int(hashlib.md5(n.encode()).hexdigest(),16)%10
    return (75+h,75+h//2,f"{name.title()} forme stable","Ras",75+h,75+h//2,5.0+h/10,5.0+h/10)

def analyse(e1,e2):
    att1,def1,info1,inj1,a1,d1,t1,c1=find_team(e1)
    att2,def2,info2,inj2,a2,d2,t2,c2=find_team(e2)
    xg1=(att1/90)*(def2/80)*1.5
    xg2=(att2/90)*(def1/80)*1.3
    tot=xg1+xg2
    corners=round(c1+c2,1)
    tirs=round(t1+t2,1)
    over25=78 if tot>3 else 68 if tot>2.6 else 58
    btts=int(min(att1,att2)*0.7)
    diff=(att1-def1)-(att2-def2)
    if diff>8: fav=f"{e1} FORT FAVORI"; safe=f"1 + Over 1.5"; scores=[f"2-0 {e1}",f"3-1 {e1}",f"2-1 {e1}"]
    elif diff>3: fav=f"{e1} favori"; safe="1X + Over 1.5"; scores=[f"2-1 {e1}",f"1-1",f"2-0 {e1}"]
    elif diff<-8: fav=f"{e2} FORT FAVORI"; safe=f"2 + Over 1.5"; scores=[f"0-2 {e2}",f"1-3 {e2}",f"1-2 {e
