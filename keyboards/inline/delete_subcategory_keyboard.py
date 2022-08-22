from unicodedata import category
from aiogram.utils.callback_data import CallbackData
from sqlalchemy import subquery
# from menu_keyboard import get_categories, count_item, get_subcategories, get_items
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.db_api.db_commands_2 import get_all_database, get_subcategories, get_items, get_cart_product
from utils.db_api.database import Product, Cart, Customer


menu_cd = CallbackData("delete_subcategory", "level", "category", "subcategory", "item_id", "name", "photo", "price")
buy_item = CallbackData("buy", "item_id")

product_db = Product()
cart_db = Cart()
customer_db = Customer()

def make_callback_data_add(level, category='0', subcategory='0', item_id='0', name='0', photo='0', price='0'):
    return menu_cd.new(level=level, category=category, subcategory=subcategory, item_id=item_id, name=name, photo=photo, price=price)

# def make_callback_buy_item(buy, item_id, count):
#     return buy_item.new(buy=buy, item_id='0', count=1 )


async def categories_keyboard():
    CURRENT_LEVEL = 0
    markup = InlineKeyboardMarkup(row_width=1)

    catrgories = product_db.get_category_name_distinct()
    
    
    for category in catrgories:
        
        button_text = f"{category[0]}"
        callback_data = make_callback_data_add(level=CURRENT_LEVEL + 1, category=category[1])
        # print(f'0. {callback_data}')

        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )
    return markup


async def subcategories_keyboard(category):

    CURRENT_LEVEL = 1
    markup = InlineKeyboardMarkup()

    subcategories = product_db.get_subcategory_name(category)
    # print(f'1. {subcategories}')
    print(category)
    for subcategory in subcategories:
        if subcategory[0] == '-':
            continue

        button_text = f"{subcategory[0]}"
        callback_data = make_callback_data_add(level=CURRENT_LEVEL + 1, category=category,subcategory=subcategory[1])
        print(callback_data)


        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )

    markup.row(
        InlineKeyboardButton(text='Назад', callback_data=make_callback_data_add(level=CURRENT_LEVEL - 1))
    )
    return markup

