import sqlite3


class Database():
    def __init__(self):
        db = sqlite3.connect("database.db")
        self.cur = db.cursor()
        

class Product():
    def get_category_name_distinct(self):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute('select distinct product.category_name, product.category_code from product;')

                db.commit()
                return cursore.fetchall()
        except Exception as _ex:
            print(f'[SQLite] {_ex}')
                
    def test_product(self):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute("UPDATE product SET photo='AgACAgIAAxkBAAILE2LXAriaTOYQ-2o_vw4D0iWtabOoAAIYwTEbecq' WHERE id=1")
                # cursore.execute('select * from product;')

                db.commit()
                return cursore.fetchall()
        except Exception as _ex:
            print(f'[SQLite] {_ex}') 

    def get_category_name(self):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute('select product.category_name from product;')

                db.commit()
                return cursore.fetchall()
        except Exception as _ex:
            print(f'[SQLite] {_ex}')
    
    def get_subcategory_name(self, category_code):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute("select distinct product.subcategory_name, product.subcategory_code from product where product.category_code=?;", ((category_code,)))

                db.commit()
                return cursore.fetchall()
        except Exception as _ex:
            print(f'[SQLite] {_ex}')

    def get_products(self, category_code, subcategory_code):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute("select * from product where subcategory_code=? and category_code=?; ", (subcategory_code, category_code))

                db.commit()
                return cursore.fetchall() 
        except Exception as _ex:
            print(f'[SQLite] {_ex}')

    def customer_db(self, category_code, subcategory_code, item_id):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute("select * from product where product.category_code=? and product.subcategory_code=? and product.id=?; ", (category_code, subcategory_code, item_id))

                db.commit()
                return cursore.fetchall()
        except Exception as _ex:
            print(f'[SQLite] {_ex}')


    def add_product(self, name, category_code, category_name, subcategory_code, subcategory_name, photo, price):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute("insert into product (category_code, category_name, subcategory_code, subcategory_name, name, photo, price) values (?, ?, ?, ?, ?, ?, ?);", (category_code, category_name, subcategory_code, subcategory_name, name, photo, price))
                
                db.commit()
                return cursore.fetchall()
        except Exception as _ex:
            print(f'[SQLite] {_ex}')

    def get_product(self, id):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute("select * from product where id=?;", (str(id),))

                db.commit()
                return cursore.fetchall()
        except Exception as _ex:
            print(f'[SQLite] {_ex}')
class Cart():
    def add_to_cart(self, user_id, product_id, count):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute("insert into cart (user_id, product_id, product_count) values (?, ?, ?)", (user_id, product_id, count))

                db.commit()
                return cursore.fetchall()
                "returning"
        except Exception as _ex:
            print(f'[SQLite] {_ex}')

    def get_cart(self, user_id):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute("select * from cart where user_id=?;", (str(user_id),))

                db.commit()
                return cursore.fetchall()  
        except Exception as _ex:
            print(f'[SQLite] {_ex}')

    def rm_cart_product(self, product_id, user_id):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute("delete from cart where user_id=? and id=?;", (user_id, product_id))

                db.commit()
                return cursore.fetchall()
        except Exception as _ex:
            print(f'[SQLite] {_ex}')

    def get_cart_product(self, cart_id):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute("select * from cart where id=?;", (str(cart_id),))

                db.commit()
                return cursore.fetchall()
        except Exception as _ex:
            print(f'[SQLite] {_ex}')

    def edit_cart_product(self, cart_id, count):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute("update cart set product_count=? where id=?;", (count, str(cart_id),))

                db.commit()
                return cursore.fetchall()
        except Exception as _ex:
            print(f'[SQLite] {_ex}')
class Customer():   
    def delete_customer(self, id):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute('delete from customer where id=?;', (id))

                db.commit()
                return cursore.fetchall()
                "returning"
        except Exception as _ex:
            print(f'[SQLite] {_ex}')
    
    def show_customer():
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute('select * from customer;')

                db.commit()
                return cursore.fetchall()
                "returning"
        except Exception as _ex:
            print(f'[SQLite] {_ex}')

    def add_customer(self, name, last_name, user_name, user_id):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute("insert into customer (name, last_name, user_name, user_id) values (?, ?, ?, ?);", (name, last_name, user_name, user_id))

                db.commit()
                return cursore.fetchall()
                "returning"
        except Exception as _ex:
            print(f'[SQLite] {_ex}')

    def read_customer_id(self):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute("select user_id from customer;")

                db.commit()
                return cursore.fetchall()
        except Exception as _ex:
            print(f'[SQLite] {_ex}')
    
    def find_customer_id(self, id):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute("select id from customer as c where user_id=?;", (str(id),))

                db.commit()
                return cursore.fetchall()
        except Exception as _ex:
            print(f'[SQLite] {_ex}')
class Referrer():
    def add_referrer(self, user_id, id):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute("insert into referrer (user_telegram_id, customer_id) values (?, ?);", (user_id, id))

                db.commit()
                return cursore.fetchall() 
                "returning"
        except Exception as _ex:
            print(f'[SQLite] {_ex}')
    
    def get_referrers_user_id(self):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute("select user_telegram_id from referrer;" )

                db.commit()
                return cursore.fetchall()
        except Exception as _ex:
            print(f'[SQLite] {_ex}')
                
    def get_referrer_id(self, user_id):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute('select id from referrer as r where r.user_telegram_id=?;', (user_id,))

                db.commit()
                return cursore.fetchall()
        except Exception as _ex:
            print(f'[SQLite] {_ex}')
class Referral():
    def add_referral(self, referrer_id, refferal_telegram_id):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute('insert into referral(referrer_id, referral_telegram_id) values (?, ?) returning referral;', (referrer_id, refferal_telegram_id))

                db.commit()
                return cursore.fetchall()
        except Exception as _ex:
            print(f'[SQLite] {_ex}')
class Admin():
    def chek_block_customer(self,  id):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute('SELECT blocked FROM customer WHERE user_id=?', (int(id),))
                # cursore.execute('select * from admin;')

                db.commit()
                return cursore.fetchall()
                
        except Exception as _ex:
            print(f'[SQLite] {_ex}') 
            

    def blocked_customer(self, id):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute('UPDATE customer SET blocked=1 WHERE user_id=?', (int(id),))
                # cursore.execute('select * from admin;')

                db.commit()
                return True
        except Exception as _ex:
            print(f'[SQLite] {_ex}') 
            return False
        pass

    def unblocked_customer(self, id):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute('UPDATE customer SET blocked=0 WHERE user_id=?', (int(id),))
                # cursore.execute('select * from admin;')

                db.commit()
                return True
        except Exception as _ex:
            print(f'[SQLite] {_ex}') 
            return False
        pass
    
    def chek_admin(self, id):
    
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute('select * from admin where user_telegram_id=?;', (int(id),))
                # cursore.execute('select * from admin;')

                db.commit()
                return cursore.fetchall()
        except Exception as _ex:
            print(f'[SQLite] {_ex}')

    def add_admin():
        pass

    def delete_admin():
        pass

    def start_mailing():
        pass

product = Product()
admin = Admin()
def test_product():
    try:
        with sqlite3.connect('utils/db_api/database.db') as db:
            cursore = db.cursor()
            # cursore.execute('UPDATE product SET photo="AgACAgIAAxkBAAILWGLXDfbxFaEqs7HBaAABTv0LEPI6EAACR8ExG3nKuUoCcbmOCAWIpQEAAwIAA3MAAykE" WHERE id=15')
            cursore.execute('select id, name, photo from product;')

            db.commit()
            return cursore.fetchall()
    except Exception as _ex:
        print(f'[SQLite] {_ex}') 
        
print(test_product())
# print(admin.chek_admin(91510596))

