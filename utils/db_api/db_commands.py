import psycopg2
from data.config import  PGUSER, PGPASSWORD, DATABASE
import asyncio
host = '127.0.0.1'

class Database():
    def __init__(self):
        self.host=host,
        self.user=PGUSER,
        self.password=PGPASSWORD,
        self.database = DATABASE
  
class Category(Database):
    pass

class Subcategory(Database):
    pass

class Product(Database):
    pass

class Cart(Database):
    pass

class Cart_product(Database):
    pass

class User(Database):
    pass

class Admin(Database):
    pass
