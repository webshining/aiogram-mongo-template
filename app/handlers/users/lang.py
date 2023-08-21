from aiogram import Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from app.keyboards import get_lang_markup
from database.services.users import update_user
from loader import _

router = Router()


@router.message(Command('lang'))
async def _lang(message: Message):
    await message.answer(_("Select language:"), reply_markup=get_lang_markup())


@router.callback_query(lambda call: call.data.startswith('lang'))
async def _lang_callback(call: CallbackQuery):
    await update_user(call.from_user.id, lang=call.data[5:])
    await call.message.edit_text(_("Language changed!", locale=call.data[5:]), reply_markup=None)