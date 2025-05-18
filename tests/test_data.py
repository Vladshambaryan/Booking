invalid_token = 'jyrjybubk'
another_user_token = '98in89ily'

TEST_DATA_CREATE = [
    {
        "firstname": "miqo",
        "lastname": "vladimirovich",
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


TEST_DATA_UPDATE = {
        "firstname": "M",
        "lastname": "R",
        "totalprice": 100000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-01-01",
            "checkout": "2025-03-01"
        },
        "additionalneeds": "lanch"
    }

NEGATIVE_DATA_CREATE = [
    {
        "firstname": ['Vl'],
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
        "firstname": "vlad",
        "lastname": ("vladimirovich", 777),
        "totalprice": 468,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-01-01",
            "checkout": "2025-08-01"
        },
        "additionalneeds": "lanch"
    },
    {
        "firstname": 55,
        "lastname": ["vladimirovich"],
        "totalprice": 468,
        "depositpaid": True,
        "bookingdates": {
            "checkin": 76476,
            "checkout": 'ghggghh'
        },
        "additionalneeds": "lanch"
    }
]

NEGATIVE_DATA_UPDATE = [
    {
        "firstname": ("vlad", True),
        "lastname": ("vladimirovich", 777),
        "totalprice": 468,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-01-01",
            "checkout": "2025-08-01"
        },
        "additionalneeds": "lanch"
    },
    {
        "firstname": "vlad",
        "lastname": ("vladimirovich", 777),
        "totalprice": 468,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-01-01",
            "checkout": "2025-08-01"
        },
        "additionalneeds": "lanch"
    },
    {
        "firstname": '55',
        "lastname": ["vladimirovich"],
        "totalprice": 468,
        "depositpaid": True,
        "bookingdates": {
            "checkin": 76476,
            "checkout": 'ghggghh'
        },
        "additionalneeds": "lanch"
    }
]
