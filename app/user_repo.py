from .models import User
from .extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

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

    
