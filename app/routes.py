from flask import  Blueprint, render_template, request, redirect, flash, url_for, abort, session
from .models import Expense
from . import services
from .validator import validate_registration
from . import expense_repo 
from .user_repo import create_user,validate_user,get_all_user_expenses
from .decorators import login_required


main = Blueprint("main", __name__)



@main.route("/")
@login_required
def home():
    
    expenses = get_all_user_expenses(session["user_id"])
    statistics = services.expense_statistics(session["user_id"])

    return render_template(
        "index.html",
        expenses=expenses,
        statistics=statistics
    )

@main.route("/edit_expense/<int:id>", methods=["GET", "POST"])
@login_required
def edit_expense(id):
    expense = services.get_expense_by_id(id,session["user_id"])
    if expense is None:
        abort(404)
        
    
    if  expense:
        

        

        if request.method == "POST":
                
            expense_date = request.form["date"]
            category = request.form["category"]
            amount = float (request.form["price"])
            item = request.form["item"]
            expense_repo.edit_expense(session["user_id"],category, item, expense_date, amount,id)
            
        
            
            flash("Expense have been updated successfully")
            return redirect(url_for("main.home"))


        return render_template(
            "edit.html",
            expense=expense
        )

    return "Expense not found"

@main.route("/delete_expense/<int:id>")
@login_required
def delete_expense(id):
    
    expense_repo.delete_expense(id,session["user_id"])
   

    flash("Expenses deleted successfully")

    return redirect(url_for("main.home"))

@main.route("/add_expense", methods=["GET", "POST"])
@login_required
def add_expense():
    if request.method == "POST":

        category = request.form["category"]
        item = request.form["item"]
        price = float (request.form["price"])
        date = str(request.form["date"])
        

        services.add_expense(session["user_id"],category, item, date, price)

        

        flash("Expense added successfully!", "success")
        return redirect(url_for("main.home"))

    return render_template("add.html")


@main.route("/register", methods = ["POST", "GET"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        confirm_password = request.form["confirm_password"]
        password = request.form["password"]

        error = validate_registration(username,email,password,confirm_password)

        if error:
            flash(error, "error")
            return redirect(url_for("main.register"))

        create_user(username,email,password)

        flash("Account created successfully!", "success")

        return redirect(url_for("main.login"))

    return render_template("register.html")



@main.route("/login", methods=["POST", "GET"])
def login():
    if "user_id" in session:
        return redirect(url_for("main.home"))

    if request.method == "POST":
        
        login = request.form["login"]
        password = request.form["password"]

        user = validate_user(login,password)
        
        if not user:
            flash("Invalid username/email or password.", "error")
            return redirect(url_for("main.login"))

        session["user_id"] = user.id

        flash("Login successful!", "success")
        return redirect(url_for("main.home"))


    return render_template("login.html")

@main.route("/logout")
def logout():

    session.pop("user_id", None)

    flash("You have been logged out successfully.", "success")

    return redirect(url_for("main.login"))

    