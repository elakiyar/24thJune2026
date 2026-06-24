import requests


def test_status():
    response = requests.get("https://simple-grocery-store-api.click/status")
    assert response.status_code == 200
    assert response.json()["status"] == "UP"
