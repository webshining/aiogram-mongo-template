from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder

from loader import i18n


class LangKeyboard(CallbackData, prefix="lang"):
    lang: str

    @staticmethod
    def keyboard(lang: str):
        builder = InlineKeyboardBuilder()

        for l in i18n.available_locales:
            builder.button(text=f'{l.upper()} *' if l == lang else l.upper(), callback_data=LangKeyboard(lang=l).pack())
        builder.adjust(3)

        return builder.as_markup()
