import asyncio
from aiogram import types
from aiogram.utils.callback_data import CallbackData
from aiogram.dispatcher.filters.builtin import CommandStart
from filters.chek_admin import IsAdmin
from utils.db_api.database import Product, Cart, Customer
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher.storage import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from typing import Union
from aiogram.types import InputFile
from aiogram.types.input_media import InputMediaPhoto

product_db = Product()
cart_db = Cart()
customer_db = Customer()

from loader import bot
from loader import dp, bot


class DeleteCategory(StatesGroup):
    choice = State()
    # name = State()
    # photo = State()
    # price = State()



from keyboards.inline.delete_category_keyboard import categories_keyboard, subcategories_keyboard, menu_cd

product_db = Product()
cart_db = Cart()
customer_db = Customer()

@dp.message_handler(IsAdmin(), commands='delete_category')
async def show_menu(message: types.Message):
    await list_categories(message)

async def list_categories(message: Union[types.Message, types.CallbackGame], **kworgs):
    markup = await categories_keyboard()

    if isinstance(message, types.Message):
        await message.answer("Выберите категорию, которую хотите удалить", reply_markup=markup)
        

    elif isinstance(message, types.CallbackQuery):
        call = message
        await call.message.edit_reply_markup(markup)


async def delete_category(message: Union[types.Message, types.CallbackGame],category,  **kworgs):
    global category_name
    category_name = product_db.get_distinct_category_name(category_code=category)

    await bot.send_message(message.from_user.id, f'Когда удаляется категория, за ним же удаляется и все подкатегории с товарами')
    await asyncio.sleep(3)
    await bot.send_message(message.from_user.id, f'Вы уверены что хотите удалить категорию {category_name[0][0]} ? \n (Да/Нет)')

    await DeleteCategory.choice.set()

@dp.message_handler(state=DeleteCategory.choice)
async def choice(message: types.Message, state: FSMContext):
    answer = message.text
    if answer.lower() == 'да':
        'Удаление категории'
        await message.answer(f'Удаление категории {category_name[0][0]}')
        product_db.delete_category(category_name)

        await state.finish()

    elif answer.lower() == 'нет':
        await message.answer('Отмена удалению')
        await state.finish()

@dp.callback_query_handler(menu_cd.filter())
async def navigate(call: types.CallbackQuery, callback_data: dict):
    current_level = callback_data.get('level')
    category = callback_data.get('category')
    subcategory = callback_data.get('subcategory')
    item_id = callback_data.get('item_id')
    name = callback_data.get('name')
    photo = callback_data.get('photo')
    price = callback_data.get('price')
    
    print(f'5. {callback_data}')


    levels = {
        "0": list_categories,
        "1": delete_category,



    }

    curremt_level_function = levels[current_level]

    await curremt_level_function(
        call, 
        category=category, 
        subcategory=subcategory, 
        item_id=item_id,
        name=name,
        photo=photo,
        price=price
        
    )

