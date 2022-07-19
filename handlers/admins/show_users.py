from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters.chek_admin import IsAdmin
from utils.db_api.database import Customer

customer_db = Customer

from loader import bot

from loader import dp

@dp.message_handler(IsAdmin(), commands='show_users')
async def admin(message: types.Message):
    users = customer_db.show_customer()
    array = []
    # await message.answer('мяу хуяу')
    print(users)
    array.append('id   Имя   Фамилия   user_name   user_id')
    for i in users:
        print(i)
        
        array.append(f'{i[0]}   {i[1]}   {i[3]}   {i[6]}   {i[7]}')
    await message.answer('\n'.join(array))
   
    await message.answer('мяу хуяу')
