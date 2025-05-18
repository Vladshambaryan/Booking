from endpoints.endpoint import Endpoint
import requests
import allure


class GetAll(Endpoint):

    @allure.step('Проверяет получить все элемент')
    def get_all_element(self, token, headers=None):
        headers = headers if headers else self.get_headers(token)
        self.response = requests.get(
            f'{self.url}',
            headers=headers
        )
        self.json = self.response.json()


    @allure.step('Проверьте ответ в виде списка')
    def check_response_is_list(self, data):
        assert self.json is not None and isinstance(data, list)
