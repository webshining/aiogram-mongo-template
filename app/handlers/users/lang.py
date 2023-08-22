from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery, Message

from app.keyboards import get_lang_keyboard
from database.services import update_user
from loader import _, dp


@dp.message_handler(Command('lang'))
async def _lang(message: Message):
    await message.answer(_("Select language:"), reply_markup=get_lang_keyboard())


@dp.callback_query_handler(lambda call: call.data.startswith('lang'))
async def _lang_callback(call: CallbackQuery):
    await call.answer()
    update_user(call.from_user.id, lang=call.data[5:])
    try:
        await call.message.edit_text(_("Language changed!", locale=call.data[5:]), reply_markup=get_lang_keyboard())
    except:
        pass