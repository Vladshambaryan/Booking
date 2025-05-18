import requests
import allure
from endpoints.endpoint import Endpoint


class DeleteElement(Endpoint):

    @allure.step('Удалить элемент')
    def delete_element(self, new_element_id, token):
        url = f"{self.url}/{new_element_id}"
        headers = {
            'Content-Type': 'application/json',
            'Cookie': f'token={token}'
        }
        self.response = requests.delete(url, headers=headers)
        print(f"Удалён элемент с ID: {new_element_id}")

    @allure.step('Проверяет код состояния 201, 200, 204')
    def check_status_code_201_200_204(self):
        assert self.response.status_code in [201, 200, 204], "Удаление не удалось"
        print(self.response.text)
        print(self.response.status_code)
