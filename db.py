import sqlite3
import logging

database = sqlite3.connect("db.db", detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
cursor = database.cursor()

try:
    cursor.execute('''CREATE TABLE answers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        review_id TEXT,
        product_id TEXT,
        product_name TEXT,
        mark INTEGER,
        comment TEXT,
        answer TEXT,
        answer_date TEXT
    )''')
except Exception as ex:
    logging.error(f'Users table already exists. {ex}')


try:
    cursor.execute('''CREATE TABLE good_reviews (
        id INTEGER PRIMARY KEY,
        answer TEXT,
        recommended_product TEXT
    )''')
except Exception as ex:
    logging.error(f'Users table already exists. {ex}')


try:
    cursor.execute('''CREATE TABLE bad_reviews (
        id INTEGER PRIMARY KEY,
        answer TEXT
    )''')
except Exception as ex:
    logging.error(f'Users table already exists. {ex}')


try:
    cursor.execute('''CREATE TABLE trigger_reviews (
        id INTEGER PRIMARY KEY,
        answer TEXT,
        trigger TEXT
    )''')
except Exception as ex:
    logging.error(f'Users table already exists. {ex}')