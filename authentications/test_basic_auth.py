import pytest

from playwright.sync_api import APIRequestContext


@pytest.mark.parametrize(
    "username,password",
    [("username", "password"), ("admin", "password")]
)
def test_basic_auth(before_each_test: APIRequestContext, username: str, password: str):
    response = before_each_test.get(
        "/auth/basic",
        headers={
            "Authorization": "Basic " + (username + ":" + password).encode("utf-8").hex()
        }
    )

    assert response.status == 200
