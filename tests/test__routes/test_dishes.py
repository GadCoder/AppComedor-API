import json


def test_create_dish(client, normal_user_token_headers):
    data = {
        "name": "Rico Rico",
        "img_url": "https://buenazo.cronosmedia.glr.pe/original/2020/09/03/5f51358bbd2a9425f715cb78.jpg",
        "score": 4.0
    }
    response = client.post("/dishes/create-dish/", json.dumps(data), headers=normal_user_token_headers)
    assert response.status_code == 200
    assert response.json()["name"] == "Rico Rico"
    assert response.json()["score"] == 4.0


def test_read_dish(client, normal_user_token_headers):
    data = {
        "name": "Rico Rico",
        "img_url": "https://buenazo.cronosmedia.glr.pe/original/2020/09/03/5f51358bbd2a9425f715cb78.jpg",
        "score": 4.0
    }
    response = client.post("/dishes/create-dish/", json.dumps(data),headers=normal_user_token_headers)
    response = client.get("/dishes/get/1/")
    assert response.status_code == 200
    assert response.json()["name"] == "Rico Rico"
