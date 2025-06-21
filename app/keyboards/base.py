from aiogram.filters.callback_data import CallbackQueryFilter
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram.utils.magic_filter import MagicFilter


class BaseInlineKeyboard:
    builder = InlineKeyboardBuilder

    @classmethod
    def filter(cls, rule: MagicFilter | None = None) -> CallbackQueryFilter:
        return cls.Callback.filter(rule)

    @classmethod
    def _get_data(cls, **kwargs) -> str:
        return cls.Callback(**kwargs).pack()


class BaseReplyKeyboard:
    builder = ReplyKeyboardBuilder
