import csv
import io

from aiogram.filters import Command
from aiogram.types import BufferedInputFile, Message
from pymongo.asynchronous.client_session import AsyncClientSession

from app.handlers.routers import admin_router as router
from database.models import User


@router.message(Command("users"))
async def _users(message: Message, session: AsyncClientSession):
    file = await _get_users_data(session)
    await message.answer_document(BufferedInputFile(file, "users.csv"))


async def _get_users_data(session: AsyncClientSession):
    file = io.StringIO()
    writer = csv.writer(file)
    writer.writerow(list(User.__annotations__.keys()))
    async for user in User.find(session=session):
        writer.writerow(list(user.dict().values()))
    file.seek(0)
    file = io.BytesIO(file.getvalue().encode())
    file.seek(0)
    return file.getvalue()
