
def validate_expense_data(data):

    if not data:
        return {"error": "No JSON data provided"}, 400

    required_fields = [
    "category",
    "item",
    "amount",
    "expense_date"
]

    missing_fields = []

    for field in required_fields:
        if field not in data:
            missing_fields.append(field)


    if missing_fields:
        return {"error":"Missing required fields", "missing":missing_fields}, 400


    return None