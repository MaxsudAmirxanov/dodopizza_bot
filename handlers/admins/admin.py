from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters.chek_admin import IsAdmin

from loader import bot

from loader import dp
array = ['Добро пожаловать Админ',
        'Вот доступные комманды',
        '/block_user',
        '/unblock_user',
        '/show_products',
        '/show_users',
        '/show_admin'
        '/change_product',
        '/add_admin'
        '/add_product'

        ]
@dp.message_handler(IsAdmin(), commands='admin')
async def admin_command(message: types.Message):
    # await message.answer(
    #     'Добро пожаловать Админ\n\n'
    #     'Вот доступные комманды\n'
    #     '/blocked_user'


    # )
    await message.answer('\n'.join(array))