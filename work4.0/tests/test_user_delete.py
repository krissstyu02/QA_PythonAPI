from work4.lib.my_requests import MyRequests
from work4.lib.base_case import BaseCase
from work4.lib.assertions import Assertions


class TestUserDelete(BaseCase):

    def setup_method(self, method):
        # REGISTER
        register_data = self.prepare_registartion_data()
        response1 = MyRequests.post("/user/", data=register_data)

        self.another_user_id = self.get_json_value(response1, "id")

    def test_delete_just_created_user(self):
        # REGISTER
        register_data = self.prepare_registartion_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data["email"]
        password = register_data["password"]
        user_id = self.get_json_value(response1, "id")

        # AUTHORIZATION
        login_data = {
            'email': email,
            'password': password,
        }
        response2 = MyRequests.post("/user/login", data=login_data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # DELETE

        response3 = MyRequests.delete(f"/user/{user_id}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid}
                                   )

        Assertions.assert_code_status(response3, 200)

        # GET
        response4 = MyRequests.get(f"/user/{user_id}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid})

        Assertions.assert_code_status(response4, 404)

    def test_delete_another_user(self):
        # REGISTER
        register_data = self.prepare_registartion_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data["email"]
        password = register_data["password"]
        user_id = self.get_json_value(response1, "id")

        # AUTHORIZATION
        login_data = {
            'email': email,
            'password': password,
        }
        response2 = MyRequests.post("/user/login", data=login_data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # DELETE

        response3 = MyRequests.delete(f"/user/{self.another_user_id}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid}
                                   )

        Assertions.assert_code_status(response3, 400)
        Assertions.assert_json_has_key(response3, "error")


    def test_delete_user_with_id_2(self):
        # AUTHORIZATION
        login_data = {

            'email': 'vinkotov@example.com',

            'password': '1234'

        }
        response2 = MyRequests.post("/user/login", data=login_data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # DELETE

        response3 = MyRequests.delete(f"/user/2",
                                      headers={"x-csrf-token": token},
                                      cookies={"auth_sid": auth_sid}
                                      )

        Assertions.assert_code_status(response3, 400)
        # print(response3.text)
        Assertions.assert_json_value_by_name(response3, "error", "Please, do not delete test users with ID 1, 2, 3, 4 or 5.", "Wrong error")
