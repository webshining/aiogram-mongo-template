from environs import Env

env = Env()
env.read_env()


TELEGRAM_BOT_TOKEN = env.str('TELEGRAM_BOT_TOKEN')

MONGO_URL = env.str('MONGO_URL', None)

RD_DB = env.int('RD_DB', None)
RD_HOST = env.str('RD_HOST', None)
RD_PORT = env.int('RD_PORT', None)
RD_PASS = env.str('RD_PASS', None)

RATE_LIMIT = env.float('RATE_LIMIT', 0.5)