def test_login(client, user):
    response = client.post("/login",data={
        "login": "emodoh",
        "password": "4199"
    },
    follow_redirects=True
)

    assert response.status_code == 200
    assert b"Logout" in response.data
    