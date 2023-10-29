import json
import pprint
import unittest

import requests

base_url = "http://127.0.0.1:8080/api"


class BaseTest(unittest.TestCase):
    def test_get(self):
        res = requests.get(f'{base_url}/user/1')
        print(res.status_code)
        pprint.pprint(res.text)

    def test_post(self):
        res = requests.post(f'{base_url}/user',
                            json={
                                'first_name': 'sname',
                                'last_name': 'somefam',
                                'middle_name': 'olas',
                                'organization_id': 1,
                                'status': 'work',
                                'job_title': 'krytoi',
                                'role': 'worker',
                                'login': 'alepa',
                                'password': 'qq',
                            })
        print(res.status_code)
        print(res.content)

    def test_delete(self):
        res = requests.get(f'{base_url}/user/2')
        print(res.status_code)
        print(res.content)

    def test_all_get(self):
        res = requests.get(f'{base_url}/users')
        t = json.loads(res.content)
        pprint.pprint(t)


if __name__ == '__main__':
    unittest.main()
