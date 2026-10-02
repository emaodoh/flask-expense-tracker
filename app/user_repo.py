from .models import User
from .extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from .models import Expense


def create_user(username, email, password):
    hashed_password = generate_password_hash(password)
    new_user = User(username=username, email=email, password_hash=hashed_password)
    db.session.add(new_user)
    db.session.commit()

def get_user_by_username(username):
    username = User.query.filter_by(username=username).first()
    return username


def get_user_by_email(email):
    user_email = User.query.filter_by(email=email).first()
    return user_email


def validate_user(login,password):
    user = get_user_by_username(login)
    if not user:
        user = get_user_by_email(login)
        
    if not user:
        return None
    
    if check_password_hash(user.password_hash,password):

        return user

    return None


def get_all_user_expenses(user_id):
    expenses = Expense.query.filter_by(user_id=user_id).all()
    return expenses



def get_expense_by_user_id(expense_id,user_id):
    return Expense.query.filter_by(
    id=expense_id,
    user_id=user_id
).first()



def create_user_expense(user_id,category,item,amount,date):
    expense = Expense(user_id=user_id,category=category,item=item,amount=amount,expense_date=validator.date_convert(date))

    db.session.add(expense)
    db.session.commit()