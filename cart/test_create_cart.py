from playwright.sync_api import APIRequestContext


def test_create_cart(before_each_test: APIRequestContext):
    response = before_each_test.post("/carts")
    response_json = response.json()

    assert response.status == 201
    assert response_json["message"] == "Cart created"
