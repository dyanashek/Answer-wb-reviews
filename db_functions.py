import sqlite3
import itertools


def delete_answers(quality):
    try:
        database = sqlite3.connect("db.db")
        cursor = database.cursor()

        cursor.execute(f'DELETE FROM {quality}_reviews')
            
        database.commit()
        cursor.close()
        database.close()
    except:
        pass


def select_good_answers(recommended_product):
    try:
        database = sqlite3.connect("db.db")
        cursor = database.cursor()

        answers = cursor.execute(f'''SELECT answer
                                FROM good_reviews
                                WHERE recommended_product IS ? OR recommended_product NOT LIKE "%{recommended_product}%"
                                ''', (None,)).fetchall()
        
        cursor.close()
        database.close()

        if answers:
            answers = list(itertools.chain.from_iterable(answers))

        return answers

    except:
        pass


def select_bad_answers():
    try:
        database = sqlite3.connect("db.db")
        cursor = database.cursor()

        answers = cursor.execute('SELECT answer FROM bad_reviews').fetchall()
        
        cursor.close()
        database.close()

        if answers:
            answers = list(itertools.chain.from_iterable(answers))
        
        return answers
        
    except:
        pass


def add_good_answer(answer, recommended_product):
    try:
        database = sqlite3.connect("db.db")
        cursor = database.cursor()

        if recommended_product == '-':
            recommended_product = None

        cursor.execute(f'''
            INSERT INTO good_reviews (answer, recommended_product)
            VALUES (?, ?)
            ''', (answer, recommended_product,))
            
        database.commit()
        cursor.close()
        database.close()
    except:
        pass


def add_bad_answer(answer):
    try:
        database = sqlite3.connect("db.db")
        cursor = database.cursor()

        cursor.execute(f'''
            INSERT INTO bad_reviews (answer)
            VALUES (?)
            ''', (answer,))
            
        database.commit()
        cursor.close()
        database.close()
    except:
        pass


def add_trigger_answer(answer, trigger):
    try:
        database = sqlite3.connect("db.db")
        cursor = database.cursor()

        cursor.execute(f'''
            INSERT INTO trigger_reviews (answer, trigger)
            VALUES (?, ?)
            ''', (answer, trigger,))
            
        database.commit()
        cursor.close()
        database.close()
    except:
        pass


def add_answer_to_report(review_id, product_id, product_name, mark, comment, answer, answer_date):
    try:
        database = sqlite3.connect("db.db")
        cursor = database.cursor()

        cursor.execute(f'''
            INSERT INTO answers (review_id, product_id, product_name, mark, comment, answer, answer_date)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (review_id, product_id, product_name, mark, comment, answer, answer_date,))
            
        database.commit()
        cursor.close()
        database.close()
    except:
        pass


def select_today_answers_to_report(current_date):
    try:
        database = sqlite3.connect("db.db")
        cursor = database.cursor()

        answers_info = cursor.execute(f'''SELECT *
                                FROM answers
                                WHERE answer_date=?
                                ''', (current_date,)).fetchall()
        
        cursor.close()
        database.close()

        return answers_info

    except:
        pass


def select_all_answers_to_report():
    try:
        database = sqlite3.connect("db.db")
        cursor = database.cursor()

        answers_info = cursor.execute('SELECT * FROM answers').fetchall()
        
        cursor.close()
        database.close()

        return answers_info

    except:
        pass


def select_answer_by_trigger(trigger):
    try:
        database = sqlite3.connect("db.db")
        cursor = database.cursor()

        answer = cursor.execute(f'''SELECT answer
                                FROM trigger_reviews
                                WHERE trigger=?
                                ''', (trigger,)).fetchall()[0][0]
        
        cursor.close()
        database.close()

        return answer

    except:
        pass