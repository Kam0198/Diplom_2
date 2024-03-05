import pytest
import requests
from data.handlers import Endpoints
from generates.generate_random_string import generate_random_string


@pytest.fixture(scope="function")
def create_new_user_and_return_email_password():
    # создаём список, чтобы метод мог его вернуть
    email_pass = []

    # генерируем логин, пароль и имя курьера
    email = generate_random_string() + "@ya.ru"
    password = generate_random_string()
    name = generate_random_string()

    # собираем тело запроса
    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post(Endpoints.create_user_url, data=payload)

    email_pass.append(email)
    email_pass.append(password)
    email_pass.append(name)

    yield email_pass

    token = response.json()['accessToken']
    requests.delete(Endpoints.delete_user_url, headers={
        'Authorization': token}, data=payload)