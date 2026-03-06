import datetime
import os

from requests import Response


class Logger:
    base_dir = os.path.dirname(os.path.dirname(__file__))
    logs_dir = os.path.join(base_dir, "logs")

    os.makedirs(logs_dir, exist_ok=True)

    file_name = os.path.join(
        logs_dir,
        "log_" + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".log"
    )

    @classmethod
    def _write_log_to_file(cls, data: str):
        with open(cls.file_name, 'a', encoding='utf-8') as logger_file:
            logger_file.write(data)

    @classmethod
    def add_request(cls, url: str, data: dict, headers: dict, cookies: dict, method: str):
        testName = os.environ.get('PYTEST_CURRENT_TEST')

        data_to_add = f"\n-----\n"
        data_to_add += f"Test: {testName}\n"
        data_to_add += f"Time: {str(datetime.datetime.now())}\n"
        data_to_add += f"Request method: {method}\n"
        data_to_add += f"Request URL: {url}\n"
        data_to_add += f"Request data: {data}\n"
        data_to_add += f"Request headers: {headers}\n"
        data_to_add += f"Request cookies: {cookies}\n"
        data_to_add += "\n"
        cls._write_log_to_file(data_to_add)

    @classmethod
    def add_response(cls, response: Response):
        cookies_as_dict = dict(response.cookies)
        headers_as_dict = dict(response.headers)

        data_to_add = f"Response code : {response.status_code}\n"
        data_to_add += f"Response text : {response.text}\n"
        data_to_add += f"Response header : {headers_as_dict}\n"
        data_to_add += f"Response cookie : {cookies_as_dict}\n"
        data_to_add = f"\n-----\n"

        cls._write_log_to_file(data_to_add)
