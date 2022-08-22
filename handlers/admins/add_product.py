
from os import stat
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
from loader import dp


class AddProduct(StatesGroup):
    # category_name = State()
    # cstegory_code = State()
    # subcategory_name = State()
    # subcatgory_code = State()
    item_id = State()
    category_name = State()
    category_code = State()
    subcategory_name = State()
    subcategory_code = State()
    name = State()
    photo = State()
    price = State()





from keyboards.inline.add_product_keyboard import categories_keyboard, subcategories_keyboard, menu_cd

product_db = Product()
cart_db = Cart()
customer_db = Customer()

@dp.message_handler(IsAdmin(), commands='add_product')
async def show_menu(message: types.Message):
    await list_categories(message)

async def list_categories(message: Union[types.Message, types.CallbackGame], **kworgs):
    markup = await categories_keyboard()

    if isinstance(message, types.Message):
        # p_3 = open('photo_3.png', 'rb')
        await message.answer("Выберите категорию товара, в которую хотите добавить товар", reply_markup=markup)
        

    elif isinstance(message, types.CallbackQuery):
        call = message
        await call.message.edit_reply_markup(markup)

async def list_subcategoies(callback: types.CallbackQuery, category, **kwargs):
    # print(f"1.1 {category}")
    markup = await subcategories_keyboard(category)
    # await callback.message.edit_reply_markup(markup)
    await callback.message.edit_text('Выберите подкатегорию товара, в которую хотите добавить товар', reply_markup=markup)

async def add_new_product(callback: types.CallbackQuery, category, subcategory, **kwargs):
    # print(f"1.1 {category}")
    # markup = await subcategories_keyboard(category)
    # await callback.message.edit_reply_markup(markup)
    # await callback.message.edit_text('Выберите подкатегорию товара, в которую хотите добавить товар', reply_markup=markup)

    product_category = product_db.get_distinct_category_name(category_code=category)
    product_subcategory = product_db.get_distinct_subcategory_name(category_code=category, subcategory_code=subcategory)


    cur_state = dp.current_state()
    async with cur_state.proxy() as data:
        data['category_code'] = category
        data['subcategory_code'] = subcategory
        data['category_name'] = product_category[0][0]
        data['subcategory_name'] = product_subcategory[0][0]

    await callback.message.answer(f'Введите название товара, которую вы хотите добавить в подкатегорию  {product_subcategory[0][0]}')

    await AddProduct.name.set()

@dp.message_handler(state=AddProduct.name)
async def price(message: types.Message, **kwargs):
    new_name = message.text

    cur_state = dp.current_state()
    async with cur_state.proxy() as data:
        data['name'] = new_name

    await message.answer(f'Введите цену для товара {new_name}')

    await AddProduct.price.set()

@dp.message_handler(state=AddProduct.price)
async def price(message: types.Message, **kwargs):
    new_price = message.text

    cur_state = dp.current_state()
    async with cur_state.proxy() as data:
        data['price'] = new_price

    data = await cur_state.get_data()
    product_name = data.get('name')
    await message.answer(f'Отправть фотографию, для товара {product_name}')

    await AddProduct.photo.set()

@dp.message_handler(state=AddProduct.photo, content_types=types.ContentTypes.PHOTO)
async def price(message: types.Message, **kwargs):
    product_photo = message.photo[0].file_id
    

    cur_state = dp.current_state()
    async with cur_state.proxy() as data:
        data['photo'] = product_photo

    data = await cur_state.get_data()
    product_name = data.get('name')
    product_price = data.get('price')
    product_category = data['category_name']
    product_category_code = data['category_code']
    product_subcategory = data['subcategory_name']
    product_subcategory_code = data['subcategory_code']
    
    await message.answer(f'{product_name} {product_price} {product_photo} {product_category} {product_category_code} {product_subcategory} {product_subcategory_code}')

    product_db.add_product(name=product_name, category_code=data.get('category_code'), category_name=data.get('category_name'),\
                                 subcategory_code=data.get('subcategory_code'), subcategory_name=data.get('subcategory_name'), \
                                    photo=product_photo, price=product_price)

    await message.answer(f'Добавлен новый товар {product_name}')

    await cur_state.finish()

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
        "1": list_subcategoies,
        "2": add_new_product
        # "3": show_item,
        # "4": edit_name,
        # '5': edit_price,
        # '6': edit_photo


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

