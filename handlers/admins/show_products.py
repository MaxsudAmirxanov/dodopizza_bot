from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters.chek_admin import IsAdmin
from utils.db_api.database import Product

product_db = Product()

from loader import bot

from loader import dp

@dp.message_handler(IsAdmin(), commands='show_products')
async def admin(message: types.Message):
    products = product_db.show_products()
    array = []
    # await message.answer('мяу хуяу')
    print(products)
    array.append('id   Категория   Подкатегория   Название   Цена')
    for i in products:
        print(i)
        
        array.append(f'{i[0]}   {i[1]}   {i[3]}   {i[5]}   {i[7]}')
    await message.answer('\n'.join(array))