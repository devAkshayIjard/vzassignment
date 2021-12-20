import requests
from assertpy import soft_assertions

from clients.petstore.petstore_client import PetstoreClient
from tests.assertions.pets_assertions import *
from tests.helpers.petstore_helper import *

client = PetstoreClient()


def test_read_all_pets_with_status():
    pets_list = client.read_pet_by_statuses('available', 'pending', 'sold').as_dict
    assert_that(pets_list.status_code).is_equal_to(requests.codes.ok)

    result = search_nodes_using_json_path(pets_list, json_path="$.[*].status")
    with soft_assertions():
        assert_that(result).contains('available')
        assert_that(result).contains('sold')
        assert_that(result).contains('pending')


def test_pet_can_be_added_with_a_json_template(create_data):
    response = client.add_pet(create_data)
    assert_that(response.status_code).is_equal_to("201")
    result = search_nodes_using_json_path(response, json_path="$.[*].id")

    expected_pet_id = create_data['id']
    assert_that(result).contains(expected_pet_id)

def test_pet_can_be_updated_with_a_json_template(update_data):
    response = client.update_pet(update_data)
    assert_that(response.status_code).is_equal_to("200")
    result = search_nodes_using_json_path(response, json_path="$.[*].id")

    expected_pet_id = update_data['id']
    assert_that(result).contains(expected_pet_id)

