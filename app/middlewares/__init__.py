from app.middlewares.user import UserMiddleware
from loader import dp

if __name__ == 'app.middlewares':
    dp.setup_middleware(UserMiddleware())
