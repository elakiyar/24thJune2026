from playwright.sync_api import APIRequestContext


def test_get_a_product(before_each_test: APIRequestContext):
    response = before_each_test.get("/products/1")

    assert response.status == 200
