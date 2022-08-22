
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

    def get_product_photo(self, id):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute("SELECT photo FROM product where id=?;", (id,))

                db.commit()
                return cursore.fetchall()
        except Exception as _ex:
            print(f'[SQLite] {_ex}')
            return False

    def edit_product_name(self, id, name):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute("UPDATE product SET name=? WHERE id=?;", (name, id))

                db.commit()
                return cursore.fetchall()
        except Exception as _ex:
            print(f'[SQLite] {_ex}')
            return False

    def edit_product_price(self, id, price):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute("UPDATE product SET price=? WHERE id=?;", (price, id))

                db.commit()
                return cursore.fetchall()
        except Exception as _ex:
            print(f'[SQLite] {_ex}')
            return False

    def edit_product_photo(self, id, photo_id):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute("UPDATE product SET photo=? WHERE id=?;", (photo_id, id))

                db.commit()
                return cursore.fetchall()
        except Exception as _ex:
            print(f'[SQLite] {_ex}')
            return False

    def get_distinct_category_name(self, category_code):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute("SELECT distinct category_name FROM product WHERE category_code=?;", (category_code,))

                db.commit()
                return cursore.fetchall()
        except Exception as _ex:
            print(f'[SQLite] {_ex}')
            return False

    def get_distinct_subcategory_name(self, category_code, subcategory_code):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute("SELECT distinct subcategory_name FROM product WHERE category_code=? AND subcategory_code=?;", (category_code, subcategory_code))

                db.commit()
                return cursore.fetchall()
        except Exception as _ex:
            print(f'[SQLite] {_ex}')
            return False

    def distinct_subcategory_name(self, category):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute("SELECT distinct subcategory_name FROM product WHERE category_code=?;", (category,))

                db.commit()
                return cursore.fetchall()
        except Exception as _ex:
            print(f'[SQLite] {_ex}')
            return False


    def delete_product(self, id):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute("DELETE FROM product where id=?;", (id,))

                db.commit()
                return True
        except Exception as _ex:
            print(f'[SQLite] {_ex}')
            return False

    def show_products(self):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute("SELECT * FROM product;")

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
                cursore.execute("SELECT * from product where subcategory_code=? and category_code=?; ", (subcategory_code, category_code))

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

    def add_category(self, catrgory_name, category_code):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute("insert into product(category_name, category_code, subcategory_name, subcategory_code, name, photo, price) values (?, ?, '-', '-', '-', '-', '-');", (catrgory_name, category_code))

                db.commit()
                return cursore.fetchall()
        except Exception as _ex:
            print(f'[SQLite] {_ex}')
            return False

    def add_subcategory(self, category_name, category_code, subcategory_name, subcategory_code):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute("INSERT INTO product(category_name, category_code, subcategory_name, subcategory_code, name, photo, price) values (?, ?, ?, ?, '-', '-', '-');", (category_name, category_code, subcategory_name, subcategory_code))

                db.commit()
                return cursore.fetchall()
        except Exception as _ex:
            print(f'[SQLite] {_ex}')
            return False

    def get_product(self, id):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute("select * from product where id=?;", (str(id),))

                db.commit()
                return cursore.fetchall()
        except Exception as _ex:
            print(f'[SQLite] {_ex}')

    def delete_category(self, catrgory_name):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute("DELETE FROM product where category_name=?", (catrgory_name[0][0],))

                db.commit()
                return cursore.fetchall()
        except Exception as _ex:
            print(f'[SQLite] {_ex}')
            return False

    def delete_subcategory(self, catrgory_name, subcategory_name):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute("DELETE FROM product where category_name=? and subcategory_name=?", (catrgory_name[0][0], subcategory_name[0][0]))

                db.commit()
                return cursore.fetchall()
        except Exception as _ex:
            print(f'[SQLite] {_ex}')
            return False

    def fined_category_name(self, catrgory_code):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute("SELECT distinct category_name FROM product whete category_code=?", (catrgory_code,))

                db.commit()
                return cursore.fetchall()
        except Exception as _ex:
            print(f'[SQLite] {_ex}')
            return False


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
                cursore.execute("DELETE from cart where user_id=? and product_id=?;", (user_id, product_id))

                db.commit()
                # return cursore.fetchall()
                return True
        except Exception as _ex:
            print(f'[SQLite] {_ex}')
            return False

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
            return False


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

    def show_admin(self):
        
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute('select a.*, c.name, c.last_name, c.user_id from admin a left join customer c on  a.customer_id=c.id;')
                # cursore.execute('select * from admin;')

                db.commit()
                return cursore.fetchall()
        except Exception as _ex:
            print(f'[SQLite] {_ex}')

class MainAdmin():
    def chek_main_admin(self, id):
        
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute('select * from main_admin where user_telegram_id=?;', (int(id),))
                # cursore.execute('select * from admin;')

                db.commit()
                return cursore.fetchall()
        except Exception as _ex:
            print(f'[SQLite] {_ex}')

    def get_admin_name(self, id):
        
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute('select c.name, c.last_name from admin a left JOIN customer c on a.customer_id=c.id where a.user_telegram_id=?', (int(id),))
                # cursore.execute('select * from admin;')

                db.commit()
                return cursore.fetchall()
        except Exception as _ex:
            print(f'[SQLite] {_ex}')

    def add_admin(test, user_name, user_telegram_id, customer_id, main_admin_id):
        
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute('insert into admin(main_admin_id, user_name, user_telegram_id, customer_id) values (?, ?, ?, ?)', (main_admin_id, user_name, user_telegram_id, customer_id))
                # cursore.execute('select * from admin;')

                db.commit()
                return cursore.fetchall()
        except Exception as _ex:
            print(f'[SQLite] {_ex}')
            return False

    def delete_admin(self, id):
        
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute('delete from admin where user_telegram_id=?', (int(id),))
                # cursore.execute('select * from admin;')

                db.commit()
                return cursore.fetchall()
        except Exception as _ex:
            print(f'[SQLite] {_ex}')

    def find_main_admin_id(self, id):
        try:
            with sqlite3.connect('utils/db_api/database.db') as db:
                cursore = db.cursor()
                cursore.execute("select id from main_admin where user_telegram_id=?;", (str(id),))

                db.commit()
                return cursore.fetchall()
        except Exception as _ex:
            print(f'[SQLite] {_ex}')

    def start_mailing():
        pass

# product = Product()
# admin = Admin()

# print(product.delete_product(16))
        
# print(test_product())
# print(admin.chek_admin(91510596))

# product.delete_subcategory(input(), input())

