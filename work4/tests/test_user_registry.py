from work4.lib.my_requests import MyRequests
from work4.lib.base_case import BaseCase
from work4.lib.assertions import Assertions

class TestUserRegistry(BaseCase):

    def test_create_user_successfully(self):
        data = self.prepare_registartion_data()

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")
        
    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registartion_data(email)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"