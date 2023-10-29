import json
import unittest
from pprint import pprint

import requests

base_url = "https://7669-188-186-201-27.ngrok-free.app/api"


class BaseTest(unittest.TestCase):
    def test_get(self):
        res = requests.get(f'{base_url}/test/5')
        pprint(json.loads(res.content))

    def test_post(self):
        res = requests.post(f'{base_url}/signin',
                            json={
                                'login': 'hello',
                                'password': '12345'
                            })
        pprint(json.loads(res.content))
    def test_delete(self):
        res = requests.get(f'{base_url}/test/1')
        pprint(json.loads(res.content))

    def test_all_get(self):
        res = requests.get(f'{base_url}/tests')
        pprint(json.loads(res.content))


if __name__ == '__main__':
    unittest.main()
