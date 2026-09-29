import sqlite3

DATABASE = "expenses.db"



def get_connection():
    connection = sqlite3.connect(DATABASE)
    return connection

def create_table():
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT NOT NULL,
            item TEXT NOT NULL,
            description TEXT,
            amount REAL NOT NULL,
            currency TEXT,
            payment_method TEXT,
            expense_date TEXT,
            created_at TEXT,
            updated_at TEXT
        )
        """)

    connection.commit()
    connection.close()

create_table()
