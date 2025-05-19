import pytest
import allure
from endpoints.data import (invalid_data_create, invalid_data_update)


@allure.feature('Post')
@pytest.mark.regression
@allure.title('Создать новый элемент - негативные тесты')
@pytest.mark.parametrize('data', invalid_data_create)
def test_add_element_with_negative_data(post_create, data, token):
    post_create.new_element(data, token)
    post_create.check_status_code_400_is_bad_request()


@allure.feature('Put')
@pytest.mark.regression
@allure.title('Обновление элемнта - негативный тест')
@pytest.mark.parametrize('data', invalid_data_update)
def test_update_element_with_negative_data(put_update_element, new_element_id, data, token):
    put_update_element.make_changes_in_element(new_element_id, data, token)
    put_update_element.check_status_code_400_is_bad_request()


@allure.feature('Put')
@pytest.mark.regression
@allure.title('Обновить элемент не авторизованым')
def test_update_element_unauthorized(new_element_id, put_update_element, token_neg):
    data = invalid_data_update
    put_update_element.make_changes_in_element(new_element_id, data, token_neg)
    put_update_element.check_status_code_403_is_unauthorized()
