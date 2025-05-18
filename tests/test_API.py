import pytest
import allure
from tests.test_data import (TEST_DATA_CREATE, NEGATIVE_DATA_CREATE, NEGATIVE_DATA_UPDATE, TEST_DATA_UPDATE, invalid_token)


@allure.feature('Get')
@pytest.mark.smoke
@allure.title('Получите один элемент')
def test_get_one_element(new_element_id, get_request, token):
    response = get_request.get_element_by_id(new_element_id, token)
    if response is not None:
        get_request.check_id_is_correct(response['bookingid'])
        get_request.check_firstname_is_correct(response['firstname'])
        get_request.check_lastname_is_correct(response['lastname'])
        get_request.check_totalprice_is_correct(response['totalprice'])
        get_request.check_depositpaid_is_correct(response['depositpaid'])
        get_request.check_bookingdates_is_correct(response['bookingdates'])
        get_request.check_additionalneeds_is_correct(response['additionalneeds'])
        get_request.check_url_is_correct()
    get_request.check_status_code_is_correct(status_code=200)


@allure.feature('Get')
@pytest.mark.smoke
@allure.title('Получить все элементы')
def test_get_all_element(get_request_all, token):
    response = get_request_all.get_all_element(token)
    if response is not None:
        data_list = response.get('data', [])
        get_request_all.check_response_is_list(data_list)
        for element in data_list:
            get_request_all.check_url_not_empty(element)
            get_request_all.check_id_not_empty(element)
            get_request_all.check_firstname_not_empty(element)
            get_request_all.check_lastname_not_empty(element)
            get_request_all.check_totalprice_not_empty(element)
            get_request_all.check_bookingdates_is_correct(element)
            get_request_all.check_additionalneeds_is_correct(element)
    get_request_all.check_status_code_is_correct(status_code=200)


@allure.feature('Post')
@pytest.mark.regression
@allure.title('Создать новый элемент')
@pytest.mark.parametrize('data', TEST_DATA_CREATE)
def test_add(post_create, data, token):
    post_create.new_element(data, token)
    post_create.check_firstname_is_correct(data['firstname'])
    post_create.check_lastname_is_correct(data['lastname'])
    post_create.check_totalprice_is_correct(data['totalprice'])
    post_create.check_depositpaid_is_correct(data['depositpaid'])
    post_create.check_bookingdates_is_correct(data['bookingdates'])
    post_create.check_additionalneeds_is_correct(data['additionalneeds'])
    post_create.check_status_code_is_correct(status_code=200)


@allure.feature('Post')
@pytest.mark.regression
@allure.title('Создать новый элемент - негативные тесты')
@pytest.mark.parametrize('data', NEGATIVE_DATA_CREATE)
def test_add_element_with_negative_data(post_create, data, token):
    post_create.new_element(data, token)
    post_create.check_status_code_500_is_bad_request()


@allure.feature('Put')
@pytest.mark.regression
@allure.title('Обновить элемент')
def test_update_element(new_element_id, put_update_element, token):
    data = TEST_DATA_UPDATE
    put_update_element.make_changes_in_element(new_element_id, data, token)
    put_update_element.check_firstname_is_correct(data['firstname'])
    put_update_element.check_lastname_is_correct(data['lastname'])
    put_update_element.check_totalprice_is_correct(data['totalprice'])
    put_update_element.check_depositpaid_is_correct(data['depositpaid'])
    put_update_element.check_bookingdates_is_correct(data['bookingdates'])
    put_update_element.check_additionalneeds_is_correct(data['additionalneeds'])
    put_update_element.check_status_code_is_correct(status_code=200)


@allure.feature('Patcht')
@pytest.mark.regression
@allure.title('Частично бновить элемент')
def test_patch_update_element(new_element_id, patch_update, token):
    data = TEST_DATA_UPDATE
    patch_update.update_test(new_element_id, data, token)
    patch_update.check_firstname_is_correct(data['firstname'])
    patch_update.check_lastname_is_correct(data['lastname'])
    patch_update.check_totalprice_is_correct(data['totalprice'])
    patch_update.check_depositpaid_is_correct(data['depositpaid'])
    patch_update.check_bookingdates_is_correct(data['bookingdates'])
    patch_update.check_additionalneeds_is_correct(data['additionalneeds'])
    patch_update.check_status_code_is_correct(status_code=200)


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



@allure.feature('Delete')
@pytest.mark.regression
@allure.title('Удаление элемента')
def test_delete_element(new_element_id, delete, token):
    delete.delete(new_element_id, token)
    delete.check_status_code_201_200_204()
    delete.delete(new_element_id, token)
    delete.check_status_code_405()


