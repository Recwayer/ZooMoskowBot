import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    FSInputFile,
)

import config
from data import animals, questions
from keyboards import main_menu, result_keyboard, feedback_detail_keyboard
from utils import send_result_to_admin, send_feedback_to_admin

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)

bot = Bot(
    token=config.BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML),
)
dp = Dispatcher(storage=MemoryStorage())

class QuizStates(StatesGroup):
    answering = State()
    waiting_feedback_text = State()

@dp.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer(
        "🦒 <b>Добро пожаловать в Московский зоопарк!</b>\n\n"
        "Пройди викторину и узнай, какое животное - твоё тотемное по духу ❤️\n\n"
        "Нажми <b>«🎲 Пройти викторину»</b>, чтобы начать.",
        reply_markup=main_menu(),
    )


@dp.message(Command("help"))
async def cmd_help(message: Message) -> None:
    await message.answer(
        "ℹ️ <b>Как пользоваться ботом</b>\n\n"
        "🎲 <b>Пройти викторину</b> - ответь на 10 вопросов и узнай своё тотемное животное.\n"
        "❤️ <b>О программе опеки</b> - как взять животное под опеку и помочь зоопарку.\n"
        "📞 <b>Связаться с зоопарком</b> - адрес, телефон, сайт и Telegram-канал.\n\n"
        "Если что-то пошло не так - нажми /start, чтобы начать заново.\n\n"
        "По вопросам о программе опеки: "
        "<a href='https://moscowzoo.ru/my-zoo/become-a-guardian/'>moscowzoo.ru</a>",
        reply_markup=main_menu(),
    )



@dp.message(F.text == "🎲 Пройти викторину")
async def start_quiz(message: Message, state: FSMContext) -> None:
    await state.clear()
    user = message.from_user
    await state.update_data(
        scores={animal: 0 for animal in animals.keys()},
        question_index=0,
        user_id=user.id,
        user_full_name=user.full_name,
        user_username=user.username,
    )
    await message.answer(
        "🎉 Отлично! Начинаем викторину.\n"
        "Впереди <b>10 вопросов</b> - выбирай ответ, который ближе всего к твоему характеру.\n\n"
        "Поехали! 🚀"
    )
    await ask_question(message, state)


async def ask_question(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    index = data.get("question_index", 0)

    if index >= len(questions):
        await show_result(message, state)
        return

    q = questions[index]

    buttons = []
    for ans_idx, ans in enumerate(q["answers"]):
        buttons.append([
            InlineKeyboardButton(
                text=ans["text"],
                callback_data=f"ans_{q['id']}_{ans_idx}",
            )
        ])

    kb = InlineKeyboardMarkup(inline_keyboard=buttons)

    await message.answer(
        f"<b>Вопрос {index + 1} из {len(questions)}</b>\n\n{q['text']}",
        reply_markup=kb,
    )
    await state.set_state(QuizStates.answering)


@dp.callback_query(QuizStates.answering, F.data.startswith("ans_"))
async def process_answer(callback: CallbackQuery, state: FSMContext) -> None:
    parts = callback.data.split("_")
    if len(parts) < 3:
        await callback.answer("❌ Ошибка. Попробуйте ещё раз.")
        return

    _, qid, ans_idx_str = parts[0], parts[1], parts[2]

    try:
        ans_idx = int(ans_idx_str)
    except ValueError:
        await callback.answer("❌ Ошибка данных.")
        return

    question = next((q for q in questions if str(q["id"]) == qid), None)
    if not question or ans_idx >= len(question["answers"]):
        await callback.answer("❌ Вопрос не найден.")
        return

    chosen_answer = question["answers"][ans_idx]

    data = await state.get_data()
    scores = data.get("scores", {animal: 0 for animal in animals.keys()})

    for animal_key, points in chosen_answer["animal_points"].items():
        if animal_key in scores:
            scores[animal_key] += points

    await state.update_data(
        scores=scores,
        question_index=data.get("question_index", 0) + 1,
    )

    await callback.answer("✅")
    await callback.message.edit_reply_markup(reply_markup=None)

    await ask_question(callback.message, state)



async def show_result(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    scores = data.get("scores", {})

    class _UserProxy:
        def __init__(self, d: dict):
            self.id = d.get("user_id", 0)
            self.full_name = d.get("user_full_name", "Неизвестно")
            self.username = d.get("user_username")

    real_user = _UserProxy(data)

    if not scores or max(scores.values()) == 0:
        winner_key = "lesser_eagle"
    else:
        winner_key = max(scores, key=scores.get)

    animal = animals[winner_key]

    try:
        bot_info = await bot.get_me()
        bot_username = bot_info.username
    except Exception:
        bot_username = "MoscowZooBot"

    result_text = (
        f"🎉 <b>Твоё тотемное животное - {animal['name']} {animal['emoji']}</b>\n\n"
        f"{animal['description']}\n\n"
        f"🔗 <a href=\"{animal['link']}\">Подробнее о {animal['name']} на сайте зоопарка</a>\n\n"
        "------------─\n"
        "❤️ <b>Хочешь помочь этому животному?</b>\n"
        "В Московском зоопарке работает программа <b>«Возьми животное под опеку»</b>. "
        "Твоё пожертвование идёт на уход за питомцами и сохранение редких видов.\n"
        "Стать опекуном может каждый - и ребёнок, и большая компания!\n\n"
        "👉 <a href='https://moscowzoo.ru/my-zoo/become-a-guardian/'>Узнать о программе опеки</a>"
    )

    try:
        photo = FSInputFile(animal["image"])
        await message.answer_photo(
            photo=photo,
            caption=result_text,
            reply_markup=result_keyboard(bot_username, f"{animal['name']} {animal['emoji']}"),
        )
    except Exception as e:
        logger.warning("Не удалось загрузить фото: %s", e)
        await message.answer(
            result_text,
            reply_markup=result_keyboard(bot_username, f"{animal['name']} {animal['emoji']}"),
            disable_web_page_preview=True,
        )

    await send_result_to_admin(bot, real_user, animal)
    await state.clear()


@dp.callback_query(F.data == "feedback_positive")
async def feedback_positive(callback: CallbackQuery) -> None:
    await callback.answer("🙏 Спасибо за отзыв!")
    await callback.message.answer(
        "❤️ Рады, что тебе понравилось! Рассказывай друзьям о зоопарке 🦒\n\n"
        "Если захочешь пройти викторину ещё раз - нажми «🎲 Пройти викторину».",
        reply_markup=main_menu(),
    )
    await send_feedback_to_admin(bot, callback.from_user, "👍 Положительный отзыв")


@dp.callback_query(F.data == "feedback_negative")
async def feedback_negative(callback: CallbackQuery) -> None:
    await callback.answer()
    await callback.message.answer(
        "😔 Жаль, что что-то не понравилось. Расскажи подробнее - это поможет нам стать лучше:",
        reply_markup=feedback_detail_keyboard(),
    )


@dp.callback_query(F.data.startswith("fb_"))
async def feedback_detail(callback: CallbackQuery, state: FSMContext) -> None:
    labels = {
        "fb_questions": "❓ Вопросы не понравились",
        "fb_result": "🎯 Результат не подходит",
        "fb_bug": "🐛 Бот работал с ошибками",
    }

    if callback.data == "fb_text":
        await callback.answer()
        await callback.message.answer(
            "✏️ Напиши свой отзыв в следующем сообщении - мы его обязательно прочитаем:"
        )
        await state.set_state(QuizStates.waiting_feedback_text)
        return

    label = labels.get(callback.data, callback.data)
    await callback.answer("Спасибо!")
    await callback.message.answer(
        "🙏 Спасибо! Мы учтём твой отзыв и постараемся стать лучше.",
        reply_markup=main_menu(),
    )
    await send_feedback_to_admin(bot, callback.from_user, label)


@dp.message(QuizStates.waiting_feedback_text)
async def receive_feedback_text(message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer(
        "🙏 Спасибо за отзыв! Мы обязательно его изучим.",
        reply_markup=main_menu(),
    )
    await send_feedback_to_admin(bot, message.from_user, f"✏️ {message.text}")

@dp.callback_query(F.data == "restart")
async def restart(callback: CallbackQuery, state: FSMContext) -> None:
    await state.clear()
    await callback.answer()
    await callback.message.answer(
        "🔄 Начинаем заново! Выбери действие в меню:",
        reply_markup=main_menu(),
    )


@dp.message(F.text == "❤️ О программе опеки")
async def about_guardianship(message: Message) -> None:
    await message.answer(
        "❤️ <b>Программа «Возьми животное под опеку»</b>\n\n"
        "Сейчас в Московском зоопарке живёт около <b>6 000 животных</b> - каждое требует внимания и ухода.\n\n"
        "Ты можешь взять под опеку слона, льва, суриката, фламинго или другого обитателя зоопарка. "
        "Стоимость опеки рассчитывается из ежедневного рациона животного - пожертвование подойдёт на любую сумму.\n\n"
        "<b>Что получает опекун:</b>\n"
        "- Почётный статус опекуна\n"
        "- Возможность круглый год навещать подопечного\n"
        "- Новости о жизни и самочувствии животного\n\n"
        "Участником может стать каждый - и ребёнок, и большая корпорация.\n\n"
        "👉 <a href='https://moscowzoo.ru/my-zoo/become-a-guardian/'>Подробнее на сайте зоопарка</a>",
        disable_web_page_preview=False,
    )


@dp.message(F.text == "📞 Связаться с зоопарком")
async def contact_zoo(message: Message) -> None:
    await message.answer(
        "📞 <b>Связаться с Московским зоопарком</b>\n\n"
        "🕒 <b>Часы работы:</b> ежедневно с 07:30 до 21:00\n"
        "📍 <b>Адрес:</b> Б. Грузинская ул., 1, Москва, 123242\n\n"
        "📞 <b>Телефон:</b> +7 495 775-33-70\n"
        "🌐 <b>Сайт:</b> <a href='https://moscowzoo.ru/'>moscowzoo.ru</a>\n"
        "📧 <b>Email:</b> info@moscowzoo.ru",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="📲 Telegram зоопарка", url="https://t.me/Moscowzoo_official")],
            [InlineKeyboardButton(text="🌐 Официальный сайт", url="https://moscowzoo.ru/")],
            [InlineKeyboardButton(text="❤️ Стать опекуном", url="https://moscowzoo.ru/my-zoo/become-a-guardian/")],
        ]),
        disable_web_page_preview=True,
    )


@dp.message(QuizStates.answering)
async def fallback_during_quiz(message: Message) -> None:
    await message.answer(
        "⬆️ Пожалуйста, выбери один из вариантов ответа выше - нажми на кнопку под вопросом."
    )


@dp.message()
async def fallback_default(message: Message) -> None:
    await message.answer(
        "🤔 Не совсем понимаю эту команду.\n\n"
        "Используй кнопки меню или напиши /help для справки.",
        reply_markup=main_menu(),
    )



async def main() -> None:
    logger.info("Бот запускается...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())