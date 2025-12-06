import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)

num_redirects = len(response.history)

print(response.history)
print(num_redirects)
print(response.url)

