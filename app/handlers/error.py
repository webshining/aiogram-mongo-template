from aiogram.types import ErrorEvent

from loader import dp
from utils import logger


@dp.error()
async def _error(event: ErrorEvent):
    logger.warning(event.exception)

