from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_lang_markup():
    markup = InlineKeyboardMarkup(row_width=1)
    
    buttons = [
        InlineKeyboardButton(text='🇺🇸 English', callback_data='lang_en'),
        InlineKeyboardButton(text='🇺🇦 Українська', callback_data='lang_ua'),
        InlineKeyboardButton(text='🇷🇺 Русский', callback_data='lang_ru')
    ]
    markup.add(*buttons)
    
    return markup