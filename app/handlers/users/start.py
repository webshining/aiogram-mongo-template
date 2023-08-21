from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from loader import _

router = Router()


@router.message(Command("start"))
async def _start(message: Message):
    await message.answer(_('Hello <b>{}</b>').format(message.from_user.full_name))
