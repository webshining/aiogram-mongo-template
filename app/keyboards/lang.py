from aiogram.filters.callback_data import CallbackData

from loader import i18n

from .base import BaseInlineKeyboard


class LangKeyboard(BaseInlineKeyboard):
    def keyboard(self):
        builder = self.builder()

        for lang in i18n.available_locales:
            builder.button(text=lang.upper(), callback_data=self._get_data(lang=lang))
        builder.adjust(3)

        return builder.as_markup()

    class Callback(CallbackData, prefix="lang"):
        lang: str


LangKeyboard = LangKeyboard()
