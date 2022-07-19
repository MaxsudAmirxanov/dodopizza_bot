import asyncio
from typing import Union
from aiogram import types, Dispatcher
from aiogram.dispatcher import DEFAULT_RATE_LIMIT
from aiogram.dispatcher.handler import CancelHandler, current_handler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.utils.exceptions import Throttled

from utils.db_api.database import Admin

admin_db = Admin()

class IsAdmin(BaseMiddleware):
    """
    Simple middleware
    """

    def __init__(self, limit=DEFAULT_RATE_LIMIT, key_prefix='antiflood_'):
        self.rate_limit = limit
        self.prefix = key_prefix
        super(IsAdmin, self).__init__()

    async def on_process_message(self, message: types.Message, data: dict):
        user_id = message.from_user.id
        result = admin_db.chek_block_customer(user_id)
        print(user_id)
        print(result)
        if result[0][0] == 1:
            await message.answer('К сожалению вы были заблокированы Админом')
            raise CancelHandler
        else:
            pass
    async def on_process_callback_query(self, message: types.CallbackQuery, data: dict):
        user_id = message.from_user.id
        result = admin_db.chek_block_customer(user_id)
        if result[0][0] == 1:
            await message.answer('К сожалению вы были заблокированы Админом')
            raise CancelHandler
        else:
            pass
    # async def message_throttled(self, message: types.Message, throttled: Throttled):
    #     if throttled.exceeded_count <= 2:
    #         await message.reply("Too many requests!")
    # async def on_pre_process_callback_query(self, cq: types.CallbackQuery, data: dict):
    #     await cq.answer()