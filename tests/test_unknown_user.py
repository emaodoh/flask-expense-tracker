def test_unknown_user(client,user):
    response = client.post("/login",
    data={
        "login":"unknown",
        "password": "4199"
    },
    follow_redirects=True
    )

    assert response.status_code == 200
    assert b"Invalid username/email or password." in response.data
