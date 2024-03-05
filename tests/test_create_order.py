import allure
import requests
from data.handlers import Endpoints


class TestCreateOrder:

    @allure.title("Проверка создания заказа с авторизацией и с ингредиентами"
                  " и возвращения правильного код ответа")
    def test_create_order_with_authorization(self, create_new_user_and_return_email_password):
        email, password, name = create_new_user_and_return_email_password
        payload = {
            "email": email,
            "password": password
        }
        response = requests.post(Endpoints.login_user_url, data=payload)
        token = response.json()['accessToken']
        payload = {
            "ingredients": ["61c0c5a71d1f82001bdaaa70"]
        }
        response = requests.post(Endpoints.create_order_url, headers={
            'Authorization': token}, data=payload)
        assert response.status_code == 200 and 'order' in response.json()

    @allure.title("Проверка создания заказа без авторизации и возвращения правильного код ответа")
    def test_create_order_without_authorization(self):
        payload = {
            "ingredients": ["61c0c5a71d1f82001bdaaa70"]
        }
        response = requests.post(Endpoints.create_order_url, data=payload)
        assert response.status_code == 200 and 'order' in response.json()

    @allure.title("Проверка создания заказа без ингредиентов")
    def test_create_order_without_ingredients(self, create_new_user_and_return_email_password):
        email, password, name = create_new_user_and_return_email_password
        payload = {
            "email": email,
            "password": password
        }
        response = requests.post(Endpoints.login_user_url, data=payload)
        token = response.json()['accessToken']
        payload = {}
        response = requests.post(Endpoints.create_order_url, headers={
            'Authorization': token}, data=payload)
        assert response.status_code == 400 and response.json()['success'] is False

    @allure.title("Проверка создания заказа с неверным хэшем ингредиентов"
                  " и возвращения правильного код ответа")
    def test_create_order_with_invalid_ingredients(self):
        payload = {
            "ingredients": ["61c0c5a71d1f82001bdaaa6y"]
        }
        response = requests.post(Endpoints.create_order_url, data=payload)
        assert response.status_code == 500