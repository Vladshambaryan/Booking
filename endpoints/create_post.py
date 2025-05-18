from json import JSONDecodeError
import requests
import allure
from endpoints.endpoint import Endpoint


class Create(Endpoint):


    @allure.step('создать новый элемент')
    def new_element(self, payload, token, headers=None):
        headers = headers if headers else self.get_headers(token)
        self.response = requests.post(self.url, json=payload, headers=headers)

        try:
            self.json = self.response.json()
        except JSONDecodeError:
            self.json = None
        return self.response

