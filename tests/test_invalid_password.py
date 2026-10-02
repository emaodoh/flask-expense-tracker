def test_invalid_password(client,user):
    response = client.post("/login",
    data={
        "login":"emodoh",
        "password": "wrongpassword"
    },
    follow_redirects=True
    )

    assert response.status_code == 200
    assert b"Invalid username/email or password." in response.data

#     Next we'll write tests for:

# Invalid password
# Unknown username/email
# Logout
# Protected routes
# Session handling