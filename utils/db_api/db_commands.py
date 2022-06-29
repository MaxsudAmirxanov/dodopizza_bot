# from operator import and_, imod
# from utils.db_api.database import db
# from sqlalchemy import and_
# from utils.db_api.models import Item
# from typing import List


# async def add_item(**kworgs):
#     newitem = await Item(**kworgs).create()
#     return newitem

# async def get_categories() -> List[Item]:
#     return await Item.query.distinct(Item.category_code).gino.all()

# async def get_subcategories(category) -> List[Item]:
#     return await Item.query.distinct(Item.subcategory_code).where(Item.category_code == category).gino.all()

# async def count_item(catrgory_code, subcatrgory_code = None):
#     conditions = [Item.category_code == catrgory_code]

#     if subcatrgory_code:
#         conditions.append(Item.subcategory_code == subcatrgory_code)

#     total = await db.select([db.func.count()]).where(
#         and_(*conditions)
#     ).gino.scaler()
#     return total

# async def get_items(catrgory_code, subcatrgory_code) -> List[Item]:
#     items = await Item.query.where(
#         and_(Item.category_code == catrgory_code,
#         Item.subcategory_code == subcatrgory_code)
#     ).gino.all()
#     return items

# async def get_item(item_id) -> Item:
#     item = await Item.query.where(Item.id == item_id).gino.first()
#     return item

# print(get_categories())
