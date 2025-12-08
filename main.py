import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

TOKEN = "7902096104:AAEv0NPY9UEqDCA1dYMntexql294iMI_zu8"  # підстав свій

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Бот працює! 🎉")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

