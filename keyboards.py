from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def test_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Тест 1", callback_data="t1"),
                InlineKeyboardButton(text="Тест 2", callback_data="t2"),
            ],
            [
                InlineKeyboardButton(text="Тест 3", callback_data="t3"),
                InlineKeyboardButton(text="Тест 4", callback_data="t4"),
            ]
        ]
    )
