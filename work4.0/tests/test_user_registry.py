from work4.lib.my_requests import MyRequests
from work4.lib.base_case import BaseCase
from work4.lib.assertions import Assertions
import random
import string
import pytest
import allure
from allure_commons.types import Severity


@allure.epic("Registry cases")
class TestUserRegister(BaseCase):

    @allure.tag("positive")
    @allure.severity(Severity.CRITICAL)
    def test_create_user_successfully(self):
        data = self.prepare_registartion_data()

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    @allure.tag("negative")
    @allure.severity(Severity.CRITICAL)
    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registartion_data(email)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"

    @allure.tag("negative")
    @allure.severity(Severity.NORMAL)
    def test_create_user_with_not_valid_email(self):
        email = 'vinkotovexample.com'
        data = self.prepare_registartion_data(email)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"Invalid email format"

    @allure.tag("negative")
    @allure.severity(Severity.NORMAL)
    def test_create_user_with_short_name(self):
        name = ''.join(random.choices(string.ascii_letters, k=1))
        data = self.prepare_registartion_data(name=name)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"The value of 'username' field is too short"

    @allure.tag("negative")
    @allure.severity(Severity.NORMAL)
    def test_create_user_with_long_name(self):
        name = ''.join(random.choices(string.ascii_letters, k=251))
        data = self.prepare_registartion_data(name=name)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"The value of 'username' field is too long"

    @pytest.mark.parametrize(
        "field",
        ["email","lastName","firstName","username","password"]
    )
    @allure.tag("negative")
    @allure.severity(Severity.CRITICAL)
    def test_create_user_without_field(self, field):
        data = self.prepare_registartion_data()

        data[field] = None
        data.pop(field)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"The following required params are missed: {field}"
