from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters.chek_admin import IsAdmin
from utils.db_api.database import Product
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher.storage import FSMContext

product_db = Product()

from loader import bot

from loader import dp

class Delete_product(StatesGroup):
    Q1 = State()
    Q2 = State()

@dp.message_handler(IsAdmin(), commands='delete_product')
async def admin(message: types.Message,  state: FSMContext):
    await message.answer(
        'Для удаление продукта введите его ID 👇(чтобы узнать ID, воспользуйтесь коммандой /show_products)\n\n'
        '!!! При удалении товара он удаляется навегда !!! '
    )
    await Delete_product.Q1.set()
    
@dp.message_handler(IsAdmin(), state=Delete_product.Q1)
async def admin(message: types.Message, state: FSMContext):
    answer = message.text
    product = product_db.get_product(int(answer))

    async with state.proxy() as data:
        data['Q1'] = answer
    
    print(product)
    try:
        await message.answer(f'Вы уверены что хотити удалить товар {product[0][5]} ? \n(Да/Нет)')
    except IndexError:
        await message.answer('Товара с таким ID не существует. Чтобы узнать ID товара воспользуйтесь коммандй  /show_products')
        await state.finish() 
    await Delete_product.Q2.set()


    
@dp.message_handler(IsAdmin(), state=Delete_product.Q2)
async def admin(message: types.Message, state: FSMContext):
    text = message.text
    if text.lower() == 'нет':
        await message.answer('Отмена удаления товара')
    elif text.lower() == 'да':
        data = await state.get_data()
        choice = product_db.delete_product(data.get('Q1'))
        product = product_db.get_product(data.get('Q1'))
        print('12345')
        print(product)

        if choice == True:
            # product = product_db.get_product(int(choice))
            await message.answer(f'Товар {product[0][5]} был удален')
        else:
            await message.answer("Товара с таким ID не существует. Чтобы узнать ID товара воспользуйтесь коммандй  /show_products")

    await state.finish() 