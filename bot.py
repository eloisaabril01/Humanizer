import os
import logging
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command

logging.basicConfig(level=logging.INFO)
TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.reply("Hello! Send me your text or upload a .docx/.txt file, and I'll humanize it for you.")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
