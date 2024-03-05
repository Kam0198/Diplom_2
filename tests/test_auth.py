import pytest
import allure
import requests
from generates.generate_random_string import generate_random_string
from data.handlers import Endpoints


class TestCreateUser:
    email = generate_random_string() + "@ya.ru"
    password = generate_random_string()
    name = generate_random_string()

    @allure.title("Проверка создания пользователя и возвращения правильного код ответа")
    def test_create_user(self):
        payload = {
            "email": self.email,
            "password": self.password,
            "name": self.name
        }
        response = requests.post(Endpoints.create_user_url, data=payload)
        assert response.status_code == 200 and response.json()['success'] is True

    @allure.title("Проверка создания зарегистрированного пользователя и возвращения правильного код ответа")
    def test_create_same_user(self):
        response = None
        payload = {
            "email": self.email,
            "password": self.password,
            "name": self.name
        }
        for i in range(2):
            response = requests.post(Endpoints.create_user_url, data=payload)
        assert response.status_code == 403 and response.json()['success'] is False

    @pytest.mark.parametrize(
        'email, password, name',
        [
            ('', '', ''),
            ('', '15363', 'KAM'),
            ('kam@ya.ru', '', 'Kam'),
            ('kam1@ya.ru', '', '')
        ]
    )
    @allure.title("Проверка создания пользователя без заполнения обязательных полей"
                  " и возвращения правильного код ответа")
    def test_create_user_with_invalid_data(self, email, password, name):
        invalid_data = {'email': email, 'password': password, 'name': name}
        response = requests.post(Endpoints.create_user_url, data=invalid_data)
        assert response.status_code == 403 and response.json()['success'] is False
