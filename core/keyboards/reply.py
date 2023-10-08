from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_reply_keyboard(buttons: list) -> ReplyKeyboardMarkup:
    keyboard_builder = ReplyKeyboardBuilder()

    for t in buttons:
        keyboard_builder.button(text=t)

    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup(resize_keyboard=True, one_time_keyboard=False)
