
from .models import Expense
from .extensions import db
from . import services


def create_expense(user_id,category,item,amount,date):
    expense = Expense(user_id=user_id,category=category,item=item,amount=amount,expense_date=services.date_convert(date))

    db.session.add(expense)
    db.session.commit()
def get_all_expenses(user_id):
    expenses = Expense.query.filter_by(user_id=user_id).all()
    return expenses


def edit_expense(user_id, category, item, expense_date, price,expense_id):
    expense = get_expense_by_id(expense_id, user_id)

    expense.item = item
    expense.category = category
    expense.expense_date = services.date_convert(expense_date)
    expense.amount = price

    db.session.commit()

def get_expense_by_id(expense_id,user_id):
    return Expense.query.filter_by(
    id=expense_id,
    user_id=user_id
).first()


def delete_expense(expense_id, user_id):
    expense = get_expense_by_id(expense_id,user_id)
    db.session.delete(expense)
    db.session.commit()

