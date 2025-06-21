from aiogram.fsm.state import State, StatesGroup


class NotifyState(StatesGroup):
    text = State()
