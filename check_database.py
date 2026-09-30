import sqlite3

conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

cursor.execute("PRAGMA table_info(expenses)")
print(cursor.fetchall())

cursor.execute("SELECT * FROM expenses")
print(cursor.fetchall())

conn.close()