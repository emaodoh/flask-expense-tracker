from app import expense_repo, validator

def test_create_expense(client, user):
    response = client.post(
        "/login", data={
            "login":"emodoh",
            "password":"4199",
        }
    )
    expenses = expense_repo.get_all_expenses()

    assert len(expenses) == 0
    

    response1 = client.post("/add_expense", data={
    "category": "rent",
    "item": "house",
    "price": "2000000.0",
    "date": "2026-10-12",
})
    expenses = expense_repo.get_all_expenses()

    
    assert len(expenses) == 1
    
    for expense in expenses:
        assert expense.item == "house"
        assert expense.amount == 2000000.0
        assert expense.expense_date == validator.date_convert("2026-10-12")
        assert expense.category == "rent"


    assert response.status_code == 302
    assert response1.status_code == 302
    assert response1.location.endswith("/")
    

def test_read_expense(client, user):
    response = client.post("/login", data={
        "login":"emodoh",
        "password":"4199",
    })

    assert response.status_code == 302

    response1 = client.post("/add_expense", data={
    "category": "Rent",
    "item": "House",
    "price": "2000000.0",
    "date": "2026-10-12",
})
    assert response1.status_code == 302

    response2 = client.get("/")

    assert response2.status_code == 200

    assert b"House" in response2.data
    assert b"Rent" in response2.data
    assert b"2000000.0" in response2.data


def test_update_expense(client, user ):
    response = client.post("/login", data={
        "login":"emodoh",
        "password":"4199",
    })

    assert response.status_code == 302


    response1 = client.post("/add_expense", data={
    "category": "Rent",
    "item": "House",
    "price": "2000000.0",
    "date": "2026-10-12",
})

    assert response1.status_code == 302

    expense_repo.edit_expense()
