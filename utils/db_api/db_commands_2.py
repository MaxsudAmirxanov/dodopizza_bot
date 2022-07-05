# from django.db import connection
import psycopg2
from data.config import  PGUSER, PGPASSWORD, DATABASE
import asyncio
host = '127.0.0.1'

def get_all_database():
    try:
        #connect to exist database
        connection = psycopg2.connect(
            host=host,
            user=PGUSER,
            password=PGPASSWORD,
            database = DATABASE
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

def get_categories():
    try:
        #connect to exist database
        connection = psycopg2.connect(
            host=host,
            user=PGUSER,
            password=PGPASSWORD,
            database = DATABASE
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(
                'select product.category_name from product;'
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

def get_subcategories(category_code):
    try:
        #connect to exist database
        connection = psycopg2.connect(
            host=host,
            user=PGUSER,
            password=PGPASSWORD,
            database = DATABASE
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

def get_items(category_code, subcategory_code):
    try:
        #connect to exist database
        connection = psycopg2.connect(
            host=host,
            user=PGUSER,
            password=PGPASSWORD,
            database = DATABASE
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

def get_item(category_code, subcategory_code, item_id):
    try:
        #connect to exist database
        connection = psycopg2.connect(
            host=host,
            user=PGUSER,
            password=PGPASSWORD,
            database = DATABASE
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

def add_item(name, category_code, category_name, subcategory_code, subcategory_name, photo, price):
    try:
        #connect to exist database
        connection = psycopg2.connect(
            host=host,
            user=PGUSER,
            password=PGPASSWORD,
            database = DATABASE
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

def delete_user(id):
    try:
        #connect to exist database
        connection = psycopg2.connect(
            host=host,
            user=PGUSER,
            password=PGPASSWORD,
            database = DATABASE
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

def add_to_cart(user_id, product_id, count):
    try:
        #connect to exist database
        connection = psycopg2.connect(
            host=host,
            user=PGUSER,
            password=PGPASSWORD,
            database = DATABASE
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

def add_customer(name, last_name, user_name, user_id):
    try:
        #connect to exist database
        connection = psycopg2.connect(
            host=host,
            user=PGUSER,
            password=PGPASSWORD,
            database = DATABASE
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

def read_user_id():
    try:
        #connect to exist database
        connection = psycopg2.connect(
            host=host,
            user=PGUSER,
            password=PGPASSWORD,
            database = DATABASE
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

def find_user_id(id):
    try:
        #connect to exist database
        connection = psycopg2.connect(
            host=host,
            user=PGUSER,
            password=PGPASSWORD,
            database = DATABASE
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

def get_cart(user_id):
    try:
        #connect to exist database
        connection = psycopg2.connect(
            host=host,
            user=PGUSER,
            password=PGPASSWORD,
            database = DATABASE
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

def get_product(id):
    try:
        #connect to exist database
        connection = psycopg2.connect(
            host=host,
            user=PGUSER,
            password=PGPASSWORD,
            database = DATABASE
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

def rm_cart_product(product_id, user_id):
    try:
        #connect to exist database
        connection = psycopg2.connect(
            host=host,
            user=PGUSER,
            password=PGPASSWORD,
            database = DATABASE
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

def get_cart_product(cart_id):
    try:
        #connect to exist database
        connection = psycopg2.connect(
            host=host,
            user=PGUSER,
            password=PGPASSWORD,
            database = DATABASE
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

def edit_cart_product(cart_id, count):
    try:
        #connect to exist database
        connection = psycopg2.connect(
            host=host,
            user=PGUSER,
            password=PGPASSWORD,
            database = DATABASE
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



# pizza = 'pizza'
# vegan = 'vegan'
# print(get_items(pizza, vegan))



