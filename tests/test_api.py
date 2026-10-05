from app import expense_repo

def test_api_create_expense_requires_login(client):
    response = client.post(
        "/api/expenses",
        json={
            "category": "Food",
            "item": "Rice",
            "amount": 1000,
            "expense_date": "2026-10-02"
        }
    )

    assert response.status_code == 401



def test_create_and_delete_expenses_after_login(client, user):
    login_response = client.post(
        "/login",
        data={
            "login": "emodoh",
            "password": "4199"
        }
    )

    assert login_response.status_code == 302

    response = client.post("/api/expenses", json={
    "category": "Food",
    "item": "Rice",
    "amount": 1000,
    "expense_date": "2026-10-02"
    })


    assert response.status_code == 201

    expense = expense_repo.get_all_expenses()

    id = expense[0].id
    

    delete_response = client.delete(f"/api/expenses/{id}")

    assert delete_response.status_code == 200



def test_get_expenses_after_login(client, user):
    client.post(
        "/login",
        data={
            "login": "emodoh",
            "password": "4199"
        }
    )

    response = client.get("/api/expenses/")

    assert response.status_code == 200


