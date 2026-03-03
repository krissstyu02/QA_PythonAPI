import requests


class TestHomeworkCookie:

    def test_homework_cookie(self):
        url = "https://playground.learnqa.ru/api/homework_cookie"
        response = requests.get(url)

        # Получаем все cookie
        cookies = response.cookies
        print(cookies)

        # Получаем конкретную cookie по имени
        cookie_name = list(cookies.keys())[0]
        cookie_value = cookies.get(cookie_name)

        print(f"Cookie name: {cookie_name}")
        print(f"Cookie value: {cookie_value}")

        # Фиксируем поведение
        assert cookie_name == "HomeWork", "Unexpected cookie name"
        assert cookie_value == "hw_value", "Unexpected cookie value"