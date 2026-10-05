from app import expense_repo, validator

def test_create_expense(client, user):
    login_response = client.post(
        "/login", data={
            "login":"emodoh",
            "password":"4199",
        }
    )
    expenses = expense_repo.get_all_expenses()

    assert len(expenses) == 0
    

    add_response = client.post("/add_expense", data={
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


    assert login_response.status_code == 302
    assert add_response.status_code == 302
    assert add_response.location.endswith("/")
    

def test_read_expense(client, user):
    login_response = client.post("/login", data={
        "login":"emodoh",
        "password":"4199",
    })

    assert login_response.status_code == 302

    add_response = client.post("/add_expense", data={
    "category": "Rent",
    "item": "House",
    "price": "2000000.0",
    "date": "2026-10-12",
})
    assert add_response.status_code == 302

    home_page_response = client.get("/")

    assert home_page_response.status_code == 200

    assert b"House" in home_page_response.data
    assert b"Rent" in home_page_response.data
    assert b"2000000.0" in home_page_response.data


def test_edit_expense(client, user ):
    login_response = client.post("/login", data={
        "login":"emodoh",
        "password":"4199",
    })

    assert login_response.status_code == 302


    add_response = client.post("/add_expense", data={
    "category": "Rent",
    "item": "House",
    "price": "2000000.0",
    "date": "2026-10-12",
})



    assert add_response.status_code == 302

    edit_response = client.post("/edit_expense/1", data={
        "category": "Transport",
        "item": "Okada",
        "price": "500",
        "date": "2026-10-12",
    })




    assert edit_response.status_code == 302

    expense = expense_repo.get_all_expenses()


    for ex in expense:
        assert ex.item == "Okada"
        assert ex.amount == 500
        assert ex.category == "Transport"


def test_delete_expense(client, user):
    login_response = client.post("/login", data={
        "login": "emodoh",
        "password": "4199"
    }
)
    assert login_response.status_code == 302


    add_response = client.post("/add_expense", data={
        "category": "Transport",
        "item": "Okada",
        "price": "500",
        "date": "2026-10-12",
    }
)  

    assert add_response.status_code == 302

    delete_response = client.delete("/delete_expense/1")

    assert delete_response.status_code == 302

    assert delete_response.location.endswith("/")

    expense = expense_repo.get_all_expenses()

    assert len(expense) == 0

