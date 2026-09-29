import sqlite3

DATABASE = "expenses.db"

def get_connection():
    connection = sqlite3.connect(DATABASE)
    return connection




def get_all_expenses():
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM expenses")

    expenses = cursor.fetchall()

    connection.close()

    return expenses

db = get_all_expenses()

for item in db:
    print(item)