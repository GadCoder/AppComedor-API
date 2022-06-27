import json


def test_create_user(client):
    data = {
        "email": "obiwan.kenobi@jedi.order.com",
        "password": "high_ground",
        "code": "20200093",
        "names": "Obi Wan",
        "lastnames": "Kenobi"

    }
    response = client.post("/users/create-user/", json.dumps(data))
    assert response.status_code == 200
    assert response.json()["email"] == "obiwan.kenobi@jedi.order.com"
    assert response.json()["is_banned"] == False






