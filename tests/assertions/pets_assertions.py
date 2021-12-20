from assertpy import assert_that


def assert_pet_is_present(response, pet_id):
    assert_that(response.as_dict).extracting('id').is_not_empty().contains(pet_id)
