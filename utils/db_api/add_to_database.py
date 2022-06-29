
# from utils.db_api.db_commands import add_item
# from utils.db_api.database import create_db
# import asyncio

# async def add_items():
#     await add_item(
#         name='Сырная 🌱', 
#         category_name='Пицца', category_code='pizza', 
#         subcategory_name='Вегансикие', subcategory_code='vegan',
#         price='299', photo='-')
#     await add_item(
#         name='Овощи и грибы 🌱', 
#         category_name='Пицца', category_code='pizza', 
#         subcategory_name='Вегансикие', subcategory_code='vegan',
#         price='439', photo='-')
#     await add_item(
#         name='Маргарита 🌱', 
#         category_name='Пицца', category_code='pizza', 
#         subcategory_name='Вегансикие', subcategory_code='vegan',
#         price='389', photo='-')
#     await add_item(
#         name='Четыре сыра 🌱', 
#         category_name='Пицца', category_code='pizza', 
#         subcategory_name='Вегансикие', subcategory_code='vegan',
#         price='489', photo='-')
        

#     await add_item(
#         name='Чоризо фреш 🌶️', 
#         category_name='Пицца', category_code='pizza', 
#         subcategory_name='Остррое', subcategory_code='Sharp',
#         price='299', photo='-')
#     await add_item(
#         name='Диабло 🌶️🌶️', 
#         category_name='Пицца', category_code='pizza', 
#         subcategory_name='Остррое', subcategory_code='Sharp',
#         price='489', photo='-')


#     await add_item(
#         name='Ветчина и сыр', 
#         category_name='Пицца', category_code='pizza', 
#         subcategory_name='Классическое', subcategory_code='Klassik',
#         price='329', photo='-')
#     await add_item(
#         name='Песто', 
#         category_name='Пицца', category_code='pizza', 
#         subcategory_name='Классическое', subcategory_code='Klassik',
#         price='489', photo='-')
#     await add_item(
#         name='Пепперони фреш', 
#         category_name='Пицца', category_code='pizza', 
#         subcategory_name='Классическое', subcategory_code='Klassik',
#         price='290', photo='-')
#     await add_item(
#         name='Ветчина и грибы', 
#         category_name='Пицца', category_code='pizza', 
#         subcategory_name='Классическое', subcategory_code='Klassik',
#         price='389', photo='-')


#     await add_item(
#         name='Грибной Стартер 🌱', 
#         category_name='Закуски', category_code='Snacks', 
#         subcategory_name='Стартер', subcategory_code='Starter',
#         price='169', photo='-')
#     await add_item(
#         name='Сырный Стартер', 
#         category_name='Закуски', category_code='Snacks', 
#         subcategory_name='Стартер', subcategory_code='Starter',
#         price='169', photo='-')
#     await add_item(
#         name='Острый Стартер 🌶️🌶️', 
#         category_name='Закуски', category_code='Snacks', 
#         subcategory_name='Стартер', subcategory_code='Starter',
#         price='169', photo='-')
#     await add_item(
#         name='Додстер Песто', 
#         category_name='Закуски', category_code='Snacks', 
#         subcategory_name='Додстер', subcategory_code='Dodster',
#         price='189', photo='-')
#     await add_item(
#         name='Острый Додстер 🌶️🌶️', 
#         category_name='Закуски', category_code='Snacks', 
#         subcategory_name='Додстер', subcategory_code='Dodster',
#         price='169', photo='-')
#     await add_item(
#         name='Додстер', 
#         category_name='Закуски', category_code='Snacks', 
#         subcategory_name='Додстер', subcategory_code='Dodster',
#         price='169', photo='-')


# loop = asyncio.get_event_loop()
# loop.run_until_complete(create_db())
# loop.run_until_complete(add_items())