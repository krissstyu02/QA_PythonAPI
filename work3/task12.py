import requests


class TestHomeworkHeaders:

    def test_homework_header(self):
        url = "https://playground.learnqa.ru/api/homework_header"
        response = requests.get(url)
        headers = response.json()

        print("Headers=", headers)

        header_name = list(headers.keys())[0]
        header_value = headers.get(header_name)

        print(f"Cookie name: {header_name}")
        print(f"Cookie value: {header_value}")
        #
        # # Фиксируем поведение
        assert header_name == "success", "Unexpected header name"
        assert header_value == "!", "Unexpected header value"