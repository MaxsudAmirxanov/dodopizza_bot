from itertools import count
from aiogram.dispatcher.filters import Command
from aiogram import types
from loader import bot
from aiogram.types import InputFile, InputMedia

import logging
from typing import Union
from loader import dp, bot
from utils.db_api.db_commands_2 import edit_cart_product, get_item, add_to_cart, read_user_id, get_cart, find_user_id, get_product, rm_cart_product, get_cart_product
from utils.db_api.database import Cart, Product, Customer
from keyboards.inline.menu_keyboards import categories_keyboard, items_keyboard, subcategories_keyboard, item_keyboard, menu_cd, buy_keyboard, edit_cart_keyboard
import pprint

product_db = Product()
cart_db = Cart()
customer_db = Customer()


@dp.message_handler(text="🍴 Меню")
async def show_menu(message: types.Message):
    await list_categories(message)

async def list_categories(message: Union[types.Message, types.CallbackGame], **kworgs):
    

    if isinstance(message, types.Message):
        # p_3 = open('photo_3.png', 'rb')
        photo_id = await message.answer_photo('AgACAgIAAxkBAAILf2LXKDX7jzyoZGVf91Uvxy0JJpFxAAJ2wTEbecq5SvyOOOmNIiHlAQADAgADcwADKQQ')
        # message.edit_media()
        
        print(photo_id)
        markup = await categories_keyboard(photo_id.message_id)
        await message.answer("Смотри што у нас есть", reply_markup=markup)
        

    elif isinstance(message, types.CallbackQuery):
        call = message
        markup = await categories_keyboard(kworgs['photo_id'])
        await call.message.edit_reply_markup(markup)

async def list_subcategoies(callback: types.CallbackQuery, category, photo_id, **kwargs):
    print(f"1.1 {category}")
    markup = await subcategories_keyboard(category, photo_id=photo_id)
    await callback.message.edit_reply_markup(markup)

async def list_item(callback: types.CallbackQuery, category, subcategory, photo_id, **kwargs):
    
    if kwargs["item_id"] != "0":
        print('add')
        id = customer_db.find_customer_id(int(callback.from_user.id))
        print(f"-- {id}")
        # print(callback.from_user.id)
        cart_db.add_to_cart(user_id=id[0][0], product_id=kwargs["item_id"], count=kwargs["count"])
        

    print(f"1.2 {category} -- {kwargs}")
    print(kwargs)
    print(subcategory)
    markup = await items_keyboard(category=category, subcategory=subcategory, photo_id=photo_id)
    
    # await callback.message.edit_media()
    await callback.message.edit_text("Смотри что у нас есть", reply_markup=markup)

    if kwargs['old_count'] == 'назад':
        media = types.InputMediaPhoto('AgACAgIAAxkBAAIMZGLbJorwvcGrkpbbiWfZMwFpWRFqAAL2uzEbMjzYSsBzk9Y5bbe_AQADAgADcwADKQQ')
        await bot.edit_message_media(media=media, chat_id=callback.message.chat.id, message_id=photo_id)


async def show_item(callback: types.CallbackQuery, category, subcategory, item_id, count, photo_id, old_count, **kwargs):
    item = product_db.customer_db(category, subcategory, item_id)
    print(f"1.3 {item}------- {callback} -- {kwargs} -- {old_count}")
    markup = item_keyboard(category, subcategory, item_id, item[0][7], count, photo_id=photo_id)

    
    print(item)
    print('111--------------------')
    text = f"{item[0][5]} - {item[0][7]}р"
    # await callback.message.edit_text(text, reply_markup=markup)

      # Показываем, где фото и как её подписать
    # media.append(types.InputMediaPhoto('data/photo/product.jpg'))
    'AgACAgIAAxkBAAILNmLXCk8MgXBCVD8dhMvJ0-C0cKbVAAInwTEbecq5SpyUf8oj6tUhAQADAgADcwADKQQ'
    video_bytes = InputFile(path_or_bytesio='data/photo/product.jpg')
    
    
    print(f'1112 -- {callback.message.chat.id} {photo_id}')

    product_photo = product_db.get_product_photo(item_id)
    print(product_photo)
    media = types.InputMediaPhoto(product_photo[0][0])
    if old_count != '+':    
        await bot.edit_message_media(media=media, chat_id=callback.message.chat.id, message_id=photo_id)
    await callback.message.edit_text(text, reply_markup=markup)
    

@dp.message_handler(text='🛒 Корзина')
async def show_carts(callback: Union[types.CallbackQuery, types.Message], **kwargs):
    # count = callback_data.get('count')

    id = customer_db.find_customer_id(int(callback.from_user.id))
    cart = cart_db.get_cart(id[0][0])
    print(cart)
    # print(callback)
    logging.info(f'{cart}')

    number = 0
    sum_price = 0
    for i in cart:
        print('000000')
        print(i)

        number += 1
        product = product_db.get_product(i[2])
        sum = int(i[3])*int(product[0][7])
        markup = buy_keyboard(item_id=i[2], cart_product_id=i[0], count=i[3], number_cart=number)

        sum_price += sum
        
        print(product)
        await bot.send_message(callback.from_user.id, f"{number}. {product[0][5]} - {i[3]}шт - {sum}p", reply_markup=markup)
    
    h = await bot.send_message(callback.from_user.id, f"Ваш заказ на {sum_price}p")
    # print(h)
    global variable_for_show_cart
    variable_for_show_cart = [h, sum_price]
    print(variable_for_show_cart)
    
    # await bot.send_message(callback.from_user.id, f"{callback.message_id}")
    # print(callback.message_id)

    await bot.send_message(callback.from_user.id, 'Корзина, тадааам')
    print(callback.from_user.id)

async def edit_cart(callback: types.CallbackQuery, category, subcategory, item_id, count, cart_product_id, number_cart, **kwargs):
    product = product_db.get_product(item_id)
    print(11111111111111111111111)
    print(cart_product_id)
    print(item_id)
    print(product)
    sum = int(count) * int(product[0][7])
    await callback.message.edit_text(f"{product[0][5]} - {product[0][7]}\n\n{count} шт - {sum}p", reply_markup=edit_cart_keyboard(cart_product_id, item_id, count, number_cart))

async def rm_cart(callback: types.CallbackQuery, category, subcategory, item_id, count, **kwargs):
    # get_item(category_code=category, subcategory_code=subcategory, item_id=item_id)
    user_id = customer_db.find_customer_id(callback.from_user.id)
    print('Удаление продукта')
    print(user_id[0][0])
    print(count)
    print(item_id)
    i = cart_db.rm_cart_product(int(item_id), int(user_id[0][0]))
    # await callback.message.edit_text(f"Ваш заказ на {variable_for_show_cart[1]}p")

    id = customer_db.find_customer_id(int(callback.from_user.id))
    cart = cart_db.get_cart(id[0][0])

    sum_price = 0
    for i in cart:
        product = product_db.get_product(i[2])
        sum = int(i[3])*int(product[0][7])
        

        sum_price += sum
    await bot.edit_message_text(f"Ваш заказ на {sum_price}p", variable_for_show_cart[0].chat.id, variable_for_show_cart[0].message_id )
    print(i)
    await callback.message.edit_text("Продукт удален")


async def show_cart(callback: types.CallbackQuery, category, subcategory, item_id, count, number_cart, cart_product_id, old_count, **kwargs):
    print(item_id, cart_product_id)
    print(3333333333333333)
    print(variable_for_show_cart[0].message_id)

    product = product_db.get_product(item_id)
    old_product_sum = int(old_count)*int(product[0][7])
    new_product_sum = int(count)*int(product[0][7])

    sum_price = int(variable_for_show_cart[1]) - int(old_product_sum) + int(new_product_sum) 
    print(f" variable_for_show_cart  --  {int(variable_for_show_cart[1])}")
    print(f" old_product_sum  --  {int(old_product_sum)}") 
    print(f" new_product_sum  --  {int(new_product_sum)}")
    print(f" old_count  --  {int(old_count)}")
    print(f" count  --  {int(count)}")


    markup = buy_keyboard(item_id, cart_product_id, count, number_cart)

    await callback.message.edit_text(f"{number_cart}. {product[0][5]} - {count}шт - {new_product_sum}p", reply_markup=markup)
    await bot.edit_message_text(f"Ваш заказ на {sum_price}p", variable_for_show_cart[0].chat.id, variable_for_show_cart[0].message_id )
    cart_db.edit_cart_product(cart_product_id, count)
    # await bot.edit_message_text()



@dp.callback_query_handler(menu_cd.filter())
async def navigate(call: types.CallbackQuery, callback_data: dict):
    current_level = callback_data.get('level')
    category = callback_data.get('category')
    subcategory = callback_data.get('subcategory')
    item_id = callback_data.get('item_id')
    count = callback_data.get('count')
    cart_product_id = callback_data.get('cart_product_id')
    number_cart = callback_data.get('number_cart')
    old_count = callback_data.get("old_count")
    photo_id = callback_data.get('photo_id')
    print(f'5. {callback_data}')


    levels = {
        "0": list_categories,
        "1": list_subcategoies,
        "2": list_item,
        "3": show_item,
        "4": show_carts,
        "5": edit_cart,
        "6": rm_cart,
        "7": show_cart

    }

    curremt_level_function = levels[current_level]

    await curremt_level_function(
        call, 
        category=category, 
        subcategory=subcategory, 
        item_id=item_id,
        count=count,
        cart_product_id=cart_product_id,
        number_cart=number_cart,
        old_count=old_count,
        photo_id=photo_id
    )

