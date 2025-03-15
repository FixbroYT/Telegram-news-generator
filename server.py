import threading
import time
from flask import Flask
from bot import start_bot

app = Flask(__name__)


@app.route('/')
def home():
    return "Bot is running!"
  
def run_bot():
    while True:
        try:
            start_bot()
        except Exception as e:
            print(f"Ошибка: {e}, перезапуск через 5 секунд...")
            time.sleep(5)


threading.Thread(target=run_bot, daemon=True).start()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
