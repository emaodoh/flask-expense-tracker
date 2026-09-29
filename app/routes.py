from flask import  Blueprint, render_template, request, redirect, flash, url_for, abort
from .models import Expense
from . import services

from . import expense_repo 


main = Blueprint("main", __name__)



@main.route("/")
def home():
    
    expenses = expense_repo.get_all_expenses()
    statistics = services.expense_statistics()

    return render_template(
        "index.html",
        expenses=expenses,
        statistics=statistics
    )

@main.route("/edit_expense/<int:id>", methods=["GET", "POST"])
def edit_expense(id):
    expense = expense_repo.get_expense_by_id(id)
    if expense is None:
        abort(404)
        
    
    if  expense:
        

        

        if request.method == "POST":
                
            expense_date = request.form["date"]
            category = request.form["category"]
            amount = float (request.form["price"])
            item = request.form["item"]
            expense_repo.edit_expense(category, item, expense_date, amount,id)
            
        
            
            flash("Expense have been updated successfully")
            return redirect(url_for("main.home"))


        return render_template(
            "edit.html",
            expense=expense
        )

    return "Expense not found"

@main.route("/delete_expense/<int:id>")
def delete_expense(id):
    
    expense_repo.delete_expense(id)
   

    flash("Expenses deleted successfully")

    return redirect(url_for("main.home"))

@main.route("/add_expense", methods=["GET", "POST"])
def add_expense():
    expenses = expense_repo.get_all_expenses()
    if request.method == "POST":

        category = request.form["category"]
        item = request.form["item"]
        price = float (request.form["price"])
        date = str(request.form["date"])
        

        services.add_expense(category, item, date, price)

        

        flash("Expense added successfully!", "success")
        return redirect(url_for("main.home"))

    return render_template("add.html")
