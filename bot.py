from aiogram import Dispatcher, Bot
import asyncio
import os

from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from dotenv import load_dotenv
from ai_request import get_post_text
import os
import threading
import http.server
import socketserver


def run_dummy_server():
    port = int(os.environ.get("PORT", 8080))  # Render требует, чтобы сервис слушал порт
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        httpd.serve_forever()

threading.Thread(target=run_dummy_server, daemon=True).start()


load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher()
bot = Bot(BOT_TOKEN)


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Hello, welcome to bot!")


@dp.message(Command("news"))
async def cmd_news(message: Message):
    await message.answer(get_post_text())


if __name__ == "__main__":
    try:
        print("Bot started!")
        asyncio.run(dp.start_polling(bot))
    except KeyboardInterrupt:
        print("Exit.")
