from aiogram.utils.i18n import I18n, SimpleI18nMiddleware

from data.config import I18N_PATH, I18N_DOMAIN

i18n = I18n(path=I18N_PATH, domain=I18N_DOMAIN)
i18n_middleware = SimpleI18nMiddleware(i18n, )