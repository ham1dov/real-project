from aiogram.fsm.state import default_state

from states.registration import Registration
from lexicon.lexicon import commands

from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types.message import Message
user_router = Router()

@user_router.message(CommandStart(), default_state=True)
async def start_handler(message:Message):
    await message.answer('hello')
