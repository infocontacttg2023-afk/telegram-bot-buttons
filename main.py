import os
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart, Command
from aiogram.enums import ChatType

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise ValueError("BOT_TOKEN environment variable is missing!")

bot = Bot(token=TOKEN)
dp = Dispatcher()


# Хендлер для будь-яких повідомлень у групах
@dp.message(
    F.chat.type.in_({ChatType.GROUP, ChatType.SUPERGROUP})
)
async def add_buttons(message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="👍 Лайк", callback_data="like"),
                InlineKeyboardButton(text="💬 Коментар", callback_data="comment")
            ]
        ]
    )

    await message.reply("Оберіть дію:", reply_markup=keyboard)


# Обробка callback кнопок
@dp.callback_query(F.data == "like")
async def process_like(call):
    await call.answer("Ти поставив лайк 👍")


@dp.callback_query(F.data == "comment")
async def process_comment(call):
    await call.answer("Ти хочеш залишити коментар 💬")


# Старт бота
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
