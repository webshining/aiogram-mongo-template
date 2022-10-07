from .user import UserMiddleware
from .i18n import i18n
from loader import dp

if __name__ == 'app.middlewares':
    dp.setup_middleware(UserMiddleware())
    dp.setup_middleware(i18n)
