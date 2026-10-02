def test_home_page(client):
    response = client.get("/")

    assert "/login" in response.location

    assert response.status_code == 302



def test_home_after_login(client, user):
    client.post(
        "/login",
        data={
            "login": "emodoh",
            "password": "4199"
        }
    )

    response = client.get("/")

    assert response.status_code == 200

def test_add_expense_page_requires_login(client):
    response = client.get("/add_expense")

    assert response.status_code == 302
    assert response.location.endswith("/login")




def test_add_expense_page_requires_login(client, user):
    response = client.get("/add_expense")

    assert response.status_code == 302
    assert response.location.endswith("/login")

