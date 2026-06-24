from playwright.sync_api import APIRequestContext


def test_delete_an_item(before_each_test: APIRequestContext):
    response = before_each_test.delete("/carts/1/items/1")

    assert response.status == 200
