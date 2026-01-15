import time
import requests
import random
from flask import Flask
from threading import Thread
import os

app = Flask('')

@app.route('/')
def home():
    return "Bot is Running 24/7!"

def run():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

# SETTINGS
TOKEN = "8588224838:AAEsECcL4pcWWKKGs3e8tDDQXx_q4seP7cs"
GROUP_1_ID = "-1003668034057"
GROUP_2_ID = "@quotex_world_inc_1"

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    try:
        requests.post(url, data={"chat_id": GROUP_1_ID, "text": msg, "parse_mode": "HTML"})
        requests.post(url, data={"chat_id": GROUP_2_ID, "text": msg, "parse_mode": "HTML"})
    except:
        pass

def start_bot():
    while True:
        assets = ["EUR/USD (OTC)", "GBP/JPY (OTC)", "USD/ZAR (OTC)"]
        asset = random.choice(assets)
        dir = random.choice(["UP 🟢", "DOWN 🔴"])
        msg = f"📊 <b>QUOTEX SIGNAL</b>\n\nAsset: {asset}\nDir: {dir}\nAcc: {random.randint(95,99)}%"
        send_telegram(msg)
        time.sleep(120) # 2 minute gap

if __name__ == "__main__":
    t = Thread(target=start_bot)
    t.start()
    run()
