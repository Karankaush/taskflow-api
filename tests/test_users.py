def test_create_user(client):
    response = client.post(
        "/users/",
        json={
            "name": "Karan",
            "email": "pytest@example.com",
            "password": "test123",
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == "Karan"
    assert data["email"] == "pytest@example.com"
    assert "password" not in data