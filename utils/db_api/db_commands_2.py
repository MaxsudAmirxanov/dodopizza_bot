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

# def get_subcategories():
#     try:
#         #connect to exist database
#         connection = psycopg2.connect(
#             host=host,
#             user=user,
#             password=password,
#             database = db_name
#         )
#         connection.autocommit = True

#         with connection.cursor() as cursor:
#             cursor.execute(
#                 'select items.subcategory_name from product;'
#             )
#             # print(cursor.fetchall()) 
#             # print(1)
#             return cursor.fetchall()
   
            

    # except Exception as _ex:
    #     print('[INFO] Error while working with PostgreSQL', _ex)

    # finally:
    #     if connection:
    #         connection.close()
    #         print('[INFO] PostgreSQL connection closed') 
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
                "select * from product where product.category_code=%s and product.subcategory_code=%s and product.name=%s; ", (category_code, subcategory_code, item_id)
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

# add_new_customer('Тема', 158347, 'ndbwu@gmail.com')


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



# pizza = 'pizza'
# vegan = 'vegan'
# print(get_items(pizza, vegan))


