from aiogram.contrib.middlewares.i18n import I18nMiddleware

from data.config import I18N_DOMAIN, I18N_PATH

i18n = I18nMiddleware(I18N_DOMAIN, I18N_PATH)