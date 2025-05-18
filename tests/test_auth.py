import allure
from tests.test_data import invalid_token
import pytest


@pytest.mark.regression
@allure.title("Проверьте авторизацию - токен активен")
def test_get_token(auth):
    auth.authorization_token()
    auth.check_token_not_empty()
    auth.check_authorization_token_is_valid()
    auth.check_status_code_is_correct(status_code=200)


@pytest.mark.regression
@allure.title('Проверить авторизацию – обновить токен')
def test_refresh_token(auth):
    auth.token = invalid_token
    auth.authorization_token()
    auth.check_token_not_empty()
    auth.check_status_code_is_correct(status_code=200)
