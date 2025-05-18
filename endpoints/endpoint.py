
import allure
import requests


class Endpoint:

    url = "https://restful-booker.herokuapp.com/booking"
    auth_url = "https://restful-booker.herokuapp.com/auth"
    response = None
    json = None
    errors = []
    token = None
    auth = None

    def get_headers(self, token=None):
        if token is None:
            token = self.auth.authorization_token()
        return {
            'Content-Type': 'application/json',
            'Authorization': f'{token}'
        }

    @allure.step('Проверить токен не пуст')
    def check_token_not_empty(self):
        print(self.response.text)
        assert self.token is not None

    @allure.step('Проверить токен просрочен')
    def is_token_alive(self, token):
        response = requests.get(f'{self.auth_url}/{token}')
        self.response = response
        return response.status_code == 200

    @allure.step('Проверяет код состояния 200')
    def check_status_code_is_correct(self, status_code):
        # print(self.response.text)
        # print(self.response.status_code)
        assert self.response.status_code == status_code

    @allure.step('Проверяет код состояния 405')
    def check_status_code_405(self):

        assert self.response.status_code == 405

    @allure.step('Проверяет код состояния 404')
    def check_status_code_404(self):
        # print(self.response.text)
        # print(self.response.status_code)
        assert self.response.status_code == 404

    @allure.step('Проверяет код состояния 400')
    def check_status_code_400_is_bad_request(self):
        # print(self.response.status_code)
        assert self.response.status_code == 400

    @allure.step('Проверяет код состояния 500')
    def check_status_code_500_is_bad_request(self):
        # print(self.response.status_code)
        # print(self.response.text)
        assert self.response.status_code == 500

    @allure.step('Проверяет код состояния 403')
    def check_status_code_403_is_unauthorized(self):
        # print(self.response.text)
        # print(self.response.status_code)
        assert self.response.status_code == 403

    @allure.step('Проверяет firstname')
    def check_firstname_is_correct(self, firstname):
        assert self.json is not None
        if 'booking' in self.json:
            actual_firstname = self.json['booking']['firstname']
        else:
            actual_firstname = self.json['firstname']
        assert actual_firstname == firstname

    @allure.step('Проверяет firstname')
    def check_firstname_is_correct(self, firstname):
        assert self.json is not None
        if 'booking' in self.json:
            actual = self.json['booking'].get('firstname')
        else:
            actual = self.json.get('firstname')
        assert actual == firstname

    @allure.step('Проверяет lastname')
    def check_lastname_is_correct(self, lastname):
        assert self.json is not None
        if 'booking' in self.json:
            actual = self.json['booking'].get('lastname')
        else:
            actual = self.json.get('lastname')
        assert actual == lastname

    @allure.step('Проверяет totalprice')
    def check_totalprice_is_correct(self, totalprice):
        assert self.json is not None
        if 'booking' in self.json:
            actual = self.json['booking'].get('totalprice')
        else:
            actual = self.json.get('totalprice')
        assert actual == totalprice

    @allure.step('Проверяет depositpaid')
    def check_depositpaid_is_correct(self, depositpaid):
        assert self.json is not None
        if 'booking' in self.json:
            actual = self.json['booking'].get('depositpaid')
        else:
            actual = self.json.get('depositpaid')
        assert actual == depositpaid

    @allure.step('Проверяет bookingdates')
    def check_bookingdates_is_correct(self, bookingdates):
        assert self.json is not None
        if 'booking' in self.json:
            actual = self.json['booking'].get('bookingdates')
        else:
            actual = self.json.get('bookingdates')
        assert actual == bookingdates

    @allure.step('Проверяет additionalneeds')
    def check_additionalneeds_is_correct(self, additionalneeds):
        assert self.json is not None
        if 'booking' in self.json:
            actual = self.json['booking'].get('additionalneeds')
        else:
            actual = self.json.get('additionalneeds')
        assert actual == additionalneeds

    @allure.step('Проверяет url')
    def check_url_is_correct(self, url):
        assert self.json is not None and self.json['url'] == url

    @allure.step('Проверяет id')
    def check_id_is_correct(self, element_id):
        assert self.json is not None and self.json['bookingid'] == element_id

    @allure.step('bookingid чека не пуст')
    def check_id_not_empty(self, element):
        assert self.json is not None and isinstance(element, dict)
        id_element = element.get('bookingid', '')
        if not id:
            self.errors.append(f"bookingid в элементе поле пусто: {id_element}")

    @allure.step('firstname проверки не пуст')
    def check_firstname_not_empty(self, element):
        assert self.json is not None and isinstance(element, dict)
        text = element.get('firstname', '')
        if not text:
            self.errors.append(f"firstname в элементе поле пусто: {element}")

    @allure.step('Проверяет URL-адрес не пуст')
    def check_url_not_empty(self, element):
        assert self.json is not None and isinstance(element, dict)
        url = element.get('url', '')
        if not url:
            self.errors.append(f"URL в элементе поле пусто: {element}")

    @allure.step('Проверяет lastname не пусто')
    def check_lastname_not_empty(self, element):
        assert self.json is not None and isinstance(element, dict)
        tags = element.get('lastname', '')
        if not tags:
            self.errors.append(f"lastname в элементе поле пусто: {element}")

    @allure.step('Проверяет bookingdates не пусто')
    def check_bookingdates_is_correct(self, element):
        assert self.json is not None and isinstance(element, dict)
        tags = element.get('bookingdates', '')
        if not tags:
            self.errors.append(f"bookingdates в элементе поле пусто: {element}")

    @allure.step('Проверяет bookingdates не пусто')
    def check_bookingdates_is_correct(self, element):
        assert self.json is not None and isinstance(element, dict)
        tags = element.get('bookingdates', '')
        if not tags:
            self.errors.append(f"bookingdates в элементе поле пусто: {element}")

    @allure.step('Проверяет additionalneeds не пуста')
    def check_additionalneeds_not_empty(self, element):
        assert self.json is not None and isinstance(element, dict)
        info = element.get('additionalneeds', '')
        if not info:
            self.errors.append(f"additionalneeds в элементе поле пусто: {element}")
