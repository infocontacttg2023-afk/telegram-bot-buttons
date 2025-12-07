from aiogram import Bot, Dispatcher, executor, types
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(content_types=['text', 'photo', 'video', 'document'])
async def auto_buttons(message: types.Message):
    if message.chat.type in ["group", "supergroup"]:
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(
            types.InlineKeyboardButton("👍 Лайк", callback_data="like")
        )
        await message.reply("Натисни:", reply_markup=keyboard)

@dp.callback_query_handler()
async def c(callback_query: types.CallbackQuery):
    await callback_query.answer("Готово!")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
