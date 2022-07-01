from unicodedata import category
from aiogram.utils.callback_data import CallbackData
from sqlalchemy import subquery
# from menu_keyboard import get_categories, count_item, get_subcategories, get_items
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.db_api.db_commands_2 import get_all_database, get_subcategories, get_items

menu_cd = CallbackData("show_menu", "level", "category", "subcategory", "item_id")
buy_item = CallbackData("buy", "item_id")

def make_callback_data(level, category='0', subcategory='0', item_id='0'):
    return menu_cd.new(level=level, category=category, subcategory=subcategory, item_id=item_id)

async def categories_keyboard():
    CURRENT_LEVEL = 0
    markup = InlineKeyboardMarkup(row_width=1)

    catrgories = get_all_database()
    print(catrgories)
    
    for category in catrgories:
        
        button_text = f"{category[0]}"
        callback_data = make_callback_data(level=CURRENT_LEVEL + 1, category=category[1])
        print(callback_data)

        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )
    return markup

async def subcategories_keyboard(category):

    CURRENT_LEVEL = 1
    markup = InlineKeyboardMarkup()

    subcategories = get_subcategories(category)
    print(subcategories)
    print(category)
    for subcategory in subcategories:

        button_text = f"{subcategory[0]}"
        callback_data = make_callback_data(level=CURRENT_LEVEL + 1, category=category,subcategory=subcategory[1])


        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )

    markup.row(
        InlineKeyboardButton(text='Назад', callback_data=make_callback_data(level=CURRENT_LEVEL - 1))
    )
    return markup

async def items_keyboard(category, subcategory):
    CURRENT_LEVEL = 2
    markup = InlineKeyboardMarkup(row_width=1)

    items = get_items(category, subcategory)
    print(f'3. {items}')
    for item in items:
        button_text = f"{item[5]} - {item[7]}р"
        callback_data = make_callback_data(level=CURRENT_LEVEL + 1, category=category, subcategory=subcategory, item_id=item[5])

        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )

    markup.row(
        InlineKeyboardButton(text='Назад', 
        callback_data=make_callback_data(level=CURRENT_LEVEL - 1, 
        category=category)
        )
    )
    return markup

def item_keyboard(category, subcategory, item_id):
    print(f'4. {item_id}')
    CURRENT_LEVEL = 3
    markup = InlineKeyboardMarkup()
    markup.add(
       InlineKeyboardButton(text="➕", callback_data='add'),
       InlineKeyboardButton(text="➖", callback_data='remove')
    )

    markup.row(
       InlineKeyboardButton(text="Купить", callback_data=buy_item.new(item_id=item_id))
    )

    markup.row(
        InlineKeyboardButton(text='Назад', 
        callback_data=make_callback_data(level=CURRENT_LEVEL - 1, 
        category=category, subcategory=subcategory)
        )
    )
    return markup

