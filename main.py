from aiogram import Bot, Dispatcher, executor, types
import os

# Беремо токен з Render / Environment Variables
TOKEN = os.getenv("7902096104:AAEv0NPY9UEqDCA1dYMntexql294iMI_zu8")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Коли хтось пише текст/кидає фото/відео/документ у групі
@dp.message_handler(content_types=['text', 'photo', 'video', 'document'])
async def add_buttons(message: types.Message):
    if message.chat.type in ['group', 'supergroup']:
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(
            types.InlineKeyboardButton("👍 Лайк", callback_data="like"),
            types.InlineKeyboardButton("💬 Комент", callback_data="comment")
        )
        await message.reply("Оберіть дію:", reply_markup=keyboard)

# Обробка натискань
@dp.callback_query_handler(lambda c: c.data in ['like', 'comment'])
async def process_callback(call: types.CallbackQuery):
    if call.data == "like":
        await call.answer("Ти поставив лайк 👍")
    elif call.data == "comment":
        await call.answer("Ти хочеш залишити коментар 💬")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
