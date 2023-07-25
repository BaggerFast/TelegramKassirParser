from aiogram import Dispatcher
from aiogram.types import BotCommand

from bot.handlers.city_router import city_router
from bot.handlers.concert_router import concert_router
from bot.handlers.main_router import common_router, main_router

bot_commands = [
    BotCommand(command="/start", description="Начало работы с ботом")
]


def register_handlers(dp: Dispatcher):
    main_router.include_routers(concert_router, city_router, common_router)
    dp.include_router(main_router)
