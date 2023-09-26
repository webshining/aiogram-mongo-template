from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_lang_markup():
    builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='English', callback_data='lang_en'),
        InlineKeyboardButton(text='Українська', callback_data='lang_uk'),
        InlineKeyboardButton(text='Русский', callback_data='lang_ru')
    ]
    builder.add(*buttons)
    return builder.as_markup()
