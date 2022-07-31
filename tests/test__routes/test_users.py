import json


def test_create_user(client, normal_user_token_headers):
    data = {
        "email": "obi.kenobi@jedi.order.com",
        "password": "hello-there",
        "code": "20200093",
        "names": "Obi Wan",
        "lastnames": "Kenobi",
        "profile_photo_url": "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/obi-wan-kenobi-1655894421.jpeg?resize=480:*",
        "is_superuser": "true"

    }
    response = client.post("/users/create-user/", json.dumps(data), headers=normal_user_token_headers)
    assert response.status_code == 200
    assert response.json()["email"] == "obi.kenobi@jedi.order.com"
    assert response.json()["is_banned"] == False
