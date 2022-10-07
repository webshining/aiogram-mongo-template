from aiogram.types import Message
from aiogram.dispatcher.filters import Command
from loader import dp, _


@dp.message_handler(Command('start'))
async def start_handler(message: Message):
    await message.answer(_('Hello <b>{}</b>').format(message.from_user.full_name))
