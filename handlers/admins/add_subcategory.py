

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
from googletrans import Translator

product_db = Product()
cart_db = Cart()
customer_db = Customer()

from loader import bot
from loader import dp


class AddSubcategory(StatesGroup):
    category_name = State()
    category_code = State()
    subcategory_name = State()
    subcategory_code = State()
    choice = State()





from keyboards.inline.add_subcategory_keyboard import categories_keyboard,  menu_cd

product_db = Product()
cart_db = Cart()
customer_db = Customer()

@dp.message_handler(IsAdmin(), commands='add_subcategory')
async def show_menu(message: types.Message):
    await list_categories(message)

async def list_categories(message: Union[types.Message, types.CallbackGame], **kworgs):
    markup = await categories_keyboard()

    if isinstance(message, types.Message):
        # p_3 = open('photo_3.png', 'rb')
        await message.answer("Выберите категорию товара, в которую хотите добавить подкатегорию", reply_markup=markup)
        

    # elif isinstance(message, types.CallbackQuery):
    #     call = message
    #     await call.message.edit_reply_markup(markup)
async def add_subcategory(callback: types.CallbackQuery, category, **kwargs):
    await callback.message.answer('Ведите название для подкатегории')
    global category_info
    category_info = category
    await AddSubcategory.subcategory_name.set()



@dp.message_handler(IsAdmin(), state=AddSubcategory.subcategory_name)
async def category_name(message: types.Message, state: FSMContext, **kwargs):
    print(kwargs)
    answer = message.text
    category = category_info
    print(category_info)
    
    subcategories = product_db.distinct_subcategory_name(category)
    print(subcategories)
    category_name = product_db.get_distinct_category_name(category)
    # print(kwargs)

    # print(subcategories)
    subcategory_names = []
    for i in subcategories:
        print(i)
        subcategory_names.append(i[0].lower())

    if  answer.lower() in subcategory_names:
        await message.answer('Такая подкатегория уже существует')
        await state.finish()
    else:


        async with state.proxy() as data:
            data['subcategory_name'] = answer
            data['category_name'] = category_name[0][0]
            data['category_code'] = category

        await message.answer(f'Подтверждаете название {answer}\n(Да/Нет)')
        translator = Translator()
        result = translator.translate(message.text, )

        # await message.answer(f'Перевод {result.text}')
        async with state.proxy() as data:
            data['subcategory_code'] = result.text
        await AddSubcategory.choice.set()   

            

@dp.message_handler(IsAdmin(), state=AddSubcategory.choice)
async def catefory_choice(message: types.Message, state: FSMContext):

    answer = message.text

    data = await state.get_data()

    answer = message.text
    if answer.lower() == 'да':
        'Добавление категории'
        await message.answer(f'Добавление подкатегории {data["subcategory_name"]}')
        product_db.add_subcategory(data['category_name'], data['category_code'], data['subcategory_name'], data['subcategory_code'])
        await state.finish()

    elif answer.lower() == 'нет':
        await message.answer('Отмена добавлению')
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
    


    levels = {
        "0": list_categories,
        "1": add_subcategory,

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

