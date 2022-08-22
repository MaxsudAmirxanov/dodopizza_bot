
from aiogram.utils.callback_data import CallbackData

# from menu_keyboard import get_categories, count_item, get_subcategories, get_items
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.db_api.db_commands_2 import get_all_database, get_subcategories, get_items, get_cart_product
from utils.db_api.database import Product, Cart, Customer


menu_cd = CallbackData("show_menu", "level", "category", "subcategory", "item_id", "count", "cart_product_id", "number_cart", "old_count", 'photo_id')
buy_item = CallbackData("buy", "item_id")

product = Product()
cart = Cart()
customer = Customer()

def make_callback_data(level, category='0', subcategory='0', item_id='0', count=1, cart_product_id='0', number_cart='0', old_count='0', photo_id='0'):
    return menu_cd.new(level=level, category=category, subcategory=subcategory, item_id=item_id, count=count, cart_product_id=cart_product_id, number_cart=number_cart, old_count=old_count, photo_id=photo_id)

# def make_callback_buy_item(buy, item_id, count):
#     return buy_item.new(buy=buy, item_id='0', count=1 )


async def categories_keyboard(photo_id):
    CURRENT_LEVEL = 0
    markup = InlineKeyboardMarkup(row_width=1)

    catrgories = product.get_category_name_distinct()
    print(catrgories)
    
    for category in catrgories:
        print(f'54321 {category[1]}')
        button_text = f"{category[0]}"
        callback_data = make_callback_data(level=CURRENT_LEVEL + 1, category=category[1], photo_id=photo_id)
        print(f'0. {callback_data}')

        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )
    return markup


async def subcategories_keyboard(category, photo_id):

    CURRENT_LEVEL = 1
    markup = InlineKeyboardMarkup()

    subcategories = product.get_subcategory_name(category)
    print(f'1. {subcategories}')
    print(category)
    for subcategory in subcategories:
        print(subcategory)
        if subcategory[0] == '-':
            continue
        button_text = f"{subcategory[0]}"
        print(f'button {button_text}')
        callback_data = make_callback_data(level=CURRENT_LEVEL + 1, category=category,subcategory=subcategory[1], photo_id=photo_id)
        print(callback_data)


        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )

    markup.row(
        InlineKeyboardButton(text='Назад', callback_data=make_callback_data(level=CURRENT_LEVEL - 1, photo_id=photo_id))
    )
    return markup

async def items_keyboard(category, subcategory, photo_id):
    CURRENT_LEVEL = 2
    markup = InlineKeyboardMarkup(row_width=1)

    items = product.get_products(category, subcategory)
    print(f'2. {items}')
    for item in items:
        if item[5] == '-':
            continue
        button_text = f"{item[5]} - {item[7]}р"
        callback_data = make_callback_data(level=CURRENT_LEVEL + 1, category=category, subcategory=subcategory, item_id=item[0], photo_id=photo_id)

        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )

    markup.row(
        InlineKeyboardButton(text='Назад', 
        callback_data=make_callback_data(level=CURRENT_LEVEL - 1, 
        category=category, photo_id=photo_id)
        )
    )
    return markup

def item_keyboard(category, subcategory, item_id, price, count, photo_id):
    print(f'3. {item_id} {count} {price}')

    sum = int(count) * int(price)
    # count = 1
    CURRENT_LEVEL = 3
    markup = InlineKeyboardMarkup()
    markup.add(
       InlineKeyboardButton(text="➕", callback_data=make_callback_data(level=CURRENT_LEVEL, category=category, subcategory=subcategory, item_id=item_id, count=int(count) + 1, photo_id=photo_id, old_count='+')),
       InlineKeyboardButton(text="➖", callback_data=make_callback_data(level=CURRENT_LEVEL, category=category, subcategory=subcategory, item_id=item_id, count=int(count) - 1, photo_id=photo_id, old_count='+'))
    )

    markup.row(
       InlineKeyboardButton(text=f"✅ Добавить {count}шт - {sum}р", callback_data=make_callback_data(level=CURRENT_LEVEL -1, category=category, subcategory=subcategory, item_id=item_id, count=int(count), photo_id=photo_id, old_count='назад'))
    )

    markup.row(
        InlineKeyboardButton(text='Назад', 
        callback_data=make_callback_data(level=CURRENT_LEVEL - 1, 
        category=category, subcategory=subcategory, old_count='назад', photo_id=photo_id)
        ),
        InlineKeyboardButton(text="Корзина", callback_data=make_callback_data(level=CURRENT_LEVEL +1, category=category, subcategory=subcategory, item_id=item_id, count=int(count), photo_id=photo_id))
    )
    return markup

def buy_keyboard(item_id, cart_product_id, count, number_cart):
    print(item_id)
    print(2222222)
    CURRENT_LEVEL = 4
    markup = InlineKeyboardMarkup()
    markup.add(
       InlineKeyboardButton(text="Удалить", callback_data=make_callback_data(level=CURRENT_LEVEL + 2, cart_product_id=cart_product_id, item_id=item_id)),
       InlineKeyboardButton(text="Изменить", callback_data=make_callback_data(level=CURRENT_LEVEL + 1, cart_product_id=cart_product_id, item_id=item_id,count=count, number_cart=number_cart))
    )

    return markup


def edit_cart_keyboard(cart_product_id, item_id, count, number_cart):

    CURRENT_LEVEL = 5
    print(cart_product_id)
    product = cart.get_cart_product(cart_product_id)
    print(f"_____________ {product}   {cart_product_id} {number_cart}")
    # count = product[0][3]
    print(count)
    # print(old_count)
    markup = InlineKeyboardMarkup()
    markup.add(
       InlineKeyboardButton(text="➕", callback_data=make_callback_data(level=CURRENT_LEVEL, cart_product_id=cart_product_id, item_id=item_id, count=int(count)+1, number_cart=number_cart, old_count=product[0][3])),
       InlineKeyboardButton(text="➖", callback_data=make_callback_data(level=CURRENT_LEVEL, cart_product_id=cart_product_id, item_id=item_id, count=int(count)-1, number_cart=number_cart, old_count=product[0][3]))
    )

    markup.row(
        InlineKeyboardButton(text='Отмена', callback_data=make_callback_data(level=CURRENT_LEVEL +2, cart_product_id=cart_product_id, item_id=item_id, count=count, number_cart=number_cart, old_count=product[0][3])),
        InlineKeyboardButton(text='Сохранить', callback_data=make_callback_data(level=CURRENT_LEVEL +2, cart_product_id=cart_product_id, item_id=item_id, count=count, number_cart=number_cart, old_count=product[0][3]))
    )
    return markup