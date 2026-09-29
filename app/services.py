
from . import models
from .database import create_table
from .expense_repo import create_expense, get_all_expenses





def expense_statistics():
    expenses = get_all_expenses()
    if not expenses:
        return {
            "total": 0,
            "count": 0,
            "highest": 0
        }


    total = sum(expense.price for expense in expenses)

    count = len(expenses)

    highest = max(
        expense.price 
        for expense in expenses
    )


    return {
        "total": total,
        "count": count,
        "highest": highest
    }


def get_expense_by_id(id):
    expenses = get_all_expenses()
    for expense in expenses:

        if expense.id == id:
            return expense

    return None

        
def add_expense(category, item, date, price):
    create_expense(category, item, price)
    
    
    



