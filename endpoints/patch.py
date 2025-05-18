from endpoints.endpoint import Endpoint
import requests
import allure


class UpdatePatchElement(Endpoint):

    @allure.step('Обновить элемент')
    def update_test(self, new_element_id, payload, token):
        url = f"{self.url}/{new_element_id}"
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Cookie': f'token={token}'
        }
        self.response = requests.patch(
            url,
            json=payload,
            headers=headers
        )
        try:
            self.json = self.response.json()
        except requests.exceptions.JSONDecodeError:
            self.json = None
        return self.response
