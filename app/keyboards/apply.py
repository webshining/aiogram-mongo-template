from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder


class ApplyKeyboard(CallbackData, prefix="apply"):
    data: str

    @staticmethod
    def keyboard(data: str):
        builder = InlineKeyboardBuilder()

        builder.button(text="🆗", callback_data=ApplyKeyboard(data=data).pack())

        return builder.as_markup()
