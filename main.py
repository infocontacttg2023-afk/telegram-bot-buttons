import os
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from aiogram.enums import ParseMode

from keyboards import test_keyboard

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

@dp.message(Command("post"))
async def post_handler(message: Message):
    args = message.text.split(" ", 1)

    if len(args) < 2:
        await message.reply("Введи текст: /post текст")
        return

    text = args[1]

    # Видаляємо команду користувача
    try:
        await message.delete()
    except:
        pass

    # Надсилаємо пост з кнопками
    await bot.send_message(
        chat_id=message.chat.id,
        text=text,
        reply_markup=test_keyboard()
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
