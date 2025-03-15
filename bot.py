from aiogram import Dispatcher, Bot
import asyncio
import os

from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from dotenv import load_dotenv
from ai_request import get_post_text
import os


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


def start_bot():
    print("Bot started!")
    asyncio.run(dp.start_polling(bot))
