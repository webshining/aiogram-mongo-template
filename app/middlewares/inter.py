from aiogram.utils.i18n import I18n, FSMI18nMiddleware

from data.config import I18N_PATH, I18N_DOMAIN

i18n = I18n(path=I18N_PATH, domain=I18N_DOMAIN)
i18n_middleware = FSMI18nMiddleware(i18n=i18n)