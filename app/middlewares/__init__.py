from loader import dp
from .user import UserMiddleware
from .inter import i18n

if __name__ == 'app.middlewares':
    dp.setup_middleware(UserMiddleware())
    dp.setup_middleware(i18n)