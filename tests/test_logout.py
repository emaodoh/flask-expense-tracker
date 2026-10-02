def test_logout(client):
    client.post(
    "/login",
    data={
        "login": "emodoh",
        "password": "4199"
    }
)
    response = client.get("/logout")
    with client.session_transaction() as session:
        assert "user_id" not in session


    assert response.status_code == 302
    assert response.location.endswith("/login")