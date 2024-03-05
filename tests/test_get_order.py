import allure
import requests
from data.handlers import Endpoints


class TestGetOrders:
    @allure.title("Проверка получения заказов авторизованного пользователя")
    def test_get_orders_authorized_user(self, create_new_user_and_return_email_password):
        email, password, name = create_new_user_and_return_email_password
        payload = {
            "email": email,
            "password": password
        }
        response = requests.post(Endpoints.login_user_url, data=payload)
        token = response.json()['accessToken']
        response = requests.get(Endpoints.get_order_url, headers={
            'Authorization': token})
        assert response.status_code == 200 and 'orders' in response.json()

    @allure.step("Проверка получения заказов неавторизованного пользователя")
    def test_get_orders_an_unauthorized_user(self):
        response = requests.get(Endpoints.get_order_url)
        assert response.status_code == 401 and response.json()['success'] is False