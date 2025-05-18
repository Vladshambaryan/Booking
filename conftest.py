import pytest
import requests

from endpoints.authorize import Authorization
from endpoints.create_post import Create
from endpoints.put import UpdateElement
from endpoints.patch import UpdatePatchElement
from endpoints.get_id import GetElement
from endpoints.get_all import GetAll
from endpoints.delete import DeleteElement


@pytest.fixture(scope='session')
def auth():
    return Authorization()


@pytest.fixture(scope='session')
def token(auth):
    return auth.authorization_token()


@pytest.fixture(scope='session')
def token_neg(auth):
    return auth.authorization_token_is_not_valid()

@pytest.fixture()
def post_create():
    return Create()


@pytest.fixture()
def put_update_element():
    return UpdateElement()


@pytest.fixture()
def patch_update():
    return UpdatePatchElement()

@pytest.fixture()
def get_request():
    return GetElement()


@pytest.fixture()
def get_request_all():
    return GetAll()


@pytest.fixture()
def delete():
    return DeleteElement()


@pytest.fixture()
def new_element_id(post_create, delete, token):
    url = f"https://restful-booker.herokuapp.com/booking"
    payload = {
        "firstname": "V",
        "lastname": "sh",
        "totalprice": 10000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-01-01",
            "checkout": "2025-03-01"
        },
        "additionalneeds": "lunch"
    }
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Cookie': f'token={token}'
    }
    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 200, "Создание объекта не удалось"
    object_id = response.json()["bookingid"]
    yield object_id


