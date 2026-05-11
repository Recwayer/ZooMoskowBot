import config
from datetime import datetime
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def send_result_to_admin(bot, user, animal_data: dict) -> None:
    if not config.ADMIN_ID:
        return

    text = (
        "🔔 <b>Новый результат викторины!</b>\n\n"
        f"👤 Имя: <b>{user.full_name}</b>\n"
        f"🆔 ID: <code>{user.id}</code>\n"
        f"📌 Username: @{user.username or 'нет'}\n"
        f"🕒 Время: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}\n\n"
        f"🦒 Тотемное животное: <b>{animal_data['name']} {animal_data['emoji']}</b>\n"
        f"🔗 {animal_data['link']}"
    )

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💬 Написать пользователю", url=f"tg://user?id={user.id}")]
    ])

    try:
        await bot.send_message(
            chat_id=config.ADMIN_ID,
            text=text,
            parse_mode="HTML",
            reply_markup=markup,
        )
    except Exception as e:
        print(f"⚠️ Ошибка отправки результата администратору: {e}")


async def send_feedback_to_admin(bot, user, feedback_text: str) -> None:
    if not config.ADMIN_ID:
        return

    text = (
        "💬 <b>Новый отзыв о боте!</b>\n\n"
        f"👤 Имя: <b>{user.full_name}</b>\n"
        f"🆔 ID: <code>{user.id}</code>\n"
        f"📌 Username: @{user.username or 'нет'}\n"
        f"🕒 Время: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}\n\n"
        f"📝 Отзыв: {feedback_text}"
    )

    try:
        await bot.send_message(
            chat_id=config.ADMIN_ID,
            text=text,
            parse_mode="HTML",
        )
    except Exception as e:
        print(f"⚠️ Ошибка отправки отзыва администратору: {e}")