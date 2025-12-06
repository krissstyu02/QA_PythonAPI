import requests
import  json
import time

#1
response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
print(response.text)
obj = json.loads(response.text)
token = obj["token"]
seconds = int(obj["seconds"])
#2
payload = {"token": token}
response2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=payload)
print(response2.text)

#3
time.sleep(seconds)
payload = {"token": token}
response3 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=payload)
print(response3.text)

data_after_waiting = response3.json()

# Проверка статуса задачи ПОСЛЕ готовности
try:
    assert data_after_waiting['status'] == 'Job is ready', f"Ошибка: После ожидания статус не 'Job is ready'"
    print("Статус задачи после ожидания верен.")
except AssertionError as e:
    print(e)

# Проверка наличия поля result
try:
    assert 'result' in data_after_waiting, f"Ошибка: Отсутствует поле 'result' в ответе"
    print("Поле 'result' присутствует в ответе.")
except AssertionError as e:
    print(e)