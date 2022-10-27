from loader import dp
from .user import UserMiddleware
from .inter import i18n_middleware

if __name__ == 'app.middlewares':
    dp.update.middleware(i18n_middleware)
    dp.update.middleware(UserMiddleware())