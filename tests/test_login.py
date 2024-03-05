import allure
import requests
from data.handlers import Endpoints
from generates.generate_random_string import generate_random_string


class TestLoginUser:
    email = generate_random_string() + "@ya.ru"
    password = generate_random_string()
    name = generate_random_string()

    @allure.title("Проверка авторизации под существующим пользователем и возвращения правильного код ответа")
    def test_login_user(self, create_new_user_and_return_email_password):
        email, password, name = create_new_user_and_return_email_password
        payload = {
            "email": email,
            "password": password
        }
        response = requests.post(Endpoints.login_user_url, data=payload)
        assert response.status_code == 200 and response.json()['success'] is True

    @allure.title("Проверка авторизации с невалидными данными и возвращения правильного код ответа")
    def test_login_user_false(self):

        payload = {
            "email": 'k',
            "password": 'k'
        }
        response = requests.post(Endpoints.login_user_url, data=payload)
        assert response.status_code == 401 and response.json()['success'] is False