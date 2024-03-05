import allure
import requests
from data.handlers import Endpoints


class TestChangeUserData:
    @allure.title("Проверка изменения данных пользователя с авторизацией"
                  " и возвращения правильного код ответа")
    def test_change_data_with_authorization(self, create_new_user_and_return_email_password):
        email, password, name = create_new_user_and_return_email_password
        payload = {
            "email": email,
            "password": password
        }
        response = requests.post(Endpoints.login_user_url, data=payload)
        token = response.json()['accessToken']
        payload = {
            "email": email,
            "name": "Kamiiiillla"
        }
        response = requests.patch(Endpoints.delete_user_url, headers={'Authorization': token}, data=payload)
        assert response.status_code == 200 and response.json()['success'] is True

    @allure.title("Проверка изменения данных пользователя без авторизации"
                  " и возвращения правильного код ответа")
    def test_change_data_without_authorization(self):
        payload = {
            "email": "kam-ya@ya.ru",
            "name": "Kamm"
        }
        response = requests.patch(Endpoints.delete_user_url, data=payload)
        assert response.status_code == 401 and response.json()['success'] is False