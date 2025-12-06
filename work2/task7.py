import requests

#1
response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response.text)

#2
response2 = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response2.text)

#3
payload = {"method": "GET"}
response31 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=payload)
print(response31.text)

response32 = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data ={"method": "POST"})
print(response32.text)

response33 = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data ={"method": "PUT"})
print(response33.text)

response34 = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data ={"method": "DELETE"})
print(response34.text)

#4
methods = ["GET", "POST", "PUT", "DELETE"]  # Список поддерживаемых методов

for real_method in methods:
    for param_value in methods:
        if real_method == 'GET':
            response = requests.request(real_method,
                                        "https://playground.learnqa.ru/ajax/api/compare_query_type",
                                        params={'method': param_value})
        else:
            response = requests.request(real_method,
                                        "https://playground.learnqa.ru/ajax/api/compare_query_type",
                                        data={'method': param_value})

        print(f'Метод запроса: {real_method}, Параметр method: {param_value}')
        print('Ответ:', response.text)
        print()

