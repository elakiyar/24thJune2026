from playwright.sync_api import APIRequestContext


def test_create_new_order(before_each_test: APIRequestContext):
    response = before_each_test.post(
        "/orders",
        data={"cartId": 1, "customerName": "Jane Doe"}
    )

    assert response.status == 201
