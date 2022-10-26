from loader import dp
from .user import UserMiddleware

if __name__ == 'app.middlewares':
    dp.update.middleware(UserMiddleware())