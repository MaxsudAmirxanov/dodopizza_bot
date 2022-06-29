from aiogram.dispatcher.filters import Command
from aiogram import types

from typing import Union
from loader import dp
from utils.db_api.db_commands_2 import get_item

from keyboards.inline.menu_keyboards import categories_keyboard, items_keyboard, subcategories_keyboard, item_keyboard, menu_cd

@dp.message_handler(Command('menu'))
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
    markup = await subcategories_keyboard(category)
    await callback.message.edit_reply_markup(markup)

async def list_item(callback: types.CallbackQuery, category, subcategory, **kwargs):
    markup = await items_keyboard(category=category, subcategory=subcategory)
    await callback.message.edit_text("Смотри что у нас есть", reply_markup=markup)

async def show_item(callback: types.CallbackQuery, category, subcategory, item_id):
    markup = item_keyboard(category, subcategory, item_id)

    item = get_item(category, subcategory, item_id)
    print(item)
    print('111--------------------')
    text = f"Купи {item[0][5]} - {item[0][7]}"
    await callback.message.edit_text(text, reply_markup=markup)


@dp.callback_query_handler(menu_cd.filter())
async def navigate(call: types.CallbackQuery, callback_data: dict):
    current_level = callback_data.get('level')
    category = callback_data.get('category')
    subcategory = callback_data.get('subcategory')
    item_id = callback_data.get('item_id')
    print(f'5. {callback_data}')

    levels = {
        "0": list_categories,
        "1": list_subcategoies,
        "2": list_item,
        "3": show_item
    }

    curremt_level_function = levels[current_level]

    await curremt_level_function(
        call, 
        category=category, 
        subcategory=subcategory, 
        item_id=item_id
    )

