from aiogram import Bot, Dispatcher
from motor.motor_tornado import MotorClient

from data.config import TELEGRAM_BOT_TOKEN, RD_DB, RD_HOST, RD_PASS, RD_PORT, MONGO_URL

bot = Bot(TELEGRAM_BOT_TOKEN, parse_mode="HTML")
if RD_DB and RD_HOST and RD_PORT:
    from aiogram.fsm.storage.redis import RedisStorage
    from redis.asyncio.client import Redis
    storage = RedisStorage(Redis(db=RD_DB, host=RD_HOST, port=RD_PORT, password=RD_PASS))
else:
    from aiogram.fsm.storage.memory import MemoryStorage
    storage = MemoryStorage()
dp = Dispatcher(storage=storage)

client = MotorClient(MONGO_URL)
db = client['bot']

from app.middlewares.inter import i18n
_ = i18n.gettext