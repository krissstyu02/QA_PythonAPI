import pytest
from work4.lib.base_case import BaseCase
from work4.lib.assertions import Assertions
from work4.lib.my_requests import MyRequests


class TestUserAuth(BaseCase):

    exclude_params=[
            ("no_cookie"),
            ("no_token")
    ]

    def setup_method(self, method):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = MyRequests.post("/user/login", data=data)

        self.auth_sid = self.get_cookie(response1, "auth_sid")
        self.token = self.get_header(response1, "x-csrf-token")
        self.user_id_from_auth_method = self.get_json_value(response1, "user_id")

    def test_auth_user(self):

        response2 = MyRequests.get("/user/auth", headers={"x-csrf-token": self.token},
                                 cookies={"auth_sid": self.auth_sid})

        Assertions.assert_json_value_by_name(response2, "user_id", self.user_id_from_auth_method, "User id from auth method is not equal to user_id from check method")

    @pytest.mark.parametrize('condition', exclude_params)
    def test_negative_auth_check(self, condition):
            url2 = "/user/auth"

            if condition == 'no_cookie':
                response2 = MyRequests.get(url2, headers={"x-csrf-token": self.token})
            else :
                response2 = MyRequests.get(url2, cookies={"auth_sid": self.auth_sid})

            Assertions.assert_json_value_by_name(response2, "user_id", 0,
                                                 "User id from auth method is not equal to user_id from check method")