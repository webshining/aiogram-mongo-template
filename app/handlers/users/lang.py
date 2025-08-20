from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from pymongo.asynchronous.client_session import AsyncClientSession

from app.handlers.routers import user_router as router
from app.keyboards import LangKeyboard
from database.models import User
from loader import _


@router.message(Command("lang"))
async def _lang(message: Message, user: User):
    await message.answer(_("Select language:"), reply_markup=LangKeyboard.keyboard(user.lang))


@router.callback_query(LangKeyboard.filter())
async def _lang_callback(call: CallbackQuery, callback_data: LangKeyboard, user: User, session: AsyncClientSession):
    user.lang = callback_data.lang
    await user.save(session)

    await call.message.edit_text(_("Select language:", locale=user.lang), reply_markup=LangKeyboard.keyboard(user.lang))
