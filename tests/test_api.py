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