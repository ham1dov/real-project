import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from config.config import token, admins



async def main():
    bot = Bot(token=token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher(storage=MemoryStorage())
    await bot.delete_webhook(drop_pending_updates=True)

    # dp.include_router(admin_router)
    # dp.include_router(user_router)
    try:
        for admin in admins:
            await bot.send_message(chat_id=admin, text='Launching...')
    except:
        print('There is a problem with launching bot or chat not found')
    await dp.start_polling(bot)

asyncio.run(main())

