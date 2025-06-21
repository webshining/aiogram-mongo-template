from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from loader import i18n

from .base import BaseInlineKeyboard


class ApplyKeyboard(BaseInlineKeyboard):
    def keyboard(self, data: str):
        builder = self.builder()

        builder.button(text="🆗", callback_data=self._get_data(data=data))

        return builder.as_markup()

    class Callback(CallbackData, prefix="apply"):
        data: str


ApplyKeyboard = ApplyKeyboard()
