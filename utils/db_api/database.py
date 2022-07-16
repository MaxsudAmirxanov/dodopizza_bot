import sqlite3


class Database():
    def __init__(self):
        self.con = sqlite3.connect("database.db")
        self.cur = self.con.cursor()
        

class Product(Database):
    def get_category_name_distinct(self):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute('select distinct product.category_name, product.category_code from product;')

                self.con.commit()
                return cursore.fetchall()
        except Exception as _ex:
            print(f'[SQLite] {_ex}')
                


    def get_category_name(self):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute('select product.category_name from product;')

                self.con.commit()
                return cursore.fetchall()
        except Exception as _ex:
            print(f'[SQLite] {_ex}')
    
    def get_subcategory_name(self, category_code):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute("select distinct product.subcategory_name, product.subcategory_code from product where product.category_code=?;", ((category_code,)))

                self.con.commit()
                return cursore.fetchall()
        except Exception as _ex:
            print(f'[SQLite] {_ex}')

    def get_products(self, category_code, subcategory_code):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute("select * from product where subcategory_code=? and category_code=?; ", (subcategory_code, category_code))

                self.con.commit()
                return cursore.fetchall() 
        except Exception as _ex:
            print(f'[SQLite] {_ex}')

    def customer_db(self, category_code, subcategory_code, item_id):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute("select * from product where product.category_code=? and product.subcategory_code=? and product.id=?; ", (category_code, subcategory_code, item_id))

                self.con.commit()
                return cursore.fetchall()
        except Exception as _ex:
            print(f'[SQLite] {_ex}')


    def add_product(self, name, category_code, category_name, subcategory_code, subcategory_name, photo, price):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute("insert into product (category_code, category_name, subcategory_code, subcategory_name, name, photo, price) values (?, ?, ?, ?, ?, ?, ?);", (category_code, category_name, subcategory_code, subcategory_name, name, photo, price))
                
                self.con.commit()
                return cursore.fetchall()
        except Exception as _ex:
            print(f'[SQLite] {_ex}')

    def get_product(self, id):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute("select * from product where id=?;", (str(id),))

                self.con.commit()
                return cursore.fetchall()
        except Exception as _ex:
            print(f'[SQLite] {_ex}')
class Cart(Database):
    def add_to_cart(self, user_id, product_id, count):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute("insert into cart (user_id, product_id, product_count) values (?, ?, ?)", (user_id, product_id, count))

                self.con.commit()
                return cursore.fetchall()
                "returning"
        except Exception as _ex:
            print(f'[SQLite] {_ex}')

    def get_cart(self, user_id):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute("select * from cart where user_id=?;", (str(user_id),))

                self.con.commit()
                return cursore.fetchall()  
        except Exception as _ex:
            print(f'[SQLite] {_ex}')

    def rm_cart_product(self, product_id, user_id):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute("delete from cart where user_id=? and id=?;", (user_id, product_id))

                self.con.commit()
                return cursore.fetchall()
        except Exception as _ex:
            print(f'[SQLite] {_ex}')

    def get_cart_product(self, cart_id):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute("select * from cart where id=?;", (str(cart_id),))

                self.con.commit()
                return cursore.fetchall()
        except Exception as _ex:
            print(f'[SQLite] {_ex}')

    def edit_cart_product(self, cart_id, count):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute("update cart set product_count=? where id=?;", (count, str(cart_id),))

                self.con.commit()
                return cursore.fetchall()
        except Exception as _ex:
            print(f'[SQLite] {_ex}')
class Customer(Database):   
    def delete_customer(self, id):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute('delete from customer where id=?;', (id))

                self.con.commit()
                return cursore.fetchall()
                "returning"
        except Exception as _ex:
            print(f'[SQLite] {_ex}')
    def add_customer(self, name, last_name, user_name, user_id):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute("insert into customer (name, last_name, user_name, user_id) values (?, ?, ?, ?);", (name, last_name, user_name, user_id))

                self.con.commit()
                return cursore.fetchall()
                "returning"
        except Exception as _ex:
            print(f'[SQLite] {_ex}')

    def read_customer_id(self):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute("select user_id from customer;")

                self.con.commit()
                return cursore.fetchall()
        except Exception as _ex:
            print(f'[SQLite] {_ex}')
    
    def find_customer_id(self, id):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute("select id from customer as c where user_id=?;", (str(id),))

                self.con.commit()
                return cursore.fetchall()
        except Exception as _ex:
            print(f'[SQLite] {_ex}')
class Referrer(Database):
    def add_referrer(self, user_id, id):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute("insert into referrer (user_telegram_id, customer_id) values (?, ?);", (user_id, id))

                self.con.commit()
                return cursore.fetchall() 
                "returning"
        except Exception as _ex:
            print(f'[SQLite] {_ex}')
    
    def get_referrers_user_id(self):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute("select user_telegram_id from referrer;" )

                self.con.commit()
                return cursore.fetchall()
        except Exception as _ex:
            print(f'[SQLite] {_ex}')
                
    def get_referrer_id(self, user_id):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute('select id from referrer as r where r.user_telegram_id=?;', (user_id,))

                self.con.commit()
                return cursore.fetchall()
        except Exception as _ex:
            print(f'[SQLite] {_ex}')
class Referral(Database):
    def add_referral(self, referrer_id, refferal_telegram_id):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute('insert into referral(referrer_id, referral_telegram_id) values (?, ?) returning referral;', (referrer_id, refferal_telegram_id))

                self.con.commit()
                return cursore.fetchall()
        except Exception as _ex:
            print(f'[SQLite] {_ex}')
class Admin(Database):
    def bloced_customer():
        pass
    
    # def chek_admin(self):
    #     try:
    #         #connect to exist database
    #         connection = psycopg2.connect(
    #             host=self.host[0],
    #             user=self.user[0],
    #             password=self.password[0],
    #             database=self.database
    #         )
    #         connection.autocommit = True

    #         with connection.cursor() as cursor:
    #             cursor.execute(
    #                 'insert into referral(referrer_id, referral_telegram_id) values (?, ?) returning referral;', (referrer_id, refferal_telegram_id)

    #             )
    #             # print(cursor.fetchall())
    #             # print(1)
                
    #             return cursor.fetchall()
            
                
    #     except Exception as _ex:
    #         # pass
    #         print('[INFO] Error while working with PostgreSQL', _ex)

    #     finally:
    #         if connection:
    #             connection.close()
    #             print('[INFO] PostgreSQL connection closed') 

    def add_admin():
        pass

    def delete_admin():
        pass

    def start_mailing():
        pass

product = Product()

