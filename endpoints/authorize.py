import allure
import requests
from endpoints.endpoint import Endpoint


class Authorization(Endpoint):
    @allure.step('Получить новый токен')
    def authorization_token(self):
        if self.token is None or not self.is_token_alive(self.token):
            response = requests.post(self.auth_url, json={
                "username": "admin",
                "password": "password123"
            })
            self.response = response
            self.token = response.json().get('token')
            # print(response.text)
        return self.token

    @allure.step('Проверить истёк ли срок действия токена')
    def authorization_token_is_not_valid(self):
        if self.token is None or not self.is_token_alive(self.token):
            response = requests.post(self.auth_url, json={
                "username": "admin",
                "password": "password123"
            })
            self.response = response
            self.token = response.json().get('token')
            # print(response.text)
        return self.token

