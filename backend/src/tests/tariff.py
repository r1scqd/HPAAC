import unittest

import requests

base_url = "http://127.0.0.1:8080/api"


class BaseTest(unittest.TestCase):
    def test_get(self):
        res = requests.get(f'{base_url}/tariff/5')
        print(res.content)

    def test_post(self):
        res = requests.post(f'{base_url}/tariff',
                            json={
                                'name': 'eqweqw',
                                'price': 20,
                                'description': 'tariffsadqweqw'
                            })
        print(res.content)

    def test_delete(self):
        res = requests.delete(f'{base_url}/tariff/4')
        print(res.status_code)
        print(res.content)

    def test_all_get(self):
        res = requests.get(f'{base_url}/tariffs')
        print(res.content)


if __name__ == '__main__':
    unittest.main()
