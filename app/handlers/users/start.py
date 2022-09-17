from aiogram.types import Message
from aiogram.dispatcher.filters import Command
from loader import dp


@dp.message_handler(Command('start'))
async def start_handler(message: Message):
    await message.answer(f'Hello <b>{message.from_user.full_name}</b>')
