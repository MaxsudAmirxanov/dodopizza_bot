from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters.chek_main_admin import IsMainAdmin
from utils.db_api.database import Admin

admin_db = Admin()

from loader import bot

from loader import dp

@dp.message_handler(IsMainAdmin(), commands='show_admin')
async def show_admin(message: types.Message):
    admins = admin_db.show_admin()
    array = []
    # await message.answer('мяу хуяу')
    # print(products)
    array.append('id | username telegram_id | Имя |  Фамиоие ')
    for i in admins:
        print(i)
        
        array.append(f'{i[0]} |  {i[2]} | {i[3]} | {i[5]} | {i[6]}')
    await message.answer('\n'.join(array))