import json


"""

class Bug(Base):
    id = Column(Integer, primary_key=True, index=True)
    day = Column(String)
    hour = Column(String)
    description = Column(String)

"""


def test_create_bug(client):
    data = {
        "day": "Domingo",
        "hour": "17:30",
        "description": "No hay moros en la costa"
    }
    response = client.post("/bugs/create-bug/", json.dumps(data))
    assert  response.status_code == 200
    assert response.json()["day"] == "Domingo"
    assert response.json()["hour"] == "17:30"

def test_read_bug(client):
    data = {
        "day": "Domingo",
        "hour": "17:30",
        "description": "No hay moros en la costa"
    }
    response = client.post("/bugs/create-bug/", json.dumps(data))
    response = client.get("/bugs/get/1")
    assert response.status_code == 200
    assert response.json()["description"] == "No hay moros en la costa"

