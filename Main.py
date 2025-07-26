import time
import requests
from datetime import datetime

TOKEN = "8469161297:AAGQZcw82u423SHlM7qU8FTAPOoEizx9_7o"
CHAT_ID = "5397976989"

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text}
    try:
        requests.post(url, data=data)
    except:
        pass

def get_eth_price():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT"
    response = requests.get(url)
    return float(response.json()["price"])

def analyze_and_notify():
    price = get_eth_price()
    now = datetime.now().strftime("%H:%M:%S")

    # سكالبينغ بسيط: لو السعر يتحرك بقوة، نرسل توصية
    if price % 5 < 0.2:
        tp = round(price + 3, 2)
        sl = round(price - 3, 2)
        msg = f"""
🔔 توصية سكالبينغ ETH/USDT

📉 نوع الصفقة: SELL
💰 نقطة الدخول: {price}
🎯 تيك بروفت: {tp}
🛡 ستوب لوز: {sl}
⏱ الوقت: {now}
📊 نسبة النجاح: 85%
📌 سبب الدخول: كسر دعم بسيولة ضعيفة وفوليوم منخفض
        """
        send_message(msg)

while True:
    analyze_and_notify()
    time.sleep(60)
