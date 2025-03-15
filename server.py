import threading
import time
from flask import Flask
from bot import start_bot
import asyncio

app = Flask(__name__)


def run_flask():
    app.run(host="0.0.0.0", port=10000)


threading.Thread(target=run_flask, daemon=True).start()


if __name__ == "__main__":
    asyncio.run(start_bot())
