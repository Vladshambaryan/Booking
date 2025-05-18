import pytest
import allure
from tests.test_data import (NEGATIVE_DATA_CREATE, NEGATIVE_DATA_UPDATE, TEST_DATA_UPDATE)



@allure.feature('Post')
@pytest.mark.regression
@allure.title('Создать новый элемент - негативные тесты')
@pytest.mark.parametrize('data', NEGATIVE_DATA_CREATE)
def test_add_element_with_negative_data(post_create, data, token):
    post_create.new_element(data, token)
    post_create.check_status_code_500_is_bad_request()


@allure.feature('Put')
@pytest.mark.regression
@allure.title('Обновление элемнта - негативный тест')
@pytest.mark.parametrize('data', NEGATIVE_DATA_UPDATE)
def test_update_element_with_negative_data(put_update_element, new_element_id, data, token):
    put_update_element.make_changes_in_element(new_element_id, data, token)
    put_update_element.check_status_code_500_is_bad_request()


@allure.feature('Put')
@pytest.mark.regression
@allure.title('Обновить элемент не авторизованым')
def test_update_element_unauthorized(new_element_id, put_update_element, token_neg):
    data = TEST_DATA_UPDATE
    put_update_element.make_changes_in_element(new_element_id, data, token_neg)
    put_update_element.check_status_code_403_is_unauthorized()



