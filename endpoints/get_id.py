from endpoints.endpoint import Endpoint
import requests
import allure



class GetElement(Endpoint):

    @allure.step('Получить элемент по id')
    def get_element_by_id(self, new_element_id, token, headers=None):
        headers = headers if headers else self.get_headers(token)
        self.response = requests.get(
            f'{self.url}/{new_element_id}',
            headers=headers
        )
        self.json = self.response.json()
