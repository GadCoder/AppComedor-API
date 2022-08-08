import json

def test_create_ticket(client):
    data = {
        "ticket_id": 1,
        "code": "20200023",
        "shift": "1",
        "hour": "Lunes - 09:03:00",
        "is_scanned": False
    }
    response = client.post("/tickets/create-ticket", json.dumps(data))
    assert response.status_code == 200
    assert response.json()["ticket"] == 1
    assert response.json()["code"] == "20200023"
    assert response.json()["shift"] == "1"
    assert response.json()["hour"] == "Lunes - 09:03:00"
    assert response.json()["is_scanned"] == False

def test_read_ticket(client):
    data = {
        "ticket_id": 1,
        "code": "20200023",
        "shift": "1",
        "hour": "Lunes - 09:03:00",
        "is_scanned": False
    }
    response = client.post("/tickets/create-ticket", json.dumps(data))
    response = client.get("/tickets/get/1")
    assert response.status_code == 200
    assert response.json()["ticket"] == 1
    assert response.json()["code"] == "20200023"
    assert response.json()["shift"] == "1"
    assert response.json()["hour"] == "Lunes - 09:03:00"
    assert response.json()["is_scanned"] == False