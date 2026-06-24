from playwright.sync_api import APIRequestContext


def test_api_key_auth(before_each_test: APIRequestContext):
    response = before_each_test.get(
        "/auth/api-key",
        headers={"x-api-key": "123456"}
    )

    assert response.status == 200
