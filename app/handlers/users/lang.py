from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from loader import dp, _
from app.keyboards import get_lang_marlup


@dp.message(Command('lang'))
async def _lang(message: Message):
    await message.answer("Select language:", reply_markup=get_lang_marlup())


@dp.callback_query(lambda call: call.data.startswith('lang'))
async def _lang_callback(call: CallbackQuery):
    await call.message.edit_text(_("Language changed!"), reply_markup=None)