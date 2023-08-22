from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from loader import _, dp


@dp.message_handler(Command('start'))
async def _start(message: Message):
    await message.answer(_('Hello <b>{}</b>').format(message.from_user.full_name))
