import sqlite3


def create_connection(hw_db):
    connection = None
    try:
        connection = sqlite3.connect(hw_db)
    except sqlite3.Error as e:
        print(e)
    return connection


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)


def insert_product(conn, product):
    sql = '''INSERT INTO product 
    (product_title, price, quantity) 
    VALUES (?, ?, ?)'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def product_all(conn):
    sql = '''SELECT * FROM product'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql)

        rows_list = cursor.fetchall()
        for row in rows_list:
            print(row)

    except sqlite3.Error as e:
        print(e)


def select_product_by__limit(conn, limit):
    sql = '''SELECT * FROM product WHERE id >= ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (limit,))

        rows_list = cursor.fetchall()
        for row in rows_list:
            print(row)

    except sqlite3.Error as e:
        print(e)


def update_student(conn, product):
    sql = '''UPDATE product SET price = ?, quantity = ? WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def delete_product(conn, id):
    sql = '''DELETE FROM product WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)


sql_create_product_table = '''
CREATE TABLE product (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR(200) NOT NULL,
price  FLOAT(5,2)  DEFAULT 0.0,
quantity INTEGER NOT NULL DEFAULT 0     
)
'''

connection_to_db = create_connection('homework_7.db')
if connection_to_db is not None:
    print('Successfully connected to DB!')
    create_table(connection_to_db, sql_create_product_table)
    insert_product(connection_to_db, ("Apple", 345.6, 23 ))
    insert_product(connection_to_db, ("Banana", 296, 455. ))
    insert_product(connection_to_db, ("Meat", 398,87, 490. ))
    insert_product(connection_to_db, ("Bread", 32, 455.99 ))
    insert_product(connection_to_db, ("Watermelon", 900, 566 ))
    insert_product(connection_to_db, ("Melon", 453.54, 44  ))
    insert_product(connection_to_db, ("Toothbrush", 115.54, 45 ))
    insert_product(connection_to_db, ("Pasta", 106.34, 100 ))
    insert_product(connection_to_db, ("Soap", 35.8, 55 ))
    insert_product(connection_to_db, ("Shampoo", 75.90, 120 ))
    insert_product(connection_to_db, ("Liquid soap", 175, 56 ))
    connection_to_db.close()