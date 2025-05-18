from faker import Faker
fake = Faker()


invalid_token = 'jyrjybubk'
another_user_token = '98in89ily'

valid_data_create = [
    {
        "firstname": fake.name(),
        "lastname": fake.name(),
        "totalprice": 10000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-01-01",
            "checkout": "2025-03-01"
        },
        "additionalneeds": "lanch"
    },
    {
        "firstname": "rafael",
        "lastname": "vladimirovich",
        "totalprice": 9999,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-01-01",
            "checkout": "2025-03-01"
        },
        "additionalneeds": "lanch"
    },
    {
        "firstname": "vlad",
        "lastname": "vladimirovich",
        "totalprice": 468,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-01-01",
            "checkout": "2025-08-01"
        },
        "additionalneeds": "lanch"
    },
    {
        "firstname": "davit",
        "lastname": "vladimirovich",
        "totalprice": 555,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2025-01-12",
            "checkout": "2025-12-01"
        },
        "additionalneeds": "lanch"
    }
]


valid_data_update = {
        "firstname": fake.name(),
        "lastname": "R",
        "totalprice": 100000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-01-01",
            "checkout": "2025-03-01"
        },
        "additionalneeds": "lanch"
    }

invalid_data_create = [
    {
        "firstname": "",
        "lastname": "",
        "totalprice": "",
        "depositpaid": [],
        "bookingdates": [],
        "additionalneeds": {}
    },
    {}
]

invalid_data_update = [
    {
        "firstname": [],
        "lastname": {},
        "totalprice": "",
        "depositpaid": [],
        "bookingdates": [],
        "additionalneeds": {}
    },
    {},
    {
        "firstname": [],
        "lastname": (),
        "totalprice": {},
        "depositpaid": "",
        "bookingdates": True,
        "additionalneeds": ""
    }
]
