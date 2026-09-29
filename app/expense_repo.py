
from .models import Expense
from .extensions import db
from . import services


def create_expense(category,item,amount,date):
    expense = Expense(category=category,item=item,amount=amount,expense_date=services.date_convert(date))

    db.session.add(expense)
    db.session.commit()
def get_all_expenses():
    return Expense.query.all()


def edit_expense(category, item, expense_date, price,id):
    expense = get_expense_by_id(id)

    expense.item = item
    expense.category = category
    expense.expense_date = services.date_convert(expense_date)
    expense.amount = price

    db.session.commit()

def get_expense_by_id(id):
    return db.session.get(Expense, id)


def delete_expense(id):
    expense = get_expense_by_id(id)
    db.session.delete(expense)
    db.session.commit()