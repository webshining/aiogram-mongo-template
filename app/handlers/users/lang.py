from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from loader import dp, _
from app.keyboards import get_lang_marlup
from database.services.users import update_user


@dp.message(Command('lang'))
async def _lang(message: Message):
    await message.answer("Select language:", reply_markup=get_lang_marlup())


@dp.callback_query(lambda call: call.data.startswith('lang'))
async def _lang_callback(call: CallbackQuery):
    await update_user(call.from_user.id, lang=call.data[5:])
    await call.message.edit_text(_("Language changed!", locale=call.data[5:]), reply_markup=None)