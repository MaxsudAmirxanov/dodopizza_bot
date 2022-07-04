from itertools import count
from aiogram.dispatcher.filters import Command
from aiogram import types
from loader import bot

import logging
from typing import Union
from loader import dp
from utils.db_api.db_commands_2 import get_item, add_to_cart, read_user_id, get_cart, find_user_id, get_product, rm_cart_product, get_cart_product

from keyboards.inline.menu_keyboards import categories_keyboard, items_keyboard, subcategories_keyboard, item_keyboard, menu_cd, buy_keyboard, edit_cart_keyboard

@dp.message_handler(text="🍴 Меню")
async def show_menu(message: types.Message):
    await list_categories(message)

async def list_categories(message: Union[types.Message, types.CallbackGame], **kworgs):
    markup = await categories_keyboard()

    if isinstance(message, types.Message):
        await message.answer("Смотри што у нас есть", reply_markup=markup)
        

    elif isinstance(message, types.CallbackQuery):
        call = message
        await call.message.edit_reply_markup(markup)

async def list_subcategoies(callback: types.CallbackQuery, category, **kwargs):
    print(f"1.1 {category}")
    markup = await subcategories_keyboard(category)
    await callback.message.edit_reply_markup(markup)

async def list_item(callback: types.CallbackQuery, category, subcategory, **kwargs):
    
    if kwargs["item_id"] != "0":
        print('add')
        id = find_user_id(int(callback.from_user.id))
        print(f"-- {id}")
        # print(callback.from_user.id)
        add_to_cart(user_id=id[0][0], product_id=kwargs["item_id"], count=kwargs["count"])
        

    print(f"1.2 {category}")
    print(kwargs)
    print(subcategory)
    markup = await items_keyboard(category=category, subcategory=subcategory)

    await callback.message.edit_text("Смотри что у нас есть", reply_markup=markup)

async def show_item(callback: types.CallbackQuery, category, subcategory, item_id, count, **kwargs):
    item = get_item(category, subcategory, item_id)
    print(f"1.3 {item}")
    markup = item_keyboard(category, subcategory, item_id, item[0][7], count)

    
    print(item)
    print('111--------------------')
    text = f"{item[0][5]} - {item[0][7]}р"
    await callback.message.edit_text(text, reply_markup=markup)

@dp.message_handler(text='🛒 Корзина')
async def show_carts(callback: Union[types.CallbackQuery, types.Message], **kwargs):
    # count = callback_data.get('count')

    id = find_user_id(int(callback.from_user.id))
    cart = get_cart(id[0][0])
    print(cart)
    # print(callback)
    logging.info(f'{cart}')

    number = 0
    sum_price = 0
    for i in cart:
        number += 1
        product = get_product(i[2])
        sum = int(i[3])*int(product[0][7])
        markup = buy_keyboard(item_id=i[0], cart_product_id=i[0], count=i[3], number_cart=number)

        sum_price += sum
        
        print(product)
        await bot.send_message(callback.from_user.id, f"{number}. {product[0][5]} - {i[3]}шт - {sum}p", reply_markup=markup)

    await bot.send_message(callback.from_user.id, f"Ваш заказ на {sum_price}p")

    await bot.send_message(callback.from_user.id, 'Корзина, тадааам')
    print(callback.from_user.id)

async def edit_cart(callback: types.CallbackQuery, category, subcategory, item_id, count, cart_product_id, number_cart):
    product = get_product(item_id)
    print(11111111111111111111111)
    print(cart_product_id)
    print(item_id)
    print(product)
    sum = int(count) * int(product[0][7])
    await callback.message.edit_text(f"{product[0][5]} - {product[0][7]}\n\n{count} шт - {sum}p", reply_markup=edit_cart_keyboard(cart_product_id, item_id, count, number_cart))

async def rm_cart(callback: types.CallbackQuery, category, subcategory, item_id, count):
    # get_item(category_code=category, subcategory_code=subcategory, item_id=item_id)
    user_id = find_user_id(callback.from_user.id)
    print(user_id[0][0])
    print(count)
    print(item_id)
    rm_cart_product(int(item_id), int(user_id[0][0]))

    await callback.message.edit_text("Продукт удален")


async def show_cart(callback: types.CallbackQuery, category, subcategory, item_id, count, number_cart):
    print(item_id)

    # await callback.message.edit_text(f"{number_cart}. {product[0][5]} - {i[3]}шт - {sum}p", reply_markup=markup)



@dp.callback_query_handler(menu_cd.filter())
async def navigate(call: types.CallbackQuery, callback_data: dict):
    current_level = callback_data.get('level')
    category = callback_data.get('category')
    subcategory = callback_data.get('subcategory')
    item_id = callback_data.get('item_id')
    count = callback_data.get('count')
    cart_product_id = callback_data.get('cart_product_id')
    number_cart = callback_data.get('number_cart')
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
        number_cart=number_cart
    )

