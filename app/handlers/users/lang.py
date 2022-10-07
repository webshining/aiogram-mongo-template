from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Command

from loader import dp, _, i18n
from app.keyboards import get_lang_markup
from database.services import edit_user_language


@dp.message_handler(Command('lang'))
async def lang_handler(message: Message):
    await message.answer(_('Select language:'), reply_markup=get_lang_markup())
    

@dp.callback_query_handler(lambda call: call.data.startswith('lang'))
async def lang_callback_query(call: CallbackQuery):
    await call.answer()
    edit_user_language(call.from_user.id, call.data[5:])
    i18n.set_user_locale(call.data[5:])
    await call.message.edit_text(_('Language changed'), reply_markup=None)