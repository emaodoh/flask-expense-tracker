from .database import get_connection
from .models import Expense


def create_expense(category,item,amount):
    connection = get_connection()
    print(connection.execute("PRAGMA database_list").fetchall())
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO expenses (category, item, amount)
        VALUES (?,?,?)
        """,

        (category, item, amount)
    )

    connection.commit()
    connection.close()


def get_all_expenses():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM expenses")

    rows = cursor.fetchall()

    expenses = []

    for row in rows:
        expense = Expense(row[0], row[1], row[2], row[7], row[4])
        expenses.append(expense)


    connection.close()

    return expenses


def edit_expense(category, item, expense_date, amount,id):
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
    """
    UPDATE expenses
    SET category =?, item = ?, expense_date = ?, amount =?
    WHERE id =?;
    """,

    (category, item, expense_date, amount, id),

    )

    connection.commit()
    connection.close()

def get_expense_by_id(id):
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM expenses WHERE id =?", (id,))

    row = cursor.fetchone()

    if row == None:
        return None
    expense = Expense(row[0], row[1], row[2], row[7], row[4])
    connection.close()

    return expense


def delete_expense(id):
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("DELETE FROM expenses WHERE id = ?", (id,))

    connection.commit()
    connection.close()