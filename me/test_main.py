from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_create_exercise():
    response = client.post(
        "/exercises/",
        headers={"X-Token": "testenvtoken"},
        json={"id": 3, "name": "Running", "length": 60},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 3,
        "name": "Running",
        "length": 60,
    }


def test_get_exercise():
    response = client.get(
        "/exercises/2",
        headers={"X-Token": "testenvtoken"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 2,
        "name": "Muay Thai",
        "length": 75
    }
