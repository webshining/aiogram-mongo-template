import asyncio

from aiogram import F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from pymongo.asynchronous.client_session import AsyncClientSession

from app.handlers.routers import admin_router as router
from app.keyboards import ApplyKeyboard
from app.states import NotifyState
from database.models import User
from loader import _
from utils import logger


@router.message(Command("notify"))
async def _notify(message: Message, state: FSMContext):
    await message.answer(_("Enter message text:"))
    await state.set_state(NotifyState.text)


@router.message(NotifyState.text)
async def _notify_to_message(message: Message, state: FSMContext):
    await message.copy_to(chat_id=message.chat.id, reply_markup=ApplyKeyboard.keyboard("notify"))
    await message.delete()
    await state.set_state(None)


@router.callback_query(ApplyKeyboard.filter(F.data == "notify"))
async def _notify_to(call: CallbackQuery, session: AsyncClientSession):
    async for u in User.find(session=session):
        try:
            await call.message.copy_to(chat_id=u.id, reply_markup=None)
        except Exception as e:
            logger.error(e)
            logger.error(f"message for {u.id} was not sent")
        await asyncio.sleep(0.5)
    await call.message.edit_reply_markup(reply_markup=None)
    await call.answer()
