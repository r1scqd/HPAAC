import json
import unittest
from pprint import pprint

import requests

base_url = "http://127.0.0.1:8080/api"


class BaseTest(unittest.TestCase):
    def test_get(self):
        res = requests.get(f'{base_url}/organization/2')
        print(res.content)
        pprint(json.loads(res.content))

    def test_post(self):
        res = requests.post(f'{base_url}/organization',
                            json={
                                'phone': 'krtest',
                                'email': 'example.com',
                                'ITN': 'krtest',
                                'name': 'example.com',
                                'address': 'krtest',
                                'tariff_id': 1,
                            })
        print(res.content)

    def test_delete(self):
        res = requests.delete(f'{base_url}/organization/3')
        pprint(json.loads(res.content))

    def test_all_get(self):
        res = requests.get(f'{base_url}/organizations')
        pprint(json.loads(res.content))


if __name__ == '__main__':
    unittest.main()
