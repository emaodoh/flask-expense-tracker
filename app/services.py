
from . import models
from .expense_repo import create_expense, get_all_expenses
from datetime import datetime




def expense_statistics(user_id):
    expenses = get_all_expenses(user_id)
    print(expenses)
    if not expenses:
        return {
            "total": 0,
            "count": 0,
            "highest": 0
        }


    total = sum(expense.amount for expense in expenses)

    count = len(expenses)

    highest = max(
        expense.amount 
        for expense in expenses
    )


    return {
        "total": total,
        "count": count,
        "highest": highest
    }


def get_expense_by_id(id, user_id):
    expenses = get_all_expenses(user_id)
    for expense in expenses:

        if expense.id == id:
            return expense

    return None

        
def add_expense(user_id,category, item, date, amount):
    create_expense(user_id,category, item, amount,date)
    
    
def date_convert(date):
    date_string = date

    pure_date = datetime.strptime(date_string, "%Y-%m-%d").date()
    return pure_date


