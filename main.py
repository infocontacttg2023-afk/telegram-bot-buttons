from aiogram import Bot, Dispatcher, executor, types
import os
import logging

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN is not set in environment variables")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(content_types=['text', 'photo', 'video', 'document'])
async def add_buttons(message: types.Message):
    if message.chat.type in ['group', 'supergroup']:
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(
            types.InlineKeyboardButton("👍 Лайк", callback_data="like"),
            types.InlineKeyboardButton("💬 Коментар", callback_data="comment")
        )
        await message.reply("Оберіть дію:", reply_markup=keyboard)

@dp.callback_query_handler(lambda c: c.data in ['like', 'comment'])
async def process_callback(call: types.CallbackQuery):
    if call.data == "like":
        await call.answer("Ти поставив лайк 👍")
    else:
        await call.answer("Ти хочеш залишити коментар 💬")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
