import sqlite3

conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tables:", cursor.fetchall())

cursor.execute("PRAGMA table_info(users);")
print("Users:", cursor.fetchall())

cursor.execute("PRAGMA table_info(expenses);")
print("Expenses:", cursor.fetchall())

conn.close()