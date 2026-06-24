from playwright.sync_api import APIRequestContext


def test_add_an_item(before_each_test: APIRequestContext):
    response = before_each_test.post(
        "/carts/1/items",
        data={"productId": 4643, "quantity": 2}
    )

    assert response.status == 200
