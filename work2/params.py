import requests
from json.decoder import JSONDecodeError

from work1.requests_lab import response

# #params GET
# payload = {"name": "User"}
# response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
#
# #parsed json
# parsed_response_text = response.json()
# print(parsed_response_text["answer"])
#
# #parsed text
# response = requests.get('https://playground.learnqa.ru/api/get_text')
# print(response.text)
#
# try:
#     parsed_response_text = response.json()
#     print(parsed_response_text)
# except JSONDecodeError:
#     print("JSON decode error")
#
# #type and params
#
# response= requests.post('https://playground.learnqa.ru/api/check_type', data={"param1":"value1"})
# print(response.text)
#
# #server code
#
# #200
# response= requests.post('https://playground.learnqa.ru/api/check_type')
# print(response.status_code)
#
# #500
# response= requests.post('https://playground.learnqa.ru/api/get_500')
# print(response.status_code)
# print(response.text)
#
# #404
# response= requests.post('https://playground.learnqa.ru/api/something')
# print(response.status_code)
# print(response.text)

#301
# response= requests.post('https://playground.learnqa.ru/api/get_301', allow_redirects=True)
#
# first_response = response.history[0]
# second_response = response
#
# print(first_response.url)
# print(second_response.url)
# print(response.status_code)

#headers

headers = {"some_header":"123"}
response= requests.get("https://playground.learnqa.ru/api/show_all_headers", headers=headers)
print(response.text)
print(response.headers)






