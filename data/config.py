from pathlib import Path

from environs import Env

env = Env()
env.read_env()

DIR = Path(__file__).absolute().parent.parent

TELEGRAM_BOT_TOKEN = env.str('TELEGRAM_BOT_TOKEN')

MONGO_URL = env.str('MONGO_URL', None)

RD_DB = env.int('RD_DB', None)
RD_HOST = env.str('RD_HOST', None)
RD_PORT = env.int('RD_PORT', None)
RD_PASS = env.str('RD_PASS', None)

RATE_LIMIT = env.float('RATE_LIMIT', 0.5)

I18N_PATH = f'{DIR}/data/locales'
I18N_DOMAIN = env.str('I18N_DOMAIN', 'bot')
