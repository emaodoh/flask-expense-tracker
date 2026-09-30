from functools import wraps 
from flask import session, redirect, url_for


def login_required(function):

    @wraps(function)
    def wrapper(*args, **kwargs):
        print(session)
        if "user_id" not in session:
            return redirect(url_for("main.login"))
        

        return function(*args, **kwargs)

    return wrapper