from aiogram.types import Message
from aiogram.contrib.middlewares.i18n import I18nMiddleware
from data.config import I18N_DOMAIN, I18N_PATH


class ACLMiddleware(I18nMiddleware):
    async def get_user_locale(self, action: str, args: list[Message, dict[str]]):
        *_, data = args
        user = data['user']

        return user.language

    def set_user_locale(self, locale: str):
        self.ctx_locale.set(locale)

    async def trigger(self, action, args):
        if 'update' not in action and 'error' not in action and action.startswith('process'):
            locale = await self.get_user_locale(action, args)
            self.set_user_locale(locale)
            return True


i18n = ACLMiddleware(I18N_DOMAIN, I18N_PATH)