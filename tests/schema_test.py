import json

import requests
from assertpy import assert_that, soft_assertions
from cerberus import Validator

from config import BASE_URI

schema = {
    "id": {
        'type': 'number'
    },
    "category": {
        "id": {'type': 'number'},
        "name": {'type': 'string'}
    },
    "name": {'type': 'string'},
    "photoUrls": {
        'type': 'array',
        'items': {
            'type': 'string'
        }
    },
    "tags": {
        'type': 'array',
        'items': {
            "id": {'type': 'number'},
            "name": {'type': 'string'}
        }
    },
    "status": {'type': 'string', 'enum': 'available,pending,sold'}
}


def test_read_all_operation_has_expected_schema():
    response = requests.get(BASE_URI)
    pets = json.loads(response.text)

    validator = Validator(schema, require_all=True)

    with soft_assertions():
        for pet in pets:
            is_valid = validator.validate(pet)
            assert_that(is_valid, description=validator.errors).is_true()
