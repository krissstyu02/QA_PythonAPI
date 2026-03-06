import pytest
import requests


class TestUserAuth:
    exclude_params = [
        ("no_cookie"),
        ("no_token")
    ]

    def setup_method(self, method):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)

        assert "auth_sid" in response1.cookies, "There is no auth cookie in the response"
        assert "x-csrf-token" in response1.headers, "There is no CSRF token header in the response"
        assert "user_id" in response1.json(), "There is no user id header in the response"

        self.auth_sid = response1.cookies.get("auth_sid")
        self.token = response1.headers.get("x-csrf-token")
        self.user_id_from_auth_method = response1.json()["user_id"]

    def test_auth_user(self):

        url2 = "https://playground.learnqa.ru/api/user/auth"

        response2 = requests.get(url2, headers={"x-csrf-token": self.token},
                                 cookies={"auth_sid": self.auth_sid})
        assert "user_id" in response2.json(), "There is no user id in the second response"
        user_id_from_check_method = response2.json()["user_id"]

        assert self.user_id_from_auth_method == user_id_from_check_method, "User id from auth method is not equal for user_id in check_method"

    @pytest.mark.parametrize('condition', exclude_params)
    def test_negative_auth_check(self, condition):
        url2 = "https://playground.learnqa.ru/api/user/auth"

        if condition == 'no_cookie':
            response2 = requests.get(url2, headers={"x-csrf-token": self.token})
        else:
            response2 = requests.get(url2, cookies={"auth_sid": self.auth_sid})

        assert "user_id" in response2.json(), "There is no user id in the second response"
        user_id_from_check_method = response2.json()["user_id"]

        assert 0 == user_id_from_check_method, f"User is authorized with condition {condition}"
