from aiogram.types.inline_keyboard import (InlineKeyboardButton,
                                           InlineKeyboardMarkup)


def get_lang_keyboard():
    keyboard = InlineKeyboardMarkup(3)

    buttons = [
        InlineKeyboardButton(text='English', callback_data='lang_en'),
        InlineKeyboardButton(text='Українська', callback_data='lang_uk'),
        InlineKeyboardButton(text='Русский', callback_data='lang_ru')
    ]

    keyboard.add(*buttons)
    
    return keyboard