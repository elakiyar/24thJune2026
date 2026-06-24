from playwright.sync_api import APIRequestContext


def test_create_account(before_each_test: APIRequestContext):
    response = before_each_test.post(
        "/accounts",
        data={"name": "John Doe", "email": "john@example.com", "password": "password123"}
    )

    assert response.status == 201
