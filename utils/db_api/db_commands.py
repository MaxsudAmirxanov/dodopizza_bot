from audioop import add
import psycopg2
from data.config import  PGUSER, PGPASSWORD, DATABASE
import asyncio
from loader import bot
host = '127.0.0.1'

class Database():
    def __init__(self):
        self.host=host,
        self.user=PGUSER,
        self.password=PGPASSWORD,
        self.database = DATABASE
  

class Product(Database):
    def get_category_name_distinct(self):
        try:
            #connect to exist database
            connection = psycopg2.connect(
                host=self.host[0],
                user=self.user[0],
                password=self.password[0],
                database=self.database
            )
            connection.autocommit = True

            with connection.cursor() as cursor:
                cursor.execute(
                    'select distinct product.category_name, product.category_code from product;'
                )
                # print(cursor.fetchall()) 
                # print(1)
                return cursor.fetchall()
    
                

        except Exception as _ex:
            print('[INFO] Error while working with PostgreSQL', _ex)

        finally:
            if connection:
                connection.close()
                print('[INFO] PostgreSQL connection closed')  

    def get_category_name(self):
        try:
            #connect to exist database
            connection = psycopg2.connect(
                host=self.host[0],
                user=self.user[0],
                password=self.password[0],
                database=self.database
            )
            connection.autocommit = True

            with connection.cursor() as cursor:
                cursor.execute(
                    'select product.category_name from product;'                )
                # print(cursor.fetchall()) 
                # print(1)
                return cursor.fetchall()
    
                

        except Exception as _ex:
            print('[INFO] Error while working with PostgreSQL', _ex)

        finally:
            if connection:
                connection.close()
                print('[INFO] PostgreSQL connection closed')  

    def get_subcategory_name(self, category_code):
        try:
            #connect to exist database
            connection = psycopg2.connect(
                host=self.host[0],
                user=self.user[0],
                password=self.password[0],
                database=self.database
            )
            connection.autocommit = True

            with connection.cursor() as cursor:
                cursor.execute(
                    "select distinct product.subcategory_name, product.subcategory_code from product where product.category_code=%s;", ((category_code,))
                )
                # print(cursor.fetchall())
                # print(1)
                return cursor.fetchall()
                
                

        except Exception as _ex:
            print('[INFO] Error while working with PostgreSQL', _ex)

        finally:
            if connection:
                connection.close()
                print('[INFO] PostgreSQL connection closed')  

    def get_products(self, category_code, subcategory_code):
        try:
            #connect to exist database
            connection = psycopg2.connect(
                host=self.host[0],
                user=self.user[0],
                password=self.password[0],
                database=self.database
            )
            connection.autocommit = True


            with connection.cursor() as cursor:
                cursor.execute(
                    "select * from product where subcategory_code=%s and category_code=%s; ", (subcategory_code, category_code)
                )
                # print(cursor.fetchall())
                # print(1)
                return cursor.fetchall()
                
                

        except Exception as _ex:
            print('[INFO] Error while working with PostgreSQL', _ex)

        finally:
            if connection:
                connection.close()
                print('[INFO] PostgreSQL connection closed')  

    def customer_db(self, category_code, subcategory_code, item_id):
        try:
            #connect to exist database
            connection = psycopg2.connect(
                host=self.host[0],
                user=self.user[0],
                password=self.password[0],
                database=self.database
            )
            connection.autocommit = True

            with connection.cursor() as cursor:
                cursor.execute(
                    "select * from product where product.category_code=%s and product.subcategory_code=%s and product.id=%s; ", (category_code, subcategory_code, item_id)
                )
                # print(cursor.fetchall())
                # print(1)
                return cursor.fetchall()
                
                

        except Exception as _ex:
            print('[INFO] Error while working with PostgreSQL', _ex)

        finally:
            if connection:
                connection.close()
                print('[INFO] PostgreSQL connection closed')  

    def add_product(self, name, category_code, category_name, subcategory_code, subcategory_name, photo, price):
        try:
            #connect to exist database
            #connect to exist database
            connection = psycopg2.connect(
                host=self.host[0],
                user=self.user[0],
                password=self.password[0],
                database=self.database
            )
            connection.autocommit = True


            with connection.cursor() as cursor:
                cursor.execute(
                    "insert into product (category_code, category_name, subcategory_code, subcategory_name, name, photo, price) values (%s, %s, %s, %s, %s, %s, %s) returning product;", (category_code, category_name, subcategory_code, subcategory_name, name, photo, price) 
                )
                # print(cursor.fetchall())
                # print(1)
                return cursor.fetchall()
                
                

        except Exception as _ex:
            print('[INFO] Error while working with PostgreSQL', _ex)

        finally:
            if connection:
                connection.close()
                print('[INFO] PostgreSQL connection closed')  

    def get_product(self, id):
        try:
            #connect to exist database
            connection = psycopg2.connect(
                host=self.host[0],
                user=self.user[0],
                password=self.password[0],
                database=self.database
            )
            connection.autocommit = True

            with connection.cursor() as cursor:
                cursor.execute(
                    "select * from product where id=%s;", (str(id),)
                )
                # print(cursor.fetchall())
                # print(1)
                return cursor.fetchall()
                
        except Exception as _ex:
            print('[INFO] Error while working with PostgreSQL', _ex)

        finally:
            if connection:
                connection.close()
                print('[INFO] PostgreSQL connection closed') 

class Cart(Database):
    def add_to_cart(self, user_id, product_id, count):
        try:
            #connect to exist database
            connection = psycopg2.connect(
                host=self.host[0],
                user=self.user[0],
                password=self.password[0],
                database=self.database
            )
            connection.autocommit = True

            with connection.cursor() as cursor:
                cursor.execute(
                    "insert into cart (user_id, product_id, product_count) values (%s, %s, %s) returning cart;", (user_id, product_id, count) 
                )
                print(cursor.fetchall())
                # print(1)
                # return cursor.fetchall()
                
        except Exception as _ex:
            print('[INFO] Error while working with PostgreSQL', _ex)

        finally:
            if connection:
                connection.close()
                print('[INFO] PostgreSQL connection closed') 

    def get_cart(self, user_id):
        try:
            #connect to exist database
            connection = psycopg2.connect(
                host=self.host[0],
                user=self.user[0],
                password=self.password[0],
                database=self.database
            )
            connection.autocommit = True

            with connection.cursor() as cursor:
                cursor.execute(
                    "select * from cart where user_id=%s;", (str(user_id),)
                )
                # print(cursor.fetchall())
                # print(1)
                return cursor.fetchall()
                
        except Exception as _ex:
            print('[INFO] Error while working with PostgreSQL', _ex)

        finally:
            if connection:
                connection.close()
                print('[INFO] PostgreSQL connection closed') 

    def rm_cart_product(self, product_id, user_id):
        try:
            #connect to exist database
            connection = psycopg2.connect(
                host=self.host[0],
                user=self.user[0],
                password=self.password[0],
                database=self.database
            )
            connection.autocommit = True

            with connection.cursor() as cursor:
                cursor.execute(
                    "delete from cart where user_id=%s and id=%s;", (user_id, product_id)
                )
                # print(cursor.fetchall())
                # print(1)
                # return cursor.fetchall()
                
        except Exception as _ex:
            print('[INFO] Error while working with PostgreSQL', _ex)

        finally:
            if connection:
                connection.close()
                print('[INFO] PostgreSQL connection closed') 

    def get_cart_product(self, cart_id):
        try:
            #connect to exist database
            connection = psycopg2.connect(
                host=self.host[0],
                user=self.user[0],
                password=self.password[0],
                database=self.database
            )
            connection.autocommit = True

            with connection.cursor() as cursor:
                cursor.execute(
                    "select * from cart where id=%s;", (str(cart_id),)
                )
                # print(cursor.fetchall())
                # print(1)
                return cursor.fetchall()
                
        except Exception as _ex:
            print('[INFO] Error while working with PostgreSQL', _ex)

        finally:
            if connection:
                connection.close()
                print('[INFO] PostgreSQL connection closed') 

    def edit_cart_product(self, cart_id, count):
        try:
            #connect to exist database
            connection = psycopg2.connect(
                host=self.host[0],
                user=self.user[0],
                password=self.password[0],
                database=self.database
            )
            connection.autocommit = True

            with connection.cursor() as cursor:
                cursor.execute(
                    "update cart set product_count=%s where id=%s;", (count, str(cart_id),)
                )
                # print(cursor.fetchall())
                # print(1)
                return cursor.fetchall()
                
        except Exception as _ex:
            print('[INFO] Error while working with PostgreSQL', _ex)

        finally:
            if connection:
                connection.close()
                print('[INFO] PostgreSQL connection closed') 

class Customer(Database):   
    def delete_customer(self, id):
        try:
            #connect to exist database
            connection = psycopg2.connect(
                host=self.host[0],
                user=self.user[0],
                password=self.password[0],
                database=self.database
            )
            connection.autocommit = True

            with connection.cursor() as cursor:
                cursor.execute(
                    'delete from customer where id=%s returning customer;', (id)
                )
                print(cursor.fetchall())
                # print(1)
                # return cursor.fetchall()
                
        except Exception as _ex:
            print('[INFO] Error while working with PostgreSQL', _ex)

        finally:
            if connection:
                connection.close()
                print('[INFO] PostgreSQL connection closed') 

    def add_customer(self, name, last_name, user_name, user_id):
        try:
            #connect to exist database
            connection = psycopg2.connect(
                host=self.host[0],
                user=self.user[0],
                password=self.password[0],
                database=self.database
            )
            connection.autocommit = True

            with connection.cursor() as cursor:
                cursor.execute(
                    "insert into customer (name, last_name, user_name, user_id) values (%s, %s, %s, %s) returning customer;", (name, last_name, user_name, user_id) 

                )
                print(cursor.fetchall())
                # print(1)
                # return cursor.fetchall()
                
        except Exception as _ex:
            print('[INFO] Error while working with PostgreSQL', _ex)

        finally:
            if connection:
                connection.close()
                print('[INFO] PostgreSQL connection closed') 

    def read_customer_id(self):
        try:
            #connect to exist database
            connection = psycopg2.connect(
                host=self.host[0],
                user=self.user[0],
                password=self.password[0],
                database=self.database
            )
            connection.autocommit = True

            with connection.cursor() as cursor:
                cursor.execute(
                    "select user_id from customer;"
                )
                # print(f"1111111111111111111 {cursor.fetchall()}")
                # print(1)
                return cursor.fetchall()
                
        except Exception as _ex:
            print('[INFO] Error while working with PostgreSQL', _ex)

        finally:
            if connection:
                connection.close()
                print('[INFO] PostgreSQL connection closed') 

    def find_customer_id(self, id):
        try:
            #connect to exist database
            connection = psycopg2.connect(
                host=self.host[0],
                user=self.user[0],
                password=self.password[0],
                database=self.database
            )
            connection.autocommit = True

            with connection.cursor() as cursor:
                cursor.execute(
                    "select id from customer as c where user_id=%s;", (str(id),)
                )
                # print(f"1111111111111111111 {cursor.fetchall()}")
                # print(1)
                return cursor.fetchall()
                
        except Exception as _ex:
            print('[INFO] Error while working with PostgreSQL', _ex)

        finally:
            if connection:
                connection.close()
                print('[INFO] PostgreSQL connection closed') 

class Referrer(Database):
    def add_referrer(self, user_id, id):
        try:
            #connect to exist database
            connection = psycopg2.connect(
                host=self.host[0],
                user=self.user[0],
                password=self.password[0],
                database=self.database
            )
            connection.autocommit = True

            with connection.cursor() as cursor:
                cursor.execute(
                    "insert into referrer (user_telegram_id, customer_id) values (%s, %s) returning referrer;", (user_id, id) 

                )
                print(cursor.fetchall())
                # print(1)
                # return cursor.fetchall()
                
        except Exception as _ex:
            print('[INFO] Error while working with PostgreSQL', _ex)

        finally:
            if connection:
                connection.close()
                print('[INFO] PostgreSQL connection closed') 

    def get_referrers_user_id(self):
        try:
            #connect to exist database
            connection = psycopg2.connect(
                host=self.host[0],
                user=self.user[0],
                password=self.password[0],
                database=self.database
            )
            connection.autocommit = True

            with connection.cursor() as cursor:
                cursor.execute(
                    "select user_telegram_id from referrer;" 

                )
                # print(cursor.fetchall())
                # print(1)
                return cursor.fetchall()
                
        except Exception as _ex:
            pass
            # print('[INFO] Error while working with PostgreSQL', _ex)

        finally:
            if connection:
                connection.close()
                print('[INFO] PostgreSQL connection closed') 
  
    def get_referrer_id(self, user_id):
        try:
            #connect to exist database
            connection = psycopg2.connect(
                host=self.host[0],
                user=self.user[0],
                password=self.password[0],
                database=self.database
            )
            connection.autocommit = True

            with connection.cursor() as cursor:
                cursor.execute(
                    'select id from referrer as r where r.user_telegram_id=%s;', (user_id,)

                )
                # print(cursor.fetchall())
                # print(1)
                return cursor.fetchall()
                
        except Exception as _ex:
            pass
            # print('[INFO] Error while working with PostgreSQL', _ex)

        finally:
            if connection:
                connection.close()
                print('[INFO] PostgreSQL connection closed') 

class Referral(Database):
    def add_referral(self, referrer_id, refferal_telegram_id):
        try:
            #connect to exist database
            connection = psycopg2.connect(
                host=self.host[0],
                user=self.user[0],
                password=self.password[0],
                database=self.database
            )
            connection.autocommit = True

            with connection.cursor() as cursor:
                cursor.execute(
                    'insert into referral(referrer_id, referral_telegram_id) values (%s, %s) returning referral;', (referrer_id, refferal_telegram_id)

                )
                # print(cursor.fetchall())
                # print(1)
                
                return cursor.fetchall()
            
                
        except Exception as _ex:
            # pass
            print('[INFO] Error while working with PostgreSQL', _ex)

        finally:
            if connection:
                connection.close()
                print('[INFO] PostgreSQL connection closed') 

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
    #                 'insert into referral(referrer_id, referral_telegram_id) values (%s, %s) returning referral;', (referrer_id, refferal_telegram_id)

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
    

