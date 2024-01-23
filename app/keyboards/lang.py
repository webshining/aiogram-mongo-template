from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from loader import i18n


def get_lang_markup():
    builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text=lang.upper(), callback_data=f'lang_{lang}') for lang in i18n.available_locales
    ]
    builder.add(*buttons)
    return builder.as_markup()
