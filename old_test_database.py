from database import get_connection

connection = get_connection()

print(connection)

connection.close()