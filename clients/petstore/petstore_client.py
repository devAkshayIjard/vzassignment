from json import dumps
from clients.petstore.base_client import BaseClient
from config import BASE_URI
from utils.request import APIRequest


class PetstoreClient(BaseClient):
    def __init__(self):
        super().__init__()

        self.base_url = BASE_URI
        self.request = APIRequest()

        def add_pet(self, body=None):
            payload = dumps(body)
            url = f'{self.base_url}/pet'
            response = self.request.post(url, payload, self.headers)
            return response

        def read_pet_by_statuses(self, status):
            params = {'status': status}
            url = f'{self.base_url}/pet/findByStatus'
            return self.request.get(url, params)

        def update_pet(self, body=None):
            url = f'{self.base_url}/pet'
            payload = dumps(body)
            response = self.request.put(self.base_url, payload, self.headers)
            return response
