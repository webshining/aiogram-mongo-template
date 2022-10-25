from aiogram.types import Message
from aiogram.filters import Command


from loader import dp


@dp.message(Command("start"))
async def _start(message: Message):
    await message.answer(f'Hello <b>{message.from_user.full_name}</b>')
