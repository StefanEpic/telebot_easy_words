import random

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message

from core.keyboards.reply import get_reply_keyboard
from core.services.base import get_words


class AnswerForm(StatesGroup):
    GET_ANSWER = State()


async def play(message: Message, state: FSMContext):
    words = await get_words()
    buttons = [words["ru"]] + words["invalid"]
    random.shuffle(buttons)
    await state.update_data(answer=words["ru"])
    await state.set_state(AnswerForm.GET_ANSWER)

    await message.answer(
        text=f"🤖: {words['en']}",
        reply_markup=get_reply_keyboard(buttons),
    )


async def get_answer(message: Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get("answer")
    if message.text == answer:
        await message.reply("🤖: 👍")
    else:
        await message.reply(f"🤖: 👎\n🤖: {answer}")
    await state.clear()
    await play(message, state)
