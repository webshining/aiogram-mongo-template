from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from app.keyboards import LangCallback, get_lang_markup
from app.routers import user_router as router
from database.models import User
from loader import _


@router.message(Command("lang"))
async def _lang(message: Message):
    await message.answer(_("Select language:"), reply_markup=get_lang_markup())


@router.callback_query(LangCallback.filter())
async def _lang_callback(call: CallbackQuery, callback_data: LangCallback):
    await User.update(call.from_user.id, lang=callback_data.lang)
    await call.message.edit_text(
        _("Language changed!", locale=callback_data.lang), reply_markup=None
    )
