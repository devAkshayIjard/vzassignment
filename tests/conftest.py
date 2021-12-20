import random
from faker import Faker
from faker.providers import lorem, internet, DynamicProvider

import pytest

from utils.file_reader import read_file

pet_status_provider = DynamicProvider(
    provider_name="pet_status",
    elements=["available", "pending", "sold"],
)


@pytest.fixture
def create_data():
    fake = Faker(['en_US'])

    fake.add_provider(lorem)
    fake.add_provider(internet)

    payload = read_file('createPet.json')

    pet_id = random.randint(0, 1000)
    photo_url = fake.image_url()
    category_id = random.randint(0, 1000)
    tag_id = random.randint(0, 1000)

    tag_name = fake.sentence(nb_words=5)
    category_name = fake.sentence(nb_words=5)

    fake.add_provider(pet_status_provider)
    pet_status = fake.pet_status()

    payload['photoUrls'][0] = photo_url
    payload['id'] = pet_id
    payload['category']['id'] = category_id
    payload['category']['name'] = category_name
    payload['tag'][0]['id'] = tag_id
    payload['tag'][0]['name'] = tag_name
    payload['status'] = pet_status

    yield payload

@pytest.fixture
def update_data():
    fake = Faker(['en_US'])

    fake.add_provider(lorem)
    fake.add_provider(internet)

    payload = read_file('updatePet.json')

    pet_id = random.randint(0, 1000)
    photo_url = fake.image_url()
    category_id = random.randint(0, 1000)
    tag_id = random.randint(0, 1000)

    tag_name = fake.sentence(nb_words=5)
    category_name = fake.sentence(nb_words=5)

    fake.add_provider(pet_status_provider)
    pet_status = fake.pet_status()

    payload['photoUrls'][0] = photo_url
    payload['id'] = pet_id
    payload['category']['id'] = category_id
    payload['category']['name'] = category_name
    payload['tag'][0]['id'] = tag_id
    payload['tag'][0]['name'] = tag_name
    payload['status'] = pet_status

    yield payload
