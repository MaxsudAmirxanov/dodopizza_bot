from unicodedata import category
from aiogram.utils.callback_data import CallbackData
from sqlalchemy import subquery
# from menu_keyboard import get_categories, count_item, get_subcategories, get_items
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def mailing_keyboard(category, subcategory, item_id, price, count, photo_id):
    print(f'3. {item_id} {count} {price}')

    sum = int(count) * int(price)
    # count = 1
    CURRENT_LEVEL = 3
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
       InlineKeyboardButton(text="Сообщение", callback_data='mailing'),
       InlineKeyboardButton(text="Фото", callback_data='mailing_photo'),
       InlineKeyboardButton(text="Сообщение + фото", callback_data='mailing+photo')
    )




    return markup