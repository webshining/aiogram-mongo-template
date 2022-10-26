from aiogram.types import Message
from aiogram.filters import Command


from loader import dp, _


@dp.message(Command("start"))
async def _start(message: Message):
    await message.answer(_('Hello <b>{}</b>').format(message.from_user.full_name))
