def setup_middlewares(dp):
    from .user import UserMiddleware
    from .i18n import i18n

    dp.setup_middleware(UserMiddleware())
    dp.setup_middleware(i18n)
