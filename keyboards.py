from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)


def main_menu() -> ReplyKeyboardMarkup:
    kb = [
        [KeyboardButton(text="🎲 Пройти викторину")],
        [KeyboardButton(text="❤️ О программе опеки")],
        [KeyboardButton(text="📞 Связаться с зоопарком")],
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)


def result_keyboard(bot_username: str, animal_name: str) -> InlineKeyboardMarkup:
    share_text = (
        f"Я прошёл викторину Московского зоопарка и узнал своё тотемное животное - "
        f"{animal_name}! Узнай своё: https://t.me/{bot_username}"
    )
    import urllib.parse
    encoded = urllib.parse.quote(share_text)

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="📲 Поделиться результатом",
                url=f"https://t.me/share/url?url=https://t.me/{bot_username}&text={encoded}",
            )
        ],
        [
            InlineKeyboardButton(text="👍 Классный бот!", callback_data="feedback_positive"),
            InlineKeyboardButton(text="👎 Есть замечания", callback_data="feedback_negative"),
        ],
        [InlineKeyboardButton(text="🔄 Пройти заново", callback_data="restart")],
    ])
    return kb


def feedback_detail_keyboard() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="❓ Вопросы не понравились", callback_data="fb_questions")],
        [InlineKeyboardButton(text="🎯 Результат не подходит", callback_data="fb_result")],
        [InlineKeyboardButton(text="🐛 Бот работал с ошибками", callback_data="fb_bug")],
        [InlineKeyboardButton(text="✏️ Написать отзыв текстом", callback_data="fb_text")],
    ])
    return kb