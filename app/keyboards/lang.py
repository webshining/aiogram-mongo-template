from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder

from loader import i18n


class LangCallback(CallbackData, prefix="lang"):
    lang: str


def get_lang_markup():
    builder = InlineKeyboardBuilder()

    [
        builder.button(text=lang.upper(), callback_data=LangCallback(lang=lang))
        for lang in i18n.available_locales
    ]

    return builder.as_markup()
