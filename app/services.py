
from . import models
from .user_repo import get_all_user_expenses




def expense_statistics(user_id):
    expenses = get_all_user_expenses(user_id)
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

    


