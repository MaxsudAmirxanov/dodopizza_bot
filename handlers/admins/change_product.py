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


class ChangeProduct(StatesGroup):
    # category_name = State()
    # cstegory_code = State()
    # subcategory_name = State()
    # subcatgory_code = State()
    item_id = State
    name = State()
    photo = State()
    price = State()





from keyboards.inline.change_product_keyboards import categories_keyboard, items_keyboard, subcategories_keyboard, item_keyboard, menu_cd

product_db = Product()
cart_db = Cart()
customer_db = Customer()

@dp.message_handler(IsAdmin(), commands='change_product')
async def show_menu(message: types.Message):
    await list_categories(message)

async def list_categories(message: Union[types.Message, types.CallbackGame], **kworgs):
    markup = await categories_keyboard()

    if isinstance(message, types.Message):
        # p_3 = open('photo_3.png', 'rb')
        await message.answer("Выберите категорию товара, которую хотите изменить", reply_markup=markup)
        

    elif isinstance(message, types.CallbackQuery):
        call = message
        await call.message.edit_reply_markup(markup)

async def list_subcategoies(callback: types.CallbackQuery, category, **kwargs):
    # print(f"1.1 {category}")
    markup = await subcategories_keyboard(category)
    await callback.message.edit_text("Выберите подкатегорию товара, которую хотите изменить",reply_markup= markup)

async def list_item(callback: types.CallbackQuery, category, subcategory, **kwargs):
    
    if kwargs["item_id"] != "0":
        # print('add')
        id = customer_db.find_customer_id(int(callback.from_user.id))
        print(f"-- {id}")
        # print(callback.from_user.id)
        cart_db.add_to_cart(user_id=id[0][0], product_id=kwargs["item_id"], count=kwargs["count"])
        

    print(f"1.2 {category} -- {kwargs}")
    print(kwargs)
    print(subcategory)
    markup = await items_keyboard(category=category, subcategory=subcategory)
    
    await callback.message.edit_text("Смотри что у нас есть", reply_markup=markup)
    # if kwargs['old_count'] == 'назад':
    #     await callback.message.delete_chat_photo(media=InputMediaPhoto(media=open('image.jpg', 'rb')))
#         message.edit_media(
#     media=InputMediaPhoto(
#         media=open('image.jpg', 'rb'),
#         caption='Title'
#     )
# )

async def show_item(callback: types.CallbackQuery, category, subcategory, item_id, **kwargs):
    item = product_db.customer_db(category, subcategory, item_id)
    print(f"1.3 {item}")

    markup = item_keyboard(category, subcategory, item_id, item[0][7])

    
    print(item)
    print('111--------------------')
    # text = f"{item[0][5]} - {item[0][7]}р"
    text = 'Выберите что хотите изменить'
    # await callback.message.edit_text(text, reply_markup=markup)

    # media = [types.InputMediaPhoto('data/photo/product.jpg')]  # Показываем, где фото и как её подписать
    # media.append(types.InputMediaPhoto('data/photo/product.jpg'))
    # 'AgACAgIAAxkBAAILNmLXCk8MgXBCVD8dhMvJ0-C0cKbVAAInwTEbecq5SpyUf8oj6tUhAQADAgADcwADKQQ'
    # video_bytes = InputFile(path_or_bytesio='data/photo/product.jpeg')
    
    # await callback.message.edit_media()
    # callback.message.edit_media()
    await callback.message.edit_text(text, reply_markup=markup)
    

# @dp.message_handler(text='🛒 Корзина')
# @dp.message_handler(state = '*')
async def edit_name(callback: types.CallbackQuery, item_id, **kwargs):
    # await callback.message.answer(f'{kwargs}')
    
    product = product_db.get_product(item_id)
    await callback.message.answer(f'Ведите новое название, для товара {product[0][5]}')
    # state= FSMContext(dp, callback.message.chat.id, )
    cur_state = dp.current_state()
    async with cur_state.proxy() as data:
        data['item_id'] = item_id
    await ChangeProduct.name.set()

@dp.message_handler(state=ChangeProduct.name)
async def name(message: types.Message, state: FSMContext, **kwargs):
    data = await state.get_data()
    item_id = data.get('item_id')

    await message.answer(f'{item_id}')
    product = product_db.get_product(item_id)
    new_name = message.text

    product_db.edit_product_name(item_id, new_name)
    await message.answer(f'Имя товара с {product[0][5]} переименовано на {new_name}')

    await state.finish()



async def edit_price(callback: types.CallbackQuery, item_id, **kwargs):
    # await callback.message.answer(f'{kwargs}')
    
    product = product_db.get_product(item_id)
    await callback.message.answer(f'Ведите новый ценик, для товара {product[0][5]}')
    # state= FSMContext(dp, callback.message.chat.id, )
    cur_state = dp.current_state()
    async with cur_state.proxy() as data:
        data['item_id'] = item_id
    await ChangeProduct.price.set()

@dp.message_handler(state=ChangeProduct.price)
async def price(message: types.Message, state: FSMContext, **kwargs):
    data = await state.get_data()
    item_id = data.get('item_id')

    await message.answer(f'{item_id}')
    product = product_db.get_product(item_id)
    new_price = message.text

    product_db.edit_product_price(item_id, new_price)
    await message.answer(f'Цена товара с {product[0][7]} изменино на {new_price}')

    await state.finish()
    


async def edit_photo(callback: types.CallbackQuery, item_id, **kwargs):
    # await callback.message.answer(f'{kwargs}')
    
    product = product_db.get_product(item_id)
    await callback.message.answer(
        f'Отправть новую фотографию, для товара {product[0][5]}'
        )
    # state= FSMContext(dp, callback.message.chat.id, )
    cur_state = dp.current_state()
    async with cur_state.proxy() as data:
        data['item_id'] = item_id
    await ChangeProduct.photo.set()

@dp.message_handler(state=ChangeProduct.photo, content_types=types.ContentTypes.PHOTO)
async def photo(message: types.Message, state: FSMContext, **kwargs):

    data = await state.get_data()
    item_id = data.get('item_id')
    

    product = product_db.get_product(item_id)
    new_price = message.text

    product_db.edit_product_photo(item_id, f'{message.photo[0].file_id}')
    await message.answer(f'Фотография товара изменина')

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
        "1": list_subcategoies,
        "2": list_item,
        "3": show_item,
        "4": edit_name,
        '5': edit_price,
        '6': edit_photo


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

