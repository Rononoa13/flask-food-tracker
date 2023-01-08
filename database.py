import sqlite3

connection = sqlite3.connect("instance/food_log.db", check_same_thread=False)
# Changes returned list to dictionaries
connection.row_factory = sqlite3.Row

INSERT_FOOD = "INSERT INTO food (name, protein, carbohydrate, fat, calories) VALUES  (?, ?, ?, ?, ?)"
SELECT_FOOD = "SELECT * FROM food"

def add_food(name, protein, carbohydrate, fat, calories):
    with connection:
        connection.execute(INSERT_FOOD, (name, protein, carbohydrate, fat, calories))


def get_food():
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_FOOD)
        return cursor.fetchall()