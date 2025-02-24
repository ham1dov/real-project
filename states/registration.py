from aiogram.fsm.state import State, StatesGroup

class Registration(StatesGroup):
    Language = State()
    Name = State()
    Phone = State()
    Address = State()
