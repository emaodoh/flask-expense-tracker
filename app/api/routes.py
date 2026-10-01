from . import api 
from ..expense_repo import get_all_expenses,get_expense_by_id, create_expense, edit_expense, delete_expense
from flask import jsonify, request, session
from .validator import validate_expense_data
from ..user_repo import get_all_user_expenses

@api.route("/expenses/", methods=["GET"])
def get_expenses_api():
    if "user_id" not in session:
        return jsonify({"error": "Unauthorized"}), 401

    expenses = get_all_user_expenses(session["user_id"])

    result = [expense.to_dict() for expense in expenses]

    return jsonify(result)


@api.route("/expenses", methods=["POST"])
def create_expense_api():
    if "user_id" not in session:
        return jsonify({"error": "Unauthorized"}), 401


    data = request.get_json()
    
    error = validate_expense_data(data)

    if error:
        message, status = error
        return jsonify(message), status
    
    create_expense(session["user_id"], data["category"],data["item"],data["amount"], data["expense_date"])


    return jsonify({
    "message": "Expense added successfully."
}), 201

@api.route("/expenses/<int:id>")
def get_expesnse_by_id_api(id):
    if "user_id" not in session:
        return jsonify({"error": "Unauthorized"}), 401

    expense = get_expense_by_id(id,session["user_id"])

    if not expense:
        return jsonify({"error":"Expense not found"}), 404

    return jsonify(expense.to_dict())
    
@api.route("/expenses/<int:id>", methods=["PUT"])
def edit_expense_api(id):
    if "user_id" not in session:
        return jsonify({"error":"Unauthorized"}), 401

    data = request.get_json()

    error = validate_expense_data(data)

    if error:
        message,status = error
        return jsonify(message), status

    expense = get_expense_by_id(id,session["user_id"])

    if not expense:
        return jsonify({"error":"Expense not found"}), 404

    edit_expense(session["user_id"],data["category"], data["item"], data["expense_date"], data["amount"],id)
    

    updated_expense = get_expense_by_id(id, session["user_id"])
    return jsonify(updated_expense.to_dict())


@api.route("/expenses/<int:id>", methods=["DELETE"])
def delete_expense_api(id):
    if "user_id" not in session:
        return jsonify({"error":"Unauthorized"}), 401

    expense = get_expense_by_id(id,session["user_id"])

    if not expense:
        return jsonify({"error":"Expense not found"}), 404

    delete_expense(id, session["user_id"])

    return jsonify({
    "message": "Expense deleted successfully."
}), 200